---
# OKF-compatible core fields
type: Concept
title: Skill 是防笨不是加聰明：三問設計法 + 可教性逼出隱性知識
description: Skill 的本質是「這個領域 AI 預設會犯什麼笨、怎麼用紀律擋下來」，不是讓 AI 更厲害；受眾一旦從自用變成要 fork 給別人，容忍度就該跟著升級，不是龜毛是紀律。
resource:
tags: [joan, ai協作, skill設計, 工程紀律]
timestamp: 2026-07-12T22:41:00+08:00

# Sean custom fields
id: pkm-20260712-jn-p15
status: seed
domain: ai
source: Joan
lang: zh-TW
confidence: medium
source_type: class
source_ref:
  - "[[joan-fb-2026]]"
notion_refs: []
aliases: [Skill防笨不加聰明, 三問設計法, 可教性]
reviewed: false
reviewed_at:
---

# Skill 是防笨不是加聰明：三問設計法 + 可教性逼出隱性知識

> [!example] 場景
> - **2026-06-26 16:11**：Skill 只寫給自己用時，一個 md 檔就夠（大概對就好）。但一旦要教給不認識自己、要 fork 的學員，「這個 skill 能不能在沒有我盯著的情況下跑出可預期的結果」變成新標準，逼著把隱性知識（版型套哪個、情境換哪個參數）寫成明文契約（`FROZEN.md`、`registry.json`）、把驗證變成程式、把核心邏輯變成回歸測試。同一篇裡她也指出：資料夾裡每一支驗證腳本背後都是一個「靠肉眼看，看漏了，付出代價」的真實案例——`validate_punct.py` 是因為交付講義夾了半形逗號印出來才發現，`check_clip.py` 是因為知識圖螢幕上看起來好好的，印出來文字被裁掉三分之一。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid02cqXDLhgsZsvTsn7wfq7A98VpjJKxHrKCMF2fBEMmmkdptc79hCmeJEXRV9AUUhEVl&id=100000500510921)
> - **2026-05-06 16:19**：Joan 花兩小時逐份讀完 Anthropic 沙盒環境裡的 30 個內建 skill 後發現，每份 skill 的本質都在做同一件事：「LLM 默認會 X，但 X 在這個情境下會出錯，所以寫一份規則叫它不要 X、要 Y」。她把觀察濃縮成三問檢查每個要做的 sub-agent：①在我的領域，LLM 默認會犯什麼笨？②怎麼用紀律避免？③怎麼讓使用者輕鬆地遵循這個紀律？並觀察到 Anthropic 對「不可逆動作」分級極嚴格——Tier 3 動作必須明確 yes，絕不接受沉默即同意，對方說 No 立刻停不准 try harder。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid02oVsNnCzozsCSm1MUreAfUbPBnhek7wU1M6XTaa7byBKRUyVNRqEztokJtYZhHoMrl&id=100000500510921)

## 判斷
Skill = 領域 SOP ＋ 踩坑筆記 ＋ 風格指南，不是給 AI 加能力。設計每一份 skill 前先問三問：這個領域 AI 默認會犯什麼笨、怎麼用紀律避免、怎麼讓人輕鬆遵循。判斷一份規範／驗證腳本該不該存在，可以回頭問「這是為了防哪一次已經發生過的痛」——工程紀律是從痛長出來的，不是先驗地設計出來的完美主義。而容忍度（要不要包成資料夾、要不要寫回歸測試）該隨受眾升級：自用一個 md 就夠，要給別人 fork 就要把隱性知識明文化。

## 為什麼是 checkpoint
多數人做 skill 的出發點是「怎麼讓 AI 更厲害」；Joan 指出真正值錢的問法是反過來的「這個領域 AI 預設會怎麼犯笨、怎麼用紀律擋下來」——這三個問題比「怎麼讓 AI 更厲害」有用得多。多數人以為嚴謹的工程紀律來自「有紀律的人」的性格；Joan 指出紀律其實是「先吃過一次虧」的痕跡。多數人以為「包資料夾」是過度工程；判準其實是這個東西要不要跨越時間穩定運作、要不要被別人接手，受眾一變，容忍度就該跟著變。

## 連結
- [[Joan-P16-先Discovery與Session衛生]]：同屬 AI 協作紀律，這張管「skill 本身該多嚴謹」，P16 管「協作節奏跟記憶該怎麼安排」。
- [[Joan-M00-那把尺]]：三問判準是同一把「先定判準再動手」的尺，滲透到 skill 設計這一層。
- 對照本 vault `CLAUDE.md` 的 Obsidian skills 段落：Sean 自己也在用「反射性考慮對應 skill 而非通用 Read/Write 硬幹」的紀律，是同一種「先問這裡該用什麼工具紀律」的判斷。
