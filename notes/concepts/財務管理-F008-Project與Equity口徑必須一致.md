---
# OKF-compatible core fields
type: Concept
title: Project 與 Equity 口徑必須一致
description: CF0 是整體投資額（如 -100）就用未扣息的 project cash flow 配資產折現率 RA；CF0 是股東投入（如 -60）就用扣息後的 equity cash flow 配股東要求報酬 RE。CF0、現金流口徑、折現率三者不可混用。
resource: https://github.com/sean3808/Sean-KB/issues/17
tags: [財務管理, NPV, 現金流, 評價, pmba]
timestamp: 2026-07-19T11:00:00+08:00

# Sean custom fields
id: pkm-20260719-fm-f008
status: seed
domain: pmba
source: 臺大 PMBA 財務管理
lang: zh-TW
confidence: medium
source_type: class
source_ref:
  - "[[財務管理-Lit]]"
  - "[[財務管理-Day2-learning-trace]]"
aliases:
  - 財務管理-F008
  - Project vs Equity 口徑
reviewed: false
reviewed_at:
---

# Project 與 Equity 口徑必須一致

## 命題
投資案評估有兩套口徑，三個元件（CF0、後續現金流、折現率）必須成套，不可混用：
- **CF0 = -100（整體投資額／資產角度）** → 後續用**未扣融資本息的 project cash flow**，折現率用**資產折現率 RA**。
- **CF0 = -60（股東投入額）** → 後續用**扣掉債權人本息後的 equity cash flow**，折現率用**股東要求報酬率 RE**。 ^claim

## 解釋
判別訣竅：現金流**有扣利息／還本**的，多半是股權現金流（配 RE）；**沒扣利息**的，是計畫／資產現金流（配 RA）。算出 NPV／IRR 後，要先判斷得到的是資產報酬還是股權報酬，再拿去和對應的要求報酬率比較。最常見的錯誤是 CF0 用整體投資額（-100），後續卻用扣息後的股權現金流、又拿 RE 去折——三件事對不齊，結論就失真。

> confidence 標 medium 的原因：
> 1. 老師課堂全程用 **RA（資產／計畫折現率）** 與 RE，**未使用「WACC」**一詞；坊間常把 RA 對應 WACC，但本堂 source 無此對照，故不寫入命題。
> 2. PLAUD 逐字稿 §AG 有一句「如果沒有扣掉利息的話，這邊就是 re」疑似口誤／轉錄錯誤，依前後文應為 RA（source 已標待確認）。以老師投影片校正後再升 confidence。

## 證據 / 來源摘錄
> [!quote] 財務管理 B（2026-07-12 下）框架 4／例子 4／§AG
> 「若 CF0 是整體投資額，後續要用 project cash flow，折現率用 RA；若 CF0 是股東投入額，後續要用 equity cash flow，折現率用 RE。」「投資計畫資產 100、負債 40、股權 60…算股權 NPV：CF0 = -60，扣掉債權人本息後看股東剩餘現金流，折現率用 RE。」

## 相關概念
- [[財務管理-F007-r是同一概念的不同角色名]]（RA／RE 就是 F007 的 r 落到資產側與股東側的兩個版本——口徑一致的底層原因是「風險對應報酬率」）
- [[財務管理-F009-債權人先過生存門檻股東再談剩餘]]（equity cash flow「扣掉本息」這個動作，就是 F009 說的「先給債權人、剩餘才歸股東」的現金流版本）

## Retrieval 題卡
> 答案待 Sean 跑迴圈後填入（我不代寫）。
Q: 一份投資案報告 CF0 是 -100，但後續現金流已扣掉利息、折現率又用 RE，你會如何判斷這份報告的問題？
A:

## 待追問
- 老師是否在課堂把 RA 明確等同於 WACC？（本卡暫不採此對照，待投影片確認）
- project cash flow 中利息稅盾與所得稅的正式處理順序？（issue #17 待查證，source 未展開）
