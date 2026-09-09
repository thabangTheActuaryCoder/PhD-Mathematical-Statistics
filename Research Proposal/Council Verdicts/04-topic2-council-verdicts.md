# Council verdicts on Topic 2: "Adapted Optimal Transport for Rough Volatility" (2026-09-09)

Pure mathematical finance, no machine learning. Brief in 03-topic2-brief-adapted-OT-rough-vol.md.

| Reviewer | Verdict |
|---|---|
| Novelty scout (14 searches + full-text check of arXiv 2505.21337 and the Oxford DPhil it comes from) | PARTIALLY DONE |
| Mathematical finance theorist | VIABLE WITH CHANGES (substantial) |
| Stochastic analyst | VIABLE WITH CHANGES (sold on a wrong premise) |
| Quant practitioner | VIABLE WITH CHANGES as theory; WEAK as desk-relevant |
| PhD examiner | APPROVE WITH MAJOR REVISIONS; 25-35% pass as written, 65-75% narrowed WITH a foreign co-supervisor, 40% without |

## Two errors in the brief that a committee would catch
1. **"Long memory" is backwards.** Rough volatility (H ~ 0.1 < 1/2) has antipersistent, SHORT-range dependent increments (summable autocovariance). Long memory is H > 1/2, the regime Gatheral-Jaisson-Rosenbaum used rough vol to refute. Research question 2's entire storyline ("mixing arguments fail, rate depends on H") is built for the wrong regime. Moreover the Riemann-Liouville driver is non-stationary, so "one long trajectory" has no ergodic target; one must switch to a stationary model (fractional OU / RFSV) before the question is well-posed. For H < 1/2 Breuer-Major gives a plain n^{-1/2} CLT with H only in constants: a null result.
2. **Research question 4 is already solved.** Jiang & Lim (2025, arXiv 2505.21337; Oxford DPhil, supervisor Obloj) prove the explicit AW_2 between Gaussian Volterra processes via causal factorisation, the closed form AW_2(B_H1, B_H2)^2 = integral of (k_H1 - k_H2)^2 with the synchronous coupling optimal, and synchronous optimality for scalar fractional SDEs with H > 1/2. They announce a follow-up on stochastic Volterra equations. Independently, three reviewers derived the same lemma in a few lines: under bicausality d<W,W'> = rho ds with |rho| <= 1, positive kernels force the synchronous coupling. Also Gunasingam & Wong (ECP 2025; arXiv 2604.22159; 2604.22453) cover the discrete-time / filtered Gaussian case.

## What survives (consensus)
- **Upper bound in RQ1 is a computation, not a theorem.** d/dH of the RL kernel has L2 norm ~ 1/(2H^2), so H -> Law is locally Lipschitz on [H_0, 1/2] with constant ~ 1/H_0 (not Holder-degenerate). Exponentiation and Ito preserve it. Must be stated for (log S, log V) since S lacks p-moments for p > 1 (Gassiat 2019).
- **The theorem-grade content is the LOWER bound / sharpness** for the non-Gaussian joint law (S, V) under sup-norm cost, where synchronous coupling is not obviously optimal, and the CAUSAL (not bicausal) distance.
- **Rough Heston** has no known strong solution, so no synchronous coupling; it must go through Markovian lifts (Abi Jaber-El Euch) with a lift-to-AW approximation theorem. That approximation theorem is genuine and is also the version practitioners would read (lift-truncation error as a function of N and H).
- **RQ3 value-functional Lipschitz continuity is a corollary** of Backhoff-Bartl-Beiglbock-Eder 2020; the constant is payoff Lipschitz constant times moment bounds. The real content is STRATEGY TRANSFER: hedge computed under H', executed under H, a causal estimate needing Lipschitz regularity of the rough-vol hedging strategy as a path functional (Viens-Zhang functional Ito). Must declare the hedger's filtration: F^{S,V} vs F^S (with rho != 0 the latter is a filtering problem).
- **RQ2 should become semi-parametric:** one-path H estimation (Fukasawa-Takabatake-Westphal; Bolko-Christensen-Pakkanen-Veraart; Chong-Hoffmann-Liu-Rosenbaum-Wang) transferred to AW via RQ1, plus a minimax lower bound showing nonparametric one-path AW estimation is impossible. Volatility is latent; only S is observed. This is the honest statistics contribution.
- **Practitioner:** desks do not carry H as a free parameter (pinned at ~0.1, xi_0 absorbs everything, or replaced by a lift). Hedging P&L is far more sensitive to vol-of-vol and forward variance than to H. A two-day Monte Carlo of hedging P&L across H in {0.05, 0.1, 0.15} must be pre-empted, not refuted by. Reframe RQ3 towards lift-truncation error. Model-risk hook (SR 11-7, IFRS 13 / prudent valuation AVA) is real but modest and needs a computable algorithm.
- **Malliavin / Viens-Zhang** is decorative except for the hedging-strategy chapter. Rough paths not needed. Delete from the methods list elsewhere.

## Nearest prior art (must cite as foundation, not gap)
- Jiang & Lim 2025, arXiv 2505.21337 (Gaussian Volterra AW_2, synchronous optimality)
- Gunasingam & Wong 2025 ECP; 2026 arXiv 2604.22159, 2604.22453
- Robinson & Szolgyenyi 2025 SPA; Hitz & Robinson arXiv 2403.09941 (AW between SDE laws)
- Richard & Talay arXiv 1605.03475 (Lipschitz in H, weak topology, H ~ 1/2)
- Acciaio & Hou 2022; Hou 2024; Blanchet et al. 2024 (adapted empirical measure rates)
- Blanchet-Larsson-Park-Wiesel (AW <= C W^theta under smooth kernels; check whether it covers the Gaussian layer)
- Hager & Kreher 2026 arXiv 2606.16619 (rough Heston expansion in H)
- Horvath, Teichmann, Zuric 2021 (deep hedging under rough vol, numerical P&L vs H)
- Backhoff, Bayraktar, Ekren, Zitridis 2026 arXiv 2605.19978 (continuous-time causal OT)

## Plausible main theorem (theorist)
Fix compact Theta in [H_0, 1/2) x (0, eta_bar] x [-1, 1] x {xi bounded}, horizon T, p >= 1. Then on C([0,T]; R^2) with sup norm,
  AW_p(Law(log S, log V)^theta, Law(log S, log V)^theta') <= C(T, p, Theta) ( |H - H'| / H_0 + |eta - eta'| + |rho - rho'| + ||xi - xi'||_inf ),
the 1/H_0 rate being attained on the log-vol marginal; rough Heston satisfies the same with H-dependence via the lift. Sharpness (matching lower bound for the joint non-Gaussian law) is the thesis theorem.

## Recommended narrowed title
Adapted Wasserstein Distances between Volterra Gaussian Processes, with Application to Hurst-Parameter Stability and Hedging in Rough Bergomi

## Publication plan
1. Y2: lower bounds / sharpness of AW between rough Bergomi laws, plus lift-to-AW approximation for rough Heston. SIAM J. Financial Math or EJP.
2. Y3: strategy transfer: hedging under Hurst misspecification in rough Bergomi, causal estimates via functional Ito. Finance & Stochastics or Mathematical Finance.
3. Y4: semi-parametric plug-in rates for rough-vol laws in AW from one price path, with minimax impossibility for the nonparametric problem. Bernoulli or SISP.

## Skeleton
- Y1: measure-theoretic probability, Brownian stochastic calculus (Karatzas-Shreve), Gaussian processes / RKHS / Volterra kernels, optimal transport (Santambrogio), the adapted-OT corpus (~10 papers), Follmer-Schweizer quadratic hedging. Reproduce Jiang-Lim and Gunasingam-Wong. Write the synchronous-coupling upper bound with explicit 1/H_0 constants. Contact Jiang/Lim/Obloj to check the announced Volterra follow-up. Proposal defence month 10-12. Add six months if the MSc lacked measure-theoretic probability.
- Y2: lower bound / sharpness; rough Heston lift theorem; paper 1.
- Y3: strategy transfer hedging theorem; Monte Carlo counterfactual (H vs eta vs xi_0); paper 2.
- Y4: semi-parametric estimation chapter; paper 3; write-up.

## Supervision
No one in South Africa has published in adapted optimal transport. Local stochastic-analysis-capable: UCT AIFMRM (Ouwehand), UP (Kufakunesu), Wits (Labuschagne). UFS has no depth here. International co-supervisor is MANDATORY: Vienna (Beiglbock, Bartl, Pammer, Backhoff), Oxford (Acciaio, Obloj), or Pakkanen for the rough-vol statistics strand (best single fit for this candidate). Without a signed co-supervisor the proposal should not go to defence.

## Examiner's comparison with Topic 1 (conformal deep hedging)
The ML topic is the safer bet; the pure topic is the better one. Conformal deep hedging is supervisable locally, uses the statistics MSc directly, yields a paper within 12 months and is finishable part-time; its weakness is that coverage guarantees are almost free and the field will be crowded by submission. Adapted transport has higher entry cost, mandatory foreign co-supervision and an empty first eighteen months, but produces theorems that will still be cited in fifteen years and opens a research career in probability. Working full-time and wanting a doctorate in 3-4 years: take Topic 1. Aiming at a research position in mathematics with full-time study and a Vienna or Oxford link: take Topic 2, narrowed.
