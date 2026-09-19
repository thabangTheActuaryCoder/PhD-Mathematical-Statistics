# Chapter 7 (The South African Converted Book) — round 1 response

Chapter file: `/Users/thabangbaloyi/Desktop/PhD Thesis/Council Workspace/thesis/chapters/ch7-zar-coda.tex`.
Every numbered item of `round-1-review.md` is closed below as DONE, DECLINED or DEFERRED.

## Lessons applied

- `[2026-09-19][review-panel][ch7,ch1,ch8]` — a negative feasibility finding is stated for the BLOCKED route only, and the unblocked marginal bound is evaluated on the same record before anything is called vacuous. (Item 1; new §7.3.4, Table 7.3.)
- `[2026-09-19][review-panel][ch7,ch4]` — the record-length condition is necessary only; feasibility is not monotone in $N$. (Item 2; Proposition 7.1(iii)–(iv) and its gap box.)
- `[2026-09-19][review-panel][ch7,ch3,ch6]` — $N$ is the calibration record, the deployment block begins after it. (Item 3; §7.3.2 "What $N$ counts", Tables 7.1–7.3 and the figure plan.)
- `[2026-09-19][review-panel][ch7]` — a scoring frequency that drives an infeasibility verdict is justified or the verdict is stated as conditional. (Item 5.)
- `[2026-09-19][review-panel][ch7,ch5]` (three entries) — undiscounted Bachelier premia must declare $P=1$; $c^*=1$ is a 3.9 per cent book assumption, not a one per cent one; the quoted half-width is not linear in $\eta$ at the top of the bracket. (Items 9, 10, 14.)
- `[2026-09-19][review-panel][ch7,ch1]` — the converted book is a sub-book. (Item 8.)
- `[2026-09-19][review-panel][ch7,ch5]` — the book reserve covers the at-the-money coordinate only. (Item 12.)
- `[2026-09-19][review-panel][ch7,ch3,ch5]` — a reserve equation states whether it is a total or an add-on and argues or gaps the double counting. (Item 11.)
- GROUND-TRUTH corrections 9, 11, 12 — the blocked rate is never called minimax; Barber and Pananjady (2026) are cited wherever Theorem 6(i) is discussed; the calibration-conditional object is named as such. (Items 1, 3.)
- STANDARD single-source rule and `[2026-09-09][orchestrator][all]` "Say it once". (Items 6, 7.)
- `[2026-09-11][revision-writer][ch4,ch3,ch6]` — two routes are compared only when the accounting charges the same terms; Table 7.3 therefore prints both calibration-count conventions rather than the flattering one. (Item 1.)
- `[2026-09-11][revision-writer][ch2,ch3,ch4]` — the 5–8 line abstract is 85–135 words. (Item 19.)
- `[2026-09-09][bibliography-verifier][all]` — a new `\bibitem` is web-verified by the verifier before use. (Item 16, deferred.)
- `[2026-09-09][review-panel][appC,all]` and `[2026-09-09][scout][ch1,ch5,ch7]` — dated absence, never proof of absence. (Item 21.)
- `[2026-09-10][revision-writer][ch5,ch7,ch8]` — the book-level corollary is a supremum, not a variance; the per-expiry variant never cancels. (Items 6, 12.)

---

## Point-by-point

### 1. [ADD] The unblocked marginal route — must — **DONE**

New subsection §7.3.4 "The route that survives without blocking" (`sec:zar-marginal`), with equation `eq:zar-marginal` and Table `tab:zar-marginal`. The bound is stated as \citep[Cor.~1, eq.~(6)]{barber2026} with $L=0$ justified from the fixed-policy construction, and evaluated on the same record: under $\Bclass{2}(1)$ the deficit is $0.280$ at $\tau=5$ on twenty-four scores, a marginal level of $0.620$, which clears criterion C2; the table also prints $n=17,18,23$ and the classes $\Bclass{1.5}(1)$ and geometric $\varphi=0.3$ (all recomputed here and agreeing with the panel's figures to three decimals). What blocking buys and this does not — the exact $\Beta(k,n+1-k)$ law and the calibration-conditional statement of Theorem 6(ii), the drift term of Theorem 6(iii), the gap-separated deployment block — is stated in the following paragraph, with the note that the paper contains no calibration-conditional result.

The headline is restated in four further places: the chapter abstract ("the unblocked marginal bound survives on the same scores at a level of about 0.62; what it costs is the calibration-conditional statement"), §7.1 ¶2–3, the verdict (§7.3.3, now "the blocked certificate has no admissible block length"), and §7.9.1. Remark `rem:zar-notrepair` is retitled "What is and is not a repair" and carries the fourth route as the one that works. The words "vacuous under every mixing class" and "the certified quantile is unavailable" are gone; nothing in the chapter now calls the blocked rate minimax or optimal.

### 2. [PROVE] Proposition 7.1(iii) — must — **DONE**

The panel's in-place correction survives verbatim: (iii) still claims necessity plus attainment at $N=N_{\min}$ and still records that the converse fails. The sufficient condition is now proved rather than gapped: new part (iv) states that $N\ge2(m+1)\max\{m,b_\gamma\}$ implies feasibility, and that any integer $b\in(N/(2m+2),N/(2m)]$ works; the proof is the three-line argument (the interval has length $N/(2m(m+1))\ge1$, so it contains an integer; that integer forces $n=m$ exactly; and $b>N/(2m+2)\ge b_\gamma$ gives the budget). The `\gap{}` box is kept and narrowed: it now records the counterexample, the non-monotonicity, and that the exact threshold $N^*$ lies in $[N_{\min},2(m+1)\max\{m,b_\gamma\}]$ and is not identified. §7.3.5's opening sentence no longer says part (iii) "answers the first half exactly"; it says (iii) bounds the length from below and (iv) from above. No other passage relies on the withdrawn equivalence (checked: §7.8 item 1 and §7.9.3 use the arithmetic directly, not the converse).

### 3. [FIX] The record count and the $N=18$ row — must — **DONE**

New paragraph "What $N$ counts" in §7.3.2 fixes the convention once, inheriting it from Chapter 3: $N$ is the calibration record, the gaps are inside it, the deployment block begins immediately after, so a calendar count of $M$ monthly observations gives $N=M-b$ and $N=M-1$ at $b=1$. Propagated everywhere:

- Table 7.1 (`tab:zar-feasible`) is rebuilt with an $M$ column and an $N=M-b$ rule. The strict reading ($M=18$) now reads infeasible at $b=1,2,3$ ($n=8,4,2$ against $k=9,5,3$); a "first feasible" row at $M=19$ ($N=18$, $n=k=9$, $10\beta(1)$) is added; the pooled reading ($M=24$) gives $N=23$, $n=k=11$, $k/(n+1)=0.917$, $12\beta(1)$.
- Table 7.2 (`tab:zar-geom`) multiplier $13\to12$ throughout; the budget inversions become $\beta(1)\le0.0333$ and $\le0.00417$, and the AR(1) coefficients $0.067$ and $0.008$ (recomputed).
- "Thirteen times a one-month mixing coefficient" is gone from the abstract, §7.3.2, §7.3.3, Remark `rem:zar-whatfails`, §7.6 and §7.9.1; the figure is now twelve on the pooled count, ten at the first feasible calendar length, and none on the strict count. $13C\to12C$, $C\ge1/13\to C\ge1/12$, $\Beta(12,1)\to\Beta(11,1)$ with $0.05^{1/11}=0.762$, and the 2031 row $13\beta(2)=3.25\to12\beta(2)=3.0$ (and $0.13\to0.12$).
- The `\figplan` grid is re-cut to $N\in\{17,23,104,270,375\}$ with the $N=17$ curve empty and the $N=23$ curve the single point $(1,12)$.

### 4. [FIX] The headline rests on an inadmissible pooling — must — **DONE**

The strict count is now the chapter's primary case and is labelled as such in §7.3.2, in the verdict, in both table captions and in §7.9.1; the count of twenty-four is called the "pooled reading", carried only as a sensitivity, and the sentence that introduces it points at Remark `rem:zar-notrepair`, which is in turn amended to say that the pooled count performs exactly the operation it forbids. The abstract quotes the pooled figure only as the more favourable of the two and no longer presents it as the record.

### 5. [CLARIFY] Monthly rebalancing — must — **DONE** (route (b))

The unsupported clause is replaced by a "Scoring frequency" paragraph in §7.3.2 (~140 words) that takes the review's option (b): monthly scoring is declared a design choice of the chapter, the three reasons it is not forced (public daily fixings, a daily-marking desk, Chapter 6's daily book) are stated, every feasibility statement below is declared conditional on it, and the reader is pointed to §7.3.5, where the same book scored daily is feasible within thirteen months. Carried into the abstract ("The verdict is a finding about monthly scoring") and into §7.9.1 and the limitations.

### 6. [CUT-REPETITION] Chapter 6 and Chapter 5 restated — must — **DONE**, all six passages

- §7.1 ¶2 cut to the one sentence the review prescribes (~120 words saved).
- §7.3.2's "South African analogue of the figure of about 126" clause deleted.
- The $k/(n+1)$ rule sentence deleted; the values kept.
- §7.5.1 ¶1 replaced by the one-sentence reminder with both forms and the reference.
- Remark `rem:zar-longshort` cut to the two South African sentences (V6 cannot be tested here; the public regime takes the absolute form).
- §7.4.1 ¶1 compressed to two sentences with references.

### 7. [REMOVE] Seven pages over budget — must — **DEFERRED in part to round 2**, with the cuts made and the residual quantified

Made: all of item 6 (~425 words), §7.7 compressed from four paragraphs to the sharp one plus a compressed summary (~200), §7.8 items 1 and 4 and the fallback paragraph (~150), §7.9.3 ¶2 (~110), the abstract (~110), both `\figplan` boxes (~180), three `\datanote{}` boxes (~180), §7.1 ¶4's section map (~110), and about 250 more across §7.2, §7.4, §7.5.2 and §7.6 — roughly 1,700 source words removed, including every passage the review's §5 named and every instance of the chapter announcing its own honesty except the one in `rem:zar-whatfails` that the review asked to keep.

Not achieved: the chapter is still over budget, because items 1, 2, 3, 5, 8–14 and 17 are must- or should-additions that together cost about 2,400 source words — the marginal subsection and its table alone are about 600. Measured on the review's own rule (strip comments and control sequences): **8,031 before, 9,521 after**, or about 31.7 typeset pages against a budget of 20. The two demands cannot both be met inside this chapter in one round. The residual cut of about 3,500 words needs a structural decision that is not mine to take, and the response records the two candidates: move §7.5.2's worked illustration, its two tables and `fig:zar-book` to Appendix C (the declared home of data and computation, about 1,100 words), and move the per-caplet rand illustration of §7.4.3 to Chapter 5's worked example (about 250). A lesson is appended so the orchestrator sees the conflict rather than the overrun alone.

### 8. [ADD] Legacy trades that do not fall back — must — **DONE**

New paragraph in §7.2.1 after "The linear book converts mechanically": 2006-Definitions trades without the April 2025 Benchmark Module fall to Reference Rate quotations and then to Calculation Agent determination \citep[Sect.~5]{isda2025}, and neither the 2020 Protocol nor Supplement 70 covers JIBAR \citep[Sect.~8]{isda2025}. The consequence is stated: everything in the chapter concerns the converted \emph{sub-book}, and the institution must separate it from the polled residue before it can produce the score record or the vega schedule of §7.8. §7.8 item 1 repeats the qualification in four words.

### 9. [FIX] Assumption A5 — must — **DONE**

A5 now gives the growth law $c^*=1+\tfrac1{24}(2-3\rho^2)\nu^2\tau^*$, the range across the ladder ($1.004$ at three months, $1.014$ at one year, $1.064$ at five years — recomputed here), the book aggregate $\sum\sqrt{\tau^*_i}c^*_i=32.693$ against $31.452$, i.e. an understatement of 3.9 per cent for the book, and the net sign of the two opposite errors: $\eta q=18.619$ bp against the exact $18.429$ bp at one year, so a 1.0 per cent overstatement there, against an understatement of about five per cent at the long end.

### 10. [ADD] No discounting — must — **DONE**

New assumption A7: the Bachelier expression is a forward premium, so $P(0,T_i+\Delta)=1$; the discount-weighted aggregate at a flat eight per cent is $24.268$ against $31.452$, so the reported half-width is about 23 per cent above its present value. Equation `eq:zar-bookwidth` now carries "undiscounted, by assumption A7" and the present value R24,204 per basis point; Table 7.4 gains a present-value column (R96,816 / R484,080 / R1,549,056, computed here) and says so in its caption.

### 11. [CLARIFY] Equation `eq:zar-reserve` — must — **DONE**

§7.6 now says first that $\mathcal R$ is a total carrying amount and that the reserve proper is the second and third terms, and second that "different questions" is not an argument for additivity. The overlap is named (the scores are measured against a policy whose own mark lies inside the identified set), the separation argument the review offers is given in full (a static measure-side width fixed at the reserve date against a quantile of realised profit and loss over one block, so a constant mismarking enters only through its change over the block), and it is labelled as an argument and not a proof. A `\gap{}` box records what must be established: a bound on the part of the score attributable to a constant mismarking within the identified set over one block.

### 12. [ADD] The skew coordinate — should — **DONE**

New paragraph at the end of §7.5.1: Chapter 5 identifies an ellipse in the level–skew plane, Corollary `cor:ident-book` aggregates the level only, the analogous skew aggregate is $\eta\nu/(2\alpha_0)\sum_i|\varsigma_i|q_ic^*_i$ per unit of strike over a skew-vega schedule, and the reserve below is therefore a lower bound for any book that is not purely at-the-money vega. Repeated in one clause in the limitations.

### 13. [ADD] Assumption A3 — should — **DONE**

A3 now says it is the maximal-vega case and not the contractual one: a converted book keeps the old strikes while the underlying moves by $s=16.19$ bp plus the forward basis, and at a 60 bp normal volatility a 20 bp moneyness shift costs about ten per cent of the Bachelier vega at the three-month expiry, four per cent at one year and one per cent at five (computed here from $\varphi(d)/\varphi(0)$). Named again in the limitations.

### 14. [FIX] "It is linear in $\eta$" — should — **DONE**

§7.4.3 now separates the exactly linear object, $[a-\eta,a+\eta]$ of Theorem `thm:ident-two`(i), from the quoted half-width, which is not linear because $\alpha_0^\pm=a\mp\eta$ and $\nu^\pm=na/(a\mp\eta)$; R65,800 is labelled a linear extrapolation, $\alpha_0=1.73$ bp and the divergence of the Hagan bracket at $\eta=64$ bp against $a=65.73$ bp are stated, $\varepsilon\approx1.07$ is quoted, and the honest reading is given as an order-of-magnitude statement. Table 7.4's caption flags the $\eta=64$ row; §7.8 item 4 and the limitations carry the qualification.

### 15. [CITE] The one published dynamic study — should — **DONE**

`\citep[Sec.~3, p.~5 and Sec.~5.1, Table~4]{alfeus2026}` added at the sentence in §7.4.2, locators checked against `References/Highlights/alfeus2026.md`. The derivation stays in Chapter 5. The key is also added to the chapter notes.

### 16. [CITE] The clearing-house gap box — should — **DEFERRED to `thesis-bibliography-verifier`, then round 2**

The gap box is unchanged. `bibliography.tex` has no `lch` key, and this brief forbids me to edit any file but the chapter, the response and LESSONS; the review itself routes the two `\bibitem`s to the verifier. Once they exist, §7.2.1's box becomes one cited sentence and §7.2.2's clause "on the date recorded in the gap box above" takes the citation. The chapter has been written so that nothing depends on the dates: they bound the start of the score record only.

### 17. [CITE] The collateral convention — should — **DONE**

New paragraph at the end of §7.2.2 with the verified quotation and locator `\citep[\S8.2, p.~27]{sarb2024conv}`: sponsor screens assume a USD-denominated zero-threshold CSA with SOFR collateral, a cleared book's discounting moves to a ZARONIA basis on the date the gap box records, the two are not the same basis, and every rand figure in the chapter is on the sponsor basis. The difference is declared unquantified rather than guessed.

### 18. [FIX] 360 versus 375 — should — **DONE**

§7.3.5 now reads $N\approx375$ at eighteen months, with $b=20$, $n=k=9$ and the unchanged deficit $0.025$. The same sentence in §7.8 item 1 no longer restates the arithmetic at all (item 6), so the error cannot recur there.

### 19. [FIX] The chapter abstract — should — **DONE**

Rewritten to 131 words (5–8 lines at 17 words a line): the blocked verdict correctly qualified, the marginal alternative and its level, the monthly-scoring condition, the valuation side in one clause, and the sentence on no number being computed from data, which survives as the closing line.

### 20. [CLARIFY] "Half the nominal level" — should — **DONE**

Replaced by "A certified level of one half, criterion C2 of Chapter~\ref{ch:usd}", so $\gamma=0.4$ follows from $0.9-0.5$ and Table 7.2 is reproducible.

### 21. [CITE] Regulatory claims — should — **DONE**

The two-thirds sentence is gone with the rewritten $\alpha=0.2$ paragraph, which now states the budget $\gamma=0.4$ of criterion C2 and nothing supervisory. "\gls{ava}" is replaced by "a valuation adjustment for model uncertainty", and a `\datanote{}` records that the European term of art is not used here, that no primary source establishing a South African prudential requirement specific to valuation uncertainty on converted benchmark books is on file as of 19 September 2026, and that none is asserted. The note claims a state of the project's files, not an exhaustive search, which is the only absence I can honestly date.

### 22. [CITE] The cessation locator — should — **DONE**

Split as prescribed: `\citep[p.~1 and Sect.~1]{isda2025}` for the cessation date, `\citep[Sect.~1.1]{isda2025}` for the Index Cessation Event. The chapter notes list the full locator set actually used.

---

## Missing-content paragraph (review §4)

The three named absences are closed by items 1, 8 + 16 + 17 + 13 + 21, and 12 respectively, and the reserve equation gains the paragraph and the gap box item 11 asks for. The one suggestion not taken is the extra sensitivity row for a long-short or realistically profiled book: **DEFERRED to round 2**. It is a new arithmetic table in a chapter that is already over budget, and Remark `rem:zar-longshort` plus Chapter 5's corollary already state what it would show (the factor 4.27 is a property of the aggregation rule under A2, and the per-expiry variant never cancels). It should be added in the same pass that moves the worked illustration to Appendix C.

## New `\gap{}` boxes

1. §7.3.1, after the proof of Proposition 7.1 — replaces the panel's box: the counterexample and non-monotonicity are kept, and what remains open is narrowed to the exact threshold $N^*\in[N_{\min},\,2(m+1)\max\{m,b_\gamma\}]$, the sufficient condition itself now being proved as part (iv).
2. §7.6, after the additivity paragraph — the overlap between the identification width and the certified hedging-error quantile is argued, not proved; what must be established is a bound on the part of the score attributable to a constant mismarking within the identified set over one rebalancing block.

The pre-existing clearing-house citation gap box in §7.2.1 is unchanged (item 16).

## Word count

| | Source words (comments and control sequences stripped) | Typeset pages at 300 words |
|---|---|---|
| Before (panel's count) | 8,031 | 26.8 |
| After | 9,521 | 31.7 |
| Budget | 6,000 | 20 |

About 1,700 words were cut and about 2,400 added, all of the additions mandated by must- or should-items above. The overrun is item 7's residual and is deferred with the two structural candidates named there.
