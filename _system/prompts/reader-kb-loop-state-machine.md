---
type: Playbook
title: Reader → kb-loop 狀態機與 Output Ports
description: 把 Reader input 透過 /kb-loop 診斷場轉成可維護、可追蹤、可應用的 Sean-KB 工作流。承接維護＝學習 SOP；重點是狀態持久化、promote gate、output target，而不是新增一套摘要流程。
timestamp: 2026-06-26T00:00:00+08:00
status: draft
domain: ai
---

# Reader → kb-loop 狀態機與 Output Ports

> 本檔是 `_system/prompts/maintenance-learning-loop.md` 的補充規格。它不取代 `/kb-loop`，而是把 `/kb-loop` 的結果變成可追蹤、可 review、可應用的狀態輸出。

## 0. 一句話

**Sean-KB 的維護不是整理資料，而是讓 input 經過診斷場後產生火花；Sean-KB 的應用不是查筆記，而是把火花導向 decision、writing、case、playbook。**

## 1. Scope

適用於：

- Readwise Reader document
- Reader Library / Inbox 主題盤點
- 已存入 `sources/` 的乾淨 Markdown article
- 其他需要透過 `/kb-loop` 消化的外部材料

不適用於：

- 純格式整理、frontmatter 修補、OKF export/lint
- 未經 Sean 生成效應的 AI 摘要入庫
- 大批量自動建卡或自動 wikilink

## 2. Input 狀態機

每個 Reader item / source candidate 至少落在一個狀態：

```text
captured
triaged
shortlisted
diagnosis_ready
diagnosis_in_progress
promote_candidate
promoted
archived
rejected
```

| State | 意義 | 下一步 |
|---|---|---|
| `captured` | 已進 Reader / sources，但尚未判斷價值 | AI triage |
| `triaged` | 已初步判斷主題與可能價值 | Sean 選題 |
| `shortlisted` | 值得進一步處理，但尚未開診斷場 | 產最小刺激問句 |
| `diagnosis_ready` | 準備請 Sean 先答／先重述 | `/kb-loop` |
| `diagnosis_in_progress` | 正在蘇格拉底／費曼／steelman／案例遷移 | 繼續追問或補洞 |
| `promote_candidate` | 已產生可審候選洞見、連結、應用出口 | Sean review |
| `promoted` | 已沉澱進 `notes/`、`maps/`、`wiki/` 或 playbook | 補 evidence / link / MOC |
| `archived` | 保留在 Reader/source，但不推進 | 結案 |
| `rejected` | 判斷不值得保留或重複 | 結案 |

## 3. `/kb-loop` 結尾固定輸出

每次 `/kb-loop` 結束，不一定要建卡，但必須輸出一段可複製、可回填、可 review 的結果：

```yaml
kb_loop_result:
  source:
    reader_id:
    source_path:
    title:
    source_type: reader | article | book | transcript | other
  learning:
    sean_claim:
    ai_diagnosis:
    blind_spots:
    earned_links:
      - target:
        why:
  maintenance:
    current_state:
    next_state:
    next_action:
    why_not_promoted_yet:
    evidence_level: pointer | excerpt | snapshot | none
  output:
    output_target:
      - decision
      - writing
      - case
      - playbook
      - teaching
      - not_yet
    suggested_artifact:
    where_to_use:
    first_next_step:
```

### 3.1 欄位判準

- `sean_claim`：Sean 先答、先重述、先套用的核心說法；沒有這欄，代表生成效應不足。
- `ai_diagnosis`：AI 追問後看見的假設、跳躍、矛盾或未定義概念。
- `blind_spots`：Sean 可能尚未看到的風險、反例、遷移限制。
- `earned_links`：只有「走這條線會產生單卡得不到的理解」才列；每條必須有 `why`。
- `why_not_promoted_yet`：防止 `AI summary → Obsidian` 的假進步。
- `output_target`：本次火花可能流向哪個應用出口。

## 4. Promote Gate

進入 `promote_candidate` 後，仍不得直接建卡。先檢查：

- [ ] Sean 是否已先答／先重述？
- [ ] 是否至少經過一輪診斷追問？
- [ ] 是否產生 Sean 自己的案例、反方或應用場景？
- [ ] 是否有 earned link？若沒有，是否仍是值得保留的長期概念？
- [ ] 是否有 `output_target`？
- [ ] 是否有足夠 evidence：pointer / excerpt / snapshot？
- [ ] 如果只是漂亮摘要，是否應留在 Reader 而非進 Obsidian？

## 5. Output Ports

每個 promote candidate 要盡量指向一個 output port。

| Output Port | 用途 | 輸出格式 |
|---|---|---|
| PMBA Lens | 把課堂、案例、文章轉成管理學習資產 | 概念 → 課堂連結 → 我的工作案例 → 可討論問題 |
| Export Logistics / Digital Transformation Lens | 把工作事件轉成流程改善、ERP、自動化、組織協調洞察 | 事件 → 流程瓶頸 → 權責/資訊流 → 自動化點 → MVP/SOP |
| Parenting / Learning Lens | 把 AI 學習、育兒、正向教養文章轉成家庭實踐原則 | 主張 → 風險/收益 → 父母不可外包的判斷 → 可執行行為 |
| Writing Lens | 把診斷場火花轉成文章或報告素材 | 核心洞見 → 反直覺點 → Sean 案例 → 讀者卡點 → 大綱 |
| Agent Playbook Lens | 把有效流程變成 skill / SOP / checklist | 觸發條件 → input → agent 可做 → Sean 必須判斷 → output → 驗收標準 |

若 `output_target: not_yet`，仍可 promote，但必須說明它為什麼是長期概念資產，而不是一篇文章的摘要。

## 6. Dashboard 銜接

本檔只定義狀態與輸出，不強制建立 dashboard。流程穩定後，交給 #7 的 Bases dashboard：

- Promote Queue：`current_state in [shortlisted, diagnosis_ready, diagnosis_in_progress, promote_candidate]`
- Link Review Queue：列出 `earned_links` 中尚未 approve 的候選
- Knowledge Health Queue：列出 evidence 不足、缺 source、frontmatter 不完整、久未 review 的材料

判準：

```text
MOC answers: 我如何理解這個主題？
Bases answers: 下一個該 review 什麼？
```

## 7. 最小落地順序

1. 先讓 `/kb-loop` 每次結束都輸出 `kb_loop_result`。
2. 用 `session-continuity.md` 指定的父母篇跑一次完整流程。
3. 只把通過 promote gate 的洞見進 Obsidian。
4. 再視需要建立 Bases Promote Queue。
5. 最後才補 evidence policy 與 snapshot 分級。

## 8. 驗收標準

- [ ] `/kb-loop` 結尾可穩定輸出 `kb_loop_result`。
- [ ] Reader item 能標記 `current_state` / `next_state`。
- [ ] promote candidate 必須標記 `output_target`。
- [ ] 至少用父母篇跑一次完整流程。
- [ ] 至少產出一個真實應用：文章大綱、育兒原則、PMBA case reflection、或 agent playbook。
