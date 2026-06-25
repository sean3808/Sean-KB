# Sean-KB Agent Rules

> Sean 的長期個人知識庫（Personal Knowledge Base）。
> 心法：Zettelkasten + LYT；引擎：AI / LLM Wiki；交換層：OKF v0.1。
> 耐久決策入口（SSOT）：Notion 頁「Obsidian AI LLM Wiki ｜ 個人知識庫耐久決策入口」。

## Mission

這個 repo 是 Sean 的長期知識本體，**不是普通筆記資料夾，也不是任務管理器**。
它存的是「值得反覆檢索與重組」的知識：PMBA、出口物流 / ERP 流程、AI tooling、
管理理論、投資邏輯、育兒與生活心法、職涯方法論。

核心轉換鏈：混亂事件 → 抽象成概念 → 連到案例 → 形成判斷框架 → 回到決策。

## Source of Truth（三層架構，定案）

- **Obsidian-native notes 是知識 SoT**（`notes/`、`maps/`、`wiki/`）。
- **`_okf/` 是 generated bundle**，由 AI / script 產出，可刪除重建，**不是第二套筆記**。
- **Notion 是行動 / 專案 / 決策控制檯**（任務、deadline、報價、出貨、客戶狀態）。

判準：會變動的狀態留 Notion / Excel / ERP；能複用的洞察才進 Obsidian。

## Safety（不可違反）

- 絕不把 `sensitivity: private` 或 `sensitivity: confidential` 的 note export 到 `_okf/`。
- 客戶名稱、報價、發票、訂單明細、個資一律視為 confidential，未經 Sean review 不得進 `_okf/`。
- 修改既有 promoted note 前，一律先產生 Git diff 讓 Sean review，不靜默覆寫。
- raw transcript / Excel / ERP / 任務狀態表 **不進** `notes/`，只留 `sources/` 或 Notion。

## Note Rules

- 一張 concept note 只講一個核心想法；用自己的話寫；離開原語境仍成立。
- 每張 promoted note 必備 OKF core fields：`type`、`title`、`description`、`timestamp`。
- frontmatter 規格見 `_system/schemas/okf-note-schema.md`；新 note 從 `templates/okf-note.md` 複製。
- 不把營運狀態表轉成 Obsidian note。
- highlight / fleeting 不是知識，是候選素材，先進 `_inbox/`，由 Sean 判斷才 promote。

## 資料分級（sensitivity → 可否 export 到 _okf/）

| sensitivity | 可 export | 說明 |
|---|---|---|
| public | ✅ | 公開資訊 |
| internal | 需 review | 工作洞察、去識別化案例 |
| private | ❌ 不可自動 export | 家庭、健康、個人心理 |
| confidential | ❌ 不可 export | 客戶、價格、內部營運、個資 |

## 維護分工

- **AI（Claude Code）**：索引、補 link、整理 MOC、產 index、export OKF、跑 content / OKF lint、敏感資料檢查；改動一律走 Git diff。
- **Sean**：判斷哪些值得留、promote、approve、最終決策。AI 是 drafter，Sean 是 curator。

## Workflows

- PMBA 課後編譯：`_system/prompts/pmba-compile.md`
- OKF export：`_system/prompts/okf-exporter.md`
- OKF lint：`_system/prompts/okf-lint.md`

## Obsidian Skills（操作本 vault 時優先使用）

這是一個 Obsidian vault。處理 vault 內容前，先反射性考慮對應的 `obsidian:*` skill，
不要只用通用 Read/Write 硬幹 Markdown。

| Skill | 何時用（對映本 vault） | 關鍵用法 |
|---|---|---|
| `obsidian:obsidian-markdown` | **預設**。寫 / 改 `notes/`、`wiki/`、`maps/` 任何卡片 | wikilink `[[Note]]`、`[[Note\|別名]]`、embed `![[Note]]`、callout `> [!warning]`、`==highlight==`、frontmatter properties |
| `obsidian:obsidian-cli` | 程式化讀 / 建 / 搜尋 note、批次操作、reload plugin | `obsidian read file=`、`obsidian create name= content= template=`、`obsidian search query= limit=`。**前提：Obsidian app 要開著** |
| `obsidian:obsidian-bases` | `maps/` 做動態 note 視圖（依 `domain` / `status` / `sensitivity` / `type` 篩選聚合），取代手動維護清單 | `.base` 檔：`filters` / `formulas` / `views`（table / card） |
| `obsidian:json-canvas` | `maps/` 視覺化 MOC、概念關係圖、流程圖 | `.canvas` 檔：`nodes`（text / file）+ `edges` |
| `obsidian:defuddle` | `sources/` 收網路文章 / 文獻，轉乾淨 markdown（**取代 WebFetch**，非 .md URL） | `defuddle parse <url> --md -o sources/<...>.md`。前提：`npm i -g defuddle` |

原則：寫卡片用 `obsidian-markdown` 語法（wikilink 是知識織網的核心）；批次 / 搜尋走 `obsidian-cli`；
導航地圖優先用 `obsidian-bases`（動態，免手工維護）或 `json-canvas`（視覺）；外部素材入 `sources/` 用 `defuddle`。
注意：export 到 `_okf/` 時 wikilink 要轉成標準 markdown link（見 `_system/prompts/okf-exporter.md`）。

## 排除項（本階段不做）

- local LLM / Ollama（永久排除）。
- 向量庫 / RAG 當主路徑、graph view 當成功指標（本階段排除）。
- Notion ↔ Obsidian 內容雙向全文同步（只做雙向異步引用）。
