# Contributing

Thank you for considering a contribution to AskProof.

AskProof is intentionally small. The goal is not to become a complex AI coding platform. The goal is to help non-engineers ask better acceptance questions when AI agents claim work is done.

## Good Contributions

- Clearer examples for non-engineers.
- Better prompt rescue rewrites.
- More realistic fictional demos.
- Safer handoff templates.
- Simpler wording.
- Translations that preserve the product positioning.

## Before You Open A Pull Request

1. Keep the change small and reviewable.
2. Use fictional projects and fictional data only.
3. Do not add integrations, network calls, telemetry, or background services.
4. Do not commit secrets, `.env` files, private logs, customer data, or real project paths.
5. Run:

```bash
python3 askproof/scripts/doctor.py
python3 -m py_compile askproof/scripts/*.py
```

## Writing Style

- Prefer plain language over technical jargon.
- If a technical term is necessary, explain what it means for the user.
- Separate “changed” from “verified”.
- Never imply work is verified without evidence.

## Version Scope

V0.1 focuses on README, Skill instructions, references, examples, and demo quality. Please do not add product integrations or heavy automation unless the roadmap changes.

