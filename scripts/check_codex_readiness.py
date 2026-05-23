#!/usr/bin/env python3
"""Check that this repository stays Codex-oriented."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_TERMS = (
    "cl" + "aude",
    "an" + "thropic",
)


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return [ROOT / line for line in result.stdout.splitlines() if line]


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def main() -> int:
    failures: list[str] = []

    for path in tracked_files():
        text = read_text(path)
        if text is None:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            normalized = line.lower()
            for term in FORBIDDEN_TERMS:
                if term in normalized:
                    rel_path = path.relative_to(ROOT)
                    failures.append(f"{rel_path}:{line_number}: contains retired provider keyword")

    if failures:
        print("Codex readiness check failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("Codex readiness check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
