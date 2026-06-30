# ISSUE-04：明確化「框架優先」設計原則（AI ≠ 人類的避免過度整理）

**Labels:** `priority:low` `type:docs` `area:system-prompt`
**Status:** open

## Context

診斷初稿曾把「防彈引擎第 11 條：避免過度整理」當成跟 System Prompt 重框架（四步流程＋三類行動＋固定格式）的**矛盾**。

Sean 釐清——**這不是矛盾**：
- 防彈筆記法的對象**是人類**。對人類，「避免過度整理」是必要的，因為人類有惰性，過度設計會變成逃避行動的藉口。
- 交給 **AI** 則相反：**先提供框架反而有助於後面的發展，更符合「心法」的規範**。Sean 是讓 AI「在維持框架的前提下，把事情導向符合心法的方向」。

## Resolution

非 bug，是刻意設計。**「框架優先」對 AI 是 feature。**

## Proposal

在 System Prompt 或防彈引擎 Skill 加**一句設計註記**，明文這條原則，避免未來（人或 AI）誤判為「過度結構化」而想砍掉框架。

建議措辭方向：
> 防彈「避免過度整理」是治人類惰性的原則；本 Agent 為 AI，採「框架優先」——先給結構再導向心法方向，兩者不衝突。

落點候選：System Prompt §2.3（Block Formatting 協定旁）或防彈引擎 Skill 開頭定位句下。

## Acceptance Criteria

- [ ] 一句「框架優先」設計原則註記落地於三頁之一
- [ ] 註記明確區分「人類 / AI」兩種對象的不同處方
