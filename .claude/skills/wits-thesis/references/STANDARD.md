# STANDARD — how the thesis must look

## Institution and format
- University of the Witwatersrand, Faculty of Science, School of Statistics and Actuarial Science. PhD by thesis.
- LaTeX `book` class, A4, 11pt, one-and-a-half spacing, twoside/openright. Chapters start on odd pages.
- Front matter in order: title page; declaration (Wits wording: "I declare that this thesis is my own, unaided work..."); abstract (max 350 words); dedication (optional); acknowledgements; contents; list of figures; list of tables; notation and abbreviations.
- Back matter: appendices; bibliography (author–year, `plainnat`).
- Headers: chapter title left on even pages, section title right on odd pages. Page number centred.

## Chapter template (every main chapter)
1. Chapter abstract (5–8 lines, italic) stating what the chapter establishes and what it leaves open.
2. Introduction to the chapter (1–2 pages): question, why it matters for the thesis, map of sections.
3. Body sections. Definitions before use. Every theorem: statement, then proof or proof route + `\gap{}`.
4. Worked example or numerical illustration where the content admits one.
5. Discussion (1–2 pages): what was shown, limitations, connection to next chapter.
6. Chapter notes (optional): literature remarks, attribution.

## Notation (from thesis/macros.tex; use nothing else)
- Measures: `\Q^{T+\Delta}` forward measure; `\Prob` physical; `\E` expectation.
- Rates: `F_t` forward compounded rate; `L_t` JIBAR forward; `B_t = L_t - F_t - s` basis; `s` fallback spread; `R(T,T+\Delta)` realised compounded rate.
- SABR: `(\alpha_0,\beta,\rho,\nu)`; decay `g`; clock `\tau(t)=\int_0^t g^2`.
- Basis: volatility `\eta`; correlations `\rho_{BF}`, `\rho_{B\alpha}`; scale `\varepsilon = \eta/(\alpha_0 F_0^\beta)`.
- Statistics: scores `S`, laws `P` (calibration) and `Q` (deployment); `\dK`, `\dTV`, `\Wone`, `\Winf`; blocks `n`, length `b`, record `N`; `k=\lceil(1-\alpha)(n+1)\rceil`; `\hat q = S_{(k)}`; mixing `\beta(k)`, class `\Bclass{r}`.
- Policy: `\pi` fixed on `\Dfit`.

## Writing rules
- Plain declarative prose. One idea per sentence. No hedging adverbs.
- Define, state, prove, illustrate, discuss. In that order.
- Standard results (Berbee coupling, DKW, Beta law of conformal coverage, Hagan formula components, forward-measure change, Bobkov–Ledoux 1-D W1 rate, Itô time change) are PROVED IN FULL in the chapter or Appendix B, with citation. This is where honest length comes from.
- Target theorems: statement in theorem environment, `\begin{route}...\end{route}`, then `\gap{exact list of what is not yet established}`.
- Every numerical claim has a source or a `\datanote{}`.
- Figures that need data not yet available are `\figplan{}{}` with a full caption describing axes, series and the claim the figure will test.
- Cite with author–year keys in `thesis/bibliography.tex` (thebibliography with `\bibitem[Author(Year)]{key}`). Do not invent references; use only those in bibliography.tex or add with full details you are certain of.

## Page budget (target 310–360 typeset pages)
| Part | Pages |
|---|---|
| Front matter | 18 (reset 2026-09-09 after audit: Wits three-level TOC) |
| Ch1 Introduction and the South African transition | 24 |
| Ch2 Preliminaries: rates, SABR, forward measures, conformal prediction, mixing | 48 |
| Ch3 Finite-sample certification of hedging error | 44 |
| Ch4 Sharpness and optimal blocking (the doctoral theorem) | 40 |
| Ch5 Identifiability of the successor-rate smile | 44 |
| Ch6 USD LIBOR-to-SOFR validation | 40 |
| Ch7 The South African converted book | 20 |
| Ch8 Conclusions | 10 |
| App A Tenor consistency | 14 |
| App B Proofs of standard results | 30 |
| App C Data, code, reproducibility | 16 |
| Bibliography | 10 |
Roughly 300 words per page at 12pt, 1.5 spacing, Wits margins (verified by scout) with displayed mathematics.

## Inspiration (structure only, never copy text)
UCT AIFMRM and Wits mathematical-finance doctorates: a long self-contained preliminaries chapter; each results chapter openable on its own; an empirical chapter with a reproducibility appendix; conclusions that list limitations before contributions.

## Structural precedents (scout, 2026-09-09; structure only, no text copied)
Repositories: OpenUCT (open.uct.ac.za) and WIReDSpace returned HTTP 500/504 on 2026-09-09; PDFs were read from the CORE mirror of OpenUCT. Handle URLs given for citation.

1. Mavuso, M. M. (2015). *Mean-variance hedging in an illiquid market*. MPhil (Mathematical Finance), Dept of Actuarial Science, Faculty of Commerce, UCT. Supervisor T. McWalter. 61 pp. https://open.uct.ac.za/handle/11427/15595 (mirror https://core.ac.uk/download/43968147.pdf)
   - Front matter: title page (dated) → UCT copyright page → declaration (UCT wording, own unaided work, dated) → abstract (one page) → acknowledgements (dedication folded in) → contents (three levels) → list of figures. No list of tables, no notation list.
   - Chapters: 1 Introduction (problem formulation; structure of dissertation) → 2 Preliminaries (Hilbert spaces; stochastic processes; continuous trading) → 3 Results, martingale case → 4 Results, semimartingale case, with numerical subsection inside → 5 Conclusion → Bibliography. No appendices. Preliminaries are a separate chapter (~14 pp of 61).
   - Pattern: each results chapter = general theory → application → specific payoff → numerics. Numerics live inside the results chapter, not a separate empirical chapter.
   - No PhD by Melusi Mavuso was found; UCT lists him as lecturer/"Mr". A second master's-level maths thesis (semilinear elliptic PDE, handle 11427/25441) is attributed to him on OpenUCT; not inspected.

2. Robbertze, Y. (2022). *Neural network Libor market model for pricing and hedging interest rate derivatives*. Master's dissertation, Dept of Statistical Sciences, Faculty of Science, UCT. Supervisor M. Mavuso. 71 pp. https://open.uct.ac.za/handle/11427/36545 (mirror https://core.ac.uk/download/590323086.pdf)
   - Front matter (CORE copy): title page (author, department, date) → copyright page → acknowledgements → list of figures → list of tables → contents. No separate abstract page: the abstract is Section 1.1 of Chapter 1. No declaration page in the mirrored copy.
   - Chapters: 1 Introduction (abstract; literature review by model family; outline) → 2 Preliminaries (stochastic calculus; continuous-time trading) → 3 LIBOR market model (specification, instruments, volatility structures, calibration) → 4 Method (variational auto-encoders, with two toy examples) → 5 Results and Discussion (proposed structures; hedging techniques; results) → 6 Conclusions (results; pitfalls; extensions). No appendices, no bibliography entry in contents.
   - Pattern: one empirical chapter carrying all experiments, results tables summarised at chapter end; limitations ("pitfalls") get their own section in the conclusion before extensions.

3. Mahomed, O. (2024/2025). *Multi-curve frameworks and information-based models*. PhD (Quantitative Finance), AIFMRM, Faculty of Commerce, UCT. Supervisor D. Taylor. 217 pp. Mirror https://core.ac.uk/download/661229068.pdf (OpenUCT bitstream 288024ff-7f7a-45a0-9f76-7ee90e2fe7b6).
   - Front matter: title page (dated) → copyright page → declaration (UCT wording) → abstract (one page, one paragraph per Part) → acknowledgements → contents (three levels) → list of figures → list of tables.
   - Body in three Parts after two framing chapters: 1 Introduction (background; historical context; practical context; structure and contributions, one subsection per Part) → 2 Modelling Context (literature and axioms, ~22 pp) → Part I (ch 3–5) → Part II (ch 6–8) → Part III (ch 9–10) → 11 Conclusion (2 pp) → Bibliography → Glossary → Appendices A–D, one appendix per Part (A for the Introduction, B for Part I, C for Part II, D for Part III), each holding worked examples, bootstrapping details and proofs.
   - Pattern worth copying: appendix per Part keyed to the chapter group; "Structure and Contributions" section in ch 1 with one subsection per Part; glossary after bibliography. Preliminaries are a separate chapter (ch 2) but short relative to ours.

Implications for this thesis (Wits Faculty of Science style guide, see LESSONS 2026-09-09 scout entries): keep the separate Preliminaries chapter (precedent in all three), keep one appendix per results group (Mahomed pattern), and put limitations before extensions in the conclusion (Robbertze pattern). Note our appendices precede the bibliography per the Wits guide §2.2.4, unlike the UCT theses which place appendices last.

## Wits administration (verified)
Verified 2026-09-09 by thesis-scout-wits-admin from primary documents. "Verified" = read from the document at the URL given. "Unverified" = stated only where marked.

Sources (all read in full or in the cited sections):
- [FSO] Faculty of Science *Faculty Standing Orders for the degrees of MSc and PhD*, approved by Faculty Board 15 Nov 2021. https://www.wits.ac.za/media/wits-university/faculties-and-schools/science/documents/science-forms/Faculty_Standing%20Orders_%20PhD_and_MSc.pdf
- [SSO] *Senate Standing Orders on Higher Degrees*, S2013/21A, amended 09 June 2015. Live Wits URL returns 404 (2026-09-09); read from the Wayback Machine copy: https://web.archive.org/web/2020/https://www.wits.ac.za/media/wits-university/faculties-and-schools/humanities/human-and-community-development/phd/documents/2017-information/SSO%20%20Higher%20Degrees%20Amended%2009%20June%202015.pdf . This is the 2015 text; whether a later amendment exists is UNVERIFIED (none found on wits.ac.za). FSO says it "should be read in conjunction with" SSO.
- [RULES] *2026 Science Rules and Syllabuses* (General Rules G9, G10, G13; Senate Rules for the Faculty of Science 3.4.3). https://www.wits.ac.za/media/wits-university/students/academic-matters/documents/Sci_eBook.pdf
- [BOOKLET] Faculty of Science *Postgraduate Information Booklet* (updated 2021). Live URL 404 (2026-09-09); read from https://web.archive.org/web/2023/https://www.wits.ac.za/media/wits-university/faculties-and-schools/science/documents/docs-science/Postgraduate_Information_Booklet_2021.pdf
- Forms index (live): https://www.wits.ac.za/science/postgraduate/forms/ — proposal form V4 2025, intention-to-submit form, AI declaration 2024 (.docx), first-submission form V4.2, acquiescence form V4.2 (2025), nomination-of-examiners form V4 2023, examiner conflict-of-interest declaration, ETD final-submission form (May 2026), PG amendment form.

### 1. Proposal timing and defence
- Deadline: full-time PhD proposal due within six months of registration; part-time within twelve months. [FSO §8; BOOKLET p.9; SSO A.2: "no more than twelve months from initial registration (normally 6 months for full-time ... 12 months for part-time)"; if not approved "registration as a candidate shall be cancelled" unless GSC finds exceptional reasons.] The course-finder page for PhD Mathematical Statistics says "register and submit a research proposal within three months" (https://www.wits.ac.za/course-finder/postgraduate/science/phd-mathematical-statistics/) — School-level and stricter than Faculty; treat three months as the working deadline, confirm with the School.
- Route: School Postgraduate Committee or readers consider the proposal first; once accepted it is signed by candidate, supervisor(s) and PG coordinator/Head of School and emailed to the Faculty Office for the Faculty GSC, then to the GSC Chair for final approval. [FSO §8; BOOKLET p.9–10; Faculty proposal guidelines https://www.wits.ac.za/media/wits-university/faculties-and-schools/science/documents/docs-science/Guidelinesonthepreparationofaresearch%20proposal2017.pdf]
- Defence: NO Faculty of Science rule mandates an oral proposal defence. SSO A.6: "provision MAY be made by Faculties or Schools for the candidate to defend his or her proposal in a seminar"; "Proposals may be referred for revision and/or resubmission." The oft-quoted "re-present within one month / committee may terminate candidature" rule is the Faculty of HUMANITIES (School of Human and Community Development) rule, https://www.wits.ac.za/shcd/phd/ — it does not apply to Science. Whether the School of Statistics and Actuarial Science requires a seminar defence is UNVERIFIED (no School document found online; ask the PG coordinator, Dr Herbert Hove per the course-finder page).
- Proposal content and length: introduction, aim, hypotheses/questions, methodology, work plan; PhD guideline ± 3000 words; Turnitin report required, guideline similarity 15 % (supervisor motivation if higher); ORCID number required. [Proposal form V4 2025; FSO §8 items i–x.]
- Title is approved with the proposal; changes via the PG Amendment Form. [FSO §5.2]
- Extensions: at most two for the whole degree; n+1 rule (hold on registration after n+1 years; n+3 absolute). [FSO §3]

### 2. Publication before first submission
- [FSO §10.5] "The Faculty requires submission for publication of a paper to a peer-reviewed journal prior to the submission of the PhD thesis for examination. If there is a compelling reason for waiving this requirement, the Supervisor would have to motivate, and the Heads of School will use their discretion."
- First Submission form V4.2 item 5: "At least one publication or one submitted manuscript covering the PhD work is a REQUIREMENT FOR QUALIFICATION"; if none, "a motivation letter from the supervisor is required." Intention-to-submit form lists "Publications (Registered for PhD 2014 onwards)" among first-submission requirements.
- Number of publications is left to each School [FSO §10.7]; recommended venues ISI or DHET-accredited journals; author order agreed by all parties. A thesis that includes publications must remain one coherent argument [FSO §10.6]; multi-authored papers need a per-author contribution statement in the declaration [FSO §10.8]. Senate Rules 3.4.3.2 note: published results may be included only if the work was done during candidature, with the candidate's share indicated.
- SSO A.18 (2015) only "encourages" publication — the hard requirement is Faculty-level (Science), not Senate-level.

### 3. AI-use declaration
- Form: "Wits University Faculty of Science post-graduate student AI declaration" (2024, .docx) https://www.wits.ac.za/media/wits-university/faculties-and-schools/science/documents/docs-science/PG%20student%20AI%20declaration%202024.docx — required at first submission per the forms page. Content (verified from the file): undeclared use of generative AI "constitutes a form of plagiarism and is classified by Wits University as academic misconduct"; candidate ticks "did not" or "did" use, then ticks categories (idea generation; sourcing related work; methods and experiment design; data analysis; theoretical development incl. theorem proving; code development; presentation; editing; writing; citation formatting), lists each tool and its use, and confirms that integral use "is clearly outlined in the relevant experimental/methodology chapters". Signed with student number and date.
- General Rule G9.8(a) (applied to PhD by G10.3): the formal declaration must state "what assistance s/he has received, including the use of any Artificial Intelligence assistance as per the University rules or Faculty practices." [RULES 2026] This means the thesis declaration page itself must carry an AI statement, not only the separate form. The exact wording in STANDARD/LESSONS (style guide §2.1.2) predates this; add one sentence on AI assistance.
- Final ETD submission form (May 2026) item 11: "I acknowledge that my research project/report complies with the Faculty's Guidelines on the Fair Use of GAI." The Faculty of Science GAI guidelines document itself was NOT located online (UNVERIFIED); University AI policy page https://www.wits.ac.za/ai-policies/ .
- Plagiarism: Turnitin report at first submission, guideline 15 % [forms page; proposal form].

### 4. Supervisors and external co-supervisors
- Definitions [FSO p.1; SSO]: Supervisor = >50 % of supervision; Co-Supervisor = >10 % and <50 % (SSO: ≤50 %). Percentages are recorded on the proposal, intention-to-submit and examiner-nomination forms.
- External supervision [FSO §6.5]: "supervision by a member of staff of another University, or by a member of staff of a research organisation or industry, must be motivated for and approved by the GSC." [SSO A.3]: "Supervision by a member of staff of another university or other structure should be exceptional. If the Supervisor-designate is not a member of the University staff, a member of the full-time staff must be appointed as a Co-Supervisor."
- Co-supervisor appointment grounds [FSO §6.1.1–6.1.5]: supervisor retiring within a year; supervisor supervising for the first time; an external supervisor is appointed ("in which case the principal Supervisor must be from the relevant School at this University"); interdisciplinary topic; co-supervisors must consult each other regularly.
- Any change of supervision needs GSC approval via the PG Amendment Form with Head of School reasons [FSO §6.7]. Statement of principles for postgraduate supervision signed with the proposal [BOOKLET p.10]. Honoraria for external supervisors exist [SSO A.28]. Consequence for this thesis: an industry or overseas co-supervisor is permissible but the principal supervisor must be in the School of Statistics and Actuarial Science, and the arrangement must be in the proposal submission, not added informally later.

### 5. Examination
- Examiners [FSO §11.1]: "at least one internal Examiner and at least two external Examiners (of whom at least one should, if feasible, be a person who would normally be working outside South Africa)"; if no suitable internal examiner, an additional external. Internal examiner "may NOT be the Supervisor". Nomination form V4 2023 note (b): "One internal and two external examiners or three external examiners required for ... PhD, of whom one should be a foreign expert." General Rule G13.2.6: Senate appoints three examiners, two external. SSO A.24 agrees (external "should include one person working outside South Africa").
- External examiner = not involved in the work and preferably not Wits staff; Wits staff as external needs GSC motivation [FSO §11.1; SSO A.24]. Conflict rule [FSO §11.1; BOOKLET p.11]: no examiner who has been supervised by, worked with or published with the supervisor in the last 5 years, nor who supervised the supervisor in the last 10 years. Examiner CVs and a suitability statement are submitted; separate Examiner Conflict of Interest declaration form on the forms page.
- Timing: examiners nominated a minimum of three months before submission [FSO §6.1.8 / §1.1.8; BOOKLET p.11]. (SSO 2015 says six weeks; Faculty rule is stricter and governs.) Title must be confirmed at nomination.
- Turnaround: examiners asked to report within six weeks of receipt [FSO §11.1; SSO A.27]. Names confidential until the process ends and revealed only with examiner consent [FSO §11.2, 11.6].
- Oral defence: General Rule G10.1(b) [RULES 2026] requires the candidate to "present her/himself for an oral defense (Viva Voce) as stipulated in the Faculty Standing Orders or Faculty Procedure document." The Faculty of Science Standing Orders (2021) contain NO viva provision; the Senate Rules for the Faculty (3.4.3.2 c) say only "if required by the Senate". Whether a viva is now actually held in Science is UNVERIFIED — ask the Faculty Office; plan for one.
- Outcomes: unanimous favourable reports can be approved by the GSC Chair; disagreement, unfavourable or inconclusive reports go to an ad hoc committee [FSO §12; SSO A.33]. Revisions: within three months without extra fees [FSO §12.3]; SSO allows a maximum of six months.
- Supervisor's report accompanies every submission; not seen by examiners; given to the candidate afterwards [FSO §10.3; SSO A.20].

### 6. Intention to submit and submission package
- Declaration of Intention to Submit for Examination: "at least THREE months before the thesis ... is submitted for examination" [form; FSO §10.1; BOOKLET p.5]. Triggers the Faculty to prompt examiner nomination and to check title/supervisor records.
- First submission (electronic, to science.phd@wits.ac.za): First Submission form V4.2; Acquiescence form (supervisor); Turnitin report; PDF of the thesis with the signed declaration in every copy; AI declaration 2024; supervisor's report (sent separately); publication details or supervisor motivation letter. Bound copies only if the supervisor/examiner asks [FSO §10.2; RULES G10.3; forms page].
- Final submission: ETD form (May 2026) — corrected electronic copy, examiners' recommendations addressed, formal declaration signed, GAI compliance acknowledgement, copyright permissions, ETD release four months after submission unless embargo (Rule G19, up to three years once) [ETD form; SSO A.37–A.39].

### Unverified or not found (2026-09-09)
- Any Senate Standing Orders text later than the 09 June 2015 amendment.
- Whether the School of Statistics and Actuarial Science holds a seminar-style proposal defence and its timing.
- The Faculty of Science "Guidelines on the Fair Use of GAI" document.
- Whether a viva voce is currently held for Science PhDs (rule exists at G10.1(b); no Faculty procedure found).
- Rule number for the declaration: style guide cites G.28, first-submission form cites G9.7; the 2026 Rules place the formal-declaration content at G9.8 (applied to PhD via G10.3). Cite "General Rules G9.8 and G10.3 (2026)" and confirm with the Faculty Office.

## Repository (added 2026-09-09)
The thesis lives in the GitHub repository `thabangTheActuaryCoder/PhD-Mathematical-Statistics`, cloned at `"~/Desktop/PhD Thesis"`, laid out exactly like the candidate's MSc repository:
`main.tex` (report class, natbib author-year, glossaries), `References.bib`, `Thesis/Chapter N/src/chapterN_slug.tex` + `Thesis/Chapter N/Figures/`, `Thesis/{Cover Page,Declarations,Abstract,Acknowledgments,Acronym Definitions,List of Equations,Annexures}`, `Thesis/macros.tex`, `Code/`, `Research Proposal/`, `CHANGES_REVIEW.md` (loop log), `README.md` (overview, structure table, citation, keywords).
During round one, agents write in the working directory `"~/Desktop/PhD Thesis/Council" Workspace/thesis/`; `sync_from_workdir.sh` copies into the repository layout. From round two the repository is the working directory and the old path is retired. Commit messages are plain and describe the change; no tool attribution of any kind appears in git history.
Acronyms: define in `Thesis/Acronym Definitions/acronyms.tex` and use `\gls{}` on first use in each chapter, as the MSc did.

## Zero-hallucination citation rule (added 2026-09-09, binding)
- Every mathematical statement that is not proved in the thesis carries a citation with a LOCATOR: `\citep[Thm.~3.3.6]{karatzas1991}`, `\citep[p.~101]{yu1994}`. This includes results any statistician would call common knowledge (Itô's formula, DKW, Berbee's lemma, Girsanov, change of numéraire, Hagan's formula, the Beta law of order statistics).
- Every market fact, date, spread value, convention or regulatory statement carries a citation to a primary source in References.bib, or a `\datanote{}` saying it is unverified.
- Every definition adapted from the literature names its source. Every algorithm names the paper it follows.
- A writer who cannot find a source for a claim writes `\gap{Citation needed: ...}` rather than asserting it.
- Reference PDFs live in `References/PDF/<key>.pdf` (open-access copies only; paywalled items are recorded, never pirated). Highlighted copies live in `References/PDF/<key>.highlighted.pdf` and reading notes in `References/Highlights/<key>.md`, maintained by `thesis-reference-librarian`. Writers and reviewers consult the Highlights notes before citing, and cite the locator recorded there.
- `thesis-citation-enforcer` sweeps every chapter after the domain review and converts unsupported assertions into cited statements or `\gap{Citation needed}` boxes.

## Canonical chapter labels (added 2026-09-09)
ch:intro, ch:prelim, ch:certification, ch:sharpness, ch:identifiability, ch:usd, ch:zar, ch:conclusions, app:tenor, app:proofs, app:data. Each chapter file carries its canonical label immediately after \chapter; the file-name label (e.g. ch7-zar-coda) is kept for backward compatibility. Refer to chapters only by canonical labels.

## Single-source rule (added 2026-09-09, binding; supersedes any "readable alone" instruction)
- Every definition, assumption, lemma, proposition, theorem, proof, algorithm, market fact, dataset description and worked example has exactly ONE home chapter, recorded in `references/CONTENT-MAP.md`.
- Any other chapter that needs it writes at most one sentence of reminder and a reference: "By the time-change lemma (Lemma~\ref{lem:prelim-tc}), ...". No restated theorem environments, no re-proofs, no re-derivations, no repeated tables of market dates, no second description of a dataset.
- Chapter introductions may summarise what other chapters established in one or two sentences each, with references, and nothing more.
- Preliminaries (Chapter 2) is the home of all standard tools. Appendix B is the home only of standard proofs too long for Chapter 2 and NOT already proved there; a proof appears in exactly one of the two.
- Appendix C is the home of all data descriptions; Chapters 6 and 7 reference it and give only the analysis.
- Chapter 1 is the home of the transition record (dates, spreads, conventions); Chapters 5, 6, 7 reference it.
- Writers consult CONTENT-MAP.md before writing and add a row for every new object they create. Panels check every round for cross-chapter repetition ([CUT-REPETITION] items are must-priority). `thesis-redundancy-cutter` sweeps pairwise after each round.
