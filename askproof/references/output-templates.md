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

## AskProof Acceptance Brief

Use this for Done Check, Same-Agent Verification Mode, or any situation where the user needs a
structured acceptance result rather than a loose summary.

```text
AskProof Acceptance Brief

1. 当前问题
<用户真正想确认的问题>

2. AI 的完成声明
<AI 声称完成、修复或应该可用的原话>

3. 已确认事实
- <已经能确认的事实>

4. 已有证据
- <证据内容>（证据类型：L1 / L2 / L3 / L4 / L5）

5. 缺失证据
- <缺少的证据>（建议补充证据类型：L1 / L2 / L3 / L4 / L5）

6. 完成可信度：低 / 中 / 高
<一句话说明原因>

7. 当前状态：已修改 / 部分验证 / 已验证 / 不建议继续
<一句话说明为什么>

8. 最小验收动作
<最小验收路径或下一步检查>

9. 下一句该怎么问 AI
<自包含 Prompt>
```

## Done Check Template

```text
当前判断：Done Check｜完成验收
完成可信度：低 / 中 / 高
当前状态：已修改 / 部分验证 / 已验证 / 不建议继续

AI 提供的证据：
- <evidence or “暂无明确证据”>（证据类型：L1 / L2 / L3 / L4 / L5）

缺少的证据：
- <missing proof>（建议补充证据类型：L1 / L2 / L3 / L4 / L5）

最小验收动作：
1. <打开页面或执行命令>
2. <观察功能点>
3. <保存证据>

你现在最应该问 AI 的一句话：
请先不要继续扩展。请针对 [具体功能名] 说明你改了什么、已有哪类证据、缺少哪类证据、如何最小验证，以及还有哪些内容没有验证。
```

## Same-Agent Verification Template

```text
当前判断：Same-Agent Verification Mode｜同一 Agent 自检模式

当前问题：
<用户要验收的功能或修复>

我能检查的现有证据：
- 实现证据：<commit / diff / 文件实现 / 未发现>
- 运行证据：<日志 / 测试输出 / 截图 / 录屏 / 用户验收 / 未发现>

证据类型判断：
- 已有：<L1 / L2 / L3 / L4 / L5>
- 缺少：<L1 / L2 / L3 / L4 / L5>

当前状态：
已修改 / 部分验证 / 已验证 / 不建议继续

限制：
- <无法运行、无法看视频、缺少依赖等限制；没有限制则写“暂无明显限制”>

最小验收动作：
<使用 Minimum Acceptance Path>

你现在最应该问 AI 的一句话：
<自包含 Prompt>
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

## Reply Confirmation Prompt Template

Use this when the user pastes an AI agent reply and wants the next structured prompt to send back.
Reply Confirmation Prompt is the workflow that produces the next copy-ready structured prompt.
This is not background automation. It runs when the user invokes AskProof after an agent reply or
pastes that reply into the chat.

```text
当前判断：Reply Confirmation Prompt｜回复后确认 Prompt

回复后确认 Prompt

1. 当前目标
<用普通话复述用户真正要推进的目标>

2. 当前状态
<基于 AI 回复说明现在推进到哪里；不确定就写“未确认”>

3. Agent 本轮声称完成 / 修改 / 判断了什么
- <agent claim from the reply>

4. 从 Agent 回复里能确认什么
- <confirmed from the reply>

5. 仍未确认 / 缺少哪些证据
- <unconfirmed item or missing evidence>

6. 做之前必须先注意什么
- <before-continuing check or warning>

7. 本次要求 Agent 怎么做
- <specific requirement>

8. 约束和不要做什么
- 不要编造验证结果。
- 不要把“已修改”当成“已验证”。
- 不要在没有验证前继续扩功能。

9. 验收要求
- <proof, command, screenshot, recording, or acceptance evidence required>

10. 最后必须输出什么
- 已修改
- 已验证
- 未验证
- 风险
- 下一步最稳妥动作

11. 可直接复制给 Agent 的 Prompt
请基于当前上下文继续，但先不要扩展新功能。

当前目标：
<goal>

当前状态：
<status>

本次你需要先确认：
1. <confirmation point>
2. <confirmation point>

本次执行要求：
1. <specific action>
2. <specific action>

约束：
- 不要编造验证结果。
- 不要把“已修改”当成“已验证”。
- 不要做与当前目标无关的重构或扩展。

最后请输出：
1. 你实际做了什么；
2. 你如何验证；
3. 验证结果是什么；
4. 还有哪些未验证或有风险；
5. 下一步建议。

你现在最应该问 AI 的一句话：
<one compact self-contained prompt>
```

## Minimum Acceptance Path

Use this when the user needs a concrete way to accept the result.

```text
Minimum Acceptance Path｜最小验收路径

1. 打开什么页面 / 执行什么命令：
<page or command>

2. 观察哪个功能点：
<specific behavior>

3. 什么现象算通过：
<pass condition>

4. 什么现象算失败：
<fail condition>

5. 需要保存什么证据：
<screenshot / recording / log / test output / user confirmation>

6. 失败后应该把什么发给 AI：
<minimum evidence to send back>
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
