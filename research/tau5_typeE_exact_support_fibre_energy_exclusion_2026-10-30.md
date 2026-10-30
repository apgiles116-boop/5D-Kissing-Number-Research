# Type E: exact D5 support-plane fibre excluded by midpoint energy
Date: 2026-10-30

**[PROVED — computer-assisted exact rational certificate; CONDITIONAL on exact D5 support-plane structure]**

Under the retained isolated-center Type-E hypotheses, add the geometric assumption that the twenty normalized projected directions form ten orthonormal pairs, each spanning one coordinate two-plane of a common orthonormal basis. Assign the four F3 core selected edges to one line on each of four star supports in K5. Under this EXTRA assumption, the 184 safe Walsh blocks and isolated center force

    A = sum_i ||m_i||^2 >= 11/14 = 396/504 > 383/504,

with an exact energy contradiction margin of 13/504.

**[OPEN]** This is not a general Type-E exclusion. The support-plane assumption has not been derived from the weighted Q-Gram or Walsh constraints. Global proved range remains 40 <= tau_5 <= 44.

## Safe-support graph and imbalance

For each selected deep edge, write x_i^+ = m_i+z_i, x_i^- = m_i-z_i, a_i=||m_i||^2 <= 1/4, w_i=||z_i||^2=1-a_i, and u_i=z_i/sqrt(w_i). The isolated unit center v satisfies |v.z_i| <= 1/2, hence |v.u_i|^2 <= 1/3.

Label the ten coordinate supports by K5 edges. Put the four F3 core edges on one line each of the four supports (1,2),(1,3),(1,4),(1,5). Discard six star-star meeting-support pairs, since each can contain an exceptional core-core line pairing. The other 24 meeting-support pairs are FULLY SAFE (all four line pairings safe): 12 star/nonstar and 12 nonstar/nonstar. Their degrees are 3 on each of four star supports and 6 on each of six nonstar supports. Four safe endpoint contacts in [-1/2,1/2] imply |z_i.z_j| <= 1/2 by Walsh inversion.

For each support e, define t_e in [0,1] as the absolute squared-coordinate imbalance of its orthonormal basis. Relative to the D5 basis this is t_e=|sin(2 delta_e)| with |delta_e|<=pi/4, modulo signs and swaps. For two meeting supports e,f, the normalized 2x2 cross-Gram matrix is an outer product, giving

    max_{s,t} |u_e^s.u_f^t|^2 = (1+t_e)(1+t_f)/4.

For a fully safe support pair, choose the maximizing line pair i,j. Since w_i,w_j >= 3/4,

    (1+t_e)(1+t_f) <= 1/(w_i w_j) <= 16/9.

Every support has a fully safe meeting neighbor, so t_e <= 7/9.

The elementary bounds for a in [0,1/4] and t in [0,7/9] are

    -log(1-a) <= 7a/6,       log(1+t) >= 11t/15.

They follow from concavity and exact endpoint estimates:
log(4/3) <= 47/162 < 7/24 and
log(16/9) >= 2*(7/25+(7/25)^3/3) > 77/135.

Taking logs of the safe maximum-pair inequality yields

    t_e+t_f <= (35/22)(a_i+a_j) <= (35/22)(A_e+A_f),

where A_e is the sum of the two midpoint energies on support e. Sum over the 24 fully safe meeting-support pairs, writing C for four star supports and N for six nonstar supports:

    T_C + 2*T_N <= (35/22)*(A_C+2*A_N) <= (35/11)*A.       (1)

## Isolated center forces total imbalance

Put p_k=v_k^2, sort p_1>=...>=p_5>=0, sum p_k=1. The two center-projection squares on support (i,j) sum to p_i+p_j and are individually <=1/3. Therefore p_1+p_2<=2/3.

For support (i,j), put D=2*sqrt(p_i*p_j), X=p_i-p_j, and B=2/3-p_i-p_j. The difference of the two squared center projections has absolute value <=B. Expressing that difference in the rotated D5 basis gives

    D*sqrt(1-t_ij^2)-X*t_ij <= B.

Since t_ij<=7/9<4/5, sqrt(1-t_ij^2)>=1-t_ij/2, and thus

    t_ij >= max(0,(sqrt(p_i)+sqrt(p_j))^2-2/3)
                  / (p_i-p_j+sqrt(p_i*p_j)).                (2)

A zero denominator means the term is zero; on the feasible domain its numerator is nonpositive. Let F(p) be the sum of the ten right-hand sides.

**[PROVED BY EXACT INTERVAL CERTIFICATE]** On the sorted simplex with sum p_i=1 and p_1+p_2<=2/3,

    F(p) >= 5/2.                                            (3)

The companion exact verifier proves (3) with no floating-point certification decisions. The sorted simplex is the convex hull of five rational vertices p^(k)=(1/k,...,1/k,0,...,0). Each simplex is bisected along its longest edge. Vertices are stored as integer vectors over common denominator D0. Let l_i and h_i be integer coordinate minima/maxima over the vertices. If 3*(l_1+l_2)>2*D0, the simplex contains no feasible point. Otherwise each summand of F is bounded below by

    max(0,3*(l_i+l_j+2*floor(sqrt(l_i*l_j)))-2*D0)
      / (3*(h_i-l_j+ceil(sqrt(h_i*h_j)))).

This is rigorous by numerator monotonicity and denominator domination. Exact integer square roots and Fraction comparisons suffice. The certificate closed after 28,707 simplex subdivisions: 23,846 children pruned by exact lower bounds and 4,862 by infeasibility. No region was left unresolved.

From (2)-(3), T_C+T_N>=F(p)>=5/2. Combining with (1),

    5/2 <= (35/11)*A  ==>  A >= 11/14 = 396/504,

contradicting the retained cap A<=383/504.

## Status

**[PROVED — exact, conditional]** The exact D5 support-plane fibre is excluded with energy gap 13/504. The interval lemma is universal on the stated five-coordinate domain.

**[OPEN]** Establish quantitative inverse stability/rounding from the global weighted Q-frame variance and five local Q-cycle residuals to an approximate support-plane representation, and propagate the 13/504 gap. Do not identify six exceptional pairings with six Q-kernel relations without proof.

**[RETAINED]** 40<=tau_5<=44, M(F3)<=89, matching mass >=2137/6, A<=383/504. Type C, Type D, generic e>=27 and non-isolated branches remain open; e=23/24 sparse classification still assumes delta(G)>=1.
