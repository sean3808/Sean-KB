# Sean-KB

Sean 的長期個人知識庫：**Human-curated, AI-processed knowledge system**。

**Sean 提供素材 = 已通過人工入口審核。** Sean 只選值得保留的來源；AI 負責解析、理解結構、語意原子化、去重、provenance、earned links 與 MOC 整合。沒有逐卡 approve queue，也不等待 Sean 先消化。

- **架構**：Obsidian Knowledge SoT + Notion action/project control plane + `_okf/` OKF exchange layer + filesystem agents + Git。
- **心法**：Zettelkasten、semantic atomic notes、flat concepts、LYT／MOC、earned links。
- **Human Gate**：Sean 以明確動作交給 Sean-KB（放進 repo／`_inbox/`、指示點名納入）即 selected；Sean 只是可存取（Reader 收藏、Drive 資料夾）或 AI 自找的資料只能作 transient research evidence，不永久 ingest。
- **Personal stance**：收錄來源不代表 Sean 同意其全部主張；個人 Principle／Decision 需明示依據。
- **Learning**：retrieval、generation effect、Feynman、Socratic 保留為主動學習方法，與 ingestion 分開。

## Ingestion

```text
selected → ingested → indexed → atomicized → integrated
```

AI 先理解整份文件與 heading hierarchy，再萃取可複用知識；不按頁拆卡。Source Tree 回答「原文在哪」，Knowledge Graph 回答「概念如何關聯」。每筆新知識可循 source_ref／source_evidence 回到來源版本與 section／page／evidence pointer。

新增卡、links／MOC 與既有卡的 Additive Update（只追加 frontmatter 或文末連結）由 AI 完成、lint、自審 diff 後直接 commit。改寫或刪除任何既有句子（Rewrite）、衝突 Sean personal principle、解析品質不足、重大矛盾、不確定合併／新建或個人立場歸因時走 exception review；其他內容繼續處理。術語見 [CONTEXT.md](CONTEXT.md)。

## 目錄

| 路徑 | 用途 |
|---|---|
| `_inbox/` | Sean 提供但尚未處理的素材暫存，不是人工消化 queue |
| `sources/` | Source metadata、external pointer、structure/index、處理進度與必要衍生資料 |
| `notes/` | 知識 SoT：concepts / cases / people / literature |
| `maps/` | 扁平 MOC／LYT 跨來源導航 |
| `wiki/` | AI 維護的敘事綜述；沿用目前 dormant 觸發條件 |
| `_system/` | schemas / prompts / scripts / validation / logs / exports |
| `_okf/` | 按需生成、可刪除重建的 OKF v0.1 bundle |
| `templates/` | atomic note 與 Source templates |
| `notion-pages/` | Notion 本地工作副本與歷史研究；不代表遠端同步完成 |

Raw PDF／錄音／大 binary／完整版權教材預設 external/local/Drive；repo 留可追溯索引與 derived knowledge。小型自有或可合法保存的原始文字可存 sources。Private 也不是 binary 倉庫。

## Agent 入口與驗證

- [CLAUDE.md](CLAUDE.md)／[AGENTS.md](AGENTS.md)：共同人機邊界、結構與安全規則。
- [Ingestion SOP](_system/prompts/maintenance-learning-loop.md)：主流程與 exception review。
- [Source lifecycle](_system/prompts/reader-kb-loop-state-machine.md)：狀態、恢復、舊資料相容。
- [Schema](_system/schemas/okf-note-schema.md)：Source Tree、provenance、立場歸因。
- [Content lint](_system/prompts/content-lint.md)：機械檢查＋AI 語意自審。
- [PMBA runbook](pmba/pmba-course-cycle-sop.md)：獨立的學習節奏與 ingestion adapter。
- [Case A–D 驗收](_system/validation/ai-first-ingestion.md)：重構的情境 walkthrough 與驗證限制。

```bash
uv run --with pyyaml python _system/scripts/lint_ingestion.py
uv run --with pyyaml python -m unittest discover -s _system/tests
```

目前是 agent-executed workflow，沒有背景服務或自動抓取器；Sean 交給 agent 執行後，AI 自行跑完安全範圍，不再逐卡等待人工。未來 PageIndex／Tree-based retrieval 可接 Source Tree node IDs／locators，本次不新增該 dependency。
