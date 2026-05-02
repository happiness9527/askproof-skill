# Quick Start For Non-Engineers

You do not need to learn commands.

Use AskProof when an AI agent says something that sounds finished, but you are not sure whether to trust it.

## Say This

```text
AI says it is fixed. Is it really done?
```

AskProof will check whether the AI provided proof.

## If Something Still Fails

Instead of:

```text
still broken
```

AskProof will help you ask:

```text
Please stop making broad changes. First restate the current failure, list what you changed last time, tell me the smallest evidence you need from me, and explain how you will verify the next fix.
```

## If You Do Not Understand Logs

You can provide any one of these:

1. A screenshot.
2. The AI’s last “fixed” message.
3. The last red error line.
4. A plain-language description of what happened.

## If The Chat Is Too Long

Say:

```text
I am opening a new chat. Create a handoff.
```

AskProof will create a compact handoff for the next AI.

