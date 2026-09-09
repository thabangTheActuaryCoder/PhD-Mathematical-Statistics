# certify — blocked conformal certificate for hedging error

Reference implementation for Chapter 3 (ground-truth Theorem 6, Proposition 7,
Theorem 9(i) of `Council Workspace/13-mathematics-3yr.tex`). Pure `numpy` + `scipy`, one module.
The test file regenerates every cell of Chapter 3's Table 3.1 (`tab:example`) and the
worked-example numbers of Section 3.7; `fig_example.py` produces the series of `fig:example`.

```
cd thesis/code
uv run --with numpy --with scipy python certify/tests/test_certify.py   # ~15 s, 7 tests
uv run --with numpy --with scipy --with pytest pytest certify/tests -s  # same tests
uv run --with numpy --with scipy python certify/fig_example.py          # ~6 s, writes certify/fig_example.csv (+ .png if matplotlib)
```

## What is implemented (`certify/__init__.py`)

| # | Function | Content |
|---|---|---|
| 1 | `blocks(N, b, n_fit=0)`, `deployment_start` | `n = floor((N - s0)/(2b))` blocks of length `b`, gaps of exactly `b`, trailing gap `b` inside the record (ch3: 250 + 240 + 10 = 500); with `n_fit = 0` this is `n = floor(N/(2b))` of Thm 9(i). First block `b` after the fitting prefix; deployment block starts at `N`. |
| 2 | `block_scores(x, starts, b)` | score = summed per-period hedging error over the block (signed); `x` 1-D or `(paths, time)`. |
| 3 | `conformal_k`, `conformal_threshold` | `k = ceil((1-alpha)(n+1))`, `q_hat = S_(k)`; `+inf` if `k > n`; row-wise on 2-D scores. |
| 4 | `certificate(n, b, alpha, beta_fn, delta, delta_prime, dK)` | Thm 6(i) `1-alpha-dK-(n+1)beta(b)`; Thm 6(ii) `b_{n,k}(delta) - dK - beta(b)/delta'` holding w.p. `>= 1-delta-n beta(b)`; `beta_quantile` = `scipy.stats.beta.ppf(delta, k, n+1-k)`; `dkw_level` = `1-alpha-sqrt(log(1/delta)/(2n))`. `dK` is a stress input or `sqrt_drift_bound(...)`. `beta_fn` is supplied, never estimated (ch3 Sec. 3.5). |
| 5 | `W1_hat`, `dK_hat`, `sqrt_drift_bound(L, W1)` | 1-D empirical `W1 = int |F_P - F_Q|` on the pooled grid; two-sample KS; Prop 7 bound `sqrt(2 L W1)`. |
| 6 | `stationary_bootstrap_quantiles(x, b, alpha, B, rng)` | Politis–Romano stationary bootstrap (geometric blocks, mean `b`, circular) of the `(1-alpha)` quantile of all overlapping block sums. Empirical comparison only; no theorem (ground truth: bootstrap theorem dropped). |
| 7 | `deficit_curve(N, r, bs)`, `optimal_block_length(N, r)`, `optimal_deficit(N, r)`, `balance_block_length(N, r)` | `f(b) = sqrt(b/N) + N b^{-(r+1)}`; its exact minimiser `b* = (2(r+1))^{2/(2r+3)} N^{3/(2r+3)}` and value `f(b*) = (2r+3)/(2(r+1)) (2(r+1))^{1/(2r+3)} N^{-r/(2r+3)}` (Thm 9(i)); the bare balance `N^{3/(2r+3)}` is kept under its own name and is **not** the minimiser (GROUND-TRUTH correction 10). |
| 8 | `expected_shortfall_bound(N, b, beta_fn)` | Thm 9(i) with constants: `E[(1-alpha-F_P(q_hat))^+] <= 1/(2 sqrt(n+2)) + (n+1) beta(b)` from Thm 6(ii), with the `n` that `b` yields. (Replaces the former `deficit_actual`, which used a DKW slack.) |
| — | `ar1_beta_bound(phi)`, `ar1_beta_exact`, `ar1_block_var`, `ar1_block_sd`, `ar1_drift_dK`, `simulate_ar1` | Gaussian AR(1) example of ch3 Sec. 3.7. |

### The AR(1) mixing constant
`ar1_beta_bound(phi)` implements Chapter 3 Lemma `lem:ar1`, first inequality:
`beta(k) <= (1/2) sqrt(-log(1 - phi^{2k}))` (Markov property, Pinsker, Jensen; `E KL = -log(1-phi^{2k})/2`).
At `phi = 0.5, k = 10` it gives `2^-11 = 4.883e-4`; the exact value by quadrature (`ar1_beta_exact`) is `3.108e-4`
(bound 1.57 times loose). The looser forms `(1/2)|phi|^k (1-phi^{2k})^{-1/2} <= |phi|^k/(2 sqrt(1-phi^2))`
(= 5.638e-4, the constant this code used before 2026-09-09) and ch2's `|phi|^k/sqrt 2` (= 6.905e-4) are valid
but are not used here; the thesis quotes each with its source and does not "correct" one into another.

## Numbers obtained (tests/test_certify.py)

Setting of ch3 Sec. 3.7: Gaussian AR(1), `phi = 0.5`, stationary variance `v = 1`, `N = 500`, `alpha = 0.1`,
`delta = delta' = 0.05`, no fitting prefix, deployment drift `mu = 0.05` per period
(`Q = N(b mu, v_b)`, `dK = 2 Phi(b mu/(2 sqrt v_b)) - 1`). Every cell agrees with Table 3.1 to the digits printed there.

| Quantity | b = 5 | b = 10 | b = 20 |
|---|---|---|---|
| `n = floor(N/(2b))`, `k` | 50, 46 | 25, 24 | 12, 12 |
| `k/(n+1)` | 0.9020 | 0.9231 | 0.9231 |
| `beta(b)` (lem:ar1) | 1.563e-2 | 4.883e-4 | 4.768e-7 |
| `(n+1) beta(b)` | 0.7971 | 0.0127 | 6.2e-6 |
| `v_b` | 11.125 | 26.0039 | 56.0000 |
| `dK(P,Q)` | 0.0299 | 0.0391 | 0.0533 |
| marginal level, Thm 6(i) | 0.0730 | **0.8482** | 0.8467 |
| `b_{n,k}(0.05)` | 0.8262 | **0.8239** | 0.7791 |
| DKW form `1-alpha-sqrt(log 20/(2n))` | — | 0.6552 | — |
| `beta(b)/delta'` | 0.3126 | 0.0098 | 9.5e-6 |
| conditional level, Thm 6(ii) | 0.4837 | **0.7750** | 0.7258 |
| confidence `1-delta-n beta(b)` | 0.1686 | 0.9378 | 0.9500 |

Also checked: `E F_Q(q_hat*) = E Phi(Phi^{-1}(U_(24)) - 0.0981) = 0.90889` (quadrature against Beta(24,2));
at `phi = 0.8`: `beta(10) = 0.0538`, `26 beta(10) = 1.40`, `beta(20) = 0.00576`, `13 beta(20) = 0.0749`.

Monte Carlo of the whole procedure (10^4 replications, seed 20260909, drift `mu = 0.05` on the deployment block, `b = 10`):
coverage **0.9113** (se 0.0028), inside ch3's predicted band [0.896, 0.922] and above the certified 0.8482;
mean `F_Q(q_hat)` 0.9096 against the coupled value 0.9089; `P(F_Q(q_hat) >= 0.7750) = 0.9710 >= 0.9378`.

`fig_example.py` (10^4 replications per point, seed 20260909, `b = 2..50`, `phi in {0.5, 0.8}`): at `phi = 0.5` the
breach frequency is 0.109 / 0.093 / 0.098 at `b = 5, 10, 20` against the bound `alpha`-excess
`(n+1)beta(b) + (1-k/(n+1)) + dK` of 0.925 / 0.129 / 0.130; at `phi = 0.8` it is 0.112 / 0.089 / 0.091 against 8.72 / 1.50 / 0.186.
The realised breach rate never exceeds the bound; almost all the slack is in the coupling term.

Drift check (Prop 7, not a ch3 number): `P = N(0, sd^2)`, `Q = N(0.5 sd, sd^2)`, `sd = 5.099`, `L = 1/(sd sqrt(2 pi))`,
4000 vs 400 samples: true `dK = 0.1974`, `dK_hat = 0.2005`, `W1_hat = 2.952` (true 2.944),
`sqrt(2 L W1_hat) = 0.632 >= 0.197`; the false linear form gives `0.200` and fails on `delta_0` vs `U[0,1/L]` (0.5 < 1).

Theorem 9(i) at `N = 500`, `r = 2`: `b* = 23.93` (integer argmin 24), `f(b*) = 0.2553 = 1.51 N^{-r/(2r+3)}`;
the bare balance `N^{3/(2r+3)} = 14.35` is not the minimiser. With the actual constants for `phi = 0.5`
(`expected_shortfall_bound`), the bound is minimised at `b = 11` (0.1077; 0.1089 at `b = 10`): geometric mixing lies in
every `B_r`, so the AR(1) example does not illustrate `b*` (LESSONS code-conformal ch4 entry).

Bootstrap comparison (200 reps, `B = 200`, no drift, `v = 1`): coverage of the deployment score by the conformal
threshold 0.935; by the median stationary-bootstrap quantile 0.860; by its 95% upper envelope 0.910. Mean thresholds
7.70 / 6.00 / 7.61 against the true `P`-quantile 6.54. The bootstrap median under-covers (it targets the quantile, not a
prediction bound); the conformal threshold over-covers by construction of `k`.

## Not done / open
- `dK` is an input: the certificate never sees deployment scores; Chapter 6 supplies `dK_hat` or `sqrt(2 L W1_hat)` from observed deployment scores with an assumed `L`.
- The dependent-data rate for `W1_hat` (Thm 9(v), Dedecker–Merlevède) is not implemented; only the estimator is.
- `blocks` discards the tail of the record shorter than `2b`; no attempt to squeeze in one more block.
- No calibration, caplet-stripping or score module exists yet (ground-truth timetable months 5–9, 12–17); Appendix C must not describe one.
