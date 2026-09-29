---
type: Playbook
title: Curated Source lifecycle 與恢復契約
description: Reader、PMBA、書籍與其他 Sean-selected source 共用的五階段狀態機；例外獨立記錄，不設逐卡候審狀態。
timestamp: 2026-09-29T18:53:23+08:00
status: stable
domain: ai
---

# Curated Source lifecycle 與恢復契約

> 流程正典：`maintenance-learning-loop.md`。舊 Reader 路徑保留，適用所有 selected sources；不再是未啟用草案。

## 1. 狀態只表示來源處理進度

`selected → ingested → indexed → atomicized → integrated`

| source_status | 意義 | AI 下一步 |
|---|---|---|
| selected | Sean 已提供／指定納入，Human Gate 完成 | 取得內容與 document quality |
| ingested | 內容可解析 | 建立 structure、metadata、Source Tree |
| indexed | 結構／導航及覆蓋明確 | 原子化、比對既有概念 |
| atomicized | 萃取完成，notes 已建／補或有不拆卡理由 | dedup、links、MOC、lint |
| integrated | 安全範圍的知識已完成 graph integration | 後續新版本或按需維護 |

AI 逐階段更新 Source frontmatter 的 `source_status`；`status: seed/growing/stable` 仍是 note 成熟度，不混用。正常流程沒有 promote_candidate、waiting_for_sean、pending_manual_digest。

## 2. 最小持久化與恢復

Source 從 `templates/source-note.md` 起底；AI 填 metadata，Sean 不需填表。以 `id`＋`resource`＋來源版本識別同一 source。`source_version` 可以是出版版本、檔案 hash 或取得時間，必須說清楚是哪一種，不捏造頁碼或版本。

每份 Source 保留 `## Integration`：

- 覆蓋：已讀 node IDs／未處理範圍及原因。
- 成果：新建、更新、重用的 note IDs／wikilinks；沒有新卡也記理由。
- 下一步：從哪個節點／階段續跑（完成則無）。
- 驗證：lint 結果、語意自審、Git diff／commit 可追溯紀錄（不要預填不存在的 commit）。

中斷後先讀 source 與已有 notes，按 evidence＋穩定 ID 對照，不因重跑重建卡。`source_status` 是**最後完成階段**，不能把 queued 動作算完成。來源改版時保留同一 source ID、記錄版本差異，回到需重作的最早階段；舊 evidence 的版本不可被新版本靜默替換。

## 3. Exception 記錄（只在需要時）

在 Source 的 `## Exceptions` 列出：

| 欄位 | 內容 |
|---|---|
| id / status | source 內穩定代號；open / resolved |
| reason | SOP §4 的具體觸發原因 |
| affected | 受影響 node／note／mutation |
| evidence | 兩邊的來源與定位 |
| safe_action | 已完成的非破壞性處理 |
| question | Sean 需決定的一個最小問題 |
| resolution | Sean 決定、依據與日期；未決留空 |

無例外填「無」。來源無法讀取先記技術阻塞與可行下一步；不把它改名成人工消化需求。能保留雙方觀點就先整合；不確定是否合併時，相關變更暫停，其他內容繼續。

## 4. Reader 入口與 output ports

Sean 明確指定 Reader item／一批收藏納入即 selected；AI 自找文章、feed 自動匯入、一般盤點不等於永久納入。僅研究時不在 repo 建候審 queue。

應用出口按需選：decision、writing、case、playbook、teaching、not_yet。PMBA 可接工作案例／論文問題，物流可接流程改善，育兒可接家庭實踐，writing 可接文章。這些是取用方式，**不是 integrated 前置條件**；不得自動把作者規範性建議改寫成 Sean 原則。

未來 dashboard 可投影 source_status 與 open exceptions；不建逐卡 Promote Queue 或 Link Review Queue。MOC 回答「如何理解領域」，Source Tree 回答「原文在哪」，個人學習排程留 Notion。

## 5. 舊資料相容

- 既有 promoted notes 是正式知識，`reviewed` 僅保留歷史審查紀錄，不批次翻旗標或推定 Sean 已內化。
- 既有 Source 沒 lifecycle 不代表未授權，也不冒稱已 indexed/integrated。下次處理時依實際證據補欄位，保留原 ID、路徑與 links。
- 舊 captured／triaged／shortlisted 不能直接假定 selected；有 Sean 指定證據才接續 pipeline。舊 diagnosis／promote_candidate 有 Source Selection 證據者，依成果映射到實際階段，不等待學習完成。
- 舊 promoted 需確認 dedup／links／MOC／coverage 才標 integrated；archived／rejected 不自動復活。
- 舊「promote run」命令視為 ingestion 的相容別名，不要求再做逐卡批准；新的 learning trace 不是 ingestion queue。
