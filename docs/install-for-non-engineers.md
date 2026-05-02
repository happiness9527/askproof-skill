# Install AskProof For Non-Engineers

This guide is for users who do not use Git and do not know where AI tools store Skills.

AskProof is a local Skill folder. You only need to download the project, find the `askproof/`
folder, and copy it into the Skill folder used by your AI tool.

## 1. Download AskProof From GitHub

1. Open the GitHub repository:

```text
https://github.com/happiness9527/askproof-skill
```

2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Unzip the downloaded file.

After unzipping, you should see a folder named something like:

```text
askproof-skill-main
```

## 2. Find The `askproof/` Folder

Open the unzipped folder.

Find this folder:

```text
askproof/
```

That is the Skill folder you need to install.

Do not copy only `SKILL.md`. Copy the whole `askproof/` folder, because it also contains references,
examples, and helper scripts.

## 3. Copy It To Your AI Tool’s Skill Folder

Different AI tools store Skills in different places.

If you already know the Skill folder, copy the entire `askproof/` folder into it.

If you do not know where the Skill folder is, ask your AI tool this:

```text
Where should I put a local Skill folder named askproof so you can use it? Please give me the exact folder path and tell me whether I need to restart or reload the app.
```

Chinese:

```text
我想安装一个名为 askproof 的本地 Skill。请告诉我应该把这个文件夹放到哪里，给我明确的文件夹路径，并说明是否需要重启或刷新应用。
```

## 4. Restart Or Reload Your AI Tool

After copying the folder, restart or reload your AI tool if it requires that.

Some tools need a full restart before they detect new Skills.

## 5. Test Whether AskProof Works

Send this test prompt:

```text
AI says it is fixed. Is it really done?
```

Chinese:

```text
AI 说修好了，真的完成了吗？
```

## 6. What A Successful Result Looks Like

If AskProof is working, the response should include ideas like:

- completion confidence / 完成可信度
- confirmed information / 已确认信息
- missing evidence / 缺少证据
- next prompt / 下一句该怎么问 AI

It should not simply say “yes, it is done”.

AskProof should help you ask for proof before trusting the AI’s claim.

