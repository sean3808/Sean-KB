# ISSUE-03：移除 Memories 自我更新機制，改 localized 預設準則

**Labels:** `priority:medium` `type:enhancement` `area:system-prompt`
**Status:** open

## Context

System Prompt §6「Memories（偏好記憶）」要求 Notion AI：「在本指令頁的 Memories 區更新一條 bullet」，並維護 §6.1 一串偏好條目。

Sean 說明原意：當時是想**展示這個 Agent 包含「記憶」功能**。

## Problem

1. **可能空轉**：§2.1-7 明說 Notion AI 不能改設定；它能否改自己這頁 System Prompt 內文存疑。若不能，§6 整套自我更新是「寫了但跑不動」的死規則。
2. **違反 localize 原則**：在 Notion 這種環境，變更更該**寫進專案文件**（localized），而非靠 AI 自我改 prompt。自我改 prompt 是不透明、不可版控的狀態漂移。

## Proposal

- **移除** §6 的「自我更新 bullet」機制。
- §6.1 現有偏好條目 → **固化為 System Prompt 的「預設準則（default 準則）」**：靜態、不由 AI 自我變更。
- 未來偏好調整由 **Sean 改文件**（或透過專案文件 localize），不由 AI 自寫。

## Acceptance Criteria

- [ ] §6 自我更新機制移除，無「AI 自我寫入本頁」指令殘留
- [ ] §6.1 內容轉為「預設準則」段落（措辭從「動態新增/更新」改為靜態準則）
- [ ] 偏好變更路徑明確指向「改文件」而非「AI 自記」

## Related

- ISSUE-04（同樣收斂到「預設準則」這個形態）
