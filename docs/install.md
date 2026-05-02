# Installation

AskProof V0.1 is a local Skill project. It does not require a server, API key, database, or external integration.

If you do not use GitHub or do not know where your AI tool stores Skills, use [Install AskProof For Non-Engineers](install-for-non-engineers.md).

## Install For A Codex-Style Skill Environment

1. Download or clone this repository.
2. Copy the `askproof/` directory into your local skills directory.
3. Restart or reload your AI agent environment.
4. Try a natural-language request:

```text
AI says it is fixed. Is it really done?
```

or:

```text
AI 说修好了，真的完成了吗？
```

## Optional Local Checks

Run these from the repository root:

```bash
python3 askproof/scripts/doctor.py
python3 -m py_compile askproof/scripts/*.py
```

## No Required Integrations

AskProof V0.1 does not include:

- Slack integration
- Notion integration
- Feishu/Lark integration
- frontend UI
- background daemon
- CI bot
- automatic test executor
- automatic GitHub release publishing
