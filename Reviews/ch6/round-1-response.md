# Chapter 6 (USD LIBOR-to-SOFR validation) — round 1 response

Reviser: thesis-revision-writer. Date: 2026-09-19. Chapter file: `/Users/thabangbaloyi/Desktop/PhD Thesis/Council Workspace/thesis/chapters/ch6-usd-validation.tex`.

## Lessons applied

Read before writing: `STANDARD.md`, `LESSONS.md`, `GROUND-TRUTH.md`, `LOOP.md`, `13-mathematics-3yr.tex`, the chapter, the round-1 report, the Highlights notes for `kunsch1989`, `politis1994`, `lahiri2003`, `kupiec1995`, `christoffersen1998`, `schmitt2026`, and `bibliography.tex`.

The lessons that governed specific edits:

- **[2026-09-11][revision-writer][ch4,all] Re-derive every number a review asserts; a review's arithmetic is evidence, not authority.** Every arithmetic claim in the report was recomputed from the chapter's own formulas before being written in. Twenty-four of twenty-five checked out exactly (item 0 of the report, items 1, 2, 9, 16, 19, 27); one did not, and is corrected in item 6 below.
- **[2026-09-11][writer-ch6][ch6,ch7] Criteria are inherited, not re-thresholded; execution detail only.** Drove items 6 and 18: V4 is restored to the estimator Chapter 5 pre-registered rather than kept at the substitute, and the V5 winsorisation is made additive rather than substitutive.
- **[2026-09-11][writer-ch6][ch6,ch7] A dependence correction is additive, never substitutive.** Same two items, and item 4 (block-bootstrap *p*-value promoted to a co-equal statistic beside the binomial one, because the certificate does not license the independence the binomial test assumes).
- **[2026-09-09][statistician][ch3] Coupling cost is `(n+1)β(b)`; the deployment block must be gap-separated.** Drove item 4, whose new paragraph fixes `M = ⌊N_dep/(2b)⌋` with gaps of `b` and cites `rem:sequence` for the `(n+M)β(b)` cost of the further blocks.
- **[2026-09-10][revision-writer][ch5] The side condition `|r| < √(1−η²/a²)` and the hypothesis `a > η√2`.** Drove item 7 verbatim.
- **[2026-09-10][revision-writer][ch5,ch2,ch6,ch7] The payment lag can be dismissed only with a number.** Drove item 23.
- **[2026-09-11][revision-writer][ch2,ch3,ch4] The 5–8 line abstract is 85–135 words.** Drove item 11.
- **[2026-09-10][orchestrator][all] Never compare two methods with bounds of unequal sharpness; check both sides carry the same cost terms.** Drove item 9's 2 × 2 table.
- **[2026-09-09][reference-librarian][ch3,ch6] No locator for `kupiec1995`, `politis1994`, `lahiri2003`; `kunsch1989` only where read.** Drove items 13, 14, 26.
- **[2026-09-10][orchestrator][all] A reviser who can show a review item is wrong should correct it with the argument, not comply.** Applied to the algebra inside item 6.
- **[2026-09-11][revision-writer][ch4,ch6] A requested simulation is DEFERRED, never drafted.** Applied to the power table asked for in §4 of the report: the numbers that can be computed without data are given; the table that would need the record is not drafted.
- **[2026-09-09][examiner][all] Do not call the bootstrap comparison a theorem.** Checked and preserved throughout §6.4 and §6.9.3.
- **Zero-hallucination citation rule (STANDARD).** No new bibliography key was added; every new citation uses a locator already recorded in a Highlights note.

---

## Items 1–27

### MUST

**1. [FIX] C1 and C3 satisfiable by degenerate outcomes over most of their own grid — DONE.**
Recomputed independently over the 180 cells (`b ∈ {1,2,5,10,13} × C ∈ {0.5,1,2} × r ∈ {1.5,2,3} × ε ∈ {0,0.02,0.05,0.10}`, N = 250, α = 0.1): C1's bound is ≥ 1 in **93** cells and C3's bound is > 0 in **2**. Both confirmed exactly, with the per-`b` breakdown 36, 36, 20, 1, 0.
(a) §6.3.4 criterion C1 (`sec:usd-cert`) now carries a second paragraph giving the count 93/180 with the breakdown, the reason ("passed by a breach on every deployment block, that is by a threshold of −∞"), and the rule that such cells are recorded **not informative** rather than **pass**; `tab:usd-cert` gains a row "C1 informative?" carrying the grid count in the block header.
(b) C3 gains the matching paragraph with the count 2/180, the two live cells named (`b=10, r=3, ε=0, C ∈ {0.5,1}`, bounds 0.0166 and 0.0101), the observation that failure there needs exactly zero breaches, and the primary-cell bound −0.157. `tab:usd-cert` gains "C3 informative?".
The primary cell was **not** moved to `(10,1,3,0)`: moving it would be choosing a cell for the outcome it can produce, which is the pre-registration failure the chapter exists to avoid. The chapter says so in terms and names the two live cells in the table instead — this is the one place where the report offered a choice and the other branch was taken.
(c) §6.9.2 "What a failure would mean" gains a closing paragraph: the binding limitation at N = 250 is the record length and not Theorem `thm:cov`, since the certified bound exceeds the parameter it bounds on more than half the grid.

**2. [FIX] C4 names no decision rule — DONE.**
§6.3.4 criterion C4 now states the rule: *consistent* when `1−α̂ ≥ b_{n,k}(0.05) − ε̂ − β̄/0.05`; *conservative* when it exceeds that by more than the width of the exact binomial interval for α̂ at M blocks; otherwise *below the certified conditional level* — never pass, never fail, because the theorem is a high-probability statement. The numbers are printed: `b_{12,12}(0.05) = 0.05^{1/12} = 0.7791`, `b_{9,9}(0.05) = 0.05^{1/9} = 0.7169`, `β̄/δ' = 20β̄ = 0.20` at b = 10 and `0.118` at b = 13, hence certified conditional levels 0.529 (primary cell) and 0.549 (b = 13). All recomputed. `tab:usd-cert`'s verdict row is split into "C1–C3 verdicts" (pass / fail / not informative) and "C4 record".

**3. [FIX] The per-period hedging error contradicts its own data note — DONE.**
§6.3.1 "The book" (`sec:usd-cert`) now defines two legs and their difference: the *risk-theoretical* leg `ΔV^rt_t` (positions revalued at the policy's own volatilities, available on every date because the policy manufactures its own marks) and the *hypothetical* leg `ΔV^hyp_t` (same positions at observed successor marks), with `e_t := ΔV^rt_t − ΔV^hyp_t`, positive for losses. The text says explicitly that marking both legs at the policy's own volatilities would make `e_t` the discretisation residual of the policy's own model, and that these are exactly the two legs the attribution test of §6.4.3 compares. It then states that `e_t` exists only from `m*`, which is why the deployment window lies after `m*`, and that before `m*` the risk-theoretical leg alone survives as a diagnostic entering no score, threshold or criterion. The `\datanote{}` that followed is rewritten in the same language so the contradiction is gone.

**4. [ADD] Deployment-block layout never fixed — DONE.**
§6.3.2 gains the paragraph "The deployment blocks": `M = ⌊N_dep/(2b)⌋` blocks of length `b` alternating with gaps of `b`, the first separated from the calibration record by the trailing gap; `M = 12` at b = 10 on 2023 alone and `M = 25` extended through 2024. It cites `Remark~\ref{rem:sequence}` for the per-block statement and for the fact that C1 bounds the **expected** breach frequency `α + max_i d_K(P,Q^(i)) + (n+1)β(b)`. Two consequences follow in the text: the binomial test's independence assumption is not supplied by the certificate, the coupling of the further blocks costing `(n+M)β(b) = 0.37` at b = 10, C = 1, r = 2, M = 25 against the 0.13 C1 charges (recomputed), which is why the block-bootstrap *p*-value is a co-equal statistic; and a sizing paragraph (see §4 below).

**5. [FIX] The gap box's exculpation is false for two of four dates — DONE.**
The `\gap{}` after the windows in §6.2.2 now names what rests on each date. 31 Dec 2021 and 8 Nov 2021: boundaries only. 5 Mar 2021: additionally the constancy of `s`, which makes `B^real` well defined, `B^real` being the sole input to `η̂` and `η̂` setting the half-width that V1, V3 and V5 test — with the exact mitigation stated, that `η̂` is a volatility of first differences and so invariant to the value of `s`, so the date matters only if `s` was still moving inside `W_η`, for which the quoted-basis drift check is the diagnostic. 30 Jun 2023: additionally the ~1,100-period record length used in R2, and nothing else. **Answering the question put to the panel:** the four boundaries stand in a gap box, now with this clause corrected.

**6. [FIX] Criterion V4 silently changed — DONE, with one correction to the review's algebra.**
Chapter 5's V4 (`sec:ident-validation`, line 728) was re-read: "the absolute error of the interval midpoint **after `v₁` has been estimated from a single successor quote at the shortest expiry in the grid**". The panel's reading is right and the substitution was real. Three edits:
- §6.2.1 now carries an explicit, and single, exemption to restriction H1: on each observation date the at-the-money successor quote at the shortest expiry is visible, is used to estimate `v₁ = ηρ_BF`, and is used for nothing else. Three consequences are recorded: the anchoring pair enters neither V4 test (its error is zero by construction) and missing/derived anchoring quotes are counted; only V4 becomes a one-parameter-anchored comparison, V1, V2, V3, V5, V6 staying under full H1; and V4 thereby rests on the shared-basis assumption V6 tests, so the two verdicts are reported together.
- §6.2.1 gains **Step 4′**, defining `v̂₁(t)` as the unique solution of `(a(t,T_min) − v̂₁)c*q = Σ^anc(t)` along the homotopy `eq:ident-homotopy` (strictly decreasing from `Σ⁻` to `Σ⁺` by `eq:ident-alpharange`), by bisection, flagged to the nearer endpoint if the quote falls outside; and `Σ^{v₁}(t,T) := (a(t,T) − v̂₁(t))c*q` at every other expiry.
- `tab:usd-ident-excess` gains the row "V4 point error: median |Σ^obs − Σ^{v₁}|, bp" and keeps the midpoint as a diagnostic row; `tab:usd-ident-rhobf`'s V4 row now reads `Σ^{v₁}` against the naive mark.

**Correction to the report.** Item 6 states that `½(Σ⁺+Σ⁻)` and the naive mark differ "only through the second-order Hagan bracket term (relative size `(1/12)(2−3r²)n²τ*`, about 1.9 %, roughly 1.2 bp on a 64 bp level)". That overstates the gap by a factor of about twenty-two. Carrying each endpoint through its own bracket,

`½(Σ⁺+Σ⁻) = q[a + (2−3r²)n²a³τ*/(24(a²−η̂²))]`,  naive mark `= q[a + (2−3r²)n²aτ*/24]`,

so the relative difference is exactly `(1/24)(2−3r²)n²τ* · η̂²/(a²−η̂²)`. At Chapter 5's worked parameters `(1/24)(2−3r²)n²τ* = 0.009339` and `η̂²/(a²−η̂²) = 400/4320`, giving **0.0865 %**, that is **0.056 bp** on a 64.6 bp level — which is precisely the "agrees to within 0.06 bp" already recorded at ch5 line 643. The review's figure is the *whole* bracket correction rather than the part that survives the difference. The conclusion is therefore **strengthened**, not weakened: the substituted estimator is even closer to vacuous than the report says, and a sign test between marks five hundredths of a basis point apart on a market quoted to one hundredth decides on rounding. The corrected algebra and the 0.0865 % / 0.056 bp figures are in the chapter at the end of Step 4′, and the lesson is appended.

**7. [ADD] No admissibility check on `η̂` — DONE.**
§6.2.1 Step 4 now states the hypotheses of Theorem `thm:ident-two` that `η̂` can violate — `a > η̂√2`, without which `α₀(p) = √(a²−η̂²(1−p²)) − pη̂` is not real along the homotopy, and the side condition `|r| < √(1−η̂²/a²)` — notes that the bracket of the closed-form half-width `η̂q[1 − (2−3r²)n²τ*a²/(24(a²−η̂²))]` falls as `η̂ → a/√2` so that the asserted ordering `Σ⁺ ≤ Σ⁻` can fail at large `η̂`, and fixes the exclusion rule in advance: a pair is excluded when `η̂(t) ≥ a(t,T)/√2` or `|r(t,T)| ≥ √(1−η̂(t)²/a(t,T)²)`. `tab:usd-ident-summary` gains the column "Inadmissible". The text names it as the upper counterpart of the `η̂ < 1` bp exclusion already fixed for V5.

**8. [FIX] "No number in this chapter is reported as computed" is false — DONE.**
Both places replaced with the precise claim. The abstract now says no number is computed **from market data** and that the block-layout, deficit and sizing arithmetic uses only the record length, the level α and the assumed mixing class. The closing `\datanote{}` (now at the end of §6.9) lists the computed numbers explicitly: `b ≤ 13`, `b* ≈ 17.8`, the sweep `n = 125,62,25,12,9` with its five `k/(n+1)`, `(n+1)Cb^{−r} = 126`, the grid counts 93/180 and 2/180, the Beta quantiles 0.7791 and 0.7169, the §6.5.2 deficit table, the binomial detection thresholds at M = 12 and M = 25, and `1/p = 3` at `n' = 25`, each with its inputs.

**9. [FIX] "The two crossings" conflates two axes and omits the proved one — DONE.**
§6.5.2 is rewritten over the 2 × 2. Every number was recomputed from the chapter's own `\datanote{}` formulas (`g_cal(b) = 1/(2√(n+2)) + nCb^{−r}` minimised over feasible `b`; Chebyshev `√((½+4Cζ(r))/(Nδ))`; sub-Gaussian `√(2σ_r²log(2/δ)/N)` with `σ_r² = ¼+2Cζ(r)`; refined values with `S₂(1) = 0.894934`), and all agree with the report:

| N | blocked (feasible b) | Chebyshev (proved) | sub-Gaussian (estimate) | refined sub-Gaussian |
|---|---|---|---|---|
| 250 | 0.2040 | 0.7526 | 0.3232 | 0.2454 |
| 1100 | 0.1313 | 0.3588 | 0.1541 | 0.1170 |
| 1700 | 0.1173 | 0.2886 | 0.1240 | 0.0941 |

The chapter now prints the first three columns as a table and states the reading: blocked smaller at all three lengths against the proved bound (factors 3.7, 2.7, 2.5); smaller at all three against the printed sub-Gaussian estimate but larger at 1100 and 1700 under the refined proxy `3.879/√N`; hence "the ordering is decided by the status of the inequality used on the unblocked side and not by the record length", which is the sharper statement the report asked for.

**10. [ADD] The certified policy cannot be executed on the record it is certified over — DONE.**
`def:usd-policy` is now **delta-only**: the vega leg is removed from the certified policy. The paragraph after it states why the choice is forced (no quoted successor option market over `D_fit` and the early calibration window, so a vega leg would be untradeable on exactly the window on which the policy is fixed; a certificate on a policy that could not have been run is a certificate on nothing) and fixes repair (b) as a **second** policy: the vega-hedged variant certified separately over the same windows with its vega leg in the listed option on the three-month successor future, at the cost of an expiry reach shorter than the book's. Both repairs the report offered are therefore taken, (a) for the certified policy and (b) for the variant, and neither is presented as the other's correction.
§6.8 gains a new subsection "Execution frictions, set to zero" between §6.8.5 and §6.8.6: daily rebalancing in a transitioning benchmark and in a market being born carries bid-offer and slippage, `e_t` is computed from marks and not fills, so every block score and every threshold is biased **downward** by an amount scaling with the rebalancing frequency and the spread; the certificate is untouched, the reading of `q̂` as a reserve is not, and no spread data are requested, so the bias is named and signed but not estimated.

**11. [FIX] Abstract 190 words against 85–135 — DONE.**
Rewritten to **125 words** (measured), one clause per result: what the identification test is, what the certificate test is, that the routes are compared on equal footing, that every criterion precedes the data, that the non-informative grid cells are counted in advance, and the precise no-market-data claim of item 8. The justifications are already in §6.1.1 and were not duplicated.

**12. [ADD] The improvement claim is untestable on the data the appendix says will be available — DONE.**
§6.2.3 "Observation dates and expiries" now states the consequence in advance: V4 passes only if its long-expiry test rejects and F5 falsifies only on that arm, so under truncation V4 is recorded **not evaluable** and the improvement claim **not tested** — not passed, not failed — with the pooled test carrying no verdict; and that the minimum viable export reaches two years on the exchange arm at best, so this is the expected outcome there and not a remote contingency. F5 carries the matching clause. F10 carries it too, together with the refusal contingency (see §4 below). `tab:usd-ident-summary` gains the row "Grid obtained".

**13. [CITE] The `n^{−1/3}` attribution is unsupported — DONE.**
§6.4.1 now reads: the cube-root order is the bias–variance balance for the arithmetic mean under fixed-length blocking, `\citep[Cor.~3.1, p.~1226]{kunsch1989}`, carried across to the stationary bootstrap's geometric length **by analogy and not by any result read here**, and used for want of a quantile-optimal rule with known constants. Künsch's two caveats are stated in the same place: his coefficient is the strong (α-) one, not the β-coefficient of `ass:mix`, and his block count assumes the record divides exactly by the block length, so the `⌈N/ℓ⌉`-with-truncation convention is this chapter's and is not attributed to him. The `\gap{}` at the end of §6.4.1 records that `politis1994` carries no locator at all and that the fixed-block-to-geometric transfer is uncited.

**14. [CITE] Two numerical regulatory facts asserted while the gap box says none is — DONE.**
The "250 trading days" and "99 %" are **removed** from §6.4.3. The traffic-light mechanism is now stated in the words the Highlights note licenses and cited `\citep[\S1, p.~1]{schmitt2026}`, explicitly marked secondary and the only source read; the window length, the confidence level and the exception counts are named as boundary values and asserted nowhere. The gap box is widened to name all four unstated boundary values. Separately, "Table 1 of that paper" in `rem:usd-notscp` now carries its locator, `\citep[Table~1, p.~4]{schmitt2026}`.

### SHOULD

**15. [FIX] F1 cannot distinguish the two hypotheses it claims to separate — DONE.**
`tab:usd-ident-excess` gains the column "Implied `η̂` ratio: median and interquartile range of `η^imp/η̂`", where `η^imp` is the basis volatility that would have made the pair exactly contained. F1 gains the third condition: gross dispersed failure can also be produced by a *biased* rather than stale estimate (a volatility risk premium is a level effect), so F1 fires only if the implied ratio is **not** concentrated near a single constant; if it is, the finding is a level error in `η̂`, is read under F2, and F1 does not fire.

**16. [ADD] Quantify what feasibility costs the route comparison — DONE.**
Recomputed: minimising `g_cal` over `b ≤ 13` gives 0.2040 at b = 13 against 0.1909 at the unconstrained minimiser b = 17, a penalty of **6.9 %**; at N = 1100 and 1700 the feasible ceilings are 61 and 94, above the minimisers 32 and 38, so the constraint does not bind; the two crossings stay at about `2.2 × 10³` and `1.0 × 10⁵`. The closing sentence of §6.5.2 states this and resolves the latent inconsistency by saying that `fig:usd-routes`'s left panel plots the constrained minimisation and marks the unconstrained crossings, which is consistent for exactly that reason.

**17. [CLARIFY] The three record lengths have no date ranges and no stated role — DONE.**
§6.5.2 now opens by saying that in Theorem `thm:block-b` the record length `N` is the calibration record on which a threshold is computed, not a span of data availability, and names each: 2 Jan–31 Dec 2022 (~250, the certificate test's own record); 2 Jan 2019–30 Jun 2023 (~1,100, the longest on which the policy's predecessor fit exists on every date); 2 Apr 2018–31 Dec 2024 (~1,700, reachable only because the certified policy is frozen at the end of `D_fit` and so keeps producing block scores after the predecessor market ends).

**18. [FIX] The V5 truncation changes a pre-registered statistic — DONE.**
§6.2.3 keeps the truncation and adds: truncation is winsorisation, the Pearson correlation of a winsorised series is not the one Chapter 5 pre-registered, so the untruncated correlation is reported in the adjacent column and disagreement between the two is recorded as inconclusive. `tab:usd-ident-rhobf`'s "Pearson ρ" and "Bootstrap p (V5)" rows now carry both.

**19. [FIX] "Seven and a half" is true at two of five block lengths — DONE.**
Recomputed: `1 − k/(n+1)` = 0.0952, 0.0952, 0.0769, 0.0769, 0.1000. §6.3.2 now prints all three values, says the ceiling in `k` moves the effective target "to between seven and a half and ten per cent depending on `b`", and requires the realised frequency to be read against the column beside it rather than against the nominal ten per cent.

**20. [ADD] Two pre-registered quantities have no column — DONE.**
`tab:usd-ident-rhobf` gains (a) "Max median gap (V6): maximum absolute difference between the per-expiry medians", with the note that *stable* needs this below 0.2 **as well as** the IQR — Chapter 5's V6 has both conditions; and (b) "V4 pooled rows: the whole grid, and expiries of three years and longer; the second decides V4", so that the pre-registered denominators are the denominators reported.

**21. [FIX] Six panels for an arm that supports two expiries — DONE.**
`fig:usd-containment` now specifies the exchange figure as **two** panels, at one and two years, and says why: the listed options run on the first eight quarterly contracts and so reach two years, while the policy-date rule removes everything below one year — "the emptiness of the rest is itself the finding".

**22. [CUT-REPETITION] Four passages restating Chapter 5 — DONE, all four.**
(a) §6.2.1 Step 4: the restated `Σ^±` display and the symmetric-interval remark are deleted; Step 4 now opens "The interval … is the one fixed in criterion V1 of Section `sec:ident-validation`, with `η̂(t)` in place of `η`", and carries only the new execution content (item 7).
(b) §6.2.1 Step 3: the `1/√(2N_w)` derivation is cut to "Section `sec:ident-validation` transmits its relative standard error one-for-one to the half-width".
(c) §6.1.3 first paragraph: cut to two sentences with a reference to Chapter 5's "What the test cannot show".
(d) §6.7 closing paragraph: the V3 sentence is replaced by a reference; the other two non-falsifying outcomes are kept, being new here.

**23. [ADD] One sentence on the payment lag — DONE.**
§6.2.1 Step 2 now states that the successor fixing is paid with the two-day backward shift of the administrator's rule book, and dismisses it with the number: under `Q^{T+Δ+δ_p}` the forward acquires a drift equal to minus its covariation with the log numeraire ratio, `δ_p` times the stub forward at first order, so the displacement is at most `α₀σ_stub δ_p (T+Δ) ≤ 0.005` bp at `α₀ = σ_stub = 60` bp, `δ_p ≤ 4` calendar days, `T+Δ = 1.25`, against a quote precision of 0.01 bp. A `\datanote{}` records that `σ_stub` is estimated nowhere in this thesis, that 60 bp is the assumed level, and — since the bound is linear in `σ_stub` — that a doubling brings the displacement to the quote precision itself, so the dismissal is safe only to about that factor.

**24. [FIX] `\Prob` used for an empirical share — DONE.**
The `tab:usd-ident-excess` row is now "Failures above — share of failures above the interval, `#{D>0}/#{D≠0}`". No `\Prob` remains outside its `macros.tex` meaning.

**25. [CLARIFY] C1's first sentence compares a realisation with a bound on an expectation — DONE.**
C1 now opens: "the realised breach frequency `α̂ := M⁻¹ Σ_i 1{S₀^(i) > q̂}` is consistent, by the test below, with the bound `α + ε̂ + (n+1)β̄` **on its expectation**."

**26. [CITE] Extend the two gap boxes, do not multiply — DONE.**
The §6.4.1 box now records that `lahiri2003`'s second-order-accuracy claim at `ℓ ≍ N^{1/3}` is the same unlocated claim Chapter 3 carries and that the two must be closed together, and that `politis1994` carries no locator at all. The §6.4.2 box now records the Highlights note's intended use for `christoffersen1998` — that `LR_ind` presumes a first-order Markov alternative and is asymptotic, hence a diagnostic and never a finite-sample guarantee — as the note's intended use rather than as an assertion with a locator. No new gap box was created.

**27. [CLARIFY] One line that makes the "126" finding sharper — DONE.**
C2 now adds: `β(b) ≤ 1` for every `b` by definition, so at `b = 1` the assumed class delivers exactly the trivial bound and 126 is what 126 copies of a trivial bound sum to. Recomputed both thresholds: for the certified level merely to be **positive** at `b = 1`, `N = 250`, no drift charge, one needs `β(1) ≤ 0.9/126 = 0.0071`; to clear the one half of C2, `β(1) ≤ 0.4/126 = 0.0032`. The chapter prints both, and names the hypothesis it would amount to.

---

## §4 of the report — "Missing for a strong doctoral chapter"

Not numbered, and handled as follows.

- **Power / sizing — DONE in part.** §6.3.2 now carries the sizing arithmetic that needs no data: at `M = 12` against the primary cell's bound 0.28, the one-sided binomial test at 5 % rejects only on seven or more breaches out of twelve (`α̂ ≥ 0.583`) and reaches power one half only against a true breach probability of 0.54; at `M = 25` it rejects on twelve or more (`α̂ ≥ 0.48`) with power one half at 0.46; against the nominal `α = 0.1` the thresholds are 0.333 and 0.240. All four computed by exact binomial enumeration. The chapter states the consequence: the test detects catastrophic failure and nothing milder, and a pass reads as the absence of catastrophe rather than as confirmation.
  **DEFERRED to round 2:** the full per-criterion sizing *table* (independent-equivalent observations after the block-bootstrap correction, and the smallest detectable departure, for each of V1–V6, C1–C5, R1–R3). `M_P` for the identification criteria cannot be known before the strict arm's length is known, and drafting a table of numbers that do not exist would put invented figures in the thesis — the ch4 round-1 lesson on deferring rather than drafting a requested computation. It also has no page room in this round (see below).
- **Null model for containment — DEFERRED to round 2 (Chapter 6).** The proposal (the containment rate an interval of the same width centred on the naive mark would achieve) is sound, costs no extra data and would turn V1 from an absolute threshold into a comparison. It is not added now because V1's threshold is pre-registered in Chapter 5 and a benchmark rate reported beside it must be specified as an addition to, not a modification of, V1 — that specification belongs with the round-2 sizing work, and the chapter has no page budget for it this round.
- **Pre-committed order of operations — DONE.** §6.2.3 gains the paragraph "Order of operations": strict arm before exchange arm; pooled row before per-expiry rows; the primary cell `(10,1,2,0.05)` before the rest of the grid; the falsification rules read before any verdict is written.
- **What to do if the terminal export is refused — DONE.** Folded into F10 rather than given a subsection: the predecessor volatility strip is the one refusal that stops the first half; since `def:usd-policy` fits that same strip on every date, the certificate test does not survive the refusal either, and what survives is the block-layout and deficit arithmetic, which uses no market data. The chapter would report that alone and say so.

## §5 of the report — "Should go"

All three smaller redundancies cut: §6.1.4's map is reduced to a single sentence; §6.4.1's "What can be said is this" paragraph is cut to one clause (the point now stands in §6.9.3, which the report judged the best-written version); §6.8.3's "every remedy available …" list is reduced to one clause plus the Appendix C reference. Item 22's four passages are cut as listed above.

## §6 of the report — direct edits made by the panel

Both verified on disk and **retained**: `\hat\pi := (n_{01}+n_{11})/(n_{00}+n_{01}+n_{10}+n_{11})` in §6.4.2, and "about twice the certificate's `n`" in §6.4.1. Both are correct (at b = 10, N = 250: `n' = 25`, `n = 12`), and neither was reverted.

---

## New `\gap{}` boxes

**None.** The chapter carries seven gap boxes, the same seven as before the revision. Four were **extended in scope**, as item 26 directed ("extend, do not multiply"):

1. §6.2.2, the four window dates — rewritten to state exactly what rests on each date, and the mitigation (item 5).
2. §6.4.1, `lahiri2003` locator — extended to record the shared unlocated claim with Chapter 3, that `politis1994` carries no locator at all, and that the fixed-block-to-geometric transfer is uncited (items 13, 26).
3. §6.4.2, `kupiec1995` / `christoffersen1998` locators — extended with the `LR_ind` Markov-and-asymptotic caveat, stated as intended use (item 26).
4. §6.4.3, `bcbs2019` locators — extended to name all four unstated numerical boundary values, the backtest window length and confidence level among them (item 14).

Unchanged: the scheduled-policy-date jump box (§6.2.3), the listed-contract-specification box (§6.2.3), and the derived-surface / `ass:mix` box (§6.3.1, reworded only to use the new two-leg language of item 3).

## Word count and page count

| | before | after |
|---|---|---|
| Source words (`wc -w`) | 12,927 | 14,567 |
| Typeset pages (tectonic, full build) | 38 (pp. 199–236) | **40** (pp. 191–230) |
| Budget | 40 | 40 |

Measured against a real build of `main.tex`, not a words-per-page proxy: Chapter 7 now opens on p. 231, so there is no blank filler page inside the span. The chapter is **on budget at exactly 40 pages**.

Getting there required more compression than the report anticipated. The report's own estimate was that item 22 plus §5 would free about three pages and that items 1, 3, 4, 9, 10 and 12 would consume roughly the same; in the event the named cuts free about 1.3 pages of source while the must-items cost about 5.5, so a further 1,100 words of concision editing was done across §6.1, §6.2.2, §6.2.4 (the six figure plans), §6.3, §6.4, §6.5, §6.7, §6.8 and §6.9. Those edits removed no rule, no threshold, no number and no citation; they removed restatement and adjectives only. The two round-2 deferrals above are recorded partly because there is no page room for them in this round.

Build check: full `tectonic main.tex` run, no errors; the only undefined reference in the manuscript is `sec:zar-frequency-need`, which belongs to Chapter 7. All new cross-references resolve: `eq:ident-homotopy`, `eq:ident-alpharange`, `rem:sequence`, `sec:ident-example`, `thm:ident-two`, `tab:usd-ident-excess`, `tab:appC-seeds`. No bibliography key was added; the two new citations (`kunsch1989` Cor. 3.1 p. 1226; `schmitt2026` §1 p. 1 and Table 1 p. 4) use locators already recorded in the Highlights notes.
