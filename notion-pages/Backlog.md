---
title: Backlog Page
---

<callout icon="🗄" color="gray_bg">
	本頁是 [Obsidian AI LLM Wiki 控制頁](https://app.notion.com/p/afa08ead8bbb4f4ca4f3f296b631e102) 的 **Backlog／封存行動筆記（防彈筆記法）**。收三類：① 已決定不要的選項（附理由，避免未來重複爭論）② 暫緩、未來可評估的 backlog ③ Deep Research 完成後被 v1.2 報告取代的歷史素材。母頁＝控制檯（只放正在推進的決策與行動），本頁＝封存區，兩者互引。
</callout>
## 🚫 已決定不要（封存決策）
> 重點是寫下「為什麼不要」，未來想重啟時先看這裡。
- **Local LLM／Ollama ｜ 永久排除（2026/06/25 拍板）**
	- 理由：Windows 11 中階筆電（i7-1165G7／16GB RAM／MX350 2GB）跑不動有意義的本地模型；採「雲端高能力模型 ＋ 本地檔案 agent（Claude Code）」更務實。
	- 連帶排除：本地 RAG 全自託管（架構模式 B）、AnythingLLM／Mini-RAG 等本地推理路線。
- **架構模式 B（本地 LLM 全自託管）｜ 排除**
	- 理由：同上，硬體與維護成本不划算；改採模式 C 的具體版（Obsidian + Claude Code + 雲端 LLM）。
- **Graph view 當成功指標 ｜ 排除**
	- 理由：v1.2 §1.2 明示成功定義是「可長期複用的卡片 ＋ 能推進行動」，不是漂亮的關係圖。
## ⏸ 暫緩／未來可評估（Backlog）
> 現在不做，但保留未來重啟的條件。
- **向量庫／RAG 當主路徑**：本階段排除；未來卡片量變大、語意檢索需求明確再評估（v1.2 G.1 第二階段）。
- **Notion Workers**：列第二階段；部署需 Business 方案以上，現階段先用 `ntn` 本地腳本即可。
- **雙向同步插件（obsidian-notion-sync）**：不採用，改用「雙向異步引用」；保留為未來若需 properties 級索引的候選。
- **Notion 官方 Importer**：單向（Notion → Obsidian），只用於一次性遷移，不作同步。
- **其他 Obsidian AI 工具（Smart Connections／Obsidian Copilot／Khoj／Zettelkasten LLM Tools）**：非主路徑（主路徑＝Claude Code）；保留為未來補充工具候選。
---
## 🗄 已用完／被取代的歷史素材（封存參考）
> 以下原放在控制頁，ChatGPT Deep Research 已完成、結論收斂進 [v1.2 研究報告](https://app.notion.com/p/38a597010d2c80408866dcdb6e54dc16) 與控制頁〈穩定決策與共用規則〉，故移此封存，供回溯。
### 📚 Web 研究初稿（2026/06/24）
**🧱 核心方法論：Karpathy 的「LLM Wiki」模式**
- **核心觀點**：知識被 AI「編譯」一次，然後持續更新；不是每次提問都重跑 RAG，而是讓 AI 維護一本隨時可查的個人百科（Wiki）。
- **三動作循環**：Ingest（扔素材）→ Query（從已編譯 wiki 找答案）→ Lint（AI 定期體檢一致性、空洞、矛盾）。
- **延伸資源**：
	- [Data Science Dojo：Obsidian AI Knowledge Base in 9 Steps](https://datasciencedojo.com/blog/obsidian-ai-knowledge-base/)
	- [helloianneo/obsidian-ai-second-brain](https://github.com/helloianneo/obsidian-ai-second-brain)（Obsidian + Claude + Karpathy 方法論 4 階段 12 步）
	- [ModemGuides：Local LLM Knowledge Base With Obsidian (2026)](https://www.modemguides.com/blogs/ai-infrastructure/local-llm-knowledge-base-obsidian-setup-guide)
**🔧 Obsidian × AI 工具選型矩陣（2026 主流方案）**
<table header-row="true">
<tr>
<td>工具</td>
<td>定位</td>
<td>隱私／成本</td>
<td>最適場景</td>
</tr>
<tr>
<td>Smart Connections</td>
<td>本地嵌入＋語意搜尋＋Smart View／Chat</td>
<td>核心免費，Pro 約 \$20/月，本地索引</td>
<td>邊寫邊推薦相關筆記</td>
</tr>
<tr>
<td>Obsidian Copilot</td>
<td>Vault QA、Web/YouTube、agentic</td>
<td>Plus 付費，可接 OpenAI／Claude／Ollama</td>
<td>「跟 vault 對話」主力</td>
</tr>
<tr>
<td>Khoj</td>
<td>開源跨平台 AI second brain</td>
<td>免費自託管，可全本地</td>
<td>重隱私／多裝置／自託管</td>
</tr>
<tr>
<td>Claude Code + Obsidian</td>
<td>Claude 住進 vault 讀寫改 markdown</td>
<td>Claude Pro／Max</td>
<td>把 Obsidian 當 Claude 工作目錄</td>
</tr>
<tr>
<td>Zettelkasten LLM Tools</td>
<td>嵌入／語意搜尋／改寫卡片</td>
<td>免費，需 LLM API</td>
<td>讓 AI 連結／改寫卡片</td>
</tr>
<tr>
<td>Local RAG 自架</td>
<td>全本地 RAG</td>
<td>免費，吃 GPU／記憶體</td>
<td>極度隱私、有硬體</td>
</tr>
<tr>
<td>Notion MCP + Obsidian MCP</td>
<td>單一 agent 操作兩邊（對話式）</td>
<td>MCP 免費，LLM 訂閱</td>
<td>橋接成單一工作流</td>
</tr>
<tr>
<td>Notion CLI（ntn）+ Workers</td>
<td>官方 CLI＋託管 Worker（自動化）</td>
<td>CLI／API 免費；Workers 需 Business＋</td>
<td>排程／批次／git hook／cron</td>
</tr>
</table>
**🌉 與 Notion Workspace 的連接性（兩條互補路線）**
- **1a. Notion MCP（對話式）**：官方 MCP Server 已 GA，可 OAuth 安全存取、以 Markdown 為單位編輯；Obsidian 側有社群 MCP（calclavia、StevenStavrakis）。強項：人在迴圈、自然語言、低門檻；弱項：不適合排程／批次，有幻覺風險。
- **1b. Notion CLI（****`ntn`****）＋ Workers（自動化，2026/05/13）**：`ntn` 所有方案可用（login／api／files／workers／tokens）；Workers 用 TypeScript、Notion 託管，可同步外部資料、暴露 agent tool、接 webhook（部署需 Business＋）。強項：可排程、可版控、確定性高、無幻覺；弱項：要寫腳本。
- **1c. 分工建議**：對話探索／重組 → MCP；重複／高頻／無人化 → CLI＋Workers；混合可在 Claude Code 內同時掛 MCP 與呼叫 `ntn`。
- **同步選項**：① 雙向同步插件 obsidian-notion-sync（只同步 properties，需 Dataview）；② 手動雙向引用（最輕量：Notion URL ↔ `obsidian://` Advanced URI）；③ Notion AI（蒜頭）管控制檯內、Obsidian AI 管知識庫內，透過 MCP 互通不重複維護。
**🃏 卡片盒筆記法（Zettelkasten）在 LLM 時代的演化**
- 基礎心法（不變）：Literature notes → Permanent notes；一卡一事、用自己的話、靠 backlinks 與 MOC 而非資料夾。
- LLM 新動作：AI 建議新卡連舊卡、把 inbox 卡整理成永久筆記草稿、定期「卡片盒體檢」（找孤兒卡／空洞／矛盾）、語意搜尋取代關鍵字。
- 延伸閱讀：[DEV：PKM with Zettelkasten and Obsidian](https://dev.to/yordiverkroost/personal-knowledge-management-with-zettelkasten-and-obsidian-20cj)、[Obsidian Forum：AI empowered Zettelkasten](https://forum.obsidian.md/t/ai-empowered-zettelkasten-with-ner-and-graph-llm/79112)、[Eric J. Ma：Mastering PKM with Obsidian and AI](https://ericmjl.github.io/blog/2026/3/6/mastering-personal-knowledge-management-with-obsidian-and-ai/)。
**🏗 三種主流架構模式**
<table header-row="true">
<tr>
<td>模式</td>
<td>核心組成</td>
<td>優勢</td>
<td>代價</td>
</tr>
<tr>
<td>A. 雲端 AI 加速</td>
<td>Obsidian + Copilot/Smart Connections + OpenAI/Claude API</td>
<td>體驗最好、設定最快、語意品質最高</td>
<td>付費、敏感資料外流風險、依賴雲服務</td>
</tr>
<tr>
<td>B. 本地 LLM 全自託管</td>
<td>Obsidian + Khoj/Mini-RAG/AnythingLLM + Ollama + 本機 embedding</td>
<td>完全隱私、零持續成本、可離線</td>
<td>需硬體、模型較小、門檻高（**已排除**）</td>
</tr>
<tr>
<td>C. 混合（最終採用具體版）</td>
<td>Obsidian 本地 vault + 雲端 LLM 重整 + Claude Code + MCP 橋接 Notion</td>
<td>隱私／成本／體驗平衡</td>
<td>需清楚「什麼上雲、什麼留本地」規則</td>
</tr>
</table>
### 🗂 ChatGPT Deep Research Prompt 種子（已用畢）
> 這批問題已在 v1.2 報告中得到回答，保留供回溯。
1. 比較 Smart Connections vs Obsidian Copilot vs Khoj vs Claude Code + Obsidian，針對「Windows 11 + 中型 vault（\< 5000 卡）+ 跨領域 PKM」哪個 ROI 最高？
2. Karpathy LLM Wiki 方法論的完整來源？成功／失敗案例？對非工程背景在職學習者的已知坑？
3. Notion 連接性 MCP × CLI 分工：哪些用 MCP、哪些必須 `ntn`＋Workers？Workers 需 Business 是否值得？只用 `ntn` 本地腳本的最佳實踐？
4. MCP 橋接 Notion＋Obsidian 的客戶端比較（Claude Desktop／Cursor／ChatGPT／VS Code），權限切割怎麼做？
5. 卡片盒筆記法在 LLM 時代的更新版有哪些書／課程（除 Eric J. Ma、Karpathy）？
6. 資料分級規則：哪些上雲、哪些留本地（工作客戶／家庭育兒／財務／PMBA）？
7. 遷移路徑：Notion 孤兒分支 → Obsidian 的順序與工具？能否用 `ntn`＋Worker 寫一次性遷移腳本？
<page url="https://app.notion.com/p/389597010d2c802ca746c49032c58264">chatgpt_deepresearch_prompt</page>