# Five-dimensional kissing number — research ledger

**Status (2026-10-09): OPEN.** Established global range: **40 ≤ τ₅ ≤ 44**. No claim that τ₅ = 40 is proved.

This repository starts with a *provenance-conscious mathematical audit*, not a completed proof. The full derivations and scripts are retained in the research correspondence; this ledger identifies statements that still need upstream certification.

## Consolidated baseline (2026-09-05; retained, not independently reproved here)

- A hypothetical 41-code has triangle-free deep graph G with α(G)≤20 and e(G)≥23. Sparse e=23/24 classifications **require** δ(G)≥1.
- Isolated-center graph H=G−x₀ has 40 vertices, α(H)≤19, e(H)≥25; e=25 and e=26 types A,B are excluded. Types C,D,E and e≥27 remain open.
- Type E: H=16K₂ ⊔ F₃. Retained exact mass inequalities: star sum ≤70/3; M(F₃)≤89; some F₃ matching P satisfies M(P)≥S/2−28/3; twenty deep edges total mass ≥2137/6, yielding A=Σ||mᵢ||²≤383/504.
- The zero-midpoint, 21-line boundary is excluded using Musin (2008), §5 and Boyvalenkov (1993); **do not** assert D₅ uniqueness.
- Of 190 pairings, 184 are safe and at most six F₃ core pairings may exceed projective correlation 1/2. Retained raw positive defect ≤1780062775/4032758016; homogeneous bound ≤5792292955405/4129544208384.
- Uniform two-sided three-point SDP at μ=1/2 saturates 21 (degrees 4/4 through 6/6); not a viable primary separation route.
- D₅ Q-Gram rank 14, nullity 6. Six zero eigenvalues are automatic dimension counting for 20 vectors in Sym₀(5), **not** evidence identifying six exceptional pairings.

## Audit (2026-10-09)

**CHECKED algebraically/exhaustively within the audit:** a singleton F₃ cross-contact has positive raw defect ≤1/8, while a double-contact pair has bound ≤1/4; for the ten-edge F₃ matching representative, the three perfect matchings have patterns (1,1,1,1,1,1) and two copies of (0,1,1,1,1,2). The capped-defect convex envelopes are ≈0.064340215418 (all-singleton) and ≈0.122445684168 (double pattern). The midpoint-energy envelope estimates are E₋≤243 A_C²/512 and E₋≤75 A_C²/128 respectively.

**CONDITIONAL implications:** combining the upstream energy ceiling, raw-defect cap, and claimed twenty-direction Q-rank floor L=31747673717745523/57813618917376000 gives safe-plus-subthreshold squared-deficit lower estimates ≈0.484798107217 (all-singleton) and ≈0.426692638467 (double). These are **not** independent proofs of the upstream hypotheses.

**OPEN / verification needed:** independently reproduce the full upstream energy and defect certificates and the refined spectral interlacing estimate; derive an incidence-sensitive *upper* bound contradicting the necessary squared-deficit floor, or find another exact obstruction. Types C,D and generic e≥27 remain open.

**Historical caution:** do not regress to superseded claims M(F₃)≤94 or M(P)≥S/2−343/32.

This ledger is deliberately conservative. A passing arithmetic script does not prove its geometric assumptions.
