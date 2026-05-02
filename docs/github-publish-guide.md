# GitHub Publish Guide For Product Managers

This guide explains how to publish AskProof V0.1 to GitHub without assuming you are an engineer.

## 1. Create A GitHub Repository

1. Go to GitHub.
2. Click **New repository**.
3. Repository name:

```text
askproof-skill
```

4. Description:

```text
AskProof helps non-engineers ask AI agents for proof before trusting “done”.
```

5. Choose **Public**.
6. Do not add another README, license, or `.gitignore` if this project already contains them.
7. Click **Create repository**.

## 2. Suggested Topics

Add these repository topics:

```text
ai-agent
ai-tools
vibe-coding
non-engineers
prompt-engineering
ai-workflow
claude-code
codex
agent-skills
handoff
verification
prompt-rescue
```

## 3. Upload Code

If you use GitHub’s web interface:

1. Open the empty repository.
2. Click **uploading an existing file**.
3. Drag the project files into the page.
4. Commit the upload.

If you use Git locally:

```bash
git init
git add .
git commit -m "Initial AskProof v0.1.0 release"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/askproof-skill.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username or organization.

## 4. Check The Repository Page

Make sure GitHub shows:

- `README.md`
- `README.zh-CN.md`
- `LICENSE`
- `askproof/SKILL.md`
- `docs/`
- `demo/`

Open the README and confirm the first screen explains the user pain, not installation commands.

## 5. Create Release Notes

Go to **Releases** and click **Draft a new release**.

Tag:

```text
v0.1.0
```

Release title:

```text
AskProof v0.1.0
```

Release notes:

```markdown
AskProof v0.1.0 is the first open-source release of AI验收官.

It helps non-engineers:

- check whether AI “done” claims include evidence;
- rewrite vague feedback such as “still broken” into actionable prompts;
- ask for minimum useful evidence without knowing logs;
- understand AI technical summaries in plain language;
- prevent scope drift before verification;
- create handoff memory for the next chat, model, platform, or agent.

This release intentionally does not include integrations, a frontend UI, background services, automatic test execution, or PR review automation.
```

Click **Publish release**.

## 6. After Publishing

Share the repository with this positioning:

```text
AskProof is not another AI coding tool. It is an AI acceptance Skill for non-engineers.
```

Recommended short link text:

```text
Don’t just ask AI to continue. Ask for proof.
```

