# Type E: safe-pair endpoint mixing and an exact D5-template second-order gap

2026-10-27. Companion exact verifier: tau5_typeE_safe_pair_mixing_D5_gap_2026-10-27_verify.py.

**[PROVED EXACTLY, LABEL-FREE]** For two selected deep edges, write endpoints as m_i ± z_i and m_j ± z_j. If all four cross-endpoint pairs are safe (inner products in [-1/2,1/2]), put B=m_i·m_j, X=z_i·m_j, Y=m_i·z_j, Z=z_i·z_j. The four correlations are B+sigma X+tau Y+sigma*tau Z. Their Walsh/Parseval identity yields

    B^2+X^2+Y^2+Z^2 <= 1/4.

The stronger exact two-sided inequalities are

    |B+Z|+|X+Y| <= 1/2,
    |B-Z|+|X-Y| <= 1/2.

These apply to the 184 Type-E edge-edge pairings involving at least one of the sixteen outside-core edges, but not automatically to the six core-core pairings. For the isolated center x0, |x0·m_i|+|x0·z_i|<=1/2.

Let a_i=||m_i||^2, r_i=1-a_i, d=r_i*r_j, h=1-d, T=B^2+X^2+Y^2 and s=Z^2/d. Then the exact **mixing-corrected normalized defect** is

    [s(s-1/4)]_+ <= [h-4T]_+/(16*d^2).

Indeed Z^2-d/4 <= h/4-T and Z^2<=1/4. A safe pair contributes positive normalized defect only if T<h/4. For center-edge pairs, with t=|x0·m_i|, the stronger linear correction is

    [s_0i(s_0i-1/4)]_+ <= [a_i-4t+4t^2]_+/(16*(1-a_i)^2).

Retaining the six-core defect budgets from the 2026-10-26 pair-normalization note, and letting R be the normalized-positive safe pairs and J_R=sum_R T_ij, gives the conditional refinement

    P <= [sum_i k_i*a_i+4C+9C^2+5C^3+C^4-4J_R]/[16*(1-A)^2].

Crucial caveat: no lower bound on *all-pair* mixing can be substituted for J_R without proving it holds on the active safe pairs.

**[PROVED EXACTLY, CONDITIONAL ON EXACT D5 NORMALIZED DIRECTIONS]** Suppose the 20 normalized directions u_i=z_i/sqrt(1-a_i) are precisely the D5 projective lines (e_p ± e_q)/sqrt(2), p<q, with any four lines selected as the F3 core and all other edge-edge pairs endpoint-safe. Write C=sum_core a_i, A_O=A-C. Midpoint orthogonality gives m_i·u_i=0. Define

    J=sum_{i!=j, not both core} (u_i·u_j)^2*(m_i·u_j)^2.

Every D5 line has 12 projective contacts with squared correlation 1/4. For outside-core i, the contact-frame operator is diag(3/4,3/4,1/2,1/2,1/2), giving J_i>=a_i/2.

For core i, fix u_i=(e1+e2)/sqrt(2) by D5 symmetry. Its 12 contact neighbours are (e_a ± e_k)/sqrt(2), a=1,2 and k=3,4,5. Deleting at most three core neighbours gives

    8T_i=diag(6,6,4,4,4)-sum_deleted w*w^T, w=e_a ± e_k.

Restrict to u_i^perp using e1-e2,e3,e4,e5. Exhaustive exact enumeration of the 220 triples gives four generalized characteristic polynomials, with multiplicities:

    96: (x-4)(x-2)(2x^2-15x+26)/2
    64: (x-3)^2(2x^2-15x+24)/2
    48: (x-4)(2x^3-19x^2+52x-40)/2
    12: (x-4)^2(2x^2-11x+8)/2

The smallest root is (11-sqrt(57))/4, so the sharp core restricted operator constant is c=(11-sqrt(57))/32. Hence

    J >= A_O/2+c*C >= c*A.

For any safe D5-contact pair, |z_i·z_j|=sqrt(r_i*r_j)/2>=3/8>|m_i·m_j|. The two-sided endpoint inequalities imply

    |m_i·z_j| <= (1-sqrt(r_i*r_j))/2
               <= (2/7)(a_i+a_j).

Since r_j>=3/4, |m_i·u_j|<=4(a_i+a_j)/(7sqrt(3)). D5's 12-regular contact graph then gives

    J <= (4/147)*sum_directed_contacts(a_i+a_j)^2
      <= (4/147)*24*A^2 = (32/49)*A^2.

Therefore the exact conditional second-order inequality is

    A_O/2 + ((11-sqrt(57))/32)*C <= (32/49)*A^2.

If A>0 this forces

    A >= 49(11-sqrt(57))/1024
      = 0.1650958131559895...

The bound is sharp at the level of the restricted D5 contact operator, not claimed attainable by a Type-E code.

**[OPEN]** An arbitrary Type-E configuration has not been proved to admit a D5 normalized-direction labeling or a quantitative approximation to one. This result does not improve the unconditional Type-E A>1/49 certificate or exclude Type E. The six exceptional pairings are not identified with the six D5 Q-kernel relations. Retain M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass>=2137/6, A<=383/504, and the Musin/Boyvalenkov zero-midpoint boundary exclusion. Types C,D, generic e>=27 and non-isolated branches remain open. The sparse e=23,24 classification is conditional on delta(G)>=1. Global proved range stays 40<=tau_5<=44.
