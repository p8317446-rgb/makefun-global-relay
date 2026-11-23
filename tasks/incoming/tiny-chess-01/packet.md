# Task Packet — tiny-chess-01

## Competition

- **Slug:** tiny-chess-01
- **Title:** Build the strongest chess engine in 4 KB of Python
- **URL:** https://make.fun/bounty/tiny-chess-01
- **Deadline:** 2026-11-24T17:00:00.000Z
- **Reward:** 500
- **Status:** intake

## Judging criteria

(To be filled from the competition description/rules.)

## Rules

(To be filled from the competition description/rules.)

## Description

Write a chess engine in at most 4,096 bytes of Python and play it against a fixed gauntlet of eight house engines, from an alpha-beta search 2 plies deep up to one of 2,000,000 nodes a move. Your engine plays each of them once a trial, with white against half of them and black against the others, and its results become an Elo rating anchored to the house engines' own ratings. To take a prize it must also beat the house baseline: sunfish's 4 KB engine, the strongest public chess engine in 4 KB of Python.

## Context
Each trial is 8 games. Your program talks to the env at MAKEFUN_ENV_URL: it asks for the game in play, sends its moves in UCI, and the house engine answers each move. A game ends by the rules of chess, by adjudication on material at 200 plies, on time (10 seconds a move) or by resignation. A trial's Elo is the rating at which your expected points against the eight anchored opponents add up to the points you scored, from 0 to 2,112, and the final's contenders rank on its mean over 6 trials, with your wins, draws and losses beside it.

Every game starts from a book opening. Before the deadline your entries play the practice openings, drawn from a drand round emitted before the competition opened and published in the kit, on practice trials of 6 games against the gauntlet's first six engines. The final draws 6 new sets of openings from the first drand round emitted 5 minutes after the deadline: every entry with a practice Elo of at least 1,154 plays the first set once, and the 50 entrants with the highest Elo there play all 6, every trial of theirs replayed.

## Deliverables
- A public GitHub repository owned by your own GitHub account, created after the competition opens, under an OSI-approved license, with your engine at main.py (Python 3.13) in the repository root; or the same files as a source bundle uploaded with `makefun bundle`
- The AI coding-agent transcripts of the sessions that built it (Claude Code, Codex, Cursor and others), uploaded with each submission

## Requirements
- main.py at most 4,096 bytes as committed, comments, whitespace and any compressed payload with its unpacker included; the whole repository at most 8,192 bytes, no file over 4,096
- Python 3.13 and its standard library: main.py alone is the engine, and it reads, imports or runs no other file of your repository
- Deterministic: search to a fixed depth or a fixed number of nodes, never to a clock, and no unseeded randomness, so the replay plays the same moves
- No model calls: any call disqualifies the entry
- At most 10 seconds a move; at most 1,800 seconds of wall time a trial, the house's thinking included (about 3 seconds a move on average), 1 CPU, 512 MB and 64 processes
- A practice Elo of at least 1,154 to enter the final, on the entry you have in at the deadline
- A prize needs a mean Elo above the house baseline's, sunfish's 4 KB engine
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
