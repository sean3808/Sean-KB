---
# OKF-compatible core fields
type: Concept
title: 連兩次同類異常＝別人的問題，該停手不是繼續內耗排查
description: 把「查證次數」本身當判斷訊號——查過兩次還沒好，繼續查是在浪費而非解決；這是對「自己可控 vs 不可控」邊界的即時判斷，不是無止盡的責任感驅動排查。
resource:
tags: [joan, 外部依賴, 決策邊界, 停損]
timestamp: 2026-07-12T22:49:00+08:00

# Sean custom fields
id: pkm-20260712-jn-p19
status: seed
domain: ai
source: Joan
lang: zh-TW
confidence: medium
source_type: class
source_ref:
  - "[[joan-fb-2025]]"
notion_refs: []
aliases: [外部依賴失效判準, 查證次數當訊號]
reviewed: false
reviewed_at:
---

# 連兩次同類異常＝別人的問題，該停手不是繼續內耗排查

> [!example] 場景
> - **2025-10-20 18:03**：Canva、Docker、Cloudflare、AWS 同天大當機。Joan 在發現兩個地方出現延遲問題之後，直接判斷「還好我有先見之明」，決定去睡覺，不繼續排查。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid02bHeCj9BTMs7PK3uwCc8e8eTDtLR75ekvGDVwKKj9xoGGZS4iMoBjHdwJDAQmYFsUl&id=100000500510921)
> - **2025-10-20 18:21**：她把這次經驗抽象成判準：「間隔三分鐘後，卻還是出現第二次的反應延遲，基本上就可以直接關掉視窗，然後去做其他事。」超過二次以上的網路延遲，一定是有哪裡出了問題，而這個問題通常不是自己可以解決的，再多修正方式都是白做工。她把這歸類為一種「斷捨離」——要遠離「我今天一定要把這件事情搞定」的心態，該做的是去睡覺或享受人生。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid0xvaQ1Djrgi1C1jCjNvvpFcSis5m3yQPhscGoWGUJTDzCWyjPbZFZPo97MZSpeTRyl&id=100000500510921)

## 判斷
面對外部系統故障，判準是「連續兩次以上出現同類異常」＝別人的問題不是自己能解的問題，此時該做的不是繼續排查、reload、內耗，而是直接停手去做別的事。把「查證次數」本身當成判斷訊號：查過兩次還沒好，繼續查是在浪費而非解決——這是對「自己可控 vs 不可控」邊界的即時判斷，不是靠責任感硬撐。

## 為什麼是 checkpoint
一般直覺是「多查一定能找到答案／解決問題」；Joan 把「查證次數」本身當作判斷訊號——查過兩次還沒好，繼續查不是負責任，是在浪費。多數人把「一定要把事情搞定」當美德；Joan 認為這裡的美德反而是斷捨離——知道什麼時候該停手去睡覺。

## 連結
- [[Joan-P18-戰略即假設]]：都是「什麼時候該停下重新判斷」的元判斷，P18 管戰略假設，這張管外部依賴的即時判斷邊界。
- [[Joan-M00-那把尺]]：「查證次數當判斷訊號」是同一把尺往「該不該繼續投入」這個最基礎的資源分配問題滲透。
- [[決策-MOC]]：呼應「先求不輸」家族——知道邊界在哪裡、什麼時候該停手，本身就是一種決策制高點。
