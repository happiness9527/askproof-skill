# Changelog

All notable changes to AskProof will be documented in this file.

## [0.2.1] - 2026-05-03

### Added

- Strengthened Reply Confirmation Prompt as a core AskProof workflow after v0.2.0.
- Clarified that AskProof does not automatically monitor agent replies.
- Added stronger copy-ready next-prompt structure for Codex / Claude Code style workflows.
- Added and linked a Reply Confirmation Prompt example.

## [0.2.0] - 2026-05-02

### Added

- Added the AskProof Acceptance Brief for structured AI acceptance results.
- Added Evidence Type classification for code, log, visual, user acceptance, and reproducible evidence.
- Added Same-Agent Verification Mode for cases where the current agent can inspect project evidence.
- Added Minimum Acceptance Path guidance for practical non-engineer verification.
- Added a fictional Same-Agent Verification example.

### Changed

- Updated Skill instructions and output templates for structured acceptance workflows.
- Updated README files with v0.2 capability summaries.
- Strengthened follow-up prompt rules so “code changed” is not treated as “feature verified”.

## [0.1.4] - 2026-05-02

### Changed

- Improved English and Chinese README onboarding for non-engineers.
- Added clearer README navigation and early demo-oriented guidance.
- Clarified README trial and installation paths without changing the project positioning.

## [0.1.3] - 2026-05-02

### Fixed

- Confirmed remote `main` and `v0.1.2` tag point to the multi-line Markdown commit.
- Added visible language switching between English and Chinese README files.

## [0.1.2] - 2026-05-02

### Fixed

- Rewrote README, docs, references, examples, and Skill files as true multi-line Markdown.
- Fixed `askproof/SKILL.md` YAML frontmatter so Skill metadata is parseable.
- Improved `doctor.py` to detect compressed Markdown lines and invalid Skill frontmatter.
- Added stricter checks for long lines, malformed headings, and non-standard Skill metadata.

## [0.1.1] - 2026-05-02

### Added

- Skill UI metadata in `askproof/agents/openai.yaml`.
- AI acceptance checklist and copy-ready prompt library for non-engineers.
- Drift Guard example for scope expansion before verification.
- Non-engineer ZIP installation guide in `docs/install-for-non-engineers.md`.
- Platform-specific Done Check examples for Cursor, Claude Code, Codex, and domestic agent platforms.
- Role-specific Prompt Rescue templates for product managers, designers, operations, and content creators.
- Example gallery documentation linking the new fictional scenarios.

### Fixed

- Standardized and guarded multi-line Markdown formatting for key README, Skill, reference, example, and docs files.
- Confirmed `askproof/SKILL.md` uses standard multi-line YAML frontmatter.
- Added `doctor.py` checks for broken README/gallery links and missing Skill reference files.

## [0.1.0] - 2026-05-02

### Added

- Initial AskProof Skill for AI acceptance and follow-up prompts.
- English and Chinese README files.
- Six core workflows: Done Check, Prompt Rescue, Evidence Ladder, Explain, Drift Guard, and Handoff Memory.
- Reference rules, output templates, and fictional examples.
- Lightweight local memory helper scripts.
- GitHub issue templates, pull request template, contribution guide, security policy, and publish guide.
