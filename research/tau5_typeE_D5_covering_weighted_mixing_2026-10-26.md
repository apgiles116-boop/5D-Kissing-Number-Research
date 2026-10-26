# Type E: exact D5 covering obstruction and weighted mixing
Date: 2026-10-26. Proof-status note; no Type-E exclusion.

## [PROVED EXACTLY] D5 projective covering constant
For the 20 D5 projective representatives v_ij^±=(e_i±e_j)/sqrt(2), every unit x in R^5 satisfies

    max_{i<j,±} |x.v_ij^±| >= sqrt(2/5).

This is sharp for |x_1|=...=|x_5|=1/sqrt(5). Proof: sort b_1>=...>=b_5>=0 as the absolute coordinates and let t=b_1+b_2. The maximum equals t/sqrt(2). Since b_3,b_4,b_5<=b_2 and 0<=b_2<=t/2,

    1 <= (t-b_2)^2+4*b_2^2 <= 5*t^2/4,

where the last step maximizes a convex quadratic over [0,t/2].

## [CONDITIONAL ON TYPE-E CENTER ENDPOINT CONSTRAINTS] Nonlocal separation
For the isolated center x_0 and endpoints m_i±z_i, the two center constraints give

    |x_0.z_i|+|x_0.m_i|<=1/2.

For any orthogonal image, permutation, and independent sign choices of the 20 D5 representatives v_i, at least one i satisfies

    ||z_i-v_i|| >= sqrt(2/5)-1/2+|x_0.m_i|.

In particular max_i ||z_i-v_i|| >= sqrt(2/5)-1/2 = 0.1324555320... . Thus actual Type E cannot be uniformly close to a D5 20-line template; this does NOT exclude Type E.

## [PROVED EXACTLY] Weighted mixing operator
Fix a D5 representative v_i. For any set T of at most three other representatives define

    W_i(T)=sum_{j not in {i} union T} (v_i.v_j)^2 v_j v_j^T.

Then W_i(T) >= (3/32)I_5. By signed-coordinate symmetry fix v_i=(e_1+e_2)/sqrt(2). There are exactly 12 other representatives with squared correlation 1/4; seven others contribute zero. The undeleted W_i is diag(3/4,3/4,1/2,1/2,1/2). It suffices to remove three of the 12 nonzero contributors. For all C(12,3)=220 choices, the five leading principal minors of the INTEGER symmetric matrix 32 W_i(T)-3I are strictly positive. The minima over the 220 choices are, respectively,

    9, 189, 13, 169, 2197.

The accompanying exact SymPy verifier enumerates all 220 matrices and certifies these integers. A witness deletion gives eigenvalue (3-sqrt(5))/8 = 0.0954915..., showing 3/32=0.09375 is close to optimal.

## [PROVED EXACTLY] Mixing identity; [CONDITIONAL] D5-model bound
For the 184 safe pairs S and arbitrary z_i,m_i, define

    J_edge=sum_{ij in S}(z_i.z_j)^2*((m_i.m_j)^2+(m_i.z_j)^2+(z_i.m_j)^2)
    W_i(z)=sum_{j:ij in S}(z_i.z_j)^2 z_j z_j^T.

Then exactly

    J_edge=sum_i m_i^T W_i(z)m_i+sum_{ij in S}(z_i.z_j)^2(m_i.m_j)^2.

If the projected vectors were exactly D5-labeled, with four core indices and six omitted core-core pairs, the operator theorem would give

    J_edge >= (1/2)A_O+(3/32)A_C.

IMPORTANT: This D5-model estimate is NOT an unconditional Type-E inequality. The center obstruction above rules out an exact D5 labeling, and no closeness theorem is established.

## [PROVED EXACTLY] Why total squared-correlation mass does not identify D5
Any twenty unit vectors with tight-frame operator 4I_5 have sum_{i<j}(u_i.u_j)^2=30. Four repeated orthonormal bases are a non-D5 example with the same total. They violate projective safe constraints, but demonstrate that the global Q/frame mass floor by itself cannot force a D5 labeling.

## [OPEN] Ledger
No improved midpoint-energy interval or Type-E exclusion. Global proved range remains 40<=tau_5<=44. Types C,D, generic e>=27, and non-isolated branches remain open. Retain M(F3)<=89, matching mass >=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504. The sparse e=23/e=24 classification assumes minimum graph degree >=1. Next: a NONLOCAL stability/classification theorem using all 184 safe constraints and six exceptional core pairs, rather than merely the total squared-correlation mass.