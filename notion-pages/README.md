# notion-pages — Notion 正典頁本地工作副本

Notion 上的專案重點無法在本地直接操作；這裡放**相關 Notion 頁的本地副本**，
讓 Claude Code 直接在 repo 內讀寫。改完後用 **Notion MCP** 回去做外科手術式修改（不覆寫整頁）。

## 工作流

1. **下載**（批次）：`ntn pages get <page-id> > "<檔名>.md"`
2. **在本地編輯**：直接改下面的 `.md`
3. **回寫 Notion**（外科手術）：Notion MCP `update_content`（`old_str`/`new_str` 定點替換），**不要整頁覆寫**

## 已追蹤頁（核心 + Backlog）

| 頁名 | Page ID | 本地檔 | URL |
|------|---------|--------|-----|
| 耐久決策入口（SSOT） | `afa08ead-8bbb-4f4c-a4f3-f296b631e102` | `耐久決策入口.md` | https://app.notion.com/p/afa08ead8bbb4f4ca4f3f296b631e102 |
| v1.2 方法論報告 | `38a59701-0d2c-8040-8866-dcdb6e54dc16` | `v1.2方法論報告.md` | https://app.notion.com/p/38a597010d2c80408866dcdb6e54dc16 |
| Backlog（封存） | `5deb4cdb-4ba5-417d-a722-a2002409b875` | `Backlog.md` | https://app.notion.com/p/5deb4cdb4ba5417da722a2002409b875 |
| 學習科學方法論（方法論層 SSOT） | `4089b0d6-f6da-4920-abee-4df3a28056c1` | `學習科學方法論.md` | https://app.notion.com/p/4089b0d6f6da4920abee4df3a28056c1 |

> 本地副本是快照，不保證與 Notion 即時一致；要最新版重跑 `ntn pages get`。
