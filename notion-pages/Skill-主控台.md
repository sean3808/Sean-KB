<!--
source: Notion page「主控台 ｜ Skill」(Notion AI Skill)
page_id: 1d2a0939-7f8f-414c-85ee-f2535708e207
parent: 技能庫 ｜ Skills（蒜頭） (96c4ee95-ab60-401b-a56e-50e3e750f6de)
url: https://app.notion.com/p/1d2a09397f8f414c85eef2535708e207
snapshot: 2026-05-29T03:15:46Z (fetched 2026-06-30)
note: 本地工作副本，唯讀快照。回寫用 Notion MCP 外科手術，勿整頁覆寫。
-->

# 🛰 主控台 ｜ Skill

> 🛰 **一句話定位**：對話開場時，給 Sean 一個 30 秒看懂全局的跨域鳥瞰面板。這對應防彈「掌控全局」的**選擇系統**——可鳥瞰的目標地圖。（A063）

## 觸發詞
`主控台`、`控台`、`面板`、`dashboard`、`開場`、`今天怎麼樣`、`現在狀態`

## 資料來源
- [工作紀錄庫](https://app.notion.com/p/2b893eac4a134aaab63d3ef6c7d1d0f0)（data source：collection://eadd62fa-d587-4823-8a8c-040d59cd6006）
- [碎片日誌](https://app.notion.com/p/2ebce39a284445dfb358ba183bb52368)（data source：collection://d5546bb0-5fd2-4e6b-88f0-d6f4e410a1b0）
- 必要時用搜尋／web 補 PMBA、家庭行程等跨頁資訊。

## 面板區塊（Sean 要「全部都要」）
1. 🎯 **今日焦點**：High 優先 ＋ 逾期／今日到期 ＋ 進行中精選（最多 3～5 項）
2. 💼 **工作進行中**：依交辦來源（經理／客戶／同事／自行）分群統計
3. 🗂 **專案管理頁**：Tags＝專案管理頁，列出仍在推進的主控頁
4. 🧩 **碎片待升級**：碎片日誌中 升級＝✓ 且 未完成
5. ⚠️ **阻礙與外部依賴**：等客戶／經理回覆者 → 我方最小跟進動作
6. 🎓 **學習與生活**：PMBA 關卡、近期家庭行程（如沖繩 6/4–6/8）

## 查詢配方
**進行中工作（依來源分群）**
```sql
SELECT url, "Name", "Tags", "Priority", "完成",
  "date:duedate:start" AS due, "母資料庫"
FROM "collection://eadd62fa-d587-4823-8a8c-040d59cd6006"
WHERE "完成" IS NULL OR "完成" NOT IN ('Done','Suspend')
ORDER BY "交辦時間" DESC
```

**碎片待升級**
```sql
SELECT url, "碎片", "升級", "Done", "建立時間"
FROM "collection://d5546bb0-5fd2-4e6b-88f0-d6f4e410a1b0"
WHERE ("Done" IS NULL OR "Done" = '__NO__')
  AND "升級" = '__YES__'
ORDER BY "建立時間" DESC
```

## 呈現規則
- 開門見山：先一句「今日全局判斷」，再展開區塊。
- 用精簡表格／條列，整體不超過一個螢幕。
- 高優先、逾期、卡關項目要醒目。
- **結尾一定給「現在最重要的一步」**（呼應防彈：選擇系統要能導向下一步行動）。
- 阻礙只列「我方可做的最小跟進」，不要把他人未完成寫成 Sean 的待辦。
