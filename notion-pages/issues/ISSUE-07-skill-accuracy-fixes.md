# ISSUE-07：防彈引擎 Skill 內容精準度修正

**Labels:** `priority:medium` `type:bug` `area:skill-防彈引擎`
**Status:** open

## Context

vault 盤點比對出防彈引擎 Skill 與原始 80 卡的三處內容出入（卡號 / 術語 / 用詞）。

## Items

### 1. 升級鏈對齊官方五階段（原判「術語混入」已被官方來源推翻）
- **現況**：心法 8 升級鏈寫「任務 → 永久 → 專案目錄 → 封存」。
- **初判（researcher，vault-only）**：「永久筆記」是 Zettelkasten 術語、vault 80 卡無此概念 → 建議刪除「永久」。
- **🔴 官方更正（websearch Esor 為準）**：防彈筆記是動態演化過程「收集箱 → 暫時的筆記 → 專案目標筆記 → 資源區知識與經驗筆記 → **永久任務筆記**」。**「永久任務筆記」是 Esor 原生概念，不是 Zettelkasten 滲入**——researcher 因只看 vault 二手萃取而誤判，官方來源直接推翻。
- **真正的問題（重新定位）**：
  - (a) Skill 升級鏈的**順序**與官方不一致：官方「永久任務筆記」在專案／資源之後，Skill 卻把「永久」放在「專案目錄」之前。
  - (b) Skill **漏了「資源區知識與經驗筆記」**這個階段。
  - (c) vault 卡片可能漏萃取「永久任務筆記」概念（vault gap，回頭補卡）。
- **修法**：升級鏈重寫對齊官方五階段 → 收集箱 → 暫時（任務）筆記 → 專案目標筆記 → 資源區知識/經驗筆記 → 永久任務筆記（→ 結案封存）。定稿前再以 Esor 官方原文校一次。
- **來源**：[防彈筆記法 - 博客來](https://www.books.com.tw/products/0010929249)、[電腦玩物 Esor](https://www.playpcesor.com/2022/08/blog-post_28.html)、[閱讀前哨站書評](https://readingoutpost.com/bulletproof/)

### 2. 重複引用
- **現況**：A008（整理得好不如寫下行動）同時被心法 2、心法 11 引用。
- **問題**：同一張卡被引兩次；且 A008 語意（批評過度整理）更貼心法 11。
- **修法**：移除心法 2 的 A008 引用，保留在心法 11。

### 3. 用詞微差（低）
- **現況**：心法 3 成果三問寫「限制風險」。
- **問題**：A007 原文「有何阻礙限制」更廣（阻礙＋限制），Skill 縮窄成「風險」。
- **修法**：視情況校正為「阻礙與限制」，不影響使用可緩。

## Acceptance Criteria

- [ ] 三項修正落地於本地 `../Skill-防彈引擎.md`
- [ ] 待回寫 Notion（用 MCP 外科手術，勿整頁覆寫）

## Source

盤點報告 Q4：`../../.subagent-output/diag-bulletproof-vault/final.md`
