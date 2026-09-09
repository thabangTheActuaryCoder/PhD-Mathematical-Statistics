# ramos2026

**Record.** Ramos, T. R., Graziadei, H., Cabezas, L. M. C. (2026). Conformal prediction via transported beta laws. arXiv:2605.19024v1 (18 May 2026), 33 pages. Affiliations: Federal University of São Carlos; University of São Paulo; Inria and Université Grenoble Alpes.

**URL.** https://arxiv.org/pdf/2605.19024 (abs https://arxiv.org/abs/2605.19024)

**Licence / access.** arXiv preprint; licence as stated on the arXiv abstract page (not verified). Downloaded 2026-09-09; first page matches the record.

**Status.** downloaded. File: `References/PDF/ramos2026.pdf`; highlighted copy: `References/PDF/ramos2026.highlighted.pdf`. Processed 2026-09-09 by thesis-reference-librarian.

**Librarian note.** Prints the Beta law of calibration-conditional coverage and the decoupled-test transport h = F_T̃ ∘ F_T^{−1}, whose sup-deviation is d_K(P,Q): the thesis's drift penalty (Thm 6(iii)) is in this paper in the decoupled case. The attained-constant-1 sharpness construction of Thm 8 is NOT here. Their dependent-calibration control is asymptotic (Berry–Esseen via Lahiri–Sun 2009), not finite-sample.

## Passages relevant to this thesis

Excerpts are verbatim from the PDF text layer (ligatures and spacing as extracted). 'Locator' is the number as printed in the source.

| Page | Locator (as printed) | Verbatim excerpt | Why it matters (chapter / ground-truth result) | Cite as |
|---|---|---|---|---|
| 4 | Theorem 1, p. 4 | Theorem 1 (Split Conformal Marginal Coverage) Assume that S1, . . . , Sn, Sn+1 are exchangeable and that there are no ties almost surely. Let kγ = ⌈(n + 1)γ⌉and ˆqn,γ = S(kγ), with the convention that S(k) = +∞whenever k > n. Then γ ≤P (Sn+1 ≤ˆqn,γ) < γ + 1/(n + 1). | ch2 Thm prelim-coverage: a 2026 statement of the two-sided marginal bound with the +∞ convention for k > n. | `\citep[Thm.~1]{ramos2026}` |
| 5 | Proposition 2, p. 5 | Then Cn,k = FS(S(k)) ∼Beta(k, n + 1 −k). | ch2 Thm prelim-beta / ch3 Thm 6(ii): the Beta(k, n+1−k) law of calibration-conditional coverage (primary: Vovk 2012); this is the recent restatement the examiners will know. | `\citep[Prop.~2, p.~5]{ramos2026}` |
| 5 | p. 5, after Proposition 2 | The marginal split conformal guarantee controls only the mean of Cn,k; the lower tail of the beta law controls how often an unfavorable calibration sample occurs. | ch3 §conditional certificate: motivation for the Beta-quantile (calibration-conditional) statement over the marginal one. | `\citep[p.~5]{ramos2026}` |
| 10 | Theorem 11, p. 10 | The theorem says that once the realized coverage law is close to the beta benchmark in Wasserstein distance, the usual conformal coverage level degrades by at most the same amount, up to the standard discretization term. | ch3/ch4: \|Cov(k) − k/(n+1)\| ≤ W_1(ν_{n,k}, β_{n,k}); a W_1-on-[0,1] penalty, distinct from the thesis's d_K penalty on the score line. | `\citep[Thm.~11, p.~10]{ramos2026}` |
| 11 | Proposition 13, p. 11 | Assume that eT is independent of Cn, and let F eT be its distribution function. Then Dn,k = F eT (T(k)), νn,k = L(F eT (T(k))). | ch3 Thm 6(iii): with the test score decoupled from calibration, realised coverage is F_Q(q̂); with h = F_Q ∘ F_P^{−1}, D = h(U_(k)) and sup_u \|h(u) − u\| = d_K(P,Q). The Kolmogorov drift penalty is therefore in print for the decoupled case; the thesis's contribution is the coupling that produces the decoupling under β-mixing plus the sharp constant. | `\citep[Prop.~13, p.~11]{ramos2026}` |
| 11 | §3.2, p. 11 | It is also a useful reduction for temporally dependent data when the test point is sufficiently separated from the calibration block and the dependence decays with the lag. | ch3 Assumption mix: independent support for the gap-separated deployment block (GROUND-TRUTH correction 4). | `\citep[§3.2, p.~11]{ramos2026}` |
| 12 | Proposition 15, p. 12 | This assumption says that the calibration order statistic has a Berry–Esseen law with asymptotic standard deviation τγ. The i.i.d. beta reference has the same form with standard deviation √(γ(1 −γ)). | ch3 chapter notes: their dependent-calibration control is asymptotic (Berry–Esseen, Lahiri–Sun conditions); the thesis's Beta statement after coupling is finite-sample. Quote to mark the difference. | `\citep[Prop.~15, p.~12]{ramos2026}` |
| 16 | §4.3, p. 16 | Different normalizations of the β-mixing coefficient appear in the literature; only its role as a decoupling error is used below. | ch2 mixing definitions: warn readers that β-mixing normalisations differ across papers (factor 2 issues). | `\citep[§4.3, p.~16]{ramos2026}` |
| 17 | §4.3, p. 17 | Coupling lemmas for separated blocks, such as Yu (1994, Corollary 2.7), allow one to replace separated dependent blocks by independent copies at a cost controlled by the corresponding β-mixing coefficients. We do not need the explicit block construction in what follows. | ch3: they name Yu (1994) blocking as one decoupling route but do not carry it out; the thesis does, with the (n+1)β(b) count. | `\citep[§4.3, p.~17]{ramos2026}` |
| 17 | Theorem 16, p. 17 | Theorem 16 (Berry–Esseen Bound for α-Mixing Sample Quantiles) | ch3/ch4 chapter notes: the external asymptotic input (Lahiri and Sun 2009) they rely on for mixing calibration; contrast with the finite-sample route. | `\citep[Thm.~16, p.~17]{ramos2026}` |

## Highlighting log

10 of 10 passages highlighted with PyMuPDF `search_for` + `add_highlight_annot`.
