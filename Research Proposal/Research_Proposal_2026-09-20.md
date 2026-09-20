Thabang Bongani Junior Baloyi\
Proposed PhD in Mathematical Statistics\
University of the Witwatersrand Johannesburg\
Proposed academic home and supervisor to be confirmed

**Status** Working draft for supervisor discussion • 20 September 2026

This proposal develops the research programme suggested by the supplied thesis manuscript. Its mathematical results, novelty claims and empirical feasibility remain to be established. The manuscript is treated as a source of conjectures and preliminary arguments; no completed research results are claimed here.

# Research summary

I propose to investigate how a transition from a term interest rate benchmark to a compounded overnight benchmark affects option valuation and hedging when successor-rate option prices are sparse or unavailable. The South African JIBAR--ZARONIA transition will motivate the application. The precise observation dates, available instruments and degree of option-market liquidity will be established through a data audit rather than assumed for every market period.

The first objective is to determine which successor-rate option prices or volatility features are identified by legacy option prices, yield curves and basis instruments within a specified arbitrage-free model class. Where identification fails, I will characterise the range of compatible valuations and establish what additional observations or restrictions would narrow it. The second objective is to investigate finite-sample upper bounds for hedging losses when observations are dependent and the loss distribution changes during transition.

The initial product scope is caplets with explicitly specified overnight compounding and payment conventions. Liquid swaps and cash instruments will form the baseline hedge set. Simulation will test mathematical claims under controlled conditions; historical validation will depend on obtaining suitable quotes and hedge-instrument data. A retrospective study in a market with observable successor options will be considered if licensed data are available. The anticipated doctoral contribution is a precise account of what can be learned and certified under limited market information, including the limits of such claims.

# Central research question

Under what assumptions can legacy market information determine successor-rate option values, and what statistically defensible bounds can be placed on the losses from hedging those options during a benchmark transition?

# Proposal overview and navigation

This proposal asks how much information is available for valuing an option on a successor interest-rate benchmark when that option cannot itself be calibrated to a liquid market. It then asks how to assess the losses from an implementable hedge. These are related questions, but they concern different objects: a valuation under a pricing measure and a loss distribution under a physical measure. The proposed research will maintain that distinction throughout.

The argument proceeds from contract definitions and the literature to a restricted mathematical model, identification analysis, hedging methods and statistical guarantees. The empirical programme follows the mathematical analysis so that the experiments test stated claims. The detailed work plan and ten-chapter thesis outline appear at the end of the main proposal.

  ---------------------------------------------------------------------------
   **Pages**  **Focus**
  ----------- ---------------------------------------------------------------
     3--4     Economic motivation and contractual cashflows

     5--9     Critical literature review and proposed originality

    10--12    Objectives probability measures and transition model

    13--16    Identification worked example and numerical pricing

    17--18    Hedging model uncertainty and optional learning methods

    19--22    Statistical guarantees dependence and distribution shift

    23--25    Data simulation and historical validation

    26--28    Research risks schedule and ten chapter thesis outline

    29--30    Selected references
  ---------------------------------------------------------------------------

## How to interpret the proposed contribution

The proposal describes a programme of investigation. A displayed definition specifies the object being studied; a worked example explains a mechanism; a research target states what remains to be established. These categories should not be read as interchangeable. The illustrative identification example and independent-score calculations are included to make the intended reasoning transparent. They are not presented as new doctoral results.

The first substantive decision is whether the chosen observation set and model family leave economically relevant target prices undetermined. The second is whether a useful loss guarantee survives the dependence and distributional changes that the application requires. A negative result can be informative if its assumptions and implications are precise. The final thesis must establish an original contribution beyond assembling existing tools.

# Economic motivation and the information problem

The financial problem begins with a contractual obligation whose value depends on future interest rates. A dealer or investor may observe a reliable market in instruments referencing a legacy benchmark, yet have little direct evidence about options referencing its replacement. Curves, swaps and basis instruments provide information about some aspects of the transition. They need not reveal the complete distribution relevant to an option payoff.

An option is sensitive to outcomes beyond an average rate. Two models can agree on forward values while assigning different probabilities to large positive rate moves. A caplet, which pays when a rate exceeds a strike, distinguishes those models. Consequently, importing one volatility parameter from the legacy market may produce a numerical answer without demonstrating that the answer follows uniquely from observed information. The thesis will investigate this distinction within explicit, restricted model classes.

## Valuation uncertainty and trading risk

Valuation uncertainty concerns the range of model prices compatible with the selected observations and assumptions. Trading risk concerns the realised profit or loss from holding and hedging the liability. A hedge can perform reasonably well even when the initial model price is uncertain, and a closely calibrated model can still generate substantial losses when trading constraints or changing dynamics matter. These outcomes will therefore be evaluated separately.

The proposed hedge must reflect instruments that could actually be traded on the relevant date. An unavailable successor option will not be included simply because it would complete the model. Similarly, a legacy option that exists in a database may not support repeated rebalancing if its quotes are stale or its transaction costs are prohibitive. The empirical audit will define the feasible instrument set before strategies are compared.

## Why the South African application matters

The JIBAR--ZARONIA setting supplies a concrete application in which benchmark definitions, basis dynamics and market development must be considered together. SARB conventions will determine the contractual implementation, while Alfeus (2026) provides a relevant example of modelling spread dynamics around scheduled events. The proposed thesis will distinguish such historical spread modelling from the separate identification of risk-neutral option valuations.

The application will be dated precisely. A statement about illiquidity will refer to a particular instrument, tenor and observation period, supported by the data audit. The title's absence of liquid option markets describes the information regime under study; it does not assert that every successor-rate option is absent at every stage of transition. This restriction makes the research question testable and prevents its interpretation from depending on an unverified description of the entire market.

# Contract definitions and a worked payoff example

The first implementation task is a contract specification sheet. It will record the legacy and successor reference rates, observation dates, accrual period, day-count convention, compounding rule, payment date, notional, strike and any contractual spread. Rate units must be explicit: a rate of 8 per cent is represented as 0.08 in the calculation. The specification will also separate a newly written successor contract from a legacy contract converted under fallback terms.

For a simple illustration, consider a hypothetical two-day accrual period with equal day fractions of 1/365 and annualised overnight rates of 8 per cent and 9 per cent. This example is deliberately simplified and is not a statement of the conventions for a particular traded instrument. Multiplying the two daily accumulation factors and annualising over 2/365 gives a compounded rate of approximately 8.50099 per cent.

$R\  = \ \frac{(1\  + \ 0.08/365)(1\  + \ 0.09/365)\  - \ 1}{2/365}\  \approx \ 0.0850099.$

With a notional of R1,000,000 and a strike of 8 per cent, the undiscounted caplet payoff is approximately R27.45. Discounting to the valuation date requires the appropriate payment-date discount factor. The purpose of the example is to connect the compounding definition to an actual cash amount and expose unit errors before a stochastic model is introduced.

## Conventions that change the random payoff

A lookback, observation shift or payment delay can change which rates enter the product and when the amount is known. Accrual fractions may differ across weekends and holidays. A spread may be added outside compounding or incorporated through a different contractual rule. The implementation will follow the applicable documented convention and will not substitute one choice for another merely because the resulting formulas look similar.

The time at which the last underlying fixing becomes available also matters. Before the accrual period begins, the full compounded rate is uncertain. During the period, some fixings are known and the remaining uncertainty decreases. A pricing algorithm must condition on the known portion rather than resimulate the whole period. Willems (2020) and Lyashenko and Mercurio (2019) will inform the treatment of backward-looking rates and their changing information structure.

## Contract validation before model validation

The baseline implementation will reproduce deterministic cashflows, a zero-volatility limit and cases where every fixing is already known. It will check that the payoff is non-negative, decreases as the strike increases, and scales linearly with notional. These checks cannot prove that the stochastic model is correct. They establish that subsequent comparisons concern the intended contract, reducing the risk of mistaking a convention error for a modelling result.

# Background and critical literature review

Interest-rate derivatives depend on contractual definitions as well as stochastic dynamics. Replacing a forward-looking term rate with a rate compounded over an accrual period changes when the underlying is observed and how uncertainty accumulates. Brigo and Mercurio (2006) provide the multi-model pricing foundation. Lyashenko and Mercurio (2019) develop a forward-market approach to backward-looking rates, while Willems (2020) studies SABR smiles for risk-free-rate caplets. These works inform the modelling framework; they do not by themselves establish identification of successor smiles from a selected set of legacy observations.

South African research offers useful starting points. Konaite's Wits dissertation (2024) develops and compares interest-rate pricing models including the forward market model. Menziwa's UCT dissertation (2023) treats pricing, calibration and hedging under the LIBOR model. Robbertze (2021) examines neural-network volatility modelling within an interest-rate framework. These studies will guide implementation and benchmark selection. Their use here does not imply that they establish the proposed identification or coverage results.

Mavuso (2014) studies mean--variance hedging with a dynamically traded liquid asset and an illiquid asset available for a static position. This distinction helps formalise trading constraints in the proposed hedge problem. Feng et al. (2018) distinguish calibration and recalibration components of model risk through relative-entropy methods. Their framework motivates keeping valuation uncertainty, parameter changes and realised hedging losses separate. Stangroom (2023) provides a UCT reference for deep hedging in incomplete markets; a learned policy will be an optional comparison after conventional hedges are established.

The statistical component builds on conformal prediction rather than claiming a new general-purpose coverage principle. Vovk (2012) addresses conditional validity, Barber et al. (2023) study departures from exchangeability, and Oliveira et al. (2024) analyse split conformal prediction for non-exchangeable data. Recent work by Barber and Pananjady (2025, revised 2026) and Ramos et al. (2026) is particularly relevant to dependence and calibration-conditional coverage. Any proposed result must be compared against their assumptions and conclusions before novelty is asserted.

# Problem statement and provisional research gap

A fitted model can return a unique successor caplet price even when the observed market information is compatible with several such prices. At the same time, small average hedging error does not imply a valid upper-tail guarantee. The proposed problem is to distinguish uncertainty that market observations resolve from uncertainty introduced by model restrictions, and then assess what guarantees remain for implementable hedges.

The provisional gap is the connection between a rigorously characterised set of transition models and a finite-sample analysis of their hedging losses under specified dependence and distributional change. I will test this gap through a structured literature comparison covering observation sets, model classes, trading constraints, guarantee types and proof assumptions. If the candidate results reduce to established theorems, the contribution will need to be narrowed or reformulated before the proposal is finalised.

# Interest rate modelling literature and its use

The literature review will distinguish a model for the level of rates, a model for forward rates, a model for the relation between benchmarks and an approximation for an option smile. These objects answer different questions. A successful description of historical spread movements, for example, does not automatically specify the pricing measure or identify the distribution of a compounded rate under that measure.

Brigo and Mercurio (2006) will supply the main reference for interest-rate pricing architecture, changes of numeraire, calibration and model comparisons. The proposal will use that foundation to define what is traded and what must be a martingale under the selected numeraire. This step precedes any discussion of a transported smile: a volatility formula alone does not constitute a complete, arbitrage-consistent transition model.

Lyashenko and Mercurio (2019) address the modelling of backward-looking replacement rates through a forward-market framework. The reading task is to follow the relationship between the state variables, the observed rate and the chosen pricing measure. Willems (2020) is relevant to the behaviour of SABR smiles for risk-free-rate caplets. Its assumptions and approximation regime will be recorded before importing any volatility mapping into the thesis.

## What the local dissertations contribute

Konaite's Wits dissertation (2024) offers a local account of interest-rate modelling and the forward market model. Menziwa's UCT dissertation (2023) links LIBOR-model pricing, calibration and hedging. Their role in this project is to provide reproducible intermediate calculations and methodological context. I will select one manageable benchmark calculation from each relevant work and reproduce it with independently documented conventions.

Robbertze (2021) connects neural-network volatility modelling with an interest-rate framework. This is relevant to flexible function approximation, but a flexible model may create additional non-identification when target option prices are unavailable. The proposed research will therefore ask what information constrains a learned volatility function, rather than infer credibility solely from fitting the observations used for training.

## From review to a precise modelling choice

For each model, I will record its state variables, traded instruments, measure, admissible parameter set, calibration inputs and target output. I will also note whether its conclusions are exact, numerical or asymptotic. This comparison will determine the smallest model family capable of representing the intended information gap. Starting with that family should make it possible to construct proofs and counterexamples before increasing dimensionality.

The main literature question is not which model is most elaborate. It is which conclusions about successor options follow from market observations once the model restrictions are made explicit. A stronger assumption may yield a narrower price range. The thesis must explain what that assumption contributes and whether any available evidence supports it.

# Incomplete markets hedging and model risk literature

In a complete market under the relevant technical assumptions, a claim can be replicated by an admissible trading strategy. The proposed setting may be incomplete because the available instruments do not span all relevant shocks or because trading restrictions prevent replication. The thesis will specify the source of incompleteness, since stochastic incompleteness, illiquidity and discrete rebalancing need not have the same mathematical treatment.

Mavuso's supplied dissertation, Mean--Variance Hedging in an Illiquid Market, is a direct starting point. Its distinction between dynamic trading in a liquid asset and an initial static position in an illiquid asset makes trading permissions part of the mathematical problem. I will study the projection arguments and their integrability requirements before adapting any result to the proposed instrument set. The initial implementation will use a small number of assets so that the source of residual risk remains interpretable.

## Quadratic criteria and their limits

A mean--variance hedge provides a tractable way to control expected squared terminal error under a specified physical model. It does not guarantee a bound on every realised loss. It can also assign the same squared penalty to a shortfall and a surplus of equal magnitude. The evaluation will therefore include an upper-tail analysis in addition to the quadratic objective. This motivates the statistical component of the thesis without claiming that one criterion subsumes the other.

The work will distinguish an optimal hedge inside a mathematical model from the performance of its estimated implementation. Parameter estimation, discretisation, transaction costs and repeated recalibration can all change realised errors. Each source will be introduced separately in simulation before the full empirical setting is attempted. This staged design should reveal why a hedge succeeds or fails.

## Model risk and flexible strategies

Feng et al. (2018) examine model risk associated with calibration and recalibration using a relative-entropy approach. That perspective is useful for asking whether a model's apparent fit is stable across dates. The proposed identification analysis asks a complementary question: whether multiple models already agree with the selected observations at one date while disagreeing about the target option. The statistical analysis then studies a realised loss distribution. These quantities will not be reported as interchangeable measures of risk.

Stangroom (2023) and Robbertze (2021) provide local references for learning-based methods. A neural strategy will be considered only after a conventional hedge is implemented and its information set is fixed. Any comparison must use the same assets, costs, training period and evaluation paths. A more flexible strategy will need a separate assessment of estimation error and stability. Its inclusion is optional; the core identification and inference questions do not depend on demonstrating that machine learning outperforms a baseline.

# Statistical literature and the meaning of coverage

Conformal prediction supplies a useful starting point because it connects an empirical ranking of scores to a finite-sample probability statement. In the proposed application, the score is a hedging loss over a specified horizon. An upper threshold is useful only if its interpretation is clear: the probability may average over repeated calibration samples, or it may concern the performance of the threshold after one particular calibration sample has been observed.

Vovk (2012) is relevant to this distinction through the study of conditional validity. The proposal will separate marginal coverage from a high-probability statement about calibration-conditional coverage. Neither automatically supplies coverage conditional on every observed market state. The exact independent-score calculation later in this proposal illustrates why a satisfactory average can coexist with unusually poor calibration samples.

## Dependence and departures from exchangeability

Financial observations commonly produce dependence through serial dynamics, shared exposures and overlapping holding periods. Barber et al. (2023) address conformal prediction beyond exchangeability, while Oliveira et al. (2024) study split conformal prediction for non-exchangeable data. These works demonstrate that the relevant research question is how the assumptions and error terms change when exchangeability is lost. Applying an unmodified independent-data interpretation to a chronological backtest would require justification.

Barber and Pananjady (2025, revised 2026) study time-series predictive inference, including predictors with memory, and characterise coverage through a switch coefficient. Their results must be examined before proposing a new generic dependence bound. Ramos et al. (2026) study deviations from the reference Beta law for calibration-conditional coverage, distinguishing effects associated with test-side shift and calibration dependence. This is particularly close to the statistical direction suggested by the supplied thesis manuscript.

## The comparison required before claiming originality

For each closest paper, I will write the precise theorem statement in common notation and compare the sampling scheme, fitted predictor, score function, dependence class, shift assumption and guarantee. A result that follows by substituting a hedging-loss score into an existing theorem will be credited as an application. It becomes a candidate theoretical contribution only if a further argument establishes something not already covered, such as a justified treatment of model selection, a new transition-specific restriction or a sharp impossibility result.

Empirical success alone will not be used to infer a finite-sample theorem. Conversely, a correct theorem can be too conservative to support useful decisions. The thesis will therefore evaluate mathematical validity and practical informativeness separately. It will report when available sample sizes or plausible dependence penalties make the proposed threshold unusable. This outcome would identify a limitation of certification in the selected information regime rather than justify changing the nominal guarantee after seeing the test results.

# Research gap and the originality assessment

The research gap is provisional. The supplied manuscript suggests combining identification of successor-rate valuations with statistical certification of hedging losses, but the presence of several techniques in one document does not establish an original contribution. The first phase will determine whether a precise question remains after the closest interest-rate and conformal results are written in a common framework.

## Candidate contribution in identification

The initial candidate is a theorem or counterexample for a stated observation map and a restricted transition model. The result should identify which combinations of parameters are constrained by legacy quotes and which target valuation functionals remain variable. If the target is not identified, the next task is to characterise the attainable valuation range and the effect of additional observations. A generic statement that sparse data create uncertainty would be insufficient.

A useful result might isolate a direction in parameter space that leaves the selected observations unchanged while altering a successor caplet value. Another might establish that a target becomes locally identified once a particular basis-sensitive instrument is added. Both require explicit assumptions, admissibility and a proof. Local rank arguments would need to be distinguished from global uniqueness, and numerical examples would need to be distinguished from exact observational equivalence.

## Candidate contribution in inference

The second candidate concerns the loss process produced by a fixed or explicitly adaptive hedge. The task is to determine whether transition-specific structure permits a useful finite-sample bound after dependence and distributional change are accounted for. The baseline conformal construction and standard distribution-function inequalities are existing tools. Novelty must arise from a new justified connection, restriction, bound or counterexample, rather than a renamed application.

One possible connection is to study how selecting a hedge from a set of observationally compatible models affects score calibration. Such selection can invalidate a guarantee if it uses the same calibration losses to choose a favourable model and certify it. The initial programme will avoid that complication through data separation. Any later theorem for selection or adaptation will have to describe the selection rule and account for it mathematically.

## Evidence required for a doctoral claim

The novelty record will contain a precise candidate statement, its nearest published result, the additional argument required, and a counterexample search. For an asymptotic claim, it will also specify the limit, the uniformity domain and the size of the remainder. For an empirical claim, it will state what comparison could falsify the proposed advantage.

At the first formal review, the supervisor and candidate will decide whether at least one candidate has a credible route to an original result. If neither does, the project must be reformulated before extensive implementation. The ten-chapter structure remains provisional and will be organised around the results actually obtained.

# Aim objectives and mathematical scope

**Aim** To develop and evaluate a framework for identifying successor-rate option valuations and quantifying residual hedging risk under limited option-market information.

**Objective 1** Specify a coherent transition model, contractual conventions and observable market information, separating risk-neutral pricing assumptions from historical estimation.

**Objective 2** Prove identification or non-identification results for a restricted model class and determine the resulting valuation ranges or approximation errors.

**Objective 3** Construct implementable hedges using the available instruments and investigate finite-sample loss guarantees under explicit assumptions.

**Objective 4** Evaluate pricing uncertainty, hedge performance and certificate informativeness in simulations and an appropriately limited empirical application.

## Research questions

RQ1 Which successor valuation functionals are constant across models compatible with legacy option quotes and curve or basis observations? RQ2 Which extra data or restrictions restore identification, and how stable is that conclusion to quote noise? RQ3 Under what dependence and distribution-shift assumptions can a calibrated loss threshold retain a finite-sample guarantee? RQ4 Are the resulting price ranges and risk bounds informative for a realistic hedge after costs and data limitations are included?

## Product and probability model

On a filtered probability space, let $r_{i}$ denote the overnight rate for accrual fraction $\delta_{i}$. For a simplified accrual interval of total length Δ, the compounded rate R and a caplet payoff H with notional N and strike K are defined by

$R = \frac{\prod_{i} (1 + r_{i}\delta_{i}) - 1}{\Delta}, \qquad H = N\Delta\,(R - K)^{+}.$

The positive part is max(R − K, 0). The actual implementation will specify observation shifts, calendars, day counts and payment delays using the applicable market conventions. If U is the payment date, D(t,U) the relevant collateral-consistent discount factor and $Q^{U}$ the associated payment-date forward measure, the model price is

$V_{\theta}(t) = D(t,U)\, E^{Q^{U}}\!\left[\, H \mid \mathcal{F}_{t} \right].$

Here θ indexes the model. The initial analysis will use a low-dimensional diffusion for the overnight-rate and legacy-basis factors with explicit admissibility and moment conditions. Historical loss probabilities will be evaluated under a physical measure P. Historical basis estimates will not be substituted for risk-neutral parameters without an identified or explicitly assumed change-of-measure relationship. Jump and multi-tenor extensions will follow only if the initial analysis is tractable.

# Probability measures information and admissibility

The mathematical model will be specified on a filtered probability space. The filtration represents information available through time, including published fixings and observed market quantities. A strategy must be predictable with respect to the selected information flow: it cannot use a future fixing, a future quote revision or a future realised loss to choose a current position. This requirement will be reflected directly in the chronology of the numerical implementation.

The physical measure P describes the distribution used for historical estimation and prospective hedge-loss analysis. A pricing measure Q, or a forward measure associated with a payment date, is used for valuation under the assumed market and collateral structure. Changing measure is a mathematical operation requiring stated conditions. It is not an instruction to replace an estimated drift with zero in every state equation.

## Pricing and conditional expectations

For a positive numeraire B, an admissible pricing measure makes the relevant traded gains, expressed in units of B, martingales under suitable integrability conditions. The associated valuation formula takes the discounted conditional expectation of the payoff. For a payment-date bond numeraire, this yields the caplet formula given earlier. The choice depends on the instruments and collateral convention actually included in the model.

The initial mathematical development will assume a simplified collateral and funding structure and state that assumption explicitly. Funding asymmetries, counterparty effects and multiple collateral currencies will not be introduced unless necessary to answer the central question. This restriction keeps attention on transition uncertainty rather than adding unrelated valuation adjustments.

## Integrability and trading constraints

Mean--variance hedging requires square-integrable terminal errors and an appropriate class of attainable gains. The proposal will specify these conditions for the chosen state process and payoff. A polynomial-looking payoff is not enough if its underlying can have tails that destroy the required moments. Numerical truncation will be recorded separately from a theorem's integrability assumption.

Admissibility will also encode position limits, financing restrictions and the prohibition of doubling strategies where relevant. In discrete experiments, positions will be bounded or otherwise regularised through a declared constraint. When a projection theorem requires a closed gain space, its closure conditions will be checked rather than assumed from the existence of a numerical least-squares solution.

## Learning the mathematics needed for this step

Mavuso's probability notes will support the progression from measurable functions and conditional expectation to martingales and stochastic integration. Shreve (2004) will connect these tools to pricing and changes of measure. Before advancing to the transition model, I will derive a discounted martingale pricing identity, explain its assumptions and reproduce it for a simple claim. This will establish the notation and reasoning on which the later identification and hedging arguments depend.

# A tractable initial transition model

The proposal needs a concrete starting family before it can ask whether parameters or prices are identified. I will begin with a low-dimensional Markov model containing an overnight-rate factor r and a spread factor b. As an analytical benchmark under a stated pricing measure, a two-factor Gaussian diffusion offers explicit covariance calculations and a tractable simulation scheme. It will be treated as an initial laboratory, with its limitations recorded.

$dr_{t}\  = \ (a(t)\  - \ \kappa r_{t})dt\  + \ \sigma\ d{W_{t}}^{r}.$

$db_{t}\  = \ (c(t)\  - \ \lambda b_{t})dt\  + \ \eta\ d{W_{t}}^{b}.$

$d\langle W^{r}, W^{b}\rangle_{t} = \rho\, dt.$

Here $W^{r}$ and $W^{b}$ are Brownian motions under the chosen pricing measure. The deterministic functions a and c control mean levels, κ and λ are positive mean-reversion constants, σ and η are volatility parameters, and ρ is a correlation between minus one and one. These dynamics are a proposed benchmark specification. The admissible parameter set will include conditions sufficient for the chosen valuation and hedging calculations.

## From factors to observable instruments

The equations alone do not define all traded contracts. I will specify how discount bonds, compounded overnight rates and legacy-tenor cashflows depend on the factors, and ensure consistency with the selected numeraire. A legacy forward rate will not simply be declared equal to r plus b unless that relation is justified in the chosen pricing construction. The complete observation map must price actual cashflows before calibration or identification is discussed.

Deterministic shifts may be used to fit initial curves where the model construction permits this. The analysis will distinguish parameters fixed by those curves from parameters constrained by option quotes or other instruments. In particular, fitting initial term structures does not by itself determine the covariance structure that drives future nonlinear payoffs.

## Model restrictions and extensions

A Gaussian benchmark permits negative rates and spread values. That feature will be assessed against the selected application and will not be hidden by truncating paths without changing the model. If a positivity-preserving model is needed, I will investigate an alternative with its own admissibility conditions. The analytical benchmark can still clarify which conclusions are structural and which depend on the chosen dynamics.

Historical dynamics under P will be estimated or stipulated separately. The relation between P and the pricing measure will require explicit market-price-of-risk assumptions. Event-related jumps, stochastic volatility and several tenors are possible extensions, but each increases the number of quantities that must be identified. Alfeus (2026) motivates examining scheduled-event effects in the South African application; its historical modelling role does not supply a ready-made pricing-measure identification argument.

# Identification and hedging methodology

## Market information and compatible models

Let O be the observations available at a valuation date and Λ(θ) the model-implied observation vector. The compatible set Θ(O) will contain admissible models whose prices lie within specified quote tolerances, preferably observed bid--ask ranges. Its definition will record instruments, maturities, timestamps and any regularity or parameter restrictions. Feasibility will be checked before computing price ranges.

$\Theta(O) = \{\theta \in \Theta : \Lambda(\theta) \text{ is compatible with } O\}.$

A valuation is identified if it is constant on Θ(O). Otherwise, its lower and upper compatible values are

$V_{-}\  = \ \inf_{\theta\  \in \ \Theta(O)}V_{\theta},\ \ \ \ \ \ \ V_{+}\  = \ \sup_{\theta\  \in \ \Theta(O)}V_{\theta}.$

These bounds form an identification range, not a statistical confidence interval. Existence, finiteness and attainment require separate conditions. Quote tolerances will not be assigned a confidence interpretation without a sampling model.

I will first attempt constructive non-identification examples: two admissible models with the same observation map and different target prices. Conversely, an identification result must show that the target is constant across the entire compatible set under its stated assumptions. Parameter counting and a good numerical fit are insufficient. If only small-parameter or short-maturity expansions are tractable, the theorem will specify the approximation order, strike and maturity domain, and a controlled remainder. Matching a finite number of moments will not be described as equality in distribution.

## Trading strategies and residual loss

The baseline strategy will trade on a fixed grid using instruments shown to be sufficiently liquid in the selected dataset. Discounted terminal wealth comprises initial capital, cumulative trading gains and transaction costs. Discounted liability minus terminal wealth defines signed hedging loss L; positive values indicate a shortfall. Admissible positions, financing, rebalancing and costs will be fixed before evaluation.

A conventional sensitivity hedge and a mean--variance hedge will provide the initial comparisons. The latter minimises expected squared loss under an explicitly chosen physical model, using projection methods where their assumptions apply. I will evaluate how the hedge changes across compatible pricing models. A worst-case objective over a stated model set is a possible extension, subject to tractability. An optional neural hedge will use the same information and trading constraints as the baseline.

The work will distinguish a policy fitted once and then held fixed from a policy recalibrated during trading. A statistical guarantee established for the former will not be transferred to the latter without accounting for adaptation and the resulting dependence.

# An illustrative non identification calculation

The following one-period example explains the information problem in a deliberately simplified setting. It is an analytical illustration, not a complete interest-rate model and not a claimed doctoral result. Let $Z_{1}$ and $Z_{2}$ be independent standard normal variables under a specified pricing measure. Define centred successor and basis shocks X and B, and a legacy shock Y, by

$X\  = \ \sigma Z_{1},\ \ \ B\  = \ \eta(\rho Z_{1}\  + \ \sqrt{1\  - \ \rho^{2}}Z_{2}),\ \ \ Y\  = \ X\  + \ B.$

Assume their means are already fixed by available linear instruments. The variance of the legacy shock is then

$\operatorname{Var}(Y) = \sigma^{2} + \eta^{2} + 2\rho\sigma\eta.$

If an idealised full legacy option surface identifies the normal distribution of Y with variance one, that observation gives one equation for the three covariance parameters. Consider two admissible choices with zero correlation. In model A, σ and η are both 1/√2. In model B, σ is 1/2 and η is √3/2. Both produce a standard normal legacy shock, so every integrable payoff depending only on Y has the same price in the two models under the common discounting assumption.

## The successor payoff differs

For a unit-notional, zero-strike call on X with unit discount factor, its value is σ/√(2π). Model A therefore gives approximately 0.2821 and model B approximately 0.1995. The agreement on the entire legacy distribution has not determined the value of this successor payoff. The difference comes from how the same legacy variance is allocated between successor and basis shocks.

$E\lbrack X^{+}\rbrack\  = \ \frac{\sigma}{\sqrt{2\pi}}.$

These calculations are dimensionless. They are not prices of actual South African contracts. They illustrate why observations of a sum can fail to identify the distribution of one component. If additional instruments identify the basis variance and its covariance with the successor factor, the conclusion can change. Additional data must therefore be represented in the observation map rather than mentioned informally.

## What the thesis must add

The thesis will need to translate this mechanism into an admissible transition model with realistic cashflow definitions, pricing measures and selected market observations. It must check whether the required parameter variation remains possible after curves, basis instruments, multiple maturities and any available options are included. If those restrictions remove the ambiguity, that is a substantive finding.

An exact counterexample must preserve the full chosen observation vector. Matching a few empirical moments or obtaining a small calibration error gives a different, approximate statement. The proposed research will maintain that distinction and investigate how observational noise widens the compatible set even when exact identification is possible.

# Identification stability and smile approximations

Identification concerns uniqueness relative to an observation map. Stability concerns how much the inferred target changes when observations are perturbed. These are different properties. A target may be uniquely identified in an idealised model but be highly sensitive to small quote errors, making its practical estimate unreliable. The proposed analysis will therefore examine both exact compatibility and compatibility within observed or declared tolerances.

## Local diagnostics and global statements

For a differentiable finite-dimensional model, the derivative of the observation map can reveal locally weakly constrained directions. Singular values and condition numbers provide numerical diagnostics. They do not establish global identification and may depend on parameter scaling. The analysis will use normalised parameters and inspect whether an apparently small singular value reflects an economic ambiguity or a numerical unit choice.

A local calculation can guide a constructive proof: move along a direction that changes the target while leaving observations unchanged to first order. To obtain an exact result, the argument must control higher-order terms or construct a curve of exactly compatible parameters. Alternatively, an approximate result must quantify the residual observation error. The distinction will appear explicitly in theorem statements and numerical reports.

## Price ranges before implied volatility ranges

The primary target will be a price functional because a price is defined directly from a payoff. An implied volatility is obtained by inverting a quoting formula and is meaningful only where that inversion exists and is sufficiently stable. At low vega, a small price difference can create a large implied-volatility difference. The empirical study will therefore report price errors alongside volatility errors and exclude or separately flag ill-conditioned inversions.

The phrase smile transport will describe a proposed relationship between legacy and successor option values or quoted volatilities. Such a relationship may be exact only in a restricted model, or it may be an approximation valid in a stated regime. The review of Willems (2020) and the chosen interest-rate framework will determine which interpretation is justified.

## Remainders and domains of validity

If an expansion uses a small basis-volatility parameter ε, the approximation must state whether the error is pointwise or uniform over a set of strikes and maturities. A formal second-order remainder without a bound does not establish an accurate price range. Numerical experiments will test the predicted error rate across successively smaller ε values, while recognising that such experiments supplement rather than replace a proof.

Far-from-the-money strikes, long maturities and near-degenerate correlations will be examined as possible failure regimes. Any proposed information loss must be qualified by the instruments actually observed: additional strikes or maturities can reveal distinctions that a short expansion suppresses. This analysis will determine whether the original manuscript's candidate smile statements should be retained, weakened or replaced.

# Pricing algorithms and numerical accuracy

The numerical implementation will use a hierarchy of calculations. Deterministic and zero-volatility cases will come first, followed by an analytically tractable stochastic benchmark, and then the full chosen transition model. This ordering provides reference values for diagnosing errors. A complicated calibration routine will not be used as the first test of the payoff and discounting code.

For path simulation, each contractual fixing will be generated or conditioned on according to its observation date. Known fixings will be stored as data. Unknown fixings will be simulated under the selected pricing measure, compounded using the contract's day fractions and converted into the terminal payoff. The average discounted payoff estimates the model price. Independent replications and Monte Carlo standard errors will quantify sampling error.

## Discretisation and calibration

Where exact transition simulation is available for the benchmark factors, it will be preferred. Otherwise, a stated numerical scheme will be evaluated under time-step refinement. Refining the simulation grid should leave contractual accrual conventions unchanged; a model discretisation step and a contract's fixing schedule are not the same object. Any bias from interpolation or curve construction will be assessed separately.

Calibration will match the observation vector using a declared weighting scheme. Bid--ask intervals, when available and credible, will define compatibility rather than an arbitrary requirement of exact midpoint fit. Multi-start optimisation and sensitivity checks will be used to distinguish a poor local solution from genuine model incompatibility. An empty feasible set will be reported as a failure of the combined model-and-tolerance specification.

## Computing compatible price ranges

The lower and upper target values require optimisation over the compatible set. A finite parameter grid can demonstrate variation and provide candidate extrema, but it does not certify a global bound. The implementation will report whether an endpoint is analytically proved, obtained through a globally justified procedure, or only the most extreme value found numerically. Parameter restrictions that make the set compact will be justified and subjected to sensitivity analysis.

Simulation noise can mislead an optimiser by making one parameter choice appear artificially attractive. Common random numbers may help compare nearby parameter values, but final candidate endpoints will be re-evaluated with fresh random numbers and adequate precision. Objective tolerances will be chosen with reference to numerical uncertainty and quote resolution.

The resulting computation record will include input curves, convention versions, parameter bounds, optimiser settings, random seeds and error estimates. This should make it possible to reproduce a reported range and identify which assumptions caused it to widen or narrow. A robust implementation is necessary for the empirical study, but numerical reliability alone does not establish identification or prove a sharp theoretical bound.

# Mean variance hedging and a projection benchmark

The first hedge benchmark will make the quadratic objective explicit. Let h denote the discounted terminal liability, x the initial discounted capital and G a vector of discounted terminal gains from a fixed set of admissible elementary strategies. Each component of G must be generated without future information. For a static combination with coefficient vector a, the loss is $h - x - a^{\top}G$, and the objective is its expected square under P.

$\min_{a}\ E^{P}\!\left[(h - x - a^{\top}G)^{2}\right].$

If the required second moments exist and the relevant matrix is invertible, differentiating this objective with respect to a gives the normal equations

$E^{P}\!\left[GG^{\top}\right] a = E^{P}\!\left[G(h - x)\right].$

The equation shows how the liability's relation to attainable gains determines the best quadratic approximation within the chosen linear class. If x is also optimised and the corresponding conditions hold, centring yields a covariance formulation. If the gain covariance is singular, the hedge coefficients may be non-unique; the attainable fitted payoff and the choice of regularisation must then be examined separately.

## What remains for a dynamic hedge

The simple projection calculation is a benchmark, not a complete solution of the dynamic problem. A dynamic policy may choose positions from current state variables at each trading date. Its gains depend on predictable decisions through time. The thesis will investigate projection or backward-regression methods under the assumptions appropriate to that model, drawing on Mavuso's treatment of mean--variance hedging and its trading constraints.

Discrete rebalancing and costs will be introduced after the frictionless benchmark is reproduced. Proportional or other documented transaction costs alter the optimisation and may make the frictionless normal equations inappropriate. The implementation will report the actual objective solved, its constraints and any approximation used to compute the policy.

## Estimation and evaluation

The expectations in the benchmark equations must be estimated from simulated or historical training data. A small training error can be misleading when the gain basis is large or nearly collinear. Regularisation and basis selection will therefore be confined to training and validation periods. The final hedge will be assessed on fresh paths or later dates, with the same notional and horizon as its comparators.

The hedge's residual squared error measures approximation and estimation under the chosen P model. Upper-tail loss, transaction costs and sensitivity to the pricing model will be reported separately. In particular, changing initial capital to match a different model price shifts the loss distribution. Comparisons will specify whether capital is held fixed across strategies or varied according to each model's valuation, because those choices answer different economic questions.

# Model uncertainty and optional learned hedges

The compatible pricing set can contain models that produce different sensitivities and therefore different hedges. The initial study will compare the strategies implied by a small, interpretable subset of compatible models. It will assess them on common evaluation scenarios so that changes in hedge behaviour can be separated from changes in the simulated market. A strategy's apparent success under the same model used to construct it is only one benchmark.

## A possible worst case formulation

A robust extension could minimise a worst-case quadratic loss over a declared set of physical laws. This set is distinct from the set of risk-neutral pricing models compatible with market quotes. The proposal will not identify the two sets without an explicit relationship between physical and pricing dynamics. That relationship may involve assumptions about risk premia that market observations alone do not determine.

$\inf_{\pi\  \in \ \Pi}\ \sup_{P\  \in \ \mathcal{P}}\ E^{P}\lbrack{L(\pi)}^{2}\rbrack.$

In this schematic objective, Π is the admissible strategy class and 𝒫 is a specified family of physical probability laws. Its mathematical treatment would require conditions for finite loss, existence of a minimiser and a justified numerical procedure. The initial thesis does not promise such a theorem. A tractable finite-scenario comparison will be used first to determine whether the extension resolves a core research question.

## A controlled role for machine learning

A neural hedge may approximate a map from current information to portfolio positions. Candidate inputs include time remaining, observed rates, accrued fixings and current instrument values. Inputs will exclude unavailable target option prices and future information. Position constraints and trading costs will be enforced consistently with the conventional hedge. Stangroom (2023) and Robbertze (2021) will guide the review of relevant learning-based methods.

Network architecture, training objective, random initialisation and tuning budget will be recorded. Comparisons will include repeated training runs so that optimisation instability is not mistaken for an economic effect. Training data generated under one model will be evaluated under alternative compatible models and deliberately misspecified dynamics. This assesses sensitivity to the simulator as well as flexibility within it.

## Keeping certification separate from selection

If several hedge policies are compared and the best is chosen using their calibration losses, a coverage statement proved for a preselected policy may no longer apply. The initial design will select and freeze the hedge before constructing the calibration threshold. A further untouched period will be reserved for evaluation. Any adaptive or continually retrained strategy will require its own analysis.

The learned hedge remains optional because the doctoral question concerns information and valid risk assessment. Its inclusion is justified only if it reveals a limitation or capability that a simpler strategy cannot answer. The project will avoid adding a neural component merely to increase the apparent complexity of the proposal.

# Statistical guarantees for hedging losses

The statistical object is an upper threshold for a future hedging loss at a specified horizon, rather than a guarantee that the option price is correct. Each score will be the signed loss of a stated hedge, measured in common discounted currency units or normalised by notional. Overlapping horizons will be recorded because they induce dependence even when daily returns have weak serial dependence.

## Baseline and proposed extension

The starting benchmark is split conformal calibration for a hedge fitted independently of its calibration sample. For n calibration losses and nominal error probability α, let k be the ceiling of (n + 1)(1 − α). The threshold q is the kth smallest calibration loss; when k exceeds n, it is defined as positive infinity. Under exchangeability of calibration and test scores, this construction has the usual finite-sample marginal guarantee, with conservative treatment of ties.

The research task is to derive and assess an appropriate extension for dependent losses and a changed test distribution. Blocking or spacing observations may control dependence, while a stated distance between calibration and test loss distributions may control shift. The intended form of a result is schematic:

$\Pr\{L_{\mathrm{new}} \leq q\} \geq 1 - \alpha - \varepsilon_{\mathrm{dep}} - \varepsilon_{\mathrm{shift}} - \varepsilon_{\mathrm{est}}.$

The terms represent dependence, distribution shift and any error introduced by estimating nuisance bounds. This display is a research target, not a proved theorem. A final result must define the probability space, sampling scheme, model class and constants. It must state whether it averages over the calibration sample or holds conditionally with an additional confidence probability. A calibration-conditional guarantee is also distinct from coverage conditional on every market state.

## Proof strategy and practical limits

I will begin with order-statistic arguments in the independent setting, then examine coupling or empirical-process bounds under a specified mixing condition. A shift penalty can be formulated through the distance between the relevant score distribution functions. Existing conformal results will be used directly where applicable; an original result must provide a demonstrable extension, sharper justified bound, or impossibility statement for the stated problem.

Neither arbitrary future distribution shift nor unrestricted dependence can be bounded from a short historical sample without assumptions. The study will therefore distinguish oracle experiments with known simulation parameters, assumption-based sensitivity analysis, and any empirically estimated bounds with their own uncertainty. A bound that is negative or requires an infinite threshold will be reported as uninformative. Marginal coverage, calibration-conditional coverage and empirical breach rates will be reported separately.

Beta-law arguments will be used only with the required continuity or tie-handling assumptions. Sharpness claims will require an explicit admissible construction and a specified class over which the bound is sharp. Numerical proximity to a bound alone will not establish sharpness.

# Exact calibration in an independent benchmark

Before studying dependence, I will reproduce the independent-score calculation. Fix a trained hedge and suppose its calibration losses $L_{1}$ through $L_{n}$ and the next loss are independent and identically distributed with continuous distribution function F. If q is the kth smallest calibration loss, then F(q) has a Beta distribution with parameters k and n + 1 − k, for k between 1 and n. This follows by applying the probability integral transform and the distribution of a uniform order statistic.

$F(q) \sim \mathrm{Beta}(k,\, n + 1 - k), \qquad E\!\left[F(q)\right] = \frac{k}{n + 1}.$

Conditional on the realised calibration sample, F(q) is the coverage probability of the threshold for an independent next loss. Averaging over calibration samples gives k/(n + 1). Selecting k as the ceiling of (n + 1)(1 − α) therefore provides marginal coverage at least 1 − α when the finite kth order statistic is available. Vovk (2012) and Ramos et al. (2026) provide relevant context for conditional validity and the Beta-law perspective.

## A finite sample example

Take n = 99 and α = 0.05. Then k = 95 and the threshold is the 95th smallest calibration loss. Its average coverage is 95/100 = 0.95 under the stated assumptions. However, the realised conditional coverage is a Beta(95,5) random quantity across calibration samples. It is not exactly 95 per cent for every sample. A lower quantile of that Beta law gives a lower confidence bound for the realised conditional coverage in this idealised setting.

If n is too small for the requested rank, the conformal construction uses an infinite threshold. For example, with n = 9 and α = 0.05, the required rank is 10. The inability to obtain a finite threshold is information about the sample size, not a reason to substitute the sample maximum and claim the same guarantee.

## Ties and the choice of score

Losses can contain ties because of rounding, limited payoff variation or a positive-part transformation that maps all surpluses to zero. In that case, the continuous probability-integral-transform argument does not directly supply the exact Beta law. The initial implementation will retain signed losses and document remaining ties. It will use a conservative order-statistic treatment or a justified randomised construction where appropriate.

This benchmark establishes the notation and provides a numerical check of the independent setting. It is not a new theorem. The research begins when the score process violates the benchmark assumptions through dependence, distribution shift, estimation or adaptation. Each extension will be compared to the exact calculation so that the source of any coverage loss is visible.

# Dependence blocking and effective information

The chronological loss sequence can be dependent for several reasons. Rate dynamics may persist, two hedge episodes may share the same market moves, and a recalibrated strategy may use overlapping estimation windows. The proposed analysis will describe the score process itself, rather than assume that a property of daily returns automatically transfers unchanged to multi-day hedging losses.

## A separated score design

The initial theoretical design will use a fixed hedge and scores separated by a declared gap. Where the score process satisfies a suitable absolute-regularity or beta-mixing condition, coupling can compare separated observations with independent counterparts. The dependence coefficient and its lag convention must be defined precisely, since different normalisations can alter constants in a displayed bound.

A useful proof template is to construct an independent comparison sample whose joint score vector differs from the actual vector with probability at most e. If the calibration rule is the same measurable function of both vectors, the probability of any coverage event differs by at most e. Combining this with an independent-score guarantee yields a lower bound of 1 − α − e, before any separate shift correction. This is a general proof strategy, not a claim of a new result.

The thesis must derive the relevant coupling error for its sampling scheme. A penalty informally written as a number of observations times a mixing coefficient will not be accepted without identifying the coupled blocks, gaps and any dependence between calibration and test scores. Oliveira et al. (2024), Barber et al. (2023), and Barber and Pananjady (2025, revised 2026) are central comparisons.

## The cost of separating observations

Larger gaps may reduce dependence while leaving fewer usable scores. A smaller sample increases order-statistic uncertainty and can force an infinite threshold at stringent nominal levels. The study will report this trade-off directly. It will compare several predeclared gap choices in simulation and select any empirical tuning rule without using the final test outcomes.

An illustrative count makes the constraint concrete: a sequence of 1,000 daily observations does not produce 1,000 independent one-month hedge outcomes. Overlapping outcomes share days, while non-overlapping outcomes yield far fewer episodes. The usable count depends on the exact horizon and sampling rule. The proposal will report both the number of market observations and the number of calibration episodes.

## Estimating what a theorem assumes

Mixing coefficients are properties of a probability law. Sample autocorrelations do not generally identify them. The empirical programme will distinguish known-coefficient simulation experiments, model-implied sensitivity ranges and any estimators whose assumptions can be justified. It will not convert a visually weak autocorrelation plot into an unrestricted finite-sample dependence guarantee.

# Distribution shift and sensitivity of loss thresholds

Let F describe a reference loss distribution and G the future loss distribution under a declared evaluation regime. If their distribution functions differ by at most d uniformly over thresholds, then G(q) is at least F(q) − d for any fixed q. This elementary inequality gives a transparent way to discuss test-side shift. Its practical usefulness depends entirely on whether a defensible upper bound for d is available.

$d = \sup_{z \in \mathbb{R}} |F(z) - G(z)|.$

$G(q)\  \geq \ F(q)\  - \ d.$

If a threshold is random, the same pointwise inequality can be averaged when the future loss has distribution G independently of that threshold. If future losses remain dependent on the calibration sample, that independence cannot be assumed; a conditional argument or an additional coupling step is required. The proposal will state which setting each bound addresses.

## Where a shift bound can come from

In simulation, the reference and test laws are controlled, so their distance can be computed or approximated with a separate error assessment. In an empirical application, future shift is unobserved. It may be restricted by an explicit model family, a prespecified scenario set or a justified statistical assumption. Without such restrictions, historical fit does not place a universal upper bound on a future distribution change.

The initial empirical analysis will therefore present a sensitivity curve over declared shift budgets. For each budget, it will show the resulting lower coverage bound and the range in which the claim remains informative. A scenario-based budget will be labelled as an assumption, not as an estimated fact. Any estimate from held-out future observations is a retrospective diagnostic and cannot retrospectively become an input available at the original decision time.

## Combining several uncertainty terms

Dependence, shift and nuisance estimation may contribute separate penalties only when the proof justifies their combination. The study will track the probability of each failure event and any allocation of confidence levels. It will avoid mixing a marginal guarantee with a high-probability calibration-conditional statement or omitting a confidence penalty when passing from one interpretation to another.

The statistical target is a defensible statement about loss coverage, not a promise of a small loss. A threshold can have adequate coverage while being economically unacceptable. The evaluation will therefore report threshold size in currency or notional units, the guaranteed coverage level and the empirical loss distribution together. When plausible assumptions produce a vacuous bound, the result will be described as an inability to certify the strategy under those assumptions.

Ramos et al. (2026) provides an especially relevant comparison because it distinguishes how test-side shift and calibration dependence affect the distribution of conditional coverage. The final novelty assessment will establish whether the proposed transition application requires any additional theoretical argument beyond that existing framework.

# Data design and validation

## Data audit and acquisition

During the first research phase, I will document accessible legacy option quotes, overnight fixings, discount and projection curves, basis quotes and hedge-instrument prices. Each series will be checked for timestamp alignment, tenor coverage, stale observations, missing values and licensing restrictions. The analysis requires contemporaneous inputs; combining quotes from different dates without a model for that mismatch would confound identification with data error.

Public fixings and official conventions can support parts of the South African case study, but they may not support a full option-pricing backtest. Access to option surfaces, executable hedge quotes and historical bid--ask spreads will be established with the supervisor and potential data providers. The audit will determine the historical sample, rather than selecting an arbitrary sample size in advance. SARB market conventions and relevant South African modelling work, including Alfeus (2026), will inform the application.

## Three complementary validation settings

**Controlled simulation** Generate data from specified transition models with known target prices and loss laws. Vary basis volatility, rate--basis dependence, maturity, strike, observation noise, transaction costs and regime changes. Include deliberately misspecified models. Numerical errors will be separated from statistical errors using Monte Carlo standard errors and time-step refinement.

**Retrospective validation** If an appropriate licensed dataset is obtained, hide successor option quotes while fitting models to the permitted legacy and curve information. Reveal those quotes only for evaluation. A historical LIBOR--SOFR dataset is a candidate, subject to availability and comparability of contracts. It will not be assumed that the South African findings transfer unchanged across currencies.

**South African application** Apply the framework to the instruments and dates supported by the audit. If successor option quotes are absent, report model-compatible valuation ranges, scenario sensitivity and observable hedge outcomes. Unobserved option prices cannot serve as empirical ground truth. Contract and spread conventions will be documented explicitly.

## Evaluation and prevention of information leakage

Chronological training, calibration and test periods will be fixed, with gaps where needed for the proposed dependence argument. Parameters, block lengths and competing strategies will be selected without using the final test period. Successor quotes withheld for validation will not enter calibration indirectly through model selection.

Pricing evaluation will report compatibility with observed quotes, range widths and sensitivity to model restrictions. Hedge evaluation will report mean squared error, upper loss quantiles, turnover and cost sensitivity. Certificate evaluation will report thresholds, theoretical lower coverage bounds, observed breaches and uncertainty calculated with a method justified for the remaining dependence. Results will be shown by regime and horizon as well as in aggregate. Economic usefulness requires finite, reasonably informative bounds; nominal coverage alone is insufficient.

# Simulation experiments and decision criteria

The simulation study will be organised around research questions rather than a large undirected grid of parameter combinations. Each experiment will specify the data-generating law, information supplied to calibration, target quantity, competing method and result that would support or challenge the proposed claim. Model parameters used to generate data will be kept separate from those estimated by the procedure.

## Identification experiments

The first experiment will compare parameter combinations that are exactly compatible in an analytical benchmark. It will check that the legacy observation vector agrees to the accuracy expected from the mathematics while successor prices differ. A second experiment will introduce quote tolerances and measure how the compatible range changes. A third will add selected instruments to test whether their information narrows that range in the way predicted by the analysis.

These experiments will distinguish the true compatible range in a tractable benchmark from the range found by a numerical search. Failure to find a second model is not evidence of identification. Conversely, a reported second model must satisfy all admissibility and observation constraints rather than only fit a subset of quotes.

## Hedging and coverage experiments

Hedge comparisons will begin under correctly specified dynamics with no costs, then introduce discrete trading, transaction costs, parameter estimation and misspecification in stages. Common evaluation paths will support paired comparisons. Strategies will use the same initial capital when the purpose is to compare trading performance; a separate analysis will examine the consequences of model-specific initial valuations.

Coverage experiments will first reproduce the independent-score benchmark, then vary dependence and shift separately before combining them. The design will include regimes where the theoretical bound is expected to be loose or uninformative. It will also include ties and overlapping horizons to test assumptions that can be hidden in an idealised continuous simulation.

## Precision and reporting

For independent simulation replications, the standard error of an estimated coverage proportion can be assessed using its binomial sampling variability. For example, at a true coverage near 0.95, 10,000 independent replications yield a standard error of approximately 0.00218. This is an illustration for planning computational precision, not a claim that 10,000 replications are always necessary or sufficient. Runtime and the required discrimination between methods will determine the final count.

Each table will report Monte Carlo uncertainty, sample size, horizon and parameter regime. A small observed difference between methods will not be interpreted without reference to that uncertainty. Numerical convergence, coverage and economic performance are distinct outcomes. A method will be considered practically informative only if its bound is valid under the stated design and its threshold or valuation range is sufficiently narrow to answer the research question.

# Empirical sample construction and historical testing

The empirical study will begin with an inventory rather than a promised date range. For every series, I will record the provider, field definition, timezone, publication time, currency, tenor, frequency, units, revision policy and licence. Option data will also require strike, expiry, underlying maturity and quoting convention. This inventory determines whether the available observations can support the proposed research design.

## Building contemporaneous observations

Curves and option quotes must describe a coherent valuation time. A quote available after the hedge decision cannot be treated as information known at that decision. Stale quotes, calendar mismatches and inconsistent day counts can create apparent model discrepancies unrelated to the transition. Cleaning rules will therefore be documented before model comparisons and applied consistently across competing methods.

Missing values will be classified by cause where possible. An absent quote can indicate a non-traded instrument, a data-vendor omission or a temporary market gap. Those cases have different implications for the observation map. Interpolation will be used only with a stated purpose and sensitivity check. An interpolated option surface will not be described as independent market evidence at every strike.

## Chronological separation and a locked test period

The sample will be divided chronologically into training, method-selection, calibration and final evaluation periods where the data length permits. The training period fits model or hedge parameters. The method-selection period determines permitted tuning choices. The calibration period constructs the loss threshold. The final period evaluates the frozen procedure. Any departure from this separation will be justified explicitly.

Rolling evaluation may be useful for studying changing regimes, but it changes which objects are fixed and which are re-estimated. The protocol will state how frequently curves, model parameters, hedge policies and thresholds are updated. An adaptive procedure will not inherit a fixed-policy theorem merely because each update resembles the original algorithm.

## What can be claimed from each dataset

With suitable successor option quotes, a retrospective study can compare predicted valuations with withheld market information. Without them, the study can still assess compatibility with observed instruments, scenario sensitivity and the cashflows of implementable hedges. It cannot estimate a pricing error against a market value that was never observed. Where liability settlement is observable but intermediate option quotes are absent, terminal hedge loss and intermediate mark-to-market accuracy must also be distinguished.

The South African application and any historical LIBOR--SOFR comparison will be analysed as separate settings before drawing common conclusions. Different contracts, liquidity and market conventions may explain different results. The report will disclose these limitations and avoid treating one currency's successful validation as proof that a model is identified or correctly priced in another.

# Reproducibility research risks and contingency plans

The research record will separate source data, cleaned observations, model configuration, fitted parameters and reported results. Every result should be traceable to a script, a configuration and an identifiable data version. Public or synthetic examples will be provided where licensing prevents redistribution of the original observations. Reproducibility will not require releasing confidential market data without permission.

## Mathematical verification

Each proposed theorem will have an assumption list, a proof outline and a record of unresolved steps. Imported results will be cited at the point of use, and their hypotheses checked against the current model. Boundary cases, degeneracies and counterexamples will be examined before generalising a numerical pattern. A proof that establishes an approximate statement will not be presented as exact after its remainder is omitted.

The supplied AI-assisted manuscript will be audited claim by claim. Its equations, citations and computational descriptions are prompts for investigation, not evidence of completed verification. Where code is unavailable, a statement about a numerical experiment will be reproduced independently or removed from the claimed evidence. The candidate must be able to explain every retained definition, assumption and inference without relying on generated text.

## Main risks and responses

Data access is a central feasibility risk. If licensed option or hedge data cannot be obtained, the empirical design will be reduced to observations that can be supported, with simulation carrying the controlled validation. The supervisor will then reassess whether the remaining theoretical contribution and application are sufficient for the intended doctorate.

Novelty is a separate risk. If the statistical result follows directly from existing conformal theory, it will be presented as an application and the original contribution must lie elsewhere or be reformulated. If the identification theorem fails, the project will investigate whether a precise counterexample, partial result or alternative observation set answers a useful question. The response will be to revise the claim, not to relax its wording until it becomes unfalsifiable.

Computational complexity will be managed by starting with caplets and a small factor model. Additional tenors, jumps and learned policies will be added only after the baseline results are stable. A failure to obtain a useful certificate is also a possible research outcome; the study will explain which assumptions or sample constraints make it uninformative.

## Ethics authorship and dissemination

The initial design involves market data and simulation rather than recruited participants. The applicable institutional ethics or exemption process will still be checked. Data licences, attribution and the treatment of confidential information will be documented. AI assistance will be disclosed according to institutional requirements, with responsibility for the final claims remaining with the candidate. Dissemination will distinguish proved results, numerical evidence and unresolved conjectures, and any paper arising from the thesis will describe its contribution and limitations directly.

# Expected contribution feasibility and work plan

The proposed contribution has two linked parts. The first is a rigorous identification analysis for a restricted benchmark-transition model and observation set. The second is a justified analysis of loss thresholds for implementable hedges under specified dependence and shift. Both contributions remain conditional on the literature audit and successful proofs. A South African implementation is an application contribution; geographic novelty alone will not establish the mathematical or statistical originality required for the doctorate.

The initial thesis will focus on caplets, a small factor system and conventional hedges. Swaptions, large portfolios, jump extensions and neural strategies will be added only where they resolve a core research question. If broad identification fails, a precise non-identification theorem and justified bounds may still be a useful outcome. If historical option data cannot be acquired, the empirical claims will be reduced and the resulting thesis scope reassessed with the supervisor.

## Indicative full time schedule

  --------------------------------------------------------------------------------------------------------------------------------
   **Months**  **Work**                                          **Evidence of progress**
  ------------ ------------------------------------------------- -----------------------------------------------------------------
      1--6     Foundations, novelty review and data audit        Approved scope; data inventory; reproduced baseline

     7--14     Transition model and identification               Proofs or counterexamples; stable valuation code

     15--22    Hedging and statistical analysis                  Defined hedge policies; proved or revised bounds

     23--29    Simulation and empirical evaluation               Controlled comparisons; documented limitations

     30--36    Synthesis, revision and examination preparation   Coherent thesis; reproducible results; oral defence preparation
  --------------------------------------------------------------------------------------------------------------------------------

This is a planning assumption, not a statement about an approved registration period. Reading, writing and supervisor review will continue throughout. The end of month 6 is the first decision point: confirm data access, the restricted model and at least one plausible original result before expanding implementation.

## Resources research practice and costs

The core resources are supervision in stochastic finance and mathematical statistics, scientific computing software, a workstation and suitable financial datasets. Data licensing and any additional computing costs will be priced before the final budget is submitted. No funding or vendor access is assumed in this draft.

Code, configurations, seeds and synthetic data will be versioned. Licensed data will be stored and shared only as permitted. The project initially proposes no human-participant research; institutional ethics or exemption requirements will be checked for the final design. The existing manuscript and this proposal were prepared with AI assistance. Their contents require the candidate's independent verification, attribution and understanding; the final disclosure will follow the applicable institutional requirements.

# Provisional thesis structure and preparation

The proposed ten chapters will form a connected argument. Their final length and allocation will follow the results obtained; the chapter count does not establish doctoral depth.

  ----------------------------------------------------------------------------
   **Chapter**  **Subject**
  ------------- --------------------------------------------------------------
        1       Introduction and research questions

        2       Benchmark reform incomplete markets and model risk

        3       Mathematical and statistical preliminaries

        4       Modelling a benchmark transition

        5       Identifiability of successor rate volatility smiles

        6       Pricing and hedging under model uncertainty

        7       Finite sample guarantees for hedging errors

        8       Sharpness stability and numerical verification

        9       Empirical evaluation and the JIBAR ZARONIA application

       10       Conclusions limitations and further research
  ----------------------------------------------------------------------------

Chapter 8 will claim sharpness only where proved. Technical lemmas, implementation details and supplementary experiments will move to appendices when they interrupt the argument. Chapters 5 and 7 are the initial locations for the proposed original results.

## Preparation for independent research

I will begin with Mavuso's UCT probability notes, progressing from random variables and conditioning to measure theory, martingales and stochastic integration. Shreve (2004) will connect these ideas to no-arbitrage pricing, followed by Brigo and Mercurio (2006) for interest-rate models. The next stage is to reproduce a caplet pricing calculation, a basic mean--variance hedge and an independent-sample conformal threshold before studying the transition extensions.

For each central paper, I will record its question, assumptions, principal result, proof technique and relevance to the proposed claim. Every theorem imported into the thesis must have its assumptions checked in the new setting. Every proposed theorem will have a separate proof record identifying established steps, unresolved steps and counterexamples. This preparation is part of the feasibility plan and will inform any revision of the indicative schedule.

## Items to resolve before submission

The supervisor and candidate must settle the precise model class, data access, institutional academic home and novelty statement. The School's current proposal template and length requirements must also be confirmed. The structure here follows the substantive proposal elements in the Wits Faculty of Science standing orders (2021), including aims, critical literature, specific problems, methods, work plan and thesis outline; it is not presented as an official Wits template.

# References

This list covers the literature, market documentation and supplied manuscripts underpinning the proposed programme. It is not restricted to works cited in the body: it records the sources against which the proposed identification and inference claims must be positioned. Supplied manuscripts and dissertations are distinguished from journal articles and preprints, and local dissertations are included for context and method rather than as evidence of the proposed results. Bibliographic details for entries added from the supplied reference list have not yet been independently verified against the sources themselves.

Adams, Terrence M., and Nobel, Andrew B. (2010). Uniform convergence of Vapnik--Chervonenkis classes under ergodic sampling. Annals of Probability, 38(4), 1345--1367.  <!-- adams2010 -->

Alfeus, Mesias (2024). Navigating the JIBAR transition: progress, impacts, readiness, and analytical insights. South African Journal of Science, 120(3/4), Art. #17841.  <!-- alfeus2024 -->

Alfeus, Mesias (2026). Event-aware jump-diffusion for the JIBAR--ZARONIA spread. South African Reserve Bank Working Paper WP/26/06.  <!-- alfeus2026 -->

Allohibi, Jamal (2026). Conformal prediction intervals for semi-functional partial linear regression under beta-mixing dependence. Mathematics, 14(17), 3201.  <!-- allohibi2026 -->

Barber, Rina Foygel, Candès, Emmanuel J., Ramdas, Aaditya, and Tibshirani, Ryan J. (2023). Conformal prediction beyond exchangeability. Annals of Statistics, 51(2), 816--845.  <!-- barber2023 -->

Barber, Rina Foygel, and Pananjady, Ashwin (2026). Predictive inference for time series: why is split conformal effective despite temporal dependence? Proceedings of the 37th International Conference on Algorithmic Learning Theory, 313, 1--24. arXiv:2510.02471.  <!-- barber2026 -->

Basel Committee on Banking Supervision (2019). Minimum capital requirements for market risk. Bank for International Settlements. Standard d457.  <!-- bcbs2019 -->

Berbee, Henry C. P. (1979). Random Walks with Stationary Increments and Renewal Theory. Mathematisch Centrum.  <!-- berbee1979 -->

Bloomberg Index Services Limited (2025). IBOR Fallbacks: Spread Fixing Event for ZAR JIBAR. Bloomberg Index Services Limited Technical Note.  <!-- bisl2025 -->

Bobkov, Sergey, and Ledoux, Michel (2019). One-dimensional empirical measures, order statistics, and Kantorovich transport distances. Memoirs of the American Mathematical Society, 261(1259).  <!-- bobkov2019 -->

Brace, Alan, Gellert, Karol, and Schlögl, Erik (2024). SOFR term structure dynamics: discontinuous short rates and stochastic volatility forward rates. Journal of Futures Markets, 44(6), 936--985.  <!-- brace2024 -->

Brigo, Damiano, and Mercurio, Fabio (2006). Interest Rate Models: Theory and Practice. 2nd edition. Springer.  <!-- brigo2006 -->

Christoffersen, Peter F. (1998). Evaluating interval forecasts. International Economic Review, 39(4), 841--862.  <!-- christoffersen1998 -->

Dedecker, Jérôme, and Merlevède, Florence (2017). Behavior of the Wasserstein distance between the empirical and the marginal distributions of stationary alpha-dependent sequences. Bernoulli, 23(3), 2083--2127.  <!-- dedecker2017 -->

Doukhan, Paul (1994). Mixing: Properties and Examples. Springer.  <!-- doukhan1994 -->

Dvoretzky, Aryeh, Kiefer, Jack, and Wolfowitz, Jacob (1956). Asymptotic minimax character of the sample distribution function and of the classical multinomial estimator. Annals of Mathematical Statistics, 27(3), 642--669.  <!-- dkw1956 -->

Feng, Y., Rudd, R., Baker, C., Mashalaba, Q., Mavuso, M., and Schlögl, E. (2018). Quantifying the Model Risk Inherent in the Calibration and Recalibration of Option Pricing Models. arXiv:1810.09112. [Source](https://arxiv.org/abs/1810.09112)  <!-- feng2018 -->

Filipovic, Damir (2009). Term-Structure Models: A Graduate Course. Springer.  <!-- filipovic2009 -->

Fournier, Nicolas, and Guillin, Arnaud (2015). On the rate of convergence in Wasserstein distance of the empirical measure. Probability Theory and Related Fields, 162(3--4), 707--738.  <!-- fournier2015 -->

Frey, Rüdiger, and Sin, Carlos A. (1999). Bounds on European option prices under stochastic volatility. Mathematical Finance, 9(2), 97--116.  <!-- frey1999 -->

Geman, Hélyette, El Karoui, Nicole, and Rochet, Jean-Charles (1995). Changes of numéraire, changes of probability measure and option pricing. Journal of Applied Probability, 32(2), 443--458.  <!-- geman1995 -->

Gibbs, Isaac, and Candès, Emmanuel J. (2021). Adaptive conformal inference under distribution shift. Advances in Neural Information Processing Systems, 34.  <!-- gibbs2021 -->

Gibbs, Isaac, Cherian, John J., and Candès, Emmanuel J. (2025). Conformal prediction with conditional guarantees. Journal of the Royal Statistical Society Series B, 87(4), 1100--1126. arXiv:2305.12616, 2023.  <!-- gibbs2025 -->

Hagan, Patrick S., Kumar, Deep, Lesniewski, Andrew S., and Woodward, Diana E. (2002). Managing smile risk. Wilmott Magazine, 84--108.  <!-- hagan2002 -->

Halkiewicz, S. M. S. (2026). Rolling-origin conformal prediction under local stationarity and weak dependence. arXiv:2605.08422.  <!-- halkiewicz2026 -->

Henrard, Marc (2014). Interest Rate Modelling in the Multi-Curve Framework. Palgrave Macmillan.  <!-- henrard2014 -->

Hoeffding, Wassily (1963). Probability inequalities for sums of bounded random variables. Journal of the American Statistical Association, 58(301), 13--30.  <!-- hoeffding1963 -->

International Swaps, and Derivatives Association (2025). JIBAR Cessation Guidance. International Swaps and Derivatives Association.  <!-- isda2025 -->

Karatzas, Ioannis, and Shreve, Steven E. (1991). Brownian Motion and Stochastic Calculus. 2nd edition. Springer.  <!-- karatzas1991 -->

Konaite, T. T. (2024). Pricing Interest Rate Derivatives Using the Forward Market Model. MSc dissertation, University of the Witwatersrand. [Source](https://wiredspace.wits.ac.za/server/api/core/bitstreams/2bab31c0-e118-479b-b66b-a8b1ae8cf291/content)  <!-- konaite2024 -->

Kupiec, Paul H. (1995). Techniques for verifying the accuracy of risk measurement models. Journal of Derivatives, 3(2), 73--84.  <!-- kupiec1995 -->

Künsch, Hans R. (1989). The jackknife and the bootstrap for general stationary observations. Annals of Statistics, 17(3), 1217--1241.  <!-- kunsch1989 -->

Lahiri, Soumendra N. (2003). Resampling Methods for Dependent Data. Springer.  <!-- lahiri2003 -->

Lyashenko, Andrei, and Mercurio, Fabio (2019). Looking forward to backward-looking rates: a modeling framework for term rates replacing LIBOR. SSRN 3330240.  <!-- lyashenko2019 -->

Lyashenko, Andrei, and Mercurio, Fabio (2020). Libor replacement II: completing the generalized forward market model. Risk.  <!-- lyashenko2020 -->

Massart, Pascal (1990). The tight constant in the Dvoretzky--Kiefer--Wolfowitz inequality. Annals of Probability, 18(3), 1269--1283.  <!-- massart1990 -->

Mavuso, M. M. (2014). Mean--Variance Hedging in an Illiquid Market. MPhil dissertation, University of Cape Town. Supplied copy dated October 2014; declaration dated April 2015. Final catalogue year to be confirmed.  <!-- mavuso2014 -->

Mavuso, Melusi (2019). Order out of Chaos I. STA2004F probability notes, University of Cape Town. Dated 15 March 2019; local copy References/Books/OrderOutOfChaos2019.pdf.  <!-- mavuso2019a -->

Mavuso, Melusi (2019). Order out of Chaos II. STA3045F probability theory notes, University of Cape Town. Dated 26 March 2019; local copy References/Books/ProbabilityTheory.pdf.  <!-- mavuso2019b -->

Menziwa, S. (2023). Pricing, Calibration and Hedging under the LIBOR Model. MPhil dissertation, University of Cape Town. [Source](https://open.uct.ac.za/bitstreams/acccbc0c-6956-4713-aadf-5e8828b7a4c2/download)  <!-- menziwa2023 -->

Oliveira, Roberto I., Orenstein, Paulo, Ramos, Thiago, and Romano, João Vitor (2024). Split conformal prediction and non-exchangeable data. Journal of Machine Learning Research, 25(225), 1--38.  <!-- oliveira2024 -->

Piterbarg, Vladimir (2020). Interest rates benchmark reform and options markets. SSRN 3537925.  <!-- piterbarg2020 -->

Politis, Dimitris N., and Romano, Joseph P. (1994). The stationary bootstrap. Journal of the American Statistical Association, 89(428), 1303--1313.  <!-- politis1994 -->

Ramos, T. R., Graziadei, H., and Cabezas, L. M. C. (2026). Conformal prediction via transported beta laws. arXiv:2605.19024.  <!-- ramos2026 -->

Rio, Emmanuel (2017). Asymptotic Theory of Weakly Dependent Random Processes. Springer.  <!-- rio2017 -->

Robbertze, Y. (2021). Neural Network LIBOR Market Model for Pricing and Hedging Interest Rate Derivatives. Master's thesis, University of Cape Town. Supplied copy dated 13 December 2021.  <!-- robbertze2021 -->

Ross, Nathan (2011). Fundamentals of Stein's method. Probability Surveys, 8, 210--293.  <!-- ross2011 -->

Schmitt, M. (2026). Taming tail risk in financial markets: conformal calibration for nonstationary portfolio VaR. arXiv:2602.03903.  <!-- schmitt2026 -->

Shreve, Steven E. (2004). Stochastic Calculus for Finance II: Continuous-Time Models. Springer. [Source](https://link.springer.com/book/9780387401010)  <!-- shreve2004 -->

South African Reserve Bank, Market Practitioners Group, Derivatives Workstream (2025). Historical Estimation of the ZARONIA OIS Curve. South African Reserve Bank.  <!-- sarb2025ois -->

South African Reserve Bank, Market Practitioners Group, Derivatives Workstream (2025). Market Conventions for ZARONIA-Based Non-Linear Derivatives. South African Reserve Bank Final draft. Consultation draft November 2024; Excel model corrected 4 August 2025.  <!-- sarb2024conv -->

South African Reserve Bank, Market Practitioners Group (2025). Jibar Transition and Fallback Credit Adjustment Spreads for the South African Market: MPG Final Recommendation. South African Reserve Bank.  <!-- sarb2025fallback -->

Stangroom, J. (2023). Deep Hedging in Incomplete Markets. MSc dissertation, University of Cape Town. [Source](https://open.uct.ac.za/bitstreams/053a1375-ae27-4302-a1b1-6dc68dbb5ccc/download)  <!-- stangroom2023 -->

Stocker, M., Małgorzewicz, W., Fontana, Matteo, and Ben Taieb, Souhaib (2025). A gentle introduction to conformal time series forecasting. arXiv:2511.13608.  <!-- stocker2025 -->

Taipe-Silvestre, M. (2022). Tuning the FMM-SABR for RFR caplets. SSRN 4046344.  <!-- taipe2022 -->

Tsybakov, Alexandre B. (2009). Introduction to Nonparametric Estimation. Springer.  <!-- tsybakov2009 -->

Turfus, Colin, and Romero-Bermudez, Alexander (2023). Analytic risk-free rates option pricing with smile and skew. Risk. Cutting Edge, September 2023. arXiv:2301.01260; SSRN 4309981.  <!-- turfus2023 -->

van der Vaart, Aad W., and Wellner, Jon A. (1996). Weak Convergence and Empirical Processes. Springer.  <!-- vdv1996 -->

Vovk, Vladimir, Gammerman, Alexander, and Shafer, Glenn (2005). Algorithmic Learning in a Random World. Springer.  <!-- vovk2005 -->

Vovk, Vladimir (2012). Conditional validity of inductive conformal predictors. Proceedings of the Asian Conference on Machine Learning, 25, 475--490.  <!-- vovk2012 -->

Willems, Sander (2020). SABR smiles for RFR caplets. arXiv:2004.04501.  <!-- willems2020 -->

Xu, R., Chen, C., Sun, Y., Venkitasubramaniam, P., and Xie, S. (2025). Wasserstein-regularized conformal prediction under general distribution shift. Proceedings of the International Conference on Learning Representations (ICLR 2025). arXiv:2501.13430.  <!-- xu2025 -->

Yu, Bin (1994). Rates of convergence for empirical processes of stationary mixing sequences. Annals of Probability, 22(1), 94--116.  <!-- yu1994 -->

Zheng, Frédéric, and Proutiere, Alexandre (2024). Conformal predictions under Markovian data. Proceedings of the 41st International Conference on Machine Learning, 235, 61470--61497.  <!-- zheng2024 -->

Zwart, P. H. (2025). Probabilistic conformal coverage guarantees in small-data settings. arXiv:2509.15349.  <!-- zwart2025 -->


## Source manuscript

Baloyi, T. B. J. (2026). Pricing and Hedging Through a Benchmark Transition Without an Options Market. Supplied AI-assisted draft manuscript, main.pdf. Used to formulate candidate research questions; not cited as evidence that its proposed results have been proved.
