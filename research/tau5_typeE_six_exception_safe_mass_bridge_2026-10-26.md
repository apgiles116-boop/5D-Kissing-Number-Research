# Type E: exact six-exception/safe-pair squared-correlation bridge (2026-10-26)

**[PROVED EXACTLY]** Frame/defect identity and sharp capped-energy scalar bound, under stated vector hypotheses. **[CONDITIONAL TYPE E]** 184-safe-pair consequences use the retained raw six-core defect certificate. **[OPEN]** Type E exclusion.

Let z_1,...,z_20 in R^5 satisfy ||z_i||^2=1-a_i, 0<=a_i<=1/4, A=sum a_i<=383/504. Write U=sum a_i^2, F=sum z_i z_i^T, V=||F-(20-A)I/5||_F^2, and S=sum_{i<j}(z_i.z_j)^2. Four core indices determine six exceptional core-core pairs, leaving 184 safe edge-edge pairs. Define S_safe=sum_safe (z_i.z_j)^2, P_raw=sum_core [(z_i.z_j)^2-1/4]_+, N_core=sum_core [1/4-(z_i.z_j)^2]_+.

**Exact bridge (proved algebraically):**

    S_safe+P_raw-N_core
      =57/2-(25/8)A+A^2/10
        +(1/2)sum_i a_i(1/4-a_i)+V/2.                 (1)

Proof: S=(tr(F)^2/5-sum_i ||z_i||^4+V)/2
=30-3A+A^2/10-U/2+V/2. Each core square s obeys
s=1/4+[s-1/4]_+-[1/4-s]_+. Subtract the six core squares and rewrite U/2=A/8-(1/2)sum_i a_i(1/4-a_i). Both remainders in (1) are nonnegative. This is a nonlocal second-order identity, not a D5 labeling or rigidity claim.

**Sharp capped-energy scalar bound (proved exactly):** At fixed A, convexity of the square gives U<=k/16+(A-k/4)^2, k=floor(4A). An extremizer has k entries 1/4, one entry A-k/4, and the rest zero. On each interval k/4<=A<=(k+1)/4, the derivative of 30-3A+A^2/10-U_max(A)/2 is -3-4A/5+k/4<0. At A=383/504, k=3, hence

    S>=8790283/317520 =27.684186822877... .           (2)

This improves the older 17456771/635040 floor by exactly 131/672. If all a_i<1/4, equality in (2) is impossible.

**[CONDITIONAL TYPE E]** Retain P_raw<=1780062775/4032758016 from the prior six-exception convex certificate. Since N_core>=0, (1)-(2) yield

    S_safe>=519072132637/20163790080
           =25.742785983070... .                        (3)

By Cauchy-Schwarz on the 184 safe pairings,

    sum_safe (z_i.z_j)^4
      >=(519072132637/20163790080)^2/184
      =269435878880323320573769/74810431191816378777600
      =3.601581685707... .                             (4)

The safe squared-correlation dispersion also satisfies

    sum_safe ((z_i.z_j)^2-1/8)^2
      >=(519072132637/20163790080-23)^2/184
      =3058638688757706875209/74810431191816378777600
      =0.0408851899398... .                            (5)

**Core-energy refinement [CONDITIONAL]:** With C=sum_core a_i>0 and the previously proved matching-uniform balanced-triangle cut, P_raw<C+899*C^2/3600. Thus the right-hand side of (1) gives

    S_safe>=57/2-(25/8)A+A^2/10
             +(1/2)sum_i a_i(1/4-a_i)+V/2
             -min(1780062775/4032758016,C+899*C^2/3600).

The inequality is strict when the core-dependent branch of the minimum is active.

**[OPEN]** These bounds do not exclude Type E or force A>383/504; they are exact additional constraints for a six-exception finite polynomial/KKT formulation. The global proved range remains 40<=tau_5<=44. Types C,D, generic e>=27, and non-isolated branches remain open. Preserve M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass>=2137/6; sparse e=23/e=24 classification requires delta(G)>=1.
