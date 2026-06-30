# Notion AI 迭代 — Issue 追蹤

> 本次迭代的本質：**用 Sean-KB 專案的系統資產（防彈卡片網 / 跨來源 MOC / 學習科學方法論層）回頭檢視並迭代 Notion AI 的三頁配置。**
> 不是同步兩邊時間序，不是補全知識——是讓 Notion AI 更符合「心法方向」。

## 統一主軸（迭代的北極星）

> **Notion AI = 結構化的「操作層」operator；框架內建為預設準則；狀態 localize 進專案文件，而非靠 AI 自我改記憶。**

三個推論直接落在這條主軸上：框架優先（ISSUE-04）、移除自我記憶（ISSUE-03）、operator 定位（ISSUE-01）。

## 來源權威序（驗證防彈內容時的優先級）

> **Esor 官方（websearch / 原書）＞ vault 二手萃取卡片 ＞ Skill 現況。**
> 防彈筆記法是台灣作者 **Esor（電腦玩物站長）** 的心法，**≠ 子彈筆記法（Bullet Journal）**，兩者不可混為一談。
> vault 卡片是二手萃取，可能漏判或重述失真——遇衝突一律以官方為準（已實證：ISSUE-07 #1 的「永久任務筆記」原被 vault 誤判為外來術語，官方確認是 Esor 原生概念）。

## 被迭代的三頁（本地副本）

| 頁 | 角色 | 本地檔 |
|---|---|---|
| My Notion AI | System Prompt 本體 | `../My-Notion-AI-System-Prompt.md` |
| 防彈引擎 ｜ 操作技能 | 全域底層引擎 Skill | `../Skill-防彈引擎.md` |
| 主控台 ｜ Skill | 開場鳥瞰面板 Skill | `../Skill-主控台.md` |

## Issue 清單

| # | 標題 | 優先 | 類型 | 相依 |
|---|---|---|---|---|
| 01 | Notion AI 定位：operator vs advisor | High | decision | ← 02 |
| 02 | 實證 Notion AI 實際 DB 操作能力 | High | spike | blocks 01 |
| 03 | 移除 Memories 自我更新，改 localized 預設準則 | Medium | enhancement | — |
| 04 | 明確化「框架優先」設計原則（AI ≠ 人類避免過度整理） | Low | docs | — |
| 05 | 操作層 vs 方法論層 邊界釐清 | Medium | discussion | — |
| 06 | 策展防彈模組納入 Skill | Medium | content | ← 01 |
| 07 | 防彈引擎 Skill 內容精準度修正 | Medium | bug | — |
| 08 | 主控台範例日期去硬編碼 | Low | chore | — |

## 依賴關係

```
02 (實證能力) ──blocks──▶ 01 (operator/advisor 定位) ──informs──▶ 06 (策展模組)
04 / 03 / 05 / 07 / 08  獨立可平行
```

## 診斷來源

本批 Issue 由 2026-06-30 session 的四軸診斷收斂而來：
- 三頁內容內部矛盾 / 過時 / 能力落差（主 agent 直推）
- vault 防彈卡片網盤點（researcher，報告：`../../.subagent-output/diag-bulletproof-vault/final.md`）
- Sean 回饋重塑（A1 非矛盾、A2 移除、B1 撤、B2 範例、B3 拆談、C 照走、D 重框）

## 狀態

全部 `open`。下一步建議：先做 **ISSUE-02（spike）**，事實出來後拍板 **ISSUE-01**。
