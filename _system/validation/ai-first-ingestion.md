# AI-first ingestion 重構驗證

日期：2026-09-29。範圍：architecture、workflow、schema、prompts、repo-local skills 與可執行 consistency checks。這是 agent 執行契約，不是新建 PDF parser、背景 ingestion service 或自動 crawler。

## 決策與改動範圍

舊架構把 Sean 的消化、診斷、逐卡 promote 和 link approve 放在 ingestion 路徑上。新架構只保留 Source Selection：Sean 主動指定／提供／匯入／要求納入 Sean-KB，即 approved source；後續 AI 自行完成，只有真正例外才詢問。

| 範圍 | 檔案 | 改變 |
|---|---|---|
| 入口與代理規則 | README.md、CLAUDE.md、AGENTS.md、session-continuity.md | Human-curated, AI-processed；冷啟動不恢復舊 Gate |
| 共用 ingestion | maintenance-learning-loop.md、reader-kb-loop-state-machine.md、kb-loop skill | 五階段 lifecycle、semantic atomicity、去重、earned links、MOC、恢復與 exception |
| 結構與 provenance | okf-note-schema.md、兩份 templates | Source Tree／quality、配對 evidence、版本與定位、claim attribution |
| PMBA／個人學習 | pmba-compile.md、pmba-cycle skill、三份 PMBA 文件、learning-trace issue template | 教材直接 ingestion；retrieval／generation／Feynman／Socratic 獨立保留 |
| 相容性與歷史 | notion-pages 本地副本、研究報告、財務 Lit／MOC、wiki/index.md | 失效 Gate 標示／修正；保留歷史事實、遠端操作邊界與 wiki dormant 條件 |
| 檢查與交換 | content-lint.md、lint_ingestion.py、test_ingestion.py、兩個 exporter 與 okf-exporter.md | 唯讀檢查、契約回歸、跨平台路徑與 provenance fragment 保留 |
| 既有 YAML 修正 | sources/The Bottom Line 商學院/學員實作 GOOGLE.md | 僅把含冒號的 title／description 加引號，使 YAML 可解析 |

全 repo 檢索 generation effect、Sean first／review、promote、candidate、digest、internalize、Reader、AI summary、source、raw、atomic、link approval 及中文對應詞；區分有效 agent 規則、學習方法與歷史紀錄。既有卡中的學習科學論述沒有被當成 ingestion 規則刪除。

## Case A–D

驗證由規則走查、兩個 skills 的獨立唯讀情境演練與 synthetic contract tests 組成。**本次沒有提供實際 120 頁 PDF 或文章供端到端 ingestion；不宣稱已完成真實來源的解析／語意品質驗證。**

| Case | 具體執行路徑 | 驗證結果 |
|---|---|---|
| A：120 頁 PMBA 教材，Sean 不再操作 | 以實際交辦記錄 selected → 可讀來源 ingested → 全篇結構／章節覆蓋 indexed → semantic atomic notes／既有卡增補 atomicized → dedup、earned links、MOC、lint 後 integrated | 流程與契約通過；不查日期、不等摘要／費曼／reviewed、不按頁配額拆卡；無 waiting_for_sean backlog |
| B：Sean 說文章符合核心價值並要求納入 | 該句即 selection_evidence；短文可一個 tree root，以 heading／anchor 定位，完成相同 pipeline | 流程與契約通過；不用 PDF 頁碼也可追溯；只支持 Sean 的概括性選擇，不把每項作者主張改成 Sean Principle |
| C：AI 自找文章，未要求入庫 | 可作本次 transient research evidence；不寫持久 Source／notes／MOC／版本化 inbox，也不藉增補既有卡繞過 Gate | 流程演練拒絕永久 ingest；契約測試拒絕 selected_by: ai／web-research。linter 無法識破偽造的 Sean 指示，仍需 agent 核對真實對話 |
| D：新書 A 與明示 Sean Principle not-A 衝突 | 核對語境後保存來源 A、保留原則 not-A、附 contradiction／comparison context；記一筆 open exception，只停改寫 Sean 原則 | 流程演練通過；safe integration 可 integrated 並保留 open exception；契約測試要求 claim_origin: sean 有 stance_evidence，不替 Sean 調和立場 |

Independent skill dry-run 結果：沒有阻塞四情境的規則矛盾。尤其 B 不因個人立場尚未確認而卡住文章入庫；D 不因一個 exception 阻塞整本書。

## 執行結果

| 驗證 | 結果 |
|---|---|
| `python -m unittest discover -s _system/tests -v` | 12 tests passed |
| `python _system/scripts/lint_ingestion.py` | 394 份知識／來源／導航文件，0 hard errors；394 份 legacy metadata 的彙總 migration warning |
| `python _system/scripts/export_anki.py` | 原有檢查通過，3 張 Q/A cards；格式與既有匯出相容 |
| `python _system/scripts/okf_export_concepts.py --sample 5` | 5/5 export 通過，0 unresolved body links；臨時產物清除，不 commit bundle |
| 兩個 repo-local skills 的 quick_validate | kb-loop、pmba-cycle 均通過 |
| `git diff --check` 與完整 diff 自審 | 通過；沒有批次重命名／搬卡／更動 reviewed 值 |

12 項測試涵蓋：selected 教材無學習門檻、無頁碼文章、非 Sean selection 拒絕、個人立場 evidence、每個來源有配對 evidence、tree cycle／未知節點、非法 page range／dangling source、階段所需 quality、legacy 相容、duplicate ID、OKF unknown fields／evidence fragment 與 Anki Q/A。

機械 lint 只檢查檔案結構與欄位，不證明來源真實性、Sean 授權、語意原子性、OCR／table 正確性、外部 pointer 存取或 heading anchor 存在。這些由 content-lint 的來源核對、語意自審與 exception 契約處理。

## Backwards compatibility

- 保留 Obsidian knowledge SoT、Zettelkasten、LYT／MOC、flat concepts、earned links、OKF、Notion control plane 與 Git。
- 不改既有 note ID、路徑、檔名與 reviewed 值；舊資料仍是正式知識，新 provenance/lifecycle 在實質處理時依證據補足，不捏造資料或批次翻旗標。
- 保留 maintenance-learning-loop／Reader 檔案路徑；「promote run」別名已移除（見下方 review 修正）。
- reviewed／Sean 學習進度不影響 export；OKF 最低 consumer contract 未加強，unknown fields 保留。
- concept-only OKF exporter 不封裝整份 Source Tree。現有 bundle 的來源定位仍依賴原 vault／external source；完整 references packaging 留給 exporter workflow 按需處理。
- Notion 文件只改 repo 本地副本（review 修正後已改以遠端最新版為基底）；未回寫遠端、未重貼 ChatGPT Project Instructions、未改遠端 issue 狀態。

## Risks / trade-offs 與未來接口

- AI 正式寫入提升吞吐量，也使來源忠實度、去重與立場歸因更依賴 agent 判斷。以 paired evidence、版本、完整 diff、Git 回復能力及例外審核控制風險，並不宣稱能消除錯誤。
- legacy warning 是逐步遷移資訊，不是 review queue；現有卡的缺失 provenance 不會在這次憑空補齊。
- Source Tree 與 Knowledge Graph 分工：前者保留原文結構／定位，後者是跨來源關係。MOC 不再被每份來源的目錄割裂。
- 外部來源可能失效或無存取權，記錄 locator 與版本仍需實際可讀來源。大 PDF／錄音／完整版權教材留外部；Private 不使 repo 適合所有 binary。
- 未來 PageIndex／tree retrieval 可把 parser 輸出映射至 source_tree.node_id／parent_id／locator，並由 source_evidence.node_id 接 graph；需保留版本與穩定 identity、驗證新 parser 後再接入。本次未新增 PageIndex、vector DB 或自動化服務 dependency。
- Source Selection 永遠不能由 retrieval adapter 或 web research 自動繞過。Sean 選來源不等於採納所有 normative claims。

## 2026-09-29 Sean review 修正（grill session）

| 修正 | 內容 |
|---|---|
| 安全線 | Additive Update（只加 frontmatter／文末連結）直接 commit；Rewrite（改寫／刪除既有句子）先給 Sean 看 diff，不在場記為 Source Exception；取代原「高價值 note」模糊門檻 |
| 正典分工 | 撤回「repo 規則高於 Notion 快照」；決策 SSOT 仍是 Notion，repo 只管知識與流程 |
| Notion 本地副本 | 原 PR 改在過期副本上（漏遠端 2026/06/26、06/27、07/06 三筆決策）；改以遠端最新版為基底，決策只追加、被取代原文保留並標註 |
| Selected Source | 限「明確交給 KB 的動作」；可存取（Reader 收藏、Drive、PLAUD app）不算；ChatGPT 二手素材的歸因規則 |
| promote 別名 | 移除 skill 觸發詞與流程文件中的相容別名 |
| PMBA | 執行層以 2026-08-28 v2 為準；移除生成效應保護區；Gold 不含 Obsidian 卡；完整改寫留 issue #18 |
| 卡片盒原則 | 忠實轉述＋Sean 加工只進 Sean 立場卡；dedup 只合併相同主張；多來源卡前綴＝首次入庫命名空間；「章節 → 卡片」目錄只在 Source Navigation 維護一份 |
| 指令 | Python 一律 `uv run`（需 PyYAML 者加 `--with pyyaml`） |
| 術語 | 新增 `CONTEXT.md` |

修正後驗證紀錄在該次 commit 訊息；上方「執行結果」表為原 PR 當時紀錄。


## 2026-09-30 首次真實素材驗收（Case A 型：大局勢 GT001）

Sean 交三檔（圖片型簡報 13 頁、PLAUD 逐字稿、PLAUD 強化筆記）後不再操作；一路 selected → integrated，產出 14 張卡＋新領域 MOC，commit `0ea0acf`。來源紀錄：`sources/pmba/115-1_大局勢_W01_20260907_導論.md`（Integration 段有覆蓋、未拆卡理由與驗證）。

| 驗證 | 結果 |
|---|---|
| `uv run --with pyyaml python _system/scripts/lint_ingestion.py` | 446 份，0 hard errors |
| `uv run --with pyyaml python -m unittest discover -s _system/tests` | 17 tests OK |
| `uv run python _system/scripts/export_anki.py` | check() passed，17 張（新增 14） |

真實素材暴露、已寫回文件的缺口：圖片型 PDF 無法直接讀（→ `maintenance-learning-loop.md` §5 轉圖指令）、多檔 Source 與逐字稿 pointer 格式（→ schema Source Tree contract）、一堂課素材包的存放與證據角色、後續週次的命名空間與種子卡深化、題卡格式契約（→ `pmba-compile.md`）。Case B–D 仍無真實素材。