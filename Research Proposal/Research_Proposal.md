---
title: "Pricing and Hedging Through a Benchmark Transition Without an Options Market"
subtitle: "Identifiability, Smile Transport and Finite-Sample Model-Risk Certification for the JIBAR-to-ZARONIA Derivatives Book"
author: "Thabang Baloyi"
date: "Research proposal for the degree of Doctor of Philosophy in Mathematical Statistics, School of Statistics and Actuarial Science, University of the Witwatersrand, Johannesburg. Draft of 9 September 2026."
---

# Administrative summary

| Item | Detail |
|---|---|
| Candidate | Thabang Baloyi, MSc Mathematical Statistics (University of the Free State, in completion) |
| Degree | PhD in Mathematical Statistics, by thesis |
| School | School of Statistics and Actuarial Science, Faculty of Science, University of the Witwatersrand |
| Proposed supervisor | To be confirmed: a member of the School working in dependent-data inference, time-series or distribution-free methods |
| Proposed co-supervisors | (i) Mathematical finance: Wits School of Computer Science and Applied Mathematics, or external (Stellenbosch or UCT African Institute of Financial Markets and Risk Management); (ii) Industry: a rates quantitative analyst at a South African Reserve Bank Market Practitioners Group member bank |
| Mode | Part-time, five years; full-time equivalent four years |
| Ethics | No human participants. Market data only. Ethics waiver to be requested from the Faculty Graduate Studies Committee |
| Funding | Self-funded tuition; data via university terminal and industry sponsor; conference travel to be applied for |

# Abstract

On 31 December 2026 the Johannesburg Interbank Average Rate (JIBAR) will be published for the last time. Under the fallback methodology adopted by the South African Reserve Bank's Market Practitioners Group and the International Swaps and Derivatives Association, every legacy JIBAR-linked cap, floor and swaption becomes an option on the South African Rand Overnight Index Average (ZARONIA) compounded in arrears, plus a fixed credit adjustment spread. Unlike the transition from USD LIBOR to SOFR, the new reference rate has no options market and none is expected before the transition completes. South African banks must therefore value, hedge and reserve against a converted option book whose volatility smile cannot be observed.

This thesis treats that problem as one of statistical identifiability and finite-sample inference. The first contribution is a theorem that decomposes the map from the observable inputs (the JIBAR option surface, JIBAR-ZARONIA basis swaps and the fallback spread) to the unobservable compounded-rate smile into a component that is identified exactly, with an explicit error bound, and a component that is provably not identified from those inputs by any method. The second contribution, which is the doctoral spine, is a finite-sample, distribution-free certificate on the realised hedging error of any fixed valuation-and-hedging policy applied to the converted book. The certificate is a split-conformal bound under serial dependence with an explicit coverage gap in total variation on the score distribution, a proof of when it out-guarantees the block-bootstrap and traffic-light backtests used in model validation today, and a matching impossibility result showing that the drift term cannot be removed by any distribution-free method. A third, smaller contribution derives no-arbitrage constraints on transported smiles from the exact multiplicative identity that compounded rates over nested windows satisfy.

The theory is rate-agnostic and is validated on the USD LIBOR-to-SOFR transition of 2021 to 2023, where both option markets eventually traded and the target smile became observable. It is then applied to the South African book through the completed 2026 to 2028 transition. The output is a model-risk reserve with a stated confidence level, which is the object model-validation and prudent-valuation teams currently approximate by re-pricing on a handful of models and reading off the spread.

# 1. Introduction and background

## 1.1 The benchmark transition in South Africa

JIBAR is a forward-looking term rate: the three-month rate is fixed at the start of each accrual period from bank negotiable certificate of deposit quotes. ZARONIA is a backward-looking overnight rate administered by the South African Reserve Bank (SARB), computed from actual unsecured overnight deposit transactions. Following the international benchmark reform programme, the Market Practitioners Group (MPG) convened by the SARB selected ZARONIA as the successor rate and published a transition roadmap. The key milestones, as they stand at the date of this proposal, are as follows.

| Date | Event |
|---|---|
| September 2024 | First ZARONIA overnight index swaps cleared at LCH |
| November 2024 | MPG publishes market conventions for ZARONIA-based non-linear derivatives |
| March 2025 | MPG final recommendation on the JIBAR fallback methodology |
| 3 December 2025 | Formal announcement of JIBAR cessation; credit adjustment spread fixed (three-month tenor: 16.19 basis points) |
| 1 May 2026 | No new JIBAR-referencing contracts, with limited exceptions |
| November 2026 | Bulk conversion of cleared JIBAR swaps to ZARONIA overnight index swaps at LCH |
| 31 December 2026 | Final publication of JIBAR |
| 2027 onward | Legacy option book trades as options on compounded ZARONIA plus spread |

Sources: SARB MPG fallback methodology recommendation (2025); MPG conventions for ZARONIA non-linear derivatives (2024); ISDA JIBAR cessation guidance (2025); LCH member circulars on ZAR conversion (2026).

Three features distinguish the South African transition from the LIBOR transitions that the academic literature has studied.

First, there is no ZARONIA options market. The MPG conventions document specifies how ZARONIA caps, floors and swaptions are to be quoted when they trade, but at the date of writing no screen quotes exist and dealers report at most bilateral prints. The MPG itself conditions the emergence of an options market on overnight-index-swap liquidity. It is realistic to assume that no observable ZARONIA smile exists for the full duration of the transition and possibly for the full duration of this thesis.

Second, the legacy JIBAR option market is itself thin. Five or six dealers quote caps, floors and swaptions through brokers, typically at-the-money with a small number of wing strikes and a sparse swaption expiry-by-tenor grid. Vendor-interpolated surfaces exist but are marks, not trades.

Third, the fallback is mechanical and already fixed. The credit adjustment spread was set on 3 December 2025 as a five-year historical median. From 1 January 2027 a legacy JIBAR caplet with strike K is, by contract, a caplet on compounded ZARONIA with strike K minus the spread. The valuation question is therefore not whether to convert but what volatility to assign to an instrument whose underlying has never had an option traded on it.

## 1.2 What the market does today

Practitioner input gathered while developing this proposal indicates that South African banks intend to handle the converted book largely through vendor systems that already implement compounded-rate caplet pricing from the SOFR and SONIA transitions. The working convention is to keep the JIBAR volatility surface, shift the strike by the credit adjustment spread, apply a volatility scaling to account for the decay of a compounded rate's volatility across its accrual period, and add a small convexity adjustment for the difference between a rate set in advance and a rate compounded in arrears. Model-validation teams then quantify model risk by re-pricing the book under three to five alternative models and reserving against the spread of the results.

This convention has two gaps that this thesis addresses. There is no statement of which part of the assigned smile is determined by the observable inputs and which part is an assumption. And there is no finite-sample guarantee on the hedging error the convention will produce, only a comparison across models that may all share the same blind spot.

## 1.3 Why this is a statistics thesis

The problem has two layers. The first is identifiability: given the observable instruments, what is the set of compounded-rate smiles consistent with them? That is a question about the structure of a map between parameter spaces and is answered by theorems in Section 6.1. The second is inference: given that a residual set of consistent smiles remains, and given a chosen policy for valuing and hedging within it, what can be said about realised hedging error with a stated confidence, from data, without assuming the policy's model is correct? That is a question of distribution-free finite-sample inference under serial dependence, and it is the spine of the thesis.

The second layer is where the candidate's training in mathematical statistics is directly applied and where the doctoral theorem sits. The first layer is required to make the second well-posed: it fixes the ambiguity set that the certificate must cover, and it supplies the fixed policy whose hedging error is being certified.

# 2. Literature review

## 2.1 Modelling backward-looking compounded rates

Lyashenko and Mercurio (2019) introduced the generalised forward market model, extending the LIBOR market model to setting-in-arrears compounded rates by allowing the forward rate's volatility to decay deterministically to zero across the accrual period. Their follow-up (Lyashenko and Mercurio 2020) completes the framework and notes that stochastic-volatility extensions carry over by scaling the diffusion coefficients by the same decay profile. Willems (2020) derived effective SABR parameters for compounded-in-arrears caplets, and Taipe-Silvestre (2022) studied calibration of the resulting model. Piterbarg (2020) analysed the effect of fallbacks and the discounting switch on swaptions, caps, in-arrears swaps and range accruals in the LIBOR setting. Turfus and Romero-Bermúdez (2023) gave analytic smile-consistent prices for compounded-rate options in a short-rate setting. Adachi, Fukasawa and co-authors (2025) derived rigorous swaption implied-volatility asymptotics in a rough SABR forward market model. Brace, Gellert and Schlögl (2024) calibrated a multifactor stochastic-volatility term-structure model to SOFR futures options and reported implied-volatility behaviour within accrual periods. Fontana and co-authors (2023) treated caplets on compounded rates in affine models.

The consequence for this thesis is that the compounded-rate stochastic-volatility model is not a contribution. If both the rate volatility and the volatility-of-volatility are scaled by the Lyashenko-Mercurio decay profile, the model is constant-parameter SABR under a deterministic time change, and the caplet formula is the Hagan expansion with maturity replaced by the time-changed maturity. This is stated as a lemma in Chapter 2 of the thesis and cited to Willems.

## 2.2 The South African literature

Alfeus (2024) discussed the JIBAR transition and compared backward-looking and forward-looking caplets in a Wishart-type model. Alfeus (2026), in a SARB working paper, modelled the JIBAR-ZARONIA spread as an event-aware jump-diffusion with jumps on monetary policy dates and derived value-at-risk and potential-future-exposure implications. The SARB's Derivatives Workstream (2025) published a synthetic historical ZARONIA overnight-index-swap curve for 2000 to 2024 constructed from JIBAR forwards and historical spreads. Earlier South African theses on LIBOR-market-model calibration to JIBAR are lognormal and pre-date the transition. No published work treats smile transport through the fallback, identifiability of the ZARONIA smile, or finite-sample guarantees on hedging error for the converted book.

## 2.3 Conformal prediction under dependence

Conformal prediction (Vovk, Gammerman and Shafer 2005) produces prediction sets with finite-sample marginal coverage under exchangeability. Barber, Candès, Ramdas and Tibshirani (2023) extended coverage guarantees beyond exchangeability, with the coverage loss bounded by a weighted total-variation distance between the calibration and test score distributions. Oliveira, Orenstein, Ramos and Romano (2024) gave coverage penalties for split conformal prediction under mixing conditions. Gibbs and Candès (2021) introduced adaptive conformal inference for distribution shift with long-run coverage guarantees, and Gibbs, Cherian and Candès (2023) treated conditional coverage. Xu and co-authors (2025) bounded the coverage gap by a Wasserstein distance between score distributions. Schmitt (2026) applied regime-weighted conformal calibration to non-stationary portfolio value-at-risk.

None of these works certifies the hedging error of a derivatives book, none addresses the situation where the underlying's option market does not exist, and none proves a lower bound showing which part of the coverage gap is irreducible for distribution-free methods. The nearest work is on point forecasting and on value-at-risk.

## 2.4 Backtesting and model validation

The regulatory backtests that model validation uses are asymptotic. The traffic-light approach counts value-at-risk breaches (Kupiec 1995; Christoffersen 1998). The Basel Fundamental Review of the Trading Book introduces a profit-and-loss attribution test based on a Spearman correlation and a Kolmogorov-Smirnov statistic between hypothetical and risk-theoretical profit and loss. The United States Federal Reserve's supervisory guidance on model risk (SR 11-7, 2011) asks for challenger models and for quantification of model uncertainty but prescribes no method. Block bootstrap methods (Künsch 1989; Politis and Romano 1994) are the standard tool for resampling dependent profit-and-loss series. The gap is that none of these gives a finite-sample guarantee that does not depend on the validity of the model being tested.

## 2.5 Positioning

The thesis sits at the intersection of three literatures that have not met: compounded-rate option modelling, conformal prediction under dependence, and model-risk quantification for derivatives books. Its contribution is neither a new pricing model nor a new conformal algorithm. It is (a) an identifiability theorem for the map that the pricing literature implements by convention, and (b) a finite-sample inference theory, with matching impossibility result, for the hedging error that the model-validation literature tests asymptotically.

# 3. Research problem

A South African bank holds a book of legacy JIBAR caps, floors and swaptions that, from 1 January 2027, are contractually options on compounded ZARONIA plus a fixed spread. It observes the JIBAR volatility surface up to cessation, JIBAR-ZARONIA basis swaps, the fixed spread, and the ZARONIA overnight-index-swap curve. It does not and will not observe any ZARONIA option price. It must choose a valuation-and-hedging policy for the converted book and hold a model-risk reserve against that choice.

The research problem is to determine, with theorems and with data, (i) which features of the converted book's volatility smile are determined by the observable inputs and which are not, and (ii) what can be guaranteed, in finite samples and without assuming any pricing model is correct, about the realised hedging error of a chosen policy, and how that guarantee compares with the backtests model validation uses today.

# 4. Aims, objectives and research questions

## 4.1 Aim

To provide the identifiability theory and the finite-sample inference theory needed to value, hedge and reserve against a converted option book when the successor rate has no options market, validated on the USD transition and applied to the South African one.

## 4.2 Objectives

1. Prove an identifiability decomposition for the map from observable JIBAR-world inputs to the compounded-rate smile, with explicit error bounds on the identified component and a characterisation of the consistent set for the non-identified component.
2. Derive no-arbitrage constraints on transported smiles from tenor consistency of compounded rates.
3. Construct a distribution-free finite-sample certificate on realised hedging error for a fixed valuation-and-hedging policy under serial dependence and drift, and prove when it out-guarantees block-bootstrap and traffic-light backtests.
4. Prove a lower bound showing the irreducible part of the coverage gap for any distribution-free method under drift.
5. Validate Objectives 1 to 4 on the USD LIBOR-to-SOFR transition, where the target smile became observable.
6. Apply the results to the South African converted book through the 2026 to 2028 transition and quantify the implied model-risk reserve against current practice.

## 4.3 Research questions

**RQ1 (identifiability).** Under a common-driver stochastic-volatility model for overnight rates, which components of the compounded-rate smile are determined by the term-rate smile, basis swaps and the fallback spread, with what error, and which are not determined by any method?

**RQ2 (tenor consistency).** Since compounded rates over nested windows satisfy an exact multiplicative identity, which families of per-tenor smile parameters can be generated by a single daily-rate volatility process, and what constraints does this place on transported smiles?

**RQ3 (certification).** For a fixed policy applied to the converted book, what finite-sample distribution-free bound on realised hedging error holds under beta-mixing and drift, and when is it tighter than block-bootstrap quantiles?

**RQ4 (impossibility).** Which part of the coverage gap in RQ3 cannot be removed by any distribution-free method, and how does that threshold relate to observable drift?

**RQ5 (application).** How large is the non-identified component in the USD transition, was the certificate valid there, and what model-risk reserve does the theory imply for the South African book relative to current practice?

## 4.4 Hypotheses

H1. The identified component of the smile map consists exactly of the fallback strike shift, a deterministic time change of the volatility, and the in-advance-to-in-arrears convexity adjustment, and its error is second order in the accrual length.

H2. The correlation between the basis spread and volatility is not identified from term-rate options plus linear instruments, and two models can match all such instruments while implying different compounded-rate smiles.

H3. A split-conformal certificate on hedging error, calibrated on disjoint blocks under beta-mixing, achieves coverage at least one minus alpha minus an explicit gap, and out-guarantees the stationary block bootstrap whenever the calibration sample is short relative to the mixing time.

H4. No distribution-free certificate can have coverage gap smaller than the total-variation distance between calibration and deployment score distributions.

# 5. Theoretical framework

## 5.1 Market model

Let the overnight rate process be driven by a single Brownian filtration. A compounded rate over the window from T to T plus Delta is a functional of the overnight path on that window. The forward-looking term rate for the same window is fixed at T. Under a stochastic-volatility specification for the overnight forward rates with a common volatility driver, the compounded forward rate has a volatility that decays deterministically across the accrual window (Lyashenko and Mercurio 2019). When both the rate volatility and the volatility-of-volatility decay with the same profile, the compounded rate is a constant-parameter SABR process under the deterministic time change given by the integral of the squared decay profile. The caplet price is then the Hagan expansion at the time-changed maturity. This is Lemma 2.1 of the thesis.

## 5.2 The smile map

Denote by S the observable JIBAR-world data: the term-rate implied-volatility surface, the basis-swap curve and the fixed fallback spread. Denote by Sigma the compounded-rate smile for the converted book. The market convention implements a map from S to Sigma. The thesis studies the structure of the set of all Sigma consistent with S under the model class of Section 5.1. Identifiability means that this set is a singleton. Partial identifiability means that some coordinates of Sigma are constant over the set and others are not.

## 5.3 Hedging error and certification

Fix a policy pi that assigns a valuation and a hedge ratio to each instrument in the converted book on each rebalancing date, using only S and the ZARONIA curve. The realised hedging error over a horizon is the terminal profit and loss of the hedged position. Its distribution depends on the true market dynamics, which are unknown and non-stationary. The certificate is a data-dependent threshold q such that the probability that realised hedging error exceeds q is at most alpha plus an explicit gap, with the probability taken over deployment paths and the guarantee holding without any assumption that the model underlying pi is correct.

The technical setting is that of Barber, Candès, Ramdas and Tibshirani (2023). Conformity scores are the realised hedging errors of pi on calibration blocks. Under exchangeability the empirical quantile of the scores gives exact marginal coverage. Under serial dependence and drift, the coverage loss is bounded by a weighted total-variation distance between the calibration and deployment score distributions plus a term from the effective sample size under mixing (Yu 1994; Oliveira and co-authors 2024). The thesis works in score space, on the scalar distribution of hedging errors, rather than on path space. This choice is deliberate: it makes the drift term estimable from blocked data and avoids the non-estimability of path-space distances from a single realised history.

## 5.4 Why the policy is fixed

The certificate is for a fixed policy pi, trained or specified before the calibration window. Conditional on pi, the hedging error on a fresh path is an ordinary score, and the conformal argument applies unchanged. The thesis does not claim that policy dependence creates a new statistical obstacle; it does not. Online retraining and market-impact feedback, which would create such an obstacle, are excluded from scope and noted as future work.

# 6. Methodology

## 6.1 Objective 1: identifiability decomposition (RQ1)

*Setting.* Common-driver stochastic-volatility model for overnight forward rates with decay profile g; term rate and compounded rate for the same window; basis spread with its own dynamics and a correlation rho with the volatility driver.

*Method.* Write the compounded-rate implied volatility as an expansion in the accrual length Delta around the term-rate implied volatility at the shifted strike. Identify the terms that depend only on S (strike shift, time change, convexity between in-advance and in-arrears) and bound the remainder. Show that the first-order dependence on rho survives in the compounded-rate smile but is absent from every instrument in S, by computing the sensitivities of each observable to rho. Construct two explicit models with different rho that match S exactly and differ in Sigma; this is the counterexample that establishes non-identifiability.

*Deliverable.* Theorem 1 (decomposition with error of order Delta squared on the identified component) and Theorem 2 (non-identifiability of the basis-volatility correlation, with the consistent set characterised as a one-parameter family in rho).

*Validation.* Section 6.5.

## 6.2 Objective 2: tenor consistency (RQ2)

*Setting.* Compounded rates over windows one-to-two, two-to-three and one-to-three satisfy one plus the long rate times its accrual equals the product of the two short factors, exactly, by construction. A forward market model specifies dynamics per tenor without enforcing this.

*Method.* Derive the constraints that the identity imposes on per-tenor SABR parameters generated by a single daily-rate volatility process. Characterise the parameter families that are closed under compounding. Show which transported smiles violate the constraints and what arbitrage results.

*Deliverable.* Theorem 3 (necessary and sufficient conditions on per-tenor parameters for consistency with a single daily-rate process), and a diagnostic that flags a transported smile as tenor-inconsistent.

## 6.3 Objective 3: certification (RQ3)

*Setting.* Stationary beta-mixing hedging-error process with mixing coefficients decaying polynomially. Policy pi fixed on the fitting sample. Calibration on n blocks of length b disjoint from the fitting sample. Deployment on a fresh window.

*Method.* Apply weighted split conformal prediction to the block-level hedging errors. Bound the coverage loss by three terms: the total-variation distance between calibration and deployment score distributions, a concentration term of order the square root of b times the logarithm of one over delta over n, and a mixing term of order n times the mixing coefficient at lag b, following the blocking arguments of Yu (1994) and the non-exchangeable bounds of Barber and co-authors (2023). Estimate the total-variation term from blocked data via a plug-in estimator with its own finite-sample bound. Compare with the stationary block bootstrap of Politis and Romano (1994) and with breach-count backtests: derive conditions on n, b and the mixing rate under which the conformal certificate has a guaranteed coverage that the bootstrap does not.

*Deliverable.* Theorem 4 (coverage bound), Proposition 5 (estimability of the gap term), Theorem 6 (conditions for dominance over block bootstrap).

## 6.4 Objective 4: impossibility (RQ4)

*Method.* Construct two hedging-error distributions with total-variation distance epsilon between calibration and deployment such that any procedure with valid coverage under one has coverage reduced by at least epsilon under the other. Le Cam's two-point method on the score distribution gives the lower bound directly.

*Deliverable.* Theorem 7 (no distribution-free method achieves coverage gap below the total-variation distance), which shows that the drift term in Theorem 4 is irreducible and that the certificate is sharp up to the concentration and mixing terms.

## 6.5 Objective 5: validation on the USD transition (RQ5, part one)

*Data.* USD LIBOR cap and swaption volatility surfaces 2019 to 2023; SOFR cap and swaption volatility surfaces from their emergence to 2024; LIBOR-SOFR basis swaps; the ISDA fallback spread for USD LIBOR; SOFR overnight-index-swap curves. Available on the university's market-data terminal.

*Design.* Treat the USD market on each date before SOFR options became liquid as if it were the South African market: only LIBOR options, basis swaps and the fallback spread are observable. Apply Theorems 1 to 3 to produce the identified component and the consistent set. Compare with the SOFR smile once it became observable. Measure the realised size of the non-identified component. Fix a policy pi as the market convention and compute its hedging error on the converted USD book; apply Theorem 4 with calibration on 2021 to 2022 and deployment on 2023; report empirical coverage against the bound and against block-bootstrap intervals.

*Outcome.* If the identified component matches the observed SOFR smile within its error bound and the non-identified component is of the predicted form, Theorems 1 and 2 are validated. If the certificate held at its stated level, Theorem 4 is validated. If either fails, the thesis reports the failure and its size, which is itself a result.

## 6.6 Objective 6: application to the South African book (RQ5, part two)

*Data.* ZARONIA fixings and the SARB synthetic historical overnight-index-swap curve (free). JIBAR fixings and the published credit adjustment spread (free). ZAR and USD swap and overnight-index-swap curves (university terminal). JIBAR cap, floor and swaption volatility surfaces (dealer-confidential; industry co-supervisor). Realised hedging profit and loss of the converted book from January 2027 (constructed from public fixings and curves, or provided by the industry co-supervisor).

*Design.* Apply Theorems 1 to 3 to the JIBAR surface on each date up to cessation to obtain the identified component of the ZARONIA smile and the consistent set. Fix pi as the market convention (strike shift, scaled volatility, convexity). Calibrate the certificate on the first eighteen months of converted-book hedging error and deploy on the following six. Compute the model-risk reserve implied by the width of the consistent set and the certified hedging-error quantile. Compare with the reserve implied by re-pricing on five alternative models.

*Outcome.* A reserve with a stated confidence level, a statement of which part of that reserve is a theorem and which part is a certified residual, and a comparison with current practice.

## 6.7 Software

All computation in Python with open-source libraries. Multi-curve bootstrap, compounded-rate caplet pricing under the time-changed SABR lemma, conformal calibration and block bootstrap will be implemented by the candidate and released with the thesis. No proprietary vendor software is required.

# 7. Preliminary work and feasibility

The following has been established during the preparation of this proposal.

1. **Novelty.** A structured literature search (twenty-six queries across arXiv, SSRN, journal indices and South African repositories, September 2026) found no work on identifiability of the successor-rate smile, no finite-sample certification of hedging error for a converted book, and no South African work on either.
2. **Non-triviality of the mathematics.** The compounded-rate stochastic-volatility model reduces to standard SABR under a time change; this is known and is not claimed. The identifiability theorem and the impossibility theorem are not consequences of existing results and were confirmed as open by three independent reviewers with expertise in interest-rate modelling, stochastic analysis and conformal prediction.
3. **Falsifiability.** The USD transition supplies a complete natural experiment in which the object the theory predicts became observable. This is what distinguishes the thesis from a calibration exercise.
4. **Data.** Every input except the JIBAR option surfaces is free or available on a university terminal. The USD validation chapter is fully feasible without any South African data.
5. **Timing.** The South African transition completes during year one of the thesis, and two years of converted-book hedging error will have accrued by the start of year four, which is the calibration sample the certificate needs.

# 8. Data, ethics and access

The thesis uses market data only. No human participants, no personal data, and no confidential client positions are involved. An ethics waiver will be requested from the Faculty of Science Graduate Studies Committee.

JIBAR option volatility surfaces are dealer-confidential. Access will be arranged through the industry co-supervisor under a data-use agreement restricting use to the thesis and requiring aggregation in any published output. If no agreement is reached in year one, the South African application chapter will be reduced to the components computable from public and terminal data, and the thesis will state so. The theoretical chapters and the USD validation are unaffected.

# 9. Expected contributions and significance

**To mathematical statistics.** A finite-sample distribution-free certificate under serial dependence for a functional (hedging error) of a fixed decision policy, with an estimable coverage gap and a matching lower bound. The impossibility theorem is, to the candidate's knowledge, the first sharp statement of what distribution-free inference cannot achieve under drift in this setting.

**To mathematical finance.** An identifiability theorem for smile transport through a benchmark fallback, with a counterexample showing non-identifiability of the basis-volatility correlation, and no-arbitrage constraints from tenor consistency of compounded rates. The results hold for SOFR, SONIA, ESTR and any successor rate; ZARONIA is the case in which the absence of an options market makes them consequential.

**To South African practice and regulation.** A model-risk reserve for the converted JIBAR book with a stated confidence level and a decomposition into what is a theorem and what is a certified residual. This speaks directly to prudent-valuation requirements and to the SARB Prudential Authority's expectations on model risk during the transition.

**To the candidate's field.** A demonstration that a statistics doctorate can take a live market event as its application without becoming a calibration exercise, by putting the inference theorem at the centre.

# 10. Thesis structure

1. Introduction: the South African transition, the problem, the contributions.
2. Preliminaries: compounded rates, the forward market model, the time-changed SABR lemma, conformal prediction under dependence.
3. Identifiability of the compounded-rate smile (Theorems 1 and 2).
4. Tenor consistency and no-arbitrage constraints (Theorem 3).
5. Finite-sample certification of hedging error (Theorems 4 to 6).
6. Impossibility (Theorem 7).
7. Validation: the USD LIBOR-to-SOFR transition.
8. Application: the South African converted book and its model-risk reserve.
9. Conclusions, limitations and future work.

# 11. Timeline

Part-time, five years. Full-time equivalent four years, with the fifth year absorbed.

| Period | Activity | Milestone |
|---|---|---|
| Y1 Q1–Q2 | Prerequisites: stochastic calculus for term structure (Filipović; Brigo and Mercurio), multi-curve framework (Henrard), Barber et al. (2023) and Oliveira et al. (2024) in detail | Reading report to supervisors |
| Y1 Q2–Q3 | Reproduce Lyashenko-Mercurio, Willems and Piterbarg numerically; build USD and ZAR multi-curve bootstrap | Working code |
| Y1 Q3 | Acquire USD option data; approach industry co-supervisor for ZAR data | Data-use agreement drafted |
| Y1 Q4 | Proposal defence | Faculty approval |
| Y2 Q1–Q2 | Theorems 1 and 2 | Draft of Chapter 3 |
| Y2 Q3 | USD identifiability validation | Draft of Chapter 7, part one |
| Y2 Q4 | Paper 1 submitted | *Quantitative Finance* or *Journal of Computational Finance* |
| Y3 Q1–Q2 | Theorems 4 to 7 | Drafts of Chapters 5 and 6 |
| Y3 Q3 | USD certification validation; block-bootstrap comparison | Chapter 7 complete |
| Y3 Q4 | Paper 2 submitted (the doctoral paper) | *Electronic Journal of Statistics* or *Bernoulli* |
| Y4 Q1 | Theorem 3 | Draft of Chapter 4 |
| Y4 Q2–Q3 | South African application on the converted book (two years of realised data available) | Chapter 8 |
| Y4 Q4 | Paper 3 submitted | *South African Journal of Economic and Management Sciences*, or *Finance and Stochastics* if Theorem 3 is strong |
| Y5 | Write-up, internal review, submission, examination | Thesis submitted |

# 12. Risks and mitigation

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| No South African option-surface data | Medium | Chapter 8 reduced | USD chapter is complete without it; Chapter 8 uses public and terminal data; state the limitation |
| Theorem 2 counterexample resists construction | Low | Identifiability result weaker | Deliver the identified-part bounds and a numerical demonstration of non-identifiability; still publishable |
| Theorem 7 lower bound resists | Low | Certificate sharpness unproven | Certificate with honest empirical coverage and block-bootstrap comparison stands alone |
| Certificate is vacuous at realistic sample sizes | Medium | Practical relevance reduced | This is itself a result: report the drift threshold above which no distribution-free certificate is informative |
| A ZARONIA options market emerges early | Low | Motivation weakened | It would supply a second validation dataset; the theorems are unchanged |
| Candidate's finance prerequisites | Medium | Year-one delay | Structured reading plan with co-supervisor; Lemma 2.1 and the multi-curve bootstrap as year-one deliverables |
| Part-time hours | High | Five years not four | Timeline already planned for five |

# 13. Supervision plan

The primary supervisor is a statistician in the School of Statistics and Actuarial Science whose work covers dependent-data inference, time series or distribution-free methods, and who will own Chapters 5 and 6 and the examination framing. A finance co-supervisor from Wits mathematical finance or from Stellenbosch or UCT will own Chapters 2 to 4. An industry co-supervisor at a SARB Market Practitioners Group member bank will provide data access and market validation for Chapters 7 and 8. An international adviser in conformal prediction may be approached for Chapter 6; this is desirable and not required.

# 14. Dissemination

Three journal papers as scheduled. Presentations at the South African Statistical Association annual conference (years two and four), the Actuarial Society of South Africa or SARB Financial Stability research forum (year four), and one international conference in mathematical finance or statistics (year three, subject to funding). Code and the USD validation dataset construction released publicly. A practitioner note for the SARB Market Practitioners Group on the model-risk reserve results, subject to the data-use agreement.

# 15. Resources

University market-data terminal access; standard computing; no proprietary software. Conference travel funding to be sought from the Faculty and the National Research Foundation. No laboratory or equipment needs.

# References

Adachi, T., Fukasawa, M., Iida, K., Ikeda, S., Nakatsu, T., Tsurumi, K. and Yamakami, Y. (2025). Rough SABR forward market model. arXiv:2509.25975.

Alfeus, M. (2024). Navigating the JIBAR transition. *South African Journal of Science*, 120(3/4).

Alfeus, M. (2026). Event-aware jump-diffusion for the JIBAR-ZARONIA spread. South African Reserve Bank Working Paper WP/26/06.

Barber, R. F., Candès, E. J., Ramdas, A. and Tibshirani, R. J. (2023). Conformal prediction beyond exchangeability. *Annals of Statistics*, 51(2), 816–845.

Basel Committee on Banking Supervision (2019). *Minimum capital requirements for market risk*. Bank for International Settlements.

Board of Governors of the Federal Reserve System (2011). *Supervisory guidance on model risk management*, SR 11-7.

Brace, A., Gellert, K. and Schlögl, E. (2024). SOFR term structure dynamics: discontinuous short rates and stochastic volatility forward rates. *Journal of Futures Markets*.

Brigo, D. and Mercurio, F. (2006). *Interest Rate Models: Theory and Practice*, 2nd ed. Springer.

Christoffersen, P. F. (1998). Evaluating interval forecasts. *International Economic Review*, 39(4), 841–862.

Filipović, D. (2009). *Term-Structure Models: A Graduate Course*. Springer.

Fontana, C., Grbac, Z. and Schmidt, T. (2023). Caplet pricing in affine models for alternative risk-free rates. arXiv:2202.09116.

Gibbs, I. and Candès, E. J. (2021). Adaptive conformal inference under distribution shift. *Advances in Neural Information Processing Systems*, 34.

Gibbs, I., Cherian, J. J. and Candès, E. J. (2023). Conformal prediction with conditional guarantees. arXiv:2305.12616.

Hagan, P. S., Kumar, D., Lesniewski, A. S. and Woodward, D. E. (2002). Managing smile risk. *Wilmott Magazine*, September, 84–108.

Henrard, M. (2014). *Interest Rate Modelling in the Multi-Curve Framework*. Palgrave Macmillan.

International Swaps and Derivatives Association (2025). *JIBAR cessation guidance*.

Künsch, H. R. (1989). The jackknife and the bootstrap for general stationary observations. *Annals of Statistics*, 17(3), 1217–1241.

Kupiec, P. H. (1995). Techniques for verifying the accuracy of risk measurement models. *Journal of Derivatives*, 3(2), 73–84.

Lyashenko, A. and Mercurio, F. (2019). Looking forward to backward-looking rates: a modeling framework for term rates replacing LIBOR. SSRN 3330240.

Lyashenko, A. and Mercurio, F. (2020). Libor replacement II: completing the generalized forward market model. SSRN.

Oliveira, R. I., Orenstein, P., Ramos, T. and Romano, J. V. (2024). Split conformal prediction and non-exchangeable data. *Journal of Machine Learning Research*, 25.

Piterbarg, V. (2020). Interest rates benchmark reform and options markets. SSRN 3537925.

Politis, D. N. and Romano, J. P. (1994). The stationary bootstrap. *Journal of the American Statistical Association*, 89(428), 1303–1313.

Schmitt, C. (2026). Taming tail risk: conformal calibration for nonstationary portfolio value-at-risk. arXiv:2602.03903.

South African Reserve Bank, Market Practitioners Group (2024). *Market conventions for ZARONIA-based non-linear derivatives*.

South African Reserve Bank, Market Practitioners Group (2025). *JIBAR fallback methodology: final recommendation*.

South African Reserve Bank, Derivatives Workstream (2025). *Historical estimation of the ZARONIA OIS curve*.

Taipe-Silvestre, M. (2022). Tuning the FMM-SABR for RFR caplets. SSRN 4046344.

Turfus, C. and Romero-Bermúdez, A. (2023). Analytic RFR option pricing with smile and skew. arXiv:2301.01260.

Vovk, V., Gammerman, A. and Shafer, G. (2005). *Algorithmic Learning in a Random World*. Springer.

Willems, S. (2020). SABR smiles for RFR caplets. arXiv:2004.04501.

Xu, R., Chen, C., Sun, Y., Venkitasubramaniam, P. and Xie, S. (2025). Wasserstein-regularized conformal prediction under general distribution shift. *International Conference on Learning Representations*. arXiv:2501.13430.

Yu, B. (1994). Rates of convergence for empirical processes of stationary mixing sequences. *Annals of Probability*, 22(1), 94–116.
