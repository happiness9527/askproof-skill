# Quick Start For Non-Engineers

You do not need to learn commands.

Use AskProof when an AI agent says something that sounds finished, but you are not sure whether to
trust it.

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

## If The AI Replied But You Do Not Know What To Say Next

Say:

```text
Turn this AI reply into the next prompt I should send.
```

AskProof will create a structured Reply Confirmation Prompt with the current goal, current status,
what must be checked before continuing, constraints, proof needed, and the final output expected
from the AI.

AskProof does not automatically listen to agent replies. Use this when you invoke AskProof after a
reply or paste the reply into the chat.

## Useful Links

- [AI Acceptance Checklist](acceptance-checklist.md)
- [Prompt Library](prompt-library.md)
- [Example Gallery](example-gallery.md)
