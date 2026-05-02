#!/usr/bin/env python3
"""Update docs/askproof-memory/index.json."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


MEMORY_ROOT = Path("docs/askproof-memory")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root. Default: current directory.")
    args = parser.parse_args()

    repo_root = Path(args.root).resolve()
    memory_root = repo_root / MEMORY_ROOT
    memory_root.mkdir(parents=True, exist_ok=True)

    entries: list[dict[str, str]] = []
    for folder in ["sessions", "handoff", "risks"]:
        directory = memory_root / folder
        directory.mkdir(parents=True, exist_ok=True)
        for path in sorted(directory.glob("*.md")):
            entries.append(
                {
                    "type": folder,
                    "path": path.relative_to(repo_root).as_posix(),
                    "updated": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
                }
            )

    status_path = memory_root / "current-status.md"
    if status_path.exists():
        entries.append(
            {
                "type": "status",
                "path": status_path.relative_to(repo_root).as_posix(),
                "updated": datetime.fromtimestamp(status_path.stat().st_mtime, timezone.utc).isoformat(),
            }
        )

    index = {
        "version": 1,
        "updated": datetime.now(timezone.utc).isoformat(),
        "entries": entries,
    }
    target = memory_root / "index.json"
    target.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(target.relative_to(repo_root).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

