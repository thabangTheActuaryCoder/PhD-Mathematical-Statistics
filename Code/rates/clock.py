"""Lyashenko-Mercurio decay profile g and clock tau(t) = int_0^t g^2 (ch2, sec. prelim-decay).

Assumption (linear decay): g(t) = (T+Delta-t)/Delta on (T, T+Delta]. This is an assumption,
exact only for flat forward-rate volatility; the code never hard-codes tau* = T + Delta/3,
it integrates g^2 numerically so the test can verify that value.
"""
import numpy as np


def g_linear(t, T, Delta):
    """g(t) = 1 for t <= T, (T+Delta-t)/Delta on (T, T+Delta], 0 after."""
    t = np.asarray(t, float)
    return np.clip((T + Delta - t) / Delta, 0.0, 1.0)


def _simpson(y, x):
    """Composite Simpson on an odd-length uniform grid (exact for cubics, hence for g^2)."""
    h = x[1] - x[0]
    return h / 3.0 * (y[0] + y[-1] + 4.0 * y[1:-1:2].sum() + 2.0 * y[2:-1:2].sum())


def tau(t, T, Delta, g=g_linear, n=2001):
    """Clock tau(t) = int_0^t g(u)^2 du, integrating numerically on [T, t] (g = 1 before T)."""
    t = float(t)
    if t <= T:
        return t
    u = np.linspace(T, min(t, T + Delta), n)
    return T + _simpson(g(u, T, Delta) ** 2, u)


def tau_star(T, Delta, **kw):
    """tau* = tau(T+Delta); equals T + Delta/3 under linear decay."""
    return tau(T + Delta, T, Delta, **kw)
