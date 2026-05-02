# Acceptance Checklists

Use these checklists when a non-engineer asks “can I trust this?” or “what should I check before continuing?”

Keep the checklist short. The user should be able to copy one prompt or perform one simple acceptance action.

## Done Claim Checklist

Before trusting “done”, ask whether the AI provided:

- changed files or changed behavior
- original problem restatement
- verification method
- verification result
- skipped checks
- remaining risk
- next safe step

If any of these are missing, mark the result as partly or fully unverified.

## Minimum Proof Checklist

Good enough proof usually includes at least one of:

- screenshot or screen recording of the fixed user flow
- exact command and passing result
- before/after behavior comparison
- manual acceptance steps and observed result
- deployment link or version plus verified path

Weak proof includes:

- “should work now”
- “I fixed it”
- “the code looks correct”
- “no obvious issue”
- “I updated the logic”

## Non-Engineer Acceptance Prompt

```text
请不要只说“已完成”。请用非工程师能理解的方式列出：
1. 你改了什么；
2. 原问题是什么；
3. 你如何验证；
4. 验证结果是什么；
5. 哪些没有验证；
6. 我现在是否可以继续下一步。
```

## Stop-Or-Continue Decision

Continue only if:

- the original goal is restated correctly
- the AI separates changed from verified
- at least one relevant proof is shown
- remaining risks are named

Stop and ask for proof if:

- the AI only says “done”
- tests were skipped without a replacement check
- the result changed scope
- the user cannot describe what was fixed

