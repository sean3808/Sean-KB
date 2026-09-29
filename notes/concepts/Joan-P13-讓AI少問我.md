---
# OKF-compatible core fields
type: Concept
title: 讓 AI 少問我：把「要不要問」設計成規則，不是臨場判斷
description: 安全感不在「每步都問」，在把決策規則寫在任務開始之前；讀寫二分判準取代危險清單，最危險操作直接拒絕不詢問。
resource:
tags: [joan, ai協作, 權限設計, 決策疲勞]
timestamp: 2026-07-12T22:35:00+08:00

# Sean custom fields
id: pkm-20260712-jn-p13
status: seed
domain: ai
source: Joan
lang: zh-TW
confidence: medium
source_type: class
source_ref:
  - "[[joan-fb-2026]]"
notion_refs: []
aliases: [讓AI少問我, 決策三層, 讀寫二分]
reviewed: false
reviewed_at:
---

# 讓 AI 少問我：把「要不要問」設計成規則，不是臨場判斷

> [!example] 場景
> - **2026-06-26 14:27**：Joan 中風後對「腦力消耗」極敏感，發現自己一天要對 AI 做 80-120 次微小決策（要不要 commit？要不要改 schema？）。她把 AI 協作的事情分成三層——①**可自動執行**（讀檔、搜尋、跑型別檢查，低風險，做完回報就好）②**先做但要回報**（技術分析、修改計畫、風險列表，會影響下一步但不直接改系統）③**必須先確認**（改 schema、push main、deploy、刪資料，錯了重工成本高）。核心轉變是「目標不是讓 AI 更自由，而是讓它少問我」。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid02xAEdgUn6VsiKtprymnUR8VLH2q69kSyBZB7aYxTTFUTbFmLwjpJAVFaDrSguvobcl&id=100000500510921)
> - **2026-06-19 16:39**：設 Claude Code 權限時她不背「哪些指令安全、哪些危險」的清單，只問一個問題：**這個指令會不會改變專案狀態？** 純讀取永久允許；會動到檔案/版本歷史/相依套件的要停下來確認。但有些指令長得像唯讀其實會寫（`sed` 沒加 `-i` 是唯讀，加了就是寫；`find` 本身是查詢，掛 `-delete` 或 `-exec` 就能執行任意命令）——規則擋的是「指令長相」不是「指令行為」。而最危險的操作（`rm -rf`、`git push --force`）不該設成「詢問」，該直接「拒絕」，因為人在連續按了十次 Approve 之後會手滑。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid02Vq9jMoxawgtGqR782pwTdTY8eJu7tt59XZ9hHQP26YDuJxe4yMtuoM8n4VKs5oS4l&id=100000500510921)

## 判斷
把「要不要問我」預先設計成規則，而不是每一步臨場判斷——任務開始前就寫清楚哪些操作可以直接做、哪些必須先確認。判斷權限的軸不是背一份危險指令清單，是問「這個指令會不會改變狀態（讀 vs 寫）」；而且要留意「長得像唯讀其實會寫」的偽裝指令。真正的最高風險操作，不該設計成「詢問」，該設計成「拒絕」——人在重複按確認之後會手滑，規則要防的是人的疲勞，不是 AI 的能力。

## 為什麼是 checkpoint
多數人覺得「AI 每步都確認」比較安全；Joan 指出這其實只是把決策疲勞轉嫁給人類——她算過一天五小時要做 80-120 次決策，安全感和效率的取捨點不在「問不問」，在「規則有沒有先想清楚」。多數人設權限靠背清單（哪些指令危險），Joan 用的是二元判準（讀 vs 寫），清單思維本身就是漏洞來源——會漏掉「偽裝成唯讀的寫入指令」這種例外。

## 連結
- [[Joan-P14-怎麼管AI的誠信]]：這張卡管「事前要不要問」，P14 管「事後怎麼審、怎麼認錯」——一個是預防設計，一個是事後校正，合起來是完整的 AI 協作紀律。
- [[Joan-M00-那把尺]]：同一把判準（先定規則再決策）從商業層滲透到「要不要問我」這個最日常的協作介面。
- [[決策-MOC]]：「先設計規則而非臨場決策」呼應 Sean 決策系列一貫的「先定判準再決策」家族。
