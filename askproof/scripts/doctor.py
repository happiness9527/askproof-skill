#!/usr/bin/env python3
"""Check that the AskProof project is ready for a public GitHub release."""

from __future__ import annotations

import argparse
import fnmatch
import re
import sys
from pathlib import Path
from urllib.parse import unquote


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
    "docs/install-for-non-engineers.md",
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

SKILL_FRONTMATTER = [
    "---",
    "name: askproof",
    "description: Use this skill when a non-engineer needs to ask AI agents for proof, check whether “done” is actually verified, rewrite vague feedback such as “still broken” into actionable prompts, request minimum evidence, prevent task drift, or create handoff memory.",
    "metadata:",
    "  short-description: Help non-engineers ask AI agents for proof before trusting “done”.",
    "---",
]

MARKDOWN_FORMAT_PATHS = [
    "README.md",
    "README.zh-CN.md",
    "askproof/SKILL.md",
    "docs/install.md",
    "docs/roadmap.md",
    "docs/example-gallery.md",
]

LINK_CHECK_PATHS = [
    "README.md",
    "README.zh-CN.md",
    "docs/example-gallery.md",
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


def markdown_paths_to_check(root: Path) -> list[Path]:
    paths = [root / relative for relative in MARKDOWN_FORMAT_PATHS]
    paths.extend(sorted((root / "askproof" / "references").glob("*.md")))
    paths.extend(sorted((root / "askproof" / "examples").glob("*.md")))
    return paths


def check_markdown_multiline(root: Path) -> list[str]:
    problems: list[str] = []
    for path in markdown_paths_to_check(root):
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        if len(lines) <= 1:
            problems.append(f"Markdown file appears compressed into one line: {path.relative_to(root).as_posix()}")
    return problems


def check_skill_frontmatter(root: Path) -> list[str]:
    path = root / "askproof" / "SKILL.md"
    if not path.exists():
        return ["Missing askproof/SKILL.md"]
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines[: len(SKILL_FRONTMATTER)] != SKILL_FRONTMATTER:
        return ["askproof/SKILL.md frontmatter does not match the required standard YAML block"]
    if len(lines) <= len(SKILL_FRONTMATTER) or lines[len(SKILL_FRONTMATTER)].strip() != "":
        return ["askproof/SKILL.md must have a blank line between frontmatter and # AskProof"]
    if len(lines) <= len(SKILL_FRONTMATTER) + 1 or lines[len(SKILL_FRONTMATTER) + 1].strip() != "# AskProof":
        return ["askproof/SKILL.md body must start with # AskProof after frontmatter"]
    return []


def check_markdown_links(root: Path) -> list[str]:
    problems: list[str] = []
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for relative in LINK_CHECK_PATHS:
        path = root / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            target = unquote(target)
            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(root)
            except ValueError:
                problems.append(f"Markdown link escapes repository in {relative}: {match.group(1)}")
                continue
            if not target_path.exists():
                problems.append(f"Broken Markdown link in {relative}: {match.group(1)}")
    return problems


def check_skill_references(root: Path) -> list[str]:
    problems: list[str] = []
    path = root / "askproof" / "SKILL.md"
    if not path.exists():
        return ["Missing askproof/SKILL.md"]
    text = path.read_text(encoding="utf-8")
    for reference in sorted(set(re.findall(r"`(references/[^`]+\.md)`", text))):
        target = root / "askproof" / reference
        if not target.exists():
            problems.append(f"SKILL.md references missing file: {reference}")
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
    problems.extend(check_markdown_multiline(root))
    problems.extend(check_skill_frontmatter(root))
    problems.extend(check_markdown_links(root))
    problems.extend(check_skill_references(root))

    if problems:
        print("AskProof doctor found problems:\n")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("AskProof doctor passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
