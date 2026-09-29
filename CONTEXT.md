# Sean-KB

Sean 的長期個人知識庫：Sean 選來源，AI 把來源處理成可反覆檢索與重組的知識。本檔只收術語，不收流程與實作。

## 兩條流程

**Knowledge Ingestion（知識入庫）**：
把 Selected Source 處理成正式知識（卡、連結、MOC）的流程；由 AI 執行，不以 Sean 是否學過為前提。
_Avoid_: promote run、promote gate、消化

**Personal Learning（個人學習）**：
Sean 主動進行的 retrieval、費曼、蘇格拉底追問等學習活動；只衡量 Sean 的內化，不決定內容能否入庫。
_Avoid_: 診斷場當入庫前置、kb-candidate

## 來源

**Selected Source（已選定來源）**：
Sean 以明確動作交給 Sean-KB 的素材——放進 repo、丟進 `_inbox/`、或指示點名要納入；包含 Sean 的課堂錄音逐字稿與 Sean 自寫的 Notion 頁。
_Avoid_: approved source、候選素材

**Transient Evidence（暫時性研究證據）**：
Sean 可存取但未明確交給 Sean-KB 的素材（Reader 標星、Drive 資料夾），或 AI 自行找到的資料；只能在當次任務中引用，不得持久寫入 vault。
_Avoid_: inbox 素材、待審候選

**Source Note（來源筆記）**：
一個 Selected Source 在 vault 內的唯一代表：記錄原文位置、章節結構（Source Tree），並以可點的「章節 → 卡片」目錄提供該來源的瀏覽入口。短文的 Source Note 即書目；需跨章綜述時才另建 Literature note。
_Avoid_: 來源 MOC、source 索引卡

## 知識圖

**Map（MOC）**：
跨來源、按概念組織的導航筆記；新 MOC 不為單一來源而建。
_Avoid_: 來源目錄、章節清單

**Sean Stance（Sean 立場）**：
Sean 明示的個人原則、判斷或 reflection，附可回溯證據；vault 中唯一能挑戰 Sean 舊想法的知識，其餘卡皆為來源的忠實轉述或標明的 AI 推論。
_Avoid_: 用自己的話寫、Sean believes

## 修改既有知識

**Additive Update（追加）**：
對既有卡只追加 frontmatter（來源、別名、MOC 歸屬）或在文末追加連結；不改動任何既有句子。AI 可直接 commit。
_Avoid_: 非破壞性修訂、reconcile

**Rewrite（改寫）**：
改寫或刪除既有卡的任何既有句子，或刪除整張卡；必須先讓 Sean 看過 diff。
_Avoid_: 大改、高價值修改

**Exception（例外）**：
AI 無法安全自行完成、需 Sean 判斷的單一 mutation，含所有待批准的 Rewrite；記在該 Source 的 Exceptions，只暫停這一項，其餘照常完成。
_Avoid_: review queue、候審、kb-candidate
