# AskProof

🌐 Languages: [English](README.md) | [中文](README.zh-CN.md)

> Don’t just ask AI to continue. Ask for proof.

AI agents often say:

- “Done.”
- “Fixed.”
- “Should work now.”

But if you are not an engineer, the real question is not whether the AI sounds confident.

The real question is:

- What did it actually change?
- Did it verify the result?
- What evidence is missing?
- Is it safe to continue?
- What should you ask next?

AskProof is an AI acceptance and follow-up Skill for non-engineers.

AI agents summarize what they did.

AskProof helps you decide whether you can trust it.

It does not do the work for the AI, and it does not replace tests, CI, PR review, or verification
tools. It helps you understand what the AI did, check whether the claim is believable, and turn
vague feedback like “still broken”, “continue”, or “fix it yourself” into a prompt that asks for
proof.

## Try It in 30 Seconds

**The AI says:**

> Fixed. It should work now.

**A normal user might say:**

> Great, continue.

**AskProof reminds you:**

```text
Current scenario: Done Check
Completion confidence: Low
Current status: The AI claims the issue is fixed, but no verification evidence is visible.

Missing evidence:
- What changed.
- How the AI verified it.
- What the verification result was.
- What remains unverified.

You should now ask the AI this one sentence:
Please do not continue building new features yet. First explain what you changed, how you verified it, what the result was, and what remains unverified.
```

## Quick Navigation

- [Why You Need AskProof](#why-you-need-askproof)
- [What AskProof Helps You Do](#what-askproof-helps-you-do)
- [Who It Is For](#who-it-is-for)
- [V0.2 Core Experience Enhancements](#v02-core-experience-enhancements)
- [Try It in 30 Seconds](#try-it-in-30-seconds)
- [Try It Without Installing](#try-it-without-installing)
- [Ask Claude Code / Codex To Install It](#ask-claude-code--codex-to-install-it)
- [Core Features](#core-features)
- [Common Use Cases](#common-use-cases)
- [Examples](#example-1-ai-says-fixed)
- [How It Differs From Verification Tools](#how-it-differs-from-verification-tools)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)

## Why You Need AskProof

AI agent summaries are often useful, but they are not the same as acceptance evidence.

An AI can say:

- “I fixed the bug.”
- “I updated the implementation.”
- “The issue should be resolved.”
- “Everything is ready.”

Those sentences may only mean that files were changed. They do not prove that the original problem
is gone, that the user-facing flow works, or that the next task is safe to start.

AskProof helps you separate:

- what was changed
- what was actually verified
- what evidence was provided
- what is still unknown
- what you should ask next

You do not need to know Git, terminals, logs, stack traces, or test commands.

## What AskProof Helps You Do

AskProof helps non-engineers ask AI agents for the right proof before trusting “done”.

It can help you:

- check whether “done” is actually verified
- identify missing evidence before continuing
- rewrite vague feedback into an actionable prompt
- ask for the easiest useful evidence when you do not know what to provide
- understand AI technical reports in plain language
- stop scope drift before the current work is accepted
- create a handoff note before switching chats, models, or platforms

AskProof is not another AI coding tool. It is an AI acceptance assistant for the human using the
AI tool.

## Who It Is For

AskProof is built for people using AI agents without being professional developers:

- founders and solo builders
- product managers
- operators
- designers
- content creators
- education product owners
- anyone using Claude Code, Codex, Cursor, OpenClaw, domestic agent platforms, or other AI tools

You can use AskProof even if you do not know how to read logs, run tests, inspect diffs, or explain
technical errors.

## V0.2 Core Experience Enhancements

AskProof V0.2 strengthens the acceptance workflow without adding a UI, integrations, or an
automatic test runner.

- **Acceptance Brief**: turns a “done” claim into a structured acceptance result with confirmed
  facts, existing evidence, missing evidence, confidence, status, and next action.
- **Evidence Type**: labels proof as code evidence, log evidence, visual evidence, user acceptance
  evidence, or reproducible evidence.
- **Same-Agent Verification Mode**: helps Claude Code, Codex, or another current agent inspect
  local project evidence instead of only asking the user for logs.
- **Self-contained follow-up prompts**: includes the feature name, target, evidence needed, and a
  stop condition before expanding scope.
- **Minimum Acceptance Path**: gives the smallest practical path to verify the current result.

## Try It Without Installing

You can test the idea in any AI chat by copying this prompt:

```text
Act as AskProof, an AI acceptance and follow-up assistant for non-engineers.

When I paste an AI agent’s “done”, “fixed”, or “should work now” message, do not assume it is true.
Tell me:
1. The current scenario.
2. Whether the claim is believable.
3. What information is confirmed.
4. What information is still missing.
5. The risk of continuing now.
6. The safest next action.
7. One copy-ready prompt I should send back to the AI agent.

Use plain language. If there is no evidence, mark it as unverified.

AI says it is fixed. Is it really done?
```

If AskProof is working, you should see ideas like:

- completion confidence
- confirmed information
- missing evidence
- risk
- next prompt

It should not simply say “yes, it is done”.

After installation, you can also write naturally:

- “AI says it is fixed. Is it really done?”
- “still broken”
- “I do not understand this error.”
- “Rewrite this into a better prompt.”
- “I am opening a new chat. Create a handoff.”
- “What did this round actually do?”
- “What should I ask the AI now?”

Advanced users can still use optional commands:

- `/askproof done-check`
- `/askproof prompt-rescue`
- `/askproof evidence`
- `/askproof explain`
- `/askproof drift-guard`
- `/askproof handoff`

## Ask Claude Code / Codex To Install It

If you use Claude Code, Codex, Cursor, or another AI agent that can work with local files, you can
ask it to install AskProof for you.

Copy this prompt:

```text
Please help me install the AskProof Skill from:
https://github.com/happiness9527/askproof-skill

Goal:
Install the local `askproof/` Skill folder so this AI tool can use it.

Please:
1. Check whether this environment supports local Skills or instruction folders.
2. Download or clone the repository if needed.
3. Copy the complete `askproof/` folder, not only `SKILL.md`.
4. Tell me the exact destination folder you used.
5. Tell me whether I need to restart or reload the app.
6. Verify installation with this test prompt:
   "AI says it is fixed. Is it really done?"

Do not add integrations, background services, or automatic test runners.
```

If your AI tool does not support Skills, ask it to explain the closest supported alternative before
copying files.

## Core Features

### 1. Done Check

Checks whether an AI agent’s “done”, “fixed”, or “should work now” message is believable.

It reports:

- completion confidence: low, medium, or high
- current status: changed, verified, unverified, risky, safe to continue, or not recommended
- evidence the AI provided
- missing evidence
- how the user can accept the result
- the next prompt to send to the AI

### 2. Prompt Rescue

Turns low-quality feedback into a clear prompt.

Weak feedback includes:

- “still broken”
- “continue”
- “just fix it”
- “fix it yourself”
- “don’t make bugs”

AskProof explains why the feedback is inefficient and rewrites it into a prompt that asks the AI to
restate the failure, list what changed, request minimum evidence, avoid blind refactors, and define
the next verification step.

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

When the task keeps expanding before the previous result is verified, AskProof warns you to close
the loop first.

It helps you decide whether to continue, stop, verify, or create a handoff note.

### 6. Handoff Memory

When the chat is too long or you want to switch models, tools, or platforms, AskProof creates a
handoff note with:

- current goal
- completed work
- verified work
- unverified work
- current risks
- key decisions
- next prompt
- mistakes to avoid repeating

## Common Use Cases

AskProof is useful when:

- Cursor says it fixed a UI bug, but you did not see a screenshot or browser check
- Claude Code reports file edits, but skipped tests
- Codex ran a technical check, but you are unsure whether it proves the user-facing issue
- a domestic agent platform says “fixed and redeployed”, but gives no evidence
- a product manager only knows how to say “still wrong”
- a designer sees the UI still looks off but cannot describe it in engineering terms
- an operator wants an automation fixed without blindly approving another rewrite
- a creator or education product owner needs a handoff before opening a new chat

See the [example gallery](docs/example-gallery.md) for more fictional but realistic cases.

## Example 1: AI Says “Fixed”

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

## Example 2: User Says “Still Broken”

User:

> still broken

AskProof rewrites it:

```text
This feedback is too vague because the AI does not know what failed, where you saw it, or what changed since the last attempt.

Copy this prompt:
Please stop making broad changes. First restate the current failure in plain language, list the files you changed in the previous attempt, explain the most likely failure point, tell me the smallest evidence you need from me, and do not refactor unrelated code before we verify the current fix.
```

## Example 3: User Does Not Know How To Provide Logs

AskProof does not say only “send logs”.

It says:

```text
You do not need to understand logs. Send any one of these:
1. A screenshot of the current page.
2. The AI’s last “fixed/done” message.
3. The last red error line from the page or terminal.
4. A plain-language description of what you clicked and what happened.
```

## Example 4: The Task Starts Drifting

User:

> The login fix is not verified yet, but please also add a new dashboard and redesign settings.

AskProof:

```text
Current scenario: Drift Guard
Current judgment: Do not expand scope yet.

Reason:
The previous fix has not been verified. If you add new features now, later problems may be hard to trace.

Safest next action:
Ask the AI to prove the current fix works before adding new work.

You should now ask the AI this one sentence:
Please pause new features. First verify the login fix with clear evidence, then summarize what is safe to build next.
```

## Example 5: Handoff For The Next Chat

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

## How It Differs From Verification Tools

AskProof does not replace your tests, CI, PR review, or verification tools.

It helps non-engineers ask better follow-up questions when AI agents claim work is done.

Other tools may help an agent submit verification evidence. AskProof helps the human user ask for
that evidence, understand it, and avoid being carried along by confident but unproven AI summaries.

## Installation

For Codex-style local skills, copy the `askproof/` directory into your skills directory, then
restart or reload your agent environment.

See [docs/install.md](docs/install.md) for step-by-step instructions.

If you do not use Git, see [docs/install-for-non-engineers.md](docs/install-for-non-engineers.md).

Advanced users can start with:

```bash
git clone https://github.com/happiness9527/askproof-skill.git
```

Then copy the complete `askproof/` folder into the Skill directory used by your AI tool.

## Project Structure

```text
askproof-skill/
├── README.md
├── README.zh-CN.md
├── askproof/
│   ├── SKILL.md
│   ├── references/
│   ├── examples/
│   └── scripts/
├── docs/
└── demo/
```

Useful docs:

- [Quick start for non-engineers](docs/quick-start-for-non-engineers.md)
- [AI acceptance checklist](docs/acceptance-checklist.md)
- [Prompt library](docs/prompt-library.md)
- [How it works](docs/how-it-works.md)
- [GitHub publish guide](docs/github-publish-guide.md)

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

V0.1 focuses on:

- clear README and examples
- the AskProof Skill instructions
- reference templates
- fictional demos
- lightweight local memory helpers

It does not include integrations, a UI, background services, PR bots, or automatic test execution.

V0.2 focuses on structured acceptance:

- AskProof Acceptance Brief
- Evidence Type classification
- Same-Agent Verification Mode
- self-contained follow-up prompts
- Minimum Acceptance Path

## License

MIT. See [LICENSE](LICENSE).

## Star

If AskProof helps you avoid blindly trusting “done”, consider starring the repo so more
non-engineers can find it.
