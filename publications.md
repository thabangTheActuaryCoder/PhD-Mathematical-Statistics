# Publication strategy

Prepared 2026-09-09 by thesis-publication-strategist. Governing documents: `~/PhD-Topic-Council/13-mathematics-3yr.tex` (third version; 36-month plan; ground truth for theorem numbering), STANDARD.md "Wits administration (verified)", LESSONS.md (scout-literature, scout-wits-admin and statistician entries of 2026-09-09). Theorem numbers are the ground-truth numbers: Thm 3 identifiability, Thm 4 two models, Thm 6 coverage, Prop 7 W1 bound, Thm 8 sharpness, Thm 9 calibration-conditional coverage error over B_r (parts (i) optimal b, (ii) not-minimax, (iii) mixing-driven lower bound, (iv) partially observed drift, (v) dependent W1).

## 1. The Wits constraint

- FSO §10.5 and First Submission form V4.2 item 5: at least one publication **or one submitted manuscript** covering the PhD work is a requirement for qualification. Waiver only by supervisor motivation at Head-of-School discretion. Plan so that the waiver is never needed.
- "Submitted" is sufficient. A manuscript under review at month 36 satisfies the rule; a manuscript rejected and not yet resubmitted does not. Keep the journal submission acknowledgement and an arXiv identifier as evidence for the form.
- Back-plan from first submission T = month 36: intention-to-submit and examiner nomination at T-3 = month 33. The intention form lists "Publications" among first-submission requirements, so publication status is declared at month 33, not 36.
- FSO §10.6, §10.8; Senate Rule 3.4.3.2: a co-authored paper needs a per-author contribution statement in the thesis declaration, and the thesis remains one coherent argument. Write the contribution statement when each paper is submitted, not at month 36.
- Venues: FSO §10.7 recommends ISI or DHET-accredited journals. EJS, Bernoulli and Quantitative Finance are Web of Science-indexed; confirm against the current DHET accredited list before the intention form.

## 2. Paper 1 (doctoral paper, statistics)

**Source chapters.** ch:certification (Thm 6, Prop 7), ch:sharpness (Thm 8, Thm 9), the statistics part of ch:usd (certificate test with the blocked route at b*).

**Target.** Bernoulli if Thm 9(iii) is proved over all threshold procedures (a logarithmic factor, or restriction to the regime-renewal subclass of B_r, is acceptable and must be stated; the delta-dependence g_r may be left open and stated as open). Electronic Journal of Statistics if by month 18 the lower bound holds only for the sample quantile and the two-point reduction over all procedures is missing: the paper is then a methodology paper (conditional certificate, sharpness, the not-minimax accounting, optimal b for the blocked route) and EJS is the right home. Decision at gate G2 (month 16), Section 4.

**Positioning against the four papers that exist.**

| Prior work | What it already has | What Paper 1 may not claim | What Paper 1 adds |
|---|---|---|---|
| Oliveira et al. (2024) `oliveira2024` | Blocked split conformal under mixing; marginal coverage with coupling cost | Blocking as a device; marginal validity under beta-mixing | Calibration-conditional Beta-law certificate under beta-mixing with drift; sharp constant on the drift penalty; the exact accounting of what blocking buys and costs |
| Barber et al. (2023) `barber2023` | Weighted conformal beyond exchangeability; coverage loss in TV between weighted laws | Any "first coverage bound under non-exchangeability" language | A fixed-policy, finite-sample certificate whose penalty is Kolmogorov (half-lines only), shown sharp with constant 1 |
| Barber and Pananjady (2026) `barber2026` | Marginal coverage for split conformal on stationary beta-mixing data without blocking, deficit of order N^{-r/(r+1)} over B_r, tight up to (1-alpha)/4 for split conformal (their Thm 2 is a lower bound for split conformal only); Discussion asks whether any method using knowledge of the mixing class can do better | Thm 6(i) as a contribution; any minimax claim for the blocked rate N^{-r/(2r+3)}; any marginal minimax claim (left to them) | The two-sided calibration-conditional coverage error at confidence delta over B_r: fixed-delta rate (N delta)^{-1/2} (Thm 9(ii)), mixing-driven lower bound (N^r delta)^{-1/(r+1)} over all threshold procedures (Thm 9(iii)); this answers the conditional analogue of their open question |
| Halkiewicz (2026) `halkiewicz2026` | Coverage-error decomposition + optimal calibration window + Le Cam lower bound "for every conformal prediction procedure" over Hoelder locally stationary alpha-mixing processes; hardness is drift-driven | "First optimal-design result for conformal under dependence" | Hardness driven by the mixing exponent r, not by drift; a beta-mixing class B_r; conditional coverage at confidence delta; finite-sample constants |

Also cite in related work: Ramos et al. (2026) `ramos2026` for the transport identity D = h(U_(k)) (their Prop. 13, the Kolmogorov drift penalty in print) and their asymptotic Berry-Esseen route to the Beta law, contrasted with the non-asymptotic Berbee route of Thm 6(ii); Zwart (2025) `zwart2025` and Vovk (2012) `vovk2012` for operational use of the Beta(k, n+1-k) quantile under exchangeability; Zheng and Proutiere (2024) `zheng2024` and Allohibi (2026) `allohibi2026` as the other gapped or thinned schemes, neither optimising block length nor proving a lower bound; Gibbs et al. (2025) `gibbs2025` for conditional guarantees under exchangeability; Dedecker and Merlevede (2017) `dedecker2017` for the dependent empirical W1 rate.

**Headline theorem.** The conditional-coverage minimax question, i.e. Thm 9(iii) with its partner (ii): over B_r, the two-sided calibration-conditional coverage error |F_P(T) - (1-alpha)| at confidence delta has fixed-delta minimax rate (N delta)^{-1/2}, attained by the unblocked sample quantile, and a mixing-driven lower bound (N^r delta)^{-1/(r+1)} that binds when delta < N^{-(r-1)/2}, with the Fuk-Nagaev upper bound (Rio 2017, Ch. 6) as its partner. The restated optimal-blocking result (Thm 9(i), exact minimiser b* = (2(r+1))^{2/(2r+3)} N^{3/(2r+3)} for the expected conditional shortfall sqrt(b/N) + N b^{-(r+1)} from Thm 6(ii)) is supporting, not the headline: it is elementary, it is the Halkiewicz template with a different class, and the rate it delivers is not minimax in any formulation. Correction 9 of GROUND-TRUTH applies verbatim in the paper: blocking buys the exact Beta law and a certificate whose only dependence on (C, r) is (n+1) beta(b); it does not buy rate.

**Contents (in order).**

1. Introduction: fixed hedging policy, hedging-error scores as a beta-mixing time series, calibration law P and deployment law Q. The finance application in one paragraph; this is a time-series predictive-inference paper for a statistics readership.
2. Related work: the table above as prose, with locators, and the honest statement that this is not the first optimal-design result for conformal under dependence.
3. Certificate (from ch:certification). Thm 6(ii): conditional Beta-law statement under beta-mixing via Berbee coupling, cost (n+1) beta(b), deployment block gap-separated, disintegrated beta coefficient and Markov for the conditional form (which is why beta- not alpha-mixing is the hypothesis); Thm 6(iii): drift penalty d_K applied after coupling, with d_K the realised d_K(P_pi, Q_pi). Thm 6(i) as a corollary, with a remark that `barber2026` gives the marginal statement without blocking and with better constants. Prop 7: F_P - F_Q <= sqrt(2 L W1), the counterexample delta_0 vs U[0, 1/L] showing L W1 is false and sqrt(2) sharp. Report exact Beta quantiles in every number; the "about 2.3 times tighter than DKW" remark is asymptotic and is stated as such.
4. Sharpness (from ch:sharpness). Thm 8: bottom-epsilon mass of P moved to a far point M attains constant 1 on d_K; the mixture (1-eps)P + eps delta_M only gives (1-eps)(1-alpha). Contrast with `ramos2026` Prop. 13 (same object, no attained constant).
5. Coverage error over B_r (from ch:sharpness). Thm 9(i) exact minimiser and value; Thm 9(ii) not-minimax via |Cov(1{S_0 <= x}, 1{S_k <= x})| <= beta(k), Var F_N(x) <= (1/4 + 2 C zeta(r))/N, Chebyshev, and the i.i.d. two-point lower bound N^{-1/2}; Thm 9(iii) regime-renewal construction and the two-point reduction over all procedures, Fuk-Nagaev upper bound, g_r stated as open. Thm 9(iv) (partially observed drift, Le Cam on the deployment sample) only if proved by month 18; otherwise thesis-only. Thm 9(v) appears as one remark citing `dedecker2017`; it is not claimed.
6. Numerical work. Primary, reproducible: the Gaussian AR(1) of ch:certification (phi = 0.5, N = 500, b = 10, alpha = 0.1, delta = 0.05; quote the recorded figures from thesis/code/certify, do not recompute). Do not present the AR(1) example as an illustration of b*; geometric mixing lies in every B_r and the minimiser depends on r. Secondary, illustrative: the USD certificate test from ch:usd, reporting k/(n+1) beside 1-alpha, with the stationary block bootstrap shown as a point estimate of the P-quantile, never as a competitor bound and never as a theorem. There is no public USD LIBOR option surface or fixing history, so the USD section publishes aggregates only and the code reads a user-supplied CSV; the reproducibility statement says so.
7. Discussion: beta(b) is not estimable (explicit copy-with-refresh construction from ch:certification; Adams and Nobel `adams2010` cited only for VC convergence under ergodic sampling); the certificate is conditional on an assumed class B_r; what a model-risk certificate needs is the high-confidence regime where mixing binds.

**Acceptance conditions.** Given the four prior papers, Paper 1 is acceptable at Bernoulli only if (a) Thm 9(iii) is proved over all threshold procedures, with any log factor or subclass restriction stated, (b) Thm 6(i) is not sold as new and the blocked rate is never called minimax, (c) the Beta-law route is contrasted with `ramos2026`, and (d) Halkiewicz is cited and the mixing-versus-drift distinction is made in the introduction. Without (a) the paper is an EJS methodology paper carrying Thm 6(ii)-(iii), Prop 7, Thm 8, Thm 9(i)-(ii).

**Authorship.** Candidate first author. Co-authors per supervision agreement; contribution statement drafted at submission (FSO §10.8).

## 3. Paper 2 (finance)

**Source chapters.** ch:identifiability (Thm 3, Thm 4, parameter-count remark), the finance part of ch:usd (USD identifiability validation). Lemma 1 and Prop 2 from ch:prelim are stated and cited, not claimed.

**Target.** Quantitative Finance.

**Headline.** Theorem 3: the successor at-the-money normal volatility is identified from the observable set S = {IBOR smile, B_0, s} only within an interval of half-width eta; nu and the map Phi_0 (strike shift by s + B_0, then the time change of Lemma 1) are identified; (eta rho_BF, eta rho_Balpha) are not identified at O(epsilon). Theorem 4: the two-model construction M_pm, matching every IBOR caplet to O(epsilon^2) and B_0 exactly, with compounded-rate ATM volatilities differing by 2 v_1 and skews by 2 v_2 nu at every strike.

**Positioning.** Willems (2020) `willems2020`, Lyashenko and Mercurio (2019, 2020) `lyashenko2019` `lyashenko2020` and Piterbarg (2020) `piterbarg2020` give the compounded-rate caplet and the fallback mechanics; none states an identifiability result for the successor smile. The scout found no 2025-2026 paper on identifiability of successor-rate smiles or smile transport through fallbacks as of 2026-09-09; write "no evidence found as of <date>" and re-run the scan in the month before submission. Alfeus (2026) `alfeus2026` models the JIBAR-ZARONIA spread and contains no option content; cite for the ZAR basis, not for smiles.

**Contents (in order).**

1. Setting: both caplets priced under Q^{T+Delta}; L = F + B + s; no convexity term (correction 1, never undone). SABR with deterministic decay g and clock tau; linear decay stated once as an assumption with c_g in (0,1) in general.
2. Lemma 1 (cited, `willems2020`, `lyashenko2019`) and Prop 2 (which vol-of-vol variant the empirical work uses; the two variants differ by about 0.002 bp on the smile under HLW weighting, per LESSONS code-multicurve).
3. Theorem 3 with the O(epsilon) expansion and its error bound; the failure mode (basis mean reversion gives half-width eta h(kappa T)) as a remark.
4. Theorem 4 with the nonsingular-Jacobian proof; parameter-count remark (deficit 3, two at O(epsilon)).
5. USD validation. Fit SABR to the USD LIBOR smile on 2019-2021; predict the SOFR smile by strike shift s = 26.161 bp (Reg ZZ 12 CFR 253.4(c)) plus B_0 and the time change; estimate eta from the realised basis (fixing minus compounded SOFR minus s) over 2019 to mid-2022 only, because the quoted basis compresses mechanically toward s in the last year before 30 June 2023; compare the predicted ATM band of half-width eta with the observed SOFR ATM volatility from the first month the vendor marks the SOFR surface as quoted rather than derived. Publish aggregates only (fitted triples, ATM and skew differences in bp, monthly averages); vendor surfaces are not redistributable.
6. Discussion: what the two-model construction means for a hedger (reserve of width 2 eta on ATM volatility); what historical basis data can and cannot pin down (physical-measure estimate versus pricing measure).

**Not in Paper 2.** Prop 5 tenor consistency (thesis appendix; at most a remark). The South African converted book (a practitioner note to the SARB Market Practitioners Group per the 36-month plan, not a journal paper).

## 4. Timeline (month-indexed, month 1 = registration)

Consistent with the 36-month table in 13-mathematics-3yr.tex (third version); additions are marked (new).

| Month | Publication action | Gate or evidence |
|---|---|---|
| 1-4 | Reading report. Add to the plan's list: `barber2026`, `halkiewicz2026`, `ramos2026`, `zheng2024`, `allohibi2026`, `zwart2025`, `dedecker2017`, Rio (2017) (new). | Related-work table of Paper 1 drafted from the reading report |
| 5 | Thm 8 proved. | Section 4 of Paper 1 drafted |
| 10 | Thm 6 proved (Beta form, drift). | Section 3 of Paper 1 drafted |
| 9-11 | Proposal approval (plan). The PhD Mathematical Statistics course page says three months; confirm the School's deadline. | Faculty approval |
| 12 | Thm 9(i)-(ii) proved (elementary; cannot fail). | Section 5 of Paper 1, first half |
| 16 | Thm 9(iii) regime-renewal lower bound. **G2:** proved over all procedures (log factor or subclass acceptable, stated) -> Bernoulli; sample-quantile only -> EJS. | Decision recorded in LESSONS |
| 17 | USD certificate test complete. | Section 6 of Paper 1 |
| 18 | Fuk-Nagaev upper bound; Thm 9(iv)-(v). **G3 (new):** (iv) in the paper only if proved; (v) a remark either way. | Paper 1 full draft begins |
| 18-22 | Paper 1 written; council statistics panel review; supervisor sign-off. | |
| 22 | **Paper 1 submitted** (Bernoulli or EJS) and posted to arXiv the same week. Wits requirement satisfied from this date. Contribution statement drafted. | Submission acknowledgement + arXiv id filed |
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

- **Under review, no decision:** no action needed for the Faculty rule. Attach the journal acknowledgement, arXiv identifier and Paper 2's acknowledgement to the first-submission package. The thesis chapters contain the full proofs, so examination does not wait on the referees.
- **Rejected between month 22 and month 33:** resubmit within four weeks so that the status is "submitted" when the intention form goes in at month 33. Order: Bernoulli -> EJS -> a time-series or methodology journal chosen with the supervisor; the manuscript is not split. Incorporate the referee reports into ch:certification and ch:sharpness before month 34; a rejection with substantive reports strengthens the chapters and is not a loss for the Wits rule.
- **Rejected after month 33 and before month 36:** Paper 2 (submitted month 28) is the qualifying submitted manuscript; resubmit Paper 1 in parallel; update the publication details at first submission.
- **Both papers rejected and not resubmitted at month 36:** supervisor motivation letter to the Head of School (FSO §10.5). Do not plan on this branch.
- **Thm 9(iii) unresolved at month 18:** submit the EJS version (Thm 6(ii)-(iii), Prop 7, Thm 8, Thm 9(i)-(ii)) by month 22 regardless; the lower bound, if proved later, goes into ch:sharpness and a short follow-up note, not into a delay of Paper 1. The Wits rule is met by the submission, not by the strength of the headline.

## 6. Open items

1. Bibliography verifier: add Rio (2017), *Asymptotic Theory of Weakly Dependent Random Processes*, to bibliography.tex before ch:sharpness or Paper 1 cite the Fuk-Nagaev inequality; it is not in the file.
2. Statistician: the delta-dependence g_r of Thm 9(iii) is open; Paper 1 states it as open. If it closes before month 22 it moves into the headline.
3. Supervisor liaison: confirm the School's proposal deadline (three months per course page vs months 9-11 in the plan) and any seminar defence; this does not move the paper dates.
4. Supervisor liaison: confirm co-authorship and author order for both papers so the FSO §10.8 contribution statement can be drafted at month 22.
5. Confirm the three target journals against the current DHET accredited list before month 33.
6. Data engineer USD: confirm the first month at which the vendor marks the SOFR surface as quoted; Paper 2's validation window starts there.
