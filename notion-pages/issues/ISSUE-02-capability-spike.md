# ISSUE-02：實證 Notion AI 實際 DB 操作能力

**Labels:** `priority:high` `type:spike` `area:capability`
**Status:** open
**Blocks:** ISSUE-01

## Context

主控台 Skill 寫了具體的 collection query SQL，假設 Notion AI 能查、能寫 DB。**這個假設從未被驗證**，卻是 operator/advisor 定位（ISSUE-01）的地基。

## Task

對兩個核心 data source 跑最小實證，產出能力矩陣：
- 工作紀錄庫：`collection://eadd62fa-d587-4823-8a8c-040d59cd6006`
- 碎片日誌：`collection://d5546bb0-5fd2-4e6b-88f0-d6f4e410a1b0`

量四個動作層級（每項給「能／不能／證據」）：
1. **查詢**：能否跑 collection query 撈列
2. **新增**：能否在 DB 內新增一頁（帶 property）
3. **改 property**：能否改既有頁的單一欄位值（如勾 checkbox、設 duedate）
4. **改 schema**：能否改欄位定義／視圖

## 重要區分（兩條能力線分開量）

| 線 | 問的是 | 工具 |
|---|---|---|
| **線 A：Notion 原生 AI agent** | Notion 平台上那個 AI 在對話中實際能執行什麼動作 | Notion AI 本身（需 Sean 手動測或查官方能力） |
| **線 B：API / MCP 程式化** | 我們透過 `ntn` / Notion MCP 能做什麼 | 本 session 可直接跑 |

operator 最終設計 = 線 B 可程式化的部分 ＋ 線 A 平台允許的部分。**兩條混淆會誤判定位。**

## Acceptance Criteria

- [ ] 一張能力矩陣：動作（4 級）× 線（A/B）× 能否 × 證據
- [ ] 標明哪些是「實測過」、哪些是「查官方文件得知」、哪些「未能驗證」

## Notes

- 線 B 可由本 session 直接做（先跑線 B，成本最低、最快給 ISSUE-01 一半的事實）。
- 線 A 可能需 Sean 在 Notion 裡實際喚起 Notion AI 試一個寫入動作回報。
