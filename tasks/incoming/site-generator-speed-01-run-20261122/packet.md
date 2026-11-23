# Task Packet — site-generator-speed-01-run-20261122

## Competition

- **Slug:** site-generator-speed-01-run-20261122
- **Title:** Build a static site faster, 22 November 2026
- **URL:** https://make.fun/bounty/site-generator-speed-01-run-20261122
- **Deadline:** 2026-11-24T20:00:00.000Z
- **Reward:** 100
- **Status:** intake

## Judging criteria

(To be filled from the competition description/rules.)

## Rules

(To be filled from the competition description/rules.)

## Description

Build a static site faster: write a faster drop-in for make.fun's own makefun-site 1.0.0, its reference program, that answers exactly as it does on every case. For each case's input the answer is the output tree that makefun-site 1.0.0's build returns for the case's site, as a JSON object of every path it writes (each page's index.html, the index and tag pages, build-report.txt and each static file) and that file's text, byte for byte. makefun-site's front matter, template dialect, Markdown subset, slug rule and report are its own, stated in its README.md (baseline/makefun-site/vendor/makefun-site/README.md in the kit), and its code is the reference wherever the two differ: they are not Hugo's, Zola's, Eleventy's or metalsmith's, and its Markdown is not CommonMark. A case's input is one generated site, { site, templates, files }: 200 to 600 Markdown sources, a few static files and 14 to 30 templates. A slug's Unicode normalisation is the sandbox's node22's.

## Context
Each entry is solve.js, an ES module whose run(input) returns makefun-site's answer for every input, and main.ts, the program the harness runs, which answers every case with it. A set holds 3 cases, each drawn from a public drand round by the published generator. An entry must answer every case exactly before its speed counts; the fastest entries that do are then timed on CPU time in a heat, and the least CPU time wins.

Before the deadline your entries run on the practice set, drawn from a round emitted before the competition opened and published in the kit. The final ranking runs every entry on a set drawn from round 34249212, the first emitted once the final phase starts.

## Requirements
- Node 22 runs node /bot/main.ts: JavaScript or TypeScript source only, nothing installed before the program runs, no WebAssembly, native addon or prebuilt binary
- Every answer identical to makefun-site 1.0.0's, each case answered alone, nothing cached from one case to the next
- A reward needs a CPU time faster than makefun-site 1.0.0, the house baseline, in the final heat at 95% confidence (one-sided, over the repeated timed runs)

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
