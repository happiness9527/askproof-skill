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

## Reply Confirmation Prompt

Route here when the user invokes AskProof after an agent reply or pastes an agent reply and wants
the next structured message to send back.

Trigger phrases include:

- what should I send next
- turn this into a prompt for Codex
- make this into a follow-up prompt
- help me confirm with the AI
- 基于这段回复，下一句该怎么问
- 帮我整理成发给 AI 的 Prompt
- 帮我写一段给 Claude Code / Codex 的确认提示
- 这轮 AI 回复后，我该怎么让它继续

Primary question: “How do I confirm status, constrain the next step, and ask for proof without
losing context?”

Behavior:

1. Restate the current goal and current status in plain language.
2. Use only the AI reply and user-provided context; mark unknowns as unconfirmed.
3. Convert the next action into a structured, copy-ready prompt.
4. Include before-continuing checks, requirements, constraints, proof needed, acceptance
   requirements, and final output expectations.
5. If the AI claims completion, include Done Check inside the prompt instead of treating the claim
   as verified.
6. Do not claim automatic monitoring, automatic cross-platform reading, automatic testing, or
   automatic verification.

## Same-Agent Verification Mode

Route here when all of these are true:

- the current AI agent can access project files, Git history, test scripts, or the runtime
  environment
- the user asks whether a feature is really fixed, really complete, or safe to trust
- the user did not only paste another AI’s summary, but wants the current agent to inspect the
  current project state

Trigger phrases include:

- can you verify this feature is really fixed
- check whether this is actually done
- inspect the current repo and tell me if it is verified
- 你看看这个功能是不是真的修好了
- 你能不能在当前项目里验收一下
- 这个功能现在能不能信

Primary question: “Can this same agent inspect enough evidence to accept the current result?”

Behavior:

1. Do not only ask the user for evidence.
2. Inspect available project evidence first when tools are available.
3. Distinguish implementation evidence from runtime evidence.
4. If runnable, propose the smallest runtime verification path.
5. If not runnable or visual evidence cannot be viewed, say so clearly.
6. Finish with a self-contained follow-up prompt.

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
2. If the user asks the current agent to inspect the current repo or runtime, use Same-Agent Verification Mode.
3. If the user explicitly asks for the next message to send to AI, use Reply Confirmation Prompt.
4. If the AI claims done without proof, use Done Check.
5. If the user only says “still broken” or “continue”, use Prompt Rescue.
6. If the user lacks evidence, use Evidence Ladder.
7. If scope is expanding without verification, use Drift Guard.
8. If the user asks what something means, use Explain.
