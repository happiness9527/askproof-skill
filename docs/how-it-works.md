# How It Works

AskProof uses intent routing and acceptance templates.

## 1. Detect The Situation

AskProof first decides whether the user needs:

- Done Check
- Prompt Rescue
- Evidence Ladder
- Explain
- Drift Guard
- Handoff Memory
- Reply Confirmation Prompt

## 2. Separate Changed From Verified

AskProof never treats “the AI changed something” as “the work is verified”.

It separates:

- modified work
- evidence
- missing evidence
- remaining risk

## 3. Ask For The Minimum Useful Evidence

AskProof does not start with “send logs”.

It asks for the easiest evidence the user can provide, such as a screenshot, AI last reply, red
error line, or plain-language symptom.

## 4. Produce The Next Prompt

The final output always gives the user one sentence or compact prompt to send to the AI.

For longer agent replies, AskProof can produce a Reply Confirmation Prompt. This prompt preserves
the current goal, current status, proof requirements, constraints, and required final output so the
next AI message stays focused.

Reply Confirmation Prompt is the workflow that produces the next copy-ready structured prompt.

AskProof does not automatically listen to every agent reply. It works when the user invokes
AskProof after a reply, or pastes the reply into the chat and asks what to send next.

## 5. Optional Local Memory

AskProof can help generate local handoff and progress memory under:

```text
docs/askproof-memory/
```

It should not write memory silently. Generate the content first, then ask the user to confirm.
