---
name: Session Continuity
description: 冷啟動入口 — 現況、第一個動作、必讀 pointer
type: project
---
最後更新：2026-06-30（Notion AI 三頁本輪迭代落地一批，operator 定位完成；下一步＝ISSUE-05/06 或 Custom Agents 岔路）

> 本檔刻意進 git（Sean 2026-06-26 覆寫 session-park「gitignore」預設）。重寫後會顯示 modified，由 Sean 決定 commit 時機。

## TL;DR — 現況一行

用**防彈卡網知識**迭代 **Notion AI 三頁**（System Prompt「My Notion AI」＋ 防彈引擎/主控台 Skill）：抓本地副本 → 防彈視角診斷出 8 issue → 卡網對一手 Esor PDF 抽核（**忠實、零失真**）→ 落地 ISSUE-01/03/07/08 並 MCP 回寫 Notion → 能力邊界對齊官方改成 **operator**。**下一步＝挑 ISSUE-05（操作層 vs 方法論層）或 ISSUE-06（策展防彈模組）落地，或談 Custom Agents 架構岔路**。

## 本次收工快照（2026-06-30）

- HEAD：`dd8329d`（chore: 註冊 playground plugin），已 push，origin 同步、working tree clean
- 推進範圍：`b6e55a4` → `dd8329d`（本 session 5 commits，rebase 疊在遠端 PR #9 `1799454` 之上 — 兩邊檔案零重疊、無衝突）
- 本輪 Notion 已實際回寫：My Notion AI §2.1-7（operator）/§6（Memories→預設準則）、防彈引擎 Skill 心法2-3、主控台範例
- 完整 log 自己跑：`git log --oneline -10`

## 第一個動作（依情境分支）

- **情境 A（預設：續 Notion AI 迭代）** → 讀 `notion-pages/issues/INDEX.md` 看 8-issue 狀態，挑 **ISSUE-06**（策展防彈模組進 Skill，卡網已驗證可信，等 Sean 挑模組：建議異步協作 A054-057 ＞ 任務拆解三階段 A028-030 ＞ 系統四等級 A006）或 **ISSUE-05**（操作層 vs 方法論層邊界，討論題）。流程：改 `notion-pages/` 本地副本 → 出 HTML diff 給 Sean 審 → MCP `update_content` 回寫 Notion → commit。**回寫前先 `notion-fetch` 拿精確 old_str**（tab 縮排逐字符匹配）。
- **情境 B（Custom Agents 架構岔路）** → Sean 是 Business → Custom Agents 可用（自主、排程/事件觸發、能 update records/post/send）。談主控台自動開場、碎片自動升級是否從 System Prompt 指令改造成 Custom Agent。這是 ISSUE-05/06 背後的真正架構決定。官方：`https://www.notion.com/help/custom-agents`。
- **情境 C（續 gh #12 卡網驗證）** → 剩 47 張防彈卡逐張對一手 PDF（方法論 SOP 寫在 issue #12 本文）。**主 agent 親自核、不派 researcher**（反污染，見 VERIFICATION 檔）。
- **情境 D（舊 track：kb-loop 父母篇診斷場）** → `/kb-loop`，材料 Reader doc `01kvye9szayhpbx52jay7vw989`，剩 5 thread（診斷導向/輸出提前逼漏洞/問問題>分數/階段性下注/設計環境）。**生成效應鐵律：Sean 先答、不先摘要**。
- **情境 E（改 vault 卡片/結構）** → 改既有 promoted note 前先出 git diff（CLAUDE.md Safety）。

## 必讀 Pointer

agent-neutral（相對專案根）：
- `./CLAUDE.md` — vault 結構/命名/note 規則正典 + Obsidian/Readwise 工具指引 + Safety
- `./notion-pages/issues/INDEX.md` — **Notion AI 迭代 8-issue 追蹤**：狀態表、統一主軸（operator）、來源權威序（Esor 官方>vault 二手>Skill）
- `./notion-pages/issues/VERIFICATION-bulletproof-cards.md` — 卡網一手 PDF 抽核帳 + **反污染鐵則（「子彈」是 Esor 原生詞、≠ Bullet Journal）**
- `./notion-pages/README.md` — Notion 頁本地副本清單 + ntn 下載/MCP 回寫工作流
- gh issue #12（`gh issue view 12`）— 剩 47 張卡待驗證 checklist + 驗證方法論 SOP
- `./_system/prompts/maintenance-learning-loop.md` — 維護=學習迴圈 SOP（kb-loop track 用）
- `git log --oneline -10` — 本輪完整推進

Claude Code auto-memory（絕對路徑；非 Claude agent 可略）：
- `C:\Users\USER\.claude\projects\D--Sean-KB\memory\MEMORY.md` — 專案 index
- `...\memory\sean-kb-sources.md` — 6 個 Notion 正典/配置頁 id（含 My Notion AI System Prompt）
- `...\memory\promote-candidates.md` — 曾碰過的坑（PC-001~004；碰坑先翻這）

## 暫態注意事項（≤3）

- CJK 檔名 repo 用腳本吃 `git diff --name-only` 要加 `-c core.quotepath=false`，否則漏中文檔（已記 PC-004）[owner: expire]
- Obsidian 開著會把卡片重存成 CRLF → 假 modified 幻影；要清就 `git add --renormalize <檔>` [owner: expire]
- 本輪審核走「本地改 → Python stdlib `difflib.HtmlDiff` 出 HTML diff → SendUserFile 給 Sean → 放行才 MCP 回寫」；playground 互動版也可（diff-review 模板）[owner: expire]

## 未決事項

- **ISSUE-05 操作層 vs 方法論層邊界**（討論題，未動）→ flag-Sean
- **ISSUE-06 策展防彈模組**（卡網已驗證，等 Sean 挑哪些模組進 Skill）→ flag-Sean
- **Custom Agents 架構岔路**（主控台/碎片升級 → Custom Agent？Business 已解鎖）→ flag-Sean
- **gh #12：剩 47 張卡逐張對一手 PDF**（非阻塞，隨時續）
- **可選**：28 張已驗證卡 `reviewed:false→true`（改 promoted note，先出 git diff）→ flag-Sean
- **舊 track（kb-loop）**：父母篇診斷場剩 5 thread（情境 D）；方法論頁待辦 #2「Notion 課程流程側 SOP」未做 → flag-Sean
