# Type E: center-contact/midpoint mixing stability (2026-10-29)

**[PROVED EXACTLY — standalone lemma]; [CONDITIONAL TYPE-E COROLLARY].** No Type-E exclusion. The global proved range remains 40 <= tau_5 <= 44.

## Standalone exact lemma

For twenty pairs (p_i,q_i) with |p_i+q_i|,|p_i-q_i| <= 1/2, set y_i=2(p_i^2+q_i^2), sorted decreasing, s=sum y_i, rho=s-13/2, B=sum p_i^2, and delta=L1 distance of y from (13 copies of 1/2, rho, 6 zeros). Assume 2/5<=rho<=7/15, delta<=1/30 and B<=1/16.

Then

(1) sum_{i<=13} p_i^2 <= (15/172)delta^2.

(2) sum_i (1/2-y_i)p_i^2 >= max(0,B-(15/172)delta^2)/60.

**Proof.** D=sum_{i<=13}(1/2-y_i), E=sum_{i>=15}y_i satisfy y_14=rho+D-E and delta=2 max(D,E), hence D,E<=1/60. For i<=13, y_i>=29/60. The two endpoint caps imply |p_i q_i|<=(1/2-y_i)/4, while q_i^2=y_i/2-p_i^2>=29/120-1/16=43/240. Thus p_i^2<=(15/43)(1/2-y_i)^2 and sum_{i<=13}p_i^2<=(15/43)D^2<=(15/172)delta^2. For i>=14, 1/2-y_i>=1/60, since rho<=7/15 and D,E<=1/60. Therefore sum_i(1/2-y_i)p_i^2 >=(B-sum_{i<=13}p_i^2)/60, and the left side is nonnegative. QED.

## Coupled harmonic remainder [PROVED EXACTLY]

Define N0=7 sum_i [(p_i+q_i)^2(1-4(p_i+q_i)^2)+(p_i-q_i)^2(1-4(p_i-q_i)^2)], n2=7rho(1-2rho), and R_N=N0-n2+56B-(56/5)B^2. The exact identity

R_N=7[sum_i y_i(1-2y_i)-rho(1-2rho)]+112 sum_i(1/2-y_i)p_i^2+224[sum_i p_i^4-B^2/20]

and the previously proved sharp capped-simplex theorem give

(3) R_N/112 >= [(1-2rho)delta-delta^2]/16 + max(0,B-(15/172)delta^2)/60.

In the critical Type-E interval rho<=7/15, the first term is >=delta/240-delta^2/16.

## Conditional Type-E stability improvement

Retain the upstream mass, harmonic, signed-Gram and derivative certificates in tau5_typeE_tensor_contact_stability_2026-10-29.md and tau5_typeE_sharp_local_contact_quantization_2026-10-29.md; these are NOT independently recertified here. In the critical rectangle x_2<=x<=1/250 and 69/10<=s<=209/30, when delta<=1/30 and B<=1/16:

Q >= F_*+(2/3)(x-x_2)+(1/10)(209/30-s)+B/160+(29/40)B^2
    +||PTv||^2+(1/2)||PTP-beta P||_F^2
    +delta/240-delta^2/16+max(0,B-(15/172)delta^2)/60,

where F_*=F(x_2,209/30)=28.3965067813... and notation is unchanged.

For epsilon=Q-F_* with 0<=epsilon<1/14400, the retained theorem gives delta<=480epsilon<1/30 and B<=160epsilon<1/16, so the lemma applies. As all other displayed terms are nonnegative,

epsilon >= B/160+max(0,B-(15/172)delta^2)/60
        >= (11/480)B-delta^2/688.

Hence the **new small-error estimate**

(4) B <= (480/11)epsilon+(30/473)delta^2
       <= (480/11+480/473)epsilon < 45epsilon.

This improves B<=160epsilon in the stated critical regime but does not improve the scalar Q floor or force a positive epsilon. The next target is incidence-sensitive coupling to the 184 safe pairings. Type E, C, D, generic e>=27, and non-isolated branches remain open.

Verifier: research/tau5_typeE_center_quantization_midpoint_mixing_2026-10-29_verify.py.
