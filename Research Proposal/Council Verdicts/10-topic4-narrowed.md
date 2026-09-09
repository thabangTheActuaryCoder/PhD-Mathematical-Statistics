# Neural Optional Decomposition and Certified Superhedging of American Options under Volatility Uncertainty
One-pager for a PhD in Mathematical Statistics, Wits (2026-09-09). Narrowed from topic 4 per council round 4.

## Statement
In a market where volatility is only known to lie in a band, the seller's price of an American option is the smallest process that dominates the payoff at every stopping time and is a supermartingale under every volatility scenario. The optional decomposition writes that process as initial capital plus a hedging integral minus an increasing consumption process. Nobody can compute it beyond two or three assets, and the deep-learning methods that exist compute prices under ONE model, not bounds over a set. The thesis builds a primal network superhedge (upper bound) and a dual network over pasting-stable volatility scenarios and stopping rules (lower bound), proves the two meet as width and sample size grow, and delivers a high-probability certified interval plus the hedging strategy. For a statistics doctorate the spine is the statistical theorem: the finite-sample error of the certified interval under dependent Monte Carlo paths and the impossibility of a dimension-free rate for the fully nonlinear obstacle problem.

## Why "volatility uncertainty" is in the title
Under unbounded stochastic volatility the superhedging price of a call is the spot; under general jumps it is the trivial bound. Only a compact ambiguity set gives a non-trivial problem: volatility band, bounded jump sizes, trading constraints, correlation ambiguity on baskets. The band is the spine; correlation ambiguity is the extension where no PDE can follow.

## Research questions
1. PASTING-STABILITY. The dynamic programming principle for the seller's price needs the scenario family to be closed under pasting. Finite families of network densities are not. Which network classes of Markov Girsanov drifts theta(t, X_t) are pasting-closed, and does the dual value converge to the true price as the class grows?
2. UNIQUENESS OF THE LEARNED DECOMPOSITION. H is unique only up to dS-null sets and C only as the minimal increasing process. State a loss whose population minimiser is the minimal-consumption decomposition (Gamma-convergence / selection theorem), or drop C as a primal unknown and recover it as slack.
3. CERTIFIED INTERVAL (statistics spine). High-probability bound d_n - eps_N <= p <= p_n + eps_N with eps_N explicit in sample size, path length and network class complexity, in a norm uniform over the ambiguity set. Statistical error via Rademacher / uniform convergence over hypothesis classes under dependent paths; approximation error via Gonon-Schwab-type expression rates; optimisation assumed global and said so.
4. DIMENSION. Is there a dimension-free rate for the fully nonlinear obstacle problem? Conjecture no; prove a lower bound or state as open with experiments at d = 2, 5, 20.

## Main theorem targets
- T1 (analysis): for S an Ito process with volatility in a compact band and g a Lipschitz bounded American payoff, primal p_n over width-n networks with pathwise dominance on N samples and dual d_n over a pasting-stable drift class and stopping-time networks satisfy d_n <= p <= p_n and p_n - d_n -> 0 as n, N -> infinity.
- T2 (statistics): finite-sample high-probability width of the certified interval, with a matching lower bound in d for the statistical term.
- T3 (numerics, optional): a priori error bound for a deep backward scheme of the reflected 2BSDE / G-Snell envelope in a Q-uniform norm.

## What already exists (position against, do not claim as gap)
Biagini-Gonon-Reitsam 2023 (neural Doob decomposition, discrete time, European); Guo-Langrene-Wu 2025, Ye-Wong DeepMartingale 2025, Yang-Li 2024, Becker-Cheridito-Jentzen 2020 (neural primal-dual for American options under ONE measure); Hu-Zou 2026 (deep reflected BSDE error bounds); Rodrigues 2025 (robust hedging duality for American claims, nondominated, no numerics: the theorem to discretise); Ye-Wong-Park 2025 (robust RL stopping under g-expectation, no hedging); Goudenege-Molent-Zanette 2024 (adversarial UVM control, European, no convergence); Eckstein-Guo-Lim-Obloj 2021, Neufeld-Sester 2021 (neural MOT, European, semi-static).

## Benchmarks
- d = 1-2: Black-Scholes-Barenblatt PDE with obstacle, exact. Correctness and triviality visible.
- d = 5: basket American put under volatility band vs Hure-Pham-Warin deep reflected BSDE and LSMC.
- d = 20: basket / multi-callable note under correlation ambiguity where no PDE exists; compare certified interval to the "spread of five models" practice.

## Customer
Model validation and prudent valuation (SR 11-7, CRR/EBA model-risk AVA for Bermudans and callables), not the desk. A certified interval over a bounded ambiguity set is what a validator signs.

## Supervision (Wits Mathematical Statistics)
- Primary: Wits statistician (learning theory / dependent-data inference) owning T2.
- Finance co-supervisor: Wits mathematical finance (School of Computer Science and Applied Mathematics) or UCT AIFMRM (Ouwehand, McWalter, Backwell) for optional decomposition and BSDEs.
- International co-supervisor REQUIRED: Cheridito (ETH) fits exactly; Pham/Warin (Paris) for the RBSDE route; Nutz (Columbia) for G-expectation American theory. Do not register without one.

## Publications
1. Y2: neural Snell envelope under a volatility band with primal-dual certificates. Quantitative Finance or Mathematics and Financial Economics.
2. Y3: finite-sample theory of the certified interval (T2) with the pasting-stability result (T1). Finance & Stochastics or SIAM JFM; statistics version to EJS.
3. Y4: correlation ambiguity on baskets and the model-risk application. Applied Mathematical Finance or J. Computational Finance.

## Skeleton
- Y1: semimartingale theory (optional sigma-field, optional projection), reflected BSDEs, G-expectation (Peng), statistical learning theory; reproduce Becker-Cheridito-Jentzen and Hure-Pham-Warin; formalise the primal loss; proposal.
- Y2: band pricer, certificates at d = 1-5; paper 1.
- Y3: T1 and T2; paper 2.
- Y4 (Y5 part-time): correlation ambiguity, d = 20; paper 3; write-up.

## Fallback that passes
Certified primal-dual method under a volatility band with a proved gap bound and empirical closure in <= 5 dimensions, even if the uniqueness theorem does not fall. If the adversary will not train, the worst-case volatility is bang-bang in the sign of gamma and the game is removed.

## Standing
Ranked third of four for this candidate by the examiner: the most mathematically serious topic that is still tractable, with a concrete fallback; needs an offshore co-supervisor and two years of catch-up.
