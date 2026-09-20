---
geometry: a4paper, margin=2.2cm
fontsize: 11pt
header-includes: |
  \usepackage{graphicx}
  \usepackage{enumitem}
  \setlist{nosep, topsep=2pt, itemsep=1pt, parsep=0pt}
  \setlength{\parskip}{3pt}
  \usepackage{titlesec}
  \titlespacing*{\section}{0pt}{7pt}{3pt}
---

<!-- Cover page. Laid out after the UFS master's dissertation cover, with the
     Wits crest. Two versions follow: raw LaTeX for the PDF, and plain
     markdown for the .docx. Keep the wording of the two in step. -->

```{=latex}
\thispagestyle{empty}
\begin{center}
\vspace*{1.8cm}

{\Large\bfseries Pricing and Hedging through Benchmark Transitions\\[0.35em]
in the Absence of Liquid Option Markets\par}

\vspace{1.3cm}
by
\vspace{0.45cm}

Baloyi Thabang Bongani Junior

\vspace{0.3cm}
Student number 1113941

\vspace{1.3cm}
Concept note submitted in support of an application to register\\
for the degree

\vspace{0.9cm}
{\bfseries Doctor of Philosophy\par}
\vspace{0.2cm}
{\bfseries (Mathematical Statistics)\par}

\vspace{1.1cm}
in the School of Statistics and Actuarial Science\\
in the Faculty of Science\\
at the University of the Witwatersrand

\vspace{1.0cm}
\includegraphics[width=3.4cm]{../Thesis/Cover Page/src/witslogo.pdf}

\vspace{0.9cm}
Johannesburg, South Africa\\
September 2026

\vspace{0.8cm}
Supervisor: To be confirmed
\end{center}
\newpage
```

```{=openxml}
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="32"/></w:rPr><w:t>Pricing and Hedging through Benchmark Transitions in the Absence of Liquid Option Markets</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>by</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>Baloyi Thabang Bongani Junior</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>Student number 1113941</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>Concept note submitted in support of an application to register for the degree</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/></w:rPr><w:t>Doctor of Philosophy</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/></w:rPr><w:t>(Mathematical Statistics)</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>in the School of Statistics and Actuarial Science</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>in the Faculty of Science</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>at the University of the Witwatersrand</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>Johannesburg, South Africa</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>September 2026</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>Supervisor: To be confirmed</w:t></w:r></w:p>
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

**Status.** Concept note for supervisor discussion; academic home and supervision to be confirmed. The results, novelty claims and feasibility described here are proposed, not established. A supplied AI-assisted draft manuscript informed the research questions; it is not evidence that its results have been proved.

# The research problem

When an interest-rate benchmark is replaced, the contractual cashflows of existing derivatives change: a forward-looking term rate fixed at the start of an accrual period gives way to a rate compounded over that period from overnight fixings. This alters when the underlying is observed and how uncertainty accumulates, for contracts written before the replacement was contemplated.

The difficulty this project addresses is informational. A dealer may observe a reliable market in instruments referencing the legacy benchmark — curves, swaps, basis instruments and legacy options — while having little or no direct evidence about options referencing the successor rate. Those observations constrain some features of the transition; they need not determine the full distribution an option payoff depends on.

This matters because an option is sensitive to outcomes beyond an average rate. Two models can agree on forward values while assigning different probabilities to large rate moves, and a caplet distinguishes them. Importing a volatility parameter from the legacy market therefore produces a number without demonstrating that it follows uniquely from what was observed: a fitted model can return a single successor price even when the observations are compatible with several.

A second, separate question concerns trading. Valuation uncertainty is the range of model prices compatible with the observations; trading risk is the realised profit or loss from holding and hedging the liability. A closely calibrated model can still produce large losses when trading constraints or changing dynamics matter, and small average hedging error does not imply a valid statement about the upper tail.

The South African JIBAR–ZARONIA transition supplies the application, with South African Reserve Bank conventions determining the contractual implementation. The application will be dated precisely: any statement about illiquidity will refer to a particular instrument, tenor and observation period, supported by a data audit rather than assumed for the market as a whole.

# Central question and research questions

> Under what assumptions can legacy market information determine successor-rate option values, and what statistically defensible bounds can be placed on the losses from hedging those options during a benchmark transition?

- **RQ1.** Which successor valuation functionals are constant across the models compatible with legacy option quotes and curve or basis observations?
- **RQ2.** Which additional observations or restrictions restore identification, and how stable is that conclusion to quote noise?
- **RQ3.** Under what dependence and distribution-shift assumptions can a calibrated loss threshold retain a finite-sample guarantee?
- **RQ4.** Are the resulting price ranges and risk bounds informative for a realistic hedge, once costs and data limitations are included?

# Aim and objectives

**Aim.** To develop and evaluate a framework for identifying successor-rate option valuations and quantifying residual hedging risk under limited option-market information.

1. Specify a coherent transition model, contractual conventions and observable market information, keeping risk-neutral pricing assumptions separate from historical estimation.
2. Prove identification or non-identification results for a restricted model class, and determine the resulting valuation ranges or approximation errors.
3. Construct implementable hedges from available instruments and investigate finite-sample loss guarantees under explicit assumptions.
4. Evaluate pricing uncertainty, hedge performance and certificate informativeness in simulation and in an appropriately limited empirical application.

# Scope and delimitations

The initial product scope is caplets, with compounding, observation shift and payment conventions stated explicitly rather than assumed from a similar-looking formula. The initial model scope is a small factor system; the initial hedge set is liquid swaps and cash instruments, restricted to instruments the data audit shows were tradeable on the relevant date. A successor option will not be used as a hedging instrument merely because it would complete the market.

Swaptions, large portfolios, jump extensions, multi-tenor consistency, learned hedging policies and rough-path methods are treated as extensions, each requiring a specific reason connected to a stated research question. They are not compulsory components, and adding them all would increase the number of quantities requiring identification without sharpening the central question. The collateral and funding structure will be simplified, with that simplification stated; funding asymmetries, counterparty effects and multiple collateral currencies are excluded unless the central question demands them.

The application is the South African JIBAR–ZARONIA transition. A retrospective study in a currency where successor options did trade is a candidate for validation, subject to licensed and comparable data, and its findings will not be assumed to transfer across currencies. The extent of the empirical programme depends on data access: what cannot be supported by observations actually obtained will be reported as unsupported rather than asserted.

# Positioning and the provisional gap

Brigo and Mercurio (2006) supply the pricing architecture; Lyashenko and Mercurio (2019) develop a forward-market treatment of backward-looking rates; Willems (2020) studies SABR smiles for risk-free-rate caplets. These inform the modelling framework. They do not by themselves establish that successor smiles are identified from a chosen set of legacy observations.

Local work provides method and context: Konaite (2024) on the forward market model, Menziwa (2023) on pricing, calibration and hedging under the LIBOR model, Robbertze (2021) on neural-network volatility modelling and Stangroom (2023) on deep hedging. Mavuso (2014) studies mean–variance hedging where a liquid asset is traded dynamically and an illiquid asset is held statically, which is a natural way to make trading permissions part of the mathematics. Feng et al. (2018) separate calibration from recalibration model risk. Alfeus (2026) models JIBAR–ZARONIA spread dynamics around scheduled events; that is historical spread modelling, and is distinct from identifying a risk-neutral option valuation.

The statistical component builds on conformal prediction rather than proposing a new general coverage principle. Vovk (2012) addresses conditional validity, Barber et al. (2023) treat departures from exchangeability, Oliveira et al. (2024) analyse split conformal prediction for non-exchangeable data, and Barber and Pananjady (2026) and Ramos et al. (2026) are closest to the dependence and calibration-conditional questions at issue.

The provisional gap is the connection between a rigorously characterised set of transition models and a finite-sample analysis of the hedging losses those models imply, under stated dependence and distributional change. It is provisional by design: the first phase of the work is a structured comparison — observation sets, model classes, trading constraints, guarantee types, proof assumptions — written in common notation. If the candidate results reduce to existing theorems, the contribution will be narrowed or reformulated rather than restated in weaker language until it becomes unfalsifiable.

# Proposed approach

**Model and observations.** The work begins with a low-dimensional Markov model containing an overnight-rate factor and a spread factor, with a stated correlation, under an explicit pricing measure. A two-factor Gaussian diffusion is the initial analytical laboratory: it admits explicit covariance calculations and tractable simulation, and its limitations, including the possibility of negative rates, will be recorded rather than concealed. The observation map from model to traded instrument prices will be specified so that it prices actual cashflows before any identification claim is made.

**Identification.** Let $O$ denote the observations available at a valuation date and $\Lambda(\theta)$ the model-implied observation vector. The compatible set is $\Theta(O) = \{\theta \in \Theta : \Lambda(\theta) \text{ is compatible with } O\}$, with compatibility defined by quote tolerances, preferably observed bid–ask ranges. A target valuation is identified if it is constant on $\Theta(O)$; otherwise the attainable range runs between $V_{-} = \inf_{\theta \in \Theta(O)} V_{\theta}$ and $V_{+} = \sup_{\theta \in \Theta(O)} V_{\theta}$. These are identification ranges, not confidence intervals. The first attempts will be constructive non-identification examples: two admissible models sharing the full observation map but disagreeing on the target. An identification proof, conversely, must establish constancy across the entire compatible set. Parameter counting and a good numerical fit are not sufficient.

A one-period calculation shows the mechanism. Let a successor shock $X = \sigma Z_1$ and a basis shock $B = \eta(\rho Z_1 + \sqrt{1-\rho^2} Z_2)$ combine into a legacy shock $Y = X + B$. If an idealised legacy surface identifies $Y$ as standard normal, that is one equation in three covariance parameters. With $\rho = 0$, both $\sigma = \eta = 1/\sqrt{2}$ and $\sigma = 1/2,\ \eta = \sqrt{3}/2$ reproduce it exactly, so every payoff depending only on $Y$ is priced identically. A zero-strike call on $X$ is worth $\sigma/\sqrt{2\pi}$, approximately $0.2821$ in the first case and $0.1995$ in the second. Agreement on the entire legacy distribution has not determined the successor payoff. This is an illustration of the mechanism, not a claimed result; the thesis must establish whether the required variation survives once curves, basis instruments, multiple maturities and any available options enter the observation map.

**Hedging.** Discounted terminal wealth comprises initial capital, cumulative trading gains and transaction costs; signed hedging loss is the discounted liability less that wealth. A sensitivity hedge and a mean–variance hedge provide the initial comparisons, with admissibility, financing, rebalancing and costs fixed before evaluation. Hedges will be compared across compatible pricing models on common evaluation scenarios. A learned policy is an optional later comparison, included only if it answers a question a simpler strategy cannot.

**Statistical guarantees.** The statistical object is an upper threshold for a future hedging loss, not a claim that the price is correct. The baseline is split conformal calibration for a hedge frozen before calibration, whose order-statistic threshold has an exact finite-sample marginal guarantee under exchangeability, with a Beta law describing realised calibration-conditional coverage in the continuous independent case. The research task is the extension: separating scores by a declared gap and using coupling under a stated mixing condition to control dependence, and a distance between calibration and test loss distributions to control shift, giving a target of the schematic form

$$\Pr\{L_{\mathrm{new}} \leq q\} \geq 1 - \alpha - \varepsilon_{\mathrm{dep}} - \varepsilon_{\mathrm{shift}} - \varepsilon_{\mathrm{est}}.$$

This display is a research target, not a proved theorem. Neither unrestricted shift nor unrestricted dependence can be bounded from a short historical sample without assumptions, so oracle simulation, assumption-based sensitivity analysis and estimated bounds will be reported separately. A bound that is vacuous will be reported as an inability to certify under those assumptions.

# Validation, data and feasibility

Three settings will be used. **Controlled simulation** generates data from specified transition models with known targets, varying basis volatility, dependence, maturity, strike, observation noise, costs and regime changes, and including deliberately misspecified models. **Retrospective validation**, if licensed data can be obtained, withholds successor option quotes while fitting to permitted legacy and curve information and reveals them only for evaluation; a historical LIBOR–SOFR dataset is a candidate, subject to availability and comparability. **The South African application** proceeds on the instruments and dates the data audit supports; where successor quotes are absent, the study reports compatible valuation ranges, scenario sensitivity and observable hedge outcomes, because unobserved prices cannot serve as ground truth. Training, method selection, calibration and final evaluation will be separated chronologically, with gaps where the dependence argument requires them, so that withheld data cannot enter calibration indirectly through model selection.

Data access is the central feasibility risk; if licensed data cannot be obtained, the empirical design reduces to what the available observations support, with simulation carrying the controlled validation. Novelty is a separate risk: if the statistical result follows directly from existing conformal theory it will be presented as an application, and the original contribution must then lie elsewhere. An indicative full-time schedule allocates months 1–6 to foundations, the novelty review and the data audit; 7–14 to the transition model and identification; 15–22 to hedging and the statistical analysis; 23–29 to simulation and empirical evaluation; and 30–36 to synthesis and examination preparation. Month 6 is the first decision point: confirm data access, the restricted model, and at least one candidate original result before expanding implementation.

# Anticipated contribution

The proposed contribution has two linked parts: a rigorous identification analysis for a restricted benchmark-transition model and observation set, and a justified analysis of loss thresholds for implementable hedges under specified dependence and shift. Both remain conditional on the literature audit and on successful proofs. A South African implementation is an application contribution; geographic novelty alone will not establish the mathematical or statistical originality the degree requires. A precise negative result — a non-identification theorem, or a demonstration that no informative certificate survives realistic sample sizes — would be a legitimate outcome, provided its assumptions and implications are exact.

# Preparation and support required

I hold an MSc in Mathematical Statistics and come to the mathematical-finance component as a learner rather than a specialist. The reading sequence is therefore explicit: Mavuso's UCT probability notes for measure-theoretic probability, conditioning, martingales and stochastic integration; Shreve (2004) to connect those tools to no-arbitrage pricing and changes of measure; and Brigo and Mercurio (2006) for interest-rate modelling. Before attempting the transition extensions I will reproduce, independently, a caplet pricing calculation, a finite-dimensional mean–variance hedge and an independent-sample conformal threshold. Possession of a draft manuscript is not evidence of understanding its contents, and the preparation plan is written on that assumption.

Four working records will run across the project: a notation register, an assumption register, a reference register, and a claim-and-proof register in which every claim carries a status — established background, proved here, proposed theorem, conjecture, verified numerical evidence, or unsupported claim requiring investigation. Imported theorems will have their hypotheses rechecked in the new setting at the point of use.

The supervision required spans two areas: mathematical statistics, particularly dependent-data inference and distribution-free methods, and mathematical finance, particularly interest-rate modelling and hedging in incomplete markets. Access to market data is the other substantive need, and a contact able to advise on instrument availability and quoting conventions would materially reduce the feasibility risk.

Items to settle before the proposal is finalised are the precise model class, data access, the novelty statement, and the School's current proposal template and length requirements. The research uses market data and simulation rather than human participants, but the applicable ethics or exemption process will still be confirmed. This concept note and the supporting manuscript were prepared with AI assistance; that assistance will be disclosed as the institution requires, and responsibility for every retained claim rests with me.

# Key references

A full bibliography accompanies the extended proposal. The sources below are those the concept note relies on directly.

- Alfeus, M. (2026). Event-aware jump-diffusion for the JIBAR–ZARONIA spread. SARB Working Paper 26/06.
- Barber, R. F., Candès, E. J., Ramdas, A., and Tibshirani, R. J. (2023). Conformal prediction beyond exchangeability. *Annals of Statistics*, 51(2), 816–845.
- Barber, R. F., and Pananjady, A. (2026). Predictive inference for time series: why is split conformal effective despite temporal dependence? *Proceedings of ALT*, 313.
- Brigo, D., and Mercurio, F. (2006). *Interest Rate Models — Theory and Practice*, 2nd ed. Springer.
- Feng, Y., Rudd, R., Baker, C., Mashalaba, Q., Mavuso, M., and Schlögl, E. (2018). Quantifying the model risk inherent in calibration and recalibration of option pricing models. arXiv:1810.09112.
- Konaite, T. T. (2024). *Pricing Interest Rate Derivatives Using the Forward Market Model*. MSc dissertation, Wits.
- Lyashenko, A., and Mercurio, F. (2019). Looking forward to backward-looking rates: a modeling framework for term rates replacing LIBOR.
- Mavuso, M. M. (2014). *Mean–Variance Hedging in an Illiquid Market*. MPhil dissertation, UCT.
- Menziwa, S. (2023). *Pricing, Calibration and Hedging under the LIBOR Model*. MPhil dissertation, UCT.
- Oliveira, R. I., Orenstein, P., Ramos, T., and Romano, J. V. (2024). Split conformal prediction and non-exchangeable data. *JMLR*, 25(225).
- Ramos, T. R., Graziadei, H., and Cabezas, L. M. C. (2026). Conformal prediction via transported Beta laws. arXiv:2605.19024.
- Robbertze, Y. (2021). *Neural Network LIBOR Market Model for Pricing and Hedging Interest Rate Derivatives*. Master's thesis, UCT.
- South African Reserve Bank (2025). *Market conventions for ZARONIA-based non-linear derivatives*. MPG.
- Stangroom, J. (2023). *Deep Hedging in Incomplete Markets*. MSc dissertation, UCT.
- Vovk, V. (2012). Conditional validity of inductive conformal predictors. *PMLR*, 25, 475–490.
- Willems, S. (2020). SABR smiles for RFR caplets. arXiv:2004.04501.
