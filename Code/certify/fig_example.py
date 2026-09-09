"""Series for ch3 Figure fig:example (deficit terms vs block length, phi in {0.5, 0.8}).
Run:  cd thesis/code && uv run --with numpy --with scipy python certify/fig_example.py [out.csv]
Writes one CSV row per (phi, b): coupling (n+1)beta(b), conformal 1-k/(n+1), drift dK at mu=0.05,
their sum, and the Monte Carlo breach frequency P(S_0 > q_hat) over REPS replications (seed SEED).
Plots to out.png if matplotlib is importable; otherwise CSV only.
"""
import sys, os, csv
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np
import certify as C

N, ALPHA, MU, REPS, SEED = 500, 0.1, 0.05, 10_000, 20260909
PHIS, BS = (0.5, 0.8), range(2, 51)

def series(phi, b, rng):
    beta_fn = C.ar1_beta_bound(phi)
    st = C.blocks(N, b); n = len(st); k = C.conformal_k(n, ALPHA); d0 = C.deployment_start(st, b)
    X = C.simulate_ar1(phi, d0 + b, REPS, rng, sigma=np.sqrt(1 - phi ** 2))
    qhat = C.conformal_threshold(C.block_scores(X, st, b), ALPHA)
    breach = np.mean(X[:, d0:d0 + b].sum(1) + b * MU > qhat)
    coup, conf, drift = (n + 1) * beta_fn(b), 1 - k / (n + 1), C.ar1_drift_dK(phi, b, MU)
    return dict(phi=phi, b=b, n=n, k=k, coupling=float(coup), conformal=conf, drift=float(drift), bound=float(coup + conf + drift), breach_mc=float(breach))

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "fig_example.csv")
    rng = np.random.default_rng(SEED)
    rows = [series(phi, b, rng) for phi in PHIS for b in BS]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f"wrote {len(rows)} rows to {out}")
    for r in rows:
        if r["b"] in (5, 10, 20): print(r)
    try:
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
        for ax, phi in zip(axes, PHIS):
            R = [r for r in rows if r["phi"] == phi]; b = [r["b"] for r in R]
            for key in ("coupling", "conformal", "drift", "bound", "breach_mc"): ax.plot(b, [r[key] for r in R], label=key)
            ax.axhline(ALPHA, ls=":", c="k"); ax.set_ylim(0, 1); ax.set_title(f"phi = {phi}"); ax.set_xlabel("block length b")
        axes[0].legend(); fig.savefig(out.rsplit(".", 1)[0] + ".png", dpi=150, bbox_inches="tight")
    except ImportError:
        pass  # ponytail: CSV is the deliverable; the figure planner plots it
