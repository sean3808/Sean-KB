---
type: Source
title: Sean-KB 維護流程研究 — Karpathy LLM Wiki 引擎 + 跨源織網
description: 為「定期維護流程定案」蒐證；核心問題＝358 卡僅靠單一決策-MOC 串接，需跨源 note-to-note 直接連結 + MOC 互連。研究 claude-obsidian 等成熟實作，產出 adopt/adapt/avoid 與流程提案（未拍板）。
timestamp: 2026-06-26T00:00:00+08:00
status: seed
domain: ai
source_type: idea
---

# Sean-KB 維護流程研究（草案，未拍板）

> 狀態：研究結論已收斂為可執行 SOP → **`_system/prompts/maintenance-learning-loop.md`**（流程層 SSOT）。方法論 SSOT＝`notion-pages/學習科學方法論.md`。本檔保留為蒐證與收斂過程紀錄。

## 1. 本地問題側寫

- **目標**：讓 358 張卡（防彈80／商學院34／問解244）形成跨源知識網，而非各自在來源型 MOC 裡孤立。
- **症狀**：目前 MOC 與 MOC 之間幾乎無連結，只有一張 `決策-MOC` 把大家串起來；跨源 note-to-note 直接連結幾乎不存在（例：決策概念 ↔ 問題解決與批判思考 的卡）。
- **約束（canon）**：Claude Code + markdown repo；**永久排除 local LLM／Ollama**；向量庫／RAG 非主路徑；Sean curate／approve，AI draft／maintain structure。
- **判斷**：織網（cross-MOC / cross-note link）價值 > lint 維護機器（Sean 2026-06-26 定調）。

## 2. 研究路徑

- `gh api`：claude-obsidian repo 結構 + 5 個 skill 原始碼（wiki-ingest / wiki-lint / wiki-fold / methodology-modes-guide）。
- WebSearch：LYT 方法論（Nick Milo）、AI/LLM note-linking（2025–26）。
- 未用 subagent：單一高命中專案，直讀原碼最快。

## 3. 首選證據專案

| 專案 | ★ | 授權 | 活躍 | 契合 |
|------|---|------|------|------|
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 7,867 | MIT | 2026-05 | **同 stack**：Claude Code + Obsidian + 純 markdown + Karpathy LLM Wiki pattern |
| [brianpetro/obsidian-smart-connections](https://github.com/brianpetro/obsidian-smart-connections) | 5,215 | — | 2026-06 | 向量 embedding 語意關聯（canon 排除向量主路徑，僅參考） |
| [danielrosehill/Awesome-Obsidian-AI-Tools](https://github.com/danielrosehill/Awesome-Obsidian-AI-Tools) | 185 | — | 2025-12 | AI×Obsidian 工具總覽，備查 |

## 4. 關鍵機制發現（直接解「MOC 孤島」）

1. **LYT 模式 MOC template 三段**：`core-notes` / **`adjacent-MOCs`** / `open-questions`。`adjacent-MOCs` 即 MOC↔MOC 互連的標準位置；每張原子卡 frontmatter 帶 `mocs:` 欄。→ 直接是「決策-MOC 不再孤島」的解。
2. **跨源 note-to-note 連結靠 lint 揪、不靠向量**：`wiki-lint` 檢查項 #4「Missing pages」+ #5「**Missing cross-references**（某頁提到的實體但沒連）」＝ Claude 直讀的 link discovery 引擎。
3. **它本身就有 review gate**：lint「**Ask before auto-fixing anything**」、fold「dry-run by default」、PostToolUse hook auto-commit 留 git trail。與「Sean approve」一致。
4. **ingest 機制**：讀源 → 抽 entity/concept → 建/更新 8–15 頁 + cross-ref + log；LYT 模式下「filing 原子卡後**更新對應 MOC**，無則用 template 新建」。

## 5. Adopt / Adapt / Avoid

**Adopt（直接採）**
- LYT MOC template 的 `adjacent-MOCs` + `open-questions` 段；原子卡 `mocs:` frontmatter。
- lint 以 missing-pages / missing-cross-references 為主的「直讀揪連結」法。
- review gate 慣例：dry-run 預設、ask-before-fix、git diff trail。

**Adapt（改寫，呼應「不照抄」）**
- claude-obsidian ingest 是「全自動建頁、無 promote gate」→ Sean-KB **保留 promote 門禁**（Sean approve 才進 `notes/`）。
- 正典鐵律：`LLM proposes structure (links / MOC / lint) via Git diff; Sean approves knowledge (truth / merge / promote). AI never silently edits a promoted note's content.`

**Avoid（不採，canon 衝突）**
- ❌ ollama 向量 rerank / semantic tiling（DragonScale Mechanism 3）：local LLM + 向量主路徑皆排除。改用 Claude 直讀 + grep / backlink。

## 6. 流程提案（5 動作，Weave 升格；**未拍板**）

| 動作 | 機制 | AI-owned | Sean-owned |
|------|------|----------|-----------|
| 1. Weave 織網（核心） | LYT `adjacent-MOCs` 互連 MOC＋每卡 `mocs:`＋Claude 直讀提案跨源 link | 提案 link、填 adjacent-MOCs、補 `mocs:`（git diff） | 裁決連結、approve diff |
| 2. Lint 體檢（探照燈） | content lint 八項砍 sensitivity，重 #4/#5 → `_system/lint-reports/` | 跑 lint、出報告、ask before fix | 看報告、裁處置 |
| 3. Ingest 納入 | `_inbox/` → Claude triage 草擬 | 分類、產 draft | promote 判斷 |
| 4. Query 取用 | 用既有 wiki + `_okf` 答，不重跑 RAG | 直讀回答 | 提問決策 |
| 5.(選) Fold 壓縮 | log rollup（extractive 不發明） | 草擬 fold | 視需要 |

## 6.5 收斂（2026-06-26 對話後，正典化進 SOP）

§6 的「5 動作 + 逐條 approve」被以下三點修正、收斂成 `maintenance-learning-loop.md`：

1. **兩篇文章再檢視**（陳聖璋〈AI輔助高效學習法〉〈AI 把解釋變便宜後父母該拿回什麼〉，本地 `art_*` 已讀）：共同母題＝AI 讓「解釋層」變便宜→價值上移到診斷/判斷/選題；**不可用便宜層取代昂貴層**（不用 AI 統整取代卡片）。
2. **沒有標準教材**：成人研究無教材，對照對象＝多重 source（原文＋既有卡網＋真實經驗＋反方＋費曼斷點）。織網的真實機制＝**診斷場**（蘇格拉底/費曼/steelman/案例遷移/source 對照），不是查表。
3. **生成效應 + 不手工串線**（Sean 兩條硬約束）：逐條 approve link diff＝高阻力，廢除。改為 **AI 產候選連結與診斷場；Sean 先生成回應→AI 補洞→Sean 只審高價值連結**。判斷活在會內化的對話裡，不在機械核可。

三層框架（工具/流程/方法論）＋兩護欄（合意困難/生成效應）已寫入 SOP，方法論 SSOT＝`notion-pages/學習科學方法論.md`。

## 7. 來源

- [claude-obsidian repo](https://github.com/AgriciDaniel/claude-obsidian)（skills/wiki-ingest・wiki-lint・wiki-fold、docs/methodology-modes-guide.md）
- [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Nick Milo — forming relationships between notes](https://medium.com/@nickmilo22/in-what-ways-can-we-form-useful-relationships-between-notes-9b9ec46973c6)
- [LYT MOCs Overview](https://notes.linkingyourthinking.com/Cards/MOCs+Overview)
- v1.2 方法論報告 §3.3（本地 `notion-pages/v1.2方法論報告.md`）
