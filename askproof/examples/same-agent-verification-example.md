# Same-Agent Verification Example

## Fictional Context

Tool: Claude Code or Codex

Project: TutorFlow, a fictional teaching assistant app.

Feature: “Explain while operating” sync. The app should keep narration text synchronized with the
visible operation steps during a guided demo.

The current AI agent can inspect the local project, Git history, and available project files.

## User Input

```text
AI 说“边讲解边操作同步功能已修复”。你能不能在当前项目里判断它是不是真的修好了？
```

## AskProof Output

```text
当前判断：Same-Agent Verification Mode｜同一 Agent 自检模式

用户真正的问题：
你不是只想知道代码有没有改，而是想知道“边讲解边操作同步功能”是否真的能正常工作。

AskProof Acceptance Brief

1. 当前问题
边讲解边操作时，讲解内容和页面操作步骤需要同步。

2. AI 的完成声明
AI 声称“边讲解边操作同步功能已修复”。

3. 已确认事实
- 当前项目中存在同步相关实现代码。
- 最近提交中有与 sync、narration、step timing 相关的修改。
- 这些信息只能证明实现存在，不能直接证明用户看到的同步效果正常。

4. 已有证据
- L1 代码证据：存在相关文件实现、diff 或提交记录。
- L2 日志证据：暂无最新运行日志。
- L3 视觉证据：暂无最新录屏或截图。
- L4 用户验收证据：暂无用户亲自跑通确认。
- L5 可复现证据：暂无完整复现步骤和期望结果。

5. 缺失证据
- L2 日志证据：需要一次最新运行或测试输出。
- L3 视觉证据：需要最新录屏，证明讲解文字与操作步骤同步。
- L4 用户验收证据：需要用户或验收者亲自跑一次并确认。
- L5 可复现证据：需要明确步骤，让别人也能复现同样结果。

6. 完成可信度：中
有实现代码和相关提交，所以不能说完全没有进展。但缺少最新运行证据和视觉证据，所以不能判定“已验证”。

7. 当前状态：已修改 / 部分验证
目前更准确的状态是：已修改，但未充分验证。不建议继续扩展新功能。

8. 最小验收动作
Minimum Acceptance Path｜最小验收路径

1. 打开什么页面 / 执行什么命令：
打开 TutorFlow 的虚构演示页面，或执行项目 README 中记录的本地启动命令。

2. 观察哪个功能点：
启动“边讲解边操作”演示，观察每一步操作出现时，讲解文本是否同步切换。

3. 什么现象算通过：
连续完成 3 个以上操作步骤时，讲解文本与页面操作保持一致，没有提前、延迟或错位。

4. 什么现象算失败：
讲解文本停在上一项、提前跳到下一项、与当前操作不一致，或演示过程中断。

5. 需要保存什么证据：
保存一段 10 到 30 秒的录屏，或至少保存关键步骤的截图和运行日志。

6. 失败后应该把什么发给 AI：
发送录屏、最后一行错误、当前步骤编号，以及你看到的不同步现象。

9. 下一句该怎么问 AI
请针对 TutorFlow 的“边讲解边操作同步功能”先不要继续扩展新功能。请说明已有的 L1 代码证据和提交记录，补充一次最新运行验证，并提供 L3 录屏或 L5 可复现步骤。不要只说代码已修改；如果没有实际运行或录屏，请标注“未充分验证”。

你现在最应该问 AI 的一句话：
请针对 TutorFlow 的“边讲解边操作同步功能”先不要继续扩展新功能。请说明已有的 L1 代码证据和提交记录，补充一次最新运行验证，并提供 L3 录屏或 L5 可复现步骤。不要只说代码已修改；如果没有实际运行或录屏，请标注“未充分验证”。
```

