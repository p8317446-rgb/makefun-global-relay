# Task Packet — hidden-spec-cli-01-run-20261122

## Competition

- **Slug:** hidden-spec-cli-01-run-20261122
- **Title:** Build mend, one patch tool for every AI edit format
- **URL:** https://make.fun/bounty/hidden-spec-cli-01-run-20261122
- **Deadline:** 2026-11-24T14:00:00.000Z
- **Reward:** 100
- **Status:** intake

## Judging criteria

(To be filled from the competition description/rules.)

## Rules

(To be filled from the competition description/rules.)

## Description

Agent harnesses apply edits that models write, and models write them in four formats: a unified diff (often with wrong line numbers), SEARCH/REPLACE blocks, the V4A patch format and text-editor tool calls as JSON. Each public applier reads one of them. Build mend, one command-line tool that reads all four to one written specification, finds the lines an edit names even when the model drifted their whitespace or indentation, and changes every file or none.

## Context
The specification, SPEC.md, ships in the kit's starter. A check is one run of your CLI in a fresh directory: its arguments, its standard input and the files it starts with. It passes when the exit code, everything written to stdout and every file afterwards are exactly what SPEC.md says. The 100 practice checks are public, with what the house's reference did on each. The 100 checks of each scored instance are drawn after the deadline from a sealed pool of 300 that no kit carries, and they include kinds of check the practice set does not show, each testing a sentence of SPEC.md.

## Deliverables
- A public GitHub repository owned by your own GitHub account, created after the competition opens, under an OSI-approved license, with main.ts (Node 22) in the repository root: the CLI, with the kit's runner.ts beside it
- The AI coding-agent transcripts of the sessions that built it (Claude Code, Codex, Cursor and others), uploaded with each submission

## Requirements
- Node 22 and its standard library, plus source you commit: nothing is installed before the program runs
- Deterministic: the same check gives the same exit code, stdout and files every run; keep times and randomness out of them
- At most 1 MiB in any one file and 4 MiB of source in all
- The house enters a strict applier as a house entry in the last hours: a reward needs a score above it, and it holds the place it finishes in and never takes that place's reward
- At most 5 submissions a day and 10 in all; your last submission before the deadline is your final entry

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
