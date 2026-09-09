# Proposed PhD topic

## Title
Certified Deep Hedging: Distribution-Free Hedging-Error Guarantees for Neural Hedging Strategies under Non-Exchangeable Market Data

## One-paragraph statement
Deep hedging (Buehler, Gonon, Teichmann, Wood 2019) replaces closed-form delta hedging with a neural network trained to minimise a convex risk measure of the terminal hedging error. It is now widely used, yet it ships with essentially no finite-sample statistical guarantee: a practitioner cannot state, with a chosen confidence, an upper bound on the realised hedging loss of a trained strategy on unseen market paths. Conformal prediction gives exactly such distribution-free, finite-sample guarantees, but its core assumption, exchangeability, is violated by financial time series (serial dependence, regime shifts, volatility clustering). The thesis would develop a theory of *certified deep hedging*: (i) construct conformal-style prediction sets for the terminal P&L of a deep-hedging policy using path-signature features as the non-conformity score, (ii) extend the non-exchangeable conformal theory of Barber, Candès, Ramdas and Tibshirani (2023) to the sequential, policy-dependent setting where the hedging network itself induces the residual distribution, obtaining explicit coverage-gap bounds in terms of a measurable drift between training and deployment path measures (e.g. a signature-kernel MMD or an adapted Wasserstein distance), (iii) derive PAC-Bayesian generalisation bounds for the risk-measure objective of deep hedging, and (iv) close the loop by making the certificate a training-time constraint: a "coverage-aware" deep hedger that trades off expected cost against the width of its certified loss interval, and is evaluated on rough-volatility simulators and on illiquid emerging-market (JSE) option data.

## Claimed gap
- Deep hedging literature: rich on architectures, risk measures, market frictions; almost nothing on finite-sample guarantees or certification of the trained strategy.
- Conformal prediction literature: strong recent progress on non-exchangeable data, but applied to point forecasting, not to the P&L of a *control policy* whose own actions shape the residual distribution.
- Signature methods: used as features for pricing/calibration and as kernels for distribution distances, but not as the non-conformity geometry for a hedging certificate.
- Adapted Wasserstein / causal optimal transport: gives the "right" distance between path measures for hedging problems (Backhoff-Veraguas, Bartl, Beiglböck, Eder 2020) but has not been connected to conformal coverage gaps.

## Candidate research questions
1. Under what dependence conditions (beta-mixing, functional dependence) does a weighted split-conformal certificate for terminal hedging P&L achieve coverage 1 - alpha - gap, with gap controlled by an adapted-Wasserstein or signature-MMD drift term?
2. Does the policy-dependence of residuals break standard conformal exchangeability arguments, and can it be repaired by an online/adaptive (ACI-style) update whose regret can be bounded?
3. What PAC-Bayes generalisation bound holds for expected-shortfall-type objectives of deep hedging, and how does it scale with hedging frequency and path length?
4. Does training with a certificate-width penalty produce strategies that are competitive in expected cost but materially more robust under regime shift?

## Candidate methods
Split and weighted conformal prediction; adaptive conformal inference; rough path signatures and signature kernels; adapted/causal Wasserstein distance; PAC-Bayes for dependent data; neural SDE / rough Bergomi simulators; empirical work on JSE equity options.

## Context of candidate
Candidate is completing an MSc in Mathematical Statistics (UFS, South Africa) and works as an AI engineer. Wants a topic that is genuinely novel, mathematically serious, and feasible for a 3-4 year PhD.
