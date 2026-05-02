---
name: askproof
description: Use this skill when a non-engineer needs to ask AI agents for proof, check whether “done” is actually verified, rewrite vague feedback such as “still broken” into actionable prompts, request minimum evidence, prevent task drift, or create handoff memory.
metadata:
  short-description: Help non-engineers ask AI agents for proof before trusting “done”.
---

# AskProof

AskProof is an AI acceptance and follow-up Skill for non-engineers.

Use it when the user asks whether an AI agent really finished work, says vague feedback like “still broken”, cannot understand an AI report or error, needs minimum evidence, is drifting into new scope before verification, or wants a handoff for a new chat, model, platform, or agent.

## Core Rules

1. Do not invent verification results.
2. Do not assume the AI has completed the work because it said “done”.
3. If there is no evidence, mark the result as “unverified”.
4. Always distinguish “changed” from “verified”.
5. Always give the user the next sentence to ask the AI.
6. Use language a non-engineer can understand first.
7. Do not require the user to understand code, Git, terminals, or logs.
8. If the user says “continue”, “still broken”, “还是不行”, or “你自己解决”, prefer Prompt Rescue.
9. If an AI says “done”, “fixed”, “completed”, “should work now”, “已完成”, “已修复”, or “现在应该可以了”, prefer Done Check.
10. If information is missing, use the Evidence Ladder before asking for logs.

## Intent Routing

Choose the most useful mode from the user’s message:

- **Done Check**: AI claims work is complete or fixed.
- **Prompt Rescue**: user gives vague feedback or asks for a better prompt.
- **Evidence Ladder**: user does not know what evidence to provide.
- **Explain**: user pastes an AI report, terminal output, or error and says they do not understand it.
- **Drift Guard**: task is expanding before prior work is verified.
- **Handoff Memory**: user wants to open a new chat, switch model/platform, or create a handoff.

Optional commands:

- `/askproof done-check`
- `/askproof prompt-rescue`
- `/askproof evidence`
- `/askproof explain`
- `/askproof drift-guard`
- `/askproof handoff`

## Required Response Shape

Every response should include as many of these as are relevant:

1. Current scenario.
2. The user’s real problem.
3. Whether the AI’s current claim is trustworthy.
4. Confirmed information.
5. Unconfirmed information.
6. Risks.
7. Safest next action.
8. A copy-ready prompt for the AI.

End every response with this exact label:

```text
你现在最应该问 AI 的一句话：
```

Then provide one clear sentence or compact prompt.

## Evidence Ladder

When the user lacks evidence, do not jump straight to “provide logs”.

Offer low-friction options:

1. Current page screenshot.
2. The AI’s last “done/fixed” reply.
3. The last red error line on the page or terminal.
4. A plain-language description of what they saw.
5. Terminal logs, Git diff, or test output if they can provide it.

## Local Memory

AskProof can create handoff and progress memory, but it must not silently write files.

Default memory path:

```text
docs/askproof-memory/
```

If writing memory would help:

1. Generate the content first.
2. Ask the user to confirm writing it.
3. Only then use helper scripts or file edits.

## Reference Files

Load reference files only when needed:

- `references/intent-router.md` for routing ambiguous user messages.
- `references/output-templates.md` for response templates.
- `references/done-check-rules.md` for completion claims.
- `references/prompt-rescue-rules.md` for vague feedback rewrites.
- `references/evidence-ladder.md` for minimum evidence guidance.
- `references/drift-guard-rules.md` for scope drift warnings.
- `references/handoff-memory-rules.md` for handoff documents.
- `references/project-profile-template.md` for optional project context.

