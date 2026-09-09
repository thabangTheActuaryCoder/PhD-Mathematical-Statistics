# Proposed PhD topic (pure mathematical finance, no machine learning)

## Title
Adapted Optimal Transport for Rough Volatility: Stability, Statistical Estimation and Hedging under Long-Memory Path Measures

## One-paragraph statement
Two of the most active programmes in mathematical finance have not yet been connected. (A) Rough volatility (Gatheral, Jaisson, Rosenbaum 2018; rough Bergomi, rough Heston) models the log-volatility as a fractional/Volterra process with Hurst index H ~ 0.1, so that the volatility path is not a semimartingale and the model is non-Markovian. (B) Adapted (causal / bicausal) optimal transport and the adapted Wasserstein distance AW_p (Pflug & Pichler; Backhoff-Veraguas, Bartl, Beiglböck & Eder 2020; Bartl, Beiglböck & Pammer 2021) is the topology on laws of stochastic processes under which the classical problems of finance (pricing, optimal stopping, utility maximisation, hedging) are continuous, and whose statistical counterpart, the adapted empirical measure (Backhoff, Bartl, Beiglböck & Wiesel 2022; Acciaio & Hou 2023), gives finite-sample convergence rates for laws on path space. Existing AW theory is proved for discrete-time processes or continuous-time semimartingales driven by Brownian motion with Markovian or short-memory structure. Rough volatility laws are exactly the case not covered: long memory, non-Markovian, driven through a singular Volterra kernel. The thesis would build the adapted-transport theory of rough volatility: (i) prove quantitative AW-stability of the joint price-volatility law in the model parameters, in particular in H, using the Volterra representation and Brownian-filtration causality; (ii) obtain convergence rates for the adapted empirical measure built from a single long trajectory of a long-range-dependent process, where standard mixing-based arguments fail, and show how the rate depends on H; (iii) derive quantitative hedging-error and pricing-error bounds under misspecification of H (how wrong can the roughness index be before a hedge fails), as Lipschitz estimates of the relevant value functionals in AW_p; (iv) characterise optimal bicausal couplings between Volterra Gaussian processes with different kernels (a Knothe-Rosenblatt / kernel-transform structure), giving closed-form or semi-closed-form AW distances between rough volatility models.

## Claimed gap
- AW stability results exist for discrete-time processes and for continuous-time semimartingales; none for non-semimartingale volatility with singular Volterra kernels.
- Adapted empirical measure rates are for i.i.d. path samples or Markov processes; single-trajectory long-memory estimation in the adapted topology is untouched.
- Rough-volatility literature has asymptotics (short maturity, large deviations), calibration, simulation and Markovian lifts, but no model-uncertainty topology in which Hurst misspecification is quantified for hedging.
- Explicit AW distances between Gaussian processes exist for finite-dimensional / Markov Gaussian cases (Gunasingam & Wong 2024 on Gaussian adapted transport; Acciaio, Backhoff, Jia); Volterra Gaussian processes with different kernels are open.

## Candidate research questions
1. Is the map (H, eta, rho, xi) -> Law(S, V) on path space Lipschitz (or Holder, with what exponent) in AW_p for rough Bergomi and rough Heston? Does the modulus degrade as H -> 0?
2. For the adapted empirical measure from one trajectory of length T of a long-range-dependent Volterra process observed at n points, what is the convergence rate in AW_p, and how does it depend on H and on the adapted-partition width?
3. What is the AW-Lipschitz constant of quadratic-hedging and superhedging value functionals for path-dependent payoffs, and what quantitative hedging-error bound under Hurst misspecification follows?
4. Do optimal bicausal couplings between two Volterra Gaussian processes reduce to a coupling of the driving Brownian motions composed with kernel transforms, giving explicit AW_2 between rough volatility models?

## Candidate methods
Causal and bicausal optimal transport, adapted Wasserstein distance, Volterra Gaussian processes and fractional calculus, Malliavin calculus and functional Ito for Volterra processes (Viens & Zhang 2019), Gaussian optimal transport, long-range dependence and non-mixing limit theorems, quadratic hedging in incomplete markets, Markovian lifts of rough volatility (Abi Jaber, Harms, Cuchiero-Teichmann).

## Context of candidate
Candidate is completing an MSc in Mathematical Statistics (UFS, South Africa). Wants a topic in pure mathematical finance (no machine learning) that is genuinely novel, mathematically serious, and feasible in 3-4 years. The statistical estimation strand (research question 2) is intended to leverage the candidate's background.
