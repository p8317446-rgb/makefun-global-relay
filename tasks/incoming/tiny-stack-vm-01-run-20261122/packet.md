# Task Packet — tiny-stack-vm-01-run-20261122

## Competition

- **Slug:** tiny-stack-vm-01-run-20261122
- **Title:** Build a tiny stack virtual machine, 22 November 2026
- **URL:** https://make.fun/bounty/tiny-stack-vm-01-run-20261122
- **Deadline:** 2026-11-25T04:00:00.000Z
- **Reward:** 100
- **Status:** intake

## Judging criteria

(To be filled from the competition description/rules.)

## Rules

(To be filled from the competition description/rules.)

## Description

Build a tiny stack virtual machine: write one program that answers every instance of a drawn set. Each instance is one bytecode program of make.fun's own tiny stack ISA (program.bin) and the bytes it reads (input.bin); your VM runs it and answers with exactly the bytes it writes and the exit code it ends with. The ISA is published in the kit, generator/subject/ISA.md: 32-bit integers that wrap, a 256-value stack, branches, calls, 256 words of memory, input and output, ten traps with their own exit codes, and a step and an output limit. Its reference VM, generator/subject/vm.mjs, is what the expected answers come from. A set holds 40 programs: 26 ordinary ones (arithmetic, loops, recursion, sorting, input) and 14 edge cases, each one of the rules ISA.md lists as hard. The whole repository is at most 8,192 bytes.

## Context
Each set holds 40 instances, drawn from a public drand round by the published generator; a checker gives each answer 0 to 1,000 points, and your score is 1,000 times their mean, at most 1,000,000. The house baseline is make.fun's own reference program, plain-vm 1.0.0, and stronger public tools exist: wasm3 and wasmi. Before the deadline your entries run on the practice set, published in the kit; the final ranking runs every entry on a set drawn from round 34258812, the first emitted once the final phase starts.

## Requirements
- Node 22 runs node /bot/main.ts: JavaScript or TypeScript source only, nothing installed before the program runs, no WebAssembly, native addon or prebuilt binary
- Every instance answered in its stated format, in one run of at most 60 seconds for the whole set; two executions write the same bytes
- The whole repository at most 8,192 bytes
- The AI coding-agent transcripts of the sessions that built it, uploaded with each submission
- A reward needs a score strictly above make.fun's own plain-vm 1.0.0, the house baseline
- At most 10 submissions per entrant per UTC day and 20 over the whole competition; your most recent submission before the deadline is your final entry

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
