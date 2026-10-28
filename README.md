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

## New exact F3 all-singleton matching lemma (2026-10-10)

**PROVED for a specific matching, not a Type-E elimination:** For the perfect matching `04|17|23|56` of the ten-edge F3, oriented as `(0,4),(7,1),(2,3),(5,6)`, the six remaining deep contacts each link different matched pairs with matching endpoint signs. For its four midpoints, let `C=Σ||m_i||²` and `N=Σ_{i<j}(-m_i·m_j)_+`. The analytic signed-Gram and Cauchy–Schwarz argument proves `C−N > 1/[24(4−C)] ≥ 1/96`. An optional improvement `C−N>125/11802` depends on a separate, not independently recertified `C>33/500` lemma.

**Crucial limitation:** the F3 Delsarte-mass theorem chooses some perfect matching, which need not be this all-singleton matching. **No** transfer to the mass-selected 20-edge bound or Type-E exclusion is claimed. See [the full proof](research/tau5_typeE_F3_singleton_signed_gram_stability_2026-10-10.md) and [the rational checker](research/tau5_typeE_F3_singleton_signed_gram_stability_2026-10-10.py). The global proved range is still `40≤τ₅≤44`.

## Current Type-E research checkpoint (2026-10-28)

**PROVED EXACTLY (algebra; Type-E consequences conditional on retained graph/mass/endpoint lemmas):** A full frame/safe-mixing SOS identity now retains the isolated fourth energy `U_I`, the nonnegative midpoint-wedge dispersion `Omega`, the core-orthogonality slack and the 184-safe-pair residual. The scalar mass-concavity inputs give `A <= Astar ≈ 0.6510370131` and `U <= Ustar ≈ 0.1389603132`, with an exact stability inequality showing that near-saturation forces isolated fourth energy and therefore positive frame/mixing cost.

**New effective corrected-harmonic core defect ceilings:** `183/1024` for the P1/P3 matchings and `6173/51200` for P2. These are *after* subtracting a rigorously retained core-orthogonality penalty; they are **not** bounds on the raw quartic defect alone. The earlier 2026-10-09 and 2026-10-27 numerical envelopes are historical and should not be substituted for these conditional caps.

See [the 2026-10-28 derivation](research/tau5_typeE_isolated_wedge_and_separable_defect_2026-10-28.md) and [exact SymPy verifier](research/tau5_typeE_isolated_wedge_defect_2026-10-28_verify.py).

**OPEN:** No Type-E contradiction; Types C, D, generic e>=27 and non-isolated branches also remain open. The sparse e=23/e=24 classification is conditional on delta(G)>=1. **Global proved range: 40<=tau_5<=44.**


## Delsarte nondeep-slack / Q-frame stability bridge (2026-10-28)

**PROVED EXACTLY, conditional on retained Type-E graph/mass inputs:** Instead of discarding negative Delsarte polynomial contributions from the 794 nondeep pairs, define `N=Σ_nondeep[-7t²(4t²−1)]≥0`. This splits into the 40 isolated-center contacts, 736 contacts across the 184 fully safe selected-edge pairings, and 18 other safe F3 core contacts. The exact scalar mass bounds now include `A+(r/15)N≤Astar` and `U+(r²/15)N≤Ustar`, where `r=D^{-1}(15)≈0.11125520695`, `Astar≈0.65103701309`, and `Ustar≈0.13896031317`.

The sharp elementary contact-quantization inequality `-F(t)≥(21/4)min(|t|,1/2−|t|)²` yields an explicit second-order stability penalty. The Q-frame identity then strengthens the 184-safe squared-correlation lower bound by `cN*N`, with `cN≈0.02169788199`, plus frame-variance and unused core-cap slack. The center row and 184 safe pairings now enter the mass/Q interface **quantitatively**. This is **not** a Type-E contradiction, and the global proved range remains `40≤τ₅≤44`.

See [derivation](research/tau5_typeE_Delsarte_safe_slack_mass_stability_2026-10-28.md) and [SymPy verifier](research/tau5_typeE_Delsarte_safe_slack_mass_stability_2026-10-28_verify.py).


## Isolated-center harmonic gap (2026-10-28)

**[PROVED EXACTLY — isolated-center theorem]** Retaining the positive degree-2/degree-4 harmonic remainder in the 41-point Delsarte mass identity and using the 40 nondeep contacts at the isolated center gives a rational SOS/contact-quantization gap of **2595/256 = 10.13671875**. This strengthens the deep mass lower bound from 410+N to at least 410+2595/256 plus the remaining noncenter nondeep slack.

**[PROVED EXACTLY — conditional Type E]** Combining this gap with the retained F3 broom and matching mass certificates yields **A <= 0.5669250570031576**, **U <= 0.1282700463200052**, and a *joint* projected squared-correlation floor **>=28.2677055569327**. The separate maximum for U occurs at a different scalar endpoint from the joint Q-floor minimum; the proof handles that distinction. Conditional six-core caps give 184-safe squared-mass floors **26.4200493069** (P1/P3) and **26.4864555569** (P2).

See [full proof](research/tau5_typeE_isolated_center_harmonic_gap_2026-10-28.md) and [exact verifier](research/tau5_typeE_isolated_center_harmonic_gap_2026-10-28_verify.py). These supersede the weaker scalar ceilings in the preceding October notes when the isolated-center and F3 mass hypotheses are retained. **[OPEN]** No Type-E exclusion or change to global **40<=tau_5<=44**.
