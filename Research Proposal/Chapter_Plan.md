# Mathematical weight and chapter plan (2026-09-09)
Companion to 11-PROPOSAL-recommended-topic.md. Web version published as the "ZARONIA Thesis Mathematics" artifact.

## Gauge (1 = MSc exercise, 5 = could fail)
| Result | Kind | Difficulty | Deepest tool | Carries doctorate |
|---|---|---|---|---|
| Lemma 2.1 time-changed SABR | cited | 1 | Ito time change (DDS) | no |
| Thm 1 identified component | expansion + error bound | 3 | forward measures, Hagan expansion | partly |
| Thm 2 non-identifiability of rho_B | construction | 4 | sensitivity calculus, two-model matching | yes (finance) |
| Thm 3 tenor consistency | algebraic | 3 | moment matching | no |
| Thm 4 coverage under mixing + drift | theorem | 4 | Berbee coupling, DKW, TV | YES, spine |
| Prop 5 drift term estimable | proposition | 3 | anti-concentration, empirical W1 (Fournier-Guillin) | supports 4 |
| Thm 6 vs block bootstrap | proposition, partly empirical | 2-3 (risk) | bootstrap asymptotics | no, may be demoted |
| Thm 7 impossibility | theorem | 3 | Le Cam two-point | YES |

~40% proof, ~25% derivation/modelling, ~35% data/validation/application.
Not needed anywhere: Malliavin, rough paths, G-expectation, optimal transport, reflected BSDEs, deep-learning theory.

## Prerequisites to learn (months)
Brownian stochastic calculus (1-4); forward measures / multi-curve (3-6); SABR / Hagan expansions as a user (4-7); mixing + blocking/coupling (6-10); conformal + non-exchangeable extensions (1-6); Le Cam method (1 month); multi-curve bootstrap in code (3-9).

## Setting
(W,Z) Brownian with d<W,Z> = rho dt. Compounded rate R(T,T+D) = (1/D)(prod(1+r_i d_i) - 1). Forward F_t = E^{T+D}[R | F_t], martingale under Q^{T+D}. JIBAR forward L_t fixed at T. Fallback L -> R + s. Basis B = L - F - s.
Decay g(t) = 1 (t <= T), (T+D-t)/D (T < t <= T+D); tau(t) = int_0^t g^2; tau(T+D) = T + D/3.
dF = g alpha F^beta dW, d alpha = g nu alpha dZ.

## Statements
Lemma 2.1: (F, alpha) in clock tau is constant-parameter SABR; caplet_R(K') = Hagan(F0, K', T + D/3; alpha0, beta, rho, nu). Proof: DDS on (int g dW, int g dZ).

Thm 1 (target): with eps = eta sqrt(T) the basis-vol scale, observable set S = {sigma_L(K,T)} U {E[B_T]} U {s}:
  sigma_F(K - s, T + D) = Phi_0(sigma_L, s, D, E[B_T]) + rho_B eps Phi_1(K,T,D) + O(eps^2) + O(D^2),
  Phi_0 = strike shift + time change + in-advance/in-arrears convexity (identified); Phi_1 explicit, nonzero.
  Route: L = F + B + s; expand JIBAR caplet under Q^T and compounded caplet under Q^{T+D} to O(eps); rho_B enters via Cov(B, alpha) only in the compounded caplet.
  Failure: convexity term may carry rho_B at O(eps); then identified part shrinks.

Thm 2 (target): for every rho_bar exist models M+, M- with rho_B = +/- rho_bar matching all JIBAR caplets to O(eps^2) and E[B_T] exactly, while wing compounded caplets differ by 2 rho_bar eps |Phi_1| + O(eps^2). Consistent set contains a one-parameter family in rho_B.
  Route: sensitivities of observables to rho_B vanish at O(eps); flip sign, re-solve remaining parameters (needs full rank of observable map).
  Failure: rank deficiency -> more than one unidentified parameter (stronger negative, weaker clean statement).

Thm 3 (target): nested windows: 1 + R13 D13 = (1 + R12 D12)(1 + R23 D23). Per-tenor time-changed SABR with common driver consistent to O(D^2) iff
  alpha13^2 D13^2 tau13 = alpha12^2 D12^2 tau12 + alpha23^2 D23^2 tau23 + 2 alpha12 alpha23 D12 D23 c_{12,23}, plus two constraints on rho, nu. Violation -> static arbitrage 6M caplet vs 3M caplet portfolio.

Thm 4 (target, spine): policy pi fixed on D_fit; per-period hedging error E_t stationary beta-mixing, beta(k) <= C k^{-r}, r > 1; n calibration blocks of length b separated by gaps >= b, disjoint from D_fit; block scores S_j ~ P^S; deployment score S_0 ~ Q^S; q_hat = ceil((1-alpha)(n+1))-th order statistic. With prob >= 1 - delta over calibration:
  P(S_0 <= q_hat | D_fit, S_1..S_n) >= 1 - alpha - d_TV(P^S, Q^S) - sqrt(log(2/delta)/(2n)) - 2 n beta(b).
  Route: (i) Berbee coupling of separated blocks with independent copies at cost 2 n beta(b); (ii) split-conformal exchangeability on coupled sample + DKW for the 1-delta statement; (iii) TV bound on the coverage event (Barber et al. 2023).
  Failure: not in proof; d_TV may be large -> vacuous bound, reported honestly (Thm 7 says unavoidable).

Prop 5 (target): if Q^S has density <= L, |Q^S(S <= q) - P^S(S <= q)| <= L W_1(P^S, Q^S); W_1 in 1-D estimable at O(n^{-1/2} + m^{-1/2}) (Fournier-Guillin 2015). Plug-in upper bound on drift with its own confidence.

Thm 6 (target, may demote): stationary bootstrap has coverage 1 - alpha + O(n^{-1/2}) under stationarity with unknown constants and no finite-sample statement; under drift 1 - alpha - d_TV + o(1). For n below the regime where bootstrap asymptotics provably bind, the certificate is the only one with a provable level. Substantive comparison is empirical.

Thm 7 (target): for any procedure T from P^S-calibration data to a threshold, exist P^S, Q^S with d_TV = eps such that P_P(S <= T) >= 1 - alpha implies P_Q(S <= T) <= (1 - eps)(1 - alpha) = 1 - alpha - eps(1 - alpha).
  Proof: Q^S = (1 - eps) P^S + eps delta_{+inf}. Half a page (Le Cam two-point). Drift term in Thm 4 sharp up to factor (1 - alpha).

## Sub-articles by year
Y1 (2027): A "Compounded rates as time-changed SABR: a self-contained note" (Ch 2, ~9k words, Lemma 2.1 + code); B "The South African benchmark transition: a factual record" (Ch 1, ~7k words). Read Barber et al. and Oliveira et al. line by line; USD data; ZAR data agreement; proposal defence months 10-12.
Y2 (2028): C "Identifiability of the successor-rate smile under a benchmark fallback" (Ch 3 + 7a, ~14k words; Thms 1, 2; USD validation) -> Paper 1 (QF / JCF).
Y3 (2029): D "Finite-sample certification of hedging error under dependence and drift, with a matching lower bound" (Ch 5, 6, 7b, ~16k words; Thms 4, 6, 7, Prop 5; USD certificate test) -> Paper 2, doctoral (EJS / Bernoulli).
Y4 (2030): E "Tenor consistency of compounded-rate smiles" (Ch 4, ~6k words; Thm 3); F "The converted JIBAR book: a certified model-risk reserve" (Ch 8, ~12k words; two years of realised converted-book data) -> Paper 3 (SAJEMS / IAJ / F&S).
Y5 (2031, part-time buffer): Ch 9 conclusions, thesis introduction, assembly (~8k new words, ~70k total), submission, examination.

Done-when tests per sub-article are in the web version.
Order rationale: D after C (Thm 4 needs the fixed policy and ambiguity set from Thms 1-2); F last (calibration sample does not exist until the converted book has traded two years); A, B first (what the proposal defence examines).
