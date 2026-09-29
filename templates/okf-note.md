---
# OKF-compatible core fields
type: Concept            # Concept / Case / Person / Literature / Playbook / Principle / Map / Decision
title:
description:
resource:
tags: []
timestamp:               # ISO 8601 with timezone

# Sean custom fields
id:                      # pkm-YYYYMMDD-<source namespace>-<code>，沿用既有號段，不撞號
status: seed             # seed / growing / stable；不是批准狀態
domain:
lang: zh-TW
confidence: medium       # 依證據判斷，不依是否經人工學習
source_type:
source_ref: []           # 新衍生 note 指向 sources/ 的 Source
source_evidence: []      # 每筆含 source、source_version、locator；格式見 schema
notion_refs: []
aliases: []
mocs: []
ingestion_version: 1
generated_by: ai         # ai / sean / mixed
claim_origin: source     # source / ai-inference / sean；Map 可省略
# stance_evidence:       # 只有 Sean 明示個人立場時填寫，不把選來源當認同全部主張
# reviewed / reviewed_at 僅保留既有歷史紀錄；不需為新 AI note 建人工 approve flag
---

# （標題）

## 核心想法
<!-- 一張卡一個可獨立理解、可複用想法；描述知識與來源，不冒充 Sean -->

## 展開 / 理由
<!-- 保留條件、限制、反例；AI 推論明示 -->

## 證據 / 來源
<!-- 對應 source_evidence，短引文按需，不大量複製原文 -->

## 相關概念
<!-- 每條知識型 wikilink 附一句 relationship context；同主題用 tags / MOC -->

## 待追問
