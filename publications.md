# Publication strategy

Prepared 2026-09-09 by thesis-publication-strategist. Governing documents: `~/PhD-Topic-Council/13-mathematics-3yr.tex` (36-month plan, ground truth for theorem numbering), STANDARD.md "Wits administration (verified)", LESSONS.md (scout-literature and scout-wits-admin entries of 2026-09-09). Theorem numbers below are the ground-truth numbers: Thm 3 identifiability, Thm 4 two models, Thm 6 coverage, Prop 7 W1 bound, Thm 8 sharpness, Thm 9 optimal blocking and minimax.

## 1. The Wits constraint

- FSO §10.5 and First Submission form V4.2 item 5: at least one publication **or one submitted manuscript** covering the PhD work is a requirement for qualification. Waiver only by supervisor motivation at Head-of-School discretion. Plan so that the waiver is never needed.
- "Submitted" is sufficient. A manuscript under review at month 36 satisfies the rule; a manuscript rejected and not yet resubmitted does not. Keep the journal submission acknowledgement and an arXiv identifier as evidence for the form.
- Back-plan from first submission T = month 36: intention-to-submit and examiner nomination at T-3 = month 33 (the form lists "Publications" among first-submission requirements, so the publication status is declared at month 33, not 36).
- FSO §10.6, §10.8; Senate Rule 3.4.3.2: if a paper is co-authored, the thesis declaration carries a per-author contribution statement and the thesis remains one coherent argument. Write the contribution statement at the time of submission of each paper, not at month 36.
- Venues: FSO §10.7 recommends ISI or DHET-accredited journals. EJS, Bernoulli and Quantitative Finance are Web of Science-indexed; confirm against the current DHET accredited list before the intention form.

## 2. Paper 1 (doctoral paper, statistics)

**Source chapters.** ch:certification (Thm 6, Prop 7), ch:sharpness (Thm 8, Thm 9), the statistics part of ch:usd (certificate test with optimal blocking).

**Target.** Bernoulli if the minimax lower bound (Thm 9(ii), restated) is proved, at least up to a logarithmic factor. Electronic Journal of Statistics if only the upper bound and the conditional certificate are proved by month 18 (EJS publishes methodology with theory; a design result without a lower bound belongs there, not in Bernoulli). Decision at gate G2 (month 16), see Section 4.

**Positioning against the four papers that exist.**

| Prior work | What it already has | What Paper 1 may not claim | What Paper 1 adds |
|---|---|---|---|
| Oliveira et al. (2024) `oliveira2024` | Blocked split conformal under mixing; marginal coverage with coupling cost | Blocking as a device; marginal validity under beta-mixing | Calibration-conditional (Beta-law) statement under beta-mixing with drift; sharpness; optimal block length for the conditional deficit |
| Barber et al. (2023) `barber2023` | Weighted conformal beyond exchangeability, coverage loss in TV between weighted laws | Any "first coverage bound under non-exchangeability" language | A fixed-policy, blocked, finite-sample certificate whose penalty is Kolmogorov (half-lines only), shown sharp with constant 1 |
| Barber and Pananjady (2026) `barber2026` | Marginal coverage for split conformal on stationary beta-mixing data **without blocking**, deficit of order N^{-r/(r+1)} over B_r, tight up to (1-alpha)/4 for split conformal; Discussion leaves open whether any method using knowledge of the mixing class can do better | Thm 6(i) as a contribution; Thm 9 as a marginal minimax rate (their bound is strictly faster than N^{-r/(2r+3)}) | The calibration-conditional deficit at confidence 1-delta, where the sqrt(b/N) term is real; a lower bound over all threshold procedures on B_r for that deficit answers their open question |
| Halkiewicz (2026) `halkiewicz2026` | Coverage-error decomposition + optimal calibration window + Le Cam two-point lower bound "for every conformal prediction procedure", over Hoelder-beta locally stationary alpha-mixing processes; hardness is drift-driven | "First optimal-design result for conformal under dependence" | Hardness driven by mixing, not drift; beta-mixing class B_r; blocking; conditional coverage; finite-sample constants |

Also cite, in the related-work section: Ramos et al. (2026) `ramos2026` for the transport identity D = h(U_(k)) that puts the Kolmogorov drift penalty in print (their Prop. 13) and their Berry-Esseen route to the Beta law (asymptotic), contrasted with the non-asymptotic Berbee route of Thm 6(ii); Zwart (2025) `zwart2025` and Vovk (2012) `vovk2012` for operational use of the Beta(k, n+1-k) quantile under exchangeability (the "2.3 times tighter than DKW" remark is not new); Zheng and Proutiere (2024) `zheng2024` and Allohibi (2026) `allohibi2026` as the other gapped or thinned schemes, neither of which optimises block length or proves a lower bound; Gibbs et al. (2025) `gibbs2025` for conditional guarantees under exchangeability.

**Headline theorem.** The calibration-conditional minimax question, i.e. Theorem 9 restated for the conditional deficit: over B_r = {beta(k) <= C k^{-r}}, what is the smallest deficit in calibration-conditional coverage at confidence 1-delta that any threshold procedure built from N calibration periods can certify, and does the blocked split-conformal quantile with b* attain it? The restated optimal-blocking upper bound (Thm 9(i)) is a supporting proposition, not the headline: as an upper bound alone it is the Halkiewicz template with a different class, and as a marginal statement it is beaten by Barber and Pananjady.

Restated form to be proved (from LESSONS, scout-literature 2026-09-09; not yet confirmed by the statistician, ch4 not yet drafted):

```
E_delta(b, N)  asymp  sqrt(b log(1/delta) / N)  +  N b^{-(r+1)}        [from Thm 6(ii), n asymp N/(2b)]
b*  asymp  N^{3/(2r+3)},   E_delta(b*, N)  asymp  N^{-r/(2r+3)}          [quote the exponent, never the bare balance number]
```

\gap{Ground truth (13-mathematics-3yr.tex, Thm 9) still states (ii) for the MARGINAL deficit "by Theorem 6(i)". Barber and Pananjady (2026, Cor. 1-2) achieve marginal deficit of order N^{-r/(r+1)} without blocking, so the marginal minimax claim at N^{-r/(2r+3)} is false. Paper 1 is planned on the conditional restatement. The ground-truth file must be corrected by the statistician before ch4 is drafted; until then this plan cites the LESSONS restatement.}

\gap{Open question that decides the headline, to be settled by the statistician and thesis-adversary-thm9 at gate G1 (month 12): the i.i.d. subclass lies in B_r, so the minimax conditional deficit over B_r is at least of order sqrt(log(1/delta)/N). For r > 1 the series sum_k beta(k) converges, so covariances of the indicators 1{S_i <= x} are summable; an unblocked empirical-process bound under beta-mixing may then give a conditional deficit of order N^{-1/2} up to logarithms, in which case blocking is suboptimal for the conditional deficit as well and the lower bound at N^{-r/(2r+3)} is false. If that is so, the honest headline becomes: exact minimax conditional rate over B_r, with a finite-sample certificate attaining it, and the price of blocking quantified. Either answer to the Barber-Pananjady open question is publishable; asserting the blocked rate as minimax without checking this is not.}

**Contents (in order).**

1. Introduction: fixed hedging policy, hedging-error scores as a beta-mixing time series, calibration law P and deployment law Q. State the finance application in one paragraph; the paper is a time-series predictive-inference paper for a statistics readership.
2. Related work: the table above, written as prose, with locators.
3. Certificate (from ch:certification). Thm 6(ii) conditional Beta-law statement under beta-mixing via Berbee coupling, cost (n+1)beta(b), deployment block gap-separated; Thm 6(iii) drift penalty d_K applied after coupling. Thm 6(i) as a corollary with a remark that `barber2026` gives the marginal statement without blocking and with better constants. Prop 7: F_P - F_Q <= sqrt(2 L W_1), with the counterexample showing L W_1 is false.
4. Sharpness (from ch:sharpness). Thm 8: bottom-epsilon mass of P moved to a far point M attains constant 1 on d_K; explicit statement that the (1-eps)P + eps delta_M mixture only gives (1-eps)(1-alpha). Contrast with `ramos2026` Prop. 13 (same object, no attained constant).
5. Optimal blocking and minimax (from ch:sharpness). Thm 9(i) restated for the conditional deficit; Thm 9(ii) lower bound over B_r (hidden-regime construction, Assouad or two-point on the regime label); contrast with `halkiewicz2026` on the source of hardness. Thm 9(iii) dependent empirical W_1 only if proved by month 18; otherwise thesis-only.
6. Numerical work. Primary, reproducible example: the Gaussian AR(1) of ch:certification (phi = 0.5, N = 500, b = 10, alpha = 0.1, delta = 0.05; quote the recorded figures from thesis/code/certify, do not recompute). Do not present the AR(1) example as an illustration of b*; the polynomial-class curve is the right object only over B_r. Secondary, illustrative: the USD certificate test from ch:usd, reporting k/(n+1) beside 1-alpha, with the stationary block bootstrap shown as a point estimate of the P-quantile, never as a competitor bound and never as a theorem. Because there is no public USD LIBOR option surface or fixing history, the USD section publishes aggregates only and the code reads a user-supplied CSV; say so in the reproducibility statement.
7. Discussion: beta(b) is not estimable (Adams-Nobel); the certificate is conditional on an assumed class B_r.

**Acceptance conditions.** Given the four prior papers, Paper 1 is acceptable at Bernoulli only if (a) the lower bound in Section 5 is proved over B_r (a log factor or a slightly smaller class is acceptable and must be stated), (b) Thm 6(i) is not sold as new, (c) the Beta-law route is explicitly contrasted with `ramos2026`, and (d) Halkiewicz is cited and the mixing-versus-drift distinction is made in the introduction. Without (a) the paper is an EJS methodology paper carrying Thm 6(ii)-(iii), Thm 8, Thm 9(i).

**Authorship.** Candidate first author. Co-authors per supervision agreement; contribution statement drafted at submission (FSO §10.8).

## 3. Paper 2 (finance)

**Source chapters.** ch:identifiability (Thm 3, Thm 4, parameter-count remark), the finance part of ch:usd (USD identifiability validation). Lemma 1 and Prop 2 from ch:prelim are stated and cited, not claimed.

**Target.** Quantitative Finance.

**Headline.** Theorem 3: the successor at-the-money normal volatility is identified from the observable set S = {IBOR smile, B_0, s} only within an interval of half-width eta; nu and the map Phi_0 (strike shift by s + B_0, then the time change of Lemma 1) are identified; (eta rho_BF, eta rho_Balpha) are not identified at O(epsilon). Theorem 4: the two-model construction M_pm, matching every IBOR caplet to O(epsilon^2) and B_0 exactly, with compounded-rate ATM volatilities differing by 2 v_1 and skews by 2 v_2 nu at every strike.

**Positioning.** Willems (2020) `willems2020`, Lyashenko and Mercurio (2019, 2020) `lyashenko2019` `lyashenko2020` and Piterbarg (2020) `piterbarg2020` give the compounded-rate caplet and the fallback mechanics; none states an identifiability result for the successor smile. The scout found no 2025-2026 paper on identifiability of successor-rate smiles or smile transport through fallbacks as of 2026-09-09; write "no evidence found as of <date>" and re-run the scan in the month before submission. Alfeus (2026) `alfeus2026` models the JIBAR-ZARONIA spread and contains no option content; cite for the ZAR basis, not for smiles.

**Contents (in order).**

1. Setting: both caplets priced under Q^{T+Delta}; L = F + B + s; no convexity term (correction 1, never undone). SABR with deterministic decay g, clock tau, Assumption of linear decay stated once as an assumption with c_g in (0,1) for the general case.
2. Lemma 1 (cited, `willems2020`, `lyashenko2019`) and Prop 2 (which vol-of-vol variant the empirical work uses; the two variants differ by about 0.002 bp on the smile under HLW weighting, per LESSONS code-multicurve).
3. Theorem 3 with the O(epsilon) expansion and its error bound; the failure mode (basis mean reversion gives half-width eta h(kappa T)) stated as a remark.
4. Theorem 4 with the nonsingular-Jacobian proof; parameter-count remark (deficit 3, two at O(epsilon)).
5. USD validation. Fit SABR to the USD LIBOR smile on 2019-2021; predict the SOFR smile by strike shift s = 26.161 bp (Reg ZZ 12 CFR 253.4(c)) plus B_0 and the time change; estimate eta from the realised basis (fixing minus compounded SOFR minus s) over 2019 to mid-2022 only, because the quoted basis compresses mechanically toward s in the last year before 30 June 2023; compare the predicted ATM band of half-width eta with the observed SOFR ATM volatility, starting from the first month the vendor marks the SOFR surface as quoted rather than derived. Publish only aggregates (fitted triples, ATM and skew differences in bp, monthly averages); vendor surfaces are not redistributable.
6. Discussion: what the two-model construction means for a hedger (reserve of width 2 eta on ATM volatility), and what historical basis data can and cannot pin down (physical-measure estimate versus pricing measure).

**Not in Paper 2.** Prop 5 tenor consistency (thesis appendix; at most a remark). The South African converted book (a practitioner note to the SARB Market Practitioners Group per the 36-month plan, not a journal paper).

## 4. Timeline (month-indexed, month 1 = registration)

Consistent with the 36-month table in 13-mathematics-3yr.tex; additions are marked (new).

| Month | Publication action | Gate or evidence |
|---|---|---|
| 1-4 | Reading report. Add to the plan's list: `barber2026`, `halkiewicz2026`, `ramos2026`, `zheng2024`, `allohibi2026`, `zwart2025` (new). | Related-work table of Paper 1 drafted from the reading report |
| 5 | Thm 8 proved. | Section 4 of Paper 1 drafted |
| 10 | Thm 6 proved (Beta form, drift). | Section 3 of Paper 1 drafted |
| 9-11 | Proposal approval (plan). Note: the PhD Mathematical Statistics course page says three months; confirm the School's deadline. | Faculty approval |
| 12 | Thm 9(i) upper bound in the conditional restatement. **G1 (new):** statistician and thesis-adversary-thm9 rule on the unblocked N^{-1/2} question above. Outcome fixes the headline and the target journal. | Written decision in LESSONS |
| 16 | Lower-bound construction. **G2:** proved (possibly up to log) -> Bernoulli; not proved -> EJS with Thm 6(ii)-(iii), Thm 8, Thm 9(i). | Decision recorded |
| 17 | USD certificate test complete. | Section 6 of Paper 1 |
| 18 | Thm 9 done (dependent W_1 in or out). | Paper 1 full draft begins |
| 18-22 | Paper 1 written, internal review by the council statistics reviewers, supervisor sign-off. | |
| 22 | **Paper 1 submitted** (EJS or Bernoulli) and posted to arXiv the same week. Wits requirement satisfied from this date. Contribution statement drafted. | Submission acknowledgement + arXiv id filed |
| 20-24 | USD identifiability validation. | Section 5 of Paper 2 |
| 24-28 | Paper 2 written; re-run literature scan for successor-smile identifiability (new). | |
| 28 | **Paper 2 submitted** (Quantitative Finance) and posted to arXiv. Second submitted manuscript on file. | Acknowledgement + arXiv id filed |
| 26-30 | ZAR coda; optional practitioner note to the MPG (not a journal paper). | |
| 30-32 | Planning assumption (new): first decision on Paper 1 not before month 30. Referee reports absorbed into ch:certification and ch:sharpness so thesis and paper stay one argument (FSO §10.6). | |
| 33 | Intention-to-submit form and examiner nomination (T-3). Publication status declared: Paper 1 (under review / revised / accepted), Paper 2 (under review). | Forms lodged |
| 34 | Complete draft. Status check on both papers; fallback branch below if needed. | |
| 36 | First submission with publication details or acknowledgements attached. | |
| 36 + 6 weeks | Examiner reports; revisions within three months fee-free. | |

## 5. Fallback if Paper 1 is still under review at month 34

- **Under review, no decision:** no action needed for the Faculty rule. Attach the journal acknowledgement, arXiv identifier and Paper 2's acknowledgement to the first-submission package. The thesis chapters already contain the full proofs, so examination does not wait on the referees.
- **Rejected between month 22 and month 33:** resubmit to the fallback venue within four weeks so that the status is "submitted" when the intention form goes in at month 33. Fallback venue order: if rejected at Bernoulli, resubmit to EJS; if rejected at EJS, split is not needed, resubmit the same manuscript to a time-series or methodology journal chosen with the supervisor. Incorporate the referee reports into ch:certification and ch:sharpness before month 34; a rejection with substantive reports strengthens the thesis chapters and is not a loss for the Wits rule.
- **Rejected after month 33 and before month 36:** Paper 2 (submitted month 28) is the qualifying submitted manuscript; resubmit Paper 1 in parallel; update the publication details at first submission.
- **Both papers rejected and not resubmitted at month 36:** supervisor motivation letter to the Head of School (FSO §10.5). Do not plan on this branch.
- **Paper 1 not submittable by month 22** (Thm 9 lower bound unresolved at month 18): submit the EJS version (Thm 6(ii)-(iii), Thm 8, Thm 9(i) restated) by month 22 regardless; the lower bound, if proved later, goes into the thesis (ch:sharpness) and a short follow-up note, not into a delay of Paper 1. The Wits rule is met by the submission, not by the strength of the headline.

## 6. Open items

1. Statistician to correct Thm 9 in 13-mathematics-3yr.tex to the conditional form and to rule on the unblocked N^{-1/2} question (gate G1). Paper 1's headline depends on it.
2. Supervisor liaison to confirm the School's proposal deadline (three months per course page vs months 9-11 in the plan) and any seminar defence; this does not move the paper dates but does move month 9-11 items.
3. Supervisor liaison to confirm co-authorship and author order for both papers so that the FSO §10.8 contribution statement can be drafted at month 22.
4. Confirm the three target journals against the current DHET accredited journal list before month 33.
5. Data engineer USD to confirm the first month at which the vendor marks the SOFR surface as quoted; Paper 2's validation window starts there.
