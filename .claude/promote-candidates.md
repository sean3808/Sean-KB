# Promote Candidates — Sean-KB

> 專案內踩過、可能值得升級到跨專案教訓的坑。由 `/promote-lesson` 定期清算。

## PC-2026-09-29-01：agent 在過期的 Notion 本地副本上改寫決策

- **Trigger**：修改 `notion-pages/` 下的 Notion 本地副本（尤其耐久決策入口）。
- **What happened**：PR #19 的執行 agent 以 repo 內 2026-06-26 的本地副本為準改寫決策頁，沒看到遠端之後新增的 3 筆決策（06/26 維護＝學習、06/27 GitHub Issue 候選審核區、07/06 前綴轉正），導致 PR 既沒交代被取代的決策，還就地改寫了歷史原文。Sean 在 review 時指出「可能是因為專案文件未更新導致當下 agent 誤判」。
- **Resolution**：動手前先 `ntn pages get <page-id>` 拉遠端最新版當基底；決策只往後追加，被取代的原文保留並標註。已寫入 `CLAUDE.md` 與 `notion-pages/README.md` 工作流第 1 步。
- **升級候選理由**：「本地副本／快照落後正典」不限 Notion，任何 SSOT 的本地 mirror 都適用。
- 來源：`[Sean-KB 2026-09]`
