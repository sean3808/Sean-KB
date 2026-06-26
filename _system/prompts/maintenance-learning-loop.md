---
type: Playbook
title: Sean-KB 維護＝學習迴圈 SOP
description: 把學習科學三層框架落地成 Sean-KB 的可執行維護流程。核心：維護迴圈就是學習迴圈；AI 只去無益摩擦、產候選連結與診斷場，Sean 做高價值判斷與內化。對應 issue #4（工具層）/#5（流程層）/ Notion 學習科學方法論（方法論層）。
timestamp: 2026-06-26T00:00:00+08:00
status: growing
domain: ai
---

# Sean-KB 維護＝學習迴圈 SOP

> 三層定位：**工具層**＝Readwise CLI/Skills/MCP（issue #4）｜**流程層**＝本檔（issue #5）｜**方法論層**＝Notion「學習科學方法論｜個人通用學習流程框架」（`notion-pages/學習科學方法論.md`，方法論 SSOT，理由回溯該頁）。Reader input 狀態機與 output ports 見 `_system/prompts/reader-kb-loop-state-machine.md`。

## 0. 一句話

**維護知識庫的迴圈，就是學習的迴圈。** 不是「AI 摘要工廠」，是「AI 建診斷場、Sean 做判斷與內化」。

Sean-KB 的維護不是整理資料，而是讓 input 經過診斷場後產生火花；Sean-KB 的應用不是查筆記，而是把火花導向 decision、writing、case、playbook。

## 1. 鐵律（不可違反）

```
AI 產候選連結與診斷場；Sean 做高價值判斷與內化。
人不手工拉所有線；人只審哪些線真的有意義。
連結預設可疑，回 source 判斷（盡信書不如無書）。
```

兩條護欄（全程監督，來自方法論層第一層通則）：
- **合意困難 Desirable Difficulties**：學習當下的摩擦換長期記憶與遷移。每個自動化先自問「這是**無益摩擦**還是**學習必要摩擦**？」AI 只去前者。
  - **診斷場觸發判準＝基礎穩不穩**：「習得感」的可靠度 ∝ 既有基礎的有無與正確性。**基礎穩** → 新答案卡進去、能自驗 → 快答即可，診斷場是無益摩擦（別硬上）；**無基礎／基礎可疑** → 同樣「拿到答案＋覺得學會」是最危險的幻覺 → **此時才跑診斷場**（有益摩擦）。盲點測試：你能不能把它放上既有基礎、且會不會察覺它錯了？不能 → 基礎不穩。
- **生成效應 Generation Effect**：所有 AI 互動鐵則——**Sean 先講／先答／先重述，AI 才能補與改**。

平衡護欄（本專案，防過度優化）：
- **維護沒在產生學習就是跑偏**：某個維護動作若沒帶來學習／內化，它就退化成「為優化而優化」（最大 PKM 失敗模式：花在完善系統 > 用系統），該停。「維護＝學習」框架天然擋這條，但寫死以防漂移。

## 2. 人機分工（可／不可自動化）

| AI 可全自動（無益摩擦＋結構層） | Sean 不可外包（必要摩擦＋知識判斷） |
|---|---|
| 搜尋 source、找相似、初步分類 | 判斷文章對我的真實價值 |
| 補背景知識、產問題清單、產反方追問（steelman） | 能不能自己說出核心論點（費曼） |
| 建初稿 scaffold、產**候選**連結、normalize frontmatter | 能不能舉自己的真實案例（案例遷移） |
| 整理診斷結果成**可審核結構**、跑 lint 出報告 | 能不能反駁／修正作者觀點 |
| 偵測 orphan / 矛盾 / 缺卡 / 缺連結 | 決定哪些值得沉澱、最終價值排序 |

> AI 的產出是用來**逼出漏洞、創造情境、給候選**，不是用來**統整取代你的卡片**。

## 3. 診斷場（織網的真實機制，取代「逐條 approve link diff」）

沒有標準教材時，對照對象是**多重 source**：原始 source＋既有卡網＋真實經驗＋反方觀點＋費曼重述暴露的斷點。

診斷方法（按需召喚）：
- **蘇格拉底追問**：暴露假設、跳躍、矛盾、未定義概念
- **費曼重述**：要 Sean 用自己的話講，看哪裡講不順
- **反方／steelman**：AI 建更強反方，測 Sean 是否只接受漂亮說法
- **案例遷移**：把概念套到出口物流／PMBA／IT 自動化／育兒／家庭溝通
- **source 對照**：回原文檢查過度詮釋／漏讀／誤讀

連結是診斷的**副產品**：火花處（通過診斷的候選）才沉澱成 wikilink；AI 串線，Sean 只審高價值的。

## 3.1 連結分兩層（反「為了連結而連結」護欄）

連結不是越多越好——**假連結比沒連結更糟**，它把真連結淹掉（link inflation）。分兩層處理：

| 層 | 機制 | 標準 |
|---|---|---|
| **導航層** | tag／共用 MOC／MOC↔MOC（`adjacent-MOCs`） | categorical，便宜，**可大方連**（解 MOC 孤島） |
| **知識層** | note↔note wikilink | **必須 earned，禁止為了連結而連結** |

**earned 測試**：走這條連結，會不會產生「單看其中一張卡得不到」的理解？會＝真連結；只是「兩張都在講 X」＝那是 **tag／MOC 的 categorical 關係，用 tag/MOC，不用 wikilink**。

**earned 連結要帶「一句 why」**：沉澱 note↔note 時，連結旁寫一句「為什麼連」（那道火花本身）。裸 `[[link]]` 沒 context＝沒理由跟隨＝低價值（zettelkasten.de〈Backlinks are bad links〉）。

- 多數卡是**主題內**、沒有跨域連結，**這完全正常**——concept 不一定要連既有 concept。
- 跨域 note↔note 連結**稀少且珍貴**，等它在診斷中自己冒出來，不製造。
- 已內化、無新增知識的想法 → **不必寫卡**（vault 只收值得反覆檢索重組的，不做完整性練習）。
- 這也是為何選「對話驅動」而非「向量／批次」：向量給 categorical 相似度，會大量製造假 note↔note 連結。

## 4. 主幹流程（對應方法論第二層：前／中／後／跨期）

| 時機 | 方法 | Sean-KB 落地動作 |
|---|---|---|
| 前 | Elaboration 精緻化提問 | 碰新 source（Reader / sources/）先問「為什麼？跟既有卡怎麼連？」 |
| 中 | Self-explanation＋Socratic | AI 開診斷場，Sean 先重述、被追問暴露漏洞 |
| 後(24h) | Retrieval 主動提取 | 不看原文先寫記得的 → AI 補漏（記憶主幹） |
| 後 | 費曼／教回去 | Sean 講給沒背景的人聽，斷點處 = 缺卡/缺連結訊號 |
| 後(結案) | Reflection / KPT | 沉澱進 `notes/`；KPT 覆盤（防彈筆記法引擎） |
| 跨期 | Spacing＋Interleaving | 隔天/週/月複習；不同主題混練提升遷移 |

第三層（特定狀況召喚）：交件/重大判斷前→steelman；複雜決策→個案法；卡關創新→第一性原理。

## 5. Reader Library workflow（issue #5 / #6 正確版）

```
Reader source
→ AI 初篩 + 提候選觀點與候選連結
→ Sean 先用費曼/蘇格拉底回應（生成效應）
→ AI 診斷盲點、矛盾、未連結處
→ AI 整理高價值候選連結
→ Sean 只審高價值連結 + 判斷是否沉澱
→ Obsidian / Sean-KB 沉澱（promote gate）
→ 輸出 kb_loop_result（maintenance + output）
```

**禁止退化**為 `Reader → AI 摘要 → Obsidian`（看似有知識庫、其實沒內化）。

Reader item 不必每次都 promote，但每次診斷場結束都要留下 `current_state`、`next_state`、`why_not_promoted_yet`、`output_target`，讓 input 可續跑、可 review、可應用。完整狀態機與 YAML contract 見 `_system/prompts/reader-kb-loop-state-machine.md`。

## 5.1 Output target（應用出口）

每個 promote candidate 要盡量指向至少一個 output target：

| Output target | 用途 |
|---|---|
| `decision` | 工具選型、流程判斷、工作與生活決策 |
| `writing` | 文章、報告、PMBA 作業、研究輸出 |
| `case` | 工作事件、PMBA、家庭或職涯案例 |
| `playbook` | 可重跑的 SOP / checklist / skill |
| `teaching` | 對家人、同事、讀者說明某個概念 |
| `not_yet` | 暫時只是候選概念，須說明為何值得保留 |

## 6. 與既有資產銜接

- **底層引擎**：防彈筆記法（成果定義／責任邊界／阻礙→對策／KPT）｜結構：Zettelkasten 扁平＋LYT MOC（MOC 互連用 `adjacent-MOCs`、每 MOC 補 `open-questions`）。
- **存量 358 卡**：不批次硬連。連結跟著學習軌跡長——Sean 學/碰某主題時，AI 拉相關存量卡進診斷場順手串；背景掃出的候選只用「火花提問」一句話確認，不丟 diff 清單。
- **工具**：Readwise CLI（read-only，issue #4 已通）／`notion-pages/`（Notion 正典本地副本，MCP 外科回寫）／`_okf`（需要時現生）。
- **狀態與應用**：Reader input 狀態機與 `/kb-loop` 收尾輸出由 `_system/prompts/reader-kb-loop-state-machine.md` 管理；dashboard 待 #7 流程穩定後再做。

## 7. 觸發時機（先定流程、不建排程）

本檔是**流程契約**，非排程。節奏先當文字守則：碰新 source 即跑前→中；累積後跑後段；跨期複習與 lint 體檢偶發手動觸發。排程化（Task Scheduler）等流程穩了再議。

> 方法論 SSOT 與完整理由：`notion-pages/學習科學方法論.md`。研究蒐證：`_system/research/2026-06-26-llm-wiki-maintenance-research.md`。
