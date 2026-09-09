# GROUND TRUTH for all mathematical claims

Source of record: `"~/Desktop/PhD Thesis/Council" Workspace/13-mathematics-3yr.tex` (compiled: `13-mathematics-3yr.pdf`). It contains the council-corrected statements. Chapters must match it exactly in hypotheses and conclusions. If a writer believes a statement there is wrong, they do NOT silently change it; they add a `\gap{}` describing the doubt and append a lesson.

## Status of each result
| Result (ground-truth numbering) | Status | Chapter |
|---|---|---|
| Lemma 1 time-changed SABR | cited, proof written in full | 2 |
| Prop 2 non-decaying vol-of-vol | derivation, write in full; CORRECTED 2026-09-09: no material curvature understatement (0.002 bp), the 17% figure referred to total variance only | 2 |
| Thm 3 identified/unidentified components | TARGET, route only | 5 |
| Thm 4 two models | corollary, proof can be written given Thm 3 | 5 |
| Prop 5 tenor consistency | part (a) provable, (b) leading-order, (c) remark | App A |
| Thm 6 coverage under mixing and drift | TARGET but assembled from standard tools: write the full proof, marking each borrowed lemma | 3 |
| Prop 7 W1 bound | provable, write full proof | 3 |
| Thm 8 sharpness | provable, write full proof | 4 |
| Thm 9 calibration-conditional coverage error over B_r: optimal blocking + minimax (restated 2026-09-09, third version) | TARGET: (i) optimal block length for the blocked route, provable, exact minimiser b* = (2(r+1))^{2/(2r+3)} N^{3/(2r+3)}, deficit bound is the EXPECTED CONDITIONAL SHORTFALL from Thm 6(ii), not 6(i); (ii) blocked rate N^{-r/(2r+3)} is NOT minimax: unblocked sample quantile has coverage error O((N delta)^{-1/2}) for all r>1, provable via covariance inequality + Chebyshev, i.i.d. two-point lower bound N^{-1/2}; (iii) mixing-driven lower bound (N^r delta)^{-1/(r+1)} at confidence delta via regime-renewal construction, route only, Fuk-Nagaev (Rio 2017 Ch. 6) upper bound, delta-dependence g_r open; (iv) partially observed drift, route only; (v) dependent W1 is Dedecker-Merlevede (2017), cited and specialised, NOT new | 4 |
| First-draft bootstrap theorem | DROPPED; empirical comparison only | 6 |

## Corrections that must never be undone
1. Both JIBAR and compounded caplets are priced under the (T+Delta)-forward measure. No convexity term.
2. Basis correlations contaminate the JIBAR smile, not the compounded caplet.
3. Two unidentified correlations (rho_BF, rho_Balpha); ATM vol identified within +/- eta.
4. Coupling cost (n+1) beta(b); deployment block gap-separated; Beta law not DKW; Kolmogorov distance for the drift penalty.
5. W1 bound is sqrt(2 L W1), not L W1.
6. Sharpness construction moves bottom-epsilon mass to a far point M; constant is 1.
7. Linear decay and Delta/3 are assumptions.
8. Tenor violation is model inconsistency, not static arbitrage.
9. Theorem 9's blocked rate N^{-r/(2r+3)} is not minimax in any coverage formulation (Barber and Pananjady 2026 marginal N^{-r/(r+1)} without blocking; unblocked sample quantile N^{-1/2} conditionally for r>1). Never call it minimax. Blocking buys the exact Beta law, not rate.
10. The deficit sqrt(b/N) + N b^{-(r+1)} is the expected calibration-conditional shortfall from Theorem 6(ii); Theorem 6(i) has no sqrt(b/N) term. Quote the exact minimiser (2(r+1))^{2/(2r+3)} N^{3/(2r+3)}, never the bare balance N^{3/(2r+3)}.
11. The minimax object of Theorem 9 is the TWO-SIDED calibration-conditional coverage error |F_P(T) - (1-alpha)| at confidence delta over B_r; one-sided deficit over all procedures is degenerate (T = +infinity). Marginal coverage is left to Barber and Pananjady (2026); their Theorem 2 is a lower bound for split conformal only.
12. Cite Barber and Pananjady (2026) and Halkiewicz (2026) wherever Theorem 9 or Theorem 6(i) is discussed. Halkiewicz's lower bound is drift-driven; Theorem 9(iii) is mixing-driven. Never claim the first optimal-design result for conformal prediction under dependence.

13. Proposition 2: the "17% curvature understatement" is withdrawn. Total vol-of-vol variance exceeds the time-changed value by (2/3) nu^2 Delta, but the smile-relevant effective parameters differ by 0.013% (nu_eff^2) and 0.12% (rho_eff nu_eff), about 0.002 bp on the smile. Never claim Lemma 1 understates curvature.
14. Attributions (librarian, 2026-09-09): Lemma 1 is Lyashenko-Mercurio (time-change remark also in Willems 2020 Remark 3.1); Prop 2's HLW treatment is Willems 2020 Thms 4.1-4.2; Prop 7's sqrt(2 L W1) inequality is Ross (2011) and Xu et al. (2025) Prop. 1, specialised not claimed; Thm 6(ii) cites Vovk (2012) Prop. 2b, binomial form, "Beta form of".
15. Assumption (mixing) is placed on the market STATE process generating both the fitting sample and the hedging errors, not on the error process alone (conformal referee, ch3). Theorem 6(ii) no longer contains the normal approximation to the Beta quantile or the "2.3 times" factor; those are a remark.
16. The non-estimability of beta(b) is established by construction in Chapter 3; Adams and Nobel (2010) support only "no distribution-free rate under ergodicity alone" (librarian, batch 1). alfeus2026 is dated 19 February 2026.
