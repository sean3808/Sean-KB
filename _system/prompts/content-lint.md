# Content Lint / Consistency Check

先執行唯讀機械檢查（沿用 OKF exporter 的 PyYAML 依賴）：

```bash
python _system/scripts/lint_ingestion.py
# 沒安裝 PyYAML 時：uv run --with pyyaml python _system/scripts/lint_ingestion.py
```

檢查 notes／sources／maps／wiki 的 frontmatter、唯一 id、wikilink 檔案目標；新 `ingestion_version: 1` 檢查 Source Selection 欄位、lifecycle、quality、Source Tree node／parent／cycle、evidence 與 source_ref 配對、page range、個人立場證據。unknown fields 保留；舊卡缺新欄位只警告，不降為 candidate。歷史驗證欄位不自動改寫。

**機械通過不是語意通過**。Agent 必須另讀來源、相關卡與完整 diff：

- 實際 Sean 指示是否支持 selection_evidence？禁止 AI 自找來源假填 approved。
- 來源版本、章節／頁碼／pointer 是否真能定位？腳本只驗形狀與 file target，不能驗外部存取／原文真實性／heading anchors。
- 全來源覆蓋完整嗎？Source Tree 是否忠於原文，OCR／table 數字是否可靠？
- 一卡是否一個獨立、可複用語意？是否重複既有概念、只有摘要、機械拆卡或大量原文？
- claim_origin 是否正確？有沒有把作者規範性主張冒充 Sean、用 AI 推論冒充 source？
- 每條 knowledge link 是否 earned 且有 context？僅同主題改用 tag／MOC；新卡可由適當 MOC 發現嗎？
- 有沒有未授權永久 ingest、覆寫個人原則、刪除或大改高價值 note？真正例外只暫停 affected mutation。
- Source Integration 的 coverage、結果、階段、例外是否反映實際完成情況？

可修的一般問題由 AI 修好再檢查；技術阻塞如實回報，不能改造成逐卡 Sean review。Source Tree／Knowledge Graph 互補，lint 不要求所有卡一定有跨域 link，也不要求每 source 獨立 MOC。

必要 export 才跑 `_system/prompts/okf-lint.md`；不為純 ingestion 常駐生成 `_okf/`。
