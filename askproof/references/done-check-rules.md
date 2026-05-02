# Done Check Rules

Done Check is used when an AI agent claims work is finished.

## Principle

An AI completion claim is not proof.

Do not mark work as verified unless the user provides or the AI clearly reports evidence such as:

- exact verification command and result
- manual reproduction steps and observed result
- screenshot or screen recording
- test output
- build output
- before/after behavior comparison
- changed files plus verification steps

## Confidence Levels

### Low

Use when:

- AI only says “done”, “fixed”, or “should work now”.
- No files, commands, screenshots, test results, or manual checks are shown.
- The user cannot describe whether the issue disappeared.

Status: unverified, risky, not recommended to continue.

### Medium

Use when:

- AI lists changed files or explains the fix.
- Some manual reasoning is provided.
- Verification is partial, vague, or not directly tied to the original failure.

Status: changed, partially verified, still has risk.

### High

Use only when:

- The original failure is described.
- The AI explains what changed.
- A relevant verification was run or manually checked.
- The result is shown.
- Remaining unverified areas are listed.

Status: verified enough to continue, with stated limits.

## Required Separation

Always separate:

- **Changed**: files, content, or behavior the AI claims it modified.
- **Verified**: evidence that the original issue is resolved.
- **Unverified**: anything not proven yet.

## Good Follow-Up Prompt

```text
请先不要继续扩展功能。请按“已修改 / 已验证 / 未验证 / 风险”四部分说明：你改了什么、如何验证、验证结果是什么、还有哪些内容没有验证。如果没有验证，请直接标注“未验证”，不要说应该可以。
```

