# Role Prompt Rescue Templates

Use these templates when the user’s role is clear or implied.

Do not force the user to provide technical evidence first. Start with the role’s natural language
and ask for the minimum useful proof.

## Product Manager

Weak feedback:

```text
这个流程还是不对，继续优化。
```

Why it is weak:

- “不对” does not define the expected user journey.
- “优化” may cause scope drift before the current flow is verified.
- The AI may redesign instead of fixing the specific acceptance gap.

Rescued prompt:

```text
请先不要继续扩展功能。请按产品验收角度复述：目标用户是谁、原本期望的流程是什么、现在实际发生了什么、上一轮修改了哪些内容、哪些验收标准已经满足、哪些还未验证。然后给出一个最小修改方案和对应验收方式。
```

## Designer

Weak feedback:

```text
这个页面不好看，重做。
```

Why it is weak:

- “不好看” does not identify the visual problem.
- “重做” may discard working behavior.
- The AI may change layout, color, spacing, and copy all at once, making review harder.

Rescued prompt:

```text
请不要整页重做。请先从视觉验收角度列出当前页面的问题：层级、间距、对齐、颜色、字体、移动端适配分别是否存在明显问题。每次只改最影响观感的 1-2 个点，并说明修改后我应该截图检查哪里。
```

## Operations

Weak feedback:

```text
这个自动化还是不稳定，你自己继续修。
```

Why it is weak:

- “不稳定” does not show which step failed.
- Operations workflows often depend on timing, inputs, permissions, and edge cases.
- Without minimum evidence, the AI may change unrelated automation logic.

Rescued prompt:

```text
请先不要大范围改自动化流程。请按运营执行链路复述：触发条件是什么、输入数据是什么、哪一步失败、成功时应该出现什么结果、上一轮修改了哪里、现在需要我提供的最小证据是什么。请先定位失败环节，再提出最小修复。
```

## Content Creator

Weak feedback:

```text
生成结果还是不对，继续改。
```

Why it is weak:

- The AI does not know whether the issue is tone, format, facts, length, or structure.
- It may rewrite everything instead of fixing the acceptance mismatch.

Rescued prompt:

```text
请不要直接重写全部内容。请先判断问题属于哪一类：语气、结构、事实、长度、格式或目标受众不匹配。请列出上一轮输出中已经符合要求的部分和不符合要求的部分，再给出最小修改方案。
```

