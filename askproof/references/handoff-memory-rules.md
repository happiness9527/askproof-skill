# Handoff Memory Rules

Use Handoff Memory when the user wants to switch chat, model, platform, or AI agent.

## Required Sections

1. Current task goal.
2. Completed work.
3. Verified work.
4. Unverified work.
5. Current risks.
6. Key decisions.
7. Next copy-ready prompt.
8. Mistakes to avoid repeating.

## Do Not Invent

If something is unknown, write:

- “暂无证据”
- “未验证”
- “从当前信息无法确认”

Do not fill gaps with assumptions.

## Recommended Handoff Prompt

```text
请根据以下交接说明继续。先复述当前目标、已完成内容、已验证内容、未验证内容和风险。不要直接扩展新功能。请先提出最小验证步骤，证明当前修改是否真的生效。
```

## Local Memory Path

Default path:

```text
docs/askproof-memory/
```

Suggested structure:

```text
docs/askproof-memory/
├── current-status.md
├── sessions/
├── handoff/
│   └── latest-handoff.md
├── risks/
└── index.json
```

Ask for confirmation before writing files.

