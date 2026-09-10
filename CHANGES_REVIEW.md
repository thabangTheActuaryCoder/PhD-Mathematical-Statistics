# Changes and review log

Running record of the write, review, revise, compile loop. One entry per round. Newest first.

## 2026-09-09 - Repository scaffold
- Repository laid out in the MSc convention: `Thesis/Chapter N/src` and `Figures`, front-matter folders, `Thesis/Annexures`, `Code/`, `Research Proposal/`.
- Root `main.tex` uses the `report` class with chapters, natbib author-year, glossaries for acronyms, Wits Faculty of Science suggested layout (12pt, 40mm left margin, left-aligned).
- Institution held in three macros at the top of `main.tex`; a UFS conditional offer for 2027 sits in `Offer/`, the text is framed for Wits pending the candidate's decision.
- Council-corrected mathematics and three-year plan filed under `Research Proposal/`.
- Round one of the loop in progress: Chapter 2 and Chapter 3 drafting, data specifications, reference code, bibliography verification.

## 2026-09-09 - Round one, partial
- Chapter 2 (Preliminaries) drafted at about 15,000 words; every standard result proved in full; one gap box on the vol-of-vol curvature accounting, under finance review.
- Appendix C data sections written for USD and ZAR from primary sources; reference code for rates and for the conformal certificate written with passing tests.
- Bibliography verified (50 entries) and converted to BibTeX.
- Zero-hallucination pipeline added: References/PDF, References/Highlights, librarian and citation-enforcer agents; every borrowed result must carry a locator.
- Literature scan found Barber and Pananjady (2026) and Halkiewicz (2026); the optimal-blocking theorem is being restated before Chapter 4 is written.
- Canonical chapter labels introduced (ch:intro ... app:data).

## 2026-09-09 - Round one continued
- Chapter 3 (Certification) drafted and refereed: off-by-one in the gap lemma fixed, the normal approximation moved out of the theorem statement, positioning against Barber and Pananjady (2026) made explicit, every worked-example number verified by hand.
- Chapter 2 refereed on the finance half: Proposition 2's claimed 17 per cent curvature understatement withdrawn (the effect on the smile is about 0.002 basis points) and corrected in the source of record.
- Appendix A (Tenor consistency) drafted at about 5,700 words.
- All 50 references processed: 58 PDFs with highlighted copies, 50 highlight notes carrying exact locators, paywalled items recorded with DOIs. Three attribution errors and three bibliographic errors corrected.
- Reference code corrected: one AR(1) mixing constant, block counting fixed, exact optimal block length, Table 3.1 regenerated and reproduced by tests.
- Review reports written for Chapter 2 (22 must-items) and Appendix C (10 must-items).

## 2026-09-09 - Round one closed for Chapter 2, Appendix B and Appendix C
- Chapter 2: all 22 must-items closed. The withdrawn curvature claim removed from the abstract, introduction, worked example and figure; about twenty references to the writing process deleted; citation locators taken from the reference notes; the Beta law with atoms and the side-condition-free autoregressive mixing bound adopted so Chapter 3 can delete its duplicates.
- Appendix B created: ten sections, each proving one standard result and referencing its statement by number. Nine proofs moved out of Chapter 2, plus the derivation sketch of the Hagan approximation.
- Appendix C: 19 items closed. The reference implementation is now described from its source rather than its readme; twelve leaks of the writing process removed from note boxes; the fallback spread values marked as resting on no obtained primary source until the final rule is retrieved.
- Page budget reallocated between the appendices: the moved proofs run shorter than budgeted, and the citation apparatus costs more than the prose it certifies.

## 2026-09-10 - Round one closed for Chapter 3
- All 37 items applied, none declined. The chapter falls from 51 to 34 typeset pages against a 44-page budget, chiefly by deleting thirteen results that Chapter 2 and Appendix B now own.
- The coupling lemma of Chapter 2 proved insufficient for the conditional certificate: it gives mutual independence of the coupled copies but neither preserves the first block nor gives independence of the actual fitting sample. Chapter 3 now carries a named strengthening, proved from Berbee's lemma, and Chapter 2 is asked to absorb it in round two.
- The two-sided over-coverage counterpart of Chapter 4's minimax object is stated here, under a continuity hypothesis without which no such bound survives.
- The bootstrap and backtest comparison is staged for Chapter 6 and the block-length sweep for Chapter 4.
- The content map is rebuilt from the files themselves: 147 objects, each with one home.

## 2026-09-10 - Chapter 5 drafted
- Identifiability of the successor-rate smile written at about 12,300 words, deriving the fitted triple in closed form by matching the second and third cumulants of the predecessor rate and the variance of its realised variance.
- Three results are stronger than the plan assumed. The admissible correlations lie on a Schur-complement ellipse; the at-the-money identified interval is exactly the level plus or minus the basis volatility, with both endpoints attained, so the result is exact rather than first order; and the identified region in the level-skew plane is an ellipse rather than a rectangle.
- At the worked-example parameters the skew interval contains zero, so the sign of the successor skew is not identified at all.
- Two errors in the plan were corrected: the curvature does move at first order, and the earlier expressions for the fitted correlation and for the skew difference between the two matching models were dimensionally inconsistent.

## 2026-09-10 - Chapter 4 drafted
- Sharpness and optimal blocking written at about 13,300 words in twelve sections, absorbing the block-length sweep staged out of Chapter 3 and defining the sweep figure the data appendix points at.
- Structural check clean: environments balanced, all fourteen citation keys present, three gap boxes and seven data notes.
- The manuscript now compiles at 263 pages with Chapters 2 to 5 and Appendices A to C drafted.
