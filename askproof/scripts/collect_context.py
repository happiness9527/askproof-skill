#!/usr/bin/env python3
"""Collect lightweight AskProof context for handoff or acceptance review."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


CONTEXT_FILES = [
    "README.md",
    "README.zh-CN.md",
    "docs/askproof-memory/current-status.md",
    "docs/askproof-memory/handoff/latest-handoff.md",
]


def read_text(path: Path, max_chars: int) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None
    if len(text) > max_chars:
        return text[:max_chars] + "\n\n[truncated]\n"
    return text


def run_git(root: Path, args: list[str]) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    output = (result.stdout + result.stderr).strip()
    return output or None


def print_section(title: str, body: str) -> None:
    print(f"\n## {title}\n")
    print(body.rstrip())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument("--max-chars", type=int, default=6000, help="Max characters per text file.")
    parser.add_argument("--no-git", action="store_true", help="Skip git status and diff stat.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        parser.error(f"Root does not exist: {root}")

    print(f"# AskProof Context\n\nRoot: {root}")

    for relative in CONTEXT_FILES:
        text = read_text(root / relative, args.max_chars)
        if text:
            print_section(relative, text)

    if not args.no_git:
        status = run_git(root, ["status", "--short"])
        if status:
            print_section("git status --short", status)

        diff_stat = run_git(root, ["diff", "--stat"])
        if diff_stat:
            print_section("git diff --stat", diff_stat)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

