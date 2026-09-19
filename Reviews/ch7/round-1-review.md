# Chapter 7 (The South African Converted Book) — round 1 review

Panel perspectives adopted: forward measures; SABR; identifiability; benchmark reform; practitioner; South African context; regulatory; honesty auditor; examiner. The zero-hallucination citation rule was applied to every assertion in the chapter.

Chapter file: `/Users/thabangbaloyi/Desktop/PhD Thesis/Council Workspace/thesis/chapters/ch7-zar-coda.tex` (284 lines, 8,031 source words).

---

## 1. Verdict

**MAJOR.**

The chapter is well conceived — a negative result stated before any data are pulled, with the record length that would reverse it computed in the same arithmetic — and almost all of its numerical work is correct, which is rare for a first draft. But its principal finding is stated more broadly than it has been proved: the chapter concludes that the record is too short for *the certificate*, when what it has shown is that the record is too short for *the blocked route*, and the unblocked marginal bound of Barber and Pananjady (2026) — which GROUND-TRUTH correction 12 and two LESSONS entries require this thesis to cite wherever Theorem 6(i) is discussed — delivers a non-vacuous level of about 0.62 on the same twenty-four-month record under the same class $\Bclass{2}(1)$. Alongside that, Proposition 7.1(iii) is false as an "if and only if" (counterexample below), the headline figure of thirteen rests on a pooling of pre-cessation scores that the chapter's own Remark 7.6 declares inadmissible, the monthly rebalancing frequency that drives the entire negative result is asserted and never justified, and the chapter runs about seven pages over its twenty-page budget with roughly 1,200 words duplicating Chapters 5 and 6.

### Verification of the load-bearing arithmetic (requested)

Recomputed independently from the definitions in Chapters 3 and 4 ($n=\lfloor N/(2b)\rfloor$, $k=\lceil(1-\alpha)(n+1)\rceil$, finite threshold iff $k\le n$, coupling cost $(n+1)\beta(b)$):

| Claim | Holds? |
|---|---|
| Feasibility ceiling $b\le N/(2m)$, and $b\le N/18$ at $\alpha=0.1$ | **Yes.** $\lceil(1-\alpha)(n+1)\rceil\le n \iff n\ge(1-\alpha)/\alpha \iff n\ge m$; $\lfloor N/(2b)\rfloor\ge m \iff b\le N/(2m)$. Both steps are correct for integer $n,m$. |
| At a 24-period record the only feasible block length is $b=1$ | **Yes** as stated ($24/18=1.33$). **But** see item 3: if the twenty-four months are the whole post-cessation record, one month must be the deployment block, $N_{\mathrm{cal}}=23$, and the conclusion is unchanged; at eighteen months $N_{\mathrm{cal}}=17$ gives $n=8<9$ and *no* finite threshold at any $b$, which the chapter does not report. |
| "Thirteen times a one-month mixing coefficient" | **Arithmetically yes** ($n=12$, $(n+1)\beta(1)=13\beta(1)$), **but not admissibly**: 13 requires $N=24$, which requires the pre-cessation pooling that Remark 7.6 forbids (item 4), and requires the deployment month not to be counted (item 3). On the strict reading the figure is 10 (at $N_{\mathrm{cal}}=18$) or the record is infeasible outright (at $N_{\mathrm{cal}}=17$). |
| Table 7.1 (all twelve entries), Table 7.2 (all seven rows), $\beta(1)\le0.0308$ and $\le0.00385$, AR(1) inversions 0.06 and 0.008, the $\alpha=0.2$ row (level 0.665), the 2029 row ($13\beta(2)$, 3.25, 0.13), $0.05^{1/12}=0.779$ and $0.05^{1/9}=0.717$, the daily figures $10/225=0.044$ and $10/400=0.025$, the weekly figures $0.44$, $0.027$ and $\varphi_{\max}=0.34$ | **All correct.** |
| $N_{\min}$ values 630 / 270 / 108, 162 / 90 / 54, and geometric 144 / 90 / 54 | **Correct given the formula**, and the formula is correct as a *necessary* condition; the "if and only if" is false (item 2). |
| Book arithmetic: $\sum\sqrt{T_i+1/12}=31.4522$, $\sum\tau^*_i=54.1667$, $\sqrt{\cdot}=7.3598$, ratio 4.2735, aggregate $3.13688\times10^8$, R31,369 per bp, and all six entries of Table 7.3 | **All correct to the digits printed.** $\vartheta_iq_i=10^8\times0.0997357\sqrt{\tau^*_i}$ is also the correct vega with respect to clock volatility under the chapter's own quoting convention. |
| Per-caplet scaling R4,100 / R65,800 from R20,550 | **Arithmetically correct, financially wrong at the upper end** (item 14): at $\eta=64$ bp against $a=65.73$ bp the lower extreme model has $\alpha_0=1.73$ bp and the Hagan bracket diverges, so linearity fails exactly where the number is quoted. |
| "Eighteen months $\Rightarrow N\approx360$" at 250 business days a year | **No.** $250\times1.5=375$ (item 18). |

---

## 2. Re-check of previous round

Not applicable: this is round 1.

---

## 3. Numbered items, hardest first

### 1. [ADD] The unblocked marginal route is not considered, and it defeats the chapter's headline claim — must

**Location.** §7.3 "Feasibility: is there an admissible block length?" (`sec:zar-feasibility`), especially the verdict subsection and Remark "What is not a repair" (`rem:zar-notrepair`); also the chapter abstract and §7.9.1.

**What exactly.** Remark `rem:zar-notrepair` lists three repairs and rejects each. It omits the one an examiner will raise first: the unblocked, gap-free marginal bound of Barber and Pananjady (2026), Corollary 1 for a pretrained score,
$$\Prob\{\text{cover}\}\ \ge\ 1-\alpha-\min_{\tau}\Big\{\frac{\tau+L}{n-L+1}+2\beta(\tau)\Big\},$$
which applies verbatim to this chapter's setting (policy fixed on $\Dfit$ before cessation, stationary $\beta$-mixing state process, $L=0$). Add a fourth paragraph to `rem:zar-notrepair` and a three-row table to §7.3.3 evaluating it on this record. The numbers, computed here and reproducible in one line:

| Class | $N=18$: min deficit ($\tau$) | level | $N=24$: min deficit ($\tau$) | level |
|---|---|---|---|---|
| $\Bclass{2}(1)$ | 0.336 ($\tau=4$) | 0.564 | 0.280 ($\tau=5$) | **0.620** |
| $\Bclass{1.5}(1)$ | 0.442 ($\tau=5$) | 0.458 | 0.376 ($\tau=6$) | 0.524 |
| geometric $\varphi=0.3$ | 0.212 ($\tau=3$) | 0.688 | 0.174 ($\tau=3$) | 0.726 |

Then state plainly what the blocked route buys that this does not: the exact $\Beta(k,n+1-k)$ law and hence the calibration-conditional statement of Theorem `thm:cov`(ii), the drift term $\dK(P,Q)$ evaluated on a fixed half-line (Barber and Pananjady assume stationarity across the whole sequence and have no drift accounting, and their paper contains no calibration-conditional result at all — see `References/Highlights/barber2026.md`, closing note), and the fixed-policy accounting. Rewrite the verdict as: *no admissible block length exists for the blocked certificate on a monthly record, and the marginal guarantee that survives without blocking costs the calibration-conditional payoff that motivated blocking in the first place.*

**Why.** GROUND-TRUTH correction 12 ("Cite Barber and Pananjady (2026) ... wherever Theorem 9 or Theorem 6(i) is discussed") and LESSONS `[2026-09-09][scout-literature][ch3]` and `[2026-09-09][reviewer-conformal][ch3,ch1,ch8]`. The chapter discusses the Theorem 6(i) coupling deficit on every page of §7.3 and never cites them. As written, the sentence "at that block length the certificate is vacuous under every mixing class the chapter is willing to assume" (chapter abstract) and "the certified quantile is unavailable" (§7.9.1) are false: under $\Bclass{2}(1)$, the class the chapter itself uses as its base case, a marginal certificate at level 0.62 is available on the same twenty-four scores. A negative result that a reader can overturn with one published corollary is the most damaging thing a coda can contain.

**Locator for the citation.** `\citep[Cor.~1, eq.~(6)]{barber2026}` for the pretrained-score form and `\citep[Cor.~2]{barber2026}` for the trained-score form; both verified in `References/Highlights/barber2026.md` (arXiv v2, pp. 9 and 12). `barber2026` is already in `bibliography.tex`.

---

### 2. [PROVE] Proposition 7.1(iii) is false as an equivalence — must (a minimal correction has been applied; the writer must complete it)

**Location.** §7.3.1, Proposition `prop:zar-feasible`(iii) and its proof; consequences in §7.3.4 and §7.8.

**What exactly.** The proof asserted "the pair is feasible exactly when it is feasible at the smallest admissible number of blocks, $n=m$". That is wrong: $n=\lfloor N/(2b)\rfloor$ is determined by $N$ and $b$, not chosen, and at the largest admissible $b$ it may still exceed $m$. Counterexample at the chapter's own parameters ($\alpha=0.1$, $m=9$, $C=1$, $r=2$, $\gamma=0.4$, so $b_\gamma=5$ and $N_{\min}=90$): $N=90$ admits $b=5$ with $n=9$ and deficit $10/25=0.40\le\gamma$; $N=100$ admits nothing, because the ceiling gives $b\le5$ and $b=5$ then yields $n=10$ and deficit $11/25=0.44>\gamma$. Feasibility is therefore **not monotone in $N$**. Necessity is fine and is what the rest of the chapter actually uses.

**Edit already made** (listed under §6 below): the statement now claims only necessity plus attainment at $N=N_{\min}$; the proof is replaced by the correct three-line argument; and a `\gap{}` box records the counterexample and the unproved sufficient condition $N\ge2(m+1)\max\{m,b_\gamma\}$.

**What the writer must still do.** Either prove the sufficient condition and replace the `\gap{}` with it (it is elementary: for $N\ge m(2m+2)$ the interval $(N/(2m+2),\,N/(2m)]$ contains an integer, and that integer $b$ gives $n=m$ exactly; combine with $b\ge b_\gamma$), or keep the gap and soften §7.3.4's opening sentence "Proposition~\ref{prop:zar-feasible}(iii) answers the first half exactly", which now overstates what part (iii) delivers.

**Why.** STANDARD: every theorem carries a proof or a proof route plus a `\gap{}`. An "if and only if" with a two-line counterexample inside the chapter's own parameter set is the kind of thing an external examiner checks first in a chapter whose only new result is a counting proposition.

---

### 3. [FIX] The record count does not say whether the deployment block is inside $N$, and on the strict reading the $N=18$ row of Table 7.1 is wrong — must

**Location.** §7.3.2 "The arithmetic at the lengths this market affords"; Table `tab:zar-feasible`; §7.3.3.

**What exactly.** Chapter 3 fixes the accounting: "the record of $N$ periods after the fitting sample holds $n=\lfloor N/(2b)\rfloor$ blocks", the trailing gap is *inside* $N$, and "the deployment block $H_0$ is the block of $b$ periods that begins immediately after the record" (ch3, `fig:blocks` caption and Example, where $250+240+10=500$ exactly). Chapter 7 says the record "runs from January 2027 to the last date before submission, which is about eighteen monthly periods" — that is the whole post-cessation record, from which the deployment month must still be taken. Add one sentence fixing the convention, and correct the table accordingly. On the strict reading:

- eighteen post-cessation months $\Rightarrow N_{\mathrm{cal}}=17$, $b=1$, $n=8<m=9$, so $k=9>n$ and **$\hat q=+\infty$ at every block length** — the $N=18$, $b=1$ row of Table 7.1 currently reads "feasible threshold" and must read infeasible;
- twenty-four months $\Rightarrow N_{\mathrm{cal}}=23$, $b=1$, $n=11$, $k=\lceil0.9\times12\rceil=11=n$, $k/(n+1)=0.917$, coupling $12\beta(1)$ — so the headline figure is twelve, not thirteen.

If instead the chapter intends $N$ to be the calibration record with deployment months beyond it, say so in one clause and state that the institution must therefore hold $N+1$ months.

**Why.** Single-source rule: the counting convention has its home in Chapter 3 and Chapter 7 inherits it, so it must be inherited exactly. The strict-reading result strengthens the chapter's case — at eighteen months there is no threshold at all — and losing it to an ambiguity is a waste.

---

### 4. [FIX] The headline number rests on a pooling the chapter itself declares inadmissible — must

**Location.** §7.3.2 (the "generous reading") against Remark `rem:zar-notrepair` (§7.7); also the chapter abstract.

**What exactly.** §7.3.2 defines the generous count of twenty-four as one that "treats the pre-cessation months as scores of the same policy applied to the same positions". Remark `rem:zar-notrepair` then rejects exactly that operation: "Pooling the converted book's scores with the pre-cessation record changes the underlying of the book in the middle of the sample, so the calibration blocks would not have a common law and Assumption~\ref{ass:mix} would fail at its first clause." Both cannot stand. Resolve by making the strict count the chapter's primary case throughout — abstract, §7.3.3 verdict, Table 7.2 caption, §7.9.1 — and demoting the generous count to a sensitivity row labelled "admissible only if the pre-cessation and post-cessation block laws are taken to be common, which Remark~\ref{rem:zar-notrepair} argues they are not".

**Why.** Assumption `ass:mix` (ch3, first clause) requires the calibration blocks to have a common law; the conversion changes the underlying of every caplet on one date by contractual fact, which the chapter states in §7.2.1 as its opening premise. Presenting "thirteen times a one-month mixing coefficient" in the chapter abstract — the single number a reader takes away — on a count the chapter later forbids is an honesty failure, not a rounding choice.

---

### 5. [CLARIFY] Monthly rebalancing is asserted, not justified, and it is the sole cause of the negative finding — must

**Location.** §7.3.2, first paragraph: "Rebalancing is monthly, because that is the frequency at which the policy's volatility input can be refreshed in a market with no screen (Section~\ref{sec:zar-book})."

**What exactly.** Replace with a justified statement, roughly 150 words, and carry the qualification into the abstract and §7.9.1. The reason given does not survive the chapter's own §7.2.2: in the public regime the policy "degrades to a historical-volatility policy", and a historical-volatility input is computable from daily public ZARONIA fixings every business day; in the sponsor regime the desk marks and rebalances daily, which is precisely what §7.8 item 1 then asks the sponsor to record. Chapter 6 rebalances daily on an equivalent book. So either (a) give the real reason — for example that a converted ZAR book cannot be delta- and vega-rebalanced daily at acceptable cost in a market with no screen quotes, with a citation or a `\datanote{}` — or (b) state explicitly that monthly scoring is a design choice of this chapter, that the infeasibility verdict is conditional on it, and that the chapter's own §7.3.4 shows the same book scored daily is feasible within thirteen months.

**Why.** The chapter's principal finding is "no admissible block length exists". The arithmetic shows that this is a property of the *scoring frequency* and not of the market: at 270 daily periods the deficit is 0.044. A finding that dissolves under a design choice the chapter made in one unsupported clause, and then recommends reversing in §7.8, cannot be presented as a finding about the South African transition. State it as a finding about monthly records and the chapter is both true and interesting.

---

### 6. [CUT-REPETITION] Chapter 6's feasibility arithmetic and Chapter 5's book corollary are restated, not referenced — must

**Location.** §7.1 (`sec:zar-question`), second paragraph; §7.3.2, final paragraph ("This is the South African analogue of the figure of about 126"); §7.3.2, the $k/(n+1)$ sentence; §7.4.1 (`sec:zar-value`), first paragraph; §7.5.1 (`sec:zar-width`), first paragraph; Remark `rem:zar-longshort`.

**What exactly, passage by passage.**

- §7.1 ¶2, beginning "Chapter~\ref{ch:usd} carried out that evaluation for a calendar year of daily observations." Three sentences reproduce ch6 lines 269 and 291 in substance and in every number ($N\approx250$, $b\le13$, $b^*\approx17.8$ at $r=2$, coupling $\approx126$). Cut to one sentence: "Chapter~\ref{ch:usd} finds that a calendar year of daily observations already cannot carry the block length the bound prefers, and that the coupling term at the shortest block length is about $126$." Saves ~120 words.
- §7.3.2 final paragraph, "This is the South African analogue of the figure of about $126$ that Chapter~\ref{ch:usd} records at its own shortest block length" — a second statement of the same ch6 number. Delete the clause.
- §7.3.2, "The realised nominal level is $k/(n+1)=0.923$ rather than $0.900$, a finite-$n$ effect of the ceiling in $k$ that must be reported beside the nominal level whenever $n$ is this small." Chapter 6 line 271 already states the rule. Keep the values, delete the rule. Saves ~25 words.
- §7.5.1 ¶1, beginning "Corollary~\ref{cor:ident-book} gives the book-level width. With one basis vector shared across expiries..." This restates the corollary in full, both the net and the per-expiry forms. The single-source rule permits one sentence of reminder: "By Corollary~\ref{cor:ident-book} the identified half-width of a book is $\eta|\sum_i\vartheta_iq_ic^*_i|$ under shared basis parameters and $\eta\sum_i|\vartheta_i|q_ic^*_i$ under per-expiry ones." Saves ~100 words.
- Remark `rem:zar-longshort` is a near-paraphrase of the remark following `cor:ident-book` in Chapter 5 (ch5 line 568: "A book long some expiries and short others is partially immunised, and by exactly the amount the shared-parameter assumption dictates... under the per-expiry variant the worst case is $\eta\sum_i|\vartheta_i|q_ic^*_i$ and a long-short book is not immunised at all"). Cut the remark to the two sentences that are genuinely South African — that the shared-basis assumption cannot be tested here because criterion V6 needs a quoted successor surface across expiries, and that the public regime must therefore take the absolute form. Saves ~100 words.
- §7.4.1 ¶1 restates Theorems 3 and 4 of Chapter 5 at paragraph length. Reduce to two sentences with references. Saves ~80 words.

**Why.** STANDARD, single-source rule (binding): "Any other chapter that needs it writes at most one sentence of reminder and a reference... No restated theorem environments, no re-proofs, no re-derivations." LESSONS `[2026-09-09][orchestrator][all]` ("Say it once") makes `[CUT-REPETITION]` items must-priority by construction.

---

### 7. [REMOVE] The chapter is about seven pages over its twenty-page budget — must

**Location.** Whole chapter.

**What exactly.** 8,031 source words after stripping comments and control sequences, which at the page-budget auditor's calibrated 300 words per typeset page for prose-heavy chapters is about 26.8 pages, plus two `\figplan{}` boxes, three tables and two `\datanote{}` boxes. Budget is 20. Cut approximately 2,000 source words. Item 6 supplies about 425 of them. The rest should come from: §7.7 `sec:zar-models`, which spends four paragraphs on a comparison it concludes cannot be made quantitatively (compress to two, keeping the second paragraph, which is the sharp one); §7.8 `sec:zar-sponsor` items 1 and 4, which restate §7.3.4 and §7.4.2 respectively (compress each to three sentences, referencing rather than repeating); §7.9.3 "The same chapter in 2029", whose second paragraph duplicates §7.4.2's identification argument.

**Why.** STANDARD page budget: Ch7 = 20 pages. The chapter is a coda by the examiner's own ruling (LESSONS `[2026-09-09][examiner][all]`: "ZAR is a coda"), and a coda that runs a third longer than budget while the chapters carrying the doctoral theorems are at budget inverts the weight of the thesis.

---

### 8. [ADD] The converted book is not the whole book: legacy trades that do not fall back — must

**Location.** §7.2.1 "What converts, and into what", after "The linear book converts mechanically."

**What exactly.** Add two to three sentences, roughly 90 words. Not every JIBAR trade falls back to compounded ZARONIA plus a spread. Trades on the 2006 Definitions without the April 2025 Benchmark Module fall to Reference Rate quotations and then to Calculation Agent determination — a dealer poll, not a converted option: "As JIBAR will not appear on the relevant screen after December 31, 2026, for the purposes of the Rate Option detailed above, the fallback to Reference Rate quotations, and the further fallback to Calculation Agent determination, will apply" `\citep[Sect.~5]{isda2025}`. Neither the 2020 IBOR Fallbacks Protocol nor Supplement 70 to the 2006 Definitions covers JIBAR `\citep[Sect.~8]{isda2025}`. State the consequence for this chapter: the score record and the vega schedule of §7.8 item 2 are of the *converted* sub-book, and an institution must be able to separate it from the polled residue, which is an additional data requirement.

**Why.** Zero-hallucination rule and completeness. The librarian's note for this source flags exactly this point as a Chapter 7 caveat (`References/Highlights/isda2025.md`, row for §5, "the converted book is not the whole book (ch7 caveat)"), and the chapter currently asserts a universality the primary source contradicts. Both locators are verified and the key is in `bibliography.tex`.

---

### 9. [FIX] Assumption A5 ($c^*_i=1$) is quantified only at the one-year expiry, where it is smallest, and the net sign is not given — must

**Location.** §7.5.2, assumption A5.

**What exactly.** A5 says setting $c^*_i=1$ "understates the width by about one per cent there", quoting the one-year value $c^*=1.009$. But $c^*=1+\tfrac1{24}(2-3\rho^2)\nu^2\tau^*$ grows linearly in $\tau^*$: at the worked parameters of Chapter 5 ($\nu=0.4$, $\rho=-0.2$) it is 1.0136 at $\tau^*=1.083$ and 1.0637 at the five-year expiry, so across the twenty expiries the book aggregate $\sum\sqrt{\tau^*_i}\,c^*_i$ is 32.693 against the 31.452 that A5 uses — an understatement of **3.9 per cent for the book**, not one per cent. Replace the sentence with the book figure and the range of $c^*_i$ across the expiry ladder. Separately, state the *net* effect of the two opposite-sign errors rather than leaving the reader to infer cancellation: at the one-year expiry, $\eta q=18.619$ bp against the exact quoted half-width of $18.429$ bp, so the A5 convention **overstates** by 1.0 per cent there, while at the long end it understates by about 5 per cent.

**Why.** The chapter's declared standard is "the arithmetic that follows from them is exact and is shown". An assumption whose error is stated at the one point where it is smallest, in a book whose weights grow with $\sqrt{\tau^*}$, is a selective disclosure, and the examiner will recompute. (All figures above recomputed from the Chapter 5 worked parameters.)

---

### 10. [ADD] No discounting: the rand figures are undiscounted forward premia — must

**Location.** §7.5.2, assumption list (add A7) and equation `eq:zar-bookwidth`; §7.4.3.

**What exactly.** Add one assumption, roughly 60 words: the Bachelier expression $0.39894\,\sigma\sqrt{t}$ is a forward premium, so every rand figure in §7.4.3, §7.5.2 and Table 7.3 assumes $P(0,T_i+\Delta)=1$. State the size of the omission: at a flat 8 per cent continuously compounded ZAR discount rate the discount-weighted aggregate $\sum\sqrt{\tau^*_i}\,P(0,T_i+\Delta)$ is 24.268 against 31.452, so the reported book half-width is about **23 per cent high**. Either apply the discount factors (they are public, from the curve §7.2.2 already lists as a required pull) or declare the convention beside the headline number R31,369 per basis point.

**Why.** Practitioner and regulatory perspectives: a reserve is a present value, and a 23 per cent overstatement on a five-year ZAR ladder at South African rate levels is not a rounding convention. Chapter 5's worked example can leave discounting aside because it prices one caplet as an illustration of a half-width in volatility units; Chapter 7 reports a book reserve in rand, which a risk system will compare with its own discounted number.

---

### 11. [CLARIFY] Equation `eq:zar-reserve` adds a mark to two reserves and does not address double counting — must

**Location.** §7.6 `sec:zar-residual`, equation `eq:zar-reserve` and the paragraph beginning "where $V_\pi$ is the value the fixed policy reports".

**What exactly.** Two things must be said in about 120 words. First, whether $\mathcal R$ is a total carrying amount ($V_\pi$ plus two add-ons) or a reserve (the two add-ons alone); as written the symbol is called "the reserve" while the display includes the mark, and a risk reader will take the second and third terms as the reserve. Second, why terms two and three do not double count. The hedging-error score of Chapter 3 is measured against the *fixed policy* $\pi$, whose mark is itself somewhere inside the identified set; a policy mismarked by up to $\eta|\sum_i\vartheta_iq_ic^*_i|$ generates hedging errors that already contain part of that mismarking, so the sum is conservative but not obviously additive in the way the sentence "The three terms answer different questions and are not substitutes" asserts. Either argue the separation (the identification width is a static, measure-side quantity fixed at the reserve date while the score is a realised profit and loss over one rebalancing block, so the overlap is second order) or record it as a `\gap{}`.

**Why.** STANDARD: definitions before use, and every assertion either proved or gapped. This equation is the chapter's own contribution to the thesis's reserve construction — it is the object §7.6, §7.7 and §7.9 all refer back to — and it is the one place where the identifiability half and the certification half of the thesis are combined into a single number. An examiner will ask whether the two halves are additive, and the chapter currently answers by assertion.

---

### 12. [ADD] The book reserve covers only the at-the-money coordinate; the skew coordinate is dropped without a word — should

**Location.** §7.5.1 and equation `eq:zar-reserve`.

**What exactly.** Add a short paragraph, about 120 words. Chapter 5 identifies a *two-dimensional* deficit: the at-the-money level within $\eta qc^*$ and the skew within $\eta qc^*\nu/(2\alpha_0)$ per unit of strike, with the identified region an ellipse in the level–skew plane (Theorem `thm:ident-two`, Proposition `prop:ident-consistent`). Corollary `cor:ident-book` and therefore §7.5 aggregate only the first. A converted book with risk reversals and collars — which a South African cap-and-collar book has by construction — carries skew exposure whose identified width is not in `eq:zar-bookwidth`. State either the analogous aggregate $\eta\,qc^*\nu/(2\alpha_0)\sum_i|\varsigma_i|$ over a skew-vega schedule $\varsigma_i$, or state explicitly that the chapter's reserve is a lower bound on the identified width for any book that is not purely at-the-money vega.

**Why.** Identifiability perspective. The chapter's own §7.4.1 says "the skew is identified at first order within a half-width $qc^*\nu\eta/(2\alpha_0)$ per unit of strike" and then never uses it. A reserve presented as *the* width of the consistent set, which covers one of the two unidentified coordinates, understates by an amount the chapter has the machinery to bound.

---

### 13. [ADD] Assumption A3 (every caplet at the money) is the least defensible assumption in the book and maximises the answer — should

**Location.** §7.5.2, assumption A3; Remark `rem:zar-longshort`.

**What exactly.** Add two sentences (~70 words). A converted book is struck at the strikes of the old JIBAR contracts; after conversion the underlying moves by the fallback spread $s=16.19$ bp plus the forward basis $B_0$, so the book is systematically off the money by a known, contractual amount on the conversion date. Since the reserve scales with $|\vartheta_i|$ and Bachelier vega falls away from the money, A3 makes the representative book the maximal-vega case. Say so, and say by roughly how much a 20 bp moneyness shift moves the aggregate at the short expiries.

**Why.** Practitioner and benchmark-reform perspectives. The whole point of the chapter is that conversion is "not a modelling choice but a contractual fact" (§7.2.1); the most direct consequence of that fact for a vega-weighted reserve is a deterministic shift in moneyness, and the chapter assumes it away in one line without noting the direction of the resulting error.

---

### 14. [FIX] "It is linear in $\eta$" fails at the upper end of the bracket, where the chapter quotes it — should

**Location.** §7.4.3, the paragraph "It is linear in $\eta$."

**What exactly.** Qualify the R65,800 figure. Chapter 5 gives the exact quoted half-width as $\tfrac12(\Sigma^+-\Sigma^-)$ with $\alpha_0^\pm=a\mp\eta$ and $\nu^\pm=na/(a\mp\eta)$; at the worked fit $a=65.73$ bp, so at $\eta=64$ bp the lower extreme model has $\alpha_0^+=1.73$ bp and $\nu^+$ roughly forty times the fitted value, and the Hagan bracket $c^{*+}$ diverges. The exactly identified statement that *is* linear in $\eta$ is the interval for the diffusion coefficient at the clock, $[a-\eta,a+\eta]$, half-width exactly $\eta$ (Theorem `thm:ident-two`(i)); the *quoted* half-width is not. Say that the upper end of the bracket is quoted as a linear extrapolation, that it corresponds to $\varepsilon\approx1.07$ where the expansion underlying the corollary has no claim to accuracy, and that the honest reading of the upper end is "the identification failure is of the same order as the volatility itself" rather than a rand figure to three significant digits.

**Why.** SABR and forward-measures perspectives. Chapter 5's own data note records $\varepsilon\approx1.07$ at $\eta=64$ bp; §7.9.2 acknowledges the first-order caveat in one clause in the limitations, but the number R65,800 and the entry R2,007,605 in Table 7.3 are presented without it, and those are the figures a reader quotes.

---

### 15. [CITE] "The one published dynamic study of the South African spread" is never cited in this chapter — should

**Location.** §7.4.2 ¶1 and Remark `rem:zar-eta`.

**What exactly.** Add `\citep{alfeus2026}` (in `bibliography.tex`; SARB Working Paper WP/26/06). Locators verified in Chapter 5's data note: `\citep[Sec.~3, p.~5 and Sec.~5.1, Table~4]{alfeus2026}`. Keep the derivation itself in Chapter 5 (single source) but name the source here, because the sentence is a claim about the literature, not a cross-reference.

**Why.** Zero-hallucination rule: "Every definition adapted from the literature names its source." A claim of the form "the one published study" is a literature claim and the strongest form of it, since it asserts absence as well as presence.

---

### 16. [CITE] The clearing-house `\gap{}` can be closed: the sources are on file — should

**Location.** §7.2.1, the `\gap{Citation needed: the clearing house's conversion...}` box.

**What exactly.** The two facts are verified and recorded in LESSONS `[2026-09-09][scout][ch1,ch7]`: ZAR discounting and PAI/PAA switch to ZARONIA on Saturday 11 April 2026 (LCH member update, 17 December 2025, https://www.lseg.com/en/post-trade/clearing/membership/ltd-membership/ltd-member-updates/zar-pai-paa-and-discounting-transition), and conversion of outstanding cleared ZAR JIBAR SwapClear contracts on Saturday 21 November 2026, dress rehearsal 10 October 2026, contingency 5 December 2026 (LCH member update, 26 February 2026, https://www.lseg.com/en/post-trade/clearing/membership/ltd-membership/ltd-member-updates/lch-conversion-of-outstanding-cleared-zar-jibar-swapclear-contracts). There is no `lch` key in `bibliography.tex`, so the item goes to the bibliography verifier: add two `\bibitem`s with issuer, title, date, URL and access date, then replace the gap box with `\citep{}` and a single sentence. If the verifier cannot confirm them, the gap stays as written.

**Why.** The zero-hallucination rule is satisfied either way, but a gap box that could be closed from the project's own verified scout record costs the chapter a fact it needs — the date from which a converted book exists in cleared form bounds the start of the score record, which is the quantity items 3 and 4 turn on.

---

### 17. [CITE] The rand figures depend on a collateral convention the chapter never names — should

**Location.** §7.2.2 (the two regimes) and §7.5.2 (the assumption list).

**What exactly.** Add one sentence with the verified locator: inter-dealer implied volatilities for ZARONIA non-linear products are quoted under an assumed USD-denominated zero-threshold CSA with SOFR collateral — "the various implied volatilities indicated on the inter-dealer broker screens make the underlying assumption of an underlying USD-denominated CSA" `\citep[\S8.2, p.~27]{sarb2024conv}` — while the cleared book's discounting and price alignment move to ZARONIA in April 2026 (item 16). A sponsor surface and a cleared reserve are therefore not on the same discounting basis, and the chapter should say which basis the rand figures assume.

**Why.** Forward-measures perspective. Everything in this thesis is priced under $\Q^{T+\Delta}$ with $P(\cdot,T+\Delta)$ as numéraire; which curve that is under a USD CSA against a ZARONIA CSA is a real difference for a five-year ZAR book, and the chapter asks a sponsor for surfaces in §7.8 item 3 without saying under which convention they must be marked.

---

### 18. [FIX] Eighteen months at 250 business days a year is 375 periods, not 360 — should

**Location.** §7.3.4 ¶3 and §7.8 item 1 (the same sentence appears twice; see item 6).

**What exactly.** Either change 360 to 375 and the deficit from $10/400=0.025$ to $b=20$ with $n=\lfloor375/40\rfloor=9$, deficit $10/400=0.025$ (which is unchanged, since $b=20$ remains admissible at $375$ and still gives $n=9$), or change "after eighteen months" to "after about seventeen months". The arithmetic conclusion survives; the stated correspondence between months and periods does not.

**Why.** The chapter sets its own convention in the same sentence ("at $250$ business days to the year") and then contradicts it. Small, but it sits in the one paragraph that carries the chapter's operational recommendation.

---

### 19. [FIX] The chapter abstract exceeds the prescribed length — should

**Location.** The opening `\begin{quote}\itshape` block.

**What exactly.** It is a single paragraph of about 250 words, which will typeset well beyond eight lines. Cut to 5–8 lines: what the chapter establishes (the feasibility verdict, correctly qualified per items 1, 4 and 5) and what it leaves open (the certified residual, and the basis volatility). The sentence "No number in this chapter is reported as computed from data; every figure that carries a currency unit follows from assumptions declared beside it" should survive the cut — it is the best sentence in the chapter.

**Why.** STANDARD chapter template: "Chapter abstract (5–8 lines, italic)".

---

### 20. [CLARIFY] "Half the nominal level" is not 0.5 — should

**Location.** §7.3.2, "To leave at least half the nominal level -- criterion C2 of Chapter~\ref{ch:usd}, a certified level of $0.5$".

**What exactly.** The nominal level is 0.9; half of it is 0.45. Criterion C2 of Chapter 6 is a certified level of at least 0.5 in absolute terms. Delete "half the nominal level" and write "a certified level of one half, criterion C2 of Chapter~\ref{ch:usd}".

**Why.** The sentence introduces the numerical budget $\gamma=0.4$ that the whole of §7.3.4 and Table 7.2 then use; a reader who takes "half the nominal level" literally computes $\gamma=0.45$ and cannot reproduce the table.

---

### 21. [CITE] The regulatory claims are asserted, and the South African prudential frame is absent — should

**Location.** §7.3.3, "A reserve held at a stated level of two-thirds is not a reserve at the level a bank or its supervisor works to"; §7.7 ¶1, "hold it as an \gls{ava} for model uncertainty".

**What exactly.** Two fixes, roughly 100 words in total. First, either cite a prudential source for the level a supervisor works to, or rewrite as a statement about the thesis's own criterion ("below the level the chapter fixed in criterion C2 of Chapter~\ref{ch:usd}"), which is defensible without a source. Second, "additional valuation adjustment" is a European term of art from the prudent-valuation regime; either cite it, or write "a valuation adjustment for model uncertainty" and add one sentence saying what, if anything, the South African prudential framework requires — and if the scouts have found nothing, say "no South African prudential requirement specific to valuation uncertainty on converted benchmark books was found as of \<date\>", in the form LESSONS `[2026-09-09][scout][ch1,ch5,ch7]` prescribes for dated absences.

**Why.** Zero-hallucination rule: "Every market fact, date, spread value, convention or regulatory statement carries a citation to a primary source in References.bib, or a `\datanote{}` saying it is unverified." This is the chapter with "South African" in its title, and it currently contains no South African regulatory source at all beyond the two benchmark-transition documents.

---

### 22. [CITE] The cessation date carries the wrong locator — should

**Location.** §7.2.1, first sentence.

**What exactly.** "JIBAR ceases permanently immediately after its final publication on 31~December 2026, and an Index Cessation Event occurred on 3~December 2025 ... `\citep[Sect.~1.1]{isda2025}`". Section 1.1 of that document supports the Index Cessation Event and the expected effective date of 4 January 2027; the cessation date itself is on p. 1 (preamble) and in §1. Split into `\citep[p.~1 and Sect.~1]{isda2025}` for the first clause and `\citep[Sect.~1.1]{isda2025}` for the second. Verified in `References/Highlights/isda2025.md`, rows for p. 1, §1 and §1.1.

**Why.** Zero-hallucination rule: the locator, not only the key, must be right. An examiner who opens §1.1 looking for "31 December 2026" finds only the expected first business day after it.

---

## 4. Missing for a strong doctoral chapter

Three absences stand out, and all three are within reach of what the thesis already proves. The first is the alternative route: the chapter proves a negative about the blocked certificate and never asks what a reader holding the same twenty-four scores could do instead, so the unblocked marginal bound that is already cited in Chapters 3 and 4 is neither evaluated nor ruled out, and with it goes the chapter's strongest possible statement — not "nothing can be certified on this record" but "a marginal statement survives and a calibration-conditional one does not, and here is exactly what that trade costs" (item 1). The second is the South African content proper: a chapter titled after the converted book should say which trades actually convert and which fall to a dealer poll (item 8), under which collateral and discounting convention a rand reserve is computed at a moment when the clearing house is itself moving that convention (items 16 and 17), what the contractual moneyness of a converted caplet is after a 16.19 bp spread is bolted onto its underlying (item 13), and what the South African prudential regime asks of a valuation reserve (item 21); at present the market-specific content is three citations and a spread value, and everything else would read identically for any IBOR. The third is the second identified coordinate: Chapter 5 hands this chapter a two-dimensional identified set and an ellipse, and Chapter 7 aggregates one of the two dimensions and reports the result as the width of the consistent set (item 12). Beyond those, the reserve equation that is the chapter's own synthesis of the thesis's two halves deserves a paragraph of justification rather than an assertion that its terms "are not substitutes" (item 11), and the representative book deserves one sensitivity row — a long-short book, or a book with a realistic expiry profile rather than a flat R100 million ladder — so that the factor 4.27 is shown to be a property of the aggregation rule and not of the particularly convenient book chosen to display it.

## 5. Should go

About 2,000 source words should come out, and almost all of the candidates are passages where the chapter explains something that has a home elsewhere. The re-derivations of Chapter 6's feasibility arithmetic in §7.1 and again in §7.3.2, of Chapter 6's finite-$n$ rule about $k/(n+1)$, of Corollary `cor:ident-book` in §7.5.1, and of Chapter 5's long-short remark in `rem:zar-longshort` are the clearest cases: each is a restatement where the single-source rule allows one sentence and a label (item 6). Section 7.7, on re-pricing across a handful of models, spends four paragraphs to arrive at the conclusion that no quantitative comparison can be made without the desk's model set; its second paragraph — that the usual model set sets both basis correlations to zero and therefore reports zero spread in precisely the unidentified directions — is the sharpest thing in the chapter and should be kept, and the other three compressed into one. Section 7.8 items 1 and 4 restate §7.3.4 and §7.4.2 respectively at nearly full length and should reference them instead. The second paragraph of §7.9.3 repeats the identification argument of §7.4.2 in the future tense. Finally, the chapter has a habit of announcing its own honesty — "That verdict is not a failure of execution and it is not repaired here", "It is reported, its exact cause is identified", "the honest conclusion is about records and designs, not about theorems", "what this chapter declines to pretend it has done" — which is admirable once and costly five times; keep the strongest instance, in Remark `rem:zar-whatfails`, and let the rest of the chapter simply be honest without saying so.

## 6. Direct edits made

One, for an outright mathematical error, as permitted:

- §7.3.1, Proposition `prop:zar-feasible`(iii) and its proof. The claim was an "if and only if"; the converse is false (counterexample at the chapter's own parameters: $\alpha=0.1$, $C=1$, $r=2$, $\gamma=0.4$ give $N_{\min}=90$, yet $N=100$ admits no block length). The statement now asserts necessity plus attainment at $N=N_{\min}$; the proof is replaced by the correct argument ($n\ge m\Rightarrow(m+1)Cb^{-r}\le\gamma\Rightarrow b\ge b_\gamma$, with $n=m$ exactly at $N=2mb_\gamma$); and a `\gap{}` box after the proof records the counterexample, states the unproved sufficient condition $N\ge2(m+1)\max\{m,b_\gamma\}$, and notes that the necessity direction is the one the rest of the chapter uses. No other text was touched.

## 7. Lessons enforced

- `[2026-09-09][orchestrator][all]` — Say it once; every object has one home chapter; `[CUT-REPETITION]` items are must-priority. (Items 6, 7.)
- STANDARD single-source rule (binding) — at most one sentence of reminder plus a reference; no restated theorem environments. (Item 6.)
- `[2026-09-09][examiner][all]` — ZAR is a coda, USD is the empirical spine. (Items 6, 7.)
- `[2026-09-09][scout-literature][ch3]` and `[2026-09-09][reviewer-conformal][ch3,ch1,ch8]` — Theorem 6(i) is dominated for marginal coverage by Barber and Pananjady (2026); cite them wherever it is discussed. GROUND-TRUTH correction 12. (Item 1.)
- `[2026-09-09][statistician][ch3]` / GROUND-TRUTH correction 4 — coupling cost $(n+1)\beta(b)$, gap-separated deployment block, Beta law not DKW. (Arithmetic verification; items 1, 3.)
- `[2026-09-09][review-panel][appC,ch7]` — with $n=\lfloor N/(2b)\rfloor$ a finite threshold needs $n\ge\lceil1/\alpha\rceil-1$; at $\alpha=0.1$ that is $N\ge18$ at $b=1$; state it before ch7 is drafted. (Items 2, 3.)
- `[2026-09-09][code-conformal][ch3,ch6]` — report $k/(n+1)$ alongside $1-\alpha$ whenever $n$ is small. (Chapter complies; item 6 only removes the restated rule, not the values.)
- `[2026-09-09][reviewer-conformal][ch3]` — nothing asymptotic inside a theorem statement; never cite the ground truth or its numbering inside a chapter. (Chapter complies.)
- `[2026-09-09][data-engineer-zar][appC,ch7]` — without a sponsor the policy is a historical-volatility policy and the reserve decomposition must be labelled accordingly. (Chapter complies; item 5 uses it against the monthly-rebalancing justification.)
- `[2026-09-09][data-engineer-zar][appC,ch5,ch7]` — never estimate $\eta$, $\rho_{BF}$ or $\rho_{B\alpha}$ from the SARB synthetic OIS curve. (Chapter complies, in `rem:zar-eta`.)
- `[2026-09-09][review-panel][appC]` — a data appendix records what exists; fitting windows, reporting rules and the certified policy are pre-registered in ch6/ch7. (Chapter complies: §7.2.2 and §7.8 hold the design, App C the datasets.)
- `[2026-09-09][review-panel][appC,all]` — secondary sources never carry a market fact without a `\datanote{}`; a writer who cannot find a source writes `\gap{Citation needed}`. (Items 8, 15, 16, 17, 21, 22.)
- `[2026-09-09][scout][ch1,ch5,ch7]` — state "no evidence found as of \<date\>", never proof of absence. (Chapter complies for screen quotes; item 21 extends it to the prudential question.)
- `[2026-09-09][reference-librarian][ch5,ch7,appC]` and `[ch1,ch7]` — use the verified `sarb2024conv` and `isda2025` locators. (Items 8, 17, 22.)
- `[2026-09-09][bibliography-verifier][all]` — every new `\bibitem` is web-verified before it is added. (Item 16, routed to the verifier.)
- `[2026-09-09][page-budget-auditor][all]` — count source words after stripping comments and control sequences, at 300 words per typeset page for prose-heavy chapters. (Item 7.)
- STANDARD chapter template — chapter abstract 5–8 lines italic. (Item 19.)
- STANDARD invisible apparatus — no mention of drafts, rounds or reviewers; disagreements resolved in the text. (Chapter complies.)
