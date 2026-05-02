# Drift Guard Rules

Drift Guard prevents the user and AI from expanding scope before the current result is verified.

## Drift Signals

- New feature requests after an unverified fix.
- “While you are at it” additions.
- Refactors proposed before the bug is understood.
- AI keeps changing files without proof.
- The user wants design polish before the core flow works.
- The conversation is long and the goal is no longer clear.

## What To Say

Be direct but not blocking.

```text
当前不建议继续扩功能。
原因是：上一轮修改还没有验证证据，如果继续新增功能，后面很难判断问题来自哪里。
你现在最应该做的是：先让 AI 证明当前修改已经生效。
```

## Recommended Actions

- Return to the original goal.
- Ask what has changed and what has been verified.
- Request one focused acceptance check.
- Create a short handoff if the conversation is long.
- Continue only after the current result is verified or explicitly accepted as unverified risk.

## Scope-Control Prompt

```text
请先停止新增功能，回到原目标。请列出上一轮已修改内容、已验证内容、未验证内容和当前风险。只有当原目标通过验收后，再讨论新功能。
```

