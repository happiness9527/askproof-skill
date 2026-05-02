# Claude Code Done Check Example

## Fictional Context

Tool: Claude Code

Project: CourseBoard, a small course admin dashboard.

## User Input

```text
Claude Code 说：
I updated the enrollment validation and fixed the failing state transition. I did not run the full test suite because dependencies are not installed.
```

## AskProof Output

```text
当前判断：Done Check｜完成验收

用户真正的问题：
你想知道 Claude Code 的修改是否足够可信，尤其是它明确说没有跑完整测试。

AI 当前说法是否可信：
完成可信度：中偏低。它说明了修改方向，但没有提供完整验证证据。

已确认的信息：
- AI 声称更新了报名校验。
- AI 声称修复了状态流转问题。
- AI 明确说没有运行完整测试。

未确认的信息：
- 原来的失败场景是否复现过。
- 修复后报名流程是否真的通过。
- 没安装依赖会不会导致其他检查也没跑。
- 是否有最小手动验收步骤。

风险点：
- 如果继续新增课程功能，后面很难判断问题来自报名校验、状态流转，还是新功能。

下一步最稳妥动作：
让 AI 把已修改、已验证、未运行、风险分开列出来。

可直接复制给 AI 的 Prompt：
Please separate this into “changed”, “verified”, “not run”, and “risk”. For every skipped check, explain why it was skipped and what minimum command or manual step I should ask the next AI to run.

你现在最应该问 AI 的一句话：
请按“已修改 / 已验证 / 未运行 / 风险”说明这次结果，并给出最小验收步骤，不要只说已经修好。
```

