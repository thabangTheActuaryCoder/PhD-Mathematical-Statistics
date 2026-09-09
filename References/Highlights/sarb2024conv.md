# sarb2024conv

**Record.** South African Reserve Bank, Market Practitioners Group, Derivatives Workstream (2025). *Market conventions for ZARONIA-based non-linear derivatives*. Cover date 6 March 2025 (page headers 'March 6, 2025'); SARB page states Published 2025-03-31, Last Modified 2025-08-06; consultation draft November 2024; Excel model corrected 4 August 2025. 33 pages.

**URL.** https://www.resbank.co.za/content/dam/sarb/publications/financial-markets/committees/mpg/mpg-ralated-documents/2024/Market%20conventions%20for%20ZARONIA-based%20non-linear%20derivatives1.pdf (landing page https://www.resbank.co.za/en/home/publications/publication-detail-pages/Financial-Markets/Committees/MPG/MPG-Related-pages/2024/market-conventions-for-zaronia-based-non-linear-derivatives0)

**Licence / access.** Public SARB document (© South African Reserve Bank). Primary source. Downloaded 2026-09-09 with a browser User-Agent; first page matches the record.

**Status.** primary document. File: `References/PDF/sarb2024conv.pdf`; highlighted copy: `References/PDF/sarb2024conv.highlighted.pdf`. Processed 2026-09-09 by thesis-reference-librarian.

**Librarian note.** This paper covers ZARONIA caps/floors/swaptions. It does NOT state the JIBAR caplet fixing/payment convention; Chapter 2 (around the 'fixes at T and pays at T+Δ' remark) should cite it only for the ZARONIA caplet paying at T(i) = T_i + 2bd. Its §8.3.2 gives the linear decay g and the δ/3 clock shift as the OPTIONAL market quoting convention, attributed to Lyashenko–Mercurio: this is the primary-source anchor for 'the market convention supplies a fixed policy' (GROUND-TRUTH §three-year programme).

## Passages relevant to this thesis

Excerpts are verbatim from the PDF text layer (ligatures and spacing as extracted). 'Locator' is the number as printed in the source.

| Page | Locator (as printed) | Verbatim excerpt | Why it matters (chapter / ground-truth result) | Cite as |
|---|---|---|---|---|
| 5 | §3 Problem statement, p. 5 | The specific recommendations herein offer the standard conventions that will form the basis for the on-the-run interbank market, which constitutes caps, floors, and swaptions that reference ZARONIA, and will in future be quoted on screens and/or via interbank broking agents. | appC/ch7: no screens yet in March 2025; the thesis's 'no evidence of quoted screens' statement. | `\citep[§3, p.~5]{sarb2024conv}` |
| 5 | §3, p. 5 | It is not meant to prescribe, mandate, or limit the ways in which they can transact based on their needs and requirements. | ch7: the conventions are recommendations, not rules. | `\citep[§3, p.~5]{sarb2024conv}` |
| 8 | §6.1 table, p. 8 | Backward-looking without lookback or lockout period. Payment lag to resolve calculation lag. | ch2 Def fallback / ch7: caplet floating rate is the compounded ACFR in arrears with a 2bd payment lag and no lookback/lockout. | `\citep[§6.1, p.~8]{sarb2024conv}` |
| 21 | §7.4 Recommendations, p. 21 | In summary, no fixing adjustments are recommended for the specification of derivative market instruments. Rather, the payment lag feature is recommended to solve for practical settlement issues. | ch2: justifies the thesis's continuous compounded rate over [T, T+Δ] with no lookback (ℓ = f = ω = 0). | `\citep[§7.4, p.~21]{sarb2024conv}` |
| 24 | §7.6, p. 24 | If this payoff is a positive value, then the writer (short position holder) of the option will pay the (long position) holder this amount at the payment date T(i). | ch2 Correction 1: the compounded caplet pays at the end of the accrual period (plus payment lag), so its price is a Q^{T+Δ}-expectation; payoff V_i = N max[α(F(i) − K), 0] δ_i. | `\citep[§7.6, p.~24]{sarb2024conv}` |
| 25 | §7.6 Recommendations, p. 25 | Suggested quoted strikes for each option tenor: {K ± 2%, K ± 1.5%, K ± 1%, K ± 0.75%, K ± 0.5%, K ± 0.25%, K} , where K is the respective at-the-money strike rate for the option tenor under consideration. | ch5 parameter count / ch7 data request: the recommended caplet strike grid (13 strikes) that a sponsor's surface would follow. | `\citep[§7.6, p.~25]{sarb2024conv}` |
| 26 | §8 Market quote conventions, p. 26 | Three quote formats are mandated — premium, Black volatility and Normal (or Bachelier) volatility. | ch2/ch5: normal (Bachelier) volatility is an official quote format, which is the σ^N the thesis works in. | `\citep[§8, p.~26]{sarb2024conv}` |
| 26 | §8, p. 26 | we also include the Normal (or Bachelier) formula. | ch2: SA historically quoted Black; Normal added for international compatibility and possible low-rate regimes. | `\citep[§8, p.~26]{sarb2024conv}` |
| 27 | §8.2, p. 27 | Consequently, the various implied volatilities indicated on the inter-dealer broker screens make the underlying assumption of an underlying USD-denominated CSA. | appC/ch7: screen vols (when they exist) assume a USD zero-threshold CSA with SOFR collateral; discounting is on the ZAR basis curve. | `\citep[§8.2, p.~27]{sarb2024conv}` |
| 28 | §8.3.1, p. 28 | Volatility decay: None (default), Linear (optional). See sub-section 8.3.2. | ch2 Assumption linear decay: decay is optional in the market convention and linear when applied. | `\citep[§8.3.1, p.~28]{sarb2024conv}` |
| 29 | §8.3.2, eq. (15), p. 29 | which linearly reduces the volatility during the fixing period, the equations for caplet and floorlet prices, (11) and (12), introduced in the previous section may be used, unmodified, with an effective change in the time to maturity parameters given by | ch2 Lemma prelim-tc: primary-source statement of g(t) = min{(T_i − t)^+/δ_i, 1} and the effective maturity T_i − δ_i − t + δ_i/3 (eq. (16)), attributed to Lyashenko and Mercurio (2019a, 2019b). | `\citep[§8.3.2, eqs~(15)--(16), p.~29]{sarb2024conv}` |
| 29 | §8.3.2, p. 29 | The same effective change in time to maturity is applicable to the Normal model. | ch2: the δ/3 clock shift is applied identically under the Normal (Bachelier) quote. | `\citep[§8.3.2, p.~29]{sarb2024conv}` |
| 29 | §8.3.2, p. 29 | [Lyashenko and Mercurio, 2019b] provide empirical evidence for this phenomenon, and make the case that volatility decay is necessary in the current accrual period. | ch2: the market document's attribution of volatility decay to Lyashenko–Mercurio; use when lyashenko2019 itself is not on disk. | `\citep[§8.3.2, p.~29]{sarb2024conv}` |

## Highlighting log

13 of 13 passages highlighted with PyMuPDF `search_for` + `add_highlight_annot`.
