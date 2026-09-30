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
- 驗證基線：17 tests OK；lint 446 份文件 0 hard errors（430 legacy 缺 ingestion_version，逐次遷移）→ `_system/validation/ai-first-ingestion.md`
- 端到端真實素材驗收：Case A 型首跑完成——大局勢 GT001（簡報＋逐字稿＋PLAUD → 14 卡＋新 MOC，integrated）→ `sources/pmba/大局勢-GT001-導論.md`；Case B–D 尚無真實素材
- PMBA 大局勢：GT001 已入庫；GT002–GT004 簡報在課程資料夾，待 Sean 指定 → `maps/總體金融與美元流動性-MOC.md`
- 教訓 ledger：2 筆 pending → `.claude/promote-candidates.md`
