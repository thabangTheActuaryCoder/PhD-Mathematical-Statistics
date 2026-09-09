"""Blocked conformal certificate for hedging error (thesis Chapter 3).

Reference implementation of ground-truth Theorem 6, Proposition 7 and
Theorem 9(i) of "Council Workspace/13-mathematics-3yr.tex", plus the
stationary block bootstrap used only as an empirical comparison.
numpy + scipy only.  All functions are pure; nothing is estimated that
the theory says is not estimable (beta(b) is supplied, never fitted).
"""
import numpy as np
from scipy.stats import beta as _beta, norm
from scipy.integrate import quad

# ---------------------------------------------------------------- blocking

def blocks(N, b, n_fit=0):
    """Start indices of n = floor((N - s0) / (2b)) calibration blocks of length b.

    Layout on the record [0, N):  [fit prefix n_fit][gap b][block][gap b]...[block][gap b].
    Consecutive blocks are separated by gaps of exactly b; the first block
    starts b after the fitting prefix (no gap if n_fit == 0); the record ends
    with a trailing gap of b, so the deployment block starts at N (ch3 Sec. 3.7:
    250 + 240 + 10 = 500).  With n_fit == 0 this is n = floor(N/(2b)) of Thm 9(i).
    """
    s0 = n_fit + b if n_fit > 0 else 0
    n = (N - s0) // (2 * b)              # ponytail: floor; leftover tail is unused
    return s0 + 2 * b * np.arange(max(n, 0))

def deployment_start(starts, b):
    """Earliest admissible deployment-block start: gap b after the last block."""
    return int(starts[-1]) + 2 * b

def block_scores(x, starts, b):
    """Score of each block = summed per-period hedging error over the block.
    x may be 1-D (one path) or 2-D (paths, time); blocks index the last axis."""
    cs = np.cumsum(np.asarray(x, float), axis=-1)
    cs = np.concatenate([np.zeros(cs.shape[:-1] + (1,)), cs], axis=-1)
    starts = np.asarray(starts)
    return cs[..., starts + b] - cs[..., starts]

# ---------------------------------------------------------------- threshold

def conformal_k(n, alpha):
    return int(np.ceil((1 - alpha) * (n + 1)))

def conformal_threshold(scores, alpha):
    """q_hat = k-th order statistic, k = ceil((1-alpha)(n+1)); +inf if k > n.
    scores may be 2-D (paths, n): one threshold per row."""
    s = np.sort(np.asarray(scores, float), axis=-1)
    n = s.shape[-1]
    k = conformal_k(n, alpha)
    return s[..., k - 1] if k <= n else np.full(s.shape[:-1], np.inf)

# ---------------------------------------------------------------- Theorem 6 deficit terms

def beta_quantile(n, k, delta):
    """b_{n,k}(delta) = Beta^{-1}(delta; k, n+1-k), the Beta-law conditional level."""
    return _beta.ppf(delta, k, n + 1 - k)

def dkw_level(n, alpha, delta):
    """DKW corollary: 1 - alpha - sqrt(log(1/delta) / (2n))."""
    return 1 - alpha - np.sqrt(np.log(1 / delta) / (2 * n))

def coupling_cost(n, b, beta_fn):
    """(n+1) beta(b): Berbee/Yu sequential coupling of n blocks, D_fit and deployment."""
    return (n + 1) * beta_fn(b)

def certificate(n, b, alpha, beta_fn, delta=0.05, delta_prime=0.05, dK=0.0):
    """Both parts of Theorem 6 as numbers.  dK is the Kolmogorov distance P vs Q
    (a stress input or `sqrt_drift_bound(...)`); 0 if Q = P."""
    k = conformal_k(n, alpha)
    bb = beta_fn(b)
    return dict(
        n=n, k=k, beta_b=bb,
        coupling=(n + 1) * bb,
        dK=dK,
        marginal=1 - alpha - dK - (n + 1) * bb,                 # Thm 6(i)
        beta_quantile=beta_quantile(n, k, delta),
        dkw_level=dkw_level(n, alpha, delta),
        markov=bb / delta_prime,
        conditional=beta_quantile(n, k, delta) - dK - bb / delta_prime,  # Thm 6(ii)
        conditional_prob=1 - delta - n * bb,                    # holds w.p. >= this
    )

# ---------------------------------------------------------------- Proposition 7 drift bound

def ecdf_gap(p_sample, q_sample):
    """Grid and F_P - F_Q on the pooled sorted sample (right-continuous ECDFs)."""
    p, q = np.sort(np.asarray(p_sample, float)), np.sort(np.asarray(q_sample, float))
    grid = np.union1d(p, q)
    Fp = np.searchsorted(p, grid, side="right") / len(p)
    Fq = np.searchsorted(q, grid, side="right") / len(q)
    return grid, Fp - Fq

def dK_hat(p_sample, q_sample):
    """Plug-in Kolmogorov distance (two-sample KS statistic)."""
    return np.abs(ecdf_gap(p_sample, q_sample)[1]).max()

def W1_hat(p_sample, q_sample):
    """1-D empirical W1 = integral |F_P - F_Q| dx."""
    grid, d = ecdf_gap(p_sample, q_sample)
    return float(np.sum(np.abs(d[:-1]) * np.diff(grid)))

def sqrt_drift_bound(L, W1):
    """Proposition 7: sup_x (F_P - F_Q)(x) <= sqrt(2 L W1) when Q has density <= L."""
    return np.sqrt(2 * L * W1)

# ---------------------------------------------------------------- Theorem 9(i)

def deficit_curve(N, r, bs):
    """f(b) = sqrt(b/N) + N b^{-(r+1)}, the constant-free expected conditional
    shortfall bound of Theorem 9(i) over B_r = {beta(k) <= C k^{-r}}."""
    bs = np.asarray(bs, float)
    return np.sqrt(bs / N) + N * bs ** (-(r + 1))

def optimal_block_length(N, r):
    """Exact minimiser of deficit_curve: b* = (2(r+1))^{2/(2r+3)} N^{3/(2r+3)}
    (ground-truth Thm 9(i); 23.9 at N=500, r=2)."""
    return (2 * (r + 1)) ** (2 / (2 * r + 3)) * N ** (3 / (2 * r + 3))

def optimal_deficit(N, r):
    """f(b*) = (2r+3)/(2(r+1)) (2(r+1))^{1/(2r+3)} N^{-r/(2r+3)} (1.51 N^{-r/(2r+3)} at r=2)."""
    return (2 * r + 3) / (2 * (r + 1)) * (2 * (r + 1)) ** (1 / (2 * r + 3)) * N ** (-r / (2 * r + 3))

def balance_block_length(N, r):
    """Bare balance sqrt(b/N) = N b^{-(r+1)}, i.e. N^{3/(2r+3)}.  NOT the minimiser
    (ground-truth correction 10); kept only to show the gap to optimal_block_length."""
    return N ** (3 / (2 * r + 3))

def expected_shortfall_bound(N, b, beta_fn):
    """Theorem 9(i) with constants: E[(1-alpha-F_P(q_hat))^+] <= 1/(2 sqrt(n+2)) + (n+1) beta(b)
    (from Thm 6(ii) via E|Beta - k/(n+1)| <= sd(Beta)), with the n that b yields."""
    n = len(blocks(N, b))
    return 1 / (2 * np.sqrt(n + 2)) + (n + 1) * beta_fn(b)

# ---------------------------------------------------------------- Gaussian AR(1) example

def ar1_beta_bound(phi):
    """Chapter 3 Lemma ar1, first inequality: beta(k) <= (1/2) sqrt(-log(1 - phi^{2k})).

    Markov property gives beta(k) = E_x d_TV(P^k(x,.), mu); Pinsker + Jensen give
    beta(k) <= sqrt(E KL / 2) with E KL(P^k(x,.) || mu) = -log(1 - phi^{2k}) / 2.
    The looser k-uniform forms (1/2)|phi|^k (1-phi^{2k})^{-1/2} <= |phi|^k / (2 sqrt(1-phi^2))
    and ch2's |phi|^k / sqrt 2 are valid too; the thesis quotes each with its source.
    """
    return lambda k: 0.5 * np.sqrt(-np.log1p(-abs(phi) ** (2 * k)))

def ar1_beta_exact(phi, k):
    """Exact beta(k) of the Gaussian AR(1) by 1-D quadrature (to gauge the bound)."""
    s2 = 1 / (1 - phi ** 2)
    sk2 = (1 - phi ** (2 * k)) * s2
    def tv(x):  # TV between N(phi^k x, sk2) and N(0, s2), via a fine grid
        z = np.linspace(-10 * np.sqrt(s2), 10 * np.sqrt(s2), 4001)
        f = norm.pdf(z, phi ** k * x, np.sqrt(sk2)) - norm.pdf(z, 0, np.sqrt(s2))
        return 0.5 * np.trapezoid(np.abs(f), z)
    return quad(lambda x: tv(x) * norm.pdf(x, 0, np.sqrt(s2)), -8 * np.sqrt(s2), 8 * np.sqrt(s2))[0]

def ar1_block_var(phi, b, v=1.0):
    """v_b = Var(sum_{t=1}^b X_t) = v (b + 2 sum_{h<b} (b-h) phi^h) for stationary variance v."""
    h = np.arange(1, b)
    return v * (b + 2 * np.sum((b - h) * phi ** h))

def ar1_block_sd(phi, b, sigma=1.0):
    """Exact sd of a b-period block sum of a stationary AR(1) with innovation sd sigma."""
    return np.sqrt(ar1_block_var(phi, b, sigma ** 2 / (1 - phi ** 2)))

def ar1_drift_dK(phi, b, mu, v=1.0):
    """Kolmogorov distance between P = N(0, v_b) and Q = N(b mu, v_b): 2 Phi(b mu / (2 sqrt v_b)) - 1."""
    return 2 * norm.cdf(b * mu / (2 * np.sqrt(ar1_block_var(phi, b, v)))) - 1

def simulate_ar1(phi, T, reps, rng, sigma=1.0, burn=200):
    """reps stationary Gaussian AR(1) paths of length T, shape (reps, T)."""
    from scipy.signal import lfilter
    eps = rng.normal(0, sigma, (reps, T + burn))
    return lfilter([1.0], [1.0, -phi], eps, axis=1)[:, burn:]

# ---------------------------------------------------------------- stationary block bootstrap

def stationary_bootstrap_quantiles(x, b, alpha, B, rng, mean_block=None):
    """Politis-Romano stationary bootstrap of the (1-alpha) block-score quantile.

    Each pseudo-series of length N is built from circular blocks of geometric
    length (mean `mean_block`, default b); its score = the (1-alpha) empirical
    quantile of all N-b+1 overlapping block sums.  Returns the B bootstrap
    quantiles; the caller chooses a summary.  Empirical comparison only:
    no coverage theorem is claimed (ground truth, Remark on the bootstrap).
    """
    x = np.asarray(x, float); N = len(x)
    p = 1 / (mean_block or b)
    restart = rng.random((B, N)) < p
    restart[:, 0] = True
    starts = rng.integers(0, N, (B, N))
    t = np.arange(N)
    tau = np.maximum.accumulate(np.where(restart, t, 0), axis=1)   # last restart time
    idx = (np.take_along_axis(starts, tau, 1) + (t - tau)) % N
    xs = x[idx]                                                    # (B, N) pseudo-series
    cs = np.concatenate([np.zeros((B, 1)), np.cumsum(xs, 1)], 1)
    sums = cs[:, b:] - cs[:, :-b]                                  # all overlapping block sums
    return np.quantile(sums, 1 - alpha, axis=1)
