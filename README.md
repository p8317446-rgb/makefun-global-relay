# makefun-global-relay

Global work relay connecting **Muse**, **ChatGPT**, **GitHub**, and **make.fun** — one coordinated workflow for tasks, bounties, competitions, and make.fun projects.

## What this is

A relay, not a dashboard. It moves work through a fixed loop:

```
Intake → Analysis → Strategy → Draft → Review → Revision → Re-evaluation
```

- **Muse** is the task monitor and intake agent. It watches make.fun, detects new bounties/tasks, records deadline, judging criteria, reward, rules, and URL, avoids duplicates, and hands each new task to ChatGPT.
- **ChatGPT** is the strategist, researcher, creative agent, developer, reviewer, and revision agent.
- **GitHub** is the single source of truth. Every draft, revision, evaluation score, and changelog lives here and is traceable.
- **make.fun** is where entries are submitted — but only with the owner's approval.

## Layout

| Path | Purpose |
|---|---|
| `config/relay-config.json` | Relay settings: accounts, cadence, permissions, limits |
| `agents/muse.md` | Muse's role, duties, and operating rules |
| `agents/chatgpt.md` | ChatGPT's roles and how it is consulted |
| `workflow/autonomous-loop.md` | The Intake → Re-evaluation loop, step by step |
| `templates/task-packet.md` | Template for a new task packet |
| `templates/review-scorecard.md` | Template for a review / evaluation scorecard |
| `templates/changelog.md` | Template for a per-task changelog |
| `tasks/` | One folder per task (packet + drafts + revisions) |
| `submissions/` | Receipts and records of submitted entries |
| `evaluations/` | Scorecards and verdicts |
| `logs/` | Relay run logs |

## Permissions (@pejuang)

Automatic (no approval needed):
- Research, analysis, coding, drafting, review, revision.

Needs the owner's explicit approval:
- Final submission, any transaction, account security changes, or any other sensitive action.

This is enforced by the relay, not just documented. A task packet must not reach "submit" without an approval record.

## Revision policy

If an entry is judged poor, fails, or does not get the expected result:
1. Analyse the shortcomings.
2. Study the criteria and any available feedback.
3. Build an improved version.
4. Repeat review and revision for **at most 5 cycles**, or until quality stops improving.

## Monitoring

Muse checks make.fun **every 1 hour** for new bounties/tasks. New tasks become task packets in `tasks/`. Duplicates are skipped by slug + competition id.

## Status

See `logs/` for run history and `config/relay-config.json` for the current connection status. The relay is only "active" once it has been tested end-to-end (intake → packet → ChatGPT analysis → draft → review). Do not claim it is active before that test passes.
