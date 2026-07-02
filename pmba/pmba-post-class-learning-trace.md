---
type: Playbook
title: PMBA 課後 learning trace → promote 完整流程（定案）
description: 課後殘存記憶提取到 Obsidian promote 的端到端 SOP。定案於 2026-07-02，實證來源＝財務管理 Day 1（issue #13）首次完整跑通。術語定案：learning trace（取代「殘存記憶卡」）。
timestamp: 2026-07-02T20:30:00+08:00
status: stable
domain: pmba
---

# PMBA 課後 learning trace → promote 完整流程（定案）

> **上層編排**：本檔是 `pmba-course-cycle-sop.md`（session 循環總表）的「課後段」細節；T-n 預習、複習日、多堂循環與角色時間軸以總表為準。
> 方法論依據：`notion-pages/學習科學方法論.md`（生成效應＋合意困難）；候選流程原則：gh issue #11；首次實證：gh issue #13（財務管理 Day 1）。
> 術語定案：**learning trace**（課後提取軌跡），取代早期的「殘存記憶卡」。

## 角色分工（ISSUE-05 邊界的落地版）

| 角色 | 負責 | 不負責 |
|---|---|---|
| Sean | T+0/T+1 retrieval（不看資料）、回答引導問題、review decision、promote 拍板 | — |
| ChatGPT Project | 課後轉化：對照 PLAUD 校正、產引導問題、標註來源支持度 | 寫入 Notion／Obsidian |
| GitHub Issue | **候審區**：body＝index＋候選稿＋decision；comments＝完整 trace 分段 | 知識本體（不長期承載已驗證知識） |
| Notion（蒜頭） | 操作層：課表、作業、**下次複習日**、issue URL 指標 | 保存 trace 內容 |
| Claude Code | **promote operator**：拆卡、織網（對存量卡跑 earned 候選連結）、lint、git diff 給 Sean 審、Anki 匯出 | 代寫 retrieval 答案 |

## 流程

```text
課後當晚（T+0）：Sean 不看資料做殘存記憶 retrieval
  ↓
T+1：第二輪 retrieval（仍不看資料）→ 保生成效應
  ↓
開 GitHub Issue（template: 課後 learning trace）
  body＝index＋T+1 校正版候選稿＋review decision
  comment 1/3＝原始 retrieval trace
  comment 2/3＝AI 對照 PLAUD 校正（標明 PLAUD 支持 vs 個人詮釋）
  comment 3/3＝retrieval 題卡＋轉卡方向＋promote 策略
  ↓
Notion 課程列：填「下次複習日」＋ issue URL（操作層只放指標）
  ↓
Review decision（Sean）：Reject / Keep in issue / Needs source / Promote
  ↓
Promote（Claude Code 執行，Sean 審 git diff）：
  1. 新來源首次 promote：建 literature note＋source 索引卡＋MOC＋獨立 pkm-id 號段
  2. 依 comment 3 轉卡方向拆原子卡（一卡一想法；AI 校正補強處 confidence 降 medium 並註明）
  3. 織網：對存量卡跑 earned 候選連結（連結旁必帶一句 why），跨來源接進主題 MOC
  4. 題卡內嵌卡片「## Retrieval 題卡」段（Q:／A: 格式）
  5. git diff 給 Sean review 後才算落地
  ↓
Anki 匯出：uv run python _system/scripts/export_anki.py → _system/exports/ → Sean 匯入 Anki
  ↓
複習雙軌：Notion 複習日＝深度複習（retrieval＋費曼）；Anki＝零碎時間輕複習
```

## 鐵則

- **未校正的 trace 不直接進 Obsidian**；未 promote 的內容不離開 issue。
- **AI 不代寫 retrieval 答案**——題卡答案必須來自 Sean 跑過的迴圈（生成效應）。
- Fully-raw（PLAUD 逐字稿、投影片）留外部，vault 只放指標。
- 課堂主線未延續前不貪多轉卡（首堂 3–5 張上限，對齊 pmba-compile 規則）。
