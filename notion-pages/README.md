# notion-pages — Notion 正典頁本地工作副本

Notion 上的專案重點無法在本地直接操作；這裡放**相關 Notion 頁的本地副本**，
讓 Claude Code 直接在 repo 內讀寫。repo 修訂不等於遠端已更新；只有明確交辦同步時才用 **Notion MCP** 定點回寫（不覆寫整頁），先讀遠端最新內容。

**本次 AI-first PR 只更新 repo**：`耐久決策入口.md`、`學習科學方法論.md` 是本地修訂待 review，沒有回寫 Notion。Ingestion 執行規則以 `../_system/prompts/maintenance-learning-loop.md` 為準；舊研究／issue 紀錄不是有效 Gate。

## 工作流

1. **下載**（批次）：`ntn pages get <page-id> > "<檔名>.md"`
2. **在本地編輯**：直接改下面的 `.md`
3. **另有明確同步交辦時，回寫 Notion**（外科手術）：Notion MCP `update_content`（`old_str`/`new_str` 定點替換），**不要整頁覆寫**

## 已追蹤頁（核心 + Backlog）

| 頁名 | Page ID | 本地檔 | URL |
|------|---------|--------|-----|
| 耐久決策入口（SSOT） | `afa08ead-8bbb-4f4c-a4f3-f296b631e102` | `耐久決策入口.md` | https://app.notion.com/p/afa08ead8bbb4f4ca4f3f296b631e102 |
| v1.2 方法論報告 | `38a59701-0d2c-8040-8866-dcdb6e54dc16` | `v1.2方法論報告.md` | https://app.notion.com/p/38a597010d2c80408866dcdb6e54dc16 |
| Backlog（封存） | `5deb4cdb-4ba5-417d-a722-a2002409b875` | `Backlog.md` | https://app.notion.com/p/5deb4cdb4ba5417da722a2002409b875 |
| 學習科學方法論（方法論層 SSOT） | `4089b0d6-f6da-4920-abee-4df3a28056c1` | `學習科學方法論.md` | https://app.notion.com/p/4089b0d6f6da4920abee4df3a28056c1 |
| My Notion AI（Notion AI System Prompt） | `2c559701-0d2c-80c5-b28b-cee4b59ecc2c` | `My-Notion-AI-System-Prompt.md` | https://app.notion.com/p/2c5597010d2c80c5b28bcee4b59ecc2c |
| Skill：防彈引擎（操作技能） | `e4e15c9d-2414-4e63-8a4e-0c22309c9fb4` | `Skill-防彈引擎.md` | https://app.notion.com/p/e4e15c9d24144e638a4e0c22309c9fb4 |
| Skill：主控台 | `1d2a0939-7f8f-414c-85ee-f2535708e207` | `Skill-主控台.md` | https://app.notion.com/p/1d2a09397f8f414c85eef2535708e207 |

> 本地副本是快照，不保證與 Notion 即時一致；要最新版重跑 `ntn pages get`。
