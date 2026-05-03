# Example Gallery

This gallery collects realistic but fictional AskProof scenarios. It is designed for non-engineers
who use AI agents but do not want to learn technical verification language.

## Platform Done Check Examples

### Cursor

Use when Cursor says it changed a file and the app “should work now”.

Read: [Cursor Done Check Example](../askproof/examples/cursor-done-check-example.md)

Acceptance focus:

- Did Cursor verify the user-facing preview?
- Did it reproduce the original issue?
- Did it check the exact workflow?

### Claude Code

Use when Claude Code reports edits, skipped commands, missing dependencies, or partial checks.

Read: [Claude Code Done Check Example](../askproof/examples/claude-code-done-check-example.md)

Acceptance focus:

- What was changed?
- What was verified?
- What was not run?
- What risk remains?

### Codex

Use when Codex provides terminal checks or implementation summaries.

Read: [Codex Done Check Example](../askproof/examples/codex-done-check-example.md)

Acceptance focus:

- Does the command prove the original user-facing issue?
- Or does it only prove syntax, formatting, or a narrow technical condition?

### Same-Agent Verification

Use when Claude Code, Codex, or another current agent can inspect the repository and the user asks
whether the feature is actually verified in the current project.

Read: [Same-Agent Verification Example](../askproof/examples/same-agent-verification-example.md)

Acceptance focus:

- Does the current agent find implementation evidence only?
- Is there runtime, visual, user acceptance, or reproducible evidence?
- What is the minimum acceptance path before expanding scope?

### Domestic Agent Platform

Use when a domestic AI agent platform says “已修复并重新部署”.

Read: [Domestic Agent Platform Done Check
Example](../askproof/examples/domestic-agent-done-check-example.md)

Acceptance focus:

- Is there a deployment address or version?
- Was the original user path verified?
- Is there a screenshot, recording, or before/after result?

## Role Prompt Rescue Examples

Read: [Role Prompt Rescue Examples](../askproof/examples/role-prompt-rescue-examples.md)

### Product Manager

Weak feedback:

```text
这个流程还是不对，继续优化。
```

Better AskProof direction:

```text
请先按产品验收角度说明目标用户、期望流程、实际流程、已满足验收标准和未验证内容。
```

### Designer

Weak feedback:

```text
这个页面不好看，重做。
```

Better AskProof direction:

```text
请不要整页重做。先判断层级、间距、对齐、颜色、字体、移动端适配中最影响观感的 1-2 个点。
```

### Operations

Weak feedback:

```text
这个自动化还是不稳定，你自己继续修。
```

Better AskProof direction:

```text
请先按运营执行链路说明触发条件、输入数据、失败步骤、预期结果和需要我提供的最小证据。
```

## Drift Guard Example

Use when a user wants to add new features before the current fix is verified.

Read: [Drift Guard Example](../askproof/examples/drift-guard-example.md)

Acceptance focus:

- Is the original result verified?
- Will new features depend on unverified behavior?
- Should the next step be proof, handoff, or scope split?

## Reply Confirmation Prompt Example

Use when an AI agent has replied and the user needs the next structured prompt to send back.

Read: [Reply Confirmation Prompt Example](../askproof/examples/reply-confirmation-prompt-example.md)

Acceptance focus:

- Does the prompt preserve the current goal and status?
- Does it prevent blind continuation?
- Does it require evidence before treating the work as verified?
- Does it tell the agent what to output at the end?
