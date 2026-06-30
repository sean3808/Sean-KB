# ISSUE-05：操作層 vs 方法論層 邊界釐清

**Labels:** `priority:medium` `type:discussion` `area:architecture`
**Status:** open

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
