# Autonomous Loop — Intake → Re-evaluation

One pass through the loop for each task. The loop is driven by Muse, advised by ChatGPT, and recorded in GitHub.

## Stages

### 1. Intake (Muse)
- Fetch make.fun competitions (hourly).
- New slug → create `tasks/incoming/<slug>/packet.md` from `templates/task-packet.md`.
- Record: slug, title, deadline, judging criteria, reward, rules, URL.
- Dedupe by slug. If a packet already exists, skip.
- Log the intake in `logs/`.

### 2. Triage (Muse)
- Move the packet from `tasks/incoming/` to `tasks/active/`.
- Decide: pursue, skip, or defer.
  - Skip: paid-entry bounties the owner declined, tasks needing phone-only steps with no draft possible, or entries already at maximum score with no real improvement path.
  - Defer: competition not yet open, or blocked on an owner step — record what is needed.
- Set the packet status and the priority (by deadline, soonest first).

### 3. Research (ChatGPT + Muse)
- Gather facts and verify claims about the competition and its top entries.
- Read the criteria and rules from the competition API (the first criterion is the gate).
- Study ALL entrants by tier (rank 1–3 winning pattern, 4–10 gaps, 11–50 clichés to avoid, middle/bottom repeated mistakes).
- Save the research in `tasks/active/<slug>/research.md`.

### 4. Analysis (ChatGPT + Muse)
- Send the packet to ChatGPT.
- Attach the current top entries (rank 1–4) for a competitiveness verdict.
- ChatGPT returns: what wins here, what the leaders do well, where the gap is.
- Save the analysis in `tasks/active/<slug>/analysis.md`.

### 5. Strategy (ChatGPT)
- ChatGPT proposes the angle: what to build, what to cut, the one change most likely to beat the leaders.
- For open-ended tasks, at least 3 concepts, then pick the strongest.
- Save the strategy in `tasks/active/<slug>/strategy.md`.

### 6. Draft (Muse)
- Build the first version from the strategy.
- Save the draft in `tasks/active/<slug>/draft-v1/` (or the task's repo/folder).
- Record what was built and what was deliberately left out.

### 7. Review (ChatGPT + Muse)
- Send the draft (or screenshots/description) to ChatGPT for a sharp review.
- Score it with `templates/review-scorecard.md` and save to `evaluations/<slug>-v<n>.md`.
- The review must name what is boring, weak, or would lose pairwise. No empty praise.

### 8. Revision (Muse)
- Turn the review into concrete fixes, prioritised by impact.
- Build the next version (`draft-v<n+1>/`).
- Update the changelog (`tasks/active/<slug>/changelog.md`, from `templates/changelog.md`).

### 9. Re-evaluation (ChatGPT + Muse)
- Review the new version the same way. Score it again.
- If the score improved, the loop may continue.
- **Stop when:** 5 revision cycles are used, or quality stops improving.
- If the entry is judged poor, fails, or does not get the expected result, analyse the shortcomings, study the criteria/feedback, and build an improved version — within the same 5-cycle cap.

## Submission

- A task reaches "submit" only with the owner's explicit approval, recorded in the packet.
- Final submission, transactions, account security changes, and sensitive actions are never automatic.
- After submission, save the receipt in `submissions/drafts/` (draft receipt) or `submissions/revisions/` (revised entry receipt) and note the outcome in the changelog.
- When a task is done (submitted or closed), move its folder from `tasks/active/` to `tasks/completed/`.

## Traceability

Every task folder keeps: packet, research, analysis, strategy, each draft version, each scorecard, and the changelog. Nothing is overwritten; new versions get new numbers.
