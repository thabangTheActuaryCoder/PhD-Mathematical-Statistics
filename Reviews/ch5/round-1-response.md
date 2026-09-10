# Chapter 5, Identifiability of the Successor-Rate Smile — round 1 response

Revision writer: thesis-revision-writer, 2026-09-10. Chapter edited in place: `thesis/chapters/ch5-identifiability.tex`.
Verdict addressed: MAJOR, 23 numbered items (16 must, 7 should).
Counts: **DONE 21, DECLINED 0, DEFERRED 2** (item 23 split: the money figure is DONE, the two plots are DEFERRED).
Word count before 10,283; after **13,574** (+3,291, +32%). Every item but two was an addition; the only deletions are the two required by the single-source and invisible-apparatus rules.

Lessons applied at the start of this run: GROUND-TRUTH corrections 1, 17 and 18; the 2026-09-10 writer-ch5 lessons on the exact half-width, the Schur ellipse and the wrong-sign caveat; every 2026-09-10 review-panel lesson; STANDARD's single-source, invisible-apparatus and zero-hallucination rules.

---

## 1. [PROVE] must — the intermediate case of Theorem 4(i)

**DONE.** Proof of Theorem~\ref{thm:ident-two}(i), new display \eqref{eq:ident-homotopy}. The invalid two sentences (a "self-consistent solution … linear in $\rho_{B\alpha}$" plus convexity of the admissible region) are deleted and replaced by the explicit one-parameter family, adopted from the report and independently rederived here:
$\rho_{BF}=p$, $\theta(p)=\sqrt{a^2-\eta^2(1-p^2)}$, $\alpha_0(p)=\theta(p)-p\eta$, $\rho(p)=ra/\theta(p)$, $\rho_{B\alpha}(p)=p\rho(p)$, $\nu(p)=na^2/(\alpha_0(p)\theta(p))$, $p\in[-1,1]$.
Four verifications are given in full: it solves \eqref{eq:ident-inverse} by construction, since $\rho_{B\alpha}=p\rho$ turns the last equation of \eqref{eq:ident-inverse} into $\rho\theta(p)=ra$, so no fixed point has to be argued for; admissibility, since the left side of \eqref{eq:ident-admiss} is $p^2(1-\rho^2)\le1-\rho^2$ with equality iff $p^2=1$; $|\rho(p)|\le|r|a/\sqrt{a^2-\eta^2}<1$ under the new side condition; and the sweep, from the strict monotonicity of $\alpha_0$ already proved in Proposition~\ref{prop:ident-inverse}. The paragraph also states explicitly why the convexity argument cannot be repaired: $\rho$ is a coefficient of the quadratic form in \eqref{eq:ident-admiss} and varies along the family. The theorem is **not** restricted to the endpoints and no gap-box item was needed.

Two changes to the report's version were required and are corrections, not declines:

- The report's clause "(a) … so the basis is driven by $W$ alone" is not right for intermediate $p$. In the Cholesky factor of Lemma~\ref{lem:ident-psd}(ii), $\rho_{B\alpha}=\rho\rho_{BF}$ gives $c_2=0$ but leaves $c_3=\sqrt{1-p^2}$; the basis loads on $W$ with weight $p$ and on a component independent of both drivers with weight $\sqrt{1-p^2}$, and carries no loading on the part of $Z$ orthogonal to $W$. The chapter states it that way. Only at $p=\pm1$ is the basis driven by $W$ alone.
- The side condition is added to the hypotheses of Theorem~\ref{thm:ident-two}, as the report asked: "let $\eta>0$ satisfy $a>\eta\sqrt2$ **and $|r|<\sqrt{1-\eta^2/a^2}$**". It binds only for intermediate $p$; at $p=\pm1$ we have $\rho=r$ and $|r|<1$ suffices. It is satisfied at the worked parameters ($|r|=0.2329$ against $0.9567$).

The two bonuses are stated, one sentence each: the family returns $\mathcal M_\pm$ at $p=\pm1$ with $\rho=r$, and at $p=0$ it returns the Step 3 model of an analyst who sets both basis correlations to zero, so the segment is a homotopy from one extreme through the desk's implicit convention to the other.

## 2. [FIX] must — the quoted half-width

**DONE**, in three places, and the theorem now proves a closed form rather than quoting an approximation.

Theorem~\ref{thm:ident-two}(i) is restated for the **diffusion coefficient at the clock**: that is what is identified within exactly $[a-\eta,a+\eta]$. The quoted half-width is given exactly, as the new display \eqref{eq:ident-quotedhw},
$$\tfrac12(\Sigma^--\Sigma^+)=\eta q\Big[1-\frac{(2-3r^2)n^2\tau^*}{24}\cdot\frac{a^2}{a^2-\eta^2}\Big]=\eta qc^*\Big[1-\frac{(2-3r^2)n^2\tau^*}{12}+O\big(\nu^2\tau^*(\varepsilon^2+\nu^2\tau^*)\big)\Big],$$
with $\Sigma^\pm=\alpha_0^\pm c^{*\pm}q$, and derived at the end of the proof of part (i) from $\alpha_0^\pm c^{*\pm}=\alpha_0^\pm+(2-3r^2)n^2a^2\tau^*/(24\alpha_0^\pm)$ and $\tfrac12(1/(a-\eta)-1/(a+\eta))=\eta/(a^2-\eta^2)$. Evaluated at the worked parameters the closed form returns **18.428980** bp, which is the chapter's own Step 4 number to six figures.

One correction to the report's diagnosis, stated here so the panel can check it. The report calls the discrepancy a relative $O(\varepsilon^2\nu^2\tau^*)$ term. It is not: the leading relative correction is $-\tfrac1{12}(2-3r^2)n^2\tau^*=-1.868\%$, which is $O(\nu^2\tau^*)$ and **does not vanish as $\eta\to0$**, because the second term of $\alpha_0^\pm c^{*\pm}$ is decreasing in $\alpha_0^\pm$ and offsets part of the spread of the first. The $\varepsilon^2$ piece is only the further $-0.087\%$. Total $-1.94\%$, matching $18.4290$ against $18.7929$. The chapter states the mechanism in one sentence.

Section~\ref{sec:ident-example} Step 4 now prints both brackets ($c^{*+}=1.018587$, $c^{*-}=1.005603$), the exact half-width $18.4290$ bp, the naive $\eta qc^*=18.7929$ bp and the $1.94\%$ overstatement, and repeats that the exact statement is $[48.70,88.70]$ bp for $\alpha_0$ at the clock.

Criterion V1 now uses the exact endpoints, each extreme model carried through its own bracket,
$\Sigma^\pm=(a\mp\hat\eta)q[1+\tfrac1{24}(2-3r^2)(na/(a\mp\hat\eta))^2\tau^*]$,
and says in the same sentence that the symmetric interval $\Phi_0(F_0)\pm\hat\eta qc^*$ is about two per cent wider, so the two per cent of conservatism is removed from the primary criterion.

## 3. [CLARIFY] must — define "exact" once

**DONE.** A new paragraph between the statement and the proof of Theorem~\ref{thm:ident-two} separates the three senses (exact in $\varepsilon$; exact as a pathwise model identity; exact as a match), and gives the report's displayed convention verbatim in a quote block, with the addition that the three matched quantities are the cumulant functionals $\kappa_2(L_T)$, $\kappa_3(L_T)$ and $\Var\langle L\rangle_T$ and **not observables**, the observables being the caplet prices.

The good news is stated immediately after and proved in two lines: $\nu^\pm=na/\alpha_0^\pm$ makes $\alpha_0^\pm\nu^\pm=na$ the same for $\mathcal M_\pm$, so the leading neglected term $\tfrac12\alpha_0^2\nu^2T^2=\tfrac12(na)^2T^2$ of \eqref{eq:ident-kappa2} is identical for the two models and cancels; their second cumulants agree to $O(\nu^4)$.

Downstream occurrences fixed: the chapter abstract; the §\ref{sec:ident-thm4} preamble; the final sentence of Theorem~\ref{thm:ident}'s statement; "All three observables are reproduced exactly" in the proof of part (i), now "All three entries of the fitted triple … in the sense fixed before this proof"; §\ref{sec:ident-discussion} paragraph 2, which now also gives the quoted half-width as \eqref{eq:ident-quotedhw} and the $-1.94\%$ factor.

## 4. [CITE] must — sarb2024conv does not mention SABR

**DONE.** §\ref{sec:ident-discussion} Limitations, final paragraph, rewritten to the report's wording: normal (Bachelier) implied volatility is the quoting convention \citep[\S8, p.~26]{sarb2024conv}, with optional linear decay and the $\Delta/3$ effective maturity \citep[\S8.3.1--\S8.3.2, pp.~28--29]{sarb2024conv}, and "the choice of SABR as the smile parameterisation inside that convention is this thesis's and not the market's". No citation was invented and none deleted from the bibliography.

## 5. [ADD] must — the two-business-day payment lag

**DONE.** §\ref{sec:ident-question}, "Why the basis and not the convexity": a new paragraph plus a `\datanote{}`. The lag is stated with its locators \citep[\S6.1, p.~8 and \S7.6, p.~24]{sarb2024conv}, its mechanism named (the successor price is a $\Q^{T+\Delta+\delta_p}$-expectation, so $F$ acquires a drift equal to minus its covariation with $\log$ of the numéraire ratio, which is $\delta_p$ times the stub forward at first order), and the size bounded: $|\text{shift}|\le\alpha_0\sigma_{\mathrm{stub}}\delta_p(T+\Delta)\le0.005$ bp taking $\sigma_{\mathrm{stub}}\sim\alpha_0=60$ bp, $\delta_p\le4$ calendar days and the correlation at one, against a quote precision of $0.01$ bp. The absolute claim is replaced by the qualified one: no convexity term of the in-advance/in-arrears kind, and a payment-lag term below quote precision at the order worked to. The data note records that no volatility of a two-day stub forward is estimated anywhere in the thesis, so the bound is an upper bound on an unmeasured quantity.

## 6. [CITE] must — the cessation date

**DONE.** §\ref{sec:ident-question} first sentence, split in two and given primary locators: `\citep[p.~1]{isda2025}` for the cessation of all remaining tenors after the final publication on 31 December 2026, and `\citep[Sects.~2 and~4]{isda2025}` for the fallback mechanism (Fallback Rate (ZARONIA), spread as the five-year historical median). The Chapter~\ref{ch:intro} pointer is kept, now for the rest of the transition record only.

## 7. [ADD] must — $\varepsilon=1/3$ is not derived

**DONE.** Remark~\ref{rem:ident-epsilon} rewritten at the front and given its own `\datanote{}`. The arithmetic is in the text: the sample standard deviation $17.12$ bp \citep[Sec.~3, p.~5]{alfeus2026} is a level and $\eta$ is a diffusion coefficient, so they are not comparable; under an Ornstein--Uhlenbeck reading the stationary level standard deviation is $\eta/\sqrt{2\kappa}$, giving the new display \eqref{eq:ident-etabracket}, $\eta=17.12\,\mathrm{bp}\times\sqrt{2\hat\kappa}$ with $\hat\kappa=0.028$ \citep[Sec.~5.1, Table~4]{alfeus2026}. With $\Delta t$ in years, $\eta\approx4$ bp and $\varepsilon\approx0.07$; with $\Delta t$ in days at 252 business days, $\eta\approx64$ bp and $\varepsilon\approx1.07$. The text then says that the one available estimate does not pin the expansion parameter to within an order of magnitude, that $\eta=20$ bp is a round illustrative value inside $[4,64]$ bp, and that the width of that bracket is itself an identifiability statement of the same kind as the theorem.

The data note carries the unit ambiguity, quotes the source's own hedge ("depends on the sampling scale used in estimation"), quotes **no** half-life in days or years, and records three further cautions the report did not ask for but which the Highlights note requires: the source's model is a CIR-type jump diffusion and not an Ornstein--Uhlenbeck process, so \eqref{eq:ident-etabracket} is an order-of-magnitude reading of it; the estimate is under $\Prob$ and $\eta$ is under $\Q^{T+\Delta}$; and the units of the reported parameters are not stated in basis points beside the estimates.

Carried through: the chapter abstract now says "illustrative South African parameters" and states the bracket; §\ref{sec:ident-example} Parameters names $\eta=20$ bp as illustrative and points to the bracket.

## 8. [ADD] must — the book-level consequence

**DONE.** New subsection §\ref{subsec:ident-book}, "The book-level consequence: the intervals add", with Corollary~\ref{cor:ident-book}, its one-line proof and display \eqref{eq:ident-bookreserve}: with the basis vector shared, the book's at-the-money mismarking is the single linear function $-v_1\sum_i\vartheta_iq_ic^*_i$ of $v_1=\eta\rho_{BF}$, so the identified interval for the book has half-width $\eta|\sum_i\vartheta_iq_ic^*_i|$; for a book long in every expiry that is the sum of the per-caplet half-widths. Chapter~\ref{ch:zar} is named as the user, in the additive form. Step 4 of the worked example ties in: R20,550 per R100 million on one caplet, twenty times that on a book of twenty such expiries and not $\sqrt{20}$ times.

One correction to the report's version, again stated for the panel rather than declined. The report says that "under the per-expiry variant the errors are independent and the reserve is a root-sum-square". As an identified-set statement that is not right: with per-expiry parameters the coordinates $v_1^{(i)}$ range over a product of intervals, and the supremum of a sum over a product set is the sum of the suprema, so the worst case is $\eta\sum_i|\vartheta_i|q_ic^*_i$, which never cancels. The chapter therefore states three readings: no diversification across expiries under the shared assumption; partial immunisation of a long-short book, which is the *only* offset the chapter licenses and is exactly what the shared assumption buys, tested by V6; and a paragraph saying that the root-sum-square a risk system would compute presupposes a probability distribution on the identified set, which the chapter does not supply, an identified set not being a distribution. This is the safer statement for Chapter 7 to inherit and a lesson is appended.

## 9. [FIX] must — V4, V5, V6 not falsifiable; V1, V2 loose

**DONE**, all five, plus the honesty point from §8 of the report.

- **V1**: exact endpoints (item 2); observation dates fixed as weekly Wednesday marks, or the preceding business day when a Wednesday is a holiday; expiry grid fixed as $\{1,2,3,5,7,10\}$ years; both stated as fixing the denominator of the $90\%$.
- **V2**: same dates and grid; and it now names which $(\alpha_0,\nu)$ enter the half-width, in the same words as Step 3, namely \eqref{eq:ident-inverse} at $p=0$, $\alpha_0=\sqrt{a^2-\hat\eta^2}$, $\nu=na^2/\alpha_0^2$.
- **V3**: the report's honesty point added — at the chapter's own parameters the half-width is 29% of the midpoint, so the illustration fails the chapter's own 25% threshold, and the text says so and says why that is the point of stating a threshold.
- **V4**: paired sign test of the two absolute errors, one-sided in favour of the interval midpoint, at the 5% level, run twice (whole grid pooled; expiries of three years and longer); ties to the quoted precision of 0.01 bp discarded with the discarded count reported; pass rule stated.
- **V5**: statistic named (Pearson correlation of the two series across dates at a fixed expiry), level 5%, and the dependence correction named — a moving-block bootstrap at the $b^*$ of Theorem~\ref{thm:block-b}, evaluated at the record length and $r=2$ — with the reason (the implied $\rho_{BF}$ series is a trailing-window construction and autocorrelated by design).
- **V6**: both terms operationalised. *Stable*: interquartile range of the series below 0.2 in correlation units, and maximum absolute difference of per-expiry medians below 0.2. *Moves with the level*: OLS regression of implied $\rho_{BF}$ on the contemporaneous $B_0(t)$ with slope significant at 5% by the same bootstrap. Both outcomes are tied to the two reserve formulas of Corollary~\ref{cor:ident-book}, and it is stated that neither falsifies the theorem.

## 10. [ADD] must — jumps in the basis, as a gap item

**DONE.** New item **(d)** in the `\gap{}` box after Theorem~\ref{thm:ident}. It names what breaks: $\kappa_3(X)$ acquires a term in the third moment of the jump measure which is proportional to neither $\rho_{BF}\eta$ nor $\rho_{B\alpha}\eta$, so the two-dimensionality of the contamination is not established for a jumping basis; and it says this is the one open item that could change the dimension of the deficit rather than its size, citing \citep[Abstract]{alfeus2026}.

## 11. [ADD] must — the expansion parameter is stochastic

**DONE.** Gap item **(a)** extended by four sentences. $\eta$ is constant while $\alpha_t$ is a lognormal martingale, so $\eta/\alpha_t$ is random; at $\nu=0.4$, $T=1$ its median is $0.361$ and its interquartile range is $[0.276,0.473]$ around a time-zero value of $1/3$; a uniform remainder bound must hold in expectation over the law of $\alpha$ or on an event of stated probability with the complement bounded; and the natural small parameter may be $\eta/\alpha_t$.

Numbers recomputed rather than copied: $\alpha_{T}=\alpha_0\exp(\nu Z_T-\tfrac12\nu^2T)$ at $Z_T=\mp0.674490$ gives $\varepsilon\in[0.2757,0.4729]$, median $0.3611$. The report's "$[0.22,0.50]$" appears to be a 10th-to-90th percentile spread; the chapter states the interquartile range with the numbers that go with it.

## 12. [CUT-REPETITION] must — Theorem 4(iii)

**DONE.** Part (iii) of the theorem statement and the `\emph{(iii).}` proof paragraph are both deleted. One sentence is inserted in the proof of part (ii): "The re-solve is well posed because the Jacobian of the observed level, skew and curvature in $(\alpha_0,\rho,\nu)$ is non-singular for $\nu\neq0$ and $|\rho|\neq\sqrt{2/3}$ (Chapter~\ref{ch:prelim}, after Proposition~\ref{prop:prelim-lsc}), and globally invertible by Proposition~\ref{prop:ident-inverse}." The forward reference in §\ref{sec:ident-count} ("That is exactly what Theorem 4(iii) records") is rewritten to point at Chapter 2 as well, so no dangling reference to a deleted part remains.

## 13. [CUT-REPETITION] must — the chapter notes repeat §5.1.3

**DONE.** The first paragraph of the Chapter notes now begins at its only new content, the Piterbarg attribution; the direction-of-contamination restatement is deleted. §\ref{sec:ident-question} remains the single home.

## 14. [FIX] must — two clauses narrate the reference pipeline

**DONE.** "no locator is given here because the paper was not available in a readable copy" is deleted and replaced by `\gap{Citation needed: a section locator in \citet{piterbarg2020} for the statement that the fallback acts as a strike shift in a normal model.}`, the plain `\citet{piterbarg2020}` remaining in the sentence. The `\gap{}` after Definition~\ref{def:ident-identified} is handled under item 15.

## 15. [CITE] must — vdv1996 is the wrong book

**DONE**, by the report's preferred option (i). The `\gap{}` after Definition~\ref{def:ident-identified} is removed entirely and replaced by one plain sentence: the definition is the standard set-identification formulation and is stated in full because the chapter needs the interval-valued version. The final clause of the Chapter notes, "The definition of identifiability is standard; \citet{vdv1996} is the intended general reference", is deleted. `vdv1996` no longer appears anywhere in the chapter, and no replacement citation was invented.

## 16. [FIX] must — Proposition 5.7(iii) outside its hypotheses

**DONE.** Both statement and proof. The statement now reads that the identified set for the diffusion coefficient at the clock is unbounded **above** and bounded below only by $0$. The proof takes $p=-1$, $\rho_{B\alpha}=-\rho$, for which the left side of \eqref{eq:ident-admiss} is $1-2\rho^2+\rho^2=1-\rho^2$, admissible with equality for every $\eta>0$ with no hypothesis relating $\eta$ to $a$; then $\theta=a$, $\alpha_0=a+\eta$, and $\eta\to\infty$ gives the conclusion. The proof says explicitly why \eqref{eq:ident-alpharange} is not available for this argument.

## 17. [PROVE] should — the Schur-complement criterion

**DONE.** Proof of Lemma~\ref{lem:ident-psd}(i) now proves it rather than asserting it, in the three lines the report suggested: with $S=\begin{psmallmatrix}I_2&M^{-1}c\\0&1\end{psmallmatrix}$ the congruence $C=S^\top\mathrm{diag}(M,\,1-c^\top M^{-1}c)S$ holds, and congruence by an invertible matrix preserves the signs of the eigenvalues because $x^\top Cx=(Sx)^\top D(Sx)$ with $x\mapsto Sx$ a bijection of $\R^3$. No bibliography entry added.

## 18. [ADD] should — closed-form check in place of the Monte Carlo

**DONE.** The `\datanote{}` after Remark~\ref{rem:ident-reading} now gives the four relative deviations ($-0.9\%$, $-1.4\%$, $+0.2\%$, $-1.2\%$), reads "to within about $1.5\%$", and adds the exact closed-form check of the $a$ entry, retaining $(e^{\nu^2T}-1)/\nu^2$ in \eqref{eq:ident-kappa2}, which gives $1.13441$ and shows in closed form that the whole residual on that entry is the dropped $O(\nu^2T^2)$ term. The simulation description is otherwise unchanged, and the Appendix~\ref{app:data} obligation stands.

## 19. [ADD] should — the estimation error in $\hat\eta$

**DONE.** New paragraph at the head of §\ref{sec:ident-validation}, before the two non-negotiable design constraints. It states that every criterion is a statement about $\hat\eta$; recalls Proposition~\ref{prop:ident-consistent}(iii); gives the one-for-one transmission, the half-width being linear in $\eta$; gives the realised-volatility relative standard error $1/\sqrt{2N_w}$, that is $4.5\%$ for a 252-day window, or $0.83$ bp on the $18.43$ bp half-width, and compares it with the $29\%$ interval width and the $1.94\%$ bracket correction; and says that the physical-to-pricing-measure gap is a risk premium with no sampling distribution and cannot be reported as a standard error.

## 20. [ADD] should — $\beta\neq0$ in the open items

**DONE.** New item **(e)** in the `\gap{}` box. It records that Black volatility is one of the three mandated formats and the historical South African one \citep[\S8, p.~26]{sarb2024conv}; that the strike shift is exact for every $\beta$ but translates the smile only at $\beta=0$; and the honest answer, that for $\beta>0$ the cumulant computation goes through with $F$-dependent coefficients while the map from cumulants to the Hagan triple no longer decouples, so two-dimensionality is not established.

## 21. [FIX] should — three numerical statements

**DONE**, all three, each recomputed in double precision here before editing.
(a) Step 3 display now reads $65.7267\times1.011058\times0.930949=61.8649$ bp, quoted as $61.86$, with the error $+5.24$ bp; the table row and the Step 4 sentence are changed to $61.86$.
(b) Step 4: midpoint $64.6110$ bp against $\Phi_0(F_0)=64.5557$ bp, "to within $0.06$ bp"; the $30\%$ ratio recomputed against $61.86$.
(c) Remark~\ref{rem:ident-extreme}: $\alpha_0(0.5)=56.4831$ bp, a deviation of $12.219$ bp, "three fifths of $\eta$ rather than half", with the numbers shown.

## 22. [FIX] should — one legal overstatement, one locator

**DONE.** (a) §\ref{sec:ident-question} now reads "every JIBAR-linked cap, floor and swaption that incorporates the fallback provisions", folded into the item-6 rewrite. (b) The Lemma~\ref{lem:ident-cumulants}(i) citation is sharpened to `\citep[Ch.~3, pp.~128--238]{karatzas1991}`, the page range the Highlights note verifies. It was not sharpened to a numbered result because the Itô isometry is part of the construction in §3.2 and the note records no single numbered statement of it; the numbered result the note does verify, Prop.~3.2.6, is about density of simple integrands and is cited in Chapter 2 for that.

## 23. [ADD] should — a real figure and a number the desk can use

**Split.**

**DONE** for the desk number. Step 4 of §\ref{sec:ident-example} now gives the at-the-money vega as $0.39894\sqrt{T+\Delta}=0.446028$ per unit notional and accrual per unit of normal volatility, that is R4,460 per basis point on R100 million at $\Delta=0.25$, and the half-width as
$100{,}000{,}000\times0.25\times0.446028\times0.001843=\text{R}20{,}550$
of undiscounted premium: the reserve on one caplet attributable solely to the unidentified basis correlation. The sentence closes by pointing at Corollary~\ref{cor:ident-book} for the twenty-expiry book.

**DEFERRED** for the two plots, to round 2 and to the figure-planner, for a reason outside this file. `main.tex` loads `graphicx` only — no `tikz`, no `pgfplots` — so an inline plot cannot be drawn from this chapter without editing `main.tex`, which I do not own, and there is no PDF in a `Figures/` directory to `\includegraphics`. The requirement is therefore: add `\usepackage{pgfplots}` to `main.tex`, or generate `Figures/ch5-ident-region.pdf` and `Figures/ch5-ident-band.pdf`. Both are closed-form and need no data: the ellipse is \eqref{eq:ident-region} at $\rho\in\{0,-0.2,-0.8\}$, and the band is the pointwise envelope of \eqref{eq:ident-decomp} over $E_\eta$ at the worked parameters. The captions in the chapter already specify axes, series and the claim each figure tests, so no further specification is needed.

---

## Panel judgements outside the numbered items

**Wrong-sign caveat placed in the theorem statement as well.** The report's judgement asked for "both, not either". A clause is now in the statement of Theorem~\ref{thm:ident}, immediately after \eqref{eq:ident-decomp}: $\Phi_1,\Phi_2$ are the $\varepsilon$-derivatives; at $\varepsilon=1/3$ the $O(\varepsilon^2)$ term in the skew coefficient exceeds the $O(\varepsilon)$ term, so the first-order part is a guide to magnitude and not to sign at that value; the at-the-money conclusion is unaffected because it is exact in $\varepsilon$. The quantitative statement stays in Remark~\ref{rem:ident-epsilon} and the gap-box item (a) is unchanged in that respect.

**Two remarks left alone, as the report directed.** The pre-registration sentence ("a criterion chosen after the result is not a criterion") and the dated literature search in the Chapter notes are untouched.

---

## New and changed `\gap{}` boxes

| Box | Change |
|---|---|
| After Definition~\ref{def:ident-identified} | **REMOVED** (item 15). Replaced by one plain sentence; no citation. |
| After Theorem~\ref{thm:ident}, item (a) | **EXTENDED** (item 11): the stochasticity of $\varepsilon$ through $\alpha_t$, with the interquartile range $[0.276,0.473]$ and the requirement that any uniform bound hold over the law of $\alpha$. |
| After Theorem~\ref{thm:ident}, item (d) | **NEW** (item 10): a basis with jumps; $\kappa_3$ acquires a term proportional to neither $\rho_{BF}\eta$ nor $\rho_{B\alpha}\eta$, so two-dimensionality is not established. |
| After Theorem~\ref{thm:ident}, item (e) | **NEW** (item 20): $\beta\neq0$; the cumulant computation survives, the map from cumulants to the Hagan triple no longer decouples. |
| Chapter notes | **NEW** (item 14): citation needed, a section locator in \citet{piterbarg2020} for the fallback as a strike shift in a normal model. |

Net: two new gap items inside the Theorem~\ref{thm:ident} box, one new citation-needed box, one box removed, one box extended. Nothing that was proved is now marked unproved, and nothing marked unproved is now asserted.

## Word count and length

| | Words | Estimated typeset pages at 300 words/page |
|---|---|---|
| Before | 10,283 | about 34 |
| After | **13,574** | about 45 |

Budget is 44 pages. The chapter has gone from roughly ten pages under to roughly at or one page over, and the two deferred figures will add about one more. Nothing was cut to make room, as instructed; the only deletions are items 12, 13, 14 and 15, which the single-source, invisible-apparatus and zero-hallucination rules required and which together remove about half a page. The page-budget auditor should confirm against the next full build rather than against the words-per-page proxy, since a large share of the added content is displayed mathematics and two data-note boxes, which do not typeset at 300 words to the page. If a cut is needed after the build, the cheapest half page without losing content is Remark~\ref{rem:ident-checks}'s second case, which duplicates the $O(\varepsilon^2)$ observation made in §\ref{sec:ident-count}.

## Build

`main.tex` does not compile in this environment for a reason unrelated to this chapter: `macros.tex` line 33 defines `\newtheorem*{failure}`, and `\failure` is already defined by one of the packages `main.tex` loads, so the run halts before any chapter is read. This chapter was therefore compiled in a standalone wrapper with the same preamble and `failure` renamed. Result: no errors, no warnings, no undefined citations, and no undefined intra-chapter references. The only undefined references are the cross-chapter ones absent from the standalone wrapper; each target was checked to exist in its own file, including the one reference this round adds, `thm:block-b` in `ch4-sharpness-blocking.tex`. The `macros.tex` clash is an orchestrator or builder item, not a chapter item.
