---
name: Session Continuity
description: 冷啟動入口 — 現況、第一個動作、必讀 pointer
type: project
---
最後更新：2026-06-26（建好「維護＝學習」全鏈；下一步＝用 /kb-loop 續跑〈父母篇〉診斷場）

> 本檔刻意進 git（Sean 2026-06-26 覆寫 session-park「gitignore」預設）。首次需 Sean commit。

## TL;DR — 現況一行

Sean-KB 這輪建好「**維護＝學習**」四層全鏈（方法論層 Notion 學習科學頁 → 流程層 SOP → 執行層 `/kb-loop` skill → 工具層 Readwise CLI），並跑了第一次真實診斷場（學習法篇 + 父母篇）；**下一步＝用 `/kb-loop` 續跑〈AI 把解釋變便宜後父母該拿回什麼〉**，把剩下幾條 thread 戳完。

## 本次收工快照（2026-06-26）

- HEAD：`7d18a58`（feat(skill): kb-loop 加診斷場觸發判準），已 push，origin 同步
- 推進範圍：`5293594` → `7d18a58`（約 7 commits：notion-pages 本地鏡像／維護=學習 SOP+研究報告／kb-loop skill／兩層連結護欄／觸發判準／readwise plugin 註冊）
- working tree：clean（但 Obsidian 開著常把卡片重存成 CRLF → 顯示假 modified，純 EOL 幻影）
- 完整 log 自己跑：`git log --oneline -10`

## 第一個動作（依情境分支）

- **情境 A（預設：續跑父母篇診斷場）** → `/kb-loop`。材料＝Reader doc `01kvye9szayhpbx52jay7vw989`（〈AI 把解釋變便宜後父母該拿回什麼〉，`readwise reader-get-document-details --document-id <id>` 取全文）。**生成效應鐵律：Sean 先答，不先摘要**。已跑完的 thread：「習得感 ∝ 基礎」已沉澱成觸發判準。**未戳的 thread**：診斷導向、輸出提前逼漏洞、問問題>分數、階段性下注、設計環境。觸發判準：基礎穩→快答別硬跑診斷場。
- **情境 B（處理其他 Reader 材料/主題）** → `/kb-loop`，從 Reader Library 撈（`readwise reader-search-documents --query ...`）。
- **情境 C（改 vault 結構/卡片維護）** → 照 SOP `_system/prompts/maintenance-learning-loop.md`；改既有卡前先出 git diff（Safety）。

## 必讀 Pointer

agent-neutral（相對專案根）：
- `./CLAUDE.md` — vault 結構/命名/note 規則正典 + Obsidian/Readwise 工具指引
- `./_system/prompts/maintenance-learning-loop.md` — **維護＝學習迴圈 SOP（流程層 SSOT）**：鐵律/護欄/診斷場/兩層連結/觸發判準
- `./.claude/skills/kb-loop/SKILL.md` — `/kb-loop` 執行層（薄層，指向 SOP）
- `./notion-pages/README.md` — Notion 正典頁本地副本清單 + ntn 下載/MCP 回寫工作流
- `./_system/research/2026-06-26-llm-wiki-maintenance-research.md` — 本輪研究蒐證（claude-obsidian/zettelkasten.de）
- `git log --oneline -10` — 本輪完整推進

Claude Code auto-memory（絕對路徑；非 Claude agent 可略）：
- `C:\Users\USER\.claude\projects\D--Sean-KB\memory\MEMORY.md` — 專案 index
- `...\memory\sean-kb-sources.md` — 3 個 Notion 正典頁 id（耐久決策入口/v1.2 報告/學習科學方法論）
- `...\memory\promote-candidates.md` — 曾碰過的坑（PC-001 背景腳本、PC-002 Notion UUID dash）

## 暫態注意事項（≤3）

- Obsidian 重存卡片成 CRLF → 假 modified（純 EOL 幻影），要清就 `git add --renormalize <檔>` [owner: expire]
- Readwise CLI 已登入 + `readonly=true` 已設；issue #4 read 能力（list/search/get markdown）已驗收 [owner: expire]
- session-continuity.md 首次進 git，待 Sean commit [owner: expire]

## 關鍵 recipe

Readwise 讀取（read-only；完整指令見 `readwise:readwise-cli` skill）：
```bash
readwise reader-list-documents --location new --limit 10 --response-fields title,author,category,saved_at
readwise reader-search-documents --query "<主題>" --limit 5 --json   # 注意：search 不支援 --response-fields、不回 id
readwise reader-get-document-details --document-id <id>              # 取全文 markdown（content 欄）
```

## 未決事項

- **父母篇診斷場未跑完**（剩 5 條 thread，見情境 A）→ 下個 session 續，flag-Sean 決定戳哪條
- **CLAUDE.md「Workflows」段建議加 `/kb-loop` + SOP pointer**（目前只列 pmba-compile/okf-exporter/okf-lint）→ flag-Sean
- **方法論頁待辦 #2 的「Notion 課程流程側 SOP」未做**（Obsidian 側已落地）→ flag-Sean
- **session-continuity.md 進 git 後首次 commit**（Sean 決定時機/訊息）
