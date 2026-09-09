# gibbs2021 — Gibbs & Candès (2021), adaptive conformal inference

**Record.** Gibbs, I., Candès, E. J. (2021). Adaptive conformal inference under distribution shift. *Advances in Neural Information Processing Systems* 34 (NeurIPS 2021). Bib entry consistent with the arXiv record (arXiv:2106.00170, v3 28 Oct 2021, 25 pp, 9 figures).

**File.** `References/PDF/gibbs2021.pdf` = arXiv:2106.00170v3, licence arXiv non-exclusive. Page numbers below are the arXiv v3 PDF pages (printed folios). Highlighted copy: `gibbs2021.highlighted.pdf`. The NeurIPS proceedings PDF is also open but was not fetched.

**What the thesis needs from it.** ch3 chapter notes / ch1 positioning: the online-adaptation alternative to a fixed-policy certificate. ACI guarantees a long-run average error frequency for any sequence, not a per-block finite-sample coverage bound; sharper statements need a hidden-Markov model with spectral gap.

| Page | As printed | Verbatim excerpt | Why it matters | Locator |
|---|---|---|---|---|
| 3 | eq. (2) | "Then, fixing a step size parameter γ > 0 we consider the simple online update α_{t+1} := α_t + γ(α − err_t). We refer to this algorithm as adaptive conformal inference." | Definition of ACI. | `\citep[eq.~(2)]{gibbs2021}` |
| 6 | Lemma 4.1 | "With probability one we have that ∀t ∈ ℕ, α_t ∈ [−γ, 1 + γ]." | Boundedness of the adapted level. | `\citep[Lemma~4.1]{gibbs2021}` |
| 6 | Proposition 4.1 | "With probability one we have that for all T ∈ ℕ, \| T^{-1} Σ_{t=1}^T err_t − α \| ≤ (max{α_1, 1 − α_1} + γ)/(Tγ). In particular, lim_{T→∞} T^{-1} Σ err_t = α a.s." | Distribution-free but only a long-run frequency; contrast with Thm 6's finite-sample block guarantee. | `\citep[Prop.~4.1]{gibbs2021}` |
| 6 | text | "So, we view Proposition 4.1 as both an agnostic guarantee that shows that our method gives the correct long-term empirical coverage frequency irrespective of the true data generating process, and as an approximately tight bound on the worst-case behaviour immediately after initialization." | The authors' own characterisation of what is and is not guaranteed. | `\citep[p.~6]{gibbs2021}` |
| 7 | Theorem 4.1 | "Assume that {A_t}_{t∈ℕ} has non-zero absolute spectral gap 1 − η > 0. … Then, P(\|T^{-1} Σ err_t − α\| ≥ ε) ≤ 2 exp(−Tε²/8) + 2 exp(−T(1−η)ε²/(8(1+η)σ_B² + 20Bε))." | Concentration needs a hidden Markov environment with spectral gap and stationarity of (α_t, A_t). | `\citep[Thm.~4.1]{gibbs2021}` |
| 8 | Theorem 4.2 | "Assume that there exists a constant L > 0 such that for all a ∈ A and all α_1, α_2 ∈ ℝ, \|M(α_2\|a) − M(α_1\|a)\| ≤ L\|α_2 − α_1\|. … Then, E[(M(α_t\|A_t) − α)²] ≤ L(1+γ)/γ · E[\|α*_{A_{t+1}} − α*_{A_t}\|] + Lγ/2." | Marginal coverage at a single time is controlled only on average and only under a Lipschitz miscoverage map. | `\citep[Thm.~4.2]{gibbs2021}` |
