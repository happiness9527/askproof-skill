# AI Acceptance Checklist

Use this checklist before trusting an AI agent’s “done”, “fixed”, or “should work now”.

## The 60-Second Check

Ask yourself:

1. Did the AI say what it changed?
2. Did the AI restate the original problem?
3. Did the AI show how it verified the result?
4. Did the AI show the verification result?
5. Did the AI say what was not verified?
6. Did the AI tell me whether it is safe to continue?

If the answer is “no” or “not sure” for 3, 4, or 5, treat the result as unverified.

## What Counts As Evidence

Useful evidence:

- screenshot or recording of the fixed flow
- exact command and passing output
- before/after comparison
- manual check steps and observed result
- deployment address or version plus verified path
- test result tied to the original problem

Weak evidence:

- “fixed”
- “should work now”
- “I updated the code”
- “I think this resolves it”
- “no obvious issues”

## Copy This Prompt

```text
请不要只说“已完成”。请用非工程师能理解的方式列出：你改了什么、原问题是什么、你如何验证、验证结果是什么、哪些没有验证，以及我现在是否可以继续下一步。
```

## If You Cannot Provide Logs

You do not need logs first. Send one of these:

1. a screenshot
2. the AI’s last “done/fixed” message
3. the last red error line
4. a plain-language description of what happened

## Stop Or Continue

Safe to continue:

- The AI showed relevant proof.
- The original problem was checked.
- Remaining risks are named.

Do not continue yet:

- The AI only claimed it was done.
- Tests were skipped with no replacement check.
- The task expanded before the current result was verified.

