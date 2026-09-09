# LOOP — write, review, revise, compile, relearn

Order of chapters (statistics first, as the examiner ruled):
1. ch2-preliminaries (foundation everyone cites)
2. ch3-certification
3. ch4-sharpness-blocking
4. ch5-identifiability
5. ch1-introduction (written after results so it describes what exists)
6. ch6-usd-validation
7. ch7-zar-coda
8. appA-tenor, appB-proofs-standard, appC-data-code
9. ch8-conclusions, frontmatter (abstract last)

Per chapter:
- WRITE: `thesis-writer` agent. Inputs: STANDARD, LESSONS, GROUND-TRUTH, the chapter brief. Output: the .tex file. Must end by appending a short "writer's open questions" list to LESSONS.md under the chapter heading.
- REVIEW-DOMAIN: `thesis-statistician` for ch3, ch4, ch6 statistics parts, appB; `thesis-finance-theorist` for ch2 finance parts, ch5, ch6 finance parts, ch7, appA. Edits the file directly. Appends lessons.
- REVIEW-EXAMINER: `thesis-examiner`. Structure, honesty, length vs budget, Wits compliance. Edits directly. Appends lessons.
- COMPILE: orchestrator runs `cd "~/Desktop/PhD Thesis/Council" Workspace/thesis" && tectonic main.tex`; fixes errors; records pages in PROGRESS.md.

Relearning: LESSONS.md is read at the start of EVERY agent run. A lesson has the form
`- [YYYY-MM-DD][reviewer][chapter] LESSON: <one sentence rule>. WHY: <one sentence>. APPLIES TO: <chapters>.`
Writers must state at the top of their run which lessons they applied.

## Fifty-agent orchestration (added 2026-09-09)
Stages per round; agents within a stage run in parallel, stages run in sequence. Every agent reads LESSONS.md first and appends to it last.
1. SCOUT: thesis-scout, thesis-scout-literature, thesis-scout-wits-admin, thesis-data-engineer-usd, thesis-data-engineer-zar, thesis-bibliography-verifier.
2. WRITE: thesis-writer (generalist) or the chapter-specific writer for the chapter in LOOP order; thesis-code-multicurve and thesis-code-conformal alongside ch2/ch3.
3. DOMAIN REVIEW (parallel on the fresh chapter): statistics chapters -> thesis-reviewer-conformal, -mixing, -minimax, -empirical-process; finance chapters -> thesis-reviewer-forward-measures, -sabr, -identifiability, -benchmark-reform; empirical chapters -> thesis-reviewer-practitioner, -regulatory, -sa-context.
4. ADVERSARIES (parallel): thesis-adversary-thm6 / -thm9 / -thm3 as applicable, thesis-counterexample-hunter, thesis-proof-step-checker.
5. CONSISTENCY (parallel): thesis-honesty-auditor, thesis-notation-keeper, thesis-crossref-checker, thesis-redundancy-cutter, thesis-figure-planner, thesis-language-editor.
6. EXAMINE: thesis-examiner-internal, then -external-sa / -external-intl as applicable.
7. BUILD AND TRACK: thesis-latex-builder, thesis-page-budget-auditor, thesis-progress-tracker, thesis-lessons-curator.
8. END-GAME (once all chapters exist): thesis-writer-ch8-conclusions, thesis-writer-abstract, thesis-viva-questioner, thesis-defence-rehearsal-panel, thesis-publication-strategist, thesis-supervisor-liaison.
Conflict rule: two agents never edit the same file in the same stage. Reviewers in stage 3 edit disjoint sections when on one file (orchestrator assigns sections) or run sequentially.

## Reference pipeline (added 2026-09-09)
- Stage 1 always includes `thesis-reference-librarian` runs over every key in References.bib that lacks a Highlights note: locate an open-access PDF, download to References/PDF/<key>.pdf, write References/Highlights/<key>.md (bibliographic record, URL, licence, list of the theorems/pages relevant to the thesis with short verbatim excerpts and locators, and the chapters that should cite them), and produce References/PDF/<key>.highlighted.pdf with the relevant passages highlighted.
- Stage 5 always includes `thesis-citation-enforcer` on every chapter touched in the round.
- A new key added to References.bib by any agent triggers a librarian run before the next WRITE stage.

## Iterative improvement protocol (added 2026-09-09, binding)
Every chapter cycles through numbered review rounds until accepted. Direct edits by referees remain allowed for outright errors, but the driver of improvement is the report-and-response cycle below.

Round k for chapter X:
1. REVIEW. `thesis-review-panel` reads chapter X, CONTENT-MAP.md and every other drafted chapter for repetition, and writes `thesis/reviews/X/round-k-review.md`:
   - Verdict: ACCEPT | MINOR | MAJOR | REWRITE.
   - Numbered items, each tagged [ADD] [REMOVE] [FIX] [CITE] [PROVE] [CUT-REPETITION] [CLARIFY], with: location (section/label), what exactly, why (rule or mathematics), priority (must / should).
   - A "content it is missing for a strong PhD chapter" paragraph and a "content that should go" paragraph.
   - Re-check of every item from round k-1: CLOSED / NOT CLOSED with reason.
2. REVISE. `thesis-revision-writer` reads the report, edits chapter X, and writes `thesis/reviews/X/round-k-response.md` answering every numbered item: DONE (how), DECLINED (why, with a lesson if it is a rule conflict), DEFERRED (to which chapter or round).
3. Orchestrator compiles, syncs, commits with a plain message, pushes, logs the round in CHANGES_REVIEW.md.
4. Repeat. A chapter is CLOSED for the round when the panel returns ACCEPT with zero must-items. Cap: 5 rounds per chapter per session; remaining items go to `thesis/reviews/X/OPEN.md` and PROGRESS.md.
5. Relearning: panel and reviser both append lessons; the panel's round-k report must list which LESSONS entries it enforced.

Panel composition per chapter (the panel agent adopts these perspectives in one report): statistics chapters (3, 4, 6-stats, App B): conformal, mixing, minimax, empirical-process, honesty, examiner. Finance chapters (2-rates, 5, 7, App A): forward measures, SABR, identifiability, benchmark reform, practitioner, honesty, examiner. Empirical (6): practitioner, regulatory, figure-planner, data engineers, honesty, examiner. Every panel also applies the zero-hallucination citation rule.
