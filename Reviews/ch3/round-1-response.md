# Chapter 3 — Finite-Sample Certification of Hedging Error — round-1 response

Reviser: thesis-revision-writer, 2026-09-10. File revised: `/Users/thabangbaloyi/Desktop/PhD Thesis/Council Workspace/thesis/chapters/ch3-certification.tex`, in one atomic rewrite so that no passage was cut before its replacement was in place.

Counts: **37 DONE, 0 DECLINED, 0 DEFERRED.** Two items (4 and 34) are DONE in Chapter 3 and their moved text is staged in this folder because the reviser owns Chapter 3 only; see "Handoffs" below, which also lists the cross-chapter repairs the cuts force.

Read before revising: `references/STANDARD.md`, `LESSONS.md`, `GROUND-TRUTH.md`, `LOOP.md`, `CONTENT-MAP.md`; `13-mathematics-3yr.tex` status via GROUND-TRUTH corrections 1–16; `chapters/ch2-preliminaries.tex` in full for every label cited; `appendices/appB-proofs-standard.tex` section headings; `bibliography.tex` for every key used; the Highlights notes `adams2010`, `barber2023`, `barber2026`, `dedecker2017`, `halkiewicz2026`, `oliveira2024`, `ramos2026`, `schmitt2026`, `stocker2025`, `vovk2012`, `xu2025`, `yu1994`, `zheng2024`, `zwart2025`. Confirmed on disk: `hoeffding1963` and `massart1990` have **no** Highlights note, so no locator for either is quoted anywhere in the chapter.

---

## 1. The load-bearing coupling dependency (item 3) — answered first

**Chapter 2's Lemma `lem:prelim-yu` is insufficient, and the strengthened form has been kept in Chapter 3 as its own lemma.**

What `cor:coupled` needs, and what `lem:prelim-yu` does not give:

1. `\Dfit` must pass through the coupling unchanged, so that `\pi(\Dfit)` is the *same* random policy on both sides. `lem:prelim-yu` asserts only that the $X_j^*$ are independent with $X_j^*\overset d= X_j$; nothing in its statement forbids the first block from being resampled, and if it is, $\pi(\Dfit^*)\neq\pi(\Dfit)$ and the certified object is the hedging error of a policy the bank never fitted.
2. Each coupled block must be independent of the **actual** `\Dfit`, not merely of the other coupled copies. `lem:prelim-yu` states mutual independence of $X_1^*,\dots,X_m^*$ only. Without independence from the actual $\Dfit$, the sentence "conditionally on $\Dfit$ the variables $S^*_1,\dots,S^*_n$ are i.i.d.\ with law $P_\pi$" does not follow, and the whole of Theorem 6(ii) rests on it.

Resolution taken, which is the review's option (b). New **Lemma `lem:firstblock`, "Sequential coupling with the first block preserved; a strengthening of Lemma~\ref{lem:prelim-yu}"**, at the head of Section `sec:step1`. It states (a) $\xi^*_1=\xi_1$ with the right marginals, (b) $\xi^*_2,\dots,\xi^*_m$ mutually independent **and jointly independent of the original $\xi_1$**, (c) the cost $(m-1)\beta(b)$. Chapter 2 is cited for the base case in the theorem title and in the one sentence that follows the statement: "What Lemma~\ref{lem:prelim-yu} supplies is (c) together with mutual independence of copies having the right marginals; what is added here is (a), that the first block is not resampled, and the strengthening of (b) from independence among the copies to independence of the later copies from the original first block." The proof is eight lines from `lem:prelim-berbee`, `lem:prelim-inherit` and `def:prelim-mixing`, and cites Remark `rem:prelim-yu-original` of Chapter 2, which already records that the sequential-Berbee construction is available and delivers these properties. Every use of the old `lem:blocks` in the chapter (`cor:coupled`, the assembly proof, `rem:jointtv`, `rem:sequence`, Figure `fig:blocks`) now points at `lem:firstblock`.

**Item for Chapter 2 round 2.** Chapter 2's Lemma `lem:prelim-yu` *could* be strengthened instead, and should be: the alternative proof already written into Remark `rem:prelim-yu-original` ("coupling $X_j$ to a copy independent of $(X_1,\dots,X_{j-1})$") delivers both clauses free. The requested amendment is to add to the statement of `lem:prelim-yu`, and to its Appendix B proof in Section `appB:yu`, the clause: "moreover $X_1^*=X_1$, and for each $j$ the copy $X_j^*$ is independent of $(X_1,\dots,X_{j-1})$." If Chapter 2 adopts it, Chapter 3's `lem:firstblock` collapses to a one-sentence citation and about 300 words leave the chapter. Until then Chapter 3 is correct as it stands, and no proof in it rests on a statement that does not support it.

---

## 2. Item-by-item

### Substantive mathematics, honesty and structure

**1. [ADD] must — two-sided counterpart. DONE.** New **Proposition `prop:twosided`** in Section `sec:cert-theorem`, immediately after Theorem `thm:cov` and before Remark `rem:betaapprox`, with parts (a) marginal over-coverage $1-\alpha+1/(n+1)+\dK+(n+1)\beta(b)$, (b) conditional over-coverage $b_{n,k}(1-\delta)+\dK+\beta(b)/\delta'$, (c) the two-sided calibration-conditional coverage error, all proved in about three-quarters of a page from the coupling event, Theorem `thm:prelim-beta` run in the other direction, and Lemma `lem:halfline` with $P$ and $Q$ exchanged. New **Remark `rem:twosided`** says in two sentences why it is needed (Theorem `thm:cov` alone is satisfied by $\hat q=+\infty$) and cites `\citep[Thm.~3]{barber2023}` as the over-coverage precedent and `\citep[Thm.~2]{halkiewicz2026}` as the precedent for the two-sided error as a minimax object. `\citep[Thm.~1]{ramos2026}` is cited for the upper half of the exchangeable rank bound. The Discussion's "Connection to Chapter~\ref{ch:sharpness}" now names `prop:twosided`(c) as the object Chapter 4 minimises and says why the one-sided deficit is degenerate.

One hypothesis was added to the review's text: **the proposition assumes $F_P$ continuous**, and says so in the statement and in the proof of (b). The reason is mathematical, not editorial: with atoms Theorem `thm:prelim-beta` gives stochastic domination in one direction only, so $\E F_P(\hat q^*)$ can exceed $k/(n+1)$ by the mass of an atom at $\hat q$ and no upper bound survives; the proof says exactly this where continuity is used. The review anticipated the point for (b) and asked that it be said; it is said for both (a) and (b). A lesson is recorded below.

**2. [FIX] must — Assumption `ass:mix` on the state process; delete the `\gap{}` box. DONE.** Assumption `ass:mix` now reads on $(X_t)$ of Section `sec:cert-policy` "which generates both the fitting sample and the per-period hedging errors", in the sense of Definition `def:prelim-mixing` of Chapter 2, with the common-law and pairwise-separation clauses. The "Reading of the assumption" paragraph is kept as the mathematical explanation of why $(e_t(\pi))_t$ does not inherit the coefficients, with every trace of what was "kept verbatim" removed. The whole `\gap{}` box is deleted: item (1) leaves with the Berbee proof (item 19), item (2) is closed by the rewrite, item (3) is closed by Remark `rem:betaapprox`.

**3. [FIX] must — `cor:coupled` against `lem:prelim-yu`. DONE.** See section 1 above.

**4. [REMOVE] must — Section 3.8 to Chapter 6. DONE.** Section `sec:cert-backtests` and its four subsections are gone from Chapter 3; the label no longer exists and the two remaining references to it (in `sec:cert-isnot` and in `rem:sequence`) now point at Chapter~\ref{ch:usd}. One paragraph is retained in the Discussion, "The certificate against the alternatives", with exactly the content the review specified: proved finite-sample level against asymptotic level, Edgeworth coefficients depending on unavailable constants, no theorem claimed, the empirical comparison is Chapter 6's. The moved text is staged verbatim at `reviews/ch3/round-1-moved-to-ch6.tex`, under `\section{Methods compared}` with a `\gap{}` recording that it is placed and not integrated; the two drafting-narration sentences of item 7(e) were stripped on the way and their honesty content preserved. It is staged rather than written into `chapters/ch6-usd-validation.tex` because this reviser owns Chapter 3 only.

**5. [FIX] must — the `zheng2024` sentence. DONE.** The panel's direct edit is carried forward verbatim into the rewritten Chapter notes and reads with the surrounding sentences; `\cite[Prop.~5.1]` and `\cite[Thm.~5.1]` are converted to `\citep` for consistency with the citation rule. The correction is flagged below for Chapters 1 and 4, which are stubs and cannot yet repeat the claim.

**6. [CITE] must — Proposition `prop:w1` attribution. DONE.** A sentence follows the statement: "The one-sided inequality is `\citep[Prop.~1, p.~4]{xu2025}`, attributed there to `\citet{ross2011}`; what is proved here is the specialisation to the certificate together with the two-sided refinement $\dK\le\sqrt{L\Wone}$ under a density bound on both laws, the $\Winf$ bound, and the sharpness of the constant." Remark `rem:counter` no longer claims the inequality. The Chapter-notes list of additions now reads "the two-sided refinement and the sharpness of the constant in Proposition~\ref{prop:w1}", and the Discussion paragraph on the drift bound repeats the attribution.

**7. [REMOVE] must — six passages narrating the writing process. DONE.** (a) Remark `rem:betaapprox` rewritten without the sentence about the source of record. (b) the `\gap{}` box deleted entire. (c) Remark `rem:counter` now opens "The obvious linear bound $|F_P(x)-F_Q(x)|\le L\Wone(P,Q)$ is false." (d) the $n^{-1/4}$ paragraph now closes "A linear bound, were one available, would give $n^{-1/2}$; Remark~\ref{rem:counter} shows it is not." (e) left the chapter with item 4 and was stripped from the staged copy too. (f) the Table `tab:example` datanote rewritten (item 14); the recomputation log, the "must not be corrected into one another" clause and the "before submission" clause are gone. A grep of the revised file for *first draft*, *ground truth*, *council*, *lessons*, *round*, *source of record*, *before submission*, *kept verbatim* returns nothing.

**8. [FIX] must — three false self-descriptions and three self-justifying sentences. DONE.** Abstract now reads "The proof is written in full from three tools established in Chapter~\ref{ch:prelim}: Berbee's coupling applied sequentially, the Beta law of conformal coverage in the form that allows atoms, and a half-line comparison of two laws." The map of the chapter no longer says "restating every borrowed lemma". The sentence before Section `sec:step1` now reads "Each borrowed result is used with a reference to its statement in Chapter~\ref{ch:prelim}." All three self-justifying sentences ("because the whole certificate rests on it", "because the conditional form of the certificate rests on it", "because the example needs the smallest number the route gives") are deleted with the environments they defended.

**9. [FIX] must — the DKW contradiction. DONE.** The paragraph in Section `sec:step2` now reads "The uniform DKW inequality is not used in the proof of Theorem~\ref{thm:cov}; it is used only in Section~\ref{sec:cert-estimable}, to bound a functional of the calibration law." The two uses in Section `sec:cert-estimable` are kept and one of them now carries the cross-reference to Theorem `thm:prelim-dkw` of Chapter 2.

**10. [FIX] must — non-estimability wording and `adams2010`. DONE.** (a) The paragraph after `prop:noest` is rewritten to the review's text: `\citet[Thm.~1]{adams2010}` for the positive Glivenko–Cantelli theorem, the quoted clause "can be arbitrarily slow and we cannot hope to obtain distribution-free probability bounds" at `\citep[Sec.~1.1]{adams2010}`, and what `prop:noest` adds. (b) The qualifier **distribution-free** is inserted in the subsection title ("The mixing coefficient is not estimable distribution-free"), in the abstract ("is not estimable distribution-free from any finite record"), in Section `sec:cert-isnot`, and in the Limitations paragraph. The proposition's own title now reads "Non-estimability of $\beta(b)$ over all stationary processes with a given marginal". (c) The sentence "Under further assumptions on the process the coefficient can be estimated; the proposition rules out only a bound that holds over all stationary processes with the observed $N$-marginal" is inserted immediately after the proof. McDonald, Shalizi and Schervish are **not** cited, per the review.

**11. [FIX] must — the exact minimiser. DONE.** Both places now carry $b^*=(2(r+1))^{2/(2r+3)}N^{3/(2r+3)}$: the paragraph after Algorithm `alg:cert` and the "Connection to Chapter~\ref{ch:sharpness}" paragraph, the latter with the numeric anchor "which is $23.93$ at $N=500$, $r=2$, against the bare balance value $14.35$" (recomputed here: $6^{2/7}=1.66843$, $500^{3/7}=14.3453$, product $23.934$). "Calibration-conditional deficit" is replaced by "expected calibration-conditional shortfall" in both places.

**12. [CITE] must — `halkiewicz2026`. DONE.** The paragraph the review drafted is added to the Chapter notes with `\citet[Thm.~4]{halkiewicz2026}` and `\citep[Sect.~3.4, eq.~(6)]{halkiewicz2026}`, ending "The certificate's drift term is an assumption rather than a class, and the lower bound of Chapter~\ref{ch:sharpness} is mixing-driven; neither result implies the other." `\citep[Thm.~2]{halkiewicz2026}` also appears in Remark `rem:twosided`.

**13. [CITE] must — Beta-law and quantile locators; no locator for `hoeffding1963` or `massart1990`. DONE.** Section `sec:step2` opens with "the Beta form of `\citep[Prop.~2b, p.~479]{vovk2012}`, stated there in the generality that allows atoms, and written as $\Beta(k,n+1-k)$ in the notation used here in `\citep[eq.~(4), p.~2]{zwart2025}`" — the word "Beta" is attributed to the form, never to Vovk. Theorem `thm:cov`(ii) carries "(Corollary~\ref{cor:prelim-beta-bound} of Chapter~\ref{ch:prelim}; `\citep[Prop.~2a, p.~478]{vovk2012}`)", and the paragraph "The explicit bound on the quantile" says the bound "is prior art and not something derived here". The `\cite{dkw1956}`/`\cite{massart1990}` pair is replaced by a cross-reference to Theorem `thm:prelim-dkw` alone, and the `[Thm.~2]{hoeffding1963}` locator is gone with Lemma `lem:hoeffding`. Per the orchestrator's standing instruction, a `\gap{Citation locator needed: ...}` box now records that both keys are cited in this thesis only through Chapter 2's statements, with no page or theorem number, no verified locator having been recorded.

**14. [FIX] must — the Table `tab:example` datanote. DONE.** Replaced by the review's text: the first inequality of Proposition `prop:prelim-ar1` giving $4.883\times10^{-4}$, the $k$-uniform third inequality giving $5.638\times10^{-4}$ as the class constant, the variance convention "the AR(1) is normalised to stationary variance $v=1$, so the innovation standard deviation is $\sqrt{1-\varphi^2}$", the two Beta-quantile roots, and "The certificate code of Appendix~\ref{app:data} regenerates every cell of this table." The stale $0.8853/0.8126/0.9359$ sentence and the "to be extended before submission" clause are gone. The $v_5$ and $v_{20}$ arithmetic travels with the swept columns to Chapter 4 (item 34).

**15. [CITE] must + [ADD] — the dependent deployment side. DONE.** The paragraph "The deployment side is dependent" now carries `\citep[Prop.~3.2, eqs.~(3.7)--(3.8)]{dedecker2017}`, `\citep[Remark~3.4(1)]{dedecker2017}` and `\citep[Remark~3.4(2), eq.~(3.12)]{dedecker2017}`, names Rio's weak $\alpha$-dependence through half-line indicators as the class containing $\beta$-mixing, and says the constant must be assembled from the quantile integrals, finite for bounded scores. The closing prose sentence is replaced by the review's `\gap{}`, stating the missing inequality in mathematical terms and nothing else.

### Repetition: results whose home is Chapter 2 or Appendix B

All thirteen cuts are made. A grep of the revised file for `def:beta`, `lem:disint`, `lem:berbee`, `lem:blocks`, `lem:beta`, `lem:hoeffding`, `cor:dkw`, `def:wass`, `lem:w1area`, `lem:winf`, `lem:bl`, `lem:markovbeta`, `lem:ar1` returns zero occurrences of each. Every replacement is the single sentence the review specified, at the point of use.

**16. [CUT-REPETITION] must — Definition `def:beta` and the two paragraphs after it. DONE.** Replaced by one sentence at the head of the new subsection "Mixing, and the distance the certificate pays": "Throughout, $\beta(k)$ is the non-stationary $\beta$-mixing coefficient of Definition~\ref{def:prelim-mixing} of Chapter~\ref{ch:prelim}, and the block scores of a fixed policy inherit the coefficients of the state process by Lemma~\ref{lem:prelim-inherit}."

**17. [CUT-REPETITION] must — Lemma `lem:disint` with its proof, and the "Two equivalent forms" paragraph. DONE.** Both deleted. The reminder sits at the point of use, in the deployment side of the assembly proof: "The coefficient is the expected conditional total-variation discrepancy (Lemma~\ref{lem:prelim-beta-tv} of Chapter~\ref{ch:prelim})". Remark `rem:jointtv` also re-points to `lem:prelim-beta-tv`.

**18. [CUT-REPETITION] must — the "Total variation and Kolmogorov distance" remark. DONE.** Replaced by one sentence citing Definition `def:prelim-dK-dTV` and Proposition `prop:prelim-dK-le-dTV`, retaining Chapter 3's own clause: "the certificate evaluates the deployment law only on half-lines, which is why the drift penalty is $\dK$ and not $\dTV$."

**19. [CUT-REPETITION] must — Lemma `lem:berbee`, its 599-word proof and its two framing paragraphs. DONE.** All deleted, attribution included. Section `sec:step1` now opens "Step 1 applies Berbee's coupling lemma (Lemma~\ref{lem:prelim-berbee} of Chapter~\ref{ch:prelim}) once per block, in time order." The one remaining use, in the proof of `prop:noest`, is re-pointed to `lem:prelim-berbee`(iii).

**20. [CUT-REPETITION] must — Lemma `lem:blocks` with its proof and the Yu preamble. DONE, subject to item 3.** Deleted and replaced by `lem:firstblock`, which is strictly the two clauses Chapter 2 does not supply plus the cost, and no more. Corollary `cor:coupled` is kept and now carries the absorbed-endpoint gap verification in two lines inside its own proof, as the review required: $s_{i+1}=t_i+b$ exactly, and $\beta(\sigma(\xi_{1:i-1}),\sigma(\xi_i))\le\beta(X_{1:t_{i-1}},X_{t_{i-1}+b:\infty})\le\beta(b)$. The "coupling form implies Yu's expectation bound" sentence is deleted, Remark `rem:prelim-yu-original` carrying it.

**21. [CUT-REPETITION] must — Lemma `lem:beta`, its 534-word proof and its preamble. DONE.** Deleted. Replaced by the review's one sentence at the head of Section `sec:step2`. Corollary `cor:exact` is kept and its proof now invokes Theorem `thm:prelim-beta` directly.

**22. [CUT-REPETITION] must — Lemma `lem:hoeffding` with its proof. DONE.** Deleted; Chapter 2's `lem:prelim-hoeffding` is the home and is reached through Corollary `cor:prelim-beta-bound`.

**23. [CUT-REPETITION] must — Corollary `cor:dkw` with its proof and the "DKW form as a corollary" paragraph. DONE.** Deleted. Theorem `thm:cov`(ii) keeps the inequality with the Chapter 2 cross-reference and the `vovk2012` locator. The "Gaussian-tail approximation" paragraph is folded into Remark `rem:betaapprox` at two sentences; the $n=25$ numbers stay where they belong, in the worked example.

**24. [CUT-REPETITION] must — Definition `def:wass`. DONE.** Deleted; one clause at the head of Section `sec:cert-drift` cites Definition `def:prelim-W`.

**25. [CUT-REPETITION] must — Lemma `lem:w1area` with its proof. DONE.** Deleted; the proof of `prop:w1` now says "By the area identity of Theorem~\ref{thm:prelim-w1-identity} of Chapter~\ref{ch:prelim}".

**26. [CUT-REPETITION] must — Lemma `lem:winf` with its proof. DONE.** Deleted. The $\Winf$ paragraph of the proof of `prop:w1` is one line: "By Proposition~\ref{prop:prelim-winf-shift} of Chapter~\ref{ch:prelim}, $F_P(x)\le F_Q(x+\Winf(P,Q))$, and the Lipschitz property of $F_Q$ gives $F_Q(x+\Winf)\le F_Q(x)+L\,\Winf(P,Q)$." The quantile identity is not asked of Chapter 2.

**27. [CUT-REPETITION] must — Lemma `lem:bl` with its proof and the $(2+\epsilon)$-moment paragraph. DONE.** Deleted and compressed into one sentence in Section `sec:cert-drift`: "On the coupling event the calibration scores are i.i.d.\ $P$ given $\pi$, so $\E[\Wone(P_n,P)\mid\Dfit]\le J_1(P)/\sqrt n$ by Theorem~\ref{thm:prelim-bobkov} of Chapter~\ref{ch:prelim}, with $J_1(P)$ finite under a finite $(2+\epsilon)$-th moment." Corollary `cor:plugin` is kept and its proof cites `thm:prelim-bobkov`.

**28. [CUT-REPETITION] must — Section 3.7.1 in its entirety. DONE.** Lemma `lem:markovbeta`, Lemma `lem:ar1` and both proofs are deleted, and the stale sentence about Chapter 2's side condition goes with them. Replaced by the review's two sentences at the head of Section `sec:cert-example`, including the variance convention and $\beta(10)\le2^{-11}=4.883\times10^{-4}$ from Proposition `prop:prelim-ar1`.

### Positioning, citation and clarity

**29. [ADD] should — three positioning sentences. DONE.** All three are in the Chapter notes. (a) `\citet[p.~2]{oliveira2024}` with both quoted clauses and `\citep[Prop.~10, pp.~20--21]{oliveira2024}` for the blocking living inside their proof, against "the certificate here blocks the scores themselves, which is what makes the calibration-conditional statement available". (b) their feasible set $\delta_{\mathrm{cal}}>4(m-1)\beta(a)+\beta(r)$ at `\citep[eq.~(12), p.~7]{oliveira2024}` against $(n+1)\beta(b)$, with the factor explained by the $2M(m-1)\beta(a)$ constant of their Proposition 10 at $M=1$ and by the two-fold count for odd and even blocks at `\citep[Lemma~4.2, p.~103]{yu1994}` (locator verified in the `yu1994` Highlights note, which records exactly this reading), and the separate train–calibration charge $\beta(r)$. (c) "Their results are all marginal: the paper contains no calibration-conditional statement, and their discussion leaves open 'whether split conformal is optimal for this class of problems' `\citep[Sec.~4]{barber2026}`, which is the question Chapter~\ref{ch:sharpness} takes up." The Introduction carries a short form of (c) as well.

**30. [FIX] should — the right corollary of `barber2026`. DONE.** Both places now cite `\citep[Cor.~2]{barber2026}` for the $2\beta(\tau)+2\beta(\tau^*)$ form and name Corollary 1 separately as the pretrained-score case at cost $2\beta(\tau)$. `\citep[Thm.~2]{barber2026}` is kept for tightness with the qualification that it is a construction for split conformal, not a minimax bound over procedures.

**31. [FIX] should — the upper bound in `prop:noest`(c). DONE.** The step is replaced by the explicit coupling the review asked for: a second copy started from an independent draw of the invariant law on $\{0,1\}^N$ and driven by the *same* $(\xi_t,\zeta_t)$ for $t>N$; agreement from time $t+k$ off the event that some coordinate lineage went $\lfloor k/N\rfloor$ consecutive steps without a refresh, of probability at most $N(1-\epsilon)^{\lfloor k/N\rfloor}$; then $\dTV\le\Prob(\text{disagreement})$ in the form of `lem:prelim-berbee`(iii). The "Lemma~\ref{lem:berbee} in reverse" phrase is gone.

**32. [CLARIFY] should — merge the two events in `thm:cov`(ii). DONE.** The statement now reads "with probability at least $1-\delta-\delta'-n\beta(b)$ over $(\Dfit,S_{1:n})$" with a single conclusion; the trailing clause "the last term holding on an event of probability at least $1-\delta'$" is deleted. A short paragraph after the theorem records why both events are $\sigma(\Dfit,S_{1:n})$-measurable, and the assembly step intersects $A'$ and $E'$ explicitly. The worked example now reports the single confidence $1-0.05-0.05-0.0122=0.8878$ where the "joint event" figure used to appear unexplained.

**33. [CLARIFY] should — the indexing on the deployment side. DONE.** The parenthetical is replaced by the review's sentence, word for word with `cor:coupled`: "with the left endpoint absorbed, $X_{H_0}$ begins at index $N_0+b+N\ge t+b$, so $X_{H_0}$ is a function of $X_{t+b:\infty}$ and the coefficient is $\beta(b)$."

**34. [REMOVE] should — the block-length sweep to Chapter 4. DONE.** Table `tab:example` is reduced to the single $b=10$ certificate (and gains the two new two-sided rows). The "Reading the table" paragraph, the $\varphi=0.8$ discussion, Figure `fig:example` and its datanote leave the chapter. What stays, as the review directed: the $b=10$ column, the drift-slack computation, the exact-versus-approximate quantile comparison, and one closing paragraph, "The block length is the design variable", which states that a geometrically $\beta$-mixing process lies in every class $\Bclass{r}$ so no sweep on it can locate $b^*$. The moved text is staged at `reviews/ch3/round-1-moved-to-ch4.tex` as Table `tab:example-sweep` and Figure `fig:example-sweep`, with the AR(1) references already re-pointed to `prop:prelim-ar1` and the variance convention added.

**35. [CITE] should — `stocker2025` and `schmitt2026`. DONE.** Both sentences are in the Chapter notes with the locators the review supplied: `\citep[§3, p.~7]`, `\citep[§3.4, p.~13]`, `\citep[p.~15]{stocker2025}`; `\citet[Thm.~1, p.~3]{schmitt2026}` and `\citep[p.~3]{schmitt2026}`.

**36. [CLARIFY] should — the Beta quantile is defined in Chapter 2. DONE.** The local definition is replaced by "Throughout, $b_{n,k}(\delta)$ is the Beta quantile of \eqref{eq:prelim-beta-quantile} of Chapter~\ref{ch:prelim}."

**37. [ADD] should — where atoms bite. DONE.** Added as the closing sentences of Remark `rem:scoremap`: the choice of $\phi$ decides whether the score law has atoms; the synthetic example is continuous so its quantiles are exact, while a real record of profit and loss rounded to the currency unit has atoms and the same numbers become lower bounds by the domination of Theorem `thm:prelim-beta`.

---

## 3. New `\gap{}` boxes

The chapter had one `\gap{}` box. It is deleted (item 2). Two new boxes replace it, both stating only what remains to be established, in mathematical or bibliographic terms:

1. Section `sec:step2`, after "The explicit bound on the quantile": `\gap{Citation locator needed: \cite{hoeffding1963} and \cite{massart1990} ... are cited in this thesis only through Lemma~\ref{lem:prelim-hoeffding} and Theorem~\ref{thm:prelim-dkw} of Chapter~\ref{ch:prelim}, with no page or theorem number, no verified locator for either having been recorded.}`
2. Section `sec:cert-drift`, after "The deployment side is dependent": `\gap{Not established here: a bound $\E\Wone(Q_m,Q)\le c_r m^{-1/2}$ for the empirical law of $m$ overlapping deployment blocks of a process in $\Bclass{r}$, with $c_r$ explicit in $(C,r)$ and in the quantile function of the score law. Chapter~\ref{ch:sharpness} supplies it by specialising \citep[Remark~3.4(2), eq.~(3.12)]{dedecker2017}; until then Corollary~\ref{cor:plugin} certifies the calibration side only.}`

A third `\gap{}` is in the staged Chapter 6 file, recording that the moved section is placed and not integrated.

## 4. Word count and pages

| | before | after |
|---|---|---|
| `wc -w` on `ch3-certification.tex` | 13,461 | **11,300** |
| typeset pages (`main.pdf`, ch3 start to ch4 start) | 51 | **34** |
| `proof` environments | 18 | 9 |
| numbered environments, excluding remarks | 23 | 12 |
| remarks | 8 | 8 |
| `\gap{}` boxes | 1 | 2 |
| `\datanote{}` boxes | 4 | 3 |
| `figplan` | 3 | 2 |

Net of the 3,730 words of repetition, the 1,740 of Section 3.8 and the 450 of the sweep, the chapter took on about 1,760 words of new content: Proposition `prop:twosided` with its proof and Remark `rem:twosided`, Lemma `lem:firstblock` with its proof, the `dedecker2017` paragraph and its `\gap{}`, the three Oliveira/Barber positioning sentences, the `halkiewicz2026` paragraph, the `stocker2025` and `schmitt2026` sentences, the two-sided worked-example computation, and the atom sentence in `rem:scoremap`. At 34 typeset pages the chapter is ten under its budget of 44; that headroom is deliberate and belongs to Chapter 4, which receives the sweep.

The document compiles (`tectonic main.tex`, exit 0, `main.pdf` written). Every `\ref` in Chapter 3 resolves; the ten remaining undefined references in the build are all in Appendix C and are listed next.

## 5. Handoffs the cuts force (not owned by this reviser)

**Appendix C, `appendices/appC-code.tex` and `appendices/appC-data-code.tex`.** Ten references now dangle because their targets left Chapter 3. Repairs:

| dangling `\ref` | replace with |
|---|---|
| `lem:blocks` (appC-code line 31) | `lem:firstblock` of Chapter 3, or `lem:prelim-yu` of Chapter 2 for the bare $(n+1)\beta(b)$ cost |
| `cor:dkw` (appC-code line 31) | `cor:prelim-beta-bound` of Chapter 2 |
| `lem:w1area` (appC-code line 34) | `thm:prelim-w1-identity` of Chapter 2 |
| `lem:ar1` (appC-code lines 43, 48) | `prop:prelim-ar1` of Chapter 2 (first inequality) |
| `fig:example` (appC-code lines 25, 46, 48; appC-data-code lines 47, 54) | `fig:example-sweep`, once Chapter 4 absorbs the staged file |

Also in `appC-code`: `test_table_3_1` is described as reproducing Table 3.1 "at $b\in\{5,10,20\}$". Table `tab:example` is now the single $b=10$ certificate plus the two-sided rows; the three-column set is Chapter 4's `tab:example-sweep`. The datanote at line 48 should be split accordingly, and the two new cells the code must also regenerate are $b_{25,24}(0.95)=0.9856$ and the two-sided bound $0.1345$ at confidence $0.8378$.

**Chapter 2, round 2.** Strengthen Lemma `lem:prelim-yu` and its Appendix B proof (Section `appB:yu`) with "moreover $X_1^*=X_1$, and for each $j$ the copy $X_j^*$ is independent of $(X_1,\dots,X_{j-1})$"; see section 1 above.

**Chapter 6.** Paste `reviews/ch3/round-1-moved-to-ch6.tex` into `chapters/ch6-usd-validation.tex` and delete the staged file. `bcbs2019` moves with it and still has no Highlights note; the Basel zone boundaries retain their `\datanote{}` saying they are unverified.

**Chapter 4.** Paste `reviews/ch3/round-1-moved-to-ch4.tex` into `chapters/ch4-sharpness-blocking.tex` and delete the staged file. Chapter 4 must also (i) use `prop:twosided`(c) as the object it minimises, (ii) quote $b^*=(2(r+1))^{2/(2r+3)}N^{3/(2r+3)}$, never the bare balance, and (iii) carry the `zheng2024` correction of item 5.

**CONTENT-MAP.md** (not edited here, to avoid a concurrent write). Rows to delete: `def:beta`, `lem:disint`, `lem:berbee`, `lem:blocks`, `lem:beta`, `lem:hoeffding`, `cor:dkw`, `def:wass`, `lem:w1area`, `lem:winf`, `lem:bl`, `lem:markovbeta`, `lem:ar1`, `sec:cert-backtests`. Rows to add, home Chapter 3 (`ch:certification`): `prop:twosided` (proposition, Two-sided companion), `rem:twosided` (remark, Why the two-sided form is needed), `lem:firstblock` (lemma, Sequential coupling with the first block preserved). Rows to add, home Chapter 6: `sec:usd-methods`. Rows to add, home Chapter 4: `tab:example-sweep`, `fig:example-sweep`.

---

## thesis-revision-writer: ch3 round 1 2026-09-10

- `[2026-09-10][revision-writer][ch2,ch3,ch4]` LESSON: before deleting a chapter's local version of a shared lemma, check the *conclusions* the local version supplies against the home statement clause by clause, not the names of the two lemmas. WHY: Chapter 2's `lem:prelim-yu` and Chapter 3's `lem:blocks` are both "sequential coupling", but only the second preserves the first block and gives independence from the *actual* predecessors, and Corollary `cor:coupled` needs both; deleting on the strength of the title would have left Theorem 6(ii) resting on a statement that does not support it. APPLIES TO: every `[CUT-REPETITION]` item in every chapter.
- `[2026-09-10][revision-writer][ch3,ch4]` LESSON: an over-coverage bound needs continuity of the calibration distribution function, where the matching under-coverage bound does not. WHY: Theorem `thm:prelim-beta` gives stochastic domination in one direction only, so with an atom at the threshold $\E F_P(\hat q)$ can exceed $k/(n+1)$ by the mass of the atom and no upper bound survives; Proposition `prop:twosided` therefore carries the hypothesis and says where it is used. APPLIES TO: ch3, ch4 (the minimax object of Theorem 9 inherits the hypothesis).
- `[2026-09-10][revision-writer][all]` LESSON: when a chapter is not the owner of the destination file, cut and stage in the same operation, and name the destination and the pasting agent in the staged file's header. WHY: "move section X to chapter Y" across an ownership boundary is the one edit that can lose content outright; a staged `.tex` beside the review report leaves nothing unplaced and nothing silently overwritten. APPLIES TO: every `[REMOVE]` item that names another chapter.
- `[2026-09-10][revision-writer][all]` LESSON: after a repetition sweep, grep the *whole* thesis for the deleted labels, not just the edited chapter. WHY: Appendix C referenced five of Chapter 3's thirteen deleted objects and now carries ten undefined references; the reviser who makes the cut is the one who knows the replacement label for each. APPLIES TO: every chapter subject to `thesis-redundancy-cutter`.
- `[2026-09-10][revision-writer][ch3]` LESSON: a `\gap{Citation locator needed: ...}` is the right response to a key with no Highlights note even when the chapter has stopped citing that key directly. WHY: `hoeffding1963` and `massart1990` are reached only through Chapter 2 now, but the thesis still rests on them, and the box records that the locator gap is known rather than letting it disappear with the cross-reference. APPLIES TO: any chapter that routes a citation through another chapter's statement.
