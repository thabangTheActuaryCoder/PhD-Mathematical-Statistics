# sarb2025ois

**Record.** South African Reserve Bank, Market Practitioners Group, Derivatives Workstream (2025). *Historical estimation of the ZARONIA OIS curve*. Document dated 6 October 2025 (cover page 2); posted on resbank.co.za 9 October 2025 (server Last-Modified 09 Oct 2025). 16 pages, with five .xlsb workbooks.

**URL.** https://www.resbank.co.za/content/dam/sarb/publications/financial-markets/committees/mpg/mpg-ralated-documents/2025/Historical%20estimation%20of%20the%20ZARONIA%20OIS%20curve.pdf (landing page https://www.resbank.co.za/en/home/publications/publication-detail-pages/Financial-Markets/Committees/MPG/MPG-Related-pages/2025/historical-estimation-of-the-zaronia-ois-curve)

**Licence / access.** Public SARB document (© South African Reserve Bank). Primary source. Downloaded 2026-09-09 with a browser User-Agent (the SARB WAF rejects bare curl); first page matches the record.

**Status.** primary document. File: `References/PDF/sarb2025ois.pdf`; highlighted copy: `References/PDF/sarb2025ois.highlighted.pdf`. Processed 2026-09-09 by thesis-reference-librarian.

**Librarian note.** BIBLIOGRAPHIC: the document is dated October 6, 2025 and was posted 9 October 2025; References.bib says '10 October'. Use '6 October 2025 (published 9 October 2025)'. The synthetic curve is JIBAR forwards minus a rolling MEDIAN spread: use it for discount factors and forwards only; never estimate η, ρ_BF, ρ_Bα from it (LESSONS data-engineer-zar).

## Passages relevant to this thesis

Excerpts are verbatim from the PDF text layer (ligatures and spacing as extracted). 'Locator' is the number as printed in the source.

| Page | Locator (as printed) | Verbatim excerpt | Why it matters (chapter / ground-truth result) | Cite as |
|---|---|---|---|---|
| 4 | §1 Overview, p. 4 | The Derivatives Workstream (DWS), a component of the South African Reserve Bank’s (SARB’s) Market Practitioners Group (MPG), was tasked with developing historical swap curves based on interest rate swap contracts that reference the South African Rand Overnight Index Average (ZARONIA). | appC §synthetic curve; ch7: what the dataset is and who produced it. | `\citep[§1, p.~4]{sarb2025ois}` |
| 4 | §1 Overview, p. 4 | with one of the primary applications being the generation of historical scenarios for Value-at-Risk (VaR) and Expected Shortfall (ES) models. | ch1/ch7: intended use is VaR/ES scenario history, i.e. a risk-management resource, not a pricing curve. | `\citep[§1, p.~4]{sarb2025ois}` |
| 4 | §2 Data requirements, p. 4 | The available historical data span from early 2005 through to the end of 2024. | appC data register: date range of the synthetic curve (daily 3 Jan 2005 to 31 Dec 2024). | `\citep[§2, p.~4]{sarb2025ois}` |
| 4 | §2, footnote 2, p. 4 | the JSE’s zero curve dataset is missing data for four historical dates, viz. 24-Dec-07, 02-Jan-09, 24-Nov-11, and 21-May-13. | appC data-quality list: the four missing dates. | `\citep[§2, fn.~2, p.~4]{sarb2025ois}` |
| 4 | §2, p. 4 | For the period from 2000 to 2015, the South African Futures and Options Exchange (SAFEX) overnight rate, as chosen by the DWS, serves as a suitable proxy for the ZARONIA rate. | appC/ch7: the ZARONIA proxy before 2016 is the SAFEX overnight rate; ZARONIA (proxy) itself is available from the beginning of 2016. | `\citep[§2, p.~4]{sarb2025ois}` |
| 6 | §3 Step 3, eqs (1)–(3), p. 6 | which is simply the median3 of the Jibar-ZARONIA spreads over the period determined by y. | ch5/ch7: the basis in the synthetic curve is a deterministic rolling median s_y(t) applied as f_1bd(t+y) = f_3M(t+y) − s_y(t); no basis volatility can be read from it. | `\citep[§3, eqs~(1)--(3), p.~6]{sarb2025ois}` |
| 6 | §3, footnote 3, p. 6 | The median statistic is chosen for the same reasons provided by the International Swaps and Derivatives Association (ISDA) in their speciﬁcation of fallback rates | ch1: the median convention is inherited from the ISDA fallback methodology. | `\citep[§3, fn.~3, p.~6]{sarb2025ois}` |
| 6 | §3 Step 4, pp. 6–7 | Apply linear interpolation over the domain [0, 5]. | appC: spread term structure is linear to 5Y then flat (next bullet on p. 7: 'use flat extrapolation'). | `\citep[§3, pp.~6--7]{sarb2025ois}` |
| 7 | §3 Step 7, p. 7 | spot-starting single-period (SSSP) OIS contracts, with maturities from 1 month (1M) to 12 months (12M) in 1-month increments; and | appC: benchmark instruments (SSSP 1M–12M monthly; SSMP 15M–30Y quarterly) whose fair rates are published. | `\citep[§3, p.~7]{sarb2025ois}` |
| 8 | §4 Results, p. 8 | Although it is challenging to fully assess the accuracy of the results, we provide visual comparisons with corresponding Jibar data. | appC/ch7 honesty: the producers themselves do not certify accuracy; the thesis must label the curve 'estimated'. | `\citep[§4, p.~8]{sarb2025ois}` |
| 8 | §4 Results, p. 8 | Provided in an Excel workbook titled “Benchmark_Rates.xlsb”, this workbook contains the estimated fair or par rates for all ZARONIA-based benchmark instruments previously speciﬁed | appC data register: the workbook names (Benchmark_Rates; Forecast_Curve_Expiry_Dates; Forecast_Curve_Discount_Factors; Discount_Curve_Payment_Dates; Discount_Curve_Discount_Factors). | `\citep[§4, p.~8]{sarb2025ois}` |
| 16 | Appendix B, p. 16 | It is also interesting to note how the spread has generally decreased through time, as evidenced by the data for 31-Dec-2024 versus that for 03-Jan-2005, as well as the percentile data. | ch7/ch5 failure mode: the JIBAR–ZARONIA spread trends down over 2005–2024, a non-stationarity to flag when the physical-measure basis is used as an ambiguity set. | `\citep[App.~B, p.~16]{sarb2025ois}` |

## Highlighting log

12 of 12 passages highlighted with PyMuPDF `search_for` + `add_highlight_annot`.
