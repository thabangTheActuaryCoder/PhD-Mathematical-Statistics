# Council agents and the thesis skill

Everything that writes, reviews and assembles this thesis is defined in plain files so it can be re-used in any future session.

## Where they live

| Location | Contents |
|---|---|
| `~/.claude/skills/wits-thesis/` | The skill: `SKILL.md` plus `references/` (STANDARD, LESSONS, GROUND-TRUTH, LOOP, CONTENT-MAP, ROSTER, PROGRESS) |
| `~/.claude/agents/thesis-*.md` | 59 agent definitions |
| `.claude/skills/` and `.claude/agents/` in this repository | Versioned copies of both, so a fresh clone carries the council |

Claude Code loads the user-level copies automatically; the repository copies are picked up when this repository is the working directory. Keep them in sync with `rsync -a ~/.claude/skills/wits-thesis/ .claude/skills/wits-thesis/ && cp ~/.claude/agents/thesis-*.md .claude/agents/`.

## How to call them

- **The skill:** type `/wits-thesis` or ask to "write, review, revise or compile" any chapter. The skill loads the standard, the lessons and the loop protocol.
- **An agent by name:** ask for it directly, for example "run thesis-review-panel round 2 on chapter 3" or "have thesis-reference-librarian process key yu1994". Agents appear as types in the Agent tool after the session that creates them.
- **The loop for one chapter:** `thesis-writer` (or the chapter-specific writer) drafts; `thesis-review-panel` writes `Reviews/<chapter>/round-k-review.md` with numbered [ADD]/[REMOVE]/[FIX]/[CITE]/[PROVE]/[CUT-REPETITION] items; `thesis-revision-writer` applies them and writes `round-k-response.md`; repeat until ACCEPT with zero must-items or five rounds; then `thesis-latex-builder`, sync, commit, push.
- **Relearning:** every agent reads `references/LESSONS.md` first and appends to it last. Read that file to see what the council has learned so far.

## The roster

Writers: `thesis-writer`, `thesis-writer-ch1-intro`, `-ch4-blocking`, `-ch5-theorems`, `-ch6-results`, `-ch7-zar`, `-ch8-conclusions`, `-appA-tenor`, `-appB-proofs`, `-appC-data`, `-abstract`, `thesis-revision-writer`.
Referees: `thesis-statistician`, `thesis-finance-theorist`, `thesis-reviewer-conformal`, `-mixing`, `-minimax`, `-empirical-process`, `-forward-measures`, `-sabr`, `-identifiability`, `-benchmark-reform`, `-practitioner`, `-regulatory`, `-sa-context`, `thesis-review-panel`.
Adversaries and checkers: `thesis-adversary-thm3`, `-thm6`, `-thm9`, `thesis-counterexample-hunter`, `thesis-proof-step-checker`, `thesis-honesty-auditor`, `thesis-citation-enforcer`, `thesis-notation-keeper`, `thesis-crossref-checker`, `thesis-redundancy-cutter`, `thesis-page-budget-auditor`, `thesis-language-editor`, `thesis-figure-planner`.
Sources and data: `thesis-reference-librarian`, `thesis-bibliography-verifier`, `thesis-scout`, `thesis-scout-literature`, `thesis-scout-wits-admin`, `thesis-data-engineer-usd`, `thesis-data-engineer-zar`, `thesis-code-multicurve`, `thesis-code-conformal`.
Build and management: `thesis-latex-builder`, `thesis-lessons-curator`, `thesis-progress-tracker`, `thesis-supervisor-liaison`, `thesis-publication-strategist`.
Examination: `thesis-examiner`, `thesis-examiner-internal`, `thesis-examiner-external-sa`, `thesis-examiner-external-intl`, `thesis-viva-questioner`, `thesis-defence-rehearsal-panel`.

The full one-line purpose of each is in `.claude/skills/wits-thesis/references/ROSTER.md`.
