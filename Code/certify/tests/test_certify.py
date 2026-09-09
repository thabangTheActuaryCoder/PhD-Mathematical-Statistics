"""Chapter 3 worked example: Gaussian AR(1), phi = 0.5, N = 500, b = 10, alpha = 0.1, delta = 0.05.
Run:  cd thesis/code && uv run --with numpy --with scipy python certify/tests/test_certify.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
import numpy as np
from scipy.stats import norm
import certify as C

PHI, N, B, ALPHA, DELTA, DELTAP, REPS, SEED = 0.5, 500, 10, 0.1, 0.05, 0.05, 2000, 20260909

def test_blocking():
    st = C.blocks(N, B)
    assert st[0] == 0 and np.all(np.diff(st) == 2 * B) and st[-1] + B <= N
    assert C.deployment_start(st, B) - (st[-1] + B) >= B            # deployment gap
    st_fit = C.blocks(N, B, n_fit=50)
    assert st_fit[0] >= 50 + B                                      # disjoint from D_fit, gap b
    assert len(C.block_scores(np.ones(N), st, B)) == len(st) and C.block_scores(np.ones(N), st, B)[0] == B

def test_certificate_numbers():
    beta_fn, Cc = C.ar1_beta_bound(PHI)
    n = len(C.blocks(N, B))
    cert = C.certificate(n, B, ALPHA, beta_fn, DELTA, DELTAP, dK=0.0)
    print(f"AR(1) phi={PHI}: beta(k) <= C phi^k with C = 1/(2 sqrt(1-phi^2)) = {Cc:.4f}; "
          f"exact beta({B}) = {C.ar1_beta_exact(PHI, B):.3e}, bound = {beta_fn(B):.3e}")
    for key, v in cert.items():
        print(f"  {key:16s} = {v:.6f}" if isinstance(v, float) else f"  {key:16s} = {v}")
    assert cert["n"] == 25 and cert["k"] == 24
    assert cert["beta_quantile"] > cert["dkw_level"]               # Beta law tighter than DKW
    assert beta_fn(B) >= C.ar1_beta_exact(PHI, B)                   # the bound is a bound

def test_monte_carlo_coverage():
    rng = np.random.default_rng(SEED)
    beta_fn, _ = C.ar1_beta_bound(PHI)
    st = C.blocks(N, B); n = len(st); d0 = C.deployment_start(st, B)
    X = C.simulate_ar1(PHI, d0 + B, REPS, rng)
    qhat = np.array([C.conformal_threshold(C.block_scores(x, st, B), ALPHA) for x in X])
    S0 = X[:, d0:d0 + B].sum(1)
    cov = np.mean(S0 <= qhat)
    cert = C.certificate(n, B, ALPHA, beta_fn, DELTA, DELTAP)
    # exact conditional coverage under the marginal law P of a block score
    Fq = norm.cdf(qhat / C.ar1_block_sd(PHI, B))
    frac_cond = np.mean(Fq >= cert["conditional"])
    se = np.sqrt(cov * (1 - cov) / REPS)
    print(f"Monte Carlo ({REPS} reps): empirical marginal coverage = {cov:.4f} (se {se:.4f}); "
          f"guaranteed (Thm 6(i), dK=0) = {cert['marginal']:.4f}; exchangeable target k/(n+1) = {cert['k']/(n+1):.4f}")
    print(f"  P(F_P(q_hat) >= {cert['conditional']:.4f}) = {frac_cond:.4f}; guaranteed >= {cert['conditional_prob']:.4f} (Thm 6(ii))")
    assert cov >= cert["marginal"]
    assert frac_cond >= cert["conditional_prob"]

def test_drift_bound():
    rng = np.random.default_rng(SEED + 1)
    sd = C.ar1_block_sd(PHI, B); shift = 0.5 * sd
    p = rng.normal(0, sd, 4000); q = rng.normal(shift, sd, 400)     # Q shifted by half a block-sd
    L = 1 / (sd * np.sqrt(2 * np.pi))
    dK_true = 2 * norm.cdf(shift / (2 * sd)) - 1
    w1, dk = C.W1_hat(p, q), C.dK_hat(p, q)
    bound = C.sqrt_drift_bound(L, w1)
    print(f"Drift: true dK = {dK_true:.4f}, plug-in dK_hat = {dk:.4f}, W1_hat = {w1:.4f} (true {shift:.4f}), "
          f"sqrt(2 L W1_hat) = {bound:.4f}, linear L*W1_hat = {L*w1:.4f}")
    assert bound >= dK_true                                          # Proposition 7 holds
    # the counterexample that killed the linear bound: P = delta_0, Q = U[0, 1/L]
    assert C.sqrt_drift_bound(1.0, 0.5) >= 1.0 - 1e-12 and 1.0 * 0.5 < 1.0

def test_optimal_block_length():
    beta_fn, _ = C.ar1_beta_bound(PHI)
    r = 2.0                                                          # geometric beta lies in every B_r
    bs = np.arange(2, 60)
    bstar = C.optimal_block_length(N, r)
    curve = C.deficit_curve(N, r, bs)
    actual = np.array([C.deficit_actual(N, b, ALPHA, beta_fn, DELTA) for b in bs])
    exact = (2 * (r + 1)) ** (2 / (2 * r + 3)) * bstar             # exact minimiser of the curve
    print(f"Theorem 9(i), r={r}: balance point N^(3/(2r+3)) = {bstar:.2f}; exact minimiser (2(r+1))^(2/(2r+3)) N^(3/(2r+3)) = {exact:.2f}; "
          f"integer argmin of sqrt(b/N)+N b^-(r+1) = {bs[curve.argmin()]}; "
          f"argmin of actual DKW+coupling deficit for phi={PHI} = {bs[actual.argmin()]} (deficit {actual.min():.4f}); at b=10: {actual[bs==10][0]:.4f}")
    assert abs(bs[curve.argmin()] - exact) <= 1

def test_bootstrap_comparison(reps=200):
    rng = np.random.default_rng(SEED + 2)
    st = C.blocks(N, B); d0 = C.deployment_start(st, B)
    X = C.simulate_ar1(PHI, d0 + B, reps, rng)
    S0 = X[:, d0:d0 + B].sum(1)
    qc = np.array([C.conformal_threshold(C.block_scores(x, st, B), ALPHA) for x in X])
    qb = np.array([C.stationary_bootstrap_quantiles(x[:N], B, ALPHA, 200, rng) for x in X])
    q_med, q_up = np.median(qb, 1), np.quantile(qb, 0.95, 1)
    print(f"Bootstrap comparison ({reps} reps, B=200): coverage conformal = {np.mean(S0<=qc):.3f}, "
          f"bootstrap median quantile = {np.mean(S0<=q_med):.3f}, bootstrap 95% upper = {np.mean(S0<=q_up):.3f}; "
          f"mean thresholds {qc.mean():.3f} / {q_med.mean():.3f} / {q_up.mean():.3f}; true P-quantile {norm.ppf(1-ALPHA)*C.ar1_block_sd(PHI,B):.3f}")

if __name__ == "__main__":
    for f in [test_blocking, test_certificate_numbers, test_monte_carlo_coverage,
              test_drift_bound, test_optimal_block_length, test_bootstrap_comparison]:
        f(); print(f"PASS {f.__name__}")
