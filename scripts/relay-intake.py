#!/usr/bin/env python3
"""Relay intake: fetch make.fun competitions hourly, create a task packet
for each new slug, skip duplicates. Writes packets under tasks/<slug>/.
Logs to logs/relay-intake-<date>.log. Exits 0 on success.

Usage: python3 scripts/relay-intake.py [--repo DIR]
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

API = "https://make.fun/api/competitions?limit=200"


def log(msg, log_path):
    line = f"{datetime.now(timezone.utc).isoformat()} {msg}"
    print(line)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def fetch_competitions():
    out = subprocess.run(
        ["curl", "-sS", "--max-time", "60", "-H", "Accept: application/json", API],
        capture_output=True, text=True, timeout=90,
    )
    if out.returncode != 0:
        raise RuntimeError(f"curl exit {out.returncode}: {out.stderr.strip()[:200]}")
    data = json.loads(out.stdout)
    return data.get("items") or []


def packet_text(c):
    slug = c.get("slug", "")
    title = c.get("title", "")
    url = "https://make.fun" + (c.get("url") or f"/bounty/{slug}")
    deadline = c.get("deadline", "")
    reward = c.get("rewardAmount", "")
    desc = (c.get("description") or "").strip()
    return f"""# Task Packet — {slug}

## Competition

- **Slug:** {slug}
- **Title:** {title}
- **URL:** {url}
- **Deadline:** {deadline}
- **Reward:** {reward}
- **Status:** intake

## Judging criteria

(To be filled from the competition description/rules.)

## Rules

(To be filled from the competition description/rules.)

## Description

{desc}

## Top entries (for competitiveness verdict)

| Rank | Handle | Title | Rate/Score |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

## ChatGPT analysis

- Date:
- Summary:
- Winning angle:
- Gap to beat:

## Strategy

- Concept (chosen):
- Concepts considered (at least 3 for open-ended tasks):
- Keep:
- Cut:
- One biggest change:

## Drafts

| Version | Date | What changed | Scorecard |
|---|---|---|---|
| v1 | | | |

## Approval

- **Final submission approved by owner:** no
- **Date / note:**

## Changelog

See `changelog.md` in this task folder.
"""


def is_open(c, now):
    """Only track competitions still open: status 'open' and deadline in the future."""
    if c.get("status") != "open":
        return False
    dl = c.get("deadline") or ""
    try:
        dl_dt = datetime.fromisoformat(dl.replace("Z", "+00:00"))
    except Exception:
        return False
    return dl_dt > now


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = ap.parse_args()
    repo = args.repo
    tasks_dir = os.path.join(repo, "tasks", "incoming")
    logs_dir = os.path.join(repo, "logs")
    os.makedirs(tasks_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_path = os.path.join(logs_dir, f"relay-intake-{today}.log")

    try:
        comps = fetch_competitions()
    except Exception as e:
        log(f"FETCH FAILED: {e}", log_path)
        return 0  # Do not spam; next hourly run retries.

    now = datetime.now(timezone.utc)
    comps = [c for c in comps if is_open(c, now)]
    existing = set()
    for sub in ("incoming", "active", "completed"):
        d = os.path.join(repo, "tasks", sub)
        if os.path.isdir(d):
            existing |= {x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x))}
    new_count = 0
    for c in comps:
        slug = c.get("slug", "")
        if not slug or slug in existing:
            continue
        task_dir = os.path.join(tasks_dir, slug)
        os.makedirs(task_dir, exist_ok=True)
        with open(os.path.join(task_dir, "packet.md"), "w", encoding="utf-8") as f:
            f.write(packet_text(c))
        # Seed an empty changelog from the template.
        with open(os.path.join(task_dir, "changelog.md"), "w", encoding="utf-8") as f:
            f.write(f"# Changelog — {slug}\n\n## v1 — {today}\n\n- Changed: intake (packet created by relay)\n- Fixed: -\n- Scorecard: -\n- Result: intake\n\n## Notes\n\n- Revision cycles used: 0 / 5\n- Quality still improving? -\n- Submitted? no\n- Outcome: -\n")
        log(f"NEW TASK: {slug} | {c.get('title','')} | reward {c.get('rewardAmount','')} | deadline {c.get('deadline','')}", log_path)
        new_count += 1

    log(f"INTAKE DONE: {len(comps)} competitions seen, {new_count} new packets.", log_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
