# Council verdicts on Topic 4 (candidate's own): "Optional Decomposition of Supermartingales and Super-Hedging of American Options using Deep Learning in Incomplete Markets" (2026-09-09)

Brief (inferred from title) in 07-topic4-brief-optional-decomposition-deep-superhedging.md.

| Reviewer | Verdict |
|---|---|
| Novelty scout (16 searches, 11 abstracts checked) | NOVEL WITH ADJACENT WORK |
| Stochastic analyst (superhedging duality) | VIABLE WITH CHANGES (WEAK as titled) |
| Deep-learning numerics theorist | VIABLE WITH CHANGES (WEAK as titled) |
| Quant practitioner | VIABLE WITH CHANGES (computes a number no desk books, unless reframed as model risk) |
| PhD examiner | APPROVE WITH REVISIONS, conditional on named international co-supervisor. 20% pass as written, 65% revised |

## Three structural problems, found independently by multiple reviewers
1. **Superhedging prices are TRIVIAL in the markets named.** Under unbounded stochastic volatility (Heston, SABR) the superhedging price of a call is the spot (Frey-Sin 1999; Cvitanic-Pham-Touzi 1999). Under general Levy jumps it is the trivial bound (Eberlein-Jacod 1997). A neural scheme that converges to the spot is not a thesis. Non-trivial regimes: (a) uncertain volatility band (Avellaneda-Levy-Paras; Lyons; Black-Scholes-Barenblatt PDE), (b) bounded / finitely many jump sizes, (c) trading constraints (Cvitanic-Karatzas 1993; Broadie-Cvitanic-Soner 1998 face-lifting), (d) correlation ambiguity on baskets, (e) semi-static hedging with vanillas. Pick one and put it in the title.
2. **RQ1 ("learn the optional decomposition") is circular.** Kramkov's decomposition takes the supermartingale V as INPUT; in superhedging V is the OUTPUT. The well-posed primal is: minimise V_0 over (V_0, H) subject to V_0 + int_0^tau H dS >= g_tau pathwise for all stopping times tau. C is not a primal unknown; it is the slack of the optimal solution, recovered afterwards. Parameterising C by a network adds a redundant unknown and worsens the loss landscape. If kept, uniqueness needs a selection principle (H unique only up to dS-null sets; C unique only as the minimal increasing process): a Gamma-convergence / uniqueness-of-minimiser theorem. That is the one place a genuinely doctoral theorem about the decomposition itself lives (examiner).
3. **"Supermartingale under ALL equivalent martingale measures" is not computable.** Neural density ratios over an unbounded set make an unstable min-max whose sup blows up. Once the prior set is compact (vol band), the American superhedging price is the viscosity solution of a fully nonlinear HJB variational inequality, equivalently a reflected 2BSDE / G-Snell envelope, and the "adversary" is often explicit (sup over sigma in a band of 1/2 sigma^2 Gamma is a sign test on Gamma: bang-bang). The game disappears. Where the family-of-measures framing is genuinely needed (nondominated, no reference measure), no convergence theory can be expected.

## Novelty: the gap claims are overstated
- **Biagini, Gonon, Reitsam (2023, Mathematical Finance, arXiv 2107.14113)** already make the Doob decomposition a direct neural target: approximate the consumption process C as an essential supremum over networks to recover the superhedging price process. Discrete time, European. RQ1 is closed there; open only in continuous time / American / nondominated.
- **Neural primal-dual certificates for American options are mature under ONE measure:** Guo, Langrene, Wu (2025, QF, arXiv 2302.12439); Ye & Wong "DeepMartingale" (2025, arXiv 2510.13868, with dimension-free expressivity theorem); Yang & Li (2024, arXiv 2409.06937); Becker, Cheridito, Jentzen (2020).
- **Deep reflected BSDE error bounds:** Hu & Zou (2026, arXiv 2609.05434).
- **Rodrigues (2025, arXiv 2506.14553)** proves aggregated Snell envelopes and robust hedging duality for American options in a nondominated semimartingale framework: the exact duality theorem the thesis would discretise. No numerics.
- **Ye, Wong, Park (2025, arXiv 2510.10260)** robust RL for optimal stopping under g-expectation ambiguity; no hedging.
- **Goudenege, Molent, Zanette (2024, arXiv 2407.13213)** adversarial-parameter NN control for the Uncertain Volatility Model, European, no convergence.
- **Eckstein, Guo, Lim, Obloj (2021 SIAM JFM); Neufeld & Sester (2021); Ansari et al. (2024 F&S)** neural MOT duality, European, semi-static.
- Nobody has: joint (H, C) learning for American claims under a family of measures in continuous time, or convergence theory for neural superhedging of American claims under multiple priors.

## Pasting-stability: where the real theorem lives (stochastic analyst)
The seller's American price is sup_Q sup_tau E_Q[g_tau]. The dynamic programming principle and Snell-envelope characterisation under a nonlinear expectation require the measure family to be stable under pasting (m-stable, Delbaen; Nutz-Zhang 2015). The set of all EMMs is m-stable, but a NEURAL parameterisation of measures (finite family of network densities) generally is NOT pasting-stable, so a sub-family gives only a lower bound and no DPP. Theorem target: which parametric network families are pasting-closed (Markov Girsanov drifts theta(t, X_t) as networks ARE, since pasting Markov drifts with a time indicator stays Markov), and does the price converge as the class grows.

## Where the optional-decomposition route beats the BSDE route
For bounded-vol and constrained settings the price is already a constrained reflected BSDE (Cvitanic-Karatzas 1993; Bouchard-Elie-Reveillac 2015), so "deep optional decomposition" risks relabelling "deep constrained reflected BSDE" (Hure-Pham-Warin adaptable). The defensible niche: the BSDE route is Markovian and needs a state process; the primal pathwise route works on any filtration (non-Markov, rough vol, path-dependent American claims) and produces a STRATEGY, not just a value.

## Strongest plausible main theorem (stochastic analyst)
Let S be an Ito process with volatility in a compact band (or a market with cone constraints K), g a Lipschitz bounded American payoff. Let H_n be feedforward networks (or LSTMs on path segments) of width n and Theta_n a pasting-stable network class of Girsanov drifts. Then the primal value p_n = min V_0 over H_n with pathwise dominance enforced on N samples via a penalty, and the dual value d_n = sup over Theta_n and stopping-time networks, satisfy d_n <= p <= p_n and p_n - d_n -> 0 as n, N -> infinity, with a rate under Lipschitz-in-path assumptions (Gonon-Schwab approximation of the face-lifted value plus Nutz-Zhang DPP). The certificate part is publishable in F&S / MF if the pasting-stability argument is clean.

## Numerics theorist on convergence (RQ4)
Standard Jentzen/Gonon triad (approximation / statistical / optimisation, global optimiser assumed) transfers as a re-run. NEW difficulties: (i) C is not a state functional: path-dependent non-negative running-sum architecture, C only BV in time, not Lipschitz in x; (ii) the sup over Q breaks the L2(Q) orthogonality used in projection proofs: error must propagate in a Q-uniform norm, needing weakly compact priors and uniformly Lipschitz generator (a 2BSDE setting). An a priori error bound for a deep backward scheme of a reflected 2BSDE / G-Snell envelope in a Q-uniform norm would be new. Dimension-free rates: plausible only in the semilinear single-measure regime; for fully nonlinear obstacle problems none is known. State as open question, not promise. "Certified gap" must become "high-probability primal-dual interval".

## Practitioner: the customer is model validation, not the desk
Desks calibrate one LSV/Heston, run LSMC or PDE, book a reserve; a superhedging number changes no trading decision. Model validation (SR 11-7) and prudent valuation (CRR/EBA model-risk AVA for Bermudans/callables) today re-price on 3-5 models and eyeball the spread with no certificate the range is complete. A primal-dual pair over a bounded ambiguity set is exactly what a validator would sign. In 1-3 dimensions BSB-PDE and trees win every time; dimension bites on multi-callable basket notes (5-20 names), Bermudan swaptions under SV + multi-factor rates, worst-of autocallables, and CORRELATION AMBIGUITY (matrix-valued, naturally bounded, no PDE handles it): the sweet spot.

## Consensus changes
1. Fix the incompleteness: uncertain volatility band (spine), with constraints / bounded jumps / correlation ambiguity as extensions. Drop unbounded stochastic vol and general jumps.
2. Delete "learn C" as a primal unknown, or make its uniqueness (minimal-consumption selection, Gamma-convergence) the stated theorem. Learn H (primal) plus a pasting-stable drift class and a stopping-time network (dual).
3. Make the primal-dual high-probability interval the deliverable and the pasting-stability + DPP + gap-closure result the main theorem; bolt the error triad on afterwards.
4. Position as the multi-measure / American extension of Biagini-Gonon-Reitsam, Guo-Langrene-Wu and DeepMartingale; discretise Rodrigues (2025).
5. Benchmark on BSB-PDE (d = 1-2) for correctness, then d = 5, 20 baskets with vol/correlation bands against reflected-BSDE and LSMC; one applied chapter comparing the certified bound to the "spread of five models" practice.

## Recommended titles
- Examiner: Neural Optional Decomposition and Certified Superhedging of American Options under Volatility Uncertainty
- Analyst: Primal-Dual Deep Superhedging of American Options under Volatility Uncertainty and Trading Constraints
- Numerics: Deep Backward Schemes for American Superhedging under Volatility (and Jump) Uncertainty: Reflected 2BSDEs, Primal-Dual Bounds and Convergence

## Publications
1. Y2: neural Snell envelope under G-expectation with primal-dual certificates. Quantitative Finance or Mathematics and Financial Economics.
2. Y3: learnable optional decomposition / pasting-stability and gap closure (the doctoral paper). Finance & Stochastics or SIAM JFM.
3. Y4: extension to constraints / jumps / correlation ambiguity, or the error bound. Applied Mathematical Finance or J. Computational Finance.

## Skeleton
- Y1: measure-theoretic stochastic calculus, semimartingale theory (optional sigma-field, optional projection), BSDE/RBSDE, G-expectation (Peng); reproduce Becker-Cheridito-Jentzen and Hure-Pham-Warin; formalise the primal loss; proposal.
- Y2: band-uncertainty American pricer, primal-dual certificates; paper 1.
- Y3: pasting-stability / uniqueness theorem; paper 2.
- Y4 (Y5 part-time): extension; paper 3; write-up.

## Fallback that still passes
Certified primal-dual method for American options under uncertain volatility (neural superhedge upper, neural stopping rule under a specific sigma-path lower), with a proved gap bound and empirical closure in <= 5 dimensions. Respectable PhD even if the uniqueness theorem does not fall. Worst-case sigma is bang-bang in sign of Gamma, so the adversarial game can be removed entirely if training is unstable.

## Supervision
Local: UCT AIFMRM (Ouwehand, McWalter, Backwell: stochastic analysis / hedging, not G-expectation), Wits (Mahomed, robust finance adjacent), Stellenbosch (weaker on BSDEs). Nobody in SA is native on optional decomposition plus neural control. International co-supervisor REQUIRED: Cheridito (ETH) fits the spine exactly; Pham/Warin (Paris) for the RBSDE route; Nutz (Columbia) if G-expectation American theory dominates. Obloj is the wrong fit (MOT, static hedges). Do not register without a committed co-supervisor.

## Examiner's updated ranking of all four topics for this candidate
1. Conformal certificates for deep hedging: feasible, locally supervisable, publishable, lowest theorem-risk.
2. SABR-FMM / JIBAR-ZARONIA (reframed to compounded-rate asymptotics and identifiability): most supervisable locally, market relevance, doctoral only after reframing.
3. This topic (narrowed): the most mathematically serious of the four that is still tractable; needs an offshore co-supervisor and two years of catch-up; ranked above adapted OT because it has a concrete fallback that passes.
4. Adapted OT for rough volatility: deepest, least supervisable, no safe fallback.
