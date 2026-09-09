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
