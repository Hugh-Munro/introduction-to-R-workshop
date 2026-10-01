#!/usr/bin/env python3
"""List playbook rules whose review date has passed."""

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AREAS = ["study", "investing", "exercise"]

SUMMARY = re.compile(r"<summary>(.*?)</summary>")
REVIEW = re.compile(r"\*\*Review:\*\*\s*(\d{4}-\d{2}-\d{2})")


def main() -> int:
    today = date.today()
    overdue = []

    for area in AREAS:
        path = ROOT / area / "playbook.md"
        if not path.exists():
            continue
        current = None
        for line in path.read_text(encoding="utf-8").splitlines():
            m = SUMMARY.search(line)
            if m:
                current = m.group(1)
                continue
            m = REVIEW.search(line)
            if m and current:
                due = date.fromisoformat(m.group(1))
                if due <= today:
                    overdue.append(f"- {area}: {current} (due {due.isoformat()})")

    if overdue:
        print("\n".join(overdue))
    else:
        print("None")
    return 0


if __name__ == "__main__":
    sys.exit(main())
