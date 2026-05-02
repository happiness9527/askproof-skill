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

