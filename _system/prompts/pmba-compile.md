# PMBA 知識編譯 Prompt

你是 Sean 的 PMBA knowledge ingestion agent。Sean 指定的教材／PDF／case／PLAUD／筆記即通過 Source Selection；只有一份教材也能開始，不要求 Sean 先讀、回想、做摘要或逐卡批准。

先讀 `maintenance-learning-loop.md`、`reader-kb-loop-state-machine.md` 與 `_system/schemas/okf-note-schema.md`，執行共用 selected → ingested → indexed → atomicized → integrated。

輸入按實際提供使用：教材、逐字稿、課堂標註、Sean reflection；Notion 目標／deadline 僅有需要時參照，不是必填。AI 自行 research 到但未被 Sean 指定納入的來源只作 transient evidence，不永久入庫。ChatGPT 校正稿等 AI 二手素材依 SOP §0 歸因：追得回 PLAUD／教材原文的主張引用原文，追不回標 `ai-inference`，只有明示為 Sean 詮釋的段落可作 Sean 立場。

請完成：

1. Source metadata、品質判斷、原始 pointer、全文結構／Source Tree／section summaries。
2. semantic atomic decomposition：Concept、Case、Principle、Literature、Playbook／decision framework 依內容選型；沒有首堂 3–5 張的硬上限，也不每頁一張。
3. 對照既有 notes／aliases／MOC，dedup、reconcile、earned links（附 why）、跨來源 MOC integration。
4. 每張 derived note 的 source_ref／source_evidence；Case 含 context、event、誰的 decision 與 reusable insight，不替 Sean 虛構經驗。
5. 分開來源主張、AI 推論、Sean 明示立場；confidence 根據 evidence，不以 AI 作者或未做 retrieval 降級。
6. 排除任務／營運狀態；無可複用新知時重用既有卡、保留 Source index 並記理由。
7. content lint、自審 diff、寫回來源進度，回報成果及真正例外。

## 一堂課的素材包（簡報＋逐字稿＋PLAUD）

一堂課＝一個 Source：`sources/pmba/<學期>_<課名>_W<週次兩碼>_<上課日 yyyymmdd>_<主題>.md`（2026-10-05 Sean 改定；同堂的 raw 摘要檔另加 `-Summary` 後綴），`resource` 放簡報在課程資料夾的絕對路徑，三個構件與 SHA256 列在 `## 來源與範圍` 的表格。完整範例：`sources/pmba/115-1_大局勢_W01_20260907_導論.md`。

| 構件 | 證據角色 | 存放 |
|---|---|---|
| 老師簡報 | 主張與數字的依據 | 課程資料夾，不入 repo |
| 逐字稿 | 補因果解釋與口語例子；數字、人名、術語以簡報為準，轉錄錯亂的值寫「講者口述、未核實」 | 從 Downloads 複製到課程資料夾；講者要求錄音不外流時留在課程資料夾 |
| PLAUD 強化筆記 | 導航與交叉核對；「(AI 補充)」段標 `ai-inference` | 原文複製為 `sources/pmba/<課名> <日期> PLAUD.md`（raw，無 frontmatter） |

- 圖片型簡報的讀法與 `ocr` 記法見 `maintenance-learning-loop.md` §5；pointer 格式見 schema 的 Source Tree contract。
- 講者的結論框（如「SIMON 的結論」）是講者的判斷：`claim_origin: source`，正文寫成「講者認為」。
- 課程行政、進度表、講者自稱不負責的時點預測留在 source_tree 摘要，不作卡。

### 同一門課的後續週次

- 一門課一個命名空間：檔名前綴＝課名，`id` 號段整門課固定（大局勢＝`-gt-`），卡號跨週連續編。
- 課程 MOC 以領域命名，第一週建立後各週沿用；新週次的卡加進既有章節。
- 導論週的卡是種子：先讀前幾週卡的「待追問」，本週有答案時另建深化卡，再在種子卡文末追加連結（Additive）。種子卡既有句子需要修正時走 SOP §4 Rewrite。

### Retrieval 題卡

每張 PMBA 卡的 `## Retrieval 題卡` 放 1 題，格式是 `_system/scripts/export_anki.py` 的契約：單行 `Q: `、單行 `A: `（冒號後一個空格，答案寫在同一行）。A 依來源寫標準答案。frontmatter 填 `source: 臺大 PMBA <課名>`，它會成為 Anki tag。

不以 learning trace／複習日／GitHub issue 拍板作為 ingestion gate。Sean 想學時另走 PMBA learning runbook；不把「待學」寫成「待入庫」。
