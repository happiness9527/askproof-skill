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

## Default Rewrite

```text
请不要继续盲目改代码。请先按以下步骤排查：
1. 复述当前失败现象；
2. 说明你上一轮修改了哪些文件；
3. 判断问题可能发生在哪个环节；
4. 告诉我需要提供的最小证据；
5. 在没有新证据前，不要大范围重构；
6. 给出下一次修改后的验证方式。
```

## English Default Rewrite

```text
Please stop making broad changes for now. First restate the current failure, list what you changed in the previous attempt, identify the most likely failure point, tell me the smallest evidence you need from me, avoid unrelated refactors, and explain how you will verify the next fix.
```

