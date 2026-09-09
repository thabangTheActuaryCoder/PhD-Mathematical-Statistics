---
name: wits-thesis
description: "Write, review and assemble the PhD thesis 'Pricing and Hedging Through a Benchmark Transition Without an Options Market' (Wits Mathematical Statistics) as a LaTeX book in "~/Desktop/PhD Thesis/Council" Workspace/thesis". Use whenever the user asks to write, extend, review, revise or compile any thesis chapter, appendix or front matter, or mentions the thesis loop, the lessons file, or the chapter writers/reviewers."
---

# /wits-thesis

One thesis, one standard, one loop. Everything below is binding for every agent that touches `"~/Desktop/PhD Thesis/Council" Workspace/thesis/`.

## Files
- `references/STANDARD.md` — format, notation, writing rules, chapter template, page budget. Read fully before writing.
- `references/LESSONS.md` — the relearning file. Every reviewer APPENDS dated lessons; every writer READS it first and applies every lesson. Never delete entries; mark superseded ones.
- `references/GROUND-TRUTH.md` — pointer to the corrected mathematics (`"~/Desktop/PhD Thesis/Council" Workspace/13-mathematics-3yr.tex`) and the rules for what may be claimed as proved vs target.
- `references/LOOP.md` — the write → review → revise → compile protocol and the order of chapters.

## The loop (short form)
1. Writer drafts a chapter into `thesis/chapters/<file>.tex` following STANDARD + LESSONS + GROUND-TRUTH.
2. Domain reviewer (statistician or finance theorist) reads the chapter, EDITS it directly to fix errors, and APPENDS lessons to LESSONS.md.
3. Examiner reviews structure, length, Wits compliance, honesty of claims; edits; appends lessons.
4. Orchestrator compiles with `tectonic main.tex` in `thesis/`, fixes LaTeX errors, records page count in `references/PROGRESS.md`.
5. Next chapter's writer reads the updated LESSONS.md first. That is the relearning.

## Hard rules
- Nothing is called "proved" unless its proof is written out in the chapter or it is a cited standard result with a full citation.
- Target theorems carry a `\gap{...}` box stating exactly what remains.
- No padding. Length comes from full derivations of standard results, worked examples, algorithms, data specifications, planned-figure specs with captions, and honest discussion.
- Use only the macros in `thesis/macros.tex`. Do not define new commands in chapters.
- Every planned figure is `\figplan{what it shows}{caption}`; every planned computation is a `\datanote{...}`.
