"""Synthetic contract regressions, not a claim of end-to-end LLM extraction."""
import copy
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

import okf_export_concepts as exporter
from export_anki import extract_qa_pairs
from lint_ingestion import lint


class IngestionContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.vault = Path(self.tmp.name)
        self.source = {
            'type': 'Source', 'title': 'Selected textbook', 'description': 'Synthetic fixture',
            'timestamp': '2026-09-29T18:53:23+08:00', 'id': 'src-test', 'resource': 'local:fixture.pdf',
            'ingestion_version': 1, 'generated_by': 'ai', 'source_status': 'integrated', 'selected_by': 'sean',
            'selection_basis': 'sean-provided', 'selection_evidence': 'Fixture: Sean asked to ingest this textbook.',
            'source_version': 'fixture-v1', 'document_quality': {'text': 'good', 'structure': 'good', 'tables': 'none', 'ocr': False},
            'parsing_strategy': 'tree', 'source_tree': [{'node_id': 'ch-1', 'parent_id': None, 'heading': 'Chapter 1',
                'section': 'Chapter 1', 'page_range': [1, 120], 'summary': 'Synthetic chapter coverage.'}]}
        self.note = {
            'type': 'Concept', 'title': 'Reusable claim', 'description': 'One independent claim.',
            'timestamp': '2026-09-29T18:53:23+08:00', 'id': 'note-test', 'ingestion_version': 1,
            'generated_by': 'ai', 'claim_origin': 'source', 'reviewed': False,
            'source_ref': ['[[sources/textbook]]'], 'source_evidence': [{'source': '[[sources/textbook]]',
                'source_version': 'fixture-v1', 'node_id': 'ch-1', 'section': 'Chapter 1', 'page_range': [2, 3],
                'evidence_pointer': 'local:fixture.pdf#page=2'}]}

    def write(self, path, data, body=''):
        target = self.vault / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text('---\n' + yaml.safe_dump(data, allow_unicode=True) + '---\n' + body, encoding='utf-8')
        return target

    def errors(self):
        self.write('sources/textbook.md', self.source)
        self.write('notes/concepts/test.md', self.note)
        return lint(self.vault)['hard_errors']

    def test_case_a_selected_textbook_needs_no_personal_learning_or_review(self):
        self.assertEqual(self.errors(), [])

    def test_case_b_selected_article_has_heading_locator_without_pages(self):
        self.source.update(selection_basis='sean-requested', resource='https://example.org/article',
                           parsing_strategy='structure-text')
        self.source['source_tree'][0].pop('page_range')
        self.note['source_evidence'][0].pop('page_range')
        self.assertEqual(self.errors(), [])

    def test_case_c_ai_research_cannot_be_marked_selected(self):
        self.source.update(selected_by='ai', selection_basis='web-research', selection_evidence='')
        errors = self.errors()
        self.assertTrue(any('Source Selection' in e for e in errors))
        self.assertTrue(any('selection_evidence' in e for e in errors))

    def test_case_d_personal_stance_needs_explicit_evidence(self):
        self.note.update(type='Principle', claim_origin='sean')
        self.assertTrue(any('stance_evidence' in e for e in self.errors()))
        self.note['stance_evidence'] = 'Fixture: Sean explicitly stated this principle.'
        self.assertEqual(self.errors(), [])

    def test_every_source_has_matching_evidence(self):
        other = copy.deepcopy(self.source)
        other['id'] = 'second-source'
        self.write('sources/second.md', other)
        self.note['source_ref'].append('[[sources/second]]')
        self.assertTrue(any('missing matching evidence' in e for e in self.errors()))

    def test_tree_cycles_and_unknown_evidence_nodes_fail(self):
        self.source['source_tree'][0]['parent_id'] = 'ch-1'
        self.note['source_evidence'][0]['node_id'] = 'missing'
        errors = self.errors()
        self.assertTrue(any('cycle' in e for e in errors))
        self.assertTrue(any('node_id not in' in e for e in errors))

    def test_invalid_pages_and_dangling_source_fail(self):
        self.note['source_ref'] = ['[[sources/missing]]']
        self.note['source_evidence'][0]['page_range'] = [3, 2]
        errors = self.errors()
        self.assertTrue(any('source_ref must resolve' in e for e in errors))
        self.assertTrue(any('invalid page_range' in e for e in errors))

    def test_selected_source_does_not_claim_indexed_quality(self):
        self.source.update(source_status='selected')
        for key in ('source_version', 'document_quality', 'parsing_strategy', 'source_tree'):
            self.source.pop(key)
        self.write('sources/textbook.md', self.source)
        self.assertEqual(lint(self.vault)['hard_errors'], [])
        self.source['source_status'] = 'indexed'
        self.write('sources/textbook.md', self.source)
        errors = lint(self.vault)['hard_errors']
        self.assertTrue(any('source_tree' in e for e in errors))
        self.assertTrue(any('document_quality' in e for e in errors))

    def test_legacy_reviewed_false_remains_formal(self):
        self.write('notes/concepts/legacy.md', {k: self.note[k] for k in
                   ('type', 'title', 'description', 'timestamp', 'id', 'reviewed')})
        result = lint(self.vault)
        self.assertEqual(result['hard_errors'], [])
        self.assertEqual(len(result['warnings']), 1)

    def test_raw_source_text_is_link_target_but_not_a_source(self):
        raw = self.vault / 'sources/transcript.md'
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text('逐字稿原文，無 frontmatter。\n', encoding='utf-8')
        self.source['source_tree'][0]['evidence_pointer'] = '[[transcript]]'
        self.assertEqual(self.errors(), [])
        self.write('notes/concepts/linker.md', {k: self.note[k] for k in
                   ('type', 'title', 'description', 'timestamp')} | {'id': 'linker'}, body='見 [[transcript]]\n')
        self.assertEqual(lint(self.vault)['hard_errors'], [])
        self.note['source_ref'] = ['[[sources/transcript]]']
        self.assertTrue(any('source_ref must resolve' in e for e in self.errors()))
        (self.vault / 'notes/concepts/bare.md').write_text('no frontmatter\n', encoding='utf-8')
        self.assertTrue(any('bare.md: missing YAML frontmatter' in e for e in lint(self.vault)['hard_errors']))

    def test_duplicate_id_detected(self):
        self.write('notes/concepts/duplicate.md', self.note)
        self.assertTrue(any('duplicate id' in e for e in self.errors()))

    def test_export_retains_unknown_fields_and_evidence_fragment(self):
        self.note['extra_future_field'] = {'nested': ['preserve-me']}
        self.note['source_evidence'][0]['evidence_pointer'] = '[[sources/textbook#Section 1|display alias]]'
        src = self.write('notes/concepts/test.md', self.note)
        dst = self.vault / 'export.md'
        exporter.export_one(src, dst, {'test'})
        actual, _ = exporter.parse_frontmatter(dst.read_text())
        self.assertEqual(actual['source_evidence'][0]['evidence_pointer'], 'sources/textbook#Section 1')
        self.assertEqual(actual['source_evidence'][0]['page_range'], [2, 3])
        self.assertEqual(actual['extra_future_field'], self.note['extra_future_field'])
        self.assertFalse(actual['reviewed'])

    def test_export_body_link_keeps_anchor(self):
        src = self.write('notes/concepts/test.md', self.note,
                         body='見 [[other#Section 2|相關段落]] 與 [[other]]\n')
        dst = self.vault / 'export.md'
        exporter.export_one(src, dst, {'test', 'other'})
        body = dst.read_text(encoding='utf-8')
        self.assertIn('[相關段落](./other.md#Section%202)', body)
        self.assertIn('[other](./other.md)', body)

    def test_non_string_id_is_reported_not_crash(self):
        for bad in (['a', 'b'], True, 7):
            self.note['id'] = bad
            self.assertTrue(any('invalid id' in e for e in self.errors()), bad)

    def test_source_note_template_with_comments_left_in_passes_lint(self):
        template = (Path(__file__).resolve().parents[2] / 'templates/source-note.md').read_text(encoding='utf-8')
        data = yaml.safe_load(template.split('---\n', 2)[1])
        data.update(title='Filled', description='Filled from template.', timestamp='2026-09-30T09:00:00+08:00',
                    id='src-from-template', resource='local:fixture.pdf',
                    selection_evidence='Fixture: Sean handed this over.')
        self.write('sources/from-template.md', data, body=template.split('---\n', 2)[2])
        self.assertEqual(lint(self.vault)['hard_errors'], [])

    def test_non_string_node_ids_are_reported_not_crash(self):
        self.source['source_tree'][0]['node_id'] = ['ch-1']
        self.note['source_evidence'][0]['node_id'] = ['ch-1']
        errors = self.errors()
        self.assertTrue(any('string node_id' in e for e in errors))
        self.assertTrue(any('evidence node_id must be a string' in e for e in errors))

    def test_anki_standard_answer_is_independent_of_learning_gate(self):
        self.assertEqual(extract_qa_pairs('## Retrieval 題卡\nQ: Why?\nA: Sourced answer.\n'),
                         [('Why?', 'Sourced answer.')])


if __name__ == '__main__':
    unittest.main()
