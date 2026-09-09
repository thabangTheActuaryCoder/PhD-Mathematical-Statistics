# stocker2025

**Record.** Stocker, M., Małgorzewicz, W., Fontana, M., Ben Taieb, S. (2025). A gentle introduction to conformal time series forecasting. arXiv:2511.13608, 31 pages. KIT; Royal Holloway; MBZUAI; University of Mons.

**URL.** https://arxiv.org/pdf/2511.13608 (abs https://arxiv.org/abs/2511.13608)

**Licence / access.** arXiv preprint; licence as stated on the arXiv abstract page (not verified). Downloaded 2026-09-09; first page matches the record.

**Status.** downloaded. File: `References/PDF/stocker2025.pdf`; highlighted copy: `References/PDF/stocker2025.highlighted.pdf`. Processed 2026-09-09 by thesis-reference-librarian.

**Librarian note.** Survey. Appendix A restates Oliveira et al. (2024) (cite the primary). Its 'SCP-block' is the split block-permutation CP of Chernozhukov et al., NOT blocked split conformal; it under-covers in their simulations. Chapters 3 and 6 must distinguish the thesis's blocked certificate from it.

## Passages relevant to this thesis

Excerpts are verbatim from the PDF text layer (ligatures and spacing as extracted). 'Locator' is the number as printed in the source.

| Page | Locator (as printed) | Verbatim excerpt | Why it matters (chapter / ground-truth result) | Cite as |
|---|---|---|---|---|
| 7 | §2, p. 7 | The crucial takeaway is that for stationary, weakly dependent processes, standard SCP is approximately valid, and its deviations from validity are indeed very mild. The true problem is non-stationarity (distribution shift), against which these theoretical results offer limited protection. | ch3 introduction: the survey's summary of why drift, not dependence, is the binding problem; the thesis's d_K term addresses exactly the drift. | `\citep[p.~7]{stocker2025}` |
| 7 | §3, p. 7 (taxonomy) | Blocking: Redefine the fundamental unit of randomization. Instead of assuming individual points are exchangeable, assume that entire blocks of data can be permuted. | ch3 chapter notes: the four-family taxonomy (reweighting, refreshing, adapting coverage, blocking); the thesis's method is blocking in the score construction, not permutation of blocks. | `\citep[§3, p.~7]{stocker2025}` |
| 13 | §3.4, p. 13 | This split-BCP approach loses the exact finite-sample validity of the transductive method. | ch3: split block CP has no finite-sample guarantee; contrast with the thesis's finite-sample certificate. | `\citep[§3.4, p.~13]{stocker2025}` |
| 15 | §5 Conclusion, p. 15 | (1) SCP-block failed to provide valid coverage even in the simple stationary settings, and (2) standard SCP and some adaptive variants (like WCP-window) fail under an abrupt distribution shift. | ch3/ch6: a negative empirical finding about a DIFFERENT blocking scheme; the thesis must say so or a reader will import it. | `\citep[p.~15]{stocker2025}` |
| 23 | Definition A.4.1, p. 23 | The process is β-mixing if β(a) →0 as a →∞. This "forgetting" property allows us to use a blocking technique. | ch2: secondary restatement of the β-mixing definition (primary: Doukhan 1994; Oliveira 2024 §3.3). | `\citep[Def.~A.4.1, p.~23]{stocker2025}` |
| 23 | Proposition A.4.1, p. 23 | If h : Rmb →R is a Borel-measurable function with \|h\| ≤M, then \|E[h(Bodd)] −E[h(B′ odd)]\| ≤2M(m −1)β(a), | ch2: same constant 2M(m−1)β(a) as Oliveira Prop. 10; cite Oliveira as primary. | `\citep[Prop.~A.4.1, p.~23]{stocker2025}` |
| 26 | Theorem A.4.1, p. 26 | Ptr[ Yi ∈C1−α(Xi) ] ≥1 −α −η, with η = δcal + εtrain + εcal, | ch3 chapter notes: restatement of Oliveira Thm 4 (secondary). | `\citep[Thm.~A.4.1, p.~26]{stocker2025}` |

## Highlighting log

7 of 7 passages highlighted with PyMuPDF `search_for` + `add_highlight_annot`.
