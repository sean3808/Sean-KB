---
name: Session Continuity
description: 冷啟動入口 — 現況、第一個動作、必讀 pointer
type: project
---

**最後更新**：2026-09-30

## TL;DR — 現況一行

PR #19（AI-first ingestion）已 merge 進 main；下一步是開「agent 介面整理」分支（內容 Sean 已拍板，見第一個動作 1）。

## 本次收工快照（2026-09-30）

- HEAD 與 origin/main 同步（`main`）
- working tree：Sean 既有未 commit 檔（問題解決 MOC、防彈 A007、兩份 sources）＋未追蹤（`_inbox/fable-five-year-letter…`、`sources/pmba/財務管理B 2026-06-28 上／下.md`）本輪未動
- 本輪推進：grill PR #19（31 題）→ 語意修正＋卡片盒補充＋lint／OKF 匯出修正，併入 Sean 7 月本機 commit，`--no-ff` merge（`245497f`），main 上 17 tests OK／lint 0 hard error
- 決策紀錄：`notion-pages/耐久決策入口.md` 決策紀錄 2026/09/29 條（遠端待回寫）

## 第一個動作

1. **開 `feat/agent-surface` 分支**（Sean 已拍板）：拆出 `/kb-atomize`（入庫，model-invoked）、`/kb-loop` 改 `disable-model-invocation`（只管個人學習）；對 CLAUDE.md／AGENTS.md／三個 skill／`_system/prompts/` 跑 `/claude-api prompt-audit`＋`/mattpocock-skills:writing-for-agents`，**產報告＋擬議 diff 交 Sean，不直接套**；README 加專案 skill 小表；`C:\sean personal file\1_學習與進修\Knowledge-Atomized` 歸檔（留講義 PDF＋README「已併入 Sean-KB」、其餘移 `_archive/`、移除 huashu-nuwa 連結與 `.agents/skills.json` 對應行、`bulletproof-notes-framework` skill 直接歸檔、不刪任何檔）。L 級 → 分段 `/closeout`。
2. **Sean 提供真實素材時** → 端到端驗收：`/kb-loop` 入庫（候選 `sources/pmba/財務管理B 2026-06-28 上／下.md`），結果補進 `_system/validation/ai-first-ingestion.md`。
3. **Notion MCP 恢復時** → 先 `ntn pages get` 重拉比對，再外科手術回寫 `notion-pages/耐久決策入口.md`（頁尾 2026/09/29 決策＋各節「已取代」標註＋§4「用自己的話寫」同步）與 `notion-pages/學習科學方法論.md`。

## 必讀 Pointer

- `CLAUDE.md` — 人機邊界、Additive Update／Rewrite 安全線、卡片規則
- `CONTEXT.md` — 術語（Selected Source、Exception、Source Note…）
- `_system/prompts/maintenance-learning-loop.md` — 入庫流程正典
- `docs/current-status.md` — 穩態快照與 pending externals
- `notion-pages/README.md` — Notion 本地副本同步規則（動手前先重拉）
- `gh issue view 18` — PMBA v2 完整改寫（agent 介面整理之後的下一支 PR；`/pmba-cycle` 去留在此決定）

## 暫態注意事項

- `C:\Sean_KB-pr19` 是 PR 工作目錄移除後殘留的空資料夾（被視窗占用），Sean 關掉相關視窗後手動刪。 `owner: expire`
- git 報 `.md` modified 但 diff 空＝Obsidian CRLF 幻影，忽略或順手正規化。 `owner: move`

## 未決事項

- 蒜頭投影 prompt（7/3 帶入：主控台複習窗＋「下次複習日＝下堂−3」）在 v2 下已不適用，Notion 端是否要改由 #18 一併處理。
- Joan 4 場課 PDF 萃取：Sean 交付才算 Selected Source，目前未交付。
