# OKF-compatible Note Schema（Sean-KB）

OKF v0.1 的最低要求仍是非空 `type`，unknown fields 必須保留。本檔的 ingestion 欄位是 Sean-KB local contract，不提高 OKF consumer 的最低門檻。新知識用 `templates/okf-note.md`，Source 用 `templates/source-note.md`。

## OKF core fields

| 欄位 | Sean-KB 正式 note | 說明 |
|---|---|---|
| `type` | 必備 | Concept / Case / Person / Literature / Playbook / Principle / Map / Source / Decision |
| `title` | 必備 | 一句話標題 |
| `description` | 必備 | 1–2 句可獨立閱讀摘要 |
| `timestamp` | 必備 | ISO 8601 含時區；note 建立或版本更新時間，不代替來源版本或證據日期 |
| `resource` | Source 必備 | 可定位的原始 URL／Drive pointer／local path；不要只寫書名 |
| `tags` | 建議 | list；沿用既有 tags，不為本次重構大量改名 |

## 共用 custom fields

| 欄位 | 說明 |
|---|---|
| `id` | 穩定內部 ID，既有 `pkm-YYYYMMDD-<source namespace>-<code>` 沿用；全 vault 唯一，改名不變。規則口語稱 pkm-id，實際欄位仍是 `id` |
| `status` | seed / growing / stable；內容成熟度，不是批准與來源處理狀態 |
| `domain` | work / pmba / ai / life / investment / parenting / career；相容既有 productivity 等值 |
| `lang` | 預設 zh-TW |
| `confidence` | low / medium / high；依證據、語意可靠度，不依 AI／人類作者或學習進度 |
| `source` / `source_type` | 相容既有來源名稱及 transcript / work-event / reading / class / idea 等類型 |
| `source_ref` | wikilink list；新衍生 notes 指向 `sources/` 的 Source。舊 Literature 引用保留，下次實質處理補足 Source 鏈 |
| `notion_refs` | Notion URL list，雙向異步引用 |
| `aliases` / `mocs` | 同義檢索／MOC wikilink list；不複製同義卡 |
| `reviewed` / `reviewed_at` | 可選，歷史人工／既有驗證紀錄；不是入庫或 export gate，也不代表來源所有主張是 Sean 立場；AI 不自行翻為 true |
| `ingestion_version` | 新 pipeline 產物填 `1`；舊卡不批次強制遷移 |
| `generated_by` | ai / sean / mixed；只表示產生方式，不是品質等級 |
| `claim_origin` | source / ai-inference / sean；新衍生 note 必填，預設 source。若混合，拆卡或逐段明示歸因，勿把 AI 推論包成來源原話。AI 二手素材（如 ChatGPT 校正稿）追得回一手原文才標 source 並引用原文，否則 ai-inference |
| `stance_evidence` | 僅 claim_origin: sean 必填：Sean 明示主張的指示／紀錄定位；選書或 reviewed 不足以證明個人主張 |

## Note types 與位置

| Type | 位置 | 用途 |
|---|---|---|
| Concept | `notes/concepts/` | 抽象概念、decision framework（無需新增型別） |
| Principle | `notes/concepts/` | 來源原則或 Sean 明示個人原則，以 claim_origin 區分；不限 life |
| Playbook | `notes/concepts/` 或 `wiki/` | 可重複流程，保留適用條件 |
| Case | `notes/cases/` | context / event / decision / reusable insight；說清楚誰做的決定 |
| Person | `notes/people/` | 作者、老師、角色 |
| Literature | `notes/literature/` | 來源脈絡與跨章綜述，可跨 source；不必每篇短文另造一張 |
| Map | `maps/` | LYT／MOC 跨來源導航，不代替來源章節樹 |
| Source | `sources/` | metadata、external pointer、source tree、解析與整合紀錄 |
| Decision | Notion 為主，長期理由可在 `notes/concepts/`／`notes/cases/` 萃取 | 個人決策須 Sean 明示；一般來源決策忠實歸因 |

一般 concept 描述知識本身，不能寫成「Sean believes」。只有明示的 Sean Principle／Decision／personal framework／reflection 才用 `claim_origin: sean`。

## Source lifecycle 與品質

新 Source 必填 `ingestion_version: 1`、core fields、`id`、`resource`、以下 selection 欄位：

```yaml
source_status: selected  # selected / ingested / indexed / atomicized / integrated
selected_by: sean
selection_basis: sean-provided  # sean-provided / sean-requested
selection_evidence: '2026-09-29 Sean 指定這份教材納入 Sean-KB（填實際指示或可回溯定位）'
source_version: '取得於 2026-09-29；原版日期未知'  # ingested 起必填，依真實情況記錄
# ingested 起必填；無法判讀用 unknown，不捏造品質
document_quality:
  text: good            # good / partial / poor / unknown
  structure: good       # good / partial / poor / unknown
  tables: partial       # good / partial / poor / unknown / none
  ocr: false            # true = 內容經 OCR；不是「需要 OCR」
parsing_strategy: tree   # tree / structure-text / repair；indexed 起必填
```

`source_status` 與 `status` 分開。選擇證據由 AI 從 Sean 的實際交辦填入，不發回讓 Sean 再 approve。AI 自找、未指定納入的 research 不得靠填 `selected_by: sean` 偽裝授權。

## Source Tree contract（indexed 起）

`source_tree` 是 list，每個 node 有以下欄位。短文章可只有單一 root；長篇保留 chapter／section hierarchy，不需要特定 parser dependency。

```yaml
source_tree:
  - node_id: chapter-2
    parent_id: null
    heading: 第 2 章 營運資金
    section: 第 2 章
    page_range: [21, 38]
    evidence_pointer: 'local:finance.pdf#page=21'
    summary: 本章建立庫存、應收與現金週轉的關係。
  - node_id: section-2-1
    parent_id: chapter-2
    heading: 2.1 現金轉換週期
    section: 第 2 章 > 2.1 現金轉換週期
    page_range: [22, 25]
    evidence_pointer: 'local:finance.pdf#page=22'
    summary: 說明庫存天數、應收天數與應付天數的關係。
```

- node ID 在該 source 內唯一且穩定；父節點必須存在，不可成環；ID 不以可變標題當唯一 identity。
- `heading`、`summary` 必填；至少具備 `section`／`page_range`／`evidence_pointer` 其中一種定位。
- `page_range` 為含首尾的正整數二元組；PDF 預設檔案實體頁序（1-based）。若印刷頁碼不同，寫進 `section`，不混用。
- 無頁碼文章用實際 heading／HTML anchor；逐字稿可用時間碼 pointer；絕不發明頁碼。`resource`＋locator 應能返回原文。
- 頁數、節點數不是 card quota。tree summary 是 navigation，不等於概念卡。

## Atomic note provenance（新 pipeline 必備）

新 AI 衍生 note 必填 `source_ref`＋`source_evidence`，每個來源至少一筆，不能只引用不可追溯的 AI 摘要。Map 是導航例外：引用 cards，不強制複製所有 cards 的 evidence；它不應引入沒有來源的新主張。

```yaml
source_ref:
  - '[[sources/pmba/財務教材]]'
source_evidence:
  - source: '[[sources/pmba/財務教材]]'  # 必須出現在 source_ref
    source_version: '第 3 版'           # 實際驗證的版本，Source 改版後仍保留
    node_id: section-2-1               # 若 source 有 tree，使用有效 node ID
    section: 第 2 章 > 2.1 現金轉換週期
    page_range: [22, 25]
    evidence_pointer: 'local:finance.pdf#page=22'
```

每筆 evidence 至少有 section、page_range、evidence_pointer 之一；跨來源綜合用多筆配對記錄，不把頁碼與來源放在互不對應的平行 arrays。具體主張在正文引用對應證據／版本，必要短引文即可。若只取得二手萃取，明示是二手及限制，不宣稱看過一手 PDF。

## 相容性與交換

- 正式 AI note 和人工 note 同等參與 retrieval、reasoning、OKF export；不按 `reviewed` 或 generated_by 過濾。
- OKF concept ID 仍是 bundle-relative path（不含 `.md`）；Sean `id` 不變，export 改名需記 `_okf/log.md`。
- unknown fields、evidence 的版本／頁碼／定位在 export 必須保留。既有 concept exporter 只產 concept bundle：source 名稱與片段保留為 vault-relative pointer；若接收端需要完整來源導航，依 exporter prompt 一併封裝 references。
- 舊卡缺新欄位僅為 migration warning，不降成 candidate；實際處理時逐步補足，不憑空替既有 362 卡新增 provenance。
- raw transcript、未獲 Sean 選定的 inbox、任務／營運狀態不進 knowledge bundle。
- Content lint 與語意自審見 `_system/prompts/content-lint.md`；技術驗證不等於驗證所有主張為真。
