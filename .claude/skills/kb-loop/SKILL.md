---
name: kb-loop
description: >
  Sean-KB 的「維護＝學習」迴圈執行介面：把一篇 Reader 文章、一份新材料、或一個想學的主題，
  透過蘇格拉底／費曼診斷對話消化進 vault，產出候選連結與 output target 交 Sean 審。核心是診斷場、不是 AI 摘要工廠。
  Use when: Sean 說 /kb-loop、「跑診斷場」、「消化這篇」、「把這個學進來」、「處理 Reader」、「織網」、
  要把外部材料沉澱進 Sean-KB、或要對某主題做診斷式學習。
  Not for: 機械 lint（走 okf-lint）、OKF export（走 okf-exporter）、純檔案搜尋。
---

# kb-loop — Sean-KB 維護＝學習迴圈

> 完整流程、理由與方法論對照：`_system/prompts/maintenance-learning-loop.md`（流程層 SSOT）＋
> `notion-pages/學習科學方法論.md`（方法論層 SSOT）。Reader input 狀態機與 output ports 見
> `_system/prompts/reader-kb-loop-state-machine.md`。本檔是可觸發的精簡執行層。

## 鐵律（不可違反）

```
AI 產候選連結與診斷場；Sean 做高價值判斷與內化。
人不手工拉所有線；人只審哪些線真的有意義。
連結預設可疑，回 source 判斷。
```

兩條護欄：
- **生成效應**：永遠 **Sean 先講／先答／先重述，AI 才補與改**。禁止先丟摘要。
- **合意困難**：每個自動化先問「這是無益摩擦（找資料/排版/初步解釋→可去）還是學習必要摩擦（提取/自我解釋/判斷→必留）？」AI 只去前者。

**觸發判準（要不要跑診斷場）＝基礎穩不穩**：基礎穩（新答案卡進既有理解、能自驗）→ 快答即可，**別硬跑診斷場**；無基礎／基礎可疑（放不上既有基礎、或錯了也不會察覺）→ 才跑診斷場。詳見 SOP §1。

## 執行步驟

1. **最小刺激**：給材料的一句核心或一個切入問，**不摘要**。
2. **逼生成**：要 Sean 先用自己的話回應／套真實場景（PMBA／出口物流／IT／育兒）。
3. **診斷**：用蘇格拉底追問／費曼重述／steelman／案例遷移／source 對照，戳假設、跳躍、誤判、未連結處。
4. **補洞**：診斷後才補背景、反例、AI 視角。
5. **候選連結**：整理高價值候選交 Sean 審——**不硬接、不預綁某主題**。
6. **Output target**：判斷火花要流向 decision／writing／case／playbook／teaching，或暫時 `not_yet`。
7. **沉澱**：Sean 判斷哪些值得進 `notes/`（promote gate）；已內化／無新知 → 不寫卡。
8. **收尾輸出**：不管是否建卡，都輸出 `kb_loop_result`，讓 input 可追蹤、可 review、可續跑。

## 收尾輸出契約（必填）

每次 `/kb-loop` 結束時，輸出下列 YAML block；缺欄位就明確寫 `null` 或 `not_yet`，不要省略：

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

### 狀態判準

Reader / source input 的最小狀態：

```text
captured → triaged → shortlisted → diagnosis_ready → diagnosis_in_progress → promote_candidate → promoted / archived / rejected
```

- 沒有 Sean 先答／先重述：不得進 `promote_candidate`。
- 只是漂亮摘要：`why_not_promoted_yet` 必須寫「缺 Sean 生成／缺診斷／缺應用出口」。
- 語意相似不是 earned link；earned link 必須有一句 `why`。

## Output ports

| Output target | 何時用 | 典型產物 |
|---|---|---|
| `decision` | 幫 Sean 做工具選型、流程判斷、工作/生活決策 | decision memo / trade-off table |
| `writing` | 可轉成文章、報告、PMBA 作業、專欄 | outline / thesis / argument map |
| `case` | 可變成工作、PMBA、家庭或職涯案例 | case note / reflection |
| `playbook` | 可重複執行的流程 | SOP / skill / checklist |
| `teaching` | 可用來教人或對家人/同事溝通 | explanation script |
| `not_yet` | 暫時只是候選概念 | 保留但不急著 promote |

## 連結兩層護欄（反「為了連結而連結」）

- **導航層**（tag／MOC／adjacent-MOC）：categorical，可大方連。
- **知識層**（note↔note wikilink）：**必須 earned**——「走這條線有沒有產生單卡得不到的理解？」沒有就別連，用 tag/MOC。
- 多數卡是主題內、無跨域連結，**正常**。跨域連結稀少珍貴，等它冒出來，不製造。

## 邊界

- 不退化成 `Reader → AI 摘要 → Obsidian`。
- 修改既有 promoted note 前先出 Git diff（vault Safety 規則）。
- 排程化不在本 skill；本 skill 是互動式診斷場執行。
