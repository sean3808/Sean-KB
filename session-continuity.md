---
name: Session Continuity
description: 冷啟動入口 — 現況、第一個動作、必讀 pointer
type: project
---
最後更新：2026-07-03（PMBA 課程循環 runbook v3 定案＋財務 Day 1 首次 promote 落地；下一步＝Sean 跑補漏掃描 → 7/9 複習日）

> 本檔刻意進 git（Sean 2026-06-26 覆寫 session-park「gitignore」預設）。重寫後會顯示 modified，由 Sean 決定 commit 時機。

## TL;DR — 現況一行

PMBA 課程軌全線通車：財務管理 Day 1（6/28）跑完首次完整迴圈（T+0/T+1 retrieval → gh #13 → **promote 4 張卡＋fm- 號段導航層**）→ 流程定案為 **runbook v3**（`pmba/pmba-course-cycle-sop.md`，人機共讀：§0 相位判定程序＋角色卡＋降級表）→ Claude Code 職責封裝成 **`/pmba-cycle`** skill → Anki 工廠上線（#10 closed）→ 跨來源 earned links 首批 12 條。**下一步＝Sean 對 ChatGPT 跑補漏掃描（~7/5 前），7/9 複習日用 /pmba-cycle 接 promote。**

## 本次收工快照（2026-07-03）

- HEAD：`9bb3acb`，已 push、working tree clean、與 origin 同步
- 本兩日推進：`656bd75`（Day 1 promote）→ `d6d57c8`（Anki 工廠）→ `ffb7740`（cycle SOP 初版＋ChatGPT prompt 迭代）→ `8f5eb01`（prompt 壓縮 3731 字）→ `de32a52`（跨來源 12 links）→ `6187ec3`/`4a9ffb4`（SOP 補漏窗＋複習日算法二迭）→ `c0edcf6`（**runbook v3**）→ `589aab4`（判準加「判斷框架」＋ `/pmba-cycle` skill）
- Notion 已做：課程 DB 加 `下次複習日`（date）/`Learning trace`（URL）兩欄；財務管理列填 7/9＋issue #13 URL
- gh 已做：#10 closed（Anki）；新開 **#14**（wiki/ 定位）**#15**（前綴正典衝突）**#16**（輸出端啟用軌道）；#12 補「33 張已驗證卡 reviewed 旗標未回寫」缺口 comment；#6/#7/#8 scope 對齊 comments
- ISSUE-05 done（操作層/方法論層邊界，以 #13 實證收斂）；notion-pages/issues/INDEX 已同步（僅剩 ISSUE-06 open）

## 第一個動作（依情境分支）

- **情境 A（預設：續 PMBA 循環）** → 先跑 `/pmba-cycle` Step 0 判相位。當前循環狀態：財務 Day 1 trace 完成於 7/2、**補漏掃描未做**（窗口 ~7/5，Sean 對 ChatGPT 跑「trace vs PLAUD 全文比對」→ 分揀 → 第二批題卡）→ 第二批落 issue #13 後我重匯 Anki → **7/9 複習日**（蒜頭浮出；Sean 答兩批題卡＋費曼＋待查證＋拍板）→ Promote 則跑 promote run → 7/10–11 預習 → **7/12 Day 2** 新循環。一切流程疑義回 `pmba/pmba-course-cycle-sop.md`（runbook v3，含 §0 判定程序與 §5 降級表）。
- **情境 B（治理決策題，等 Sean 拍板）** → gh **#14**（wiki/ 三選一）、**#15**（前綴轉正，建議修 Notion 耐久決策入口 §8 一句，MCP 可代辦）、**#16**（輸出端三觸發器，事件驅動不催工）。
- **情境 C（防彈卡驗證舊帳）** → gh #12 剩 47 張對一手 PDF（主 agent 親自核、反污染鐵則見 issue 本文）；另有「33 張已驗證卡 reviewed 旗標批次翻」等 Sean 授權（改 promoted note，先出 git diff）。
- **情境 D（ISSUE-06 策展防彈模組）** → 判準已由 ISSUE-05 給定（「會改變操作行為」才入 Skill）；等 Sean 挑模組（建議序：異步協作 A054-057 ＞ 任務拆解 A028-030 ＞ 四等級 A006）。
- **情境 E（Reader/隨材診斷場）** → `/kb-loop`（已補軌道邊界：PMBA 課程材料不走它）。舊 track 父母篇診斷場剩 5 thread。

## 必讀 Pointer

agent-neutral（相對專案根）：
- `./pmba/pmba-course-cycle-sop.md` — **PMBA 循環 runbook v3（本專案當前最重要正典）**：§0 今天該做什麼判定程序、§2 角色卡、§3 相位 checklist、§5 降級表、§8 版本紀錄
- `./.claude/skills/pmba-cycle/SKILL.md` — Claude Code 執行層（promote run checklist＋Anki 重匯）
- `./pmba/chatgpt_project_systemprompt.md` — ChatGPT Project Instructions 正典（3964 字/限 8000）
- `./notion-pages/issues/INDEX.md` — Notion AI 迭代 8-issue 狀態（僅剩 06 open）
- gh issue #13（`gh issue view 13`）— 財務 Day 1 learning trace 本體＋promote 紀錄
- `./CLAUDE.md` — vault 結構/命名/Safety 正典（Workflows 段第一行有 runbook pointer）

Claude Code auto-memory（絕對路徑；非 Claude agent 可略）：
- `C:\Users\USER\.claude\projects\D--Sean-KB\memory\MEMORY.md` — 專案 index
- `...\memory\promote-candidates.md` — 曾碰過的坑（碰坑先翻這）

## 暫態注意事項（≤3）

- **Sean 有兩個手動貼板待確認**：①迭代後的 ChatGPT prompt 重貼 Project Instructions（判準新措辭版）②蒜頭投影 prompt（主控台「今日待複習/T-3 預習窗」＋課程管理 skill「下次複習日＝下堂−3」規則）[owner: Sean]
- 補漏分揀判準定案：「會改變我的**決策、判斷框架**或工作方法嗎？」以 Sean 為準不以老師重點為準；未入選留 PLAUD＋issue，考試/作業走平行軌 [owner: expire]
- Obsidian 開著會把卡片重存成 CRLF → 假 modified 幻影；stage 後零差異即幻影，直接 commit 正規化或忽略 [owner: expire]

## 未決事項

- **補漏掃描**（Sean × ChatGPT，~7/5 前）→ 第二批題卡 → flag-me（重匯 Anki）
- **7/9 複習日**：兩批題卡＋review decision；Promote → `/pmba-cycle` promote run
- **gh #14/#15/#16** 三個決策/追蹤題 → flag-Sean
- **#12**：47 張待驗證＋33 張 reviewed 旗標批次翻（等授權）
- **ISSUE-06** 策展防彈模組（等 Sean 挑模組）
- 舊 track（kb-loop）：父母篇診斷場剩 5 thread
