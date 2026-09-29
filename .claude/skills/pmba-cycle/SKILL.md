---
name: pmba-cycle
description: >
  PMBA 的 AI-first 教材 ingestion、學習相位查詢與 Anki 匯出入口。
  Use when: /pmba-cycle、「教材放進 KB」、「重匯 Anki」、
  「PMBA 今天該做什麼」、「複習日到了」、「課程結案」。Sean 提供來源即完成人工 Gate，不等複習或逐卡拍板。
  正典為 pmba/pmba-course-cycle-sop.md；一般 Reader ingestion／診斷場也可用 /kb-loop。
---

# pmba-cycle — ingestion 與學習排程分流

## Step 0 — 按任務分流

- **交教材／case／PLAUD／learning trace 給 Sean-KB**：立即跑下方 ingestion，不查日期、不等待學習相位或另開候審 issue。
- **詢問今天學什麼／複習／結案**：預設只有 Bronze（課初回想上一堂＋課末 3 點＋1 疑問，runbook 檔首）；只有 Sean 已把該堂升級 Silver／Gold 時，才讀 `pmba/pmba-course-cycle-sop.md`，取台北日期（`date`／`Get-Date` 配合時區），查本課 T0／T0next 與 learning trace，依 §0 判相位。資料不足只詢問缺的學習排程資訊，不擋已授權 ingestion。
- **重匯 Anki**：執行下方命令。只讀 `notes/concepts/` 的「Retrieval 題卡」Q/A；issue 內尚未落卡的題不會匯出，不宣稱已包含。

## Ingestion run

1. 讀 `_system/prompts/pmba-compile.md`、`maintenance-learning-loop.md`、schema；記錄 Sean 指定來源的 evidence，無逐卡 Gate。
2. 取得完整素材、評估品質、建立 Source Tree／index，依語意原子化；只有一份 120 頁 PDF 也可開始，不要求 Sean 的 retrieval、感受、Notion deadline 或摘要。
3. 對照現有卡 dedup／reconcile，建立 source_ref＋source_evidence；按來源可靠度設 confidence，不因 AI 產出或 Sean 未答題而降級。
4. 原則／框架說清楚 source vs AI inference vs Sean stance。新來源衝突 Sean Principle 時保留雙方與 comparison link，原則不覆寫。
5. 直接建 earned links（旁留 why），更新既有跨來源 MOC；書籍／課程視需求加 Literature，來源的「章節 → 卡片」目錄寫在 Source Note 的 Source Navigation。既有卡只做 Additive Update；需改寫既有句子走 SOP §4 Rewrite。
6. content lint＋語意自審＋完整 diff；更新 source_status／Integration／Exceptions，依任務 commit／PR。只在真正例外請 Sean 判斷，其他內容完成。
7. 題卡有變更才重匯 Anki。AI 可依來源寫標準答案，不能代寫 Sean 的個人 recall 紀錄。

## Anki 匯出

```bash
uv run python _system/scripts/export_anki.py
```

輸出 `_system/exports/anki-cards.txt`（gitignored）；Sean 匯入 Anki。Anki 是學習輸出，不是入庫前置。

## 維護邊界

新增與 Additive Update 自動完成並留 Git trail；Rewrite 與高風險刪改依共用 SOP §4 處理。本機文件修改不等於 Notion／ChatGPT Project Instructions 已更新；不自行寫遠端、發 comment 或 merge。
