---
name: Session Continuity
description: 冷啟動入口 — 現況、第一個動作、必讀 pointer
type: project
---

**最後更新**：2026-10-05

## TL;DR — 現況一行

大局勢 W01–W04 全部入庫（41 張卡，G001–G041），W01 來源已改名為 `115-1_大局勢_W01_20260907_導論`；全部 commit 在 `main`、未 push。下一堂是 W05（利率走廊）。

## 2026-10-05 本輪推進

- 改名：`大局勢-GT001-導論` → `115-1_大局勢_W01_20260907_導論`，17 處引用同步；新命名慣例寫進 `_system/prompts/pmba-compile.md`
- W02（G015–G021）、W03（G022–G029）、W04（G030–G041）各一個 commit；來源是簡報＋課堂 AI 摘要（`…-Summary.md`），**沒有逐字稿**
- 簡報進度比上課慢一週：GT002 後半在 W03 講、GT003 後半在 W04 講，各週 Source 的「來源與範圍」有寫
- 5 張卡標 `ai-inference`（G018、G022、G027、G028、G039）：核心主張只在 AI 摘要裡；Sean 若補逐字稿可升級
- W03 的 Summary 檔有缺損（知識點索引第二到四節不見，原檔第 188 行）
- Anki 已重匯（`_system/exports/anki-cards.txt`，大局勢 41 題）；`/closeout` 見本輪回報

## 本次收工快照（2026-09-30）

- HEAD：`feat(docs)` 文件迭代 commit（`main`，領先 origin 2 個 commit，未 push）
- working tree：只剩 Sean 既有 7 檔未 commit（本輪未動）
- 本輪推進：GT001 → 14 卡＋`maps/總體金融與美元流動性-MOC.md`；Case A 真實素材驗收完成；`/closeout` Medium 完成，Sean 拍板純文件不跑 `/codex-review`；Sean 認可「講者要求錄音不外流 → 逐字稿不入 repo」

## 第一個動作

1. **Sean 交 W05 之後的素材時** → `/pmba-cycle` 照 `_system/prompts/pmba-compile.md`「一堂課的素材包」（含「只有簡報與 AI 摘要」與「簡報頁與週次錯開」兩條）：沿用 `-gt-` 號段（下一張 G042）、同一張 MOC，先讀 MOC 的 Open Questions 與各卡「待追問」；W05 講利率走廊時回頭補 G040。
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
- `sources/pmba/財務管理B 2026-06-28 上／下.md` 與 `_inbox/fable-five-year-letter-2026-07-07.md` 是 Sean 的未追蹤檔，本輪未動、未指定納入。 `owner: expire`

## 未決事項

- 蒜頭投影 prompt（7/3 帶入：主控台複習窗＋「下次複習日＝下堂−3」）在 v2 下已不適用，Notion 端是否要改由 #18 一併處理。
- Joan 4 場課 PDF 萃取：Sean 交付才算 Selected Source，目前未交付。
