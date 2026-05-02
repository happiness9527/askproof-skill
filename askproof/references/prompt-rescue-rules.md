# Prompt Rescue Rules

Prompt Rescue rewrites vague user feedback into actionable prompts.

## Low-Quality Feedback Patterns

- “还是不行”
- “继续”
- “你自己解决”
- “不要出现 bug”
- “重新改”
- “怎么又报错了”
- “still broken”
- “just fix it”
- “continue”
- “fix it yourself”

## Why These Are Inefficient

They do not tell the AI:

- what failed
- what the user saw
- what changed since last time
- whether the previous fix was tested
- what evidence is available
- what should not be changed

This can cause blind edits, broad refactors, repeated mistakes, and longer conversations.

## Rewrite Requirements

A rescued prompt should ask the AI to:

1. Stop broad changes temporarily.
2. Restate the current failure.
3. List the last changed files or actions.
4. Identify likely failure points.
5. Ask for the minimum evidence needed.
6. Avoid unrelated refactors.
7. Define how the next fix will be verified.

## Self-Contained Follow-Up Prompt Rule

The final “你现在最应该问 AI 的一句话” must be self-contained.

It must include:

1. The specific project or feature name.
2. The target that needs verification.
3. The evidence types required, such as code evidence, logs, screenshots, recordings, user
   acceptance, or reproducible steps.
4. A clear instruction that “code was changed” is not enough.
5. A clear stop condition: do not expand features before verification.

If the user did not provide a feature name, use `[具体功能名]` and tell the user to replace it before
sending the prompt.

Weak:

```text
请说明你怎么验证的。
```

Better:

```text
请针对 [具体功能名] 先不要继续扩展功能。请说明要验证的目标、已有哪类证据、缺少哪类证据、实际运行或用户验收结果是什么。不要只说代码已修改；如果还没有验证，请标注“未验证”。
```

## Default Rewrite

```text
请不要继续盲目改代码。请先按以下步骤排查：
1. 复述当前失败现象；
2. 说明你上一轮修改了哪些文件；
3. 判断问题可能发生在哪个环节；
4. 告诉我需要提供的最小证据；
5. 在没有新证据前，不要大范围重构；
6. 给出下一次修改后的验证方式；
7. 请把下一句回复写成针对 [具体功能名] 的自包含验收 Prompt。
```

## English Default Rewrite

```text
Please stop making broad changes for now. First restate the current failure, list what you changed in the previous attempt, identify the most likely failure point, tell me the smallest evidence you need from me, avoid unrelated refactors, and explain how you will verify the next fix.
```
