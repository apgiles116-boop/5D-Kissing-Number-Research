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


## Isolated-center directional Q-frame gap (2026-10-28)

**[PROVED EXACTLY — conditional Type E]** The isolated-center second-moment row forces nonzero directional variance in the 20-vector projected frame. Coupling the harmonic center-row estimate to the mass-concavity scalar envelopes yields the strengthened global squared-correlation bound **>=28.3885724064515**, superseding the earlier conditional 28.2677055569 floor. More precisely, with x the midpoint energy on the 16 isolated selected edges and B_v=sum_i(v.m_i)^2 for the isolated center v, the bound is

    sum_{i<j}(z_i.z_j)^2 >= L0 + (27/56)*x + (9/20)*B_v + (5/8)*B_v^2,

where L0=28.3885724064515... is an explicitly defined algebraic constant. The proof includes an exact rational derivative certificate; no D5 labeling or new SDP is used. Under retained F3 six-core caps, the 184-safe squared-correlation floors improve to **26.5409161564515** (P1/P3) and **26.6073224064515** (P2), with the same extra penalties.

See [derivation](research/tau5_typeE_center_frame_directional_gap_2026-10-28.md) and [SymPy verifier](research/tau5_typeE_center_frame_directional_gap_2026-10-28_verify.py). **[OPEN]** No Type-E contradiction; global range still **40<=tau_5<=44**.


## Center-contact quantization and exact KKT refinement (2026-10-28)

**[PROVED EXACTLY — conditional Type E]** Retaining the isolated-center fourth-harmonic row's nondeep-contact slack produces a new exact two-branch inequality. If the center second moment `s=sum_{w!=v}(v.w)^2` is at least 7, the sixteen isolated-edge midpoint energy obeys `x<=D^{-1}(5/64)=0.000399120052...`, and the total Delsarte slack of all 794 nondeep pairs satisfies `N<=5/64`. Thus **at most five** nondeep scalar products can be at distance at least 1/20 from `{0,+/-1/2}`. This is a necessary near-integrality condition, not a combinatorial classification.

A two-variable rational KKT/resource-exchange argument, combined with the preceding directional frame result for `s<=7`, improves the conditional global projected squared-correlation floor to **28.38917770968655...**. The conditional 184-safe-pair floors are now **26.54152145968655** (P1/P3) and **26.60792770968655** (P2). The gain over 28.3885724 is small but certified without numerical optimization or a generic SDP.

See [derivation](research/tau5_typeE_center_quantized_KKT_2026-10-28.md) and [exact rational verifier](research/tau5_typeE_center_quantized_KKT_2026-10-28_verify.py). **[OPEN]** Type E remains unresolved; global proved range remains **40<=tau_5<=44**.


## High-center binary-contact and signed-Gram reduction (2026-10-28)

**[PROVED EXACTLY — conditional on retained Type-E high-center mass/harmonic certificates]** In the branch where the isolated-center second moment `s>=7`, the global nondeep Delsarte slack is at most `5/64` and the isolated-edge midpoint energy `x<1/2500`. Every nondeep scalar product is either `|t|<1/9` or `|t|>12/25`. Exactly **28 of the 40 center contacts are high**, and **12 low**. Among the 120 pairings of the 16 isolated deep edges, every pairing has either four low or four high contacts with forced alternating signs. The 16 projected vectors consequently have **at least 71 high-correlation pairings** (via the rank-five Welch bound and the tiny low-contact squared-mass budget).

The 184 safe Walsh blocks admit a discrete `(1/8)Z` rounding with total coefficient squared error at most `5/1344`. More strongly, the true rank-five Gram matrix of the isolated center plus the sixteen isolated projected vectors is within Frobenius distance **<1/8** of a symmetric half-integral 17-by-17 matrix `Ghat`, with `2Ghat` integral, diagonal 2, off-diagonal 0 or ±1. An exact determinant-integrality argument forces **rank(Ghat)<=8**, equivalently its signed adjacency matrix has eigenvalue -2 with multiplicity >=9. **No PSD or rank-five property is claimed for the rounded matrix.**

This reduces the high-center branch to a finite signed-graph/rank problem; it does not eliminate Type E or resolve the low-center branch. See [the proof](research/tau5_typeE_high_center_binary_rank8_2026-10-28.md) and [exact rational verifier](research/tau5_typeE_high_center_binary_rank8_2026-10-28_verify.py). Global proved range remains **40<=tau_5<=44**.


## High-center rank-seven and binary-rank-six upgrade (2026-10-28)

**[NEW, EXACT — conditional on the preceding high-center certificates]** On the two contact intervals already proved for the \(s\ge7\) branch, the nondeep quantization polynomial obeys the sharper inequality \(7t^2(1-4t^2)\ge(539/81)\rho(t)^2\), where \(\rho(t)=\min(|t|,1/2-|t|)\). Consequently, the true rank-five PSD 17-vector Gram \(G\) and its half-integral rounding \(\widehat G\) satisfy the stronger exact bound
\[
\|G-\widehat G\|_F^2<158205281/13475000000<1/81.
\]
An inertia-sensitive determinant/integrality argument, verified by 50 rational comparisons, upgrades the previous **rank(\(\widehat G\)) \(\le8\)** to **rank(\(\widehat G\)) \(\le7\)**. Thus the signed adjacency \(2\widehat G-2I\) has eigenvalue \(-2\) with multiplicity at least **10**. Modulo two, the unsigned adjacency matrix is alternating, hence has **binary rank at most 6** and binary nullity at least 11. An exact Schur-complement/star-complement formulation reduces the remaining high-center classification to at most seven base vertices and columns from \(\{-1,0,1\}^7\).

See [the exact proof and finite reduction](research/tau5_typeE_high_center_rank7_2026-10-28.md) and [Fraction verifier](research/tau5_typeE_high_center_rank7_2026-10-28_verify.py). The old rank-eight statement is retained above only as historical context. **[OPEN]** Neither high-center nor low-center Type E is excluded; Types C, D, generic \(e\ge27\), and non-isolated branches remain open. **Global proved range unchanged: \(40\le\tau_5\le44\).**


## High-center 82-support and determinant-four pruning (2026-10-28)

**[NEW, EXACT — conditional on the retained high-center certificates]** The rank-five Welch inequality applied to the isolated center plus sixteen projected isolated-edge vectors, combined with the nondeep slack bound `N<=5/64`, forces **at least 82** high/rounded-nonzero pairings among the 136 possible pairs (previously 81). If the center has exactly ten high isolated-edge neighbors, at least **72** of the 120 isolated-isolated pairings are high (previously 71).

The stronger `||G-Ghat||_F<1/9` estimate also gives a sharp integral restriction on any nonsingular principal seven-by-seven block `T` of `2Ghat`: **det(T) is one of -4,-2,2,4**. Therefore a rank-seven rounded candidate necessarily has binary unsigned-support rank **exactly six**; candidates of binary rank at most four have rounded real rank **at most six**. This reduces the exact star-complement base enumeration, without assuming the rounded matrix is PSD or rank five.

See [proof](research/tau5_typeE_high_center_82_support_det4_2026-10-28.md) and [Fraction verifier](research/tau5_typeE_high_center_82_support_det4_2026-10-28_verify.py). **[OPEN]** Type E remains unresolved, including the low-center branch; global proved range remains **40<=tau_5<=44**.


## High-center exact finite rank-six reduction (2026-10-28)

**[NEW — EXACT FINITE CERTIFICATE, CONDITIONAL ON RETAINED HIGH-CENTER INPUTS]** An exhaustive switching-normalized signed-graph atlas calculation, using integer characteristic polynomials and exact rational real-root counts (not numerical eigenvalues), improves the rounded 17-vector Gram bound from **rank at most seven to rank at most six**. The 197629 seven-vertex signed representatives reduce to 13812 determinant-eligible cases, 4802 distinct characteristic polynomials, and exactly two bases compatible with the rank-five PSD Frobenius proximity. Each has 112 possible eighth-vertex Schur-complement columns, and all 224 extensions violate an exact rational spectral-gap inequality. Therefore the rounded signed adjacency has eigenvalue **-2 with multiplicity at least eleven**. This is not a Type-E exclusion, and the low-center branch remains open.

See [the exact proof](research/tau5_typeE_high_center_rank6_exact_atlas_2026-10-28.md) and [the executable integer/rational verifier](research/tau5_typeE_high_center_rank6_exact_atlas_2026-10-28_verify.py). The preceding rank-seven result is retained only as historical context. **Global proved range unchanged: 40<=tau_5<=44.**


## High-center exact rank-five reduction (2026-10-28)

**[NEW — EXACT FINITE CERTIFICATE; TYPE-E CONSEQUENCE CONDITIONAL ON UPSTREAM HIGH-CENTER INPUTS]** The rounded 17-vector signed Gram matrix now has **rank at most five**, improving the earlier rank-six ceiling. A universal exact atlas lemma shows that an integer symmetric matrix of order at least 17, diagonal 2 and off-diagonal 0 or ±1, cannot have rank exactly six while lying within squared Frobenius distance **<1/16** of a PSD rank-five matrix. The proof enumerates 156 six-vertex supports, 4,562 switching-normalized signings, 246 rationally eligible six-bases, 10,956 Schur columns, 3,010 seven-block survivors, and 14,404 eight-block-compatible pairs; the maximum exact extension-compatibility clique is **10**, whereas 11 outside vertices would be necessary.

Under the retained high-center rounding estimate, `||2Ghat-2G||_F^2 < 158205281/3368750000 < 1/16`, the previous rank-six ceiling therefore becomes `rank(Ghat)<=5`. Modulo two, the unsigned support adjacency has **binary rank at most four**, forcing at least one pair of nonadjacent false twins among its 17 vertices. The finite calculation uses exact integer characteristic polynomials, rational sign-variation root counts, integer Schur complements and independently checked clique search.

See [proof](research/tau5_typeE_high_center_rank5_exact_clique_2026-10-28.md) and [exact verifier](research/tau5_typeE_high_center_rank5_exact_clique_2026-10-28_verify.py). **[OPEN]** The rounded matrix is not yet known PSD; the low-center Type-E branch and other graph cases remain open. **Global proved range remains 40<=tau_5<=44.**


## High-center PSD rigidity and exact D5 rounded labeling (2026-10-28)

**[NEW — EXACT FINITE CERTIFICATE; APPLICATION CONDITIONAL ON HIGH-CENTER GEOMETRY]** An independent integral star-complement enumeration proves that any symmetric integer matrix of order at least 13 with diagonal 2, off-diagonal 0 or ±1, and rank at most five must be **positive semidefinite of rank exactly five**. Exact maximum sizes for ranks 1–4 are 1, 3, 6, and 12; an **indefinite** rank-five matrix has at most 10 vertices. This uses 24 switching-normalized rank-four signings and 220 rank-five signings (164 nonsingular indefinite bases), with maximum outside-column cliques 8 and 5, respectively.

Combining this universal lemma with the preceding high-center rank-five reduction proves that the **rounded** 17-line Gram is PSD and belongs to the **D5 root system** by the standard ADE classification: rank-five A5 has only 15 root lines, reducible types at most 13, and D5 has 20. This is a justified D5 labeling for the rounded subsystem, **not** for the unrounded vectors and not a uniqueness claim about optimal projective packings.

The 17 rounded D5 lines have **84–87 high-correlation edges**, center degree `k_I in {10,11,12}`, and at least 74/73/72 high isolated-isolated pairings in those respective branches. Their 5D frame operator has the sharper exact spectral gap `F_17 >= 2I_5`. These give concrete inputs for the next Q-kernel perturbation and second-order stability analysis. **Type E remains open. Global proved range remains 40<=tau_5<=44.**

See [proof and limitations](research/tau5_typeE_high_center_PSD_D5_root_rigidity_2026-10-28.md) and [exact integer verifier](research/tau5_typeE_high_center_PSD_D5_root_rigidity_2026-10-28_verify.py).


## High-center D5 Q-kernels and exact Gram stability (2026-10-28)

**[NEW — EXACT ALGEBRA, TYPE-E APPLICATION CONDITIONAL]** For any 17 of the 20 D5 root lines, the traceless-tensor Q matrix has **rank 14 (nullity 3)** if the three omitted lines belong to distinct coordinate supports, or **rank 13 (nullity 4)** if both signs of one support are omitted. An independent exact/modular enumeration of all 1,140 omitted triples gives 960 and 180 cases respectively. All Q-kernel relations are explicitly weighted-degree relations on the seven or eight coordinate supports retaining both D5 signs.

The 17-line rounded D5 frame has the **sharp spectral bound `F_17>=2I_5`**, since the three missing unit roots have a Gram operator norm at most 2. Combining this with the retained `||G-Ghat||_F<1/9` shows the **true** 17-vector Gram has rank exactly five, nonzero eigenvalues `>17/9`, and its 12-dimensional kernel is close to the rounded kernel: projections of rounded-kernel vectors onto the true range have norm `<||w||/17`; projections of true-kernel vectors onto the rounded range have norm `<||u||/18`. These are quantitative stability bounds, not a Type-E exclusion.

See [derivation](research/tau5_typeE_high_center_D5_Qkernels_2026-10-28.md) and [exact verifier](research/tau5_typeE_high_center_D5_Qkernels_2026-10-28_verify.py). The rounded Q relations have **not** been transferred as exact relations to the true Type-E vectors. **Global proved range remains 40<=tau_5<=44.**


## Exact 17-line D5 flexibility theorem (2026-10-28)

**[PROVED EXACTLY — D5 TEMPLATE; CONDITIONAL TYPE-E RELEVANCE]** Every 17-line subset of the standard 20 projective D5 root lines admits a **noncongruent finite deformation preserving coherence <=1/2**. The 1140 omitted triples form seven Weyl orbits (sizes 120,60,160,40,40,480,240). Explicit sparse integer velocities and 952 exact quartic Bernstein positivity certificates prove the claim on the whole parameter interval 0<=t<=1/10; no numerical LP or floating-point eigenvalue decisions enter the final certificate.

**Research consequence:** Full-D5 infinitesimal rigidity does **not** pass automatically to the rounded high-center 17-line subsystem. The remaining four F3 directions and their six exceptional pairings are indispensable for any rigidity-based Type-E contradiction. This is a negative result for a tempting shortcut, **not** an elimination of Type E.

[Full theorem and witnesses](research/tau5_typeE_D5_17line_flex_2026-10-28.md) · [Standalone exact verifier](research/tau5_typeE_D5_17line_flex_2026-10-28_verify.py).

**[OPEN]** Type E high/low center, C, D, generic e>=27, non-isolated branches. **Global proved range unchanged: 40<=tau_5<=44.**
