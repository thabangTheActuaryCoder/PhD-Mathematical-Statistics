"""OIS discount-curve bootstrap and forward compounded rate (ch2, sec. prelim-forward/compounded)."""
import numpy as np


def bootstrap_ois(pillars, par_rates):
    """Sequential bootstrap of discount factors P(0, t_i) from OIS par rates.

    pillars   : increasing maturities t_1 < ... < t_n in years.
    par_rates : par fixed rate R_i of the OIS maturing at t_i (decimal).
    The fixed leg of swap i pays R_i * (t_j - t_{j-1}) at every pillar t_j <= t_i;
    the floating (compounded overnight) leg is worth 1 - P(0, t_i).
    Hence P_i = (1 - R_i * sum_{j<i} delta_j P_j) / (1 + R_i * delta_i).
    # ponytail: fixed coupons on the pillar grid; pass a real annual schedule if pillars are not annual past 1y.
    """
    t = np.asarray(pillars, float)
    R = np.asarray(par_rates, float)
    if t.ndim != 1 or t.shape != R.shape or np.any(np.diff(t) <= 0) or t[0] <= 0:
        raise ValueError("pillars must be strictly increasing positive, same length as par_rates")
    delta = np.diff(np.concatenate(([0.0], t)))
    P = np.empty_like(t)
    annuity = 0.0
    for i in range(len(t)):
        P[i] = (1.0 - R[i] * annuity) / (1.0 + R[i] * delta[i])
        annuity += delta[i] * P[i]
    return t, P


def discount(t, pillars, dfs):
    """P(0, t) by log-linear interpolation in t (flat continuous forward between pillars).

    Extrapolation: P(0,0)=1 at the short end; flat forward beyond the last pillar.
    """
    t = np.asarray(t, float)
    x = np.concatenate(([0.0], pillars))
    y = np.concatenate(([0.0], np.log(dfs)))
    logP = np.interp(t, x, y)
    beyond = t > x[-1]
    if np.any(beyond):  # flat forward extrapolation
        fwd = -(y[-1] - y[-2]) / (x[-1] - x[-2])
        logP = np.where(beyond, y[-1] - fwd * (t - x[-1]), logP)
    return np.exp(logP)


def forward_compounded(T, Delta, pillars, dfs):
    """Forward compounded rate F_0 for the window [T, T+Delta]: 1 + Delta F_0 = P(0,T)/P(0,T+Delta)."""
    PT, PTD = discount([T, T + Delta], pillars, dfs)
    return (PT / PTD - 1.0) / Delta
