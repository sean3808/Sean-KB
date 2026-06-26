# Sean-KB Codex Agent Rules

> Sean 的長期個人知識庫（Personal Knowledge Base）。
> 這是 Obsidian vault，不是 coding 專案。
> 心法：Zettelkasten + LYT；交換層：OKF v0.1；Sean 是 curator，AI 是 drafter / maintainer。

## Mission

這個 repo 存放值得反覆檢索、連結與重組的知識，不是任務管理器，也不是 raw data dump。

核心轉換鏈：

```text
混亂事件 -> 抽象成概念 -> 連到案例 -> 形成判斷框架 -> 回到決策
```

主要知識範圍包含 PMBA、出口物流 / ERP 流程、AI tooling、管理理論、投資邏輯、育兒與生活心法、職涯方法論。

## Cold Start

開始任何工作前先看：

- `README.md`：vault 目錄概要。
- `CLAUDE.md`：目前最完整的 vault 結構、命名、note 規則正典。
- `session-continuity.md`：跨 agent handoff；若是恢復前一輪工作，先照這裡的第一個動作走。
- `_system/schemas/okf-note-schema.md`：OKF frontmatter 規格。
- `templates/okf-note.md`：新增 promoted note 的起始模板。

如果使用者只是要求建立、整理或稽核 Obsidian 內容，不要套用一般軟體專案的 build / test / lint 流程；只在任務明確需要時執行 `_system/` 內的腳本或 content lint。

## Source of Truth

- `notes/`、`maps/`、`wiki/` 是 Obsidian-native knowledge SoT。
- `_okf/` 是 generated bundle，可刪除重建；它是交換層，不是第二套筆記。
- Notion 是行動 / 專案 / 決策控制檯，承接任務、deadline、報價、出貨與客戶狀態。
- 會變動的營運狀態留在 Notion / Excel / ERP；能複用的洞察才進 Obsidian。

## Safety

- 修改既有 promoted note 前，先看 diff 範圍；不要靜默覆寫 Sean 已整理好的知識卡。
- 不要把 raw transcript、Excel、ERP、任務狀態表放進 `notes/`。
- Fully raw 素材（PDF、錄音逐字稿、原始講義）不進 repo；note 內只放外部路徑指標。
- 初階萃取後、品質足夠的 `.md` 才可放進 `sources/`。
- 不要把 `_okf/` 當長期資料源；需要交付給其他 agent 時才現生、用完即刪。
- worktree 可能有 Sean 或其他 agent 的變更；改檔前先看 `git status --short --branch`，不得還原 unrelated changes。

## Obsidian Writing Rules

- 優先使用 Obsidian Markdown：wikilink `[[Note]]`、alias `[[Note|別名]]`、embed `![[Note]]`、callout、frontmatter properties。
- 一張 concept note 只講一個核心想法，用自己的話寫，離開原語境仍成立。
- 每張 promoted note 必備 OKF core fields：`type`、`title`、`description`、`timestamp`。
- 新 note 從 `templates/okf-note.md` 複製，並對照 `_system/schemas/okf-note-schema.md`。
- highlight / fleeting 不是知識，只是候選素材；先放 `_inbox/`，由 Sean 判斷後才 promote。
- 外部素材摘要或來源索引放 `sources/`；不要把 `sources/` 誤當最終知識本體。

## Structure Rules

### `notes/`

- 只按型別切一層：`concepts/`、`cases/`、`people/`、`literature/`。
- 不開領域 / 主題命名的資料夾。
- Principle 併入 `concepts/`，以 `type` 與 `domain` frontmatter 表達。

### `notes/concepts/`

- 扁平結構，不開「每來源一子資料夾」。
- 檔名一律帶來源前綴：`<來源>-<卡號>-<標題>.md`。
- `pkm-id` 必須全 vault 唯一；每個來源使用獨立號段，不得跨來源重號。
- 每個來源必備 literature note、source 卡與對應 MOC。
- `source_ref` 不得指向不存在的卡。

### `maps/`

- 一律扁平，作為 MOC / LYT 導航層。
- MOC 階層用 MOC 互連表達，不用巢狀資料夾。
- 主題、領域、來源是 frontmatter + MOC + wikilink 的導航層，不是物理資料夾層。

## Module Responsibilities

| 路徑 | 職責 |
|---|---|
| `_inbox/` | fleeting / import / voice 等候選素材，待 Sean 判斷 |
| `sources/` | 原始素材摘要、來源索引、初階萃取；不是知識本體 |
| `notes/` | knowledge SoT；存放 promoted concepts / cases / people / literature |
| `maps/` | MOC、LYT 導航、跨來源主題連結 |
| `wiki/` | AI 維護的領域 wiki 與索引 |
| `_system/` | schemas、prompts、scripts、lint reports、exports、logs |
| `_okf/` | generated OKF bundle；暫態、可重建、通常 gitignored |
| `templates/` | note templates |

## Workflows

- PMBA 課後編譯：`_system/prompts/pmba-compile.md`
- OKF export：`_system/prompts/okf-exporter.md`
- OKF lint：`_system/prompts/okf-lint.md`

若要做 vault 稽核，優先檢查：

- `notes/` 只切型別、`maps/` 全扁平。
- concept note 檔名有來源前綴。
- `pkm-id` 全 vault 唯一。
- promoted note frontmatter 必備欄位齊全。
- broken wikilink 為 0。
- 每個來源有 literature note、source 卡與 MOC。
- `_okf/` 沒被當成常駐 SoT。

## Exclusions

- 不導入 local LLM / Ollama。
- 不把向量庫 / RAG 當主路徑。
- 不把 Obsidian graph view 當成功指標。
- 不做 Notion ↔ Obsidian 內容雙向全文同步；只做雙向異步引用。

## Collaboration

- 對內容性變更，先保留可 review 的 diff；Sean 決定哪些值得留。
- 對工程性腳本變更，保持範圍小，只改任務需要的部分。
- 給下一個 agent 的 handoff 要保留可 grep 的路徑、命令、錯誤字串與驗證結果。
- 使用者說「先做到這裡」就停在指定邊界，不自動延伸。

