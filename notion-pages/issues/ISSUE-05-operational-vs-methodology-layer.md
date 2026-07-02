# ISSUE-05：操作層 vs 方法論層 邊界釐清

**Labels:** `priority:medium` `type:discussion` `area:architecture`
**Status:** done（2026-07-02，以 gh issue #13 實證收斂）

## Context

診斷初稿曾建議：把 2026-06-26 建立的「學習科學方法論層」註冊進 Notion AI 技能庫（§5B）。

Sean 否決並指出關鍵：**方法論層不完全適用 Notion AI，因為 Notion AI 負責的是「操作層」。這需要拆出來細談。**

## Problem

兩層職責邊界沒畫清：
- 哪些屬**操作層**（Notion AI 該管：任務、碎片、DB 操作、開場面板）？
- 哪些屬**方法論層**（學習科學、診斷式學習——可能屬 Sean-KB / kb-loop / Obsidian 側）？
- 學習科學方法論該不該、以何種形式接觸 Notion AI？

## Open Questions（本 issue 先收斂討論，不直接改 prompt）

1. 「操作層」的明確定義與邊界是什麼？（Notion AI 的責任天花板在哪）
2. 方法論層的 SSOT 在 Obsidian 還是 Notion？兩者如何分工？
3. 兩層如何「互相引用而不互相混入」？（避免把方法論硬塞進操作層 prompt）
4. 是否存在「操作層需要的最小方法論」——即少數方法論原則確實該下放到 Notion AI？

## Acceptance Criteria

- [ ] 一份「操作層 / 方法論層」邊界定義
- [ ] 一條判準：Notion AI 該 / 不該載入哪類方法論
- [ ] （若有）操作層需內建的最小方法論清單

## Notes

此 issue 的產出會回頭影響 ISSUE-01（operator 定位）與 ISSUE-06（要不要把方法論型的防彈卡放進 Skill）。

---

## Resolution（2026-07-02 定讞）

**收斂方式**：不走抽象討論——財務管理 Day 1 的完整迴圈（gh issue #13，T+0/T+1 retrieval → PLAUD 校正 → 候審 → promote）實際跑出了邊界，以下為實證定案。

### 邊界定義

| 層 | SSOT | 執行者 | 管什麼 |
|---|---|---|---|
| **操作層** | Notion 主控頁／課程 DB | Notion AI（蒜頭） | 任務、課表、狀態、deadline、複習排程、DB 操作、開場面板——「現在該推什麼」 |
| **方法論層** | Notion「學習科學方法論」頁（理論）＋ `_system/prompts/maintenance-learning-loop.md`（流程） | ChatGPT Project（課後轉化／診斷場）＋ Claude Code（promote gate＋織網） | 學習流程怎麼設計、知識怎麼沉澱——「東西怎麼進腦、怎麼進 vault」 |

### 判準（Notion AI 該／不該載入哪類方法論）

> **只載入「會改變其操作行為」的最小方法論；解釋性、流程設計性的方法論一律不進 prompt。**

### 操作層需內建的最小方法論清單

1. **防彈 11 心法**（已內建於防彈引擎 Skill）——直接塑造任務梳理行為。
2. **生成效應的操作層投影一條**：蒜頭不代寫 retrieval 答案、不在 Sean 提取前餵摘要。
3. 其餘（診斷場、合意困難判準、promote gate）留方法論層，Notion 只保存**指標**（learning trace 的 issue URL、下次複習日）。

### 兩層互引不互混

- Notion 課程列 → issue URL＋複習日（指標，不存內容）。
- Obsidian 卡片 frontmatter → `notion_refs` 回指主控台（雙向異步引用，維持既有定案）。

### Acceptance Criteria

- [x] 「操作層 / 方法論層」邊界定義（上表）
- [x] 判準一條（最小方法論原則）
- [x] 操作層需內建的最小方法論清單（3 項）

完整流程落地版見 `_system/prompts/pmba-post-class-learning-trace.md`。此 resolution 同時給出 ISSUE-06 的策展參照系：防彈模組入 Skill 的門檻＝「會改變操作行為」，與本判準同一條。
