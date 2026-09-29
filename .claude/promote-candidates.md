---
name: Promote Candidates
description: 本專案累積的待 promote 教訓 backlog，由 session-park 寫入、/promote-lesson drain
type: feedback
---

## PC-001
- status: pending
- origin: local-new
- hit_count: 1
- last_hit: 2026-09-29
- target_hint: harness_rule
- domain: —
- source_project: Sean-KB
- date: 2026-09-29
- canonical: self
- draft: |
    **在 SSOT 的本地副本上改寫前，先拉正典最新版當基底**：本地 mirror（Notion 頁下載檔、設定快照、文件副本）常落後正典。
    PR #19 的執行 agent 以 repo 內 2026-06-26 的 Notion 決策頁副本為準改寫，漏看遠端之後的 3 筆決策（其中一筆正是它要推翻的），
    結果既沒交代被取代的決策，還就地改寫了歷史原文。處置：動手前重拉（`ntn pages get <id>`），決策只追加、被取代原文保留並標註。
    訊號：本地副本的 last-edited 早於最近一次相關討論，或改動涉及「推翻既有決策」。 `[Sean-KB 2026-09]`

## PC-002
- status: pending
- origin: local-new
- hit_count: 1
- last_hit: 2026-09-29
- target_hint: domain_pack
- domain: git
- source_project: Sean-KB
- date: 2026-09-29
- canonical: self
- draft: |
    **殘留的 `.git/*.lock` 會讓 commit 靜默卡住好幾個月**：`index.lock` 與 `refs/heads/<branch>.lock` 可能同時殘留（Sean-KB 兩個都停在 2026-07-19，
    之後 Sean 一直沒成功 commit）。`git status` 照常可讀，只有寫入才報 `Unable to create ... .lock: File exists`。
    處置：確認 lock 是 0 byte、時間久遠、沒有 git 行程在跑（`tasklist | grep git`），再刪；刪一個後重試若報另一個 lock，用 `find .git -name "*.lock"` 一次找齊；刪完跑 `git fsck --no-dangling`。 `[Sean-KB 2026-09]`
