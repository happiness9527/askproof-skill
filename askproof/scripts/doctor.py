#!/usr/bin/env python3
"""Check that the AskProof project is ready for a public GitHub release."""

from __future__ import annotations

import argparse
import fnmatch
import sys
from pathlib import Path


REQUIRED_PATHS = [
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    ".gitignore",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/ISSUE_TEMPLATE/use_case.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "askproof/SKILL.md",
    "askproof/agents/openai.yaml",
    "askproof/references/intent-router.md",
    "askproof/references/output-templates.md",
    "askproof/references/acceptance-checklists.md",
    "askproof/references/done-check-rules.md",
    "askproof/references/platform-done-check-patterns.md",
    "askproof/references/prompt-rescue-rules.md",
    "askproof/references/role-prompt-rescue-templates.md",
    "askproof/references/evidence-ladder.md",
    "askproof/references/drift-guard-rules.md",
    "askproof/references/handoff-memory-rules.md",
    "askproof/references/project-profile-template.md",
    "askproof/examples/done-check-example.md",
    "askproof/examples/cursor-done-check-example.md",
    "askproof/examples/claude-code-done-check-example.md",
    "askproof/examples/codex-done-check-example.md",
    "askproof/examples/domestic-agent-done-check-example.md",
    "askproof/examples/prompt-rescue-example.md",
    "askproof/examples/role-prompt-rescue-examples.md",
    "askproof/examples/evidence-ladder-example.md",
    "askproof/examples/ai-report-explain-example.md",
    "askproof/examples/drift-guard-example.md",
    "askproof/examples/handoff-example.md",
    "askproof/scripts/collect_context.py",
    "askproof/scripts/write_memory.py",
    "askproof/scripts/update_index.py",
    "askproof/scripts/doctor.py",
    "docs/install.md",
    "docs/quick-start-for-non-engineers.md",
    "docs/acceptance-checklist.md",
    "docs/prompt-library.md",
    "docs/example-gallery.md",
    "docs/use-cases.md",
    "docs/how-it-works.md",
    "docs/roadmap.md",
    "docs/github-publish-guide.md",
    "demo/before.md",
    "demo/after.md",
    "demo/sample-handoff.md",
]

REQUIRED_GITIGNORE_LINES = [
    ".env",
    "*.local",
    "project-profile.local.md",
    "docs/askproof-memory/private/",
    "node_modules/",
    "__pycache__/",
]

FORBIDDEN_FILES = [
    ".env",
    ".env.*",
    "*.pem",
    "*.key",
    "project-profile.local.md",
]

SECRET_MARKERS = [
    "BEGIN" + " PRIVATE KEY",
    "AWS" + "_SECRET_ACCESS_KEY=",
    "GITHUB" + "_TOKEN=",
    "OPENAI" + "_API_KEY=",
    "ANTHROPIC" + "_API_KEY=",
]


def iter_files(root: Path):
    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            yield path


def check_required(root: Path) -> list[str]:
    return [f"Missing required path: {path}" for path in REQUIRED_PATHS if not (root / path).exists()]


def check_gitignore(root: Path) -> list[str]:
    path = root / ".gitignore"
    if not path.exists():
        return ["Missing .gitignore"]
    lines = {line.strip() for line in path.read_text(encoding="utf-8").splitlines()}
    return [f".gitignore is missing: {line}" for line in REQUIRED_GITIGNORE_LINES if line not in lines]


def check_forbidden_files(root: Path) -> list[str]:
    problems: list[str] = []
    for path in iter_files(root):
        relative = path.relative_to(root).as_posix()
        if relative.startswith("docs/askproof-memory/private/"):
            problems.append(f"Private memory file should not be committed: {relative}")
            continue
        name = path.name
        for pattern in FORBIDDEN_FILES:
            if fnmatch.fnmatch(name, pattern):
                problems.append(f"Forbidden local/private file: {relative}")
    return problems


def check_secret_markers(root: Path) -> list[str]:
    problems: list[str] = []
    for path in iter_files(root):
        if path.suffix.lower() not in {".md", ".py", ".txt", ".json", ".yml", ".yaml", ""}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for marker in SECRET_MARKERS:
            if marker in text:
                problems.append(f"Possible secret marker in {path.relative_to(root).as_posix()}: {marker}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root. Default: current directory.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        parser.error(f"Root does not exist: {root}")

    problems: list[str] = []
    problems.extend(check_required(root))
    problems.extend(check_gitignore(root))
    problems.extend(check_forbidden_files(root))
    problems.extend(check_secret_markers(root))

    if problems:
        print("AskProof doctor found problems:\n")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("AskProof doctor passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
