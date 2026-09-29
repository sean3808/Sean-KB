---
# OKF-compatible core fields
type: Concept
title: 出口貿易 CCC 診斷 MVP
description: 把現金轉換循環落到出口貿易場景的兩週 MVP：依客戶算 A/R days、依供應商算 A/P days、依產品群算存貨天數，組成 CCC 找出資金占用最高的組合，並納入缺貨／急單／空運成本避免只追最低庫存。
resource: https://github.com/sean3808/Sean-KB/issues/17
tags: [財務管理, 營運資金, CCC, work-transfer, 出口物流, pmba]
timestamp: 2026-07-19T11:00:00+08:00

# Sean custom fields
id: pkm-20260719-fm-f013
status: seed
domain: work
source: 臺大 PMBA 財務管理
lang: zh-TW
confidence: medium
source_type: idea
source_ref:
  - "[[財務管理-Lit]]"
  - "[[財務管理-Day2-learning-trace]]"
aliases:
  - 財務管理-F013
  - 出口貿易CCC MVP
reviewed: false
reviewed_at:
---

# 出口貿易 CCC 診斷 MVP

## 命題
把 CCC 概念落到 Sean 的出口貿易與庫存場景，先做一個**兩週可交付的 MVP**：不是先建大系統，而是先算出「哪個客戶／產品／供應商組合占用最多資金」，用一張表推動對話。 ^claim

## 展開 / 做法
1. **依客戶算 A/R days**，並拆出逾期結構（正常帳期 vs 逾期）。
2. **依供應商算 A/P days**，區分正式付款條件與實際逾期（避免把拖欠誤讀成議價力）。
3. **依產品或產品群算存貨天數**（inventory days）。
4. 三者組成 **CCC**，排序找出資金占用最高的客戶／產品／供應商組合。
5. 加入「缺貨成本、急單成本、空運成本」作為約束，避免 MVP 退化成「只追最低庫存」而犧牲交期與客戶。

> confidence 標 medium：這是 Sean 依課堂 CCC 概念對自身場景提出的落地方案，尚未實作驗證。落地後（有真實資料與一次迭代）再升 confidence 並補檢核點。

## 相關概念
- [[財務管理-F011-CCC是營運資金時間差的結果]]（母卡：本卡是 F011 的工作遷移——把三個天數拆到客戶／供應商／產品維度做診斷）
- [[財務管理-F004-貿易公司的營運資金庫存應收三角]]（F004 是同一場景的定性版；本卡把三角變成可算、可排序的診斷表）
- [[問解-C056-在不確定情境下「先做 MVP 再迭代優化」優於等待更多資料|問解 C056 先做 MVP 再迭代]]（跨來源：本卡「兩週 MVP、先出成果再迭代」正是 C056 的方法論落地，也對齊 Sean 個人偏好）

## 待追問
- 資料來源：A/R、A/P、存貨天數各自能否從現有 ERP／Excel 直接拉？欄位口徑是否一致？
- 驗收條件：MVP 能否在兩週內產出一張「資金占用 Top N 組合」表，並至少驅動一個付款條件／庫存水位的調整？
