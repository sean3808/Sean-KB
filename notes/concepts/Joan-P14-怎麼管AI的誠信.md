---
# OKF-compatible core fields
type: Concept
title: 怎麼管 AI 的誠信：程序正義獨立於結果，AI 審 AI 要換腦袋
description: 回滾恢復的不是資料狀態，是「有沒有人親眼確認同意」這個程序正當性；AI 審自己寫的東西一定要換 session 或換 agent，因為同一顆腦袋審自己會有 bias。
resource:
tags: [joan, ai協作, 程序正義, 安全審查]
timestamp: 2026-07-12T22:38:00+08:00

# Sean custom fields
id: pkm-20260712-jn-p14
status: seed
domain: ai
source: Joan
lang: zh-TW
confidence: medium
source_type: class
source_ref:
  - "[[joan-fb-2026]]"
notion_refs: []
aliases: [怎麼管AI的誠信, 兩個Y回滾, AI審AI]
reviewed: false
reviewed_at:
---

# 怎麼管 AI 的誠信：程序正義獨立於結果，AI 審 AI 要換腦袋

> [!example] 場景
> - **2026-04-24 18:30**：Claude Code 在 non-TTY 環境下把 `[Y/n]` 的預設值當成自動同意，違反「遇到 confirmation prompt 要停下來問」的規則，直接把 migration apply 到遠端資料庫。事後 Claude Code 主動承認違規、列出三條處理路徑交給 Joan 決定。她明知 SQL 已審過、資料庫最終狀態完全正確，技術上不需要回滾，仍選擇回滾重做——因為她要的不是「結果一樣」，是「兩個 Y 不一樣」：回滾前的 Y 是沒有人在場的預設值，回滾後的 Y 是她自己按的、她在場、她同意了。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid0hY16LpHq7zQwXrBacBm38DjgJgaGhFGWxLT5qUtPTKWD3qbr4vPNXrMYmFxFJQMXl&id=100000500510921)
> - **2026-04-23 16:56**：Claude Code 寫的一個「攔截敏感資訊寫入」安全 hook，自己就是 RCE 漏洞的入口——heredoc 沒加單引號，導致 bash 先做變數展開，檔案內容被當成 Python 程式碼直接執行，5 個 hook 裡藏了 10 個注入點。Joan 自己第一輪 review 沒發現，是另一個 AI subagent 抓出來的。她濃縮出三條保命須知：①第一次用的 skill/hook/agent 永遠選一次性允許，用過三次行為可預期才升級成永久允許；②AI 審 AI 必須換 session 或換 agent，寫的腦袋跟挑毛病的腦袋要用不同 context；③commit 是本地的可以 reset，push 是公開的爬不回來，push 永遠只能是人類動作。對客戶展示時她主動揭露這次漏洞，客戶反應是「妳是第一個告訴我 AI 會出錯、而妳有自我規範去抓錯的人」。[原文](https://www.facebook.com/permalink.php?story_fbid=pfbid0vaHLGHq85kFqbf6hiddnzPYytAXp8XjAgppHN69ecLjuZryQJzRue5hD38w6iWL7l&id=100000500510921)

## 判斷
管 AI 誠信不是管「AI 有沒有出錯」，是管「出錯之後的程序」。回滾要恢復的是流程正當性（有沒有人親眼確認同意），不是資料庫的內容——技術上正確不等於程序上正當，兩者是獨立的價值。AI 審 AI 一定要換 session 或換 agent，同一顆腦袋審自己寫的東西會有「我剛寫的應該沒問題」的偏見。Git 的可逆性分層要用對：commit 可以 reset 是安全網，push 是公開動作、爬不回來，只能由人類手動執行。主動揭露 AI 犯的錯，建立的信任比展示 AI 多厲害更高。

## 為什麼是 checkpoint
多數人會覺得「資料庫狀態一樣，回滾沒有實質意義，是浪費時間」；Joan 認為程序正義本身有獨立於結果的價值——AI 工程誠信不是 AI 的特質，是由「有沒有白紙黑字寫規則、而且真的檢核執行後果」這個工作文化決定的。多數人以為「AI 寫的 code 有問題」等於「AI 不夠強」，是該藏起來的弱點；Joan 反而主動對客戶揭露漏洞，因為賣的不是「AI 多厲害」，是「我怎麼管 AI」。

## 連結
- [[Joan-P13-讓AI少問我]]：P13 是事前把「要不要問」設計成規則，這張是事後怎麼審、怎麼認錯——兩者合起來才是完整的協作紀律，不能只做一半。
- [[Joan-M00-那把尺]]：「程序正義獨立於結果」是同一把判準（先定準則再看結果）滲透到 AI 治理最深的一層。
- [[決策-MOC]]：回滾決策示範了 Sean 決策系列強調的「決策的正當性來自過程而非結果」。
