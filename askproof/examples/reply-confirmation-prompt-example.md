# Reply Confirmation Prompt Example

Use this when the AI has replied, but the user needs a clearer next prompt to send back.

## User Input

```text
The AI said:

"I changed auth.py and updated the login flow. It should work now."

I want to ask Codex to continue, but I do not want it to blindly add more features.
```

## AskProof Output

```text
当前判断：Reply Confirmation Prompt｜回复后确认 Prompt

当前目标：
确认登录失败问题是否真的修好。

当前状态：
AI 声称修改了 auth.py 和登录流程，但没有提供明确验证结果。

Agent 本轮声称完成 / 修改 / 判断了什么：
- Agent 声称修改了 auth.py。
- Agent 声称更新了登录流程。
- Agent 判断登录流程现在应该可用。

从 Agent 回复里能确认什么：
- AI 声称修改了 auth.py。
- AI 声称更新了登录流程。

仍未确认 / 缺少哪些证据：
- 原来的登录失败是否已经消失。
- 是否运行过登录流程。
- 是否有测试、日志、截图或人工验收结果。

做之前必须先注意什么：
- 当前只能确认 Agent 声称改了代码，不能确认登录功能已经可用。
- 在验收登录修复前，不要扩展新功能。

本次要求 Agent 怎么做：
- 先说明原登录失败是什么。
- 再说明具体改动和验证方式。
- 如果没有验证，必须标注“未验证”。

约束和不要做什么：
- 不要编造验证结果。
- 不要把“已修改”当成“已验证”。
- 不要做与登录修复无关的重构。

验收要求：
- 至少提供登录流程的运行证据、测试输出、截图，或可复现的手动验收步骤。

最后必须输出什么：
- 已修改
- 已验证
- 未验证
- 当前风险
- 下一步最稳妥动作

可直接复制给 Agent 的 Prompt：
请基于当前登录修复继续，但先不要新增功能。

当前目标：
确认登录失败问题是否真的修好。

当前状态：
你说已经修改 auth.py，并且登录流程应该可用，但我还没有看到验证证据。

本次你需要先确认：
1. 你修复的具体登录问题是什么；
2. 你修改了哪些文件或行为；
3. 你是否运行或手动检查过登录流程。

本次执行要求：
1. 如果已经验证，请给出命令、截图、日志或手动步骤和结果；
2. 如果没有验证，请明确标注“未验证”；
3. 在登录修复验收前，不要扩展新功能。

约束：
- 不要编造验证结果；
- 不要把“已修改”当成“已验证”；
- 不要做与登录修复无关的重构。

最后请输出：
1. 已修改；
2. 已验证；
3. 未验证；
4. 当前风险；
5. 下一步最稳妥动作。

你现在最应该问 AI 的一句话：
请先基于当前登录修复说明已修改、已验证、未验证和风险；如果没有验证，请明确标注“未验证”，不要继续扩展新功能。
```
