# Proposed PhD topic (candidate's own title)

## Title
A SABR Extension of the Forward Market Model: Smile-Consistent Calibration for the Transition from JIBAR to ZARONIA

## Brief (inferred from the title by the council secretary; the candidate supplied only the title)
South Africa is replacing JIBAR (Johannesburg Interbank Average Rate, a forward-looking term rate) with ZARONIA (South African Rand Overnight Index Average, a backward-looking overnight rate compounded in arrears), under the SARB Market Practitioners Group programme. The Forward Market Model (FMM) of Lyashenko and Mercurio (2019, "Looking Forward to Backward-Looking Rates") generalises the LIBOR Market Model to handle backward-looking compounded setting-in-arrears rates, with the forward rate's volatility decaying to zero across the accrual period. Standard FMM is lognormal or shifted-lognormal and does not produce a volatility smile. The thesis would (i) extend the FMM with SABR-type stochastic volatility for each forward (compounded) rate, deriving the appropriate in-accrual-period volatility decay for both the rate and its stochastic volatility, (ii) derive smile-consistent approximations (Hagan-type expansions) for caplets, floorlets and swaptions on backward-looking compounded ZARONIA rates, (iii) build a smile-consistent joint calibration to the existing JIBAR cap/swaption volatility surface and the emerging ZARONIA-linked instruments (OIS, basis swaps), transporting the JIBAR smile to the ZARONIA world through the JIBAR-ZARONIA basis and fallback spread, and (iv) apply this to valuation and risk of legacy JIBAR-linked derivatives through the transition, using South African market data.

## Claimed gap (as the candidate would presumably claim it)
- FMM literature is dominated by USD SOFR, GBP SONIA and EUR ESTR; no published treatment for ZAR / ZARONIA.
- SABR extensions of the FMM exist in sketch form but a full smile-consistent, multi-curve calibration through a benchmark transition is not published.
- The JIBAR to ZARONIA transition has features unlike LIBOR to SOFR: a much smaller and less liquid derivatives market, a long-standing JIBAR-linked cap/floor and swaption market that must be transported to a rate with no options market yet, and a SARB-driven timeline.

## Candidate research questions
1. What is the correct SABR dynamics for a backward-looking compounded forward rate inside its accrual period (decay of both alpha and the rate's volatility, behaviour of the effective beta and rho), and does a closed-form or asymptotic implied-volatility formula exist?
2. How should a JIBAR smile be transported to ZARONIA-linked options when no ZARONIA options trade, given the basis, the fallback spread and the term-rate versus compounded-rate convexity difference?
3. Can the extended model be jointly calibrated to JIBAR caps/swaptions and ZARONIA OIS/basis swaps with stable parameters through the transition window?
4. What is the valuation and hedging impact on legacy JIBAR-linked exotics (caps, swaptions, range accruals) of the transition under the smile-consistent model versus the lognormal FMM?

## Candidate methods
Forward Market Model (Lyashenko-Mercurio 2019, 2020), SABR and its asymptotics (Hagan et al. 2002; Hagan, Lesniewski, Woodward; Antonov free-boundary/ mixture SABR), SABR-LMM (Rebonato, McKay, White; Hagan-Lesniewski LMM-SABR), multi-curve framework (Henrard; Bianchetti), RFR option pricing (Piterbarg 2020; Willems 2020; Turfus), ZAR market data from JSE / Bloomberg / SARB.

## Context of candidate
Completing an MSc in Mathematical Statistics (UFS, South Africa), works as an AI engineer. Wants a topic that is novel, mathematically serious, feasible in 3-4 years, and grounded in the South African market.
