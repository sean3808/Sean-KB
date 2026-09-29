---
# OKF-compatible core fields
type: Concept
title: 先 Discovery 再 Coding；記憶交給文件，不是聊天視窗
description: 方向錯了 AI 越快只會越快到錯的地方，所以先做根因分析再動工；長對話會讓 AI 越混，把上下文從「聊天紀錄」整理成「專案狀態」交接摘要，才是真正的記憶載體。
resource:
tags: [joan, ai協作, discovery, session管理]
timestamp: 2026-07-12T22:44:00+08:00

# Sean custom fields
id: pkm-20260712-jn-p16
status: seed
domain: ai
source: Joan
lang: zh-TW
confidence: medium
source_type: class
source_ref:
  - "[[joan-fb-2026]]"
notion_refs: []
aliases: [先Discovery再Coding, Session衛生, 交接摘要]
reviewed: false
reviewed_at:
---

# 先 Discovery 再 Coding；記憶交給文件，不是聊天視窗

> [!example] 場景
> - **2026-06-26 14:27（Discovery 先行）**：Joan 提到「上上週」一個每天投入 12 小時、雷打不動的專案，最後被她自己砍掉重練——因為一開始沒先釐清問題根因就直接動工。這次她改成先 Discovery（讓 AI 研究問題根因：是 UI 問題還是資料問題？是 API 沒接還是本來就沒同步完整？需不需要改資料庫？）→ 思考產品決策、做 Blueprint → 再讓 Claude Code 動工 → 驗收，結果同一類專案只花三個工作天就做得更完整。她的結論：「AI 很快，但如果方向錯，快只會讓你更快走到錯的地方」。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid02xAEdgUn6VsiKtprymnUR8VLH2q69kSyBZB7aYxTTFUTbFmLwjpJAVFaDrSguvobcl&id=100000500510921)
> - **2026-06-26 14:27（Session 衛生）**：同一篇裡她描述自己養成的習慣——每完成一個重要階段就刻意換新 session（ChatGPT 和 Claude Code 都換），換之前一定先讓 AI 整理一份只保留「下一個 session 真正需要知道的資訊」的交接摘要：目前分支、最新 commit、已完成什麼、還有哪些待辦、這次不能碰什麼、下一步要做什麼。她點名這是個反直覺：「專案上下文要累積，不代表對話要無限延長」——累積的應該是精煉過的專案狀態文件，不是原始聊天記錄。[原文同上](https://www.facebook.com/permalink.php?story_fbid=pfbid02xAEdgUn6VsiKtprymnUR8VLH2q69kSyBZB7aYxTTFUTbFmLwjpJAVFaDrSguvobcl&id=100000500510921)

## 判斷
動工前先做根因分析（是 UI 問題還是資料問題、是 API 沒接還是本來就沒同步完整），收斂成產品決策再拆小 task，不要「以為要做 A，結果真正問題是 B」就先動工。AI 讓「想到就能做」的衝動太容易被滿足，但好想法要先放進 Roadmap 延後決策（不是放棄），不能插隊實作。長對話會讓 AI 混進舊資訊，人自己也會搞不清楚「這件事是不是已經解決」——把記憶交給精煉過的交接摘要文件，把執行交給 AI，把決策留給自己；每次換 session 就是一次上下文清理。

## 為什麼是 checkpoint
「先想清楚再動工」聽起來比較慢；Joan 的論點是方向錯了，AI 越快只會讓你越快走到錯的地方——Discovery 的價值是省下後面的重工，不是拖慢速度。一般人覺得留在同一個對話裡才「AI 才記得上下文」；Joan 指出對話越長 AI 越蠢，真正的記憶載體應該是文件不是聊天視窗——這也同時降低了「人自己」的決策負擔，不只是省 AI 的。

## 連結
- [[Joan-P15-Skill是防笨不是加聰明]]：同屬 AI 協作紀律的一體兩面，P15 管單次任務的 skill 品質，這張管跨 session 的節奏與記憶。
- [[Joan-M00-那把尺]]：「記憶交給文件不是聊天視窗」是同一把尺滲透到「怎麼跟 AI 交接」這一層。
- 對照本 vault 根目錄的 `session-continuity.md`：Sean 自己的跨-agent session 交接機制，正是同一套「上下文從聊天紀錄整理成專案狀態」原則在 Sean-KB 的具體落地。
