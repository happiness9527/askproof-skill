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
    "CHANGELOG.md",
    "askproof/SKILL.md",
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
    paths.extend(sorted((root / "docs").glob("*.md")))
    paths.extend(sorted((root / "askproof" / "references").glob("*.md")))
    paths.extend(sorted((root / "askproof" / "examples").glob("*.md")))
    return sorted(set(paths))


def check_markdown_format(root: Path) -> tuple[list[str], list[str]]:
    problems: list[str] = []
    warnings: list[str] = []
    for path in markdown_paths_to_check(root):
        if not path.exists():
            continue
        relative = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        if len(lines) <= 1:
            problems.append(f"{relative}:1 Markdown file appears compressed into one line")
        if len(lines) < 10 and len(text) > 1000:
            problems.append(f"{relative}:1 Markdown file has only {len(lines)} lines but {len(text)} characters")

        in_code_block = False
        for line_number, line in enumerate(lines, start=1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue

            line_length = len(line)
            if line_length > 1000:
                problems.append(f"{relative}:{line_number} line is {line_length} characters; compressed Markdown must be split")
            elif line_length > 500:
                warnings.append(f"{relative}:{line_number} line is {line_length} characters; consider splitting it")

            if in_code_block:
                continue

            if stripped.startswith("#"):
                if not re.match(r"^#{1,6}(\s+\S.*)?$", stripped):
                    problems.append(f"{relative}:{line_number} malformed Markdown heading")
                if re.search(r"\s#{1,6}\s+\S", stripped):
                    problems.append(f"{relative}:{line_number} appears to contain multiple headings on one line")
                if re.search(r"\s(```|>\s+)", stripped):
                    problems.append(f"{relative}:{line_number} heading appears to include body/list content on the same line")
                if "**" in stripped and len(stripped) > 40:
                    problems.append(f"{relative}:{line_number} heading appears to include emphasized body text on the same line")

            if re.match(r"^\s*[-*]\s+", line) and re.search(r"\s[-*]\s+\S", line.strip()[2:]):
                problems.append(f"{relative}:{line_number} list items appear compressed onto one line")
            if re.match(r"^\s*\d+\.\s+", line) and re.search(r"\s\d+\.\s+\S", line.strip()[3:]):
                problems.append(f"{relative}:{line_number} ordered list items appear compressed onto one line")

    return problems, warnings


def check_skill_frontmatter(root: Path) -> list[str]:
    path = root / "askproof" / "SKILL.md"
    if not path.exists():
        return ["Missing askproof/SKILL.md"]
    lines = path.read_text(encoding="utf-8").splitlines()
    problems: list[str] = []
    if not lines:
        return ["askproof/SKILL.md:1 file is empty"]
    if lines[0] != "---":
        problems.append("askproof/SKILL.md:1 first line must be exactly ---")
    if len(lines) < len(SKILL_FRONTMATTER):
        problems.append("askproof/SKILL.md:1 frontmatter is incomplete")
        return problems

    for index, expected in enumerate(SKILL_FRONTMATTER, start=1):
        actual = lines[index - 1] if index - 1 < len(lines) else ""
        if actual != expected:
            problems.append(f"askproof/SKILL.md:{index} expected {expected!r}, got {actual!r}")

    closing_line = len(SKILL_FRONTMATTER)
    if lines[closing_line - 1] != "---":
        problems.append(f"askproof/SKILL.md:{closing_line} frontmatter closing line must be exactly ---")
    if len(lines) <= closing_line or lines[closing_line].strip() != "":
        problems.append(f"askproof/SKILL.md:{closing_line + 1} must be blank between frontmatter and # AskProof")
    if len(lines) <= closing_line + 1 or lines[closing_line + 1].strip() != "# AskProof":
        problems.append(f"askproof/SKILL.md:{closing_line + 2} body must start with # AskProof")
    return problems


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
    warnings: list[str] = []
    problems.extend(check_required(root))
    problems.extend(check_gitignore(root))
    problems.extend(check_forbidden_files(root))
    problems.extend(check_secret_markers(root))
    markdown_problems, markdown_warnings = check_markdown_format(root)
    problems.extend(markdown_problems)
    warnings.extend(markdown_warnings)
    problems.extend(check_skill_frontmatter(root))
    problems.extend(check_markdown_links(root))
    problems.extend(check_skill_references(root))

    if warnings:
        print("AskProof doctor warnings:\n")
        for warning in warnings:
            print(f"- {warning}")
        print()

    if problems:
        print("AskProof doctor found problems:\n")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("AskProof doctor passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
