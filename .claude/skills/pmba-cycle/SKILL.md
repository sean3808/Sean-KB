---
name: pmba-cycle
description: >
  PMBA 課程循環中 Claude Code 職責的執行介面：判定今天相位、執行 promote run（拆卡→織網→diff 審→commit）、
  重匯 Anki、結案清算。正典＝pmba/pmba-course-cycle-sop.md（本 skill 只是執行層，流程疑義一律回 runbook）。
  Use when: Sean 說 /pmba-cycle、「promote run」、「跑 promote」、「第二批題卡進 Anki」、「重匯 Anki」、
  「PMBA 今天該做什麼」、「複習日到了」、「課程結案」，或 learning trace issue 出現 Promote 拍板。
  Not for: 診斷場／Reader 材料消化（走 /kb-loop）、Notion 行政操作（蒜頭的事）、
  retrieval 與校正（Sean＋ChatGPT 的事，我不代寫答案）。
---

# pmba-cycle — PMBA 課程循環的 Claude Code 執行層

> **正典**：`pmba/pmba-course-cycle-sop.md`（runbook v3+）。本 skill 只封裝 Claude Code 那一欄的動作；
> 相位定義、其他角色職責、降級路徑、判準理由，一律以 runbook 為準，不在此複製。

## Step 0 — 定位相位（每次觸發必做）

1. 跑 `Get-Date` 取系統時間（不可臆測日期）。
2. 收集三個輸入：`today`、本課最近一堂 `T0`、下一堂 `T0next`（Notion 課程頁內文場次表；MCP 可查 `collection://2964dadb-14ce-4eaf-81b2-75dc0fc019d7`，或直接問 Sean）。
3. 依 runbook §0 判定程序算出相位，向 Sean 回報「現在是＜相位＞，我這欄的動作是＜X＞／無動作」。

## 相位 → 我的動作對照

| 相位 | 我做什麼 |
|---|---|
| 預習窗（T-3） | （可選）Sean 點名主題時，拉 vault 既有相關卡供預習 context |
| 課中／T+0／T+1 | **無動作**（Sean＋ChatGPT＋蒜頭的段） |
| 補漏窗（T+2~T+4） | 第二批題卡落 issue 後 → 重匯 Anki（下方命令） |
| 複習日＋Sean 拍板 Promote | **執行 promote run**（下方 checklist） |
| 課程結案 | 結案 promote run＋課程 MOC 的 open-questions 收斂＋資產六件套檢查 |
| 任何時候（Sean 點名） | vault 體檢、跨來源織網、runbook 迭代（§8 規則：改完同步投影並提醒 Sean 重貼） |

## Promote run checklist（runbook §3.8 的展開）

前置：Sean 已在 issue 拍板 **Promote**（未拍板不啟動——鐵則）。

1. `gh issue view <N> --json body,comments` 讀 trace 全文，依 comment 3 的轉卡方向拆卡。
2. **新來源首次 promote** 先建導航層：literature note＋`sources/` 索引卡＋MOC＋**獨立 pkm-id 號段**（先 grep 既有號段防撞；命名規則見 repo `CLAUDE.md`）。
3. 原子卡：一卡一想法；從 `templates/okf-note.md` 起底；AI 校正補強處 `confidence: medium` 並在卡內註明；題卡內嵌「`## Retrieval 題卡`」段（`Q:`/`A:` 行，答案必須來自 Sean 跑過的迴圈——**我不代寫**）。
4. 織網：對存量卡跑 earned 候選連結——判準＝「合看會不會產生單卡得不到的理解？會改變 Sean 的決策、判斷框架或工作方法嗎？」每條**必帶一句 why**；禁止批次相似度硬連；跨來源者視情接進主題 MOC（如 `決策-MOC`）。
5. 驗證：跑 vault 完整性檢查（dangling link／pkm-id 撞號／MOC 孤兒——可重用 scratchpad 的 vault_health 腳本邏輯）。
6. **git diff 給 Sean 審**（CLAUDE.md Safety：改既有 promoted note 不靜默覆寫）→ 放行才 commit（`feat(vault)`/`feat(pmba)`）。
7. 重匯 Anki（下方命令）＋在 issue 補 promote 紀錄 comment（audit trail）。

## Anki 重匯

```powershell
$env:PYTHONIOENCODING = 'utf-8'
uv run python _system/scripts/export_anki.py
```

輸出 `_system/exports/anki-cards.txt`（gitignored），提醒 Sean 到 Anki File→Import。

## 我的鐵則（runbook §4 中屬於我的子集）

- 不代寫 retrieval 答案；不在 Sean 拍板前 promote。
- 改既有 promoted note 一律先出 git diff。
- earned link 沒有一句 why 就不連（改用 tag／MOC）。
- runbook 改動後必同步投影（ChatGPT prompt、蒜頭 Skill 各自那欄）並提醒 Sean 重貼——投影不會自己更新。
