# Intent Router

AskProof should let users speak naturally. Do not require commands.

## Done Check

Route here when the message includes an AI completion claim:

- done
- fixed
- completed
- should work now
- resolved
- 已完成
- 已修复
- 现在应该可以了
- 问题已经解决
- AI 说修好了

Primary question: “Can I trust this?”

## Prompt Rescue

Route here when the user gives vague feedback:

- still broken
- just fix it
- continue
- fix it yourself
- 还是不行
- 继续
- 你自己解决
- 不要出现 bug
- 重新改
- 怎么又报错了

Primary question: “How do I say this in a way the AI can act on?”

## Evidence Ladder

Route here when the user lacks evidence or says:

- I do not know what to send
- I do not know logs
- where do I find the error
- 我不知道怎么提供日志
- 我只知道不行
- 我不会看终端

Primary question: “What is the easiest useful evidence I can provide?”

## Explain

Route here when the user pastes:

- an AI technical report
- a terminal output
- an error
- a build summary
- a test result
- a diff summary

Primary question: “What does this mean for me?”

## Drift Guard

Route here when the user or AI keeps expanding scope before verification:

- add another feature
- optimize it too
- refactor everything
- while you are at it
- 顺便再做
- 继续扩展
- 再加一个功能

Primary question: “Should we continue building, or verify first?”

## Handoff Memory

Route here when the user says:

- new chat
- context is too long
- switch model
- switch platform
- hand off to another AI
- 我要新开对话
- 上下文太长
- 换模型
- 换平台
- 交给下一个 AI
- 帮我生成交接说明

Primary question: “What should the next AI know?”

## Conflict Handling

If multiple intents appear, choose the one that protects the user from the largest immediate risk:

1. If a handoff is requested, create Handoff Memory.
2. If the AI claims done without proof, use Done Check.
3. If the user only says “still broken” or “continue”, use Prompt Rescue.
4. If the user lacks evidence, use Evidence Ladder.
5. If scope is expanding without verification, use Drift Guard.
6. If the user asks what something means, use Explain.

