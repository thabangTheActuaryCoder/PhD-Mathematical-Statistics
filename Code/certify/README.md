# certify — blocked conformal certificate for hedging error

Reference implementation for Chapter 3 (ground-truth Theorem 6, Proposition 7,
Theorem 9(i) of `13-mathematics-3yr.tex`). Pure `numpy` + `scipy`, one module.

```
cd thesis/code
uv run --with numpy --with scipy python certify/tests/test_certify.py   # ~20 s
uv run --with numpy --with scipy --with pytest pytest certify/tests -s  # same tests
```

## What is implemented (`certify/__init__.py`)

| # | Function | Content |
|---|---|---|
| 1 | `blocks(N, b, n_fit=0)`, `deployment_start` | `n = floor((N - s0 + b)/(2b))` blocks of length `b`, gaps of exactly `b`, first block `b` after the fitting prefix (`s0 = n_fit + b`); deployment block starts `b` after the last block (Assumption "Mixing and separation"). |
| 2 | `block_scores(x, starts, b)` | score = summed per-period hedging error over the block (signed). |
| 3 | `conformal_k`, `conformal_threshold` | `k = ceil((1-alpha)(n+1))`, `q_hat = S_(k)`; `+inf` if `k > n`. |
| 4 | `certificate(n, b, alpha, beta_fn, delta, delta_prime, dK)` | Thm 6(i) `1-alpha-dK-(n+1)beta(b)`; Thm 6(ii) `b_{n,k}(delta) - dK - beta(b)/delta'` holding w.p. `>= 1-delta-n beta(b)`; `beta_quantile` = `scipy.stats.beta.ppf(delta, k, n+1-k)`; `dkw_level` = `1-alpha-sqrt(log(1/delta)/(2n))`. `dK` is a plug-in placeholder (use `dK_hat` or `sqrt_drift_bound`). `beta_fn` is supplied, never estimated (Adams–Nobel remark). |
| 5 | `W1_hat`, `dK_hat`, `sqrt_drift_bound(L, W1)` | 1-D empirical `W1 = int |F_P - F_Q|` on the pooled grid; two-sample KS; Prop 7 bound `sqrt(2 L W1)`. |
| 6 | `stationary_bootstrap_quantiles(x, b, alpha, B, rng)` | Politis–Romano stationary bootstrap (geometric blocks, mean `b`, circular) of the `(1-alpha)` quantile of all overlapping block sums. Returns the `B` bootstrap quantiles. Empirical comparison only; no theorem (ground-truth remark on the dropped bootstrap theorem). |
| 7 | `optimal_block_length(N, r)`, `deficit_curve(N, r, bs)`, `deficit_actual` | `N^{3/(2r+3)}` and `E(b,N) = sqrt(b/N) + N b^{-(r+1)}` of Thm 9(i); `deficit_actual` = DKW slack + coupling with the real `n(b)`. |
| — | `ar1_beta_bound(phi)`, `ar1_beta_exact`, `ar1_block_sd`, `simulate_ar1` | Gaussian AR(1) example used by the tests. |

### The AR(1) mixing constant
For a stationary Gaussian AR(1) `X_t = phi X_{t-1} + eps_t`, the code uses
`beta(k) <= C phi^k` with **`C = 1/(2 sqrt(1 - phi^2))`**. Derivation: by the
Markov property `beta(k) = E_x ||P^k(x,.) - pi||_TV`; Pinsker and Jensen give
`beta(k) <= sqrt(E KL / 2)` with `E KL(P^k(x,.) || pi) = -log(1 - phi^{2k})/2`, and
`-log(1-u) <= u/(1-u) <= u/(1-phi^2)` for `u = phi^{2k}`, `k >= 1`.
At `phi = 0.5`: `C = 0.5774`; exact `beta(10) = 3.108e-4` (quadrature), bound `5.638e-4`
(factor 1.8 loose). `ar1_beta_exact` is available to gauge the slack for other `phi`.

## Numbers obtained (tests/test_certify.py, seed 20260909)

Setting: Gaussian AR(1), `phi = 0.5`, unit innovations, `N = 500`, `b = 10`,
`alpha = 0.1`, `delta = delta' = 0.05`, no fitting prefix (`n_fit = 0`; the policy
is fixed and the series is its per-period error), `Q = P` so `dK = 0`.

| Quantity | Value |
|---|---|
| `n` blocks, `k` | 25, 24 |
| `beta(b)` bound `C phi^10` | 5.638e-4 |
| coupling `(n+1) beta(b)` | 0.014659 |
| Thm 6(i) guaranteed marginal coverage | **0.885341** |
| exchangeable target `k/(n+1)` | 0.923077 |
| Beta quantile `b_{25,24}(0.05)` | **0.823879** |
| DKW level `1-alpha-sqrt(log 20 / 50)` | 0.655225 |
| Thm 6(ii) conditional level `b_{n,k}(delta) - beta(b)/delta'` | 0.812603, holding w.p. `>= 0.935905` |
| Monte Carlo (2000 reps) marginal coverage | **0.9310** (se 0.0057) `>= 0.8853` |
| Monte Carlo `P(F_P(q_hat) >= 0.8126)` | 0.9620 `>= 0.9359` |

Both parts of Theorem 6 hold empirically with room; the Beta quantile is 0.169
above the DKW level, i.e. the DKW slack (0.245) is 3.2 times the Beta slack (0.076)
here (the ground truth quotes "about 2.3 times" at `alpha = 0.05`; at `alpha = 0.1`,
`n = 25` it is larger). Empirical coverage 0.931 exceeds even `k/(n+1)`: with `n = 25`
the ceiling in `k` makes the exchangeable target 0.923, and the positive
autocorrelation across the gap adds a little.

Drift check (Prop 7): `P = N(0, sd_S^2)`, `Q = N(0.5 sd_S, sd_S^2)`, `sd_S = 5.888`
(exact block-sum sd), `L = 1/(sd_S sqrt(2 pi))`, 4000 vs 400 samples:
true `dK = 0.1974`, `dK_hat = 0.2005`, `W1_hat = 2.952` (true 2.944),
`sqrt(2 L W1_hat) = 0.632 >= 0.197`; the false linear form would give `0.200`,
which is below the true `dK` in the `delta_0` vs `U[0,1/L]` counterexample (0.5 < 1).

Theorem 9(i) at `r = 2`: balance point `N^{3/(2r+3)} = 14.35`; the exact minimiser
of `sqrt(b/N) + N b^{-(r+1)}` is `(2(r+1))^{2/(2r+3)} N^{3/(2r+3)} = 23.93`
(integer argmin 24). The theorem's `≍` absorbs this constant; the worked example
should quote the exponent, not the number 14. With the actual constants
(DKW slack + coupling, geometric `beta`), the deficit is minimised at `b = 10`
(0.2594) because geometric mixing makes the coupling term negligible for `b >= 8`.

Bootstrap comparison (200 reps, `B = 200`): coverage of the deployment score by the
conformal threshold 0.935; by the median stationary-bootstrap quantile 0.860; by its
95% upper envelope 0.910. Mean thresholds 8.89 / 6.92 / 8.79 against the true
`P`-quantile 7.55. The bootstrap median under-covers (it targets the quantile, not a
prediction bound); the conformal threshold over-covers by construction of `k`.

## Not done / open
- `dK` is a placeholder: the certificate never sees deployment scores; Chapter 6 supplies `dK_hat` or `sqrt(2 L W1_hat)` from observed deployment scores with an assumed `L`.
- The dependent-data rate for `W1_hat` (Thm 9(iii)) is not implemented; only the estimator is.
- `blocks` discards the tail of the record shorter than `2b`; no attempt to squeeze in one more block.
