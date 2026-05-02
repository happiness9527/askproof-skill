# AskProof

**Don’t just ask AI to continue. Ask for proof.**

AI agents often say “done”, “fixed”, or “should work now”.

But if you are not an engineer, how do you know whether it is actually done?

AskProof helps non-engineers check what the AI did, what evidence is missing, what is still unverified, and what to ask next.

AskProof does not ask you to become an engineer. It gives you better acceptance questions.

## What Is AskProof

AskProof is an AI acceptance and follow-up Skill for non-engineers.

It helps you review an AI agent’s “done” message and turn vague feedback like “still broken” or “continue” into a clear prompt that asks for proof, minimum evidence, and a safer next step.

AskProof helps non-engineers ask AI agents for the right proof before trusting “done”.

## Who It Is For

AskProof is built for people using AI agents without being professional developers:

- founders and solo builders
- product managers
- operators
- designers
- content creators
- education product owners
- anyone using Claude Code, Codex, Cursor, OpenClaw, or other AI tools to build software, automations, content workflows, or internal tools

You do not need to know Git, terminals, logs, stack traces, or test commands.

## Why AI Agent Summaries Are Not Enough

AI agents can summarize their work confidently even when they have not verified it.

Common weak summaries include:

- “Fixed.”
- “Should work now.”
- “The issue has been resolved.”
- “I updated the code and everything is ready.”

These may mean the AI changed files. They do not automatically mean the result was tested, verified, or safe to continue building on.

AskProof separates:

- what was changed
- what was actually verified
- what evidence was provided
- what is still unknown
- what you should ask next

## How AskProof Is Different From Verification Tools

AskProof does not replace your tests, CI, PR review, or verification tools.

It helps non-engineers ask better follow-up questions when AI agents claim work is done.

Other tools may help an agent submit verification evidence. AskProof helps the human user ask for that evidence, understand it, and avoid being carried along by confident but unproven AI summaries.

## Core Features

### 1. Done Check

Checks whether an AI agent’s “done”, “fixed”, or “should work now” message is believable.

It reports:

- completion confidence: low, medium, or high
- current status: changed, verified, unverified, risky, safe to continue, or not recommended to continue
- evidence the AI provided
- missing evidence
- how the user can accept the result
- the next prompt to send to the AI

### 2. Prompt Rescue

Turns low-quality feedback into a clear prompt.

Examples of weak feedback:

- “still broken”
- “continue”
- “just fix it”
- “fix it yourself”
- “don’t make bugs”

AskProof explains why the feedback is inefficient and rewrites it into a prompt that asks the AI to restate the failure, list what changed, request minimum evidence, avoid blind refactors, and define the next verification step.

### 3. Evidence Ladder

AskProof does not assume you know logs.

When information is missing, it asks for the easiest useful evidence first:

- L0: you only know “it does not work”
- L1: you can describe what you see
- L2: you can share a screenshot
- L3: you can paste the AI’s last “done” message
- L4: you can paste the last red error line
- L5: you can provide terminal logs, Git diff, or test results

### 4. Explain

AskProof explains AI technical reports in plain language:

- what the AI is saying
- what it actually did
- what it means for your project
- what has been confirmed
- what has not been verified
- what you should ask next

### 5. Drift Guard

When the task keeps expanding before the previous result is verified, AskProof warns you to slow down and close the loop first.

It helps you decide whether to continue, stop, verify, or create a handoff note.

### 6. Handoff Memory

When the chat is too long or you want to switch models, tools, or platforms, AskProof creates a handoff note with:

- current goal
- completed work
- verified work
- unverified work
- current risks
- key decisions
- next prompt
- mistakes to avoid repeating

## Quick Start Without Memorizing Commands

You can write naturally:

- “AI says it is fixed. Is it really done?”
- “still broken”
- “I do not understand this error.”
- “Rewrite this into a better prompt.”
- “I am opening a new chat. Create a handoff.”
- “What did this round actually do?”
- “What should I ask the AI now?”

Optional advanced commands are also supported:

- `/askproof done-check`
- `/askproof prompt-rescue`
- `/askproof evidence`
- `/askproof explain`
- `/askproof drift-guard`
- `/askproof handoff`

## Example: AI Says “Fixed”

User:

> The AI said: “Fixed. It should work now.”

AskProof:

```text
Current scenario: Done Check
Completion confidence: Low
Current status: changed claim, unverified

What is confirmed:
- The AI claims it made a fix.

What is not confirmed:
- Which files changed.
- Whether the app was run.
- Whether the original failure disappeared.
- Whether any test, screenshot, or manual check was done.

Risk:
- If you continue adding features now, later failures may be harder to trace.

Safest next action:
- Ask the AI to provide proof before making more changes.

You should now ask the AI this one sentence:
Please do not continue building yet. First show what you changed, what exact verification you ran, the result of that verification, and what remains unverified.
```

## Example: User Says “Still Broken”

User:

> still broken

AskProof rewrites it:

```text
This feedback is too vague because the AI does not know what failed, where you saw it, or what changed since the last attempt.

Copy this prompt:
Please stop making broad changes. First restate the current failure in plain language, list the files you changed in the previous attempt, explain the most likely failure point, tell me the smallest evidence you need from me, and do not refactor unrelated code before we verify the current fix.
```

## Example: User Does Not Know How To Provide Logs

AskProof does not say only “send logs”.

It says:

```text
You do not need to understand logs. Send any one of these:
1. A screenshot of the current page.
2. The AI’s last “fixed/done” message.
3. The last red error line from the page or terminal.
4. A plain-language description of what you clicked and what happened.
```

## Example: Handoff For Next Chat

AskProof can generate a handoff before switching tools:

```text
Current goal:
Make the fictional “TinyInvoice” app export invoices as PDF.

Completed:
- Added an export button.
- Connected the button to a PDF export function.

Verified:
- None provided yet.

Unverified:
- Whether the PDF downloads.
- Whether invoice totals are correct.

Current risk:
- The AI may have changed UI code without proving the export flow works.

Next prompt:
Please continue from this handoff. Do not add new features until you verify that the PDF export button downloads a PDF with the correct invoice total.
```

## Installation

For Codex-style local skills, copy the `askproof/` directory into your skills directory, then restart or reload your agent environment.

See [docs/install.md](docs/install.md) for step-by-step instructions.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

V0.1 focuses on:

- clear README and examples
- the AskProof Skill instructions
- reference templates
- fictional demos
- lightweight local memory helpers

It does not include integrations, a UI, background services, PR bots, or automatic test execution.

## License

MIT. See [LICENSE](LICENSE).

