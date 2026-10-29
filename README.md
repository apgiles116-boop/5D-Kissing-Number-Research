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


## High-center Type E: eight-endpoint D5 extension obstruction (2026-10-28)

**[NEW EXACT DERIVATION; CONDITIONAL BRANCH EXCLUSION]** The Type-E high-center branch `s>=7` is impossible **provided** the previously retained high-center harmonic/mass resource, quantization, rounded-Gram error `<1/9`, and rank-five PSD/D5 finite classification hold. The new proof aligns the true 17-vector frame to the rounded D5 frame with Frobenius error `<2/17<1/8`. Each of the **eight F3 endpoints** then produces a rounded integer correlation column. Exact three-root relations (rank 12 for every 17-line D5 subset) force the column to lie in the D5 frame's column space. A discrete norm-gap theorem restricts each endpoint to a neighborhood of one of the **six signed omitted roots**. Eight endpoints cannot occupy six signed neighborhoods without violating the kissing inequality. The seven-orbit integer verifier passed; it also classifies all 49/51 feasible discrete extension patterns.

**[CONDITIONAL / AUDIT REQUIRED]** This does **not** independently re-prove the upstream mass/harmonic/rounding/D5 certificates and is not a global Type-E elimination. The **low-center branch `s<7` remains open**, as do Types C,D, generic `e>=27`, and non-isolated cases. Retain `M(F3)<=89`, matching `M(P)>=S/2-28/3`, and `A<=383/504`. **Global proved range remains `40<=tau_5<=44`.**

[Full proof](research/tau5_typeE_high_center_core_extension_2026-10-28.md) | [Exact integer verifier](research/tau5_typeE_high_center_core_extension_2026-10-28_verify.py).


## Low-center near-seven exclusion via sixteen-line D5 rigidity (2026-10-28)

**[NEW EXACT ALGEBRA AND FINITE CERTIFICATES; CONDITIONAL TYPE-E EXCLUSION]** The center-harmonic/quantization polynomial extends the near-integrality resource to the *low-center* strip \(209/30\le s\le7\), with \(s=\sum_{w\ne v}(v\cdot w)^2\). On this strip, the noncenter nondeep slack \(R=N-N_0\) and isolated-edge midpoint energy \(x\) satisfy \(D_I+R+g_-(7-s)\le5/64\), where \(g_-(d)=7d(84d^3+28d^2-151d+5)/16\ge0\). Consequently \(x<1/2500\), \(R\le5/64\), and the sixteen isolated projected directions have a half-integral rounded Gram within Frobenius distance \(1/13\).

**[NEW FINITE CHECK]** Exhaustive exact enumeration of 4,096 maximal rank-six sixteen-vertex Schur extensions gives one nonzero characteristic polynomial, all six roots \(>1/2\), excluding rounded rank six under the geometric proximity bound. Together with the retained seven-basis and PSD atlases, the rounded sixteen lines are a \(D_5\) subsystem. All 4,845 omitted-four-line subsets form 17 Weyl orbits; three-term integer root relations span the eleven-dimensional kernel, and exactly eight signed norm-two extensions are possible. A new separate center rounding estimate brings the isolated center and all eight \(F_3\) endpoints within eight omitted signed-root neighborhoods. Nine unit vectors cannot occupy eight neighborhoods under the kissing constraint. Thus **\(209/30\le s\le7\) is excluded conditionally**. Together with the earlier conditional \(s\ge7\) exclusion, **surviving Type E requires \(s<209/30\)**.

[Full proof](research/tau5_typeE_low_center_near7_D5_extension_2026-10-28.md) · [Exact algebra/17-orbit verifier](research/tau5_typeE_low_center_near7_2026-10-28_verify.py) · [4096-clique exact atlas verifier](research/tau5_typeE_low_center_16rank6_atlas_2026-10-28_verify.py).

**[OPEN]** The low-center range \(s<209/30\) remains, as do Types C and D, generic \(e\ge27\), non-isolated cases, and sparse classification without \(\delta(G)\ge1\). The global proved range remains **\(40\le\tau_5\le44\)**. Upstream Type-E mass and finite-atlas completeness are retained inputs; this result is not an unconditional \(\tau_5=40\) proof.


## Residual Type-E center bracket and Q-floor (2026-10-28)

**[NEW EXACT ALGEBRA; CONDITIONAL TYPE E]** The isolated-center harmonic resource and capped-simplex quantization give an algebraic lower bound s >= sigma=5.827662491235... for the center second moment. This lower bracket does not rely on signed-Gram atlases. Combining it with the **previously conditional** near-seven exclusion s>=209/30 confines the remaining Type-E branch to sigma<=s<209/30. The retained directional-frame/KKT inequality then strengthens the conditional projected squared-correlation floor to Q>=28.395623511729..., with 184-safe floors 26.5479672617 (P1/P3) and 26.6143735117 (P2). All new arithmetic was checked with exact rationals. This does not eliminate Type E or independently certify the upstream finite atlases.

[Derivation](research/tau5_typeE_low_center_bracket_Q_2026-10-28.md) · [Verifier](research/tau5_typeE_low_center_bracket_Q_2026-10-28_verify.py). **Global proved range remains 40<=tau_5<=44.**


## Analytic D5 17-line Q-kernel decomposition (2026-10-28)

**[PROVED EXACTLY — STANDALONE D5]** For any subset of D_n projective root lines, if S is the set of represented coordinate supports and D is the set of supports retaining both signs, then `rank(Q)=|S|+rank(P B_D)`, where `B_D` is the unsigned support incidence matrix and `P` projects off the all-ones diagonal. This gives an analytic proof of the 17-line D5 Q-rank dichotomy: rank 14/nullity 3 for 960 omitted-triple patterns and rank 13/nullity 4 for 180 patterns.

Every 17-line D5 subset contains **local eight-line Q-kernel relations** from alternating four-cycles of doubly represented supports. A complete exact 165-support-graph check shows these cycles span a kernel subspace of dimension 2 (seven doubled supports) or 3 (eight doubled supports); one additional global equal-degree relation completes the Q-kernel. This replaces a large root-vector rank enumeration with a structural incidence proof. **[CONDITIONAL TYPE-E RELEVANCE]** Application requires the previously conditional rounded D5 labeling. It does not eliminate the residual Type-E branch or change `40<=tau_5<=44`.

[Analytic derivation](research/tau5_D5_17line_Qkernel_sparse_2026-10-28.md) · [Exact verifier](research/tau5_D5_17line_Qkernel_sparse_2026-10-28_verify.py).


## Exact 16-line D5 Q-rank persistence under quadratic perturbations (2026-10-28)

**[NEW — PROVED EXACTLY, standalone]** For unit D5 root-line columns x_i and projected columns y_i with ||y_i||²=1-a_i, the exact identity
`||Q(y_i)-Q(x_i)||_F²=(2-a_i)||y_i-x_i||²-(1/2)||y_i-x_i||⁴+(3/10)a_i²`
gives `||T_Y-T_X||_op²<=2 epsilon²+(3/10)b²`, where `epsilon=||Y-X||_F` and `b=sum a_i`. The exact 16-line Q spectral atlas has `lambda_min^+=(13-sqrt(149))/20>31/800`. Moreover the sharp unit-ball Lipschitz bound `||T_Y-T_X||_op <= (4/sqrt(5))*epsilon` proves the **stronger result that epsilon<=1/10 ALONE forces rank(T_Y)>=rank(T_X)** for every sixteen-line D5 subset, with no radial-energy assumption. The previous 0.099589 threshold came from the unnecessarily weak `2 epsilon` estimate. When b<1/2500, the quadratic identity even permits epsilon<=7/50=0.14 for rank persistence.

**[CONDITIONAL Type E]** In the already conditionally excluded near-seven branch, the retained bounds `epsilon<1/10` and `b<1/2500` strengthen this to `sigma_rank(T_X)(T_Y)>57/1000`. For rank-14 rounded templates this gives an explicit fourth-moment coercivity inequality. **No new Type-E interval is excluded**; the residual low-center branch still lacks a uniform rounded-D5 certificate. The global proved range remains **40<=tau_5<=44**.

[Derivation](research/tau5_D5_Q_rank_persistence_sharp_2026-10-28.md) · [Exact 4,845-subset verifier](research/tau5_D5_Q_rank_persistence_sharp_2026-10-28_verify.py).


## Sparse-eight D5 Q-kernel incidence bridge (2026-10-28)

**[PROVED EXACTLY — standalone D5 algebra and finite combinatorics]** Every 16-line D5 subset contains at least one Q-kernel relation on exactly eight root lines; every 17-line subset contains at least three. The shortest relations are either alternating four-cycles (15 patterns) or positive triangle-plus-complementary-edge tight frames (10 patterns). Crucially, 240 of the 4,845 sixteen-line subsets have **no** four-cycle but retain a positive eight-line relation. The full 20-line Q-Gram has positive eigenvalues 3/2 (fourfold) and 1 (tenfold), with an explicit minimum-norm right inverse.

**[CONDITIONAL TYPE-E APPLICATION]** If the 16 isolated projected edges admit a rigorously justified D5 labeling, the positive eight-line relation yields an exact squared-correlation identity on 28 pairings, all contained in the 184 **safe** Walsh blocks. This bypasses the six exceptional F3-core pairings but does **not** yet yield an upper-bound contradiction or eliminate Type E. Upstream geometric rounding and alignment certificates were not independently recertified. [Derivation](research/tau5_D5_sparse8_Q_incidence_2026-10-28.md) · [exact verifier](research/tau5_D5_sparse8_Q_incidence_2026-10-28_verify.py). **Global proved range remains 40<=tau_5<=44.**


## F3 double-pattern five-block Walsh/SOS obstruction (2026-10-28)

**[PROVED EXACTLY — under the Type-E F3 deep-edge and endpoint hypotheses]** Both double-pattern perfect matchings of the ten-edge F3 graph force a strict signed Walsh-mixing inequality. After switching and relabeling the four matching pairs as hubs 0,3 and leaves 1,2, write c_ij=m_i.w_j+w_i.m_j and T=c_01-c_02-c_31+c_32. The six deep contacts and the missing leaf-leaf safe pairing give an **exact nonnegative-remainder identity**

    -T-1/4-|c_12|/2
      = ||v_0+v_3+(v_1+v_2)/2||²
        + (1/2-K_12-|c_12|)/2 + Delta > 0,

where v_i=(m_i,w_i), K_ij=v_i.v_j and Delta is the sum of the six positive deep-contact slacks. Hence the four hub-leaf mixed terms have squared sum **>1/64**, without any D5 labeling or SDP. For the all-singleton matching, the six signed mixed terms have squared sum **>1/6**. Consequently **every F3 perfect matching, including the mass-selected one**, has a graph-switched six-pair Walsh squared-energy sum **>1/64**. A standalone P2 midpoint floor C>1/128 follows but is weaker than the retained C>=17/250.

**[OPEN]** The same-sign mixed terms here cannot be identified with the earlier active-sign q_ij; a quantitative transfer to Delsarte nondeep slack or the 184-safe-pair Q bound is still needed. No Type-E elimination. [Full derivation](research/tau5_typeE_F3_double_matching_Walsh_SOS_2026-10-28.md) · [exact verifier](research/tau5_typeE_F3_double_matching_Walsh_SOS_2026-10-28_verify.py). **Global proved range remains 40<=tau_5<=44.**


## Sharp F3 double-matching stress and deep-edge Q cap (2026-10-28)

**[PROVED EXACTLY — STANDALONE F3 CORE]** Both double-pattern F3 matchings have sharp midpoint-energy infimum
\(C>1-\sqrt{\sqrt3-3/4}=0.0090152334324824\ldots\).
An explicit rank-five PSD stress, rank-three boundary witness, unique equality Gram, strict 3D perturbation and quantitative spectral-gap identity are given in
[the proof](research/tau5_typeE_F3_double_matching_exact_sharp_2026-10-28.md)
and [the exact SymPy verifier](research/tau5_typeE_F3_double_matching_exact_sharp_2026-10-28_verify.py).
Together with the prior sharp all-singleton bound, this completes the **sharp matching-uniform local F3 energy floor**.
Conditional on the retained at-most-three-active core theorem, the uniform raw-excess slack improves to \(>0.00120781225890586\).

**[PROVED EXACTLY — USING RETAINED TYPE-E ENERGY CEILING]** Every selected deep edge has \(a_i=\|m_i\|^2<1/4\).
The sharp convex envelope for \(\sum a_i^2\) improves the universal twenty-line Q-frame squared-correlation floor from
\(17456771/635040\) to **\(8790283/317520=27.6841868228773\ldots\)**, a gain of \(131/672\).
An exact six-exception decomposition gives a label-free 184-safe squared-correlation floor
\(64520136179/2520473760\), with additional nonnegative variance/defect terms.
See [the derivation](research/tau5_typeE_deep_edge_cap_Q_floor_2026-10-28.md)
and [exact rational verifier](research/tau5_typeE_deep_edge_cap_Q_floor_2026-10-28_verify.py).
This universal scalar floor is weaker than separately retained center-sensitive conditional estimates.

**[OPEN]** Neither result eliminates Type E or proves \(\tau_5=40\).
The global proved range remains **\(40\le\tau_5\le44\)**. All earlier graph-classification qualifications and unresolved branches remain.


## Residual Type-E center quantization Q-floor (2026-10-28)

**[NEW EXACT ALGEBRA — CONDITIONAL TYPE E]** Retaining the 40 isolated-center nondeep contact quantization penalty in the mass/harmonic resource eliminates the minimizer of the previous residual-center Q relaxation. A three-region rational monotonicity certificate strengthens the projected squared-correlation floor from 28.395623511729... to **Q > 709911/25000 = 28.39644**. Under the separately retained six-core caps, the 184-safe-pair floors become **>26.54878375** (P1/P3) and **>26.61519** (P2). An independent exact paired-center identity additionally couples the center quantization penalty to the midpoint-direction energy B_v, suggesting a future two-variable KKT improvement.

[Exact derivation](research/tau5_typeE_residual_center_quantization_2026-10-28.md) · [Rational verifier](research/tau5_typeE_residual_center_quantization_2026-10-28_verify.py).

**[RETAINED, NOT REPROVED]** Type-E mass/harmonic inputs, conditional finite-atlas exclusion s>=209/30, and previous L'(x)>27/56 certificate. **[OPEN]** No Type-E contradiction; Types C/D, generic e>=27, and non-isolated branches remain. Global proved range **40<=tau_5<=44**.


## Paired-center/frame joint stability (2026-10-29)

**[NEW EXACT ALGEBRA — CONDITIONAL TYPE E]** Jointly retaining the paired-center quantization bound \(N_0\ge n_2(s)-56B_v+(56/5)B_v^2\) and the *full* directional frame term \((5/8)(h+B_v)^2\) gives a quadratic coercivity inequality \(Q\ge J(x,s)+(29/40)B_v^2\). The exact relaxed critical point satisfies \(D(x_2)=2509/6400\), \(x_2\approx0.0020134422834\), and a rational certificate strengthens the conditional twenty-line correlation floor to **\(Q>283965067/10000000=28.3965067\)**. In the narrow strip \(x_2\le x\le1/250,\ 69/10\le s\le209/30\), a new quantitative stability estimate is \(Q\ge F(x_2,s_0)+(2/3)(x-x_2)+(1/10)(s_0-s)+(29/40)B_v^2\). Retained core caps imply 184-safe-pair floors **>26.54885045** (P1/P3) and **>26.6152567** (P2).

[Proof](research/tau5_typeE_paired_center_joint_stability_2026-10-29.md) · [Exact rational verifier](research/tau5_typeE_paired_center_joint_stability_2026-10-29_verify.py). **[RETAINED, NOT REPROVED]** Upstream mass/harmonic certificates, the conditional signed-Gram-atlas exclusion \(s\ge209/30\), and the old large-\(x\) monotonicity. **[OPEN]** No Type-E contradiction or global improvement; \(40\le\tau_5\le44\).


## Tensor-frame and 13+1+6 center-contact stability (2026-10-29)

**[PROVED EXACTLY — STANDALONE ALGEBRA; CONDITIONAL TYPE-E APPLICATION]** An exact five-dimensional frame-operator decomposition retains the transverse terms \(\|PTv\|^2+\frac12\|PTP-\beta P\|_F^2\). A new sorted capped-simplex identity gives a **linear** penalty for deviation of the twenty paired center-contact energies from the 13-at-\(1/2\), one-residual, six-zero pattern. On the critical strip, the retained harmonic/atlas certificates now imply
\[
Q\ge F(x_2,s_0)+\frac23(x-x_2)+\frac1{10}(s_0-s)
+\frac1{160}B_v+\frac{29}{40}B_v^2
+\|PTv\|^2+\frac12\|PTP-\beta P\|_F^2
+\frac1{480}\|\sigma-\sigma_*(s)\|_1.
\]
The new **linear** \(B_v\) coefficient and tensor/contact rigidity improve the earlier quadratic-only stability statement, but **do not increase** the conditional scalar floor \(Q>28.3965067\). The upstream mass/harmonic/conditional signed-Gram inputs are retained, not reverified. **[OPEN]** No Type-E contradiction. Global proved range remains \(40\le\tau_5\le44\).

[Proof](research/tau5_typeE_tensor_contact_stability_2026-10-29.md) · [Exact SymPy verifier](research/tau5_typeE_tensor_contact_stability_2026-10-29_verify.py).


## Sharp local center-contact quantization (2026-10-29)

**[PROVED EXACTLY — standalone capped-simplex theorem]** For the sorted 20 center-contact energies `y_i in [0,1/2]`, with sum `s=13/2+rho` and `1/4<=rho<1/2`, let `delta` be their L1 distance to the sorted `13 x 1/2, rho, 6 x 0` pattern. The concavity gap satisfies the **sharp local quadratic bound** `gap >= (1-2rho)*delta-delta^2`, with equality for every `0<=delta<=1/2-rho` in an explicit two-coordinate transfer family.

**[CONDITIONAL TYPE-E STABILITY]** On the retained critical rectangle `69/10<=s<=209/30`, the prior tensor-contact stability penalty `delta/480` improves to `max(delta/480, delta/240-delta^2/16)`. If `epsilon=Q-F_*<1/14400`, then `delta<=1/30-sqrt(1/900-16epsilon)=240epsilon+O(epsilon^2)`, improving the old first-order `480epsilon` control by a factor of two. The conditional numerical Q-floor does **not** change. This relies on previously retained upstream harmonic/mass/atlas certificates; **no Type-E exclusion**.

See [proof](research/tau5_typeE_sharp_local_contact_quantization_2026-10-29.md) and [exact checker](research/tau5_typeE_sharp_local_contact_quantization_2026-10-29_verify.py). **Global proved range remains 40<=tau_5<=44.**


## Paired-center midpoint concentration (2026-10-29)

**[PROVED EXACTLY — standalone lemma]** For the twenty paired center contacts, let B=sum_i(v.m_i)^2 and delta be the L1 distance of their sorted paired contact energies from the 13+1+6 capped-simplex pattern. If delta<=1/30 and B<=1/16, the first thirteen nearly saturated pairs carry at most (15/172)delta^2 of midpoint-direction energy. The harmonic remainder gains the positive term max(0,B-(15/172)delta^2)/60.

**[CONDITIONAL TYPE-E CONSEQUENCE]** On the retained critical rectangle, for epsilon=Q-F_* with 0<=epsilon<1/14400, this gives B<45epsilon (previously B<=160epsilon). The conditional scalar Q floor remains Q>28.3965067; no Type-E exclusion. The upstream mass/harmonic/signed-Gram/derivative certificates are retained, not independently recertified. **Global proved range remains 40<=tau_5<=44.**

[Proof](research/tau5_typeE_center_quantization_midpoint_mixing_2026-10-29.md) · [Exact rational verifier](research/tau5_typeE_center_quantization_midpoint_mixing_2026-10-29_verify.py).


## Three-zone center-contact coercivity (2026-10-29)

**[PROVED EXACTLY — standalone; CONDITIONAL Type E]** Partition the twenty paired center contacts into thirteen near-saturated pairs, one residual pair, and six low-contact pairs. An exact weighted midpoint-mixing inequality retains the residual weight $h=1/2-\rho-\delta/2$ and an additional $\rho B_T$ penalty on the six low pairs. Combining it with the earlier conditional tensor/harmonic certificates gives, for $\varepsilon=Q-F_*\in[0,1/57600]$,

$$
B_v\le \frac{8282195}{307536}\,\varepsilon<27\varepsilon,\qquad
B_H\le\frac{253500}{43}\varepsilon^2,\qquad
B_T<2\varepsilon\quad(\varepsilon>0).
$$

The asymptotic coefficient improves to $\limsup B_v/\varepsilon\le480/19$, compared with the previous 45 finite-range bound and 480/11 asymptotic coefficient. This improves **stability**, not the scalar Q-floor; the upstream mass/harmonic/conditional signed-Gram certificates were not independently recertified, and **Type E remains open**. [Exact proof](research/tau5_typeE_three_zone_center_coercivity_2026-10-29.md) · [Fraction verifier](research/tau5_typeE_three_zone_center_coercivity_2026-10-29_verify.py). **Global proved range unchanged: 40<=tau_5<=44.**


## Finite-range optimal linear midpoint-direction coercivity (2026-10-29)

**[PROVED EXACT ALGEBRA; CONDITIONAL TYPE-E CONSEQUENCE]** A sharper combination of the exact three-zone center-contact inequality and the previously retained tensor/harmonic inequality upgrades the coefficient `480/19` from an asymptotic limsup to a **uniform finite-range bound**. For `0<=epsilon=Q-F_*<=1/57600`, write `B_v=sum_i(v.m_i)^2`, `delta` for the L1 center-contact distribution deviation, `V_tensor` for the two nonnegative frame anisotropy terms, and `V_4=2(sum p_i^4-B_v^2/20)>=0`. Then

```
epsilon >= (19/480)B_v+(29/40)B_v^2
           +(553/247680)delta+V_tensor+V_4.
B_v <= (480/19)epsilon,
B_v <= 2epsilon/(19/480+sqrt((19/480)^2+(29/10)epsilon)).
```

At the endpoint `epsilon=1/57600`, the nonlinear upper bound gives `B_v/epsilon<=25.06341`, improving the previous finite-range coefficient `27`. The proof is exact rational algebra; **the Type-E application retains earlier harmonic, signed-Gram, and critical-rectangle certificates without re-auditing them**. No positive epsilon gap and no Type-E elimination. [Proof](research/tau5_typeE_finite_range_optimal_linear_B_2026-10-29.md) · [Exact verifier](research/tau5_typeE_finite_range_optimal_linear_B_2026-10-29_verify.py). Global proved range remains `40<=tau_5<=44`.


## Exact F3 double-pattern leaf-concentration obstruction (2026-10-29)

**[PROVED EXACTLY — STANDALONE F3]** For double-pattern matching P1=02|14|36|57, with leaf B=14 and the other pairs A=02,C=36,D=57, put a_i=||m_i||² and R=sqrt(a_A+a_C+a_D). An exact four-contact Gram identity and a two-deep/two-safe Walsh inequality give

\[
(2+2R)\sqrt{a_B}+\sqrt{7R}+\frac32 R\ge\frac12.
\]

Thus **a_B<=1/100 implies a_A+a_C+a_D>1/8100**. By F3 matching automorphisms the same holds for the other leaf and the equivalent double-pattern matching P3. In the weak-contact boundary system, if the other three midpoint vectors vanish, **a_B>=1/12**; a rank-three exact equality witness establishes sharpness for that *weak* system. With strict deep edges the other three midpoints cannot all vanish, by an exact frustration identity.

This rules out **one incidence subcase** of the a_i<1/4 fourth-moment cap-envelope extremizers (the residual 5/504 placed on a core leaf with the other three core energies zero). It **does not** exclude hub-cap patterns, improve the global Q floor, or eliminate Type E. [Proof](research/tau5_typeE_F3_leaf_concentration_obstruction_2026-10-29.md) · [exact SymPy checker](research/tau5_typeE_F3_leaf_concentration_obstruction_2026-10-29_verify.py). All prior mass/harmonic/atlas inputs remain retained, not independently recertified. **Global range unchanged: 40<=tau_5<=44.**


## 2026-10-29 — exact local F3 near-cap adversarial certificates (all twelve patterns)

**[PROVED EXACTLY — finite rational witnesses]** For each of the three F3 perfect matchings and each of its four possible distinguished small edges, eight rational unit vectors in R5 realize the *exact* strict ten-edge F3 deep graph: all ten prescribed edges have dot product < -1/2 and all eighteen nonedges lie strictly between -1/2 and 1/2. Three matched midpoint energies lie in (0.249998,0.25), the fourth in (0.00992,0.00993), with 0.7599 < A_core < 383/504 and U_core=sum a_i^2 > U* - 1/600000 > 99.999% of the capped-simplex envelope U*=47653/254016. All 12 updated ultra-near-cap JSON certificates were independently checked using exact BigInt rational arithmetic after fetching from GitHub. [Research note](research/tau5_typeE_F3_near_cap_all_12_exact_2026-10-29.md) · [witness data](research/tau5_typeE_F3_all_12_near_cap_witnesses_2026-10-29.json) · [exact verifier](research/tau5_typeE_F3_all_12_near_cap_exact_verifier_2026-10-29.py).

**[LIMITATION / RESEARCH DECISION]** This is a negative result for *large F3-only* cap-envelope penalties, not a Type-E construction or contradiction. The sixteen additional deep edges, isolated center, 184 safe Walsh blocks and global Q-frame constraints were not imposed. A uniform F3-only improvement of U* by >=1/600000 is impossible over A_core<=383/504; a smaller penalty is not excluded. Focus on global cross-pair/frame incompatibility. Upstream harmonic and signed-Gram certificates remain conditional. **Global proved range unchanged: 40<=tau_5<=44.**


## D5 sixteen-line complement/frame anisotropy theorem (2026-10-29)

**[PROVED EXACTLY — standalone D5/frame algebra]** Any sixteen of the twenty projective D5 roots leave a four-root complement of rank 4 (4015 cases) or rank 3 (830 cases). The missing-root orthogonal subspace has dimension `k=1` or `k=2`. If the sixteen isolated projected Type-E directions admit an aligned D5 labeling with weighted angular discrepancy `eta²=sum_I (1-a_i)||y_i-r_i||²`, isolated midpoint energy `x=sum_I a_i`, and total midpoint energy `A=sum a_i`, then the *full twenty-vector* frame variance obeys

`V=||sum z_i z_i^T-(4-A/5)I||_F² >= [5k/(5-k)]([(sqrt(4-x)-eta)_+²-(4-A/5)]_+)².`

The global squared-correlation sum gains the positive term `V/2`. In the radial case `eta=0`, the variance gap is `[5k/(5-k)](A/5-x)_+²`, **regardless of the four core directions**. At the illustrative limiting parameters `A=383/504,x=1/250`, this gives an extra Q penalty of at least 0.013687 (k=1) or 0.036499 (k=2). An exact robust example: `A>=1/2,x<=1/250,eta<=1/100` implies `V>=10621081/3125000000>0.00339`.

**[CONDITIONAL Type E]** No D5 alignment is proved in the residual low-center branch, so these gains cannot yet be inserted into the unconditional Type-E floor. This is a quantitative target for geometric rounding, not a Type-E elimination. [Proof](research/tau5_D5_sixteen_complement_frame_gap_2026-10-29.md) · [exact verifier](research/tau5_D5_sixteen_complement_frame_gap_2026-10-29_verify.py). **Global proved range remains 40<=tau_5<=44.**


## Label-free rank-four frame completion theorem (2026-10-29)

**[PROVED EXACTLY — standalone linear algebra; necessary for the retained Type-E 16+4 decomposition]** Let S=sum of the sixteen isolated projected rank-one matrices z_i z_i^T, C=sum of the four F3 projected rank-one matrices, A=sum ||m_i||^2, x=sum_I ||m_i||^2, mu=4-A/5, and V=||S+C-mu I||_F^2. Because C is PSD of rank at most four, if s1>=...>=s5 are the eigenvalues of S, an **exact optimal** label-free lower bound is V>=Phi(S,4-A+x), where Phi is the water-filling completion formula. In particular,

    V >= (5/4)*(lambda_max(S)-(4-A/5))^2.

Hence the twenty-vector projected squared-correlation sum satisfies

    Q >= 30-3A+A^2/10-(1/2)sum a_i^2
         +(5/8)*(lambda_max(S)-(4-A/5))^2.

No D5 labeling, rounding, or core-direction assumption is needed. The coefficient 5/4 is sharp for abstract rank-four PSD completions; the full water-filling formula can be strictly stronger. **[OPEN]** No uniform positive spectral-pinning gap has been established from the 184 safe Walsh blocks, so this is not a Type-E elimination or improved scalar Q floor. [Proof](research/tau5_typeE_label_free_rank4_frame_completion_2026-10-29.md) · [exact verifier](research/tau5_typeE_label_free_rank4_frame_completion_2026-10-29_verify.py). Earlier upstream mass/harmonic/atlas certificates are retained, not independently recertified. **Global proved range unchanged: 40<=tau_5<=44.**


## Norm-aware rank-four completion and core-dispersion bridge (2026-10-29)

**[PROVED EXACTLY — standalone matrix algebra; Type-E application conditional on retained 16+4 matching decomposition]** The preceding rank-four PSD frame completion bound is sharpened by retaining the **four individual F3 core column norms** w_j=1-a_j. Schur-Horn yields an exact four-variable convex quadratic completion over eigenvalues lambda majorizing w. A new SOS identity for the four-column core C and the sixteen-column isolated frame S proves

    ||C-(c/4)(I-P)||_F^2
      = sum_j(w_j-c/4)^2 + 2 sum_{j<k}(q_j.q_k)^2
        + (c/2)sum_j(p.q_j)^2,

where c=sum w_j, p is a top eigenvector of S, P=pp^T. With mu=(tr S+c)/5, S0=mu P+(mu-c/4)(I-P), sigma=||S-S0||_F and V=||S+C-mu I||_F^2, this implies **sqrt(V)+sigma>=sqrt(sum_j(w_j-c/4)^2)**. A rational abstract cap-boundary example has the old rank-four completion gap V=0 but the new fixed-norm minimum V=14641/338688, yielding an extra Q penalty 14641/677376 (~0.0216143). **This is not a uniform Type-E gap or a code realization.** The remaining objective is to control sigma via the 184 safe Walsh blocks or exploit the retained core-core terms. Full proof: [norm-aware completion](research/tau5_typeE_core_norm_spectral_majorization_2026-10-29.md); [exact Fraction verifier](research/tau5_typeE_core_norm_spectral_majorization_2026-10-29_verify.py). Upstream certificates not recertified. Global proved range remains **40<=tau_5<=44**.


## Exact cap L1 stability and outside-16 spectral improvement (2026-10-29)

**[PROVED EXACTLY — algebra/4D polynomial; Type-E use conditional on retained inputs]** The existing capped Q-frame floor L=8790283/317520 now has a quantitative L1 stability refinement: if A<=B=383/504, delta is the L1 distance of the sorted twenty midpoint energies to their capped filling vector at total A, and V is full projected-frame variance, then

    Q>=L+(57/20)(B-A)+delta^2/40+V/2.

The 16+4 midpoint split adds the exact penalty x(A-3/4-x) when 3/4<=A<=B and 0<=x<=A-3/4. Separately, the 16 isolated projected vectors under the retained raw projective-safety and energy hypotheses satisfy **lambda_min(S)>9/160**, improving the earlier >1/18 certificate. The corresponding 184-safe Walsh squared-slack bound strengthens to **H_184>(9/320)(A+A_C)** when A>0. The new 9/160 certificate is a strict positive rational 4D Gegenbauer/Schur-convex comparison.

See [proof](research/tau5_typeE_cap_stability_outside16_gap_2026-10-29.md) and [exact Fraction verifier](research/tau5_typeE_cap_stability_outside16_gap_2026-10-29_verify.py). **[OPEN]** No Type-E contradiction or global bound improvement; all previously listed open branches remain open. Global proved range **40<=tau_5<=44**.


## Universal 21-line quartic defect improvement (2026-10-29)

**[PROVED EXACTLY — standalone]** For any 21 unit projective representatives in R^5, with s_ij=(u_i.u_j)^2, the normalized positive quartic defect P=sum_{i<j}[s_ij(s_ij-1/4)]_+ satisfies **P>1/61**, improving the earlier exact P>1/64. The proof combines the positive degree-four harmonic kernel, exact convex two-well rounding with a two-branch negative-defect envelope, the Q-Gram Gershgorin bound, and a finite integer-degree/Huber certificate with eight strict rational/surd comparisons. No D5 labeling or generic SDP is required.

**[CONDITIONAL TYPE E]** Under the retained isolated-center 16+4 matching and six raw exceptions, the exact raw-quartic bridge is P_raw > 81/15616-(5/4)A-(9/16)A_C. This is weak at the retained Type-E energy ceiling and **does not** eliminate Type E or improve the strongest conditional A bounds. The normalized quartic P and raw/homogeneous defects must not be conflated.

See [proof](research/tau5_21line_quartic_gap_1over61_2026-10-29.md) and [exact verifier](research/tau5_21line_quartic_gap_1over61_2026-10-29_verify.py). **[OPEN]** Type E, C, D, generic e>=27, and non-isolated branches; global proved range remains 40<=tau_5<=44.


## Universal 21-line quartic defect strengthened to P > 1/58 (2026-10-29)

**[PROVED EXACTLY — standalone]** For any 21 unit vectors in \(\mathbb R^5\), \(P=\sum_{i<j}[(u_i\cdot u_j)^2((u_i\cdot u_j)^2-1/4)]_+>1/58\), improving the prior exact \(P>1/61\). The improvement uses the frame/Bessel estimate \(\sum_i(u_i^T\Delta u_i)^2\le(21/5+\sqrt{4V/5})V\), where \(\Delta=\sum_i u_iu_i^T-(21/5)I\), \(V=\operatorname{tr}\Delta^2\), together with a **signed Huber dual** retaining the exact signed degree-rounding error. The proof reduces to eight strictly positive rational/surd comparisons, checked with exact Fraction arithmetic and integer-square-root intervals. [Full proof](research/tau5_21line_quartic_gap_1over58_2026-10-29.md) · [exact verifier](research/tau5_21line_quartic_gap_1over58_2026-10-29_verify.py).

**[CONDITIONAL TYPE E]** The previously retained normalization bridge becomes \(P_{\rm raw}>81/14848-(5/4)A-(9/16)A_C\); this remains weak at \(A\le383/504\) and is **not** a Type-E elimination. Upstream graph/mass/harmonic/signed-Gram certificates were not recertified. Type E, C, D, generic \(e\ge27\), and non-isolated branches remain open. **Global proved range unchanged: \(40\le\tau_5\le44\).**
