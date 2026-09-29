---
name: kb-loop
description: >
  Sean-KB 的 AI-first ingestion 與按需學習入口。Sean 指定／提供／匯入／要求納入的素材直接通過 Source Selection，
  AI 完成 structure-first 解析、semantic atomic decomposition、dedup、earned links、MOC 與 lint。
  Use when: /kb-loop、「放進 Sean-KB」、「處理這篇 Reader」、「匯入這份教材」、「織網」，或要求診斷式學習。
  PMBA 教材可走同一 ingestion；課程學習排程／Anki 走 /pmba-cycle。純 export／lint 用對應 prompts。
---

# kb-loop — AI-first ingestion / personal learning

讀取 `_system/prompts/maintenance-learning-loop.md`（流程正典）、`reader-kb-loop-state-machine.md`（狀態與恢復）及 `_system/schemas/okf-note-schema.md`。

## 1. 判斷任務與 Source Selection

- Sean 指定給 Sean-KB 的來源：記錄實際 selection evidence，直接 selected，不再問逐卡批准。
- Sean 只要求研究／學習，或 AI 自行找到文章：只作 transient evidence，不能永久入庫、也不建 repo 候審 queue。Reader feed／整個 Library 不因可讀取就自動獲授權。
- Sean 主動要求費曼／Socratic／retrieval：走 §3；若同時交辦入庫，兩條流程獨立進行。

## 2. Ingestion run

1. 檢查 Git 狀態與既有 source ID／resource／版本，避免重跑造重複卡。
2. 用 `templates/source-note.md` 建／更新 Source；取得內容、評估 document quality。raw binary 預設留外部，repo 放 pointer。
3. 先理解全文結構，重建 headings／Source Tree／section summaries；章節覆蓋不完整就如實記錄，不能只讀摘要冒稱全書完成。
4. 做 semantic atomicity：一個可複用主張一張，保留條件、限制；按內容選 Concept／Principle／Case／Literature／Playbook 等 type。300 頁不等於 300 張卡。
5. 查 title／aliases／既有 MOC 並讀相關卡，dedup／reconcile；新卡或更新卡都填 source_ref／source_evidence。一般來源不變成 Sean 個人立場。
6. 直接建立 earned wikilinks，附近留一句 why；同主題關係用 tags／MOC。更新既有跨來源 MOC，真正新領域才新建；來源的「章節 → 卡片」目錄寫在 Source Note 的 Source Navigation，不另建單一來源 MOC。
7. 依 content-lint prompt 做機械＋語意自審、檢查完整 diff，更新 Source 的 Integration／Exceptions 與 source_status，保留 Git trail。正常一路到 integrated，不等 Sean 消化。
8. 回報新建／更新／重用、provenance、MOC、驗證與例外。遵循本次任務的 commit／PR 邊界，不自行 merge。

既有卡只做 Additive Update；改寫或刪除既有句子走 SOP §4 Rewrite（Sean 不在場時記為 Source Exception）。只暫停真正例外的 mutation，其餘繼續；不覆寫 Sean Principle。

## 3. Personal learning（按需）

Sean 想學某主題時，可讓他先重述／先答，再做 Socratic、Feynman、steelman、案例遷移與 source 對照；基礎穩時可快答，不硬上診斷場。

保護盲測時不先展示答案，但 AI 可平行完成來源處理。AI 可產有來源的標準答案，不能冒充 Sean 已經回答／內化。學習的進度、output target、題卡數量都不阻塞 ingestion；不建立逐卡／逐 link approve checklist。
