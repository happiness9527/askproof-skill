#!/usr/bin/env python3
"""Write AskProof local memory after the user has confirmed the content."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


MEMORY_ROOT = Path("docs/askproof-memory")


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = value.strip("-")
    return value[:60] or "memory"


def read_content(args: argparse.Namespace) -> str:
    if args.content:
        return args.content.strip()
    if args.content_file:
        return Path(args.content_file).read_text(encoding="utf-8").strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return ""


def ensure_dirs(root: Path) -> None:
    for relative in ["sessions", "handoff", "risks", "private"]:
        (root / relative).mkdir(parents=True, exist_ok=True)


def write_index(memory_root: Path) -> None:
    entries: list[dict[str, str]] = []
    for folder in ["sessions", "handoff", "risks"]:
        for path in sorted((memory_root / folder).glob("*.md")):
            entries.append(
                {
                    "type": folder,
                    "path": path.as_posix(),
                    "updated": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
                }
            )
    index = {
        "version": 1,
        "updated": datetime.now(timezone.utc).isoformat(),
        "entries": entries,
    }
    (memory_root / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument("--kind", choices=["status", "session", "handoff", "risk"], required=True)
    parser.add_argument("--title", default="", help="Optional title used for generated filenames.")
    parser.add_argument("--content", default="", help="Memory content. If omitted, stdin is used.")
    parser.add_argument("--content-file", default="", help="Read memory content from a UTF-8 text file.")
    args = parser.parse_args()

    repo_root = Path(args.root).resolve()
    memory_root = repo_root / MEMORY_ROOT
    ensure_dirs(memory_root)

    content = read_content(args)
    if not content:
        parser.error("No content provided. Use --content, --content-file, or stdin.")

    title = args.title or args.kind
    stamp = utc_stamp()
    slug = slugify(title)

    if args.kind == "status":
        target = memory_root / "current-status.md"
    elif args.kind == "handoff":
        target = memory_root / "handoff" / "latest-handoff.md"
        archive = memory_root / "handoff" / f"{stamp}-{slug}.md"
        archive.write_text(content + "\n", encoding="utf-8")
    elif args.kind == "risk":
        target = memory_root / "risks" / f"{stamp}-{slug}.md"
    else:
        target = memory_root / "sessions" / f"{stamp}-{slug}.md"

    target.write_text(content + "\n", encoding="utf-8")
    write_index(memory_root)
    print(target.relative_to(repo_root).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

