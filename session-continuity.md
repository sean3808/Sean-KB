---
name: Session Continuity
description: 冷啟動入口 — 現況、第一個動作、必讀 pointer
type: project
---

**最後更新**：2026-09-30

## TL;DR — 現況一行

大局勢 GT001 已入庫、入庫經驗已寫回 PMBA 入庫說明／schema／SOP 並 commit（未 push）；Sean 會陸續交 GT002–GT004。

## 本次收工快照（2026-09-30）

- HEAD：`feat(docs)` 文件迭代 commit（`main`，領先 origin 2 個 commit，未 push）
- working tree：只剩 Sean 既有 7 檔未 commit（本輪未動）
- 本輪推進：GT001 → 14 卡＋`maps/總體金融與美元流動性-MOC.md`；Case A 真實素材驗收完成；`/closeout` Medium 完成，Sean 拍板純文件不跑 `/codex-review`；Sean 認可「講者要求錄音不外流 → 逐字稿不入 repo」

## 第一個動作

1. **Sean 交 GT002–GT004 素材時** → `/pmba-cycle` 照 `_system/prompts/pmba-compile.md`「一堂課的素材包」與「同一門課的後續週次」：沿用 `-gt-` 號段（下一張 G015）、同一張 MOC，先讀 G001–G014 的「待追問」。
2. **開 `feat/agent-surface` 分支**（Sean 已拍板）：拆 `/kb-atomize`、`/kb-loop` 改 `disable-model-invocation`；對 CLAUDE.md／AGENTS.md／三個 skill／`_system/prompts/` 跑 `/claude-api prompt-audit`＋`/mattpocock-skills:writing-for-agents`，產報告＋擬議 diff 交 Sean、不直接套（pmba-cycle 與 pmba-compile 已於本輪先迭代，以新版為基底）；README 加 skill 小表；`C:\sean personal file\1_學習與進修\Knowledge-Atomized` 歸檔（留講義 PDF＋README、其餘移 `_archive/`、移除 huashu-nuwa 連結與 `.agents/skills.json` 對應行、`bulletproof-notes-framework` 歸檔、不刪檔）。L 級 → 分段 `/closeout`。Notion MCP 恢復時另依 `docs/current-status.md` 回寫。

## 必讀 Pointer

- `CLAUDE.md` — 人機邊界、Additive Update／Rewrite 安全線、卡片規則
- `CONTEXT.md` — 術語（Selected Source、Exception、Source Note…）
- `_system/prompts/maintenance-learning-loop.md` — 入庫流程正典
- `_system/prompts/pmba-compile.md` — PMBA 一堂課素材包與後續週次慣例
- `docs/current-status.md` — 穩態快照與 pending externals（含 Notion 回寫）
- `gh issue view 18` — PMBA v2 完整改寫（`/pmba-cycle` 去留在此決定）

## 暫態注意事項

- `C:\Sean_KB-pr19` 是 PR 工作目錄移除後殘留的空資料夾（被視窗占用），Sean 關掉相關視窗後手動刪。 `owner: expire`
- git 報 `.md` modified 但 diff 空＝Obsidian CRLF 幻影，忽略或順手正規化。 `owner: move`
- 大局勢逐字稿與 PLAUD 原檔的穩定位置是課程資料夾 `115-1_大局勢\`（Downloads 那份可刪）；逐字稿不入 repo。 `owner: expire`

## 未決事項

- 蒜頭投影 prompt（7/3 帶入：主控台複習窗＋「下次複習日＝下堂−3」）在 v2 下已不適用，Notion 端是否要改由 #18 一併處理。
- Joan 4 場課 PDF 萃取：Sean 交付才算 Selected Source，目前未交付。
