---
type: Playbook
title: PMBA 課後 learning trace（獨立學習軌）
description: 保留 T+0/T+1 recall、來源校正、題卡與深複習；learning trace 不再是知識入庫／promote Gate。
timestamp: 2026-09-29T18:53:23+08:00
status: stable
domain: pmba
---

# PMBA 課後 learning trace（獨立學習軌）

> 學習時間軸見 `pmba-course-cycle-sop.md`。Sean 交教材給 Sean-KB 即完成 Source Selection，AI 立即走 `_system/prompts/pmba-compile.md`，不等待本流程。
> learning trace 保留 Sean 真正的記憶／思考過程，與 source knowledge 分別歸因；舊 issue #13 的首次實跑仍是歷史紀錄。

## 角色分工

| 角色 | 負責 |
|---|---|
| Sean | 選來源；主動學習時 recall、費曼、個人立場與 reflection |
| ChatGPT／學習 agent | 以實際教材／PLAUD 校正，提供標準答案、問題與回饋，不冒充 Sean 答案 |
| GitHub Issue／對話 | 按需保存 learning trace；不是每張 knowledge card 的候審 queue |
| Notion | 課表、作業、複習日與 trace URL；不承擔長期 knowledge SoT |
| Filesystem agent | 對 Sean-selected sources 自動 index、原子化、去重、links、MOC、lint 與版本紀錄 |

## Sean 主動學習時的流程

1. T+0 不看資料 recall；AI 只確認收到，避免先餵答案。
2. T+1 第二輪 recall，再以實際 PLAUD／教材對照；沒有對照源不得憑空評分。
3. 標明 source 支持／Sean 詮釋／AI 推論，產引導問題與有來源的標準答案。
4. 按需保存 trace：body＝index＋校正摘要＋學習進度，comments 分 recall／校正／題卡（只有明確交辦時才對外寫入）。
5. 補漏掃描與深複習按 runbook；學習待練項不變成 waiting_for_sean ingestion backlog。
6. 若學習產生新的明示 Sean reflection／personal framework，可帶 stance_evidence 納入；來源主張仍歸因來源。

## Ingestion 的獨立完成條件

來源可解析、Source Tree／provenance 齊全、semantic atomicity、dedup／reconcile、earned links 與 MOC 完成、lint／完整 diff 自審通過。題卡可附於 concept 的「Retrieval 題卡」段（Q:／A:），再執行 `uv run python _system/scripts/export_anki.py`。

無首堂固定卡數上限；無 Sean 先重述／複習日拍板前置；AI-generated 不自動降 confidence。大 PDF／錄音等留外部 pointer，真正解析或立場衝突才走 exception review。
