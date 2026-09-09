# schmitt2026

**Record.** Schmitt, M. (2026). Taming tail risk in financial markets: conformal calibration for nonstationary portfolio VaR. arXiv:2602.03903v3 [q-fin.RM], 3 August 2026, 7 pages. University of Oxford.

**URL.** https://arxiv.org/pdf/2602.03903 (abs https://arxiv.org/abs/2602.03903)

**Licence / access.** arXiv preprint; licence as stated on the arXiv abstract page (not verified). Downloaded 2026-09-09; first page matches the record.

**Status.** downloaded. File: `References/PDF/schmitt2026.pdf`; highlighted copy: `References/PDF/schmitt2026.highlighted.pdf`. Processed 2026-09-09 by thesis-reference-librarian.

**Librarian note.** Finance application of weighted (Barber et al. 2023) conformal calibration to one-sided VaR with Kupiec and DQ backtests. Its Theorem 1 carries a factor 2 on d_TV that the author shows is not removable for the swap argument; the thesis's constant 1 on d_K (after coupling) is the contrast for ch4.

## Passages relevant to this thesis

Excerpts are verbatim from the PDF text layer (ligatures and spacing as extracted). 'Locator' is the number as printed in the source.

| Page | Locator (as printed) | Verbatim excerpt | Why it matters (chapter / ground-truth result) | Cite as |
|---|---|---|---|---|
| 1 | Abstract, p. 1 | Coverage bounds are derived for arbitrary data-driven weights under smooth regime drift, without assuming weighted exchangeability. | ch3 chapter notes / ch6 related work: the nearest finance application of conformal drift bounds. | `\citep[p.~1]{schmitt2026}` |
| 1 | §1, p. 1 | under the Basel traffic-light framework, a bank that records too many VaR exceptions in its one-year backtest is moved into a higher penalty zone, and the multiplier applied to its market-risk capital charge rises accordingly. | ch6 traffic-light comparison: a one-sentence statement of the Basel traffic-light mechanism (secondary; cite BCBS as primary). | `\citep[§1, p.~1]{schmitt2026}` |
| 3 | Assumption 1, p. 3 | dTV(Pi(· \| z), Pt(· \| z′)) ≤Lz∥z −z′∥+ Lt(t −i). | ch3 Prop 7 / ch4: a TV-Lipschitz drift assumption; the thesis uses d_K ≤ d_TV and bounds d_K by √(2 L W_1) instead. | `\citep[Assumption~1, p.~3]{schmitt2026}` |
| 3 | Theorem 1, p. 3 | P(yt ≤Ut \| Zt) ≥1 −α −εt, εt = 2 Σ i∈It w̄i(t) dTV(Pi(· \| zi), Pt(· \| zt)), | ch4 Thm 8 discussion: the swap argument of Barber et al. yields a coefficient 2 on d_TV; the thesis's coupling-then-d_K route attains coefficient 1 and proves it sharp. | `\citep[Thm.~1, p.~3]{schmitt2026}` |
| 3 | Theorem 1, proof, p. 3 | (The factor 2 is not removable in general: for Pi uniform on {1, 2} and Pt uniform on {2, 3}, dTV(Pi, Pt) = 1/2 while the swapped products are at distance 3/4.) | ch4 Thm 8: explicit example that the factor 2 in the swapped-product bound is tight for that argument, which motivates the thesis's different route to constant 1. | `\citep[p.~3]{schmitt2026}` |
| 4 | Table 1, p. 4 | †: Kupiec unconditional-coverage rejection at 5%; ‡: Engle–Manganelli DQ rejection at 5%. | ch6: precedent for reporting Kupiec POF alongside conformal coverage on financial backtests. | `\citep[Table~1, p.~4]{schmitt2026}` |
| 6 | §7 Limitations, p. 6 | the coverage gap does not vanish for fixed (λ,h), and long-run marginal coverage is better served by feedback methods, three of which we benchmark. | ch3/ch6 discussion: weighted calibration has a non-vanishing gap; the thesis's certificate is likewise conditional on an assumed mixing class and says so. | `\citep[§7, p.~6]{schmitt2026}` |

## Highlighting log

7 of 7 passages highlighted with PyMuPDF `search_for` + `add_highlight_annot`.
