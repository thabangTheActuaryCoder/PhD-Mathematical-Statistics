# Chapter 5, Identifiability of the Successor-Rate Smile — round 1 review

Panel perspectives adopted: forward measures, SABR, identifiability, benchmark reform, practitioner, honesty, examiner, plus the zero-hallucination citation rule.
Files read: the chapter; STANDARD.md, LESSONS.md, GROUND-TRUTH.md, LOOP.md, CONTENT-MAP.md; `13-mathematics-3yr.tex`; ch2, ch3, ch4; the Highlights notes for hagan2002, karatzas1991, sarb2024conv, bisl2025, alfeus2026, turfus2023, willems2020, lyashenko2019, piterbarg2020, vdv1996.
No previous round exists, so item 2 of the report structure is omitted.

## 1. Verdict

**MAJOR.** All four strengthened claims survive independent verification and the closed-form fitted triple is correct, including the special case and the Monte Carlo, which an independent simulation reproduced to three decimal places; the chapter's mathematical core is sound and is the strongest chapter drafted so far. The verdict is MAJOR and not MINOR because the proof of the intermediate case of Theorem~\ref{thm:ident-two}(i) is not a proof, the word "exact" is used in three different senses without being defined once, the quoted-convention half-width $\eta c^*q$ asserted in the theorem is contradicted by the chapter's own worked example, and four load-bearing statements about the market carry no source that exists on disk. None of these threatens a result; every one of them would be found by an examiner in an afternoon.

## 2. Re-check of previous round

Not applicable: this is round 1.

## 3. Numbered items, hardest first

### 1. [PROVE] must — the intermediate case of Theorem 4(i) has no valid proof

Location: §5.5.2 "The theorem", proof of Theorem~\ref{thm:ident-two}(i), the paragraph beginning "For intermediate $w$, apply Proposition~\ref{prop:ident-inverse}".

The sentence "choose $\rho_{B\alpha}$ to be the self-consistent solution of the last equation of \eqref{eq:ident-inverse}, which exists and is unique because that equation is linear in $\rho_{B\alpha}$ once $\rho$ is required to equal $\rho_{B\alpha}$ only at the endpoints and is otherwise free within $(-1,1)$" is not an argument. The last equation of \eqref{eq:ident-inverse} is one equation, $\rho=(ra-\eta\rho_{B\alpha})/\alpha_0(p)$, in two unknowns $(\rho,\rho_{B\alpha})$; nothing in it is unique. The sentence that follows is also invalid: it appeals to "convexity of the admissible region", but the admissible region $\{\rho_{BF}^2-2\rho\rho_{BF}\rho_{B\alpha}+\rho_{B\alpha}^2\le1-\rho^2\}$ has $\rho$ as a *coefficient*, and $\rho$ varies along the segment joining the two endpoint models, so the two endpoints are feasible for two *different* regions and convexity says nothing.

Replace both sentences with an explicit one-parameter family, which I have verified. For $p\in[-1,1]$ set

    theta(p) = sqrt(a^2 - eta^2 (1-p^2)),   alpha_0(p) = theta(p) - p eta,
    rho_Balpha(p) = rho(p) p,               rho(p) = r a / theta(p),
    nu(p) = n a^2 / (alpha_0(p) theta(p)).

Then: (a) $\rho_{B\alpha}=\rho\rho_{BF}$ is exactly the condition $c_2=0$ in the Cholesky construction of Lemma~\ref{lem:ident-psd}(ii), so the basis is driven by $W$ alone; (b) substituting into the last equation of \eqref{eq:ident-inverse} gives $\rho(\alpha_0(p)+p\eta)=ra$, that is $\rho=ra/\theta(p)$, so the family is self-consistent by construction and no fixed point has to be argued for; (c) admissibility is immediate, since the left side of \eqref{eq:ident-admiss} becomes $p^2-2\rho^2p^2+\rho^2p^2=p^2(1-\rho^2)\le1-\rho^2$ with equality if and only if $p=\pm1$; (d) $|\rho(p)|\le|r|a/\sqrt{a^2-\eta^2}<1$ under the standing hypothesis $a>\eta\sqrt2$ whenever $|r|\le\sqrt{1-\eta^2/a^2}$, which should be added to the hypotheses or checked as a side condition. I verified (c) and (d) numerically at the worked-example values for $p\in\{-1,-\tfrac12,0,\tfrac12,1\}$: admissibility holds at every $p$, with equality only at $p=\pm1$. Two bonuses worth one sentence each in the chapter: at $p=\pm1$ the family returns exactly $\mathcal M_\pm$ with $\rho=r$, and at $p=0$ it returns exactly the naive analyst's model of Step 3 ($\rho_{B\alpha}=0$, $\rho=ra/\alpha_0$, $\alpha_0=\sqrt{a^2-\eta^2}$), so the segment is a homotopy from one extreme through the market convention to the other. About fifteen lines. Why: without this the exactness of the identified interval rests on an existence claim that is asserted rather than shown, and the interval is the chapter's headline.

### 2. [FIX] must — the quoted-convention half-width in Theorem 4(i) is not exact, and the chapter's own worked example says so

Location: Theorem~\ref{thm:ident-two}(i), final sentence ("Hence the successor at-the-money volatility is identified within an interval of half-width exactly $\eta$ at the clock, and $\eta\,c^*\sqrt{\tau^*/(T+\Delta)}$ in the quoted convention"); also §5.7 Step 4 and criterion V1.

The two extreme models have different vol-of-vol, $\nu^\pm=na/(a\mp\eta)$, hence different correction brackets $c^{*\pm}$. Recomputation at the worked parameters:

| quantity | value |
|---|---|
| $\mathcal M_+$ quoted at-the-money | 46.1820 bp |
| $\mathcal M_-$ quoted at-the-money | 83.0400 bp |
| actual quoted half-width | **18.4290 bp** |
| $\eta q c^*$ with $c^*$ from the observed triple | 18.7929 bp |
| $\eta q c^*$ with $c^*$ from the true triple | 18.8718 bp |

The exact statement is the one the chapter proves: the *diffusion coefficient at the clock*, $\alpha_0$, is identified within exactly $[a-\eta,a+\eta]$. Pushing that interval through the Hagan bracket is not an affine map, and the quoted half-width is $\eta qc^*\big[1+\tfrac1{24}(2-3r^2)n^2\tau^*\,a^2/(a^2-\eta^2)\big]/c^*$-type expression, i.e. $\eta qc^*$ up to a relative $O(\varepsilon^2\nu^2\tau^*)$ term worth $-2\%$ here. Do three things: state part (i) for $\alpha_0$ at the clock and call *that* exact; give the quoted half-width as $\eta qc^*+O(\varepsilon^2\nu^2\tau^*)$ with the worked number 18.43 against 18.79 as the illustration; and change V1's interval to the exact endpoints $\Phi_0$-implied $a\mp\hat\eta$ each carried through its own bracket, which costs nothing and removes a 2% conservatism from the primary acceptance criterion. Why: a theorem that says "exactly" and a worked example that contradicts it by 2% in the same chapter is the single most damaging thing an examiner can find, and here the underlying result is right.

### 3. [CLARIFY] must — define "exact" once, and say what is matched exactly

Location: chapter abstract (line 4), §5.5 preamble, Theorem~\ref{thm:ident-two}(i) ("All three observables are reproduced exactly, not to first order"), Remark~\ref{rem:ident-epsilon}, §5.9.1 paragraph 2.

The chapter uses "exact" for three different things: exact in $\varepsilon$ (true of \eqref{eq:ident-map}, \eqref{eq:ident-inverse}, \eqref{eq:ident-alpharange}); exact in the sense of an identity in the model (true of the strike shift $(R+s-K)^+=(R-K')^+$); and "all three observables are reproduced exactly", which is *false as written*, because $(a,r,n)$ are not observables. They are the three functionals $\kappa_2$, $\kappa_3$ and $\Var\langle L\rangle_T$ matched **at leading order in $\nu$**; the observables are the caplet prices, and two models that agree on $(a,r,n)$ agree on the prices only up to the neglected $\nu$-terms and the Hagan error. Add one displayed sentence after Theorem~\ref{thm:ident-two}(i):

> Throughout, "exactly" means as an identity in $\varepsilon$ at the leading order in $\nu$ at which the triple $(a,r,n)$ is defined by Proposition~\ref{prop:ident-map}; the two models of part (i) reproduce the three matched cumulant functionals identically in $\varepsilon$, and reproduce the caplet prices themselves up to the $O(\nu^2)$ cumulant error and the error of the Hagan approximation.

Then give the good news, which is checkable in two lines and strengthens the chapter: because $\nu^\pm=na/\alpha_0^\pm$, the product $\alpha_0\nu=na$ is the *same* for $\mathcal M_+$ and $\mathcal M_-$, so the leading neglected term of the exact second cumulant, $\tfrac12\alpha_0^2\nu^2T^2$, is identical for the two models and the observable mismatch between them is $O(\nu^4)$, not $O(\nu^2)$. That is a genuine robustness statement and it belongs in the chapter. Why: the qualifier must be in place before the claim is copied into Chapter 1, Chapter 8 and the abstract, which the orchestrator's lessons of 2026-09-10 already schedule.

### 4. [CITE] must — sarb2024conv does not mention SABR

Location: §5.9.2 Limitations, final paragraph: "Normal SABR with a linearly decaying volatility is the class in which the market convention is written \citep[\S8.3.1--\S8.3.2, pp.~28--29]{sarb2024conv}".

A full-text check of the Highlights note for sarb2024conv returns **no occurrence of SABR anywhere in the paper**. What §8 p.26 supports is that normal (Bachelier) implied volatility is one of three mandated quote formats; what §8.3.1 p.28 and §8.3.2 eqs (15)–(16) p.29 support is that volatility decay is optional and linear when applied, with the $\delta/3$ effective maturity. Rewrite as: "The quoting convention in which the market conventions paper is written is normal (Bachelier) implied volatility \citep[\S8, p.~26]{sarb2024conv} with an optional linear volatility decay and the $\Delta/3$ effective maturity \citep[\S8.3.1--\S8.3.2, pp.~28--29]{sarb2024conv}. The choice of SABR as the smile parameterisation inside that convention is this thesis's, not the market's". Why: zero-hallucination rule; and the corrected sentence is a *better* sentence for the chapter's own argument that identifiability is a property of the class the modeller chose.

### 5. [ADD] must — the two-business-day payment lag against "no convexity term appears anywhere in this chapter"

Location: §5.1.3 "Why the basis and not the convexity", final sentence of paragraph 1.

The chapter's foundational claim is that both instruments pay at $T+\Delta$ and are therefore priced under one measure. The Highlights note for sarb2024conv records that the ZARONIA caplet in the market convention pays at $T(i)=T_i+2$ business days (§7.6, p.~24), and the librarian's note says explicitly that Chapter 2 should cite it only for that. Chapter 2 does not treat the lag; neither does this chapter. Add two sentences and a `\datanote{}`: the successor caplet under the convention pays two business days after the accrual end, so the change from $\Q^{T+\Delta}$ to $\Q^{T+\Delta+2\mathrm{bd}}$ contributes a convexity term of order $\alpha_0\,\sigma_{2\mathrm{bd}}\,(2/365)$, which at the worked parameters is below $10^{-6}$ of the rate and invisible at quote precision; the statement in the text is then "no convexity term of the in-advance/in-arrears kind, and a payment-lag term below quote precision" rather than "no convexity term appears anywhere in this chapter". Why: GROUND-TRUTH correction 1 and the LESSONS entry of 2026-09-09 forbid the in-advance/in-arrears term, which is right; they do not license silence about the lag, and a benchmark-reform examiner will raise it in the first ten minutes.

### 6. [CITE] must — the cessation date has a source on disk and does not use it

Location: §5.1.1 "The problem", first sentence: "At the close of business on 31 December 2026 the JIBAR fixing is published for the last time ... (Chapter~\ref{ch:intro})".

Chapter 1 is a stub containing a single `\gap{}`, so the cross-reference certifies nothing. The primary source is on disk with a locator: isda2025, p.~1, "publication of all such remaining tenors of JIBAR will permanently cease immediately following their final publication on December 31, 2026", and §1 quotes the SARB announcement itself. `isda2025` is in `bibliography.tex`. Add `\citep[p.~1]{isda2025}` to the sentence and keep the Chapter 1 pointer for the rest of the transition record. Do the same for the fallback mechanism sentence in the same paragraph. Why: zero-hallucination rule; the single-source rule points to a chapter that does not yet exist, and one locator costs one line.

### 7. [ADD] must — the load-bearing empirical claim, $\varepsilon=1/3$, is not derived from anything

Location: Remark~\ref{rem:ident-epsilon}, "The rate volatility $\alpha_0=60$ bp is a plausible three-month caplet level and $\eta=20$ bp of annualised basis volatility is modest against the observed level variation of the spread"; also §5.7.1 and the chapter abstract's "a third of the at-the-money level".

Everything the chapter says about the market rests on $\varepsilon=\eta/\alpha_0=1/3$: the 29% interval, the "expansion parameter is not small" limitation, the skew interval containing zero, and the sentence quoted above. The comparison offered is between an annualised diffusion volatility (bp per $\sqrt{\text{year}}$) and a *level* standard deviation of 17.12 bp \citep[Sec.~3, p.~5]{alfeus2026}. Those are different units and the inference is not stated. Do the arithmetic in the text. Under an Ornstein–Uhlenbeck reading of the only published dynamic model, the stationary level standard deviation is $\eta/\sqrt{2\kappa}$, so $\eta=17.12\sqrt{2\hat\kappa}$ with $\hat\kappa=0.028$ \citep[Sec.~5.1, Table~4]{alfeus2026}. The paper leaves the time unit of $\hat\kappa$ ambiguous, as the Highlights note and LESSONS entry of 2026-09-09 both record: with $\Delta t$ in years, $\eta\approx4$ bp and $\varepsilon\approx0.07$; with $\Delta t$ in days and 252 business days, $\eta\approx64$ bp and $\varepsilon\approx1.07$. State that bracket, with a `\datanote{}` recording the unit ambiguity, and then say that $\eta=20$ bp sits inside it and is chosen as a round illustrative value. Roughly one paragraph. Why: this *strengthens* the chapter. "The one available estimate does not pin the expansion parameter to within an order of magnitude" is a far more defensible sentence than "20 bp is modest", it is exactly the kind of ambiguity the identifiability result is about, and it pre-empts the examiner's question "where does a third come from?" Under no circumstances quote a half-life in days or years without the `\datanote{}`.

### 8. [ADD] must — the book-level consequence of shared basis parameters is missing, and it is the practitioner's first question

Location: new final paragraph of §5.6.3 "What would close the deficit", or a new short subsection in §5.9.

Table~\ref{tab:ident-count} makes $(\eta,\rho_{BF},\rho_{B\alpha})$ shared across expiries; that is what makes the deficit 3 rather than $3m$. The consequence is not drawn: because the nuisance is one vector for the whole surface, the sign of the mismarking is the *same* at every expiry, so the identified intervals across a book of caplets do not diversify. A bank holding $m$ expiries faces a reserve equal to the sum of the per-caplet half-widths $\sum_i \hat\eta\,q_ic^*_i\,\mathrm{vega}_i$, not its root-sum-square; a book that is long some expiries and short others is partially immunised, and by exactly the amount the shared-parameter assumption dictates. Under the per-expiry variant (deficit $3m$) the errors are independent and the reserve is a root-sum-square. Three to five sentences and one display. Why: it converts the chapter from a statement about one caplet into a statement about a book, it is a one-line corollary of the chapter's own table, and it is what Chapter 7's reserve decomposition will need. This is the largest single piece of missing content.

### 9. [FIX] must — three of the six acceptance criteria are not falsifiable as stated

Location: §5.8.2, criteria V4, V5, V6.

The chapter sets the right standard for itself ("a criterion chosen after the result is not a criterion") and then fails it three times.
- **V4**: "If the theory has content, the second error is smaller at longer expiries ... reported with a paired sign test." Not falsifiable: no partition of "longer expiries" is fixed, no significance level, no one- or two-sidedness, no rule for ties. Fix: "the paired sign test of the two absolute errors, one-sided, at the 5% level, over the expiry set $\{1,2,3,5,7,10\}$ years pooled, and separately for expiries of 3 years and longer".
- **V5**: "a correlation across dates significantly different from zero" — no test, no level, no treatment of serial dependence, and the implied-$\rho_{BF}$ series is strongly autocorrelated by construction. Fix: name the statistic, the level and the dependence correction (a block bootstrap with the block length of Chapter 4, which the thesis already owns).
- **V6**: "A stable series ... a series that moves with the level of the basis" — no operational definition of either. Fix: state the regression of the implied $\rho_{BF}$ on the level of $B_0(t)$ with a stated level, and a stated bound on the interquartile range of the series for "stable".
Also fix in V1 and V2: the observation frequency and the expiry grid are not fixed in advance, so the denominator of the 90% is adjustable; state both (for example weekly Wednesday marks on a named expiry grid). And V2 must say which $(\alpha_0,\nu)$ enter its half-width; the worked example uses the observable-based values of Step 3, and V2 should say so in the same words. Why: pre-registration is the whole point of putting §5.8 in this chapter, and three of six criteria as written can be satisfied after the fact.

### 10. [ADD] must — a fourth open item: jumps in the basis

Location: the `\gap{}` box after Theorem~\ref{thm:ident}, as item (d).

The chapter's own Limitations paragraph says the only published dynamic study of the South African spread models it with jumps on monetary-policy dates \citep[Abstract]{alfeus2026}, and that "a jump component would break the cumulant computation of Lemma~\ref{lem:ident-cumulants} at third order and is not treated here". That is precisely an open item and it belongs in the gap box with the other three, not only in the discussion. State what breaks: $\kappa_3$ acquires a term in the third moment of the jump measure that is *not* proportional to either $\rho_{BF}\eta$ or $\rho_{B\alpha}\eta$, so the two-dimensionality of the contamination — the structural fact the whole chapter rests on — is not established for a jumping basis. Two or three sentences. Why: the honesty auditor's standard is that the gap box, not the discussion, is where a reader looks for what is unproved; and this is the one open item that could change the *dimension* of the deficit rather than its size.

### 11. [ADD] must — the expansion parameter is stochastic, and gap item (a) does not say so

Location: the `\gap{}` box after Theorem~\ref{thm:ident}, item (a).

Item (a) asks for a bound $|\cdot|\le C(\nu,T,|u|)\varepsilon^2$ uniform over the strike grid and the admissible ellipse. It omits the third uniformity, which is the hard one: $\varepsilon=\eta/\alpha_0$ is the ratio at time zero, but $\eta$ is constant while $\alpha_t$ is a lognormal martingale with vol-of-vol $\nu=0.4$, so the instantaneous ratio $\eta/\alpha_t$ is itself random and at $T=1$ has roughly a $[0.22,0.50]$ interquartile spread around $1/3$ at the worked parameters. Any uniform remainder bound must hold in expectation over the law of $\alpha$, or on an event of stated probability with the complement bounded; and the natural small parameter may be $\eta/\alpha_t$ rather than $\eta/\alpha_0$. Add two sentences to item (a). Why: this is the reason the remainder is genuinely hard rather than routine, and saying so is worth more to an examiner than the current formulation.

### 12. [CUT-REPETITION] must — Theorem 4(iii) re-derives a result Chapter 2 already states

Location: Theorem~\ref{thm:ident-two}(iii) and its proof paragraph "\emph{(iii).}".

Chapter 2, in the paragraph after Proposition~\ref{prop:prelim-lsc} (ch2-preliminaries.tex line 540), already says: "the Jacobian of $(\ell,\mathsf s,\mathsf c)$ with respect to $(\alpha_0,\rho,\nu)$ is, to first order, upper triangular with non-zero diagonal $(1,\nu/2,(2-3\rho^2)\nu/(3\alpha_0))$ whenever $\nu\ne0$ and $|\rho|\neq\sqrt{2/3}$. Chapter~\ref{ch:identifiability} uses this non-singularity". Theorem~\ref{thm:ident-two}(iii) restates it as a numbered part of a theorem and its proof re-derives the diagonal and the determinant. Under the single-source rule this is the Chapter 2 object and Chapter 5 gets one sentence. Delete part (iii) from the theorem statement and delete its proof paragraph; put in the proof of part (ii), where it is used, the single sentence "the re-solve is well posed because the Jacobian of the observed level, skew and curvature in $(\alpha_0,\rho,\nu)$ is non-singular for $\nu\neq0$ and $|\rho|\neq\sqrt{2/3}$ (Chapter~\ref{ch:prelim}, after Proposition~\ref{prop:prelim-lsc}), and globally invertible by Proposition~\ref{prop:ident-inverse}". Saves about half a page and removes a duplicate. Why: [CUT-REPETITION] items are must-priority by the single-source rule, and this is the clearest instance in the chapter.

### 13. [CUT-REPETITION] must — the chapter notes repeat §5.1.3

Location: §"Chapter notes", first paragraph, beginning "The direction of the contamination established here reverses the intuition".

The direction-of-contamination argument is made in §5.1.3 paragraph 3 ("The direction of the contamination is the point of the chapter and is easily got backwards..."), again in Remark~\ref{rem:ident-reading}, again in §5.9.1, and a fourth time here; and Chapter 2 already carries it once at line 305. Cut the chapter-notes paragraph down to its only new content, which is the Piterbarg attribution, and begin the paragraph there. Why: single-source rule and the redundancy sweep; §5.1.3 is the right home and three restatements dilute it.

### 14. [FIX] must — two sentences narrate the reference pipeline

Location: §"Chapter notes", "no locator is given here because the paper was not available in a readable copy"; and the `\gap{}` after Definition~\ref{def:ident-identified}, "is cited in the chapter notes without a locator until the page is checked".

The invisible-apparatus rule forbids the thesis text from mentioning drafts, rounds or the state of the reference collection; a `\gap{}` box states only what remains to be established, in mathematical terms. Replace the first with `\gap{Citation needed: a section locator in \citet{piterbarg2020} for the statement that the fallback acts as a strike shift in a normal model.}` and keep the plain `\citet{piterbarg2020}` in the sentence, which the librarian's note explicitly permits without a page. Replace the second with `\gap{Citation needed: a textbook locator for the definition of identifiability of a parametric family.}` and nothing else. Why: binding rule; and both sentences currently tell the reader something about the candidate's library rather than about the mathematics.

### 15. [CITE] must — vdv1996 is the wrong book for identifiability

Location: the `\gap{}` after Definition~\ref{def:ident-identified} and §"Chapter notes", final sentence.

`vdv1996` in `bibliography.tex` is van der Vaart and Wellner (1996), *Weak Convergence and Empirical Processes*. That book is about empirical-process theory; it is not a source for the definition of identifiability of a parametric family, and the Highlights note records that it was never obtained and that **no locator may be cited from it**. Naming it as "the intended source" is a misattribution of exactly the kind the zero-hallucination rule exists to prevent. Two acceptable fixes, in order of preference: (i) drop the claim to a source altogether — Definition~\ref{def:ident-identified} is stated in full and self-contained, and the chapter notes can say "the definition used here is the standard set-identification formulation, stated in full above because the chapter needs the interval-valued version" with no citation and no gap; or (ii) if a citation is wanted, it must be to a work whose bibliographic details are certain and which actually contains the definition — van der Vaart (1998), *Asymptotic Statistics*, §5.5 is the usual one, but it is not in `bibliography.tex` and has no Highlights note, so under the rule it cannot be cited until the librarian has one. Take (i) now. Why: a wrong citation is worse than no citation, and here none is needed.

### 16. [FIX] must — Proposition 5.7(iii) applies a result outside its hypotheses

Location: proof of Proposition~\ref{prop:ident-consistent}(iii), "take $\eta$ arbitrarily large with $\rho_{BF}$ chosen to keep $a$ fixed: by \eqref{eq:ident-alpharange} the at-the-money value ranges over $[a-\eta,a+\eta]$".

Equation \eqref{eq:ident-alpharange} is proved under $a>\eta\sqrt2$, which fails for every $\eta\ge a/\sqrt2$; and for $\eta>a$ the value $a-\eta$ is negative and not attainable at all. The conclusion is nonetheless true and has a one-line proof that needs no hypothesis: take $p=-1$, so $\theta=a$, $\rho_{B\alpha}=-\rho$ and $\alpha_0=a+\eta$, which is admissible with equality in \eqref{eq:ident-admiss} for every $\eta>0$; hence the at-the-money value $a+\eta$ is attainable for arbitrarily large $\eta$ and the set is unbounded above. Substitute that argument. Also correct the claim's shape: the interval is unbounded *above*; below it is bounded by 0, since $\alpha_0>0$. Why: a proof that cites a display outside its stated hypotheses is a defect an examiner reads as carelessness, and the repair is two lines.

### 17. [PROVE] should — the Schur-complement criterion is used without proof or locator

Location: proof of Lemma~\ref{lem:ident-psd}(i), "$C\succeq0$ if and only if the Schur complement $1-c^{\!\top}M^{-1}c\ge0$".

Every other step of this lemma is proved in full, including the Cauchy–Schwarz maximisation, which is the harder part. The Schur-complement equivalence is the one borrowed fact and it carries neither a proof nor a locator, which the zero-hallucination rule requires even for results "any statistician would call common knowledge". Prove it in three lines rather than adding a reference: with $M\succ0$, the congruence $C=S^{\!\top}\begin{psmallmatrix}M&0\\0&1-c^{\!\top}M^{-1}c\end{psmallmatrix}S$ with $S$ unit upper triangular is immediate, and congruence by an invertible matrix preserves the sign of the spectrum. Why: no new bibliography entry is needed and the chapter is then self-contained on this point.

### 18. [ADD] should — replace the Monte Carlo check of the level by an exact closed-form check

Location: the `\datanote{}` after Remark~\ref{rem:ident-reading}.

I reran the simulation independently (1000 Euler steps, $2\times10^6$ paths in ten batches, common random numbers between the $\eta=0.002$ and $\eta=0$ runs, the three functionals extracted from the sample exactly as described) and obtained ratios **1.1344, 1.1469, 0.8416, 0.9652** against the chapter's 1.135, 1.148, 0.841, 0.965. The data note is honest and reproducible; that is a real finding and the chapter deserves the credit. Two improvements. First, the $a$ entry needs no simulation at all: the *exact* second cumulant of Lemma~\ref{lem:ident-cumulants}(i), retaining $(e^{\nu^2T}-1)/\nu^2$ instead of $T$, gives the ratio $1.13441$, which agrees with the simulation to five significant figures and demonstrates in closed form that the residual is exactly the dropped $O(\nu^2T^2)$ term. State that, since a closed-form check beats a Monte Carlo check. Second, the sentence "The four agree to within $1.5\%$" is at the boundary: the $r$ entry differs from the closed form by 1.38% with the chapter's numbers and 1.51% with mine, the discrepancy being simulation noise in the third cumulant. Write "to within about 1.5%" or quote the four relative deviations. Why: the tighter statement cannot be attacked, and the closed-form check makes one third of the data note independent of any code.

### 19. [ADD] should — the estimation error in $\hat\eta$ is nowhere propagated

Location: §5.8.1 step (4) and §5.8.3 "What the test cannot show".

The whole validation replaces $\eta$ by a trailing-window estimate $\hat\eta$, and Proposition~\ref{prop:ident-consistent}(iii) has just established that the identified set is *unbounded* when $\eta$ is unknown. So every criterion in §5.8.2 is a statement about $\hat\eta$, not about $\eta$, and the chapter says nothing about how the sampling error in $\hat\eta$ enters. Add a paragraph: the interval half-width is linear in $\eta$, so a relative standard error $\mathrm{se}(\hat\eta)/\hat\eta$ transmits one-for-one into the half-width; with a trailing window of $n$ daily observations of a driftless basis the realised-volatility relative standard error is about $1/\sqrt{2n}$, roughly 4.5% for a one-year window, which is small against the 2% and 29% numbers elsewhere in the chapter but must be reported alongside V1; and the physical-to-pricing-measure gap, which the chapter rightly calls a risk premium, is *not* a standard error and cannot be reported as one. Half a page. Why: a containment criterion evaluated with an estimated half-width is otherwise uninterpretable, and Chapter 6 will need the sentence.

### 20. [ADD] should — $\beta\neq0$ belongs in the open items

Location: the `\gap{}` box after Theorem~\ref{thm:ident}.

$\beta=0$ is fixed in the standing assumptions and defended by the normal quoting convention, which is right. But the chapter itself notes that the strike shift is exact for any $\beta$ "though only for $\beta=0$ does it act as a pure translation of the smile", and the South African market has historically quoted Black volatility \citep[\S8, p.~26]{sarb2024conv}. Whether the two-dimensionality of the contamination survives for $\beta>0$, where the basis is additive but the diffusion coefficient is not, is not established and is not listed. Two sentences in the gap box. Why: an examiner who prices in lognormal will ask, and the honest answer — the cumulant computation goes through but the map from cumulants to the Hagan triple no longer decouples — is short.

### 21. [FIX] should — three small numerical statements

Location: §5.7 Step 3, §5.7 Step 4 paragraph 2, Remark~\ref{rem:ident-extreme}, Table~\ref{tab:ident-example}.

Recomputed in double precision: (a) the analyst's reported successor at-the-money volatility is $65.7267\times1.011058\times0.930949=61.8649$ bp, which rounds to **61.86**, not 61.87, and the error against 56.6254 is **+5.24** bp, not +5.25; correct the two places in the text and the table row. (b) The midpoint of $[46.1820,83.0400]$ is 64.6110 and $\Phi_0(F_0)=64.5557$, a difference of **0.055** bp; "to within $0.05$ bp" should read "to within $0.06$ bp". (c) In Remark~\ref{rem:ident-extreme}, "a correlation of $0.5$ already costs half the interval" understates the exact figure: $\alpha_0(0.5)=56.4831$ bp, a deviation of 12.219 bp from $a$, which is **61%** of $\eta$, not 50%. Say "already costs three fifths of the interval", which is both exact and a stronger reply to the objection the remark is answering. Why: numbers in a thesis are checked; each of these is a one-token edit and the third improves the argument.

### 22. [FIX] should — one legal overstatement and one locator to sharpen

Location: §5.1.1 first sentence; proof of Lemma~\ref{lem:ident-cumulants}(i).

(a) "every JIBAR-linked cap, floor and swaption on a South African bank's book falls back to compounded ZARONIA plus a fixed credit adjustment spread" — the fallback operates through the contractual definitions, so it reaches contracts that incorporate the ISDA definitions or the Rulebook, not literally every contract. Write "every JIBAR-linked cap, floor and swaption that incorporates the fallback provisions". (b) `\citep[Ch.~3, \S2]{karatzas1991}` for "the Itô isometry and the covariance formula for stochastic integrals against correlated Brownian motions" is a section-level locator where the Highlights note records numbered results in that section (Prop. 3.2.6 at p. 134); either sharpen to a numbered result or state the section with its page range, which the note gives as 128–238. Why: zero-hallucination rule asks for locators, and the first is the kind of sentence a practitioner reader will stop at.

### 23. [ADD] should — make Figure 5.1 a real figure and give the desk a number it can use

Location: Figure~\ref{fig:ident-region} and the `\figplan{}` after Table~\ref{tab:ident-example}; §5.7 Step 4 final paragraph.

The identified region is an ellipse in closed form, \eqref{eq:ident-region}, with no data dependence at all; it can be drawn today for $\rho\in\{0,-0.2,-0.8\}$ from three lines of code, and the hand-built placeholder box should be replaced by the actual plot. Do the same for the smile band, whose ingredients are all closed-form. And in Step 4, the price interval is already computed as a factor of 1.80 between the cheapest and dearest admissible mark, which is good; add the same number in the units a desk uses, namely the reserve per R100 million notional per unit accrual at the worked at-the-money vega, so that the width of the identified set appears once as money. Why: the chapter's own page budget leaves room (see below), and Figure~\ref{fig:ident-region} is the one picture that makes "ellipse, not rectangle" land.

## 4. Missing for a strong doctoral chapter

The mathematics is there and it is better than the brief; what is missing is the last step from a theorem about one caplet to a statement about a bank. Three additions would carry it. First, the book-level corollary of item 8: the shared basis vector makes the mismarkings perfectly aligned across expiries, so intervals add rather than diversify, and a converted book's reserve is therefore linear in the number of expiries — a result the chapter owns already and does not state. Second, an honest bracket for $\varepsilon$ (item 7): the chapter's most quotable numbers all depend on $\varepsilon=1/3$, and the only published estimate of the basis dynamics leaves $\eta$ ambiguous by more than an order of magnitude; saying so converts a soft spot into a result. Third, the two figures should exist (item 23) — both are closed-form and neither needs data. Beyond those, the chapter would be stronger for a short subsection on what the *desk* does on the morning of 1 January 2027: mark the midpoint, hold the half-width times vega as a reserve, and disclose the width, with the three-line calculation shown once. On length there is room for all of this: at 10,283 words the chapter should typeset to about 34 pages against a budget of 44, judged from Chapter 2's 14,484 words over 52 pages and Chapter 3's 11,300 over 34. Nothing here needs to be bought by cutting.

## 5. Should go

Little should go, and none of it for length. Theorem~\ref{thm:ident-two}(iii) and its proof paragraph must go, because Chapter 2 already states the Jacobian non-singularity and refers forward to this chapter for its use (item 12); it becomes one sentence inside the proof of part (ii). The first paragraph of the Chapter notes must go, because the direction-of-contamination argument is already made in §5.1.3, in Remark~\ref{rem:ident-reading} and in §5.9.1, and Chapter 2 makes it once more at its own line 305 (item 13); only the Piterbarg attribution is new. Two clauses must go on the invisible-apparatus rule: "because the paper was not available in a readable copy" and "until the page is checked" (item 14). The claim that `vdv1996` is the intended source for identifiability must go outright rather than be relocated (item 15). Finally the phrase "No convexity term appears anywhere in this chapter" should go in its absolute form and return qualified by the payment lag (item 5). Everything else in the chapter is earning its space; the three cumulants, the inverse map and the worked arithmetic in particular are exactly the kind of honest length the standard asks for.

## 6. Verification record for the four strengthened claims and the fitted triple

All recomputed independently; scripts held in the session scratchpad, not in the repository.

| Claim | Status |
|---|---|
| 1. Schur-complement ellipse; $\max_{E_\eta}\lvert v_1\rvert=\max_{E_\eta}\lvert v_2-2\rho v_1\rvert=\eta$ | **SURVIVES.** Schur complement, the change of coordinates $y=v_2-2\rho v_1$ (the $\mp4\rho^2x^2$ terms cancel as claimed), and the three values of $c^{\!\top}A^{-1}c$ all check; the third is $4\rho^2-4\rho^2+1=1$ as printed. |
| 2. At-the-money interval exactly $[a-\eta,a+\eta]$, endpoints attained by $dL=(\alpha_t\pm\eta)dW$ | **SURVIVES for $\alpha_0$ at the clock.** $\alpha_0(p)=\theta(p)-p\eta$ is strictly decreasing on $[-1,1]$ under $a>\eta\sqrt2$ with $\alpha_0(\pm1)=a\mp\eta$; both endpoint models are admissible with equality in \eqref{eq:ident-admiss} and give $W^B=\pm W$. Two repairs required: the intermediate case has no valid proof (item 1, explicit family supplied and verified) and the *quoted* half-width is not $\eta qc^*$ (item 2: 18.4290 against 18.7929 at the worked parameters). |
| 3. Identified region in the level–skew plane is an ellipse | **SURVIVES.** $\hat A=-v_1/\eta$, $\hat S=-(v_2-2\rho v_1)/\eta$, and the substitution into Lemma~\ref{lem:ident-psd}(iii) gives \eqref{eq:ident-region} with axis projections $[-1,1]$ for every $\lvert\rho\rvert<1$; the degeneration to a segment along $\hat A=-\hat S$ as $\lvert\rho\rvert\to1$ is also correct, with the $x$-extent staying exactly $\eta$. |
| 4. The skew interval contains zero at the worked parameters | **SURVIVES.** Half-width $qc\,\nu\eta/(2\alpha_0)=0.052509$ per unit strike $=5.251$ bp per 100 bp; centred on $-4.2007$ gives $[-9.45,+1.05]$, which contains zero, and the ratio to the naive skew is $\eta/(\alpha_0\lvert\rho\rvert)=1.2500$ exactly. |
| Fitted triple $a,r,n$ | **CONFIRMED** by rederiving the cumulant match: $a^2=\alpha_0^2+2\rho_{BF}\alpha_0\eta+\eta^2$, $a^4n^2=\alpha_0^2\theta^2\nu^2\Rightarrow a^2n=\alpha_0\theta\nu$, and $r=(\alpha_0\rho+\eta\rho_{B\alpha})/a$ on dividing. First-order expansions and $rn$ all check. |
| Special case $\rho_{BF}=1$, $\rho_{B\alpha}=\rho$ | **CONFIRMED.** Admissible with equality; $W^B=W$ from the Cholesky factor ($c_2=c_3=0$); $dL=(\alpha_t+\eta)dW$; $a=\alpha_0+\eta$, $r=\rho$, $n=\nu\alpha_0/(\alpha_0+\eta)$ all reproduce \eqref{eq:ident-map}. One caveat for item 3: the check compares the map against the *instantaneous* coefficients of a model that is not itself SABR, so it verifies the algebra rather than the approximation, and "verified without any expansion" overstates it slightly. |
| Monte Carlo agreement within 1.5% | **CONFIRMED, at the boundary.** Independent simulation gives 1.1344, 1.1469, 0.8416, 0.9652 against the chapter's 1.135, 1.148, 0.841, 0.965 and closed forms 1.1450, 1.1644, 0.8390, 0.9769. Maximum relative deviation 1.38% with the chapter's numbers, 1.51% with mine; the exact second cumulant explains the $a$ entry in closed form as 1.13441. See item 18. |

No code for this simulation exists anywhere in `Code/` or `Council Workspace/thesis/code/`; the data note's promise that "the simulation code and a regression test belong to Appendix~\ref{app:data}" is therefore an outstanding obligation on Appendix C, and the parameters recorded in the note are sufficient to reproduce it.

## 7. Direct edits made

None. Every defect found is either a proof repair, a citation change or an addition, and none of them is a mathematical or factual error that would mislead the next reader if left in place for one round: the four headline claims are true as stated, and the two statements that are wrong as written (the quoted half-width in Theorem~\ref{thm:ident-two}(i), item 2; the hypothesis violation in Proposition~\ref{prop:ident-consistent}(iii), item 16) are wrong in the direction of conservatism and are recorded above with their repairs. The revision writer should make them.

## 8. Judgements the panel was asked for

**Are the acceptance criteria falsifiable?** V1 and V3 are: both name a quantity, a threshold and a decision. V2 is nearly so and needs only the sentence saying which $(\alpha_0,\nu)$ enter the half-width. V4, V5 and V6 are not falsifiable as written and are covered by item 9. One further honesty point: at the chapter's own worked parameters the half-width is 29% of the midpoint, so V3's 25% threshold would record the South African illustration as *uninformative*. Say so in §5.8.2 — it is a point in the chapter's favour, since V3 is then demonstrably a criterion that can fail, and a reader who spots it unaided will assume the threshold was chosen to pass.

**Does the wrong-sign note belong in the theorem statement?** It bounds the theorem's validity; it does not undermine it. Theorem~\ref{thm:ident} is an asymptotic statement as $\varepsilon\to0$ and is untouched by the numerical size of the remainder at $\varepsilon=1/3$; and the at-the-money conclusion is exact in $\varepsilon$, so the failure is confined to the first-order skew and curvature terms $\Phi_1,\Phi_2$ at large $\varepsilon$. The right placement is both, not either: one clause in the theorem statement immediately after \eqref{eq:ident-decomp} — "the terms in $\Phi_1$ and $\Phi_2$ are the $\varepsilon$-derivatives; at $\varepsilon=1/3$ the $O(\varepsilon^2)$ term in the skew coefficient exceeds the $O(\varepsilon)$ term, see Remark~\ref{rem:ident-epsilon}" — and the quantitative statement left in Remark~\ref{rem:ident-epsilon} where it is now. Keep it in the gap box as well, since item (a) is what would remove it. A theorem whose statement carries the domain in which its first-order part is useful is stronger, not weaker, and the current arrangement invites the examiner to think the chapter found the defect after stating the theorem.

**Are the three open items complete?** No. Four are missing: jumps in the basis (item 10, must, because it is the only one that could change the *dimension* of the deficit); the stochasticity of $\varepsilon$ through $\alpha_t$ inside item (a) (item 11, must); $\beta\neq0$ (item 20, should); and the propagation of estimation error in $\hat\eta$, which is not a gap in the theorem but is a gap in §5.8 and is item 19. Item (c) on far-strike information is well posed and is the right open item; items (a) and (b) are correctly identified.

**Does any text mention the writing process?** Two clauses do and are covered by item 14. Two others were examined and are acceptable: "Stating the criteria here rather than in Chapter~\ref{ch:usd} is deliberate: a criterion chosen after the result is not a criterion" is a pre-registration statement about scientific method, not about drafting; and the dated literature search in the Chapter notes, with its explicit "This is a statement about a dated search and not a proof of novelty", is normal scholarly practice and matches the LESSONS instruction of 2026-09-09 to write "no evidence found as of" rather than claiming novelty. Leave both.

**Page budget.** About 34 typeset pages estimated against a budget of 44, from 10,283 words benchmarked on Chapter 2 (14,484 words, 52 pages) and Chapter 3 (11,300 words, 34 pages). The chapter is roughly ten pages under. This is unusual and it is the reason every addition above is an addition and only one item asks for a deletion on grounds of repetition rather than of length. Two live cross-references, `app:tenor` and `app:data`, resolve to appendix files that exist but were not in the last build of `main.tex`; the builder should confirm they resolve. No other dangling reference was found: all 60-odd `\ref` targets used by the chapter exist.

## 9. Lessons enforced

- [2026-09-09][council round 5][all] both caplets under $\Q^{T+\Delta}$, no in-advance/in-arrears convexity term — enforced and extended by item 5 (the payment lag is a different mechanism and must be named).
- [2026-09-09][finance theorist][ch5] the basis contaminates the observed JIBAR smile, not the compounded caplet — enforced; the chapter has the direction right, four times over, which is item 13.
- [2026-09-09][finance theorist][ch2] linear decay and $\Delta/3$ are assumptions, said once and inherited — enforced; §5.2.1 does exactly this.
- [2026-09-09][scout] $s=16.19$ bp for 3M JIBAR, fixing date 3 December 2025 — enforced; the value and the `bisl2025` locator are correct.
- [2026-09-09][scout] no evidence of quoted ZARONIA screens as of September 2026; state as dated absence — enforced; §5.1.1 and the Chapter notes both do.
- [2026-09-09][data-engineer-zar] never estimate $\eta$, $\rho_{BF}$, $\rho_{B\alpha}$ from the SARB synthetic curve — enforced; the data note after §5.6.3 states it.
- [2026-09-09][writer][ch2] reuse the worked-example numbers rather than recomputing — enforced; §5.7.2 reuses 60.81, 56.62, $q=0.93095$, $c^*=1.013578$ and $-4.05$ bp exactly as Chapter 2 has them.
- [2026-09-09][writer][ch2] the $z/x(z)$ series and the sign convention for the skew (differentiate in $K$) — enforced; the skew signs in §5.5 and §5.7 are consistent with it.
- [2026-09-09][reference-librarian][ch2] cite `(A.67a)` with $\beta=0$ or `(A.69a)`, never `(A.70a)` alone — enforced; the Chapter notes state the erratum correctly.
- [2026-09-09][reference-librarian] `sarb2024conv` locators §7.6 p.25, §8 p.26, §8.3.1–8.3.2 pp.28–29 — enforced, and item 4 records the one place where the citation is asked to support more than the source says.
- [2026-09-09][reference-librarian] `alfeus2026` $\hat\kappa=0.028$ with an ambiguous time unit; quote only with a `\datanote{}` — enforced; the chapter correctly avoids quoting a half-life, and item 7 asks it to use the ambiguity rather than sidestep it.
- [2026-09-09][review-panel][ch2,ch5] cite `willems2020` Thms 4.1–4.2 for the non-decaying variant, not for the time-change lemma — enforced; §5.9.2 cites it correctly.
- [2026-09-10][writer-ch5] the half-width $\eta$ is exact in $\varepsilon$; quote the at-the-money statement as exact and every skew statement as first order — enforced, and refined by items 2 and 3 (exact for $\alpha_0$ at the clock, not for the quoted volatility).
- [2026-09-10][writer-ch5] the admissible region is the Schur-complement ellipse and the identified region is an ellipse, not a rectangle — enforced and independently verified.
- [2026-09-10][writer-ch5] never present a first-order skew or curvature number for ZAR without the wrong-sign caveat — enforced; see the judgement in §8 on where the caveat belongs.
- [2026-09-10][writer-ch5] the deficit is a rank statement, not a counting statement — enforced; §5.6.1 paragraph 2 is correct and well aimed at the thirteen-strike objection.
- STANDARD, single-source rule — enforced by items 12 and 13.
- STANDARD, invisible apparatus — enforced by item 14.
- STANDARD, zero-hallucination citation rule — enforced by items 4, 6, 15, 17 and 22.
