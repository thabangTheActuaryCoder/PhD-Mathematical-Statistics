# oliveira2024

**Record.** Oliveira, R. I., Orenstein, P., Ramos, T., Romano, J. V. (2024). Split conformal prediction and non-exchangeable data. *Journal of Machine Learning Research* 25(225), 1–38. Submitted 11/23, revised 7/24, published 7/24. Editor Chris Oates.

**URL.** https://jmlr.org/papers/volume25/23-1553/23-1553.pdf (abstract https://jmlr.org/papers/v25/23-1553.html; code https://github.com/jv-rv/split-conformal-nonexchangeable)

**Licence / access.** JMLR: CC BY 4.0 (journal policy). Downloaded 2026-09-09; 38 pages; first page matches the record.

**Status.** downloaded. File: `References/PDF/oliveira2024.pdf`; highlighted copy: `References/PDF/oliveira2024.highlighted.pdf`. Processed 2026-09-09 by thesis-reference-librarian.

**Librarian note.** This is the closest prior work to Chapter 3 (GROUND-TRUTH Thm 6). Their blocking lives in the PROOF (Blocking Technique, Prop. 10), not in the algorithm; the coupling cost in their feasible set is 4(m−1)β(a)+β(r), against the thesis's (n+1)β(b) via Yu (1994) Lemma 4.1. They optimise block sizes inside the bound (p. 8) but prove no lower bound: that is the room Theorem 9 occupies.

## Passages relevant to this thesis

Excerpts are verbatim from the PDF text layer (ligatures and spacing as extracted). 'Locator' is the number as printed in the source.

| Page | Locator (as printed) | Verbatim excerpt | Why it matters (chapter / ground-truth result) | Cite as |
|---|---|---|---|---|
| 2 | §1, p. 2 | Importantly, split CP is computationally simple, avoiding intensive routines such as bootstrapping, ensembling or blocking. Finally, the method is exactly the same as the one used for the iid data | ch3 chapter notes: in Oliveira et al. the algorithm is unblocked; the thesis blocks the scores themselves. State the difference. | `\citep[p.~2]{oliveira2024}` |
| 5 | eq. (5), p. 5 | First, it is necessary to have some form of concentration over the calibration data, as well as a degree of decoupling over the test data. | ch3 §setup: their two abstract conditions (concentration ε_cal, decoupling ε_train) are what the thesis replaces by one Berbee coupling event. | `\citep[eq.~(5), p.~5]{oliveira2024}` |
| 5 | Theorem 1, p. 5 | Theorem 1 (Marginal coverage over test data) Given α ∈(0, 1) and δcal > 0, if conditions (5) and (6) hold, then, for all i ∈Itest: P[Yi ∈C1−α(Xi)] ≥1 −α −εcal −δcal −εtrain. | ch3 Thm 6(i) comparison: additive penalty structure 1−α−(concentration)−(decoupling). | `\citep[Thm.~1]{oliveira2024}` |
| 7 | §3.3, p. 7 (definition of β(a)) | The process is said to be β-mixing if β(a) →0 when a →∞. | ch2 mixing section: their β-mixing coefficient is the TV distance between the joint law of (Z_{−∞:0}, Z_{a:∞}) and the product of marginals, stationary form. The thesis uses the non-stationary supremum-over-origins form; say so. | `\citep[§3.3, p.~7]{oliveira2024}` |
| 7 | §3.3, p. 7 (Blocking Technique attribution) | In particular, the so-called Blocking Technique (Yu, 1994; Mohri and Rostamizadeh, 2010; Kuznetsov and Mohri, 2017) allows one to compare a β-mixing process with another process made of independent blocks. | ch2/ch3: attribution chain for blocking; Yu 1994 is the primary source the thesis proves in full. | `\citep[§3.3, p.~7]{oliveira2024}` |
| 7 | eq. (12) and F_cal, p. 7 | Fcal = {(a, m, r) ∈N3 >0 : 2ma = ncal −r + 1, δcal > 4(m −1)β(a) + β(r)}, | ch3 Thm 6 remark: their coupling cost is 4(m−1)β(a) plus a train–calibration gap penalty β(r); the thesis pays (n+1)β(b) once. Quote when comparing constants. | `\citep[eq.~(12), p.~7]{oliveira2024}` |
| 8 | Theorem 4, p. 8 | Theorem 4 (Marginal coverage: stationary β-mixing processes) Suppose the sample (Xi, Yi)n i=1 is stationary β-mixing. Then given α ∈(0, 1) and δcal > 0, for i ∈Itest, P [Yi ∈C1−α(Xi)] ≥1 −α −η, with η = εcal + εtrain + δcal, where εcal is as in (12) and εtrain = β(i −ntrain). | ch3 chapter notes and ch4 positioning: the published marginal bound under β-mixing for unblocked split CP. | `\citep[Thm.~4]{oliveira2024}` |
| 8 | p. 8, remark after Theorem 4 | We emphasize that this optimization of block sizes plays a role exclusively on the coverage guarantees below; the split CP algorithm itself remains unchanged. | ch4 Thm 9: they optimise (a, m) inside the bound (m = n^λ, a = n^{1−λ}/2 with 1/2 < λ < (b−c)/(b+1) for β(k) ≤ k^{−b}) but the design is not a procedure and no lower bound is proved. Theorem 9(i) makes the block-length choice explicit for the BLOCKED route (exact minimiser, expected conditional shortfall from Thm 6(ii)); it is not a minimax claim (GROUND-TRUTH corrections 9–12). | `\citep[p.~8]{oliveira2024}` |
| 8 | p. 8, rate remark | Under certain assumptions over the dependence of the processes, the stationary β-mixing bounds given by (12) are of the same asymptotic order as the corresponding iid bounds. | ch4: their claim that polynomial mixing β(k) ≤ k^{−b}, b > 1, recovers the iid order; compare with the N^{−r/(2r+3)} rate of the blocked design and the Barber–Pananjady N^{−r/(r+1)} marginal rate (LESSONS 2026-09-09). | `\citep[p.~8]{oliveira2024}` |
| 12 | Example 2, p. 12 | Consider a β-mixing sequence generated from a random walk on the cycle graph. | ch4 Thm 9(ii) lower-bound construction: an explicit hidden-Markov β-mixing example with β(r) decaying at rate e^{−r/v²} for v vertices (geometric, so it lies in every B_r; a polynomial-mixing construction is still needed). | `\citep[Ex.~2, p.~12]{oliveira2024}` |
| 21 | Proposition 10 (Blocking Technique), pp. 20–21 | If h : Rmb →R is a Borel-measurable function with \|h\| ≤M for some M > 0, then \|E[h(Bodd)] −E[h(B∗ odd)]\| ≤2M(m −1)β(a), | ch2 Lemma prelim-yu / App B: the expectation form of Yu's blocking lemma with constant 2M(m−1)β(a); for indicators (M = 1) this is twice the TV cost (m−1)β(a) the thesis uses. Cite when explaining why the thesis's constant is (n+1)β(b). | `\citep[Prop.~10, pp.~20--21]{oliveira2024}` |
| 22 | Proposition 13, proof, p. 22 | To ﬁx this problem, it will be necessary to create a gap between our training and calibration data and use the Blocking Technique, Proposition 10, to transpose our problem to an independent setting. | ch3 Assumption mix: independent confirmation that a gap between the fitting sample and calibration is needed when the score depends on training data (the thesis's D_fit gap of length b). | `\citep[Prop.~13, p.~22]{oliveira2024}` |

## Highlighting log

12 of 12 passages highlighted with PyMuPDF `search_for` + `add_highlight_annot`.
