# Council verdicts on "Certified Deep Hedging" (2026-09-09)

Five independent reviewers interrogated the brief in 01-topic-brief.md.

| Reviewer | Verdict |
|---|---|
| Novelty scout (13 literature searches) | NOVEL WITH ADJACENT WORK |
| Mathematical finance theorist | VIABLE WITH CHANGES |
| ML theorist (conformal / PAC-Bayes) | VIABLE WITH CHANGES |
| Quant practitioner | VIABLE WITH CHANGES (empirical leg leaning weak) |
| PhD examiner | APPROVE WITH MAJOR REVISIONS; 35% pass as written, ~75% if narrowed |

## Consensus points
1. RQ1 (non-exchangeable conformal certificate for the P&L of a frozen deep-hedging policy under beta-mixing and drift) is the only spine. It is theorem-bearing and unclaimed.
2. RQ2's claim that "policy-dependent residuals break exchangeability" is FALSE in the split-conformal setting (policy is fixed before calibration). It only becomes a real problem with (a) online retraining on calibration data or (b) market-impact feedback making the deployment measure endogenous. Prinster et al. (ICML 2024) already shows agent-induced shift is repairable in principle.
3. RQ3 (PAC-Bayes for expected shortfall) is tractable but will be vacuous: constants scale like exp(Lipschitz * T) in path length. Reppen & Soner (2023) already give Rademacher bounds. Cut or demote to a year-one pilot.
4. RQ4 (coverage-aware training) risks being "deep hedging with a different spectral risk measure" unless the penalised width is the drift-corrected width. Then it must be positioned against He-Sutter-Gonon (NeurIPS 2025) and distributionally robust deep hedging. Keep as applied chapter only.
5. Adapted Wasserstein is the wrong object for the coverage gap. The gap lives on the scalar score law (TV, or W1 with an anti-concentration assumption). Keep AW only for a policy-misspecification Lipschitz lemma. Signature-MMD is estimable from blocked data; AW is not from one path history.
6. JSE illiquid options are a data trap. Use liquid index options (Top40 or SPX), secure data in year one, make the 2020 / 2022 regime-shift out-of-sample test the centrepiece.
7. Mandatory baseline: stationary block bootstrap and historical-simulation quantiles of hedge residuals. If the certificate cannot out-guarantee them the thesis is embarrassed.
8. Commercial framing: a finite-sample challenger to FRTB P&L-attribution tests and SR 11-7 model validation for ML hedgers.

## Nearest prior art (must cite and differentiate)
- He, Sutter, Gonon 2025, NeurIPS, arXiv:2508.14757 (distributional adversarial training for deep hedging)
- Reppen & Soner 2023, Math. Finance (deep ERM generalisation bounds)
- Prinster, Stanton, Liu, Saria 2024, ICML, arXiv:2405.06627 (conformal under agent-induced shift)
- Gan et al. 2025, arXiv:2510.26026 (conformal intervals for RL policy returns)
- Oliveira et al. 2024, JMLR (split CP under mixing)
- Xu et al. ICLR 2025, arXiv:2501.13430 (Wasserstein-bounded coverage gap)
- Schmitt 2026, arXiv:2602.03903 (regime-weighted conformal VaR)
- Gasteratos, Jacquier, Lemercier, Lyons, Salvi 2025, arXiv:2512.03243 (signature novelty detection on path space)
- Taufiq et al. 2022 (conformal off-policy evaluation)
- Barber, Candes, Ramdas, Tibshirani 2023; Gibbs & Candes ACI; Gibbs, Cherian, Candes 2023 (conditional coverage)

## Plausible main theorem (math finance theorist)
Let (X_t) be stationary beta-mixing with beta(k) <= C k^{-r}, r > 1. Policy theta-hat trained on D, calibrated on n blocks of length b disjoint from D, score s(x) = loss(x, theta-hat). For the weighted split-conformal quantile q-hat, with probability >= 1 - delta over calibration:

  P_Q(s(X) <= q-hat | D) >= 1 - alpha - d_TV(P_cal^s, Q^s) - C sqrt(b log(1/delta)/n) - n beta(b).

If Q is within adapted-Wasserstein distance eps of the training measure and loss(., theta-hat) is AW-Lipschitz with constant Lip(theta-hat), the TV term is replaced by O(Lip(theta-hat) eps) in W1 on the score law. The AW-Lipschitz lemma for a bounded adapted neural policy is the hard, novel piece.

## Fallback if the bound is vacuous
Prove the impossibility direction: no distribution-free finite-sample certificate is non-vacuous once drift exceeds X. That is publishable on its own.

## Recommended narrowed title
Distribution-Free Certification of Deep Hedging Strategies under Serial Dependence and Distribution Drift

## Publication plan
1. Year 2: conformal certificate for terminal P&L of a fixed hedging policy under beta-mixing. Quantitative Finance or SIAM J. Financial Math.
2. Year 3: coverage gaps under path-measure drift, signature-MMD bound plus impossibility result. EJS / Annals (ambitious) or Mathematical Finance.
3. Year 3-4: coverage-aware deep hedging vs block bootstrap and FRTB PLA on rough-Bergomi and index-option data. J. Computational Finance or NeurIPS/ICML finance workshop then journal.

## Year-by-year skeleton
- Y1: probability and stochastic calculus coursework; reproduce Buehler et al. 2019; split conformal on frozen hedger P&L in simulation; PAC-Bayes vacuity pilot (cut if vacuous); secure data source; proposal defence month 9-12.
- Y2: prove RQ1 under beta-mixing with one drift metric; rough-Bergomi experiments; Paper 1.
- Y3: drift bound and impossibility result; ACI/conditional-coverage online variant; data pipeline; Paper 2; coverage-aware prototype.
- Y4: empirical chapter, Paper 3, write-up.

## Supervision
Primary: statistician who knows conformal (UFS/UP). Co: math finance with deep hedging and signatures (Wits or UCT AIFMRM). International co-supervisor near-mandatory for the theorem chapter (CMU/Berkeley conformal cluster, ETH Teichmann school, or Oxford signatures group).
