"""Tests for rates/: run with `python3 -m pytest tests/` or `python3 tests/test_rates.py`."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from rates import (bootstrap_ois, discount, forward_compounded, tau, tau_star,
                   bachelier_call, hagan_normal_vol, caplet_time_changed,
                   caplet_nondecaying_volvol, hlw_effective)

# Chapter 2 worked example (subsec:prelim-worked)
T, DELTA, F0, K, ALPHA, BETA, RHO, NU = 1.0, 0.25, 0.07, 0.07, 0.006, 0.0, -0.2, 0.4
BP = 1e4


def test_bootstrap_flat_curve_and_reprice():
    pillars = np.arange(1, 11, dtype=float)
    r = 0.05
    t, P = bootstrap_ois(pillars, np.full(10, r))
    assert np.allclose(P, (1 + r) ** -pillars, rtol=0, atol=1e-14)   # annual pay, flat: P_n = (1+r)^-n
    # reprice: par rate = (1 - P_n) / annuity_n
    ann = np.cumsum(np.diff(np.concatenate(([0.0], t))) * P)
    assert np.allclose((1 - P) / ann, r, atol=1e-14)
    # log-linear interpolation: flat curve stays flat between pillars and beyond
    assert abs(discount(2.5, t, P) - (1 + r) ** -2.5) < 1e-14
    assert abs(discount(12.0, t, P) - (1 + r) ** -12.0) < 1e-13
    # forward compounded rate for [1, 1.25] on the flat curve
    F = forward_compounded(1.0, 0.25, t, P)
    assert abs(F - ((1 + r) ** 0.25 - 1) / 0.25) < 1e-13


def test_clock_linear_decay_is_T_plus_Delta_over_3():
    assert abs(tau_star(T, DELTA) - (T + DELTA / 3)) < 1e-12
    assert abs(tau_star(2.0, 0.5) - (2.0 + 0.5 / 3)) < 1e-12
    assert tau(0.7, T, DELTA) == 0.7                                       # g = 1 before T
    assert abs(tau(T + DELTA / 2, T, DELTA) - (T + DELTA / 3 * (1 - 0.5 ** 3))) < 1e-12  # tau = T + Delta/3 (1-g^3)


def test_bachelier_closed_form():
    # ATM: E[(F-K)^+] = sigma sqrt(t) / sqrt(2 pi)
    assert abs(bachelier_call(F0, F0, ALPHA, 1.0833) - ALPHA * math.sqrt(1.0833) / math.sqrt(2 * math.pi)) < 1e-16
    # put-call parity via C(K) - C_put = f - K with put = C(K) - (f - K); check deep ITM -> intrinsic, deep OTM -> 0
    assert abs(bachelier_call(0.07, 0.01, 0.006, 1.0) - 0.06) < 1e-12
    assert bachelier_call(0.07, 0.20, 0.006, 1.0) < 1e-12
    assert bachelier_call(F0, K, 0.0, 1.0) == 0.0


def test_hagan_normal_reproduces_ch2_hand_arithmetic():
    ts = tau_star(T, DELTA)
    atm = hagan_normal_vol(F0, F0, ts, ALPHA, BETA, RHO, NU)
    lo = hagan_normal_vol(F0, F0 - 0.005, ts, ALPHA, BETA, RHO, NU)
    hi = hagan_normal_vol(F0, F0 + 0.005, ts, ALPHA, BETA, RHO, NU)
    assert abs(atm * BP - 60.815) < 0.005          # ch2: 60.81 bp (0.0060815)
    assert abs(lo * BP - 63.79) < 0.01             # ch2: 63.79 bp
    assert abs(hi * BP - 59.90) < 0.01             # ch2: 59.90 bp
    assert abs(atm * math.sqrt(ts / (T + DELTA)) * BP - 56.62) < 0.01   # quoted at T+Delta
    # nu -> 0 returns Bachelier vol alpha exactly
    assert hagan_normal_vol(F0, F0 - 0.005, ts, ALPHA, 0.0, RHO, 0.0) == ALPHA


def test_time_changed_caplet_worked_example():
    price, sig, ts = caplet_time_changed(F0, K, T, DELTA, ALPHA, BETA, RHO, NU)
    assert abs(price - 0.0025254) < 1e-6           # ch2: 0.39894 * 0.0060815 * sqrt(1.0833)
    no_decay = bachelier_call(F0, K, hagan_normal_vol(F0, K, T + DELTA, ALPHA, BETA, RHO, NU), T + DELTA)
    assert abs(no_decay - 0.0027178) < 1e-6
    assert abs(price / no_decay - 1 + 0.071) < 0.002   # 7.1% reduction from the run-off
    print(f"\nTime-changed caplet (T={T}, Delta={DELTA}, F0=K={F0}, alpha0={ALPHA}, nu={NU}, rho={RHO}, beta={BETA}):")
    print(f"  tau*      = {ts:.6f}  (T + Delta/3 = {T + DELTA / 3:.6f})")
    print(f"  sigma_N at clock = {sig * BP:.4f} bp; quoted at T+Delta = {sig * math.sqrt(ts / (T + DELTA)) * BP:.4f} bp")
    print(f"  price (P=1)      = {price:.7f}   no-decay SABR to T+Delta = {no_decay:.7f}   ratio = {price / no_decay:.4f}")


def test_nondecaying_volvol_curvature_difference():
    ts = tau_star(T, DELTA)
    strikes = [F0 - 0.005, F0, F0 + 0.005]
    base = [hagan_normal_vol(F0, k, ts, ALPHA, BETA, RHO, NU) for k in strikes]
    out = {}
    for acc in ("total", "hlw"):
        vols = [caplet_nondecaying_volvol(F0, k, T, DELTA, ALPHA, BETA, RHO, NU, accounting=acc)[1] for k in strikes]
        d = [(v - b) * BP for v, b in zip(vols, base)]
        curv = 0.5 * (d[0] + d[2]) - d[1]          # wing lift net of ATM lift, bp at +/-50 bp
        out[acc] = (d, curv, caplet_nondecaying_volvol(F0, K, T, DELTA, ALPHA, BETA, RHO, NU, accounting=acc)[3])
    rho_eff, nu_eff = hlw_effective(RHO, NU, T, DELTA)
    # ground-truth accounting: nu_eff = 0.42967, lifts +0.42/+0.13/+0.15 bp, curvature 0.16 bp (ch2)
    assert abs(out["total"][2] - 0.42967) < 1e-4
    assert abs(out["total"][1] - 0.16) < 0.02
    # effective-parameter accounting: nu_eff^2 = 1.00013 nu^2 (ch2 gap box; analytic 1 + (2/567) Delta^3 / (tau*^3/3))
    assert abs(nu_eff ** 2 / NU ** 2 - (1 + 2 / 567 * DELTA ** 3 / (ts ** 3 / 3))) < 1e-9
    # rho_eff nu_eff / (rho nu) = (T tau* - T^2/2 + Delta^2/15) / (tau*^2/2), a 0.12% skew shift
    assert abs(rho_eff * nu_eff / (RHO * NU) - (T * ts - T * T / 2 + DELTA ** 2 / 15) / (ts ** 2 / 2)) < 1e-9
    # vol differences at +/-50 bp are ~0.002 bp (skew shift), curvature difference below 1e-4 bp
    assert max(abs(x) for x in out["hlw"][0]) < 0.005
    assert abs(out["hlw"][1]) < 1e-4
    print("\nNon-decaying vol-of-vol variant vs Lemma (time-changed SABR), vol differences in bp at [-50, ATM, +50] bp:")
    for acc, (d, curv, ne) in out.items():
        print(f"  {acc:5s}: nu_eff = {ne:.5f}  diffs = [{d[0]:+.4f}, {d[1]:+.4f}, {d[2]:+.4f}]  curvature (wing net of ATM) = {curv:+.5f} bp")
    print(f"  HLW rho_eff = {rho_eff:.6f} (rho = {RHO})")


if __name__ == "__main__":
    fails = 0
    for name, fn in [(n, f) for n, f in globals().items() if n.startswith("test_") and callable(f)]:
        try:
            fn(); print(f"PASS {name}")
        except AssertionError as e:
            fails += 1; print(f"FAIL {name}: {e!r}")
    sys.exit(1 if fails else 0)
