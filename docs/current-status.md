---
name: Current Status
description: Sean-KB 穩態快照 — 現在是什麼（非事件日誌）
owner: session-park
---

- 入庫模式：AI-first（Sean 選來源、AI 整合；Additive Update 直接 commit、Rewrite 先給 Sean 看 diff）→ `CLAUDE.md` > Human / AI Boundary、Safety
- 流程正典：`_system/prompts/maintenance-learning-loop.md`；術語：`CONTEXT.md`
- 決策 SSOT：Notion「耐久決策入口」；本地副本 `notion-pages/耐久決策入口.md` 含 2026/09/29 決策，**遠端未回寫**（pending external：Notion MCP 恢復）→ `notion-pages/README.md`
- ChatGPT Project Instructions：v2 防彈學習版，repo 與 ChatGPT 端一致（2026-09-30 Sean 已重貼）→ `pmba/chatgpt_project_systemprompt.md`
- PMBA 執行層：2026-08-28 v2（Bronze／Silver／Gold）；runbook 只做最小對齊，完整改寫 pending → `gh issue view 18`
- 驗證基線：17 tests OK（2026-09-30 量測）；lint 476 份文件 0 hard errors（2026-10-05）（430 legacy 缺 ingestion_version，逐次遷移）→ `_system/validation/ai-first-ingestion.md`
- 端到端真實素材驗收：Case A 已用大局勢 GT001 驗過；Case B–D 尚無真實素材 → `_system/validation/ai-first-ingestion.md` > 2026-09-30 首次真實素材驗收
- PMBA 大局勢：W01–W04 已入庫，共 41 張卡（G001–G041）；W02–W04 只有簡報與課堂 AI 摘要、沒有逐字稿，5 張卡因此標 `ai-inference`（G018、G022、G027、G028、G039）→ `maps/總體金融與美元流動性-MOC.md` > Open Questions
- PMBA Source 檔名：`<學期>_<課名>_W<週次>_<上課日>_<主題>.md`（2026-10-05 Sean 改定）→ `_system/prompts/pmba-compile.md` > 一堂課的素材包
- 教訓 ledger：3 筆 pending → `.claude/promote-candidates.md`
