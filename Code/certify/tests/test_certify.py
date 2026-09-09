"""Chapter 3 worked example (Sec. 3.7, Table 3.1): Gaussian AR(1), phi = 0.5, v = 1, N = 500,
alpha = 0.1, delta = delta' = 0.05, deployment drift mu = 0.05 per period, b in {5, 10, 20}.
Run:  cd thesis/code && uv run --with numpy --with scipy python certify/tests/test_certify.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
import numpy as np
from scipy.stats import norm, beta as Beta
from scipy.integrate import quad
import certify as C

PHI, N, B, ALPHA, DELTA, DELTAP, MU, REPS, SEED = 0.5, 500, 10, 0.1, 0.05, 0.05, 0.05, 10_000, 20260909
SIGMA = np.sqrt(1 - PHI ** 2)          # innovation sd giving stationary variance v = 1 (ch3 units)

def test_blocking():
    st = C.blocks(N, B)
    assert len(st) == N // (2 * B) and st[0] == 0 and np.all(np.diff(st) == 2 * B)
    assert st[-1] + 2 * B <= N                                      # trailing gap inside the record
    assert C.deployment_start(st, B) == N                           # deployment block starts at N
    assert [len(C.blocks(N, b)) for b in (5, 10, 20)] == [50, 25, 12]
    st_fit = C.blocks(N, B, n_fit=50)
    assert st_fit[0] >= 50 + B                                      # disjoint from D_fit, gap b
    assert C.block_scores(np.ones(N), st, B)[0] == B and C.block_scores(np.ones((3, N)), st, B).shape == (3, len(st))

def test_ar1_bound_is_a_bound():
    beta_fn = C.ar1_beta_bound(PHI)
    ex = C.ar1_beta_exact(PHI, B)
    print(f"AR(1) phi={PHI}: Lemma ar1 bound beta({B}) = {beta_fn(B):.4e}, exact (quadrature) = {ex:.4e}, ratio {beta_fn(B)/ex:.2f}")
    assert beta_fn(B) >= ex
    assert abs(beta_fn(B) - 2 ** -11) < 1e-9                        # ch3: 2^-11 = 4.883e-4 to four figures
    # ch3 "Reading the table": phi = 0.8
    b8 = C.ar1_beta_bound(0.8)
    assert abs(b8(10) - 0.0538) < 5e-5 and abs(26 * b8(10) - 1.40) < 5e-3
    assert abs(b8(20) - 0.00576) < 5e-6 and abs(13 * b8(20) - 0.0749) < 5e-5

# Table 3.1 of ch3-certification.tex, column by column (b = 5, 10, 20).
TABLE = {
    "n":                (50, 25, 12),
    "k":                (46, 24, 12),
    "k/(n+1)":          (0.9020, 0.9231, 0.9231),
    "beta(b)":          (1.563e-2, 4.883e-4, 4.768e-7),
    "(n+1)beta(b)":     (0.7971, 0.0127, 6.2e-6),
    "dK":               (0.0299, 0.0391, 0.0533),
    "marginal":         (0.0730, 0.8482, 0.8467),
    "b_{n,k}(0.05)":    (0.8262, 0.8239, 0.7791),
    "beta(b)/delta'":   (0.3126, 0.0098, 9.5e-6),
    "conditional":      (0.4837, 0.7750, 0.7258),
    "confidence":       (0.1686, 0.9378, 0.9500),
}

def table_3_1(b):
    beta_fn = C.ar1_beta_bound(PHI)
    n = len(C.blocks(N, b))
    dK = C.ar1_drift_dK(PHI, b, MU)
    c = C.certificate(n, b, ALPHA, beta_fn, DELTA, DELTAP, dK=dK)
    return {"n": n, "k": c["k"], "k/(n+1)": c["k"] / (n + 1), "beta(b)": c["beta_b"], "(n+1)beta(b)": c["coupling"],
            "dK": dK, "marginal": c["marginal"], "b_{n,k}(0.05)": c["beta_quantile"], "beta(b)/delta'": c["markov"],
            "conditional": c["conditional"], "confidence": c["conditional_prob"], "dkw": c["dkw_level"]}

def test_table_3_1():
    cols = [table_3_1(b) for b in (5, 10, 20)]
    print(f"Table 3.1 (phi={PHI}, N={N}, alpha={ALPHA}, mu={MU}, delta=delta'={DELTA}):")
    for key, targets in TABLE.items():
        vals = [c[key] for c in cols]
        print(f"  {key:16s}" + "".join(f"{v:>14.4e}" if abs(v) < 1e-3 else f"{v:>14.4f}" for v in vals) + f"   (ch3: {targets})")
        for v, t in zip(vals, targets):
            tol = 0.5e-4 if isinstance(t, float) and t >= 1e-3 else abs(t) * 0.01   # 4 dp, or 1% for the tiny cells
            assert abs(v - t) <= tol + 1e-12, (key, v, t)
    assert abs(C.ar1_block_var(PHI, 10) - 26.0039) < 5e-5 and abs(C.ar1_block_var(PHI, 5) - 11.125) < 1e-9
    assert abs(cols[1]["dkw"] - 0.6552) < 5e-5                      # DKW form vs exact 0.8239
    # E F_Q(q_hat*) = E Phi(Phi^{-1}(U_(24)) - b mu / sqrt(v_b)) = 0.9089 (ch3 datanote), U_(24) ~ Beta(24, 2)
    shift = B * MU / np.sqrt(C.ar1_block_var(PHI, B))
    EFQ = quad(lambda u: norm.cdf(norm.ppf(u) - shift) * Beta.pdf(u, 24, 2), 0, 1)[0]
    print(f"  E F_Q(q_hat*) = {EFQ:.5f} (ch3: 0.90889); shift b mu / sqrt(v_b) = {shift:.4f} (ch3: 0.0981)")
    assert abs(EFQ - 0.90889) < 5e-5 and abs(shift - 0.0981) < 5e-5

def test_monte_carlo_coverage():
    """Ch3 scenario: calibration on [0, N), deployment block at N with per-period drift mu."""
    rng = np.random.default_rng(SEED)
    c = table_3_1(B)
    st = C.blocks(N, B); d0 = C.deployment_start(st, B)
    X = C.simulate_ar1(PHI, d0 + B, REPS, rng, sigma=SIGMA)
    qhat = C.conformal_threshold(C.block_scores(X, st, B), ALPHA)
    S0 = X[:, d0:d0 + B].sum(1) + B * MU
    cov = np.mean(S0 <= qhat); se = np.sqrt(cov * (1 - cov) / REPS)
    sd = np.sqrt(C.ar1_block_var(PHI, B))
    FQ = norm.cdf((qhat - B * MU) / sd)                             # exact conditional coverage under Q
    frac_cond = np.mean(FQ >= c["conditional"])
    print(f"Monte Carlo ({REPS} reps, seed {SEED}): coverage = {cov:.4f} (se {se:.4f}); Thm 6(i) level {c['marginal']:.4f}; "
          f"ch3 predicts realised coverage in [0.896, 0.922]; mean F_Q(q_hat) = {FQ.mean():.4f} (coupled value 0.9089)")
    print(f"  P(F_Q(q_hat) >= {c['conditional']:.4f}) = {frac_cond:.4f}; Thm 6(ii) guarantees >= {c['confidence']:.4f}")
    assert cov >= c["marginal"] and frac_cond >= c["confidence"]
    assert 0.896 - 3 * se <= cov <= 0.922 + 3 * se

def test_drift_bound():
    rng = np.random.default_rng(SEED + 1)
    sd = C.ar1_block_sd(PHI, B); shift = 0.5 * sd
    p = rng.normal(0, sd, 4000); q = rng.normal(shift, sd, 400)     # Q shifted by half a block-sd
    L = 1 / (sd * np.sqrt(2 * np.pi))
    dK_true = 2 * norm.cdf(shift / (2 * sd)) - 1
    w1, dk = C.W1_hat(p, q), C.dK_hat(p, q)
    bound = C.sqrt_drift_bound(L, w1)
    print(f"Drift (Prop 7): true dK = {dK_true:.4f}, plug-in dK_hat = {dk:.4f}, W1_hat = {w1:.4f} (true {shift:.4f}), "
          f"sqrt(2 L W1_hat) = {bound:.4f}, linear L*W1_hat = {L*w1:.4f}")
    assert bound >= dK_true                                          # Proposition 7 holds
    # the counterexample that killed the linear bound: P = delta_0, Q = U[0, 1/L]
    assert C.sqrt_drift_bound(1.0, 0.5) >= 1.0 - 1e-12 and 1.0 * 0.5 < 1.0

def test_optimal_block_length():
    r = 2.0
    bs = np.arange(2, 60)
    bstar, bal = C.optimal_block_length(N, r), C.balance_block_length(N, r)
    curve = C.deficit_curve(N, r, bs)
    assert abs(bstar - 23.93) < 5e-3 and abs(bal - 14.35) < 5e-3    # ground truth: 23.9 vs 14.3
    assert abs(bs[curve.argmin()] - bstar) <= 1
    assert abs(C.optimal_deficit(N, r) - C.deficit_curve(N, r, [bstar])[0]) < 1e-12
    assert abs(C.optimal_deficit(N, r) / N ** (-r / (2 * r + 3)) - 1.51) < 5e-3
    # first-order condition: f'(b*) = 0
    h = 1e-4; assert abs((C.deficit_curve(N, r, [bstar + h])[0] - C.deficit_curve(N, r, [bstar - h])[0]) / (2 * h)) < 1e-8
    beta_fn = C.ar1_beta_bound(PHI)
    actual = np.array([C.expected_shortfall_bound(N, b, beta_fn) for b in bs])
    print(f"Theorem 9(i), r={r}, N={N}: b* = {bstar:.2f} (integer argmin {bs[curve.argmin()]}), f(b*) = {C.optimal_deficit(N, r):.4f} "
          f"= {C.optimal_deficit(N, r) / N ** (-r / (2 * r + 3)):.2f} N^(-r/(2r+3)); bare balance N^(3/(2r+3)) = {bal:.2f} (not the minimiser). "
          f"Expected-shortfall bound 1/(2 sqrt(n+2)) + (n+1)beta(b) for phi={PHI}: argmin b = {bs[actual.argmin()]} ({actual.min():.4f}); at b=10: {actual[bs==10][0]:.4f}")

def test_bootstrap_comparison(reps=200):
    rng = np.random.default_rng(SEED + 2)
    st = C.blocks(N, B); d0 = C.deployment_start(st, B)
    X = C.simulate_ar1(PHI, d0 + B, reps, rng, sigma=SIGMA)
    S0 = X[:, d0:d0 + B].sum(1)
    qc = C.conformal_threshold(C.block_scores(X, st, B), ALPHA)
    qb = np.array([C.stationary_bootstrap_quantiles(x[:N], B, ALPHA, 200, rng) for x in X])
    q_med, q_up = np.median(qb, 1), np.quantile(qb, 0.95, 1)
    print(f"Bootstrap comparison ({reps} reps, B=200, no drift): coverage conformal = {np.mean(S0<=qc):.3f}, "
          f"bootstrap median quantile = {np.mean(S0<=q_med):.3f}, bootstrap 95% upper = {np.mean(S0<=q_up):.3f}; "
          f"mean thresholds {qc.mean():.3f} / {q_med.mean():.3f} / {q_up.mean():.3f}; true P-quantile {norm.ppf(1-ALPHA)*C.ar1_block_sd(PHI,B,SIGMA):.3f}")

if __name__ == "__main__":
    for f in [test_blocking, test_ar1_bound_is_a_bound, test_table_3_1, test_monte_carlo_coverage,
              test_drift_bound, test_optimal_block_length, test_bootstrap_comparison]:
        f(); print(f"PASS {f.__name__}")
