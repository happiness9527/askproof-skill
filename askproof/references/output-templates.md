# Output Templates

Use these templates as flexible structures. Keep wording plain and specific.

## Universal Template

```text
当前判断：<mode>

用户真正的问题：
<plain-language restatement>

AI 当前说法是否可信：
<low / medium / high, with short reason>

已确认的信息：
- <confirmed item>

未确认的信息：
- <unconfirmed item>

风险点：
- <risk>

下一步最稳妥动作：
<action>

可直接复制给 AI 的 Prompt：
<prompt>

你现在最应该问 AI 的一句话：
<one sentence>
```

## Done Check Template

```text
当前判断：Done Check｜完成验收
完成可信度：低 / 中 / 高
当前状态：已修改 / 已验证 / 未验证 / 有风险 / 可继续 / 不建议继续

AI 提供的证据：
- <evidence or “暂无明确证据”>

缺少的证据：
- <missing proof>

用户应该如何验收：
1. <simple check>
2. <simple check>

你现在最应该问 AI 的一句话：
请先不要继续扩展。请说明你改了什么、如何验证、验证结果是什么，以及还有哪些内容没有验证。
```

## Prompt Rescue Template

```text
当前判断：Prompt Rescue｜低质量反馈救援

这句话低效的原因：
- <why vague feedback fails>

你应该补充的信息：
- <minimum evidence>

改写后的 Prompt：
<copy-ready prompt>

你现在最应该问 AI 的一句话：
<copy-ready prompt>
```

## Evidence Ladder Template

```text
当前判断：Evidence Ladder｜证据阶梯

你不用懂日志，先任选下面一种证据发回来：
1. 当前页面截图；
2. AI 最后一段“已完成/已修复”的回复；
3. 页面或终端里最后一行红色错误文字；
4. 你看到的异常现象，用普通话描述也可以；
5. 如果你会操作，再补充终端日志、Git diff 或测试结果。

你现在最应该问 AI 的一句话：
我现在只能提供最低门槛证据。请告诉我你最需要哪一种：截图、最后一段 AI 回复、最后一行红色错误，还是我用普通话描述现象？
```

## Explain Template

```text
当前判断：Explain｜解释 AI 做了什么

AI 在说什么：
<plain-language summary>

它实际做了什么：
<known work>

这对项目意味着什么：
<impact>

已经确认：
- <confirmed>

还没验证：
- <unverified>

你现在最应该问 AI 的一句话：
请用非工程师能理解的语言说明：哪些已经验证，哪些只是修改了但没有验证，以及我应该怎么验收。
```

## Drift Guard Template

```text
当前判断：Drift Guard｜防跑偏

当前不建议继续扩功能。

原因：
- 上一轮修改还没有验证证据。
- 如果继续新增功能，后面很难判断问题来自哪里。

应该先验证：
- <specific current result>

是否建议 handoff：
<yes/no and why>

你现在最应该问 AI 的一句话：
请先停止新增功能，回到原目标，证明上一轮修改已经生效，并列出仍未验证的部分。
```

## Handoff Memory Template

```text
当前判断：Handoff Memory｜交接记忆

当前任务目标：
<goal>

已完成内容：
- <completed>

已验证内容：
- <verified or “暂无验证证据”>

未验证内容：
- <unverified>

当前风险：
- <risk>

关键决策：
- <decision>

不要重复踩坑：
- <pitfall>

下一轮可复制 Prompt：
<prompt>

你现在最应该问 AI 的一句话：
请根据这份交接继续，先验证未验证内容，不要直接扩展新功能。
```

