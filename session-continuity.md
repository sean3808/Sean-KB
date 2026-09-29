---
name: Session Continuity
description: AI-first ingestion 重構 handoff；舊學習排程保留為歷史
type: project
---

> 🔴 **換機注意（2026-08-06 全專案通告）**
>
> 這台電腦已換機（ASUS VivoBook X513EQ → ASUS Vivobook 16 X1607CA），
> **資料根目錄從 `D:\` 搬到 `C:\`**：
>
> | | 舊機 | 新機 |
> |---|---|---|
> | 專案根 | `D:\IT_Projects\...` | **`C:\IT_Projects\...`** |
> | 資料碟 | D: 內接 Crucial MX500 | **不存在**（單碟，C: 就是系統碟） |
> | 備份碟 | `E:\backups` | **`D:\backups`**（USB 外接 SMR 機械碟，非工作碟） |
>
> **⚠️ 開工第一件事：先檢查換槽會不會對本專案造成負面影響。** 至少要查：
>
> - 程式碼 / 設定 / 腳本裡寫死的 `D:\` 或 `E:\` 絕對路徑
> - Task Scheduler 排程 XML、NSSM 服務、`.env`、CI 設定裡的路徑
> - **任何「非系統碟」的假設** —— 新機是單碟，所有東西都在系統碟上
> - 備份腳本的 source / destination
> - 文件裡引用的絕對路徑（README、交接文件、runbook）
>
> 已知實例（供比對症狀）：
> - `jean-wan-mail-platform` 的 `storage.py` 預設 DB 路徑仍寫死 `D:\IT_Projects\...`
> - 同專案測試套件因 runtime root 落在系統碟被自家守門擋下，101 個測試失敗
>
> 換機基準線與完整對照見 `C:\IT_Projects\my-pc-maintenance\CLAUDE.md`
> （「換機分界線」段）；舊機事實凍結在 git tag `old-pc-x513eq`。

最後更新：2026-09-29（PR #19 AI-first ingestion＋Sean review 修正；合併本機 main 的 7 月 commit）

## 現況與第一個動作

- 核心決策：Sean 提供素材給 Sean-KB 即完成 Source Selection；AI 自動處理、原子化、去重、provenance、earned links、MOC 與 lint。無逐卡／逐 link 人工批准或先消化 Gate。
- Knowledge ingestion 與 personal learning 分開；PMBA、Reader 共用 pipeline，學習／複習保留獨立流程。
- 接手先看 `git status --short --branch`、`README.md`、`CLAUDE.md`、`AGENTS.md`、`_system/prompts/maintenance-learning-loop.md`、`_system/schemas/okf-note-schema.md`。
- 新來源：`/kb-loop` 或 `/pmba-cycle` 直接 ingestion；只有查學習排程才讀 PMBA runbook 的相位程序。不要拿 7 月的日期當今日待辦。
- 術語見 `CONTEXT.md`（Selected Source、Additive Update／Rewrite、Exception、Source Note 等）。
- 驗證入口：`uv run --with pyyaml python _system/scripts/lint_ingestion.py`、`uv run --with pyyaml python -m unittest discover -s _system/tests`；Case A–D、review 修正與已知限制見 `_system/validation/ai-first-ingestion.md`。
- Notion 本地副本（耐久決策入口、學習科學方法論）已以遠端最新版為基底修訂，**待 Notion MCP 恢復後回寫**；ChatGPT Project Instructions 未重貼。

## 待辦（2026-09-29 grill session 定案，依序）

1. **分支「agent 介面整理」**（PR #19 merge 後）：拆出 `/kb-atomize`（入庫）、`/kb-loop` 改只手動觸發（學習）；`/claude-api prompt-audit`＋writing-for-agents 審查全部 agent 文件（產報告＋擬議 diff 給 Sean 審）；README 加專案 skill 小表；Knowledge-Atomized 資料夾歸檔（留講義 PDF＋README，其餘移 `_archive/`，移除 nuwa 連結，不刪檔；防彈筆記法顧問 skill 直接歸檔）。
2. **issue #18 PMBA v2 改寫**（另開 PR）：runbook、課後細節、ChatGPT prompt 同步；`/pmba-cycle` 去留在此決定。
3. **Notion 回寫**（等 MCP）：頁尾追加 2026/09/29 決策＋各節「已取代」標註，以 `notion-pages/` 本地副本為參照。
4. **真實素材端到端驗收**（等 Sean 提供素材；候選：`sources/pmba/財務管理B 2026-06-28 上／下.md`）。
- 既有 note ID／檔名／reviewed 值保留；新欄位逐次補齊。AI 不把歷史未驗證內容假標為已驗證。

## 歷史 handoff（2026-07-13；不是現行操作指令）

以下保留當時事實；其中 promote gate、等 Sean 授權逐卡或舊日期動作已由上方規則取代。遠端 issue 的當前狀態需另查，不推定仍 open。防彈原文反污染提醒仍可參考。

## TL;DR — 現況一行

本 session（7/12–13）完成**「Joan 思維模式」知識資產第一版**：爬 750 則 Joan FB 歷年公開貼文 → `sources/joan/`；蒸餾 **M00 脊椎＋21 張接地 pattern 卡** → `notes/concepts/Joan-*`；建 `joan-MOC` 並織進 `決策-MOC`。已分 2 commit（`a06793b` 素材層、`d69f45a` 卡＋導航），**未 push（ahead origin/main 2）**。**待 Sean：promote 判斷**——22 張卡全 `reviewed:false`，由 Sean review git diff 決定 promote／cull（尤其 4 張單源卡）。PMBA 循環為背景線，未在本 session 推進（下一站原訂 7/12 Day 2，待 Sean 確認狀態）。

## 本次收工快照（2026-07-13 · Joan KB build）

- HEAD：`d69f45a`，**ahead origin/main 2 未 push**（`a06793b` 素材層、`d69f45a` 卡＋導航）
- working tree：`session-continuity.md`（本檔）＋`sources/解決問題的領導力.md`（**CRLF 幻影，diff 空**）＋`_inbox/fable-five-year-letter-2026-07-07.md`（?? 舊有未處理，本 session 未動）
- 本 session 推進（全新 Joan 資產鏈）：
  - 爬取：Apify `cleansyntax/facebook-profile-posts-scraper`（免登入、個人 profile）抓 750 則（$4.5）→ `joan-fb-2025.md` 531＋`2026.md` 214，含日期＋permalink
  - 萃取：2 張 source card（舉一反十、六問＋治理，PDF 留外部只放路徑指標）
  - 原子層：`Joan-M00-那把尺`（Tier 0 脊椎）＋`Joan-P01~P21`（七域 pattern 卡，接地體例）
  - 導航：`Joan-王Joan` lit note＋`joan-MOC`（Tier 0＋七域）＋`決策-MOC` 新增 Joan 六問段；grep 確認零 dangling
- **卡片體例定案**（Sean 三輪 feedback 收斂）：棄去脈絡化細原子卡，改「場景（帶 permalink）→ 判斷 → 為什麼是 checkpoint → 帶理由連結」的 pattern 卡；教訓存 auto-memory `card-design-no-decontextualization.md`
- 候選池（未成卡）：`.subagent-output/joan-batch2/2025-candidates.md`、`2026-candidates.md`（含高價值深度文清單）

## 第一個動作（依情境分支）

- **情境 F（最新：Joan KB curator gate）** → 入口 `maps/joan-MOC.md` → 先讀脊椎 `Joan-M00-那把尺`，走一遍 21 張 pattern 卡。22 張全 `reviewed:false`，Sean review git diff 決定 promote（改 `reviewed:true`）／cull。**特別裁決**：4 張單源卡 `P08 替代成本`／`P10 客訴痛點`／`P11 B2B流程轉譯`／`P16 Discovery/Session`（單則貼文拆多子場景，判斷可否接受，或降級）。未成卡的高價值深度文在 `.subagent-output/joan-batch2/`。**2 commit 未 push，Sean 定 push 時機**。另 4 場課 PDF 未萃取（Sean 指示本輪只做舉一反十）。
- **情境 A（預設：續 PMBA 循環）** → 先跑 `/pmba-cycle` Step 0 判相位。已知：財務 Day 1 trace 完成 7/2、**7/9 複習日**（Sean 答兩批題卡＋費曼＋待查證＋拍板）→ 7/10–11 預習 → **7/12 Day 2** 新循環。先確認補漏掃描第二批題卡是否已落 issue #13（是 → 重匯 Anki）。流程疑義一律回 `pmba/pmba-course-cycle-sop.md`（現行 v4＋v2 執行層）。
- **情境 B（防彈卡驗證舊帳）** → gh #12 剩 47 張對一手 PDF：主 agent 親自核、反污染鐵則見 issue 本文；每張驗完**當場**翻 reviewed 旗標（SOP 已補此措辭）。
- **情境 C（Reader track 啟動）** → #6 是主 issue：用〈父母篇〉等材料實跑 2–3 篇 `/kb-loop` 診斷場（舊 track 剩 5 thread），再回頭收斂 `_system/prompts/reader-kb-loop-state-machine.md` 草案。#7（Bases dashboard）、#8（evidence policy）都排它後面。
- **情境 D（輸出端事件觸發）** → #16：財務課進到營運資金量化 → CCC MVP 子 issue；人脈知識事件 → people/ 首卡。事件驅動，不催工。
- **情境 E（ISSUE-06 策展防彈模組）** → 等 Sean 挑模組（建議序：異步協作 A054-057 ＞ 任務拆解 A028-030 ＞ 四等級 A006）。

## 必讀 Pointer

agent-neutral（相對專案根）：
- `./pmba/pmba-course-cycle-sop.md` — PMBA 學習 runbook v4（執行層以 2026-08-28 v2 為準，見檔首；完整改寫待 #18）
- `./.claude/skills/pmba-cycle/SKILL.md` — PMBA 教材 ingestion、學習排程查詢、Anki 重匯
- `./pmba/chatgpt_project_systemprompt.md` — ChatGPT Project Instructions 正典
- gh issue #13（`gh issue view 13 --comments`）— 財務 Day 1 learning trace 本體＋promote 紀錄
- `./notion-pages/issues/INDEX.md` — Notion AI 迭代 issue 狀態（僅剩 ISSUE-06 open）
- `./CLAUDE.md` — vault 結構/命名/Safety 正典
- `./wiki/index.md` — wiki 層 dormant 定案＋生成觸發條件（#14 落地處）

Claude Code auto-memory（絕對路徑；非 Claude agent 可略）：
- `C:\Users\USER\.claude\projects\D--Sean-KB\memory\MEMORY.md` — 專案 index＋Trigger→Resolution hot 條
- `C:\Users\USER\.claude\projects\D--Sean-KB\memory\promote-candidates.md` — 曾碰過的坑（碰坑先翻這；PC-001~006）

## 暫態注意事項（≤3）

- **Sean 兩個手動貼板待確認**（7/3 帶入，未確認完成）：①迭代後 ChatGPT prompt 重貼 Project Instructions ②蒜頭投影 prompt（主控台複習窗＋「下次複習日＝下堂−3」）[owner: Sean]
- git 報 .md modified 但 diff 空 ＝ Obsidian CRLF 幻影，忽略或順手 commit 正規化（已升 hot：MEMORY.md／PC-005；此行留給非 Claude agent）[owner: expire]

## 未決事項

- ~~Joan KB promote pass~~（2026-09-29 結案：AI-first 取消 promote 關卡，Sean 核准連同 PR #19 push）；4 場課 PDF（GPT三層駕馭術/0625/0810/Vibe Coding）待日後萃取
- ~~補漏掃描／7/9 複習日~~（2026-09-29 失效：PMBA 改 v2，未升級 Silver／Gold 的課不形成待辦）
- **#12**：47 張待驗證（等排程，主 agent 親核）
- **ISSUE-06**：策展防彈模組（等 Sean 挑）
- Reader track（#6/#7/#8）：等父母篇實跑啟動
