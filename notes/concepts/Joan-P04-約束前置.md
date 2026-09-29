---
# OKF-compatible core fields
type: Concept
title: 約束前置：成本天花板寫進架構，不等做完才砍
description: 財務或資源限制不是事後才拿來修剪成品的關卡，而是在設計當下就當成設計輸入之一，滲透到最底層的技術選型（連DB索引都在替預算著想）；約束越早進場，越不會走到推翻重做那一步。
resource:
tags: [joan, 成本約束, 架構設計, 治理]
timestamp: 2026-07-12T23:15:00+08:00

# Sean custom fields
id: pkm-20260712-jn-p04
status: seed
domain: ai
source: Joan
lang: zh-TW
confidence: medium
source_type: class
source_ref:
  - "[[joan-02-Joan思維骨架-六問與治理本能]]"
notion_refs: []
aliases:
  - 約束前置
  - 成本天花板
  - 成本寫進架構
reviewed: false
reviewed_at:
---

# 約束前置：成本天花板寫進架構，不等做完才砍

> [!example] 場景
> - 2025-10-21 17:58「Google免費層架n8n」：故意只用50%運算量留餘裕，用「保守估算」而非榨乾額度去架n8n，還原「免費層可控可測可長大」的判斷——約束不是拿來卡到極限，是拿來換未來的彈性。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid02zdr64zFjJTuXD2tNYyH9pE2GA82KEhmcD2SyAWtvXKMZBAPhsCmCi7xgkkoJ6Nsil&id=100000500510921)
> - 2026-07-09 15:30 六份開發指令橫向比對：「後端用Neon，不希望超過免費門檻」「資料庫索引盡量重複使用避免單一索引」，成本考量一路滲透到schema／索引設計這種最底層的技術決策，不是等系統跑起來後才回頭砍功能。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid0oYGnftW1rRV3b97y87RuxPeBtzoPVT51EQLNLFAwN9wmwfU7x1uyeWyuQzzwGnpRl&id=100000500510921)

## 判斷

面對任何資源／預算限制，第一個動作不是「先把功能做完，超支了再回頭砍」，而是在設計最初期就把這個天花板當成一項設計輸入，跟功能需求平起平坐——連資料庫要不要建索引、索引要不要重複使用這種底層技術選型都要先過這關。而且天花板不是拿來卡滿的，故意留一截餘裕（只用50%），本身就是為了讓系統「可控、可測、可長大」而不是一次性榨乾。

## 為什麼是 checkpoint（反直覺）

工程直覺通常是「先做對，再做省」——把成本優化當成完成功能之後的第二階段工作，甚至是被迫砍功能才做的妥協。Joan 的順序把「省」提到跟「對」同時進場：省是設計正確性的一部分，不是正確做完之後的犧牲品。這也代表事後很難再走「先做完再砍」這條路，因為成本判準已經滲透進最底層的技術選型，砍的不是功能表層，是要動架構。

## 連結

- [[Joan-M00-那把尺]]（「先問錢在哪」滲透到DB schema，是尺的滲透性特徵最直接的舉例）
- [[Joan-P01-風險雷達分層]]（同一次「六份指令」橫向比對長出的另一層本能，一個管風險分層一個管成本天花板）
- [[Joan-P02-預警是責任升級鏈]]（三卡同源於同一份指令覆盤，都是把判準寫進設計輸入而非事後補救的具體展開）
