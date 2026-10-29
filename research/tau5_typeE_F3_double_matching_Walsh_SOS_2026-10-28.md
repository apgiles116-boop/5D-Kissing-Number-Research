# F3 double matching: exact five-block Walsh/SOS forcing (2026-10-28)

**[PROVED EXACTLY — under stated F3 deep-edge and endpoint hypotheses]. [OPEN]** No Type-E exclusion; global proved range remains 40 <= tau_5 <= 44.

Use the ten-edge F3 graph 02,04,05,14,17,23,27,36,56,57. Its three perfect matchings are 02|14|36|57, 04|17|23|56, 05|14|27|36. The first and third have cross-multiplicity pattern (0,1,1,1,1,2); the middle is all-singleton. The two double patterns are equivalent under relabeling and switching.

For 02|14|36|57, orient the four pairs (0,2),(1,4),(3,6),(5,7). Write their unit endpoints m_i +/- z_i, with m_i.z_i=0 and ||m_i||²+||z_i||²=1. Switch w=(z_0,-z_1,-z_2,z_3) and set v_i=(m_i,w_i) in R^5 direct-sum R^5; ||v_i||=1. Hubs are 0,3, leaves 1,2. Six cross-deep contacts comprise two hub-hub contacts with switched signs ++ and -- and four hub-leaf contacts with signs +,-,-,+ in order 01,02,31,32.

Set K_ij=v_i.v_j, c_ij=m_i.w_j+w_i.m_j, and T=c_01-c_02-c_31+c_32. Let Delta be the sum of six strictly positive deep-contact slacks (-1/2 - endpoint_dot). Let rho=1/2-K_12-|c_12|>=0, from the two same-sign safe leaf-leaf endpoint inequalities.

The six deep inner products sum to
D=2K_03+K_01+K_02+K_31+K_32+T=-3+R+T,
where R=(||v_0+v_3+v_1||²+||v_0+v_3+v_2||²)/2.
The parallelogram identity yields
R=||v_0+v_3+(v_1+v_2)/2||²+(1-K_12)/2.
Because Delta=-3-D=-R-T, we obtain the **exact SOS identity**

    -T-1/4-|c_12|/2
      = ||v_0+v_3+(v_1+v_2)/2||² + rho/2 + Delta > 0.  (1)

Consequently

    c_01-c_02-c_31+c_32 < -1/4-|c_12|/2,                 (2)
    c_01²+c_02²+c_31²+c_32²
       > (1/4+|c_12|/2)²/4 >= 1/64.                       (3)

This is a compulsory **signed same-sign Walsh mixing** floor on the four hub-leaf pairings, independent of which core projected correlations exceed 1/2. The c_ij must NOT be identified without proof with the active-sign q_ij in the earlier three-active theorem.

A standalone (but weaker than retained P2) midpoint-energy corollary is C=sum||m_i||²>1/128. Indeed with p=m_0-m_3, q=m_1-m_2, U=w_1-w_2, V=w_0-w_3, r²=||q||²+||U||²=||v_1-v_2||²>=1, the opposite-sign hub-hub endpoint constraints give ||V||²<=3. Hence |T|=|p.U+V.q|<=sqrt(2C)*sqrt(r²+3), whereas |T|>R>=r²/4. Thus C>r^4/[32(r²+3)]>=1/128. The retained P2 bound C>=17/250 is stronger.

**[VERIFIED]** Exact enumeration checks both double-pattern F3 matchings, sign switching, the checkerboard pattern, and the formal SOS identity. **[RETAINED, NOT REPROVED]** M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, and the Musin/Boyvalenkov zero-midpoint exclusion. **[OPEN]** Convert (1)-(3) into an upper-bound contradiction using the full endpoint/Delsarte nondeep slack; Types C, D, generic e>=27 and non-isolated branches remain open.

Verifier: research/tau5_typeE_F3_double_matching_Walsh_SOS_2026-10-28_verify.py.
