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

## 5. Optional Local Memory

AskProof can help generate local handoff and progress memory under:

```text
docs/askproof-memory/
```

It should not write memory silently. Generate the content first, then ask the user to confirm.

