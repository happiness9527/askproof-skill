# Evidence Ladder

Evidence Ladder helps non-engineers provide useful information without knowing technical tools.

## Levels

### L0: Only Knows “It Does Not Work”

User can only say:

- “还是不行”
- “不对”
- “没反应”
- “still broken”

Ask for one visible symptom.

### L1: Can Describe What They See

User can say:

- what they clicked
- what they expected
- what happened instead
- whether the screen changed

### L2: Can Share A Screenshot

Screenshots are useful even if the user cannot explain them.

Ask for a screenshot of the current page, modal, error, or blank state.

### L3: Can Paste The AI’s Last Reply

The last AI reply often shows:

- what it claims it changed
- whether it ran verification
- what it skipped

### L4: Can Paste The Last Red Error Line

Do not ask for the whole log first. Ask for the last visible red line.

Explain: “The last red line often tells the AI where the failure stopped.”

### L5: Can Provide Technical Evidence

Only ask for this if the user can provide it:

- terminal logs
- Git diff
- test command output
- build output
- browser console error

## Default User Guidance

```text
你不用懂日志，先任选下面一种证据发回来：
1. 当前页面截图；
2. AI 最后一段“已完成/已修复”的回复；
3. 页面或终端里最后一行红色错误文字；
4. 你看到的异常现象，用普通话描述也可以。
```

## Evidence Type Classification

Use this classification during Done Check and Same-Agent Verification Mode. These levels describe
evidence strength, not user skill level.

### L1 Code Evidence

Shows that implementation exists.

Examples:

- commit
- Git diff
- changed files
- function or component implementation

Meaning for the user: “The code appears to be changed, but this alone does not prove the feature
works.”

### L2 Log Evidence

Shows that something was run.

Examples:

- terminal run log
- test output
- build output
- command result

Meaning for the user: “The AI ran a check, but we still need to confirm whether the check matches
the exact user-facing problem.”

### L3 Visual Evidence

Shows the visible result.

Examples:

- screenshot
- screen recording
- before/after image

Meaning for the user: “There is visual proof, but it may still need user acceptance if the flow is
interactive.”

### L4 User Acceptance Evidence

Shows that the user personally ran the expected flow and confirmed it.

Examples:

- user says they clicked through and it worked
- user confirms the expected result appeared
- user verifies the original problem no longer happens

Meaning for the user: “The result is much more trustworthy because the real user path was checked.”

### L5 Reproducible Evidence

Shows that another person or agent can repeat the verification.

Examples:

- exact reproduction steps
- exact command
- expected result
- actual result
- saved screenshot, recording, or log

Meaning for the user: “This is the strongest evidence because someone else can repeat the check.”

## Done Check Evidence Rule

In Done Check, explicitly state:

- which evidence types already exist
- which evidence types are missing
- whether the available evidence proves implementation only or runtime behavior
- what the minimum next evidence should be
