# ISSUE-01：Notion AI 定位 — operator vs advisor

**Labels:** `priority:high` `type:decision` `area:system-prompt`
**Status:** done（Sean 放行 2026-06-30，已上傳 Notion）
**Depends on:** ISSUE-02 — 由官方文件取代實證（Sean = Business + 3.0）
**Blocks:** ISSUE-06

> **決議（2026-06-30）**：選方案 C（按官方實測能力重畫邊界）。Notion 3.0 Agent（全平台狀態）+ Business 確認 Notion AI 本就是 operator。§2.1-7 由「尊重能力邊界（只給文字稿/教手動）」改寫為「能力邊界（operator）」：**能**建改頁面/欄位/屬性/關聯/視圖/公式、檔案灌 DB、分析摘要；**不能**建 DB 自動化/模板/rollup/按鈕、改權限/成員/帳單、留言。依據官方 [Notion Agent help](https://www.notion.com/help/notion-agent)。已 commit + 回寫 Notion。殘留：公式那條官方自相矛盾，可隨手實證（不擋本 issue）。

## Context

Sean 對 Notion AI 的核心定位：**「代我操控資料庫」**——這是一個 operator 期望。

但現行 System Prompt §2.1-7「尊重能力邊界」把它鎖成 advisor：
- **不能**：改 schema／欄位／視圖、調權限／成員／方案、建模板／自動化／按鈕
- **能**：設計欄位／模板的「文字規格」給 Sean 貼上去、提供「手動操作步驟」教 Sean 改

通讀全份，真正的 DB 寫入動作只有兩個：§3.2 補 `duedate`、§3B 新增碎片。其餘皆為「輸出思考與文字建議」。

## Problem

**期望（operator）≠ 設計（advisor）。** 這個落差不解決，其餘迭代都是在錯誤定位上打磨。

## Proposal（三選一，待 ISSUE-02 事實出來再定）

- **A. 升級為 operator**：把 §2.1-7 的能力邊界改寫成「平台真能做的動作清單」（建頁、改 property、查詢、移動頁…），「教你手動」降為 fallback。
- **B. 維持 advisor、誠實命名**：承認 Notion AI 是軍師層，實際操作交給 `ntn` / Notion MCP 自動化管線。
- **C. 混合（傾向）**：能力邊界**按實證過的真實能力重畫**，不按保守假設。能程式化的進 operator，平台不允許的留 advisor + 指向外部工具。

## Recommendation

傾向 **C**。理由：(1) 對齊 ISSUE-04「框架優先」——operator 要的正是內建結構；(2) 對齊 ISSUE-05「操作層」身份；(3) 不憑假設砍能力，憑 ISSUE-02 的證據畫線。

## Acceptance Criteria

- [ ] ISSUE-02 能力矩陣完成
- [ ] §2.1-7 能力邊界改寫為「實證過、平台真能做」的動作清單
- [ ] 「教你手動」明確降為 fallback 而非主路徑

## Open Questions

- Notion 原生 AI agent 的動作能力，跟「我們透過 API/MCP 的能力」是兩條線——operator 設計要取哪一條，或兩條疊加？（ISSUE-02 要分開量）
