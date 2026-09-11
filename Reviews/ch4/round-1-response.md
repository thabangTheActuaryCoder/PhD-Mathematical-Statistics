# Chapter 4 (`ch4-sharpness-blocking.tex`) — round 1 response

Reviser: `thesis-revision-writer`. Date 2026-09-11. File owned and edited: `thesis/chapters/ch4-sharpness-blocking.tex` only.

Every numerical claim introduced or moved in this round was recomputed independently before it was written: the three rows of the table in Remark~\ref{rem:sharp-constants} at all six record lengths, the four crossover record lengths, the refined variance series $S_2(1)$, the two Chebyshev constants and the two sub-Gaussian constants. No number appears in the chapter that was not reproduced.

## Items

### 1. Confidence range of Theorem~\ref{thm:block-lower} — DONE
Option (i) taken. The theorem now defines $\delta^{\max}_N:=\kappa_rN^{-(r-1)/2}$ with $\kappa_r\in(0,1]$ and states parts (a) and (b) on $\delta\in[N^{-r},\delta^{\max}_N]$; the sentence after the display says that for $r>1$ no $N$-free confidence lies inside the range, and gives $[4\times10^{-6},0.045\kappa_2]$ at $N=500$, $r=2$. (The review's $4\times10^{-7}$ for the lower endpoint is a slip: $N^{-r}=500^{-2}=4\times10^{-6}$.) The proof route in §\ref{sec:sharp-lower} now names $\delta^{\max}_N$ as the endpoint it can service and says the range cannot be extended to an $N$-free $\delta_0$. Residue recorded as item (6) of the §\ref{sec:sharp-lower} `\gap{}` box: $\kappa_r$ is not exhibited, and what happens above $\delta^{\max}_N$ is not determined.

### 2. "Blocked wins at every record length" is an artefact of Chebyshev — DONE
Option (a), with the closing claim rewritten as option (b) requires. Remark~\ref{rem:sharp-constants} now carries three rows at six record lengths and states both crossings. The unblocked sub-Gaussian row is $\sqrt{2\sigma_r^2\log(2/\delta)/N}$ with the chapter's own variance proxy $\sigma_r^2=\tfrac14+2C\zeta(r)=3.540$ from Lemma~\ref{lem:sharp-var}, that is $5.11N^{-1/2}$, against the Chebyshev $11.90N^{-1/2}$. The crossover moves from $9.95\times10^4$ to $2.17\times10^3$ periods, quoted as $10^5$ and $2.2\times10^3$. The recommendation is reversed in all three places: Remark~\ref{rem:sharp-constants} ("on the present accounting the unblocked route is preferred on any record longer than a few thousand periods"), §\ref{sec:sharp-example} design rule step 4, and §\ref{sec:sharp-discussion} "What blocking buys, stated once". A `\datanote{}` marks the third row an estimate and not a proved bound and records both crossings and both refined crossings; item (5) of the §\ref{sec:sharp-lower} `\gap{}` box repeats that status.

One deviation from the report, stated for the record. The review writes $\sigma^2=\tfrac14+2C\zeta(r)=3.79$ and hence $5.3N^{-1/2}$; the formula it gives evaluates to $3.540$ at $C=1$, $r=2$ ($3.79$ is $\tfrac12+2\zeta(2)$, the Chebyshev numerator). The chapter uses the value the formula and Lemma~\ref{lem:sharp-var} produce, $3.540$ and $5.11$. Both land on "about two and a half thousand"; the settled crossover is $2.2\times10^3$.

### 3. $b^*$ minimises an upper bound with two constants set to one — DONE (all three parts)
(i) The proof of Theorem~\ref{thm:block-b}(b) now carries the general-constant minimiser $\big(2(r+1)c_2/c_1\big)^{2/(2r+3)}N^{3/(2r+3)}$, its value $\big(2\sqrt2\,C(r+1)\big)^{2/(2r+3)}N^{3/(2r+3)}=26.4$ at $r=2$, $C=1$, $N=500$ against the $23.9$ of \eqref{eq:sharp-bstar}, the statement that $b^*$ is quoted for the normalised $f$, that only the exponent and $b^*/b_{\mathrm{bal}}$ are constant-free, and that $f$ dominates \eqref{eq:sharp-shortfall} only when $C\le1$.
(ii) Remark~\ref{rem:sharp-rate} gains two sentences saying that Theorem~\ref{thm:block-b} minimises an upper bound and that no lower bound on $\E[(1-\alpha-F_P(\hat q))^+]$ for the blocked route is proved. A new `\gap{}` box follows it, stating that the optimality of $b^*$ is optimality of the bound and naming the two missing pieces.
(iii) §\ref{sec:sharp-block} and the theorem are titled "The block length that minimises the certified shortfall (of the blocked route)". The abstract and §\ref{sec:sharp-discussion} "What was shown" now say "minimises the bound of \eqref{eq:sharp-shortfall} on the expected calibration-conditional shortfall"; design-rule step 2 says "the minimiser ... of the certified shortfall".

### 4. The two routes are compared on unequal terms — DONE
The deployment coupling was removed from the blocked side, so that both columns are calibration-side. Theorem~\ref{thm:block-rate}(c) now states that \eqref{eq:sharp-cheb} charges no coupling for the deployment block and that the blocked figures compared against it carry $n\beta(b)$, not $(n+1)\beta(b)$. The table of Remark~\ref{rem:sharp-constants} is computed from $g_{\mathrm{cal}}(b)=1/(2\sqrt{n+2})+nCb^{-r}$ and its `\datanote{}` reports both forms and shows the choice moves no entry by more than a unit in the third digit. §\ref{sec:sharp-functional} "Why the drift and the deployment gap are excluded" says both routes pay a deployment gap, $\beta(b)/\delta'$ and $\beta(b_g)/\delta'$, and that every comparison below is calibration-side to calibration-side. Design-rule step 4 says the same and requires the deployment gap of each route to be reported alongside. Which was done: the coupling was removed from the blocked route, not added to the Chebyshev bound, because the length $b_g$ of the unblocked route's gap is a free parameter and adding $\beta(b_g)/\delta'$ would have put an arbitrary constant into a proved bound.

### 5. The chapter narrates its own earlier position — DONE
The clause "this thesis included at an earlier stage of its own argument" is deleted from §\ref{sec:sharp-discussion} "What carries doctoral weight"; the sentence stands. The point is already made without apparatus in §\ref{sec:sharp-intro}.

### 6. "Threshold procedure" defined twice — DONE
Definition~\ref{def:sharp-proc} is the definition. Definition~\ref{def:sharp-error} now opens "From here a threshold procedure in the sense of Definition~\ref{def:sharp-proc} is taken to be record-measurable, $T=T(S_{1:N})$, which is the case optimised over below" and no longer redefines the term. Theorem~\ref{thm:sharp}'s use of the wider class ($T$ using side information, $T=+\infty$) is unaffected: it cites Definition~\ref{def:sharp-proc} only.

### 7. §\ref{sec:sharp-example} repeats Chapter 3's worked example — DONE
"Reading the table" now begins "The $b=10$ column reproduces the certificate of \S\ref{sec:cert-example} of Chapter~\ref{ch:certification}; the two new columns show what the design variable does. For a slowly mixing process the picture changes." The stationary-variance sentence is deleted from the `\datanote{}`. The paragraph that opened the subsection and re-described the process and its parameters is replaced by one sentence referring to \S\ref{sec:cert-example}.

### 8. §\ref{sec:sharp-functional} "Why two-sided" re-argues Chapter 3's Remark~\ref{rem:twosided} — DONE
The two-citation sentence is replaced by "Charging for over-coverage is the established form; its precedents are recorded in Remark~\ref{rem:twosided} of Chapter~\ref{ch:certification}." The $T\equiv+\infty$ degeneracy and the capital-held-against-a-loss-that-will-not-occur sentence are kept.

### 9. §\ref{sec:sharp-notes} repeats Chapter 2 on `zwart2025` — DONE
Shortened to the part that is new: "what is new here is the optimisation of a design parameter against the conditional object under dependence, not the object itself, whose operational use under exchangeability through the Beta quantile is recorded in the chapter notes of Chapter~\ref{ch:prelim}, citing the preprint of \citet[Sec.~2.2]{zwart2025}."

### 10. Chapter abstract — DONE
Cut from 192 words to 105, one clause per result, no internal justification. Measured in the chapter's own geometry and font it sets to **6 lines**, inside the 5–8 line rule. The material cut survives in §\ref{sec:sharp-intro} and §\ref{sec:sharp-discussion}.

### 11. Chapter 4's objects absent from `CONTENT-MAP.md` — DEFERRED (to the orchestrator; file not owned)
This reviser owns `chapters/ch4-sharpness-blocking.tex` only. The seventeen rows to add, all with Chapter 4 (`ch:sharpness`) as home, are listed at the end of this response so the orchestrator can paste them.

### 12. Chapter 3 restates $b^*$ and the shortfall curve — DEFERRED (to the Chapter 3 round, `thesis-redundancy-cutter`)
Confirmed as the report describes: the home of $b^*$ and of $\sqrt{b/N}+Nb^{-(r+1)}$ is Theorem~\ref{thm:block-b} of Chapter 4, which now also carries the general-constant form (item 3(i)), so Chapter 3's display is doubly duplicative.

### 13. "settled" overstates `barber2026` — DONE
§\ref{sec:sharp-functional} "Why conditional" now reads "bounded for split conformal under $\beta$-mixing by \citet[Cor.~2]{barber2026} without blocking, tightly for that procedure up to a factor $(1-\alpha)/4$ \citep[Thm.~2]{barber2026} but not over procedures". Both locators are the ones recorded in `References/Highlights/barber2026.md`.

### 14. Two pages over the 40-page budget — DONE
Measured in an isolated build (`tectonic`, same preamble and geometry, chapter alone): the chapter now runs **pages 1–40**, exactly the budget. `macros.tex` line 33 already defines the environment as `failuremode`, so the clash the review reports no longer blocks the build; nothing in `macros.tex` was touched by this reviser. Text cut: `\begin{quote}` abstract (item 10), Remark~\ref{rem:sharp-scope}, the second half of Remark~\ref{rem:sharp-lecam}, Remark~\ref{rem:sharp-func-numbers}, the prose of Example~\ref{ex:sharp-corr} duplicating its `\datanote{}`, "Why the drift and the deployment gap are excluded", "Connection to the empirical chapters", the §\ref{sec:sharp-intro} map and two of the four question paragraphs, the tail of Remark~\ref{rem:sharp-mixture}, Remark~\ref{rem:sharp-var}, the tail of Remark~\ref{rem:sharp-bp-check}, the closing sentences of the proof of Theorem~\ref{thm:block-b}(c), parts of the `ramos2026`, `zheng2024` and `halkiewicz2026` positioning paragraphs, the route of Theorem~\ref{thm:block-drift}, and three paragraphs of §\ref{sec:sharp-discussion}. No mathematical content, no gap-box content and no citation was removed.

### 15. Fuk–Nagaev locator — DONE
`\citep[Ch.~6]{rio2017}` in the proof route of §\ref{sec:sharp-lower}. Item (5) of that section's `\gap{}` box now says the chapter locator is the one recorded in the mathematical record of this thesis and that no theorem or page number has been checked against the printed text, and extends the same status to the sub-Gaussian estimate of Remark~\ref{rem:sharp-constants}. `References/Highlights/rio2017.md` does not exist; a librarian request for `rio2017` (theorem number and the exact two terms) is passed to the orchestrator and is the one input that would let item 2's third row become a proved bound.

### 16. Improve the variance constant for free — DONE
Lemma~\ref{lem:sharp-var} now states both forms, the second with $S_r(C):=\sum_{k\ge1}\min\{1/(4C),k^{-r}\}\le\zeta(r)$, and the proof derives it from $|\Cov|\le\min\{\tfrac14,Ck^{-r}\}$. Recomputed: $S_2(1)=0.894934$ against $\zeta(2)=1.644934$, Chebyshev constant $11.90\to9.03$, sub-Gaussian constant $5.11\to3.88$, and the two crossings move to $2.79\times10^4$ and $6.85\times10^2$, quoted as $2.8\times10^4$ and $6.9\times10^2$. The displayed bounds of Theorem~\ref{thm:block-rate} are left in the $\zeta(r)$ form, with a sentence saying every conclusion drawn from them is strengthened by the refinement, so that no downstream constant changes silently.

### 17. Two rigour slips — DONE
(i) The functional is written $\mathcal E(T;\Prob)$ and $\mathcal E_\delta(T;\Prob)$ throughout Definition~\ref{def:sharp-error}, with a closing sentence saying the law is suppressed where only one is in play and that $C$ is suppressed in $\mathcal E^*_\delta(N,r)$.
(ii) Theorem~\ref{thm:block-lower}(a) now concludes with probability $\ge2\delta$, and a sentence after the display says why: $\Prob(\mathcal E>\varepsilon)>\delta$ strictly is what Definition~\ref{def:sharp-error} needs before $\mathcal E_\delta$ can be bounded below. The route supplies the factor by taking $Nm^{-(r+1)}\asymp2\delta$, which changes $c_r$ by $2^{-1/(r+1)}$ and nothing else.

### 18. Consistency check integrates outside the range — DONE
Remark~\ref{rem:sharp-bp-check} now states the qualification: over $[0,\delta^{\max}_N]$ the integral $\frac{r+1}r\delta^{r/(r+1)}$ is of order $N^{-r/2}$ and the contribution of $[0,N^{-r}]$ is $O(N^{-r})$, so what the agreement tests is the shape of the rate function and not a deduction of either statement from the other. The missing lag is added: the comparison is with $(\tau+L)/(n-L+1)+2\beta(\tau)$, "up to the score-training lag $L$", cited `\citep[Cor.~1, eq.~(6)]{barber2026}`, the locator recorded in the Highlights note.

### 19. Two residues of the writing process — DONE
§\ref{sec:sharp-notes} now reads "No use of it as a lower-bound construction for a conformal prediction problem appears in the literature cited here." §\ref{sec:sharp-discussion} begins "Theorem~\ref{thm:block-b} is elementary"; the clause about what should be said plainly is deleted.

### 20. "(Attained.)" — DONE
Theorem~\ref{thm:sharp}(b) is labelled "(Attained in the limit.)", with the half-sentence "the limit taken as $M\to\infty$ in part (c) because no $Q_M$ with $M<\infty$ attains the infimum". This no longer contradicts §\ref{sec:sharp-thm8}'s explanation that $\delta_{+\infty}$ is not a law on $\R$.

### 21. Mark `zwart2025` as a preprint — DONE
"citing the preprint of \citet[Sec.~2.2]{zwart2025}", per `References/Highlights/zwart2025.md`.

### 22. Two cross-chapter locator inconsistencies — DEFERRED (to the Chapter 2 and Chapter 3 rounds)
Both resolved in Chapter 4's favour and left untouched here. (i) Chapter 4 cites `\citep[Thm.~4]{halkiewicz2026}` for the two-sided minimax statement, which matches the Highlights note; Chapter 3's "Thm. 2" must be corrected there. (ii) The caption of Table~\ref{tab:example-sweep} says "the first inequality of Proposition~\ref{prop:prelim-ar1}" and its numbers are the first inequality's; Chapter 2's sentence pointing at the middle bound must be corrected there.

### 23. Point Appendix C at the sweep labels — DEFERRED (to the Appendix C round; file not owned)
`tab:example-sweep` and `fig:example-sweep` both exist in this chapter and are stable. Nothing to change in Chapter 4.

### 24. One simulation on a genuinely polynomially mixing process — DEFERRED (to `thesis-code-conformal`, then Chapter 4 round 2)
Not declined on merit: the report is right that this is the largest available gain and the construction is already in place. It is deferred for two reasons, both rule-based. First, the numbers it asks for — the realised shortfall curve against $f(b^*)=0.255$, and the empirical $0.95$-quantile of $|F_P(T_N)-(1-\alpha)|$ — do not exist; writing a figure or a table before the run would put invented numbers in the chapter, which the zero-hallucination rule forbids and which no `\datanote{}` can repair. Second, the chapter is at exactly its 40-page budget after item 14, and the subsection is costed at about a page; it has to arrive with a page of cuts or a budget change, not on top. The chapter already states the omission plainly in §\ref{sec:sharp-discussion} "Limitations" and in "What the sweep does not show", so nothing is concealed in the interim. The simulation specification the report gives ($P_1=N(0,1)$, $P_2=N(\gamma,1)$ with $\dK=0.2$, $\Prob(D>m)=m_0^{r+1}m^{-(r+1)}$, $m_0=2$, $r=2$, $N\in\{500,10^4\}$) is passed through unchanged.

## New `\gap{}` boxes

The chapter carries four. One is new in this round and two gained items:

1. **New**, §\ref{sec:sharp-block}, after Remark~\ref{rem:sharp-rate}: no lower bound on the expected calibration-conditional shortfall of the blocked route is established, so the optimality of $b^*$ is optimality of the bound \eqref{eq:sharp-shortfall} and not of the design; a matching statement would need $1/(2\sqrt{n+2})$ shown unimprovable at fixed $b$ together with a lower bound on the price of the coupling, for which no construction is offered. (Item 3(ii).)
2. **Extended**, §\ref{sec:sharp-lower}: item (5) now records that the `rio2017` chapter locator is unverified against the printed text and that the sub-Gaussian estimate of Remark~\ref{rem:sharp-constants}, on which the reversed recommendation turns, has the same status, \eqref{eq:sharp-cheb} remaining the only proved bound for the unblocked route. (Items 2 and 15.)
3. **Extended**, §\ref{sec:sharp-lower}: new item (6), the confidence range — the bound is claimed only for $\delta\le\delta^{\max}_N=\kappa_rN^{-(r-1)/2}$, which shrinks with $N$ when $r>1$; $\kappa_r$ is not exhibited and the regime above $\delta^{\max}_N$ is not determined. (Item 1.)
4. Unchanged: §\ref{sec:sharp-drift} (five items on the partially observed drift) and §\ref{sec:sharp-w1} (the constant $\kappa$).

## Rows for `CONTENT-MAP.md` (item 11; not added by this reviser)

Seventeen, each with home Chapter 4 / `ch:sharpness` / `chapters/ch4-sharpness-blocking.tex`:

| Object | Label | What it is |
|---|---|---|
| Definition | `def:sharp-proc` | Threshold procedure and its coverage $C_T(R)$ |
| Definition | `def:sharp-transport` | Bottom-mass transport $Q_M$ |
| Lemma | `lem:sharp-dist` | $\dTV(P,Q_M)=\dK(P,Q_M)=\varepsilon$ and the cdf difference |
| Theorem | `thm:sharp` | Sharpness of the drift penalty, constant $1$ (GT Thm 8) |
| Remark | `rem:sharp-mixture` | Why the far-mass mixture attains only $1-\alpha$ |
| Definition | `def:sharp-error` | Calibration-conditional coverage error, $\mathcal E_\delta$, minimax $\mathcal E^*_\delta$ |
| Theorem | `thm:block-b` | Block length minimising the certified shortfall, $b^*$ (GT Thm 9(i)) |
| Lemma | `lem:sharp-cov` | Covariance of half-line indicators $\le\alpha(k)\le\beta(k)$ |
| Lemma | `lem:sharp-var` | Variance of $F_N$ under $\Bclass{r}$, with the $\min\{\tfrac14,Ck^{-r}\}$ refinement |
| Theorem | `thm:block-rate` | The blocked rate is not minimax (GT Thm 9(ii)) |
| Definition | `def:sharp-renewal` | Regime-renewal process |
| Lemma | `lem:sharp-renewal-beta` | Mixing of the regime-renewal process (route only) |
| Theorem | `thm:block-lower` | Mixing-driven lower bound at high confidence (GT Thm 9(iii), target) |
| Theorem | `thm:block-drift` | Minimax certifiable deficit under partially observed drift (GT Thm 9(iv), target) |
| Proposition | `prop:block-w1` | Dependent empirical Wasserstein rate over $\Bclass{r}$ (GT Thm 9(v), specialised) |
| Table | `tab:example-sweep` | Block-length sweep on the Chapter 3 synthetic process |
| Figure | `fig:example-sweep` | Planned figure: deficit terms against block length |

## Counts, length and pages

- **DONE 19 · DECLINED 0 · DEFERRED 5.** DONE: items 1–10, 13–21. DEFERRED: 11 (CONTENT-MAP, orchestrator), 12 (Chapter 3 round), 22 (Chapter 2 and Chapter 3 rounds), 23 (Appendix C round), 24 (`thesis-code-conformal`, then Chapter 4 round 2). Eleven of the thirteen must-items (1–10, 13) were closed in the chapter; the two remaining musts, 11 and 12, and the should-items 22, 23 and 24 lie in files this reviser does not own or need a run that has not happened.
- Word count (`wc -w` on the .tex, markup included): **13,999 before this pass → 13,081 after**, a net cut of 918 words on top of the content added for items 1–4 and 16. The panel's own count on its build was 13,285.
- Typeset pages, isolated build: **42 before → 40 after**. Budget 40.
- Crossover settled: **$N\approx2.2\times10^3$ periods** ($2.17\times10^3$ exactly) at $C=1$, $r=2$, $\delta=0.05$, against $9.95\times10^4$ for the Chebyshev comparison; $6.9\times10^2$ ($685$ exactly) under the refined variance constant of item 16.
