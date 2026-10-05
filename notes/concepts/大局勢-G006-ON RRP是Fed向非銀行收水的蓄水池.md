---
type: Concept
title: ON RRP 是 Fed 向非銀行收水的蓄水池
description: 貨幣市場基金等非銀行不能在 Fed 開準備金帳戶，資金過多時只能放銀行或停進 Fed 的隔夜逆回購（ON RRP）；Fed 藉此把市場上多餘的美元收回負債端。ON RRP 餘額下降，代表這批錢流去別處。
resource: 'local:115-1_大局勢\大局勢 20260907-transcript.txt'
tags: [大局勢, ON RRP, 貨幣市場基金, Fed, 美元流動性, pmba]
timestamp: 2026-09-30T11:30:13+08:00
id: pkm-20260930-gt-g006
status: seed
domain: pmba
source: 臺大 PMBA 大局勢
lang: zh-TW
confidence: medium
source_type: class
source_ref:
  - '[[115-1_大局勢_W01_20260907_導論]]'
source_evidence:
  - source: '[[115-1_大局勢_W01_20260907_導論]]'
    source_version: '逐字稿 SHA256 55B6D0A69AB7…'
    node_id: t-fed-onrrp
    section: 逐字稿 00:40:33–00:51:25
    evidence_pointer: 'transcript#00:41:33'
  - source: '[[115-1_大局勢_W01_20260907_導論]]'
    source_version: '逐字稿 SHA256 55B6D0A69AB7…'
    node_id: t-bslens
    section: 逐字稿 00:20:52–00:22:37（非銀行不能存央行）
    evidence_pointer: 'transcript#00:22:04'
  - source: '[[115-1_大局勢_W01_20260907_導論]]'
    source_version: 'GT001 簡報 SHA256 C8342C3E22D1…（引用 Fed H.4.1，2026-09-03 發布）'
    node_id: s-fedbs
    section: 粗談 FED B/S > Reverse repurchase agreements
    page_range: [10, 10]
    evidence_pointer: 'local:課程 2026 0907 台大PMBA GT001 SIMON.pdf#page=10'
notion_refs: []
aliases:
  - 大局勢-G006
  - 隔夜逆回購
  - Overnight Reverse Repo
mocs:
  - '[[總體金融與美元流動性-MOC]]'
ingestion_version: 1
generated_by: ai
claim_origin: source
---

# ON RRP 是 Fed 向非銀行收水的蓄水池

## 核心想法
只有銀行能在央行開帳戶；貨幣市場基金（MMF）、退休基金等非銀行資金很多，卻只能把錢存在商業銀行，或透過 Fed 的隔夜逆回購工具（ON RRP）停泊。當市場上的錢太多、可能推升通膨時，Fed 用 ON RRP 把多餘的美元收進自己的負債端。 ^claim

## 展開 / 理由
- **為何 MMF 願意停進 ON RRP**：放在商業銀行有倒閉風險，放在 Fed 除非美國本身出事，否則沒問題（逐字稿 00:43:55）。交易形式是 MMF 把錢借給 Fed、Fed 以持有的債券作抵押。
- **餘額下降的兩種解讀**（講者提出）：一是超額儲蓄已經用掉，二是資金移去做別的事，例如買股票或短中期債券（00:50:55–00:51:25）。
- **規模**：簡報 H.4.1 顯示截至 2026-09-02 的週平均，逆回購餘額約 3,650 億美元（365,043 百萬美元），其中多數是外國官方帳戶（363,763 百萬）。講者口述過去高峰「三到四兆美元」，逐字稿數字轉錄錯亂，本卡不採用具體高峰值。
- **和 Repo 的方向相反**：ON RRP 是 Fed 從市場收水；Repo 是市場參與者拿債券去借錢，壓力大時利率會飆高（見 [[大局勢-G007-Repo與SOFR是短期美元壓力的溫度計|G007]]）。
- 同一個「非銀行不能直接存央行」的原則在台灣也成立：非銀行不能把台幣存在央行（00:22:04）。

## 證據 / 來源
- 逐字稿 00:41:33：「銀行儲蓄把錢存在這邊……TGA 是財政部把錢存在這邊。」
- 逐字稿 00:43:24：「市場的水我先把它收在我的口袋裡。那我要怎麼收呢？我就用 ON RRP 這項工具。」
- 簡報 p10：Reverse repurchase agreements 365,043（百萬美元，週平均）。

## 相關概念
- [[大局勢-G003-Fed資產負債表負債端是美元資產端是美債與MBS]]（ON RRP 是 G003 負債端的一個帳戶；它縮小時，錢可能流向準備金或市場）
- [[大局勢-G007-Repo與SOFR是短期美元壓力的溫度計]]（同樣以債券作抵押的短期交易，但一個收水、一個反映缺水）

## Retrieval 題卡
Q: 為什麼貨幣市場基金會把資金停在 Fed 的 ON RRP？這個工具對 Fed 有什麼作用？
A: MMF 是非銀行，不能在 Fed 開準備金帳戶，放商業銀行又有倒閉風險，所以把錢停進 Fed 的隔夜逆回購；Fed 藉此把市場上過多的美元收回負債端，調節水量。

## 待追問
- 第 9–10 週「回購與雙向視角」會怎麼從 MMF 端與 Fed 端各畫一次這筆交易？

## 後續深化
- 第 4 週：[[大局勢-G039-ON RRP耗盡後財政部發債直接抽走銀行準備金]]（蓄水池放乾之後，發債的壓力落到銀行準備金）
- 第 3 週：[[大局勢-G029-Fed是一間有盈虧的銀行盈餘上繳財政部高利率時會虧損]]（收水要付利息，是 Fed 的成本）
