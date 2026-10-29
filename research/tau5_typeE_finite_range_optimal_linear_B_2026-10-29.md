# Type E: finite-range optimal linear midpoint-direction coercivity (2026-10-29)

**Proof status:** [PROVED EXACT ALGEBRA UNDER EXPLICIT HYPOTHESES]; [CONDITIONAL TYPE-E COROLLARY]. **No Type-E elimination.** Global proved range remains 40 <= tau_5 <= 44.

## Context and dependencies

Retain the notation and critical-rectangle hypotheses of `tau5_typeE_tensor_contact_stability_2026-10-29.md` and `tau5_typeE_three_zone_center_coercivity_2026-10-29.md`: twenty selected deep pairs, center unit vector v, p_i=v.m_i, sorted y_i=2(p_i^2+q_i^2), rho=s-13/2 in [2/5,7/15], delta=||y-y_*||_1, B=sum p_i^2, B_H=sum_{i<=13}p_i^2, B_T=sum_{i>=15}p_i^2, c=15/172, and epsilon=Q-F_* >= 0. Here F_*=F(x_2,209/30). The prior **conditional** tensor/harmonic certificate gives

    epsilon >= B/160 + (29/40) B^2 + ||PTv||^2
               + (1/2)||PTP-beta P||_F^2 + R_N/112,

with additional nonnegative scalar-envelope terms omitted. The **exact** paired-center identity is

    R_N/112 = gap/16 + mix + 2(sum p_i^4-B^2/20),
    gap >= (1-2rho)delta-delta^2,
    mix = sum_i(1/2-y_i)p_i^2,

and sum p_i^4-B^2/20 >= 0 by Cauchy-Schwarz. The exact three-zone lemma gives

    mix >= h (B-c delta^2)_+ + rho B_T,
    h = 1/2-rho-delta/2.

The previous conditional tensor bound gives B<=160 epsilon and delta<=480 epsilon. Hence for 0<=epsilon<=1/57600 we have B<=1/360, delta<=1/120, and h>=1/30-delta/2>0. The previously proved cap estimate B_H<=c delta^2 is applicable (delta<1/30, B<1/16).

## New finite-range theorem

**[PROVED EXACTLY FROM THE DISPLAYED ASSUMPTIONS]** Throughout 0<=epsilon<=1/57600, writing

    V_tensor = ||PTv||^2 + (1/2)||PTP-beta P||_F^2,
    V_4 = 2(sum p_i^4-B^2/20) >= 0,

we have the simultaneous stability inequality

    epsilon >= (19/480) B + (29/40) B^2
               + (553/247680) delta + V_tensor + V_4.       (A)

In particular,

    B <= (480/19) epsilon,                                  (B)

and the stronger finite-range nonlinear bound

    B <= 2 epsilon / [19/480 + sqrt((19/480)^2+(29/10)epsilon)]. (C)

At epsilon=1/57600, the right side of (C) is approximately 0.0004351286358829, corresponding to B/epsilon <= 25.06340943, compared with the preceding bound B<27 epsilon. The linear constant 480/19 was previously established only as a **limsup** as epsilon->0; it is now a rigorous finite-range coefficient. It is not claimed to be sharp for realizable Type-E configurations.

## Proof

Since rho<=7/15, the sharp quantization inequality yields

    gap/16 >= delta/240-delta^2/16.

Since h>=1/30-delta/2>0 and (t)_+>=t, the three-zone lemma gives

    mix >= (1/30-delta/2)(B-c delta^2).

Adding the retained positive tensor and fourth-moment terms and expanding gives

    epsilon >= (19/480)B+(29/40)B^2+V_tensor+V_4
               + delta*[1/240-delta/16-B/2-c delta/30+c delta^2/2].

For delta<=1/120, B<=1/360, and c=15/172, the square bracket is bounded below by

    1/240 - 1/1920 - 1/720 - (15/172)/(3600)
      = 553/247680 > 0.

This proves (A). Dropping the nonnegative terms yields (B) and solving the quadratic yields (C).

## Proof-status ledger

- **[PROVED EXACTLY]** The elementary finite-range implication (A)-(C), conditional only on the explicitly displayed inequalities, and the rational coefficient 553/247680.
- **[RETAINED, NOT RE-CERTIFIED IN THIS PASS]** The Type-E mass/harmonic envelopes, critical rectangle, conditional signed-Gram exclusion, B_H<=15 delta^2/172, and derivative certificate used to produce epsilon>=....
- **[OPEN]** No positive epsilon gap and no contradiction with A<=383/504. Type E, Types C and D, generic e>=27, and non-isolated graph branches remain open. Global proved range is still 40<=tau_5<=44.

Verifier: research/tau5_typeE_finite_range_optimal_linear_B_2026-10-29_verify.py.
