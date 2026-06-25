# OKF-compatible Note Schema（Sean-KB）

依據 OKF v0.1 SPEC。OKF 只有 `type` 是唯一必填；`title`、`description`、`resource`、
`tags`、`timestamp` 是建議欄位；unknown fields **必須被保留**，不得導致 consumer reject。
新 note 從 `templates/okf-note.md` 複製。

## OKF core fields

| 欄位 | 必填 | 說明 |
|---|---|---|
| `type` | ✅（OKF 唯一硬性） | Concept / Case / Person / Literature / Playbook / Principle / Map / Source / Decision |
| `title` | 建議 | 一句話標題 |
| `description` | 建議 | 1–2 句摘要，能獨立閱讀 |
| `resource` | 建議 | 對應外部資源（URL / 檔案），可空 |
| `tags` | 建議 | list，小寫 kebab |
| `timestamp` | 建議（promoted note 視為必備） | ISO 8601 含時區，如 `2026-06-25T10:30:00+08:00` |

> promoted note（要進 `_okf/` 的）至少必備 `type`、`title`、`description`、`timestamp`。

## Sean custom fields

| 欄位 | 說明 |
|---|---|
| `id` | `pkm-YYYYMMDD-NNN`，穩定內部 ID，note 改名也不變 |
| `status` | seed / growing / stable |
| `domain` | work / pmba / ai / life / investment / parenting / career |
| `lang` | 預設 zh-TW |
| `confidence` | low / medium / high |
| `source_type` | transcript / work-event / reading / class / idea |
| `source_ref` | wikilink list 指向 `sources/` |
| `notion_refs` | Notion page URL list（雙向異步引用） |
| `aliases` | 別名，協助檢索 |
| `reviewed` / `reviewed_at` | Sean curate 標記 |

## Note types 與位置

| Type | 位置 | 用途 |
|---|---|---|
| Concept | `notes/concepts/` | 抽象概念、判斷框架 |
| Case | `notes/cases/` | 可複用的具體案例（context / event / decision / insight） |
| Person | `notes/people/` | 老師、同學、作者、客戶角色 |
| Literature | `notes/literature/` | 書、論文、文章、課堂教材 |
| Playbook | `notes/concepts/` 或 `wiki/` | 可重複流程 |
| Principle | `notes/concepts/` | 個人生活原則（`type: Principle` + `domain: life`，不另開領域資料夾，見 issue #2） |
| Map | `maps/` | MOC / LYT 導航 |
| Source | `sources/` | 原始素材摘要或索引 |
| Decision | Notion 為主，Obsidian 可萃取 | 長期決策與理由 |

## OKF concept ID vs Sean internal ID

- **OKF concept ID** = `_okf/` 內相對 path without `.md`（如 `concepts/requirement-framing`）。OKF 以 path 作 identity，path 改名須寫入 `_okf/log.md`。
- **Sean `id`**（`pkm-...`）= 追蹤原始 note 的穩定 ID。兩者不可混淆。

## 不進 Obsidian / 不進 _okf

- 報價、月用量、發票、訂單狀態、出貨進度、每日 task、即時營運資料 → 不進 Obsidian（會變動的營運狀態 vs 可複用知識的分層）。
- raw transcript、未 review 的 inbox note → 不進 `_okf/`。
