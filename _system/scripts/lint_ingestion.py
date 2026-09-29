#!/usr/bin/env python3
"""Read-only Sean-KB integrity checks; PyYAML is shared with the OKF exporter.

This checks structure, not source truth, semantic atomicity or human authorization.
Legacy notes stay first-class: missing v1 ingestion metadata is only a warning.
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

STATES = ('selected', 'ingested', 'indexed', 'atomicized', 'integrated')
LINK = re.compile(r'\[\[([^\]\n]+)\]\]')


def frontmatter(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        raise ValueError('missing YAML frontmatter')
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError('frontmatter must be a mapping')
    return data


def link_target(value):
    match = LINK.fullmatch(value) if isinstance(value, str) else None
    return match.group(1).split('|', 1)[0].split('#', 1)[0].removesuffix('.md') if match else None


def lint(vault):
    errors, warnings = [], []
    docs, by_stem, ids = {}, defaultdict(list), {}
    for folder in ('notes', 'sources', 'maps', 'wiki'):
        for path in sorted((vault / folder).rglob('*.md')):
            rel = path.relative_to(vault).as_posix()
            text = path.read_text(encoding='utf-8-sig')
            try:
                data = frontmatter(text)
            except (ValueError, yaml.YAMLError) as exc:
                errors.append(f'{rel}: {exc}')
                continue
            docs[rel] = (data, text)
            by_stem[path.stem].append(rel)
            for field in ('type', 'title', 'description', 'timestamp'):
                if not data.get(field):
                    errors.append(f'{rel}: missing {field}')
            identity = data.get('id')
            if identity:
                if identity in ids:
                    errors.append(f'{rel}: duplicate id {identity} ({ids[identity]})')
                ids[identity] = rel

    def resolve(value):
        target = link_target(value)
        if not target:
            return None
        if '/' in target:
            path = f'{target}.md'
            return path if path in docs else None
        matches = by_stem.get(target, [])
        return matches[0] if len(matches) == 1 else None

    def locator(entry, label):
        if not any(entry.get(k) for k in ('section', 'page_range', 'evidence_pointer')):
            errors.append(f'{label}: missing locator')
        if 'page_range' in entry:
            pages = entry['page_range']
            if not (isinstance(pages, list) and len(pages) == 2
                    and all(type(p) is int and p > 0 for p in pages) and pages[0] <= pages[1]):
                errors.append(f'{label}: invalid page_range (expected [start, end], 1-based inclusive)')

    legacy = 0
    for rel, (data, text) in docs.items():
        # Body + metadata file targets, including legacy source_ref. Do not invent missing links.
        for target in sorted(set(LINK.findall(text))):
            if not resolve(f'[[{target}]]'):
                errors.append(f'{rel}: unresolved/ambiguous wikilink [[{target}]]')
        if 'ingestion_version' not in data:
            legacy += 1
            continue
        if type(data['ingestion_version']) is not int or data['ingestion_version'] != 1:
            errors.append(f'{rel}: unsupported ingestion_version')
            continue
        for field in ('id', 'generated_by'):
            if not data.get(field):
                errors.append(f'{rel}: missing {field}')
        if data.get('generated_by') not in ('ai', 'sean', 'mixed'):
            errors.append(f'{rel}: invalid generated_by')
        if data.get('type') == 'Source':
            if not rel.startswith('sources/'):
                errors.append(f'{rel}: ingestion Source must live in sources/')
            for field in ('resource', 'selection_evidence'):
                if not isinstance(data.get(field), str) or not data[field].strip():
                    errors.append(f'{rel}: missing {field}')
            if data.get('selected_by') != 'sean' or data.get('selection_basis') not in ('sean-provided', 'sean-requested'):
                errors.append(f'{rel}: missing Sean Source Selection')
            state = data.get('source_status')
            if state not in STATES:
                errors.append(f'{rel}: invalid source_status')
                continue
            if STATES.index(state) >= 1:
                if not data.get('source_version'):
                    errors.append(f'{rel}: missing source_version')
                quality = data.get('document_quality')
                if not isinstance(quality, dict):
                    errors.append(f'{rel}: missing document_quality')
                else:
                    for field in ('text', 'structure', 'tables'):
                        allowed = ('good', 'partial', 'poor', 'unknown') + (('none',) if field == 'tables' else ())
                        if quality.get(field) not in allowed:
                            errors.append(f'{rel}: invalid document_quality.{field}')
                    if type(quality.get('ocr')) is not bool:
                        errors.append(f'{rel}: document_quality.ocr must be boolean')
            if STATES.index(state) >= 2:
                if data.get('parsing_strategy') not in ('tree', 'structure-text', 'repair'):
                    errors.append(f'{rel}: invalid parsing_strategy')
                tree = data.get('source_tree')
                if not isinstance(tree, list) or not tree:
                    errors.append(f'{rel}: indexed source requires non-empty source_tree')
                    continue
                parents = {}
                for node in tree:
                    if not isinstance(node, dict) or not isinstance(node.get('node_id'), str) or not node['node_id']:
                        errors.append(f'{rel}: node requires string node_id')
                        continue
                    nid = node['node_id']
                    if nid in parents:
                        errors.append(f'{rel}: duplicate node_id {nid}')
                    parent = node.get('parent_id')
                    if parent is not None and not isinstance(parent, str):
                        errors.append(f'{rel}: invalid parent_id for {nid}')
                        parent = None
                    parents[nid] = parent
                    for field in ('parent_id', 'heading', 'summary'):
                        if field not in node or (field != 'parent_id' and not node[field]):
                            errors.append(f'{rel}: node {nid} missing {field}')
                    locator(node, f'{rel}: node {nid}')
                for nid, parent in parents.items():
                    if parent is not None and parent not in parents:
                        errors.append(f'{rel}: missing parent {parent}')
                    seen, current = set(), nid
                    while current is not None and current in parents:
                        if current in seen:
                            errors.append(f'{rel}: source_tree cycle at {nid}')
                            break
                        seen.add(current)
                        current = parents[current]
            continue
        if data.get('type') == 'Map':
            continue  # Navigation references cards; it does not duplicate their evidence.
        origin = data.get('claim_origin')
        if origin not in ('source', 'ai-inference', 'sean'):
            errors.append(f'{rel}: invalid claim_origin')
        if origin == 'sean' and not data.get('stance_evidence'):
            errors.append(f'{rel}: Sean stance requires stance_evidence')
        refs = data.get('source_ref')
        evidence = data.get('source_evidence')
        if not isinstance(refs, list) or not refs:
            errors.append(f'{rel}: missing source_ref')
            refs = []
        resolved_refs = set()
        for ref in refs:
            path = resolve(ref)
            if not path or not path.startswith('sources/') or docs[path][0].get('type') != 'Source':
                errors.append(f'{rel}: source_ref must resolve to Source in sources/: {ref}')
            else:
                resolved_refs.add(path)
        if not isinstance(evidence, list) or not evidence:
            errors.append(f'{rel}: missing source_evidence')
            evidence = []
        covered = set()
        for entry in evidence:
            if not isinstance(entry, dict):
                errors.append(f'{rel}: evidence must be a mapping')
                continue
            path = resolve(entry.get('source'))
            if path not in resolved_refs:
                errors.append(f'{rel}: evidence source not in source_ref')
            else:
                covered.add(path)
                source = docs[path][0]
                tree = source.get('source_tree') or []
                nodes = {n.get('node_id') for n in tree if isinstance(n, dict)} if isinstance(tree, list) else set()
                if nodes and entry.get('node_id') not in nodes:
                    errors.append(f'{rel}: evidence node_id not in source tree')
                if not source.get('resource'):
                    errors.append(f'{rel}: provenance Source missing resource')
            if not entry.get('source_version'):
                errors.append(f'{rel}: evidence missing source_version')
            locator(entry, f'{rel}: evidence')
        if resolved_refs - covered:
            errors.append(f'{rel}: source_ref missing matching evidence')
    if legacy:
        warnings.append(f'{legacy} legacy documents lack ingestion_version; retain as formal knowledge, migrate on touch (no manual review queue).')
    return {'checked': len(docs), 'hard_errors': errors, 'warnings': warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--vault', type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    result = lint(args.vault.resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['hard_errors']))


if __name__ == '__main__':
    main()
