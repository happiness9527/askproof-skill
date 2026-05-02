# Platform Done Check Patterns

These patterns help AskProof respond to “AI says fixed” claims from common AI agent tools.

Use fictional project names and sanitized details. Do not assume that any platform’s summary equals verification.

## Cursor

Cursor users often see code-focused summaries such as:

```text
Fixed the issue in CheckoutButton.tsx. It should work now.
```

AskProof should check:

- Did Cursor list changed files?
- Did it run or ask the user to run the app?
- Did it verify the original click, page, or workflow?
- Did it mention browser console errors or screenshots?
- Did it separate code edit from user-facing verification?

Good follow-up:

```text
Please do not continue editing yet. Show the files you changed, the exact user flow you verified in the app preview, the observed result, and anything still unverified. If you did not open the preview or reproduce the original issue, mark it as unverified.
```

## Claude Code

Claude Code summaries may include file edits, shell commands, tests, and “not run” notes.

AskProof should check:

- Did it say which commands were run?
- Did the command output pass?
- Did it skip tests because dependencies, time, or environment were missing?
- Did it explain whether the original bug was reproduced?
- Did it leave a clear next verification step?

Good follow-up:

```text
Please separate this into “changed”, “verified”, “not run”, and “risk”. For every skipped check, explain why it was skipped and what minimum command or manual step I should ask the next AI to run.
```

## Codex

Codex-style reports often include terminal checks and file summaries.

AskProof should check:

- Did it run a relevant local check?
- Was the check only syntax-level, or did it verify the user-facing problem?
- Did it mention limitations of the environment?
- Did it avoid claiming product behavior that was not actually tested?

Good follow-up:

```text
Please clarify whether your verification proves the original user-facing problem is fixed, or only proves that the edited files compile. List the remaining manual acceptance checks before we continue.
```

## Domestic Agent Platforms

Some domestic AI platforms may summarize in product-friendly language:

```text
已修复并重新部署，现在应该可以正常使用。
```

AskProof should check:

- Is there a deployment link or version?
- Is there a screenshot or screen recording?
- Did the AI test the exact user scenario?
- Did it provide logs, error comparison, or before/after behavior?
- Did it say what is still unverified?

Good follow-up:

```text
请先不要继续扩展。请提供这次修复对应的部署地址或版本、你验证过的用户路径、验证结果截图或文字记录，以及仍未验证的内容。如果只是完成了发布但没有验收，请标注“已发布但未验证”。
```

