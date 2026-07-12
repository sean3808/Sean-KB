---
# OKF-compatible core fields
type: Concept
title: 為對方設計：立場建模、善意內建、機制隨情緒濃度換目的
description: 系統設計不能只站在下指令者自己的角度，要事先把每個利害關係人的立場、甚至個體差異（信仰、情緒狀態）都建進模型；善意與合規不是事後補的免責條款，是內建進系統邏輯與情感歷程本身的一等公民。
resource:
tags: [joan, 使用者建模, 系統設計, 同理心工程化]
timestamp: 2026-07-12T23:10:00+08:00

# Sean custom fields
id: pkm-20260712-jn-p03
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
  - 為對方設計
  - 多立場建模
  - 善意內建系統
reviewed: false
reviewed_at:
---

# 為對方設計：立場建模、善意內建、機制隨情緒濃度換目的

> [!example] 場景
> - **角色層**（2025-08-25 11:35「Multi-LLM Collaboration System」）：把7個AI Provider刻意分派成不同立場角色（協調者／法規合規／數據趨勢／國際案例／程式細節／唱反調），核心判斷「單一AI再強也只有一個腦袋，決策要靠多立場團隊」。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid0R8fzjNo46UDD4W68VFLATCT7t4GxeRzo2iZXBF4LSr4q3bykLGcturEZ4L7x23ACl&id=100000500510921)
> - **立場層**（2026-07-09 15:17 訂房系統指令對比）：「一般人只站自己角度，我同時建好每個立場」——指令裡同時站了前台、廚房、房客、回頭客、合作景區、大型訂房平台，打第一輪時就同步分好每個角色要看到什麼、要被通知什麼，不是先做完再回頭補。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid0t9qZyfExCYiSVJQooxbJ5AhkpV2rDGEysv4qVYJE3pVpgLHsQxSX8BqsYpfEVbful&id=100000500510921)
> - **信仰個體差異層**（2026-07-09 16:12 寵物殯葬暨身後紀念平台指令）：要求「依寵物主信仰，邀請在火化時刻同步祝福寵物」——立場建模從「角色職能」升級到「個人信念系統」這個更深的個體差異變數。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid033fM9fukf2uoYCfMZdUKmJeKsGTqak4PAXa4x7wxtNYSPSRerkvoQexMiQwtujD9sl&id=100000500510921)
> - **機制隨情緒切換目的、合規嵌情感**（同一份指令）：同一種「進度顯示、狀態追蹤」透明化機制，一般商業場景是給管理者／客戶「監控」用，但這裡目的整個反過來是「安撫」，讓當事人覺得自己沒有被排除在過程之外；而「需生成線上授權書供寵物主線上簽署」這句法律條款，被刻意擺在指令最後、緊接感謝信分享之後，而非切成獨立的合規模組，讓法律保障變成服務歷程自然的一環。[原文同上](https://www.facebook.com/permalink.php?story_fbid=pfbid033fM9fukf2uoYCfMZdUKmJeKsGTqak4PAXa4x7wxtNYSPSRerkvoQexMiQwtujD9sl&id=100000500510921)

## 判斷

下指令或做系統設計時，先把「所有會被這個系統影響到的人」一次列出來，不是只站在委託人自己的角度描述功能；而且對象不能只用「角色／職能」建模就打住，要往下一層問這個角色可能有的個體差異（信仰、情緒狀態、當下最需要什麼），因為同一個角色底下的不同人，可能需要完全相反的東西（同一機制對某人是監控、對某人是安撫）。合規／法務保障也一樣不是「有沒有做」的技術模組打勾題，是「放在使用者旅程的哪一步」的設計決策，順手放進情感最需要被安放的時刻，比切成獨立表單更接近使用者的真實需要。

## 為什麼是 checkpoint（反直覺）

多數指令只有一個視角——下指令的人自己。多數系統把「合規」「監控」當成獨立、可插拔的技術模組，做完功能再補。Joan 的判斷相反：立場要在打第一輪指令時就同步建好，不是先做完再回頭補「欸廚房那邊是不是也要有東西看」；合規文件放在流程的哪一步，本身就是設計決策而不只是「有沒有」的問題；同一套機制的「功能」定位也不是寫死的，會隨對象的情緒濃度自動切換目的——多數人只問「要不要做」，這裡多問一層「做出來是為了誰安心」。

## 連結

- [[Joan-M00-那把尺]]（信仰個體差異、機制隨情緒切換目的，都是「尺往高情緒場景滲透時自動長出新層」的具體案例）
- [[Joan-P01-風險雷達分層]]（寵物殯葬同一份指令，既示範情緒風險治理層，也示範為對方設計——兩卡是同一素材的不同切面：一個看怎麼防錯，一個看怎麼替對方著想）
- [[Joan-P02-預警是責任升級鏈]]（立場建模決定「每個角色要被通知什麼」，跟P02「預警接通知誰」在同一份指令裡是同一個動作的兩種展開）
