"""Hagan normal SABR, Bachelier pricer, time-changed caplet (Lemma prelim-tc) and the
non-decaying vol-of-vol variant via HLW effective parameters (Prop. prelim-novol / prelim-nueff).
"""
import math
import numpy as np
from .clock import g_linear, tau, tau_star, _simpson

_SQRT2PI = math.sqrt(2.0 * math.pi)


def _Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bachelier_call(f, K, sigma, t):
    """Undiscounted Bachelier call E[(F_t - K)^+] with F_t ~ N(f, sigma^2 t)."""
    v = sigma * math.sqrt(t)
    if v <= 0.0:
        return max(f - K, 0.0)
    d = (f - K) / v
    return (f - K) * _Phi(d) + v * math.exp(-0.5 * d * d) / _SQRT2PI


def hagan_normal_vol(f, K, t, alpha, beta, rho, nu):
    """Hagan et al. (2002) normal implied volatility, eq. (prelim-hagan-N); beta=0 gives (prelim-hagan-N0)."""
    if beta == 0.0:
        lead = alpha
        bracket = (2.0 - 3.0 * rho * rho) * nu * nu / 24.0
        zeta = nu * (f - K) / alpha
    else:
        fk = f * K
        lead = alpha * (1.0 - beta) * (f - K) / (f ** (1 - beta) - K ** (1 - beta)) if f != K else alpha * f ** beta
        bracket = (-beta * (2.0 - beta) * alpha ** 2 / (24.0 * fk ** (1.0 - beta))
                   + rho * beta * nu * alpha / (4.0 * fk ** ((1.0 - beta) / 2.0))
                   + (2.0 - 3.0 * rho * rho) * nu * nu / 24.0)
        zeta = nu / alpha * (f ** (1 - beta) - K ** (1 - beta)) / (1 - beta)
    if abs(zeta) < 1e-12:
        zx = 1.0
    else:
        x = math.log((math.sqrt(1.0 - 2.0 * rho * zeta + zeta * zeta) + zeta - rho) / (1.0 - rho))
        zx = zeta / x
    return lead * zx * (1.0 + bracket * t)


def caplet_time_changed(F0, K, T, Delta, alpha, beta, rho, nu, P=1.0, g=g_linear):
    """Lemma prelim-tc: caplet per unit accrual = P(0,T+Delta) * C^SABR(F0, K, tau(T+Delta)).

    Returns (price, normal vol at the clock, tau*). Both legs are under Q^{T+Delta}: no convexity term.
    """
    ts = tau_star(T, Delta, g=g)
    sig = hagan_normal_vol(F0, K, ts, alpha, beta, rho, nu)
    return P * bachelier_call(F0, K, sig, ts), sig, ts


def hlw_effective(rho, nu, T, Delta, g=g_linear, n=4001):
    """Effective (rho_eff, nu_eff) for time-dependent vol-of-vol nu~(u) = nu / g(tau^{-1}(u)), eq. (prelim-eff).

    APPROXIMATION: Hagan-Lesniewski-Woodward leading-order matching of the third cumulant and Var(V).
    Integrals are taken in calendar time via du = g^2 dt, which removes the w^{-2/3} singularity:
      rho_eff nu_eff = 2 rho nu / tau*^2 * int_0^{T+Delta} g(t) (tau* - tau(t)) dt
      nu_eff^2       = 3 nu^2  / tau*^3 * int_0^{T+Delta} (tau* - tau(t))^2 dt
    """
    ts = tau_star(T, Delta, g=g)
    t = np.linspace(0.0, T + Delta, n)
    rem = ts - np.array([tau(ti, T, Delta, g=g) for ti in t])
    I1 = _simpson(g(t, T, Delta) * rem, t)
    I2 = _simpson(rem ** 2, t)
    nu_eff = math.sqrt(3.0 * nu * nu / ts ** 3 * I2)
    rho_eff = 2.0 * rho * nu / ts ** 2 * I1 / nu_eff
    return rho_eff, nu_eff


def caplet_nondecaying_volvol(F0, K, T, Delta, alpha, beta, rho, nu, P=1.0, accounting="hlw"):
    """Prop. prelim-novol variant (d alpha = nu alpha dZ, no decay on vol-of-vol). APPROXIMATION.

    accounting="hlw"   : (rho_eff, nu_eff) of Prop. prelim-nueff (effective-parameter theory);
    accounting="total" : ground-truth accounting nu_eff^2 = nu^2 (T+Delta)/tau*, rho unchanged.
    Returns (price, normal vol at the clock, rho_eff, nu_eff).
    """
    ts = tau_star(T, Delta)
    if accounting == "hlw":
        rho_eff, nu_eff = hlw_effective(rho, nu, T, Delta)
    elif accounting == "total":
        rho_eff, nu_eff = rho, nu * math.sqrt((T + Delta) / ts)
    else:
        raise ValueError("accounting must be 'hlw' or 'total'")
    sig = hagan_normal_vol(F0, K, ts, alpha, beta, rho_eff, nu_eff)
    return P * bachelier_call(F0, K, sig, ts), sig, rho_eff, nu_eff
