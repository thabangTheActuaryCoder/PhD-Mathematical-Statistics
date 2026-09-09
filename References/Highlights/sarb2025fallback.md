# sarb2025fallback

**Record.** South African Reserve Bank, Market Practitioners Group (2025). *Jibar transition and fallback credit adjustment spreads for the South African interest rate market* — prepared by the MPG's Transition Planning and Coordination Workstream (TPCW); MPG final recommendation, 19 March 2025 (file name 'Jibar fallback methodology - MPG final recommendation 2025.03.19'). PDF metadata title: 'JIBAR Fallback Methodology Recommendation'. 15 pages.

**URL.** https://www.resbank.co.za/content/dam/sarb/publications/financial-markets/committees/mpg/mpg-ralated-documents/2025/Jibar%20fallback%20methodology%20-%20MPG%20final%20recommendation%202025.03.19%20(1).pdf

**Licence / access.** Public SARB document (© South African Reserve Bank). Primary source. Downloaded 2026-09-09 with a browser User-Agent; first page matches the record.

**Status.** primary document. File: `References/PDF/sarb2025fallback.pdf`; highlighted copy: `References/PDF/sarb2025fallback.highlighted.pdf`. Processed 2026-09-09 by thesis-reference-librarian.

**Librarian note.** BIBLIOGRAPHIC: the printed title ends '...for the South African interest rate market' (References.bib omits 'interest rate'); the paper is 'prepared by the Transition Planning and Coordination Workstream', not the Derivatives Workstream. The document carries no date on its cover; the 19 March 2025 date comes from the SARB file name. It gives the METHODOLOGY (five-year median) and projections (3M ≈ 18 bp for Dec 2025); the fixed value 16.19 bp is in the BISL note of 22 Dec 2025, not here.

## Passages relevant to this thesis

Excerpts are verbatim from the PDF text layer (ligatures and spacing as extracted). 'Locator' is the number as printed in the source.

| Page | Locator (as printed) | Verbatim excerpt | Why it matters (chapter / ground-truth result) | Cite as |
|---|---|---|---|---|
| 3 | §1 Executive summary, p. 3 | The spread should be based on a historical median of the differences between Jibar and compounded ZARONIA over a five-year lookback period. | ch1/ch2 Def fallback: the recommended CAS methodology. | `\citep[§1, p.~3]{sarb2025fallback}` |
| 3 | §1, p. 3 | The results of the analyses did not suggest any material reason to deviate from the standard ISDA fallback methodology. | ch1: SA adopted the ISDA methodology unchanged. | `\citep[§1, p.~3]{sarb2025fallback}` |
| 4 | §2 Background, p. 4 | Following the TPCWs initial proposal in November 2024 and the subsequent public consultation process, this document confirms the MPG’s endorsement of the approach recommended by the TPCW. | bibliography: establishes the November 2024 consultation and that this is the MPG's endorsement (hence 'MPG final recommendation'). | `\citep[§2, p.~4]{sarb2025fallback}` |
| 7 | §4.1, p. 7 | The five-year lookback period is specified relative to the respective IBOR’s cessation announcement date (spread adjustment fixing date), after subtracting both the tenor for the relevant IBOR and the two-banking-day payment delay, as per Appendix 1 of [6]. | ch2/appC: exact definition of the lookback window used for s. | `\citep[§4.1, p.~7]{sarb2025fallback}` |
| 9 | §5.1, p. 9 | a formal announcement on the Jibar cessation is expected in December 2025. This would serve as the Jibar cessation trigger date. | ch1 timeline: expected trigger date (realised 3 December 2025, per SARB media release and BISL note). | `\citep[§5.1, p.~9]{sarb2025fallback}` |
| 9 | §5.1, p. 9 | We restrict ourselves to a data set extending back to 4 January 2016 (where proxy data for ZARONIA is available). | appC: ZARONIA proxy history starts 4 January 2016. | `\citep[§5.1, p.~9]{sarb2025fallback}` |
| 10 | §5.2, Table 1, p. 10 | Calculated for 5 August 2024, Table 1 below presents spread adjustments for all Jibar tenors. | ch1/ch7: Table 1 (5 Aug 2024): 3M median 19 bp, mean 27 bp; 1M 15/17; 6M 59/74; 9M 74/97; 12M 92/123. | `\citep[§5.2, Table~1, p.~10]{sarb2025fallback}` |
| 11 | §5.2, Table 2, p. 11 | Spread adjustments are then calculated for the end of December 2025 and presented in Table 2 below: | ch1/ch7: projected Dec 2025 3M median 18 bp (mean 15); the realised fixing was 16.19 bp: quote both when discussing the CAS. | `\citep[§5.2, Table~2, p.~11]{sarb2025fallback}` |
| 11 | §5.3.1, p. 11 | As an overnight index, ZARONIA has been published by the SARB since 1 August 2022. The SARB has provided proxy data backdated to 4 January 2016. | appC data classes: NOTE the date 1 August 2022 here versus the observation period from 1 November 2022 in the data-engineer lesson; reconcile against the SARB benchmark page before citing. | `\citep[§5.3.1, p.~11]{sarb2025fallback}` |
| 12 | §5.3.2, p. 12 | The adoption of a new Monetary Policy Implementation Framework (MPIF) phased in from June 2022, redefines what was previously an overnight market with a liquidity shortage policy (maintained by the SARB) as an overnight market with a liquidity surplus policy and a tiered flooring system. | ch1/ch5 failure mode: a regime change in the basis process (MPIF) inside the five-year window; relevant to the mean-reversion caveat of Thm 3. | `\citep[§5.3.2, p.~12]{sarb2025fallback}` |
| 12 | §5.3.3, p. 12 | The impact on the spread between Jibar and the compounded ZARONIA rate is such that a cycle of rate cuts widens this spread while a cycle of rate hikes narrows this spread with no floor (meaning the compounded ZARONIA rate can be higher than Jibar at times). | ch5 basis dynamics: the realised basis B is driven by policy-rate cycles inside the compounding window; supports modelling B with its own noise and possibly mean reversion. | `\citep[§5.3.3, p.~12]{sarb2025fallback}` |
| 13 | §5.4, p. 13 | working with 31 December 2025 as the cessation announcement date or trigger date, the start of a five-year lookback period would be 1 October 2020 for 3M Jibar (ignoring lags and calendar effects). | appC: the lookback window for 3M (approximately Oct 2020 – Sep 2025). | `\citep[§5.4, p.~13]{sarb2025fallback}` |
| 14 | §6 Recommendation, p. 14 | It is recommended that the Jibar fallback rate comprises a compounded South African Rand Overnight Index Average (ZARONIA) rate and a spread that accounts for the differences between Jibar and ZARONIA. | ch1/ch2: the formal recommendation R(T,T+Δ) + s. | `\citep[§6, p.~14]{sarb2025fallback}` |

## Highlighting log

13 of 13 passages highlighted with PyMuPDF `search_for` + `add_highlight_annot`.
