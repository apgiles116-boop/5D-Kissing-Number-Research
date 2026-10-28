# D5 Walsh subframe atlas and sharper midpoint stress (2026-10-28)

**Proof status:** [PROVED EXACTLY — standalone D5 integer linear algebra and finite Weyl-orbit classification]. The midpoint gap below is [CONDITIONAL on full 20-line alignment and epsilon^2 <= A]. **No Type-E elimination; global range remains 40 <= tau_5 <= 44.**

## Definition

For the 20 projective D5 roots x_{ij}^{+/-}=(e_i +/- e_j)/sqrt(2), put v_i=sqrt(2)x_i. For a subset S of n lines, let C_S be its pairs with |x_i.x_j|=1/2 and sigma_ij=2x_i.x_j. Define the integer operator L_S on n five-vectors w_i by the n diagonal rows v_i.w_i and one row v_i.w_j+sigma_ij w_i.v_j for each contact {i,j} in C_S.

## New exact finite atlas

| Retained | Omitted-root pattern | Subsets | dim ker L_S |
|---|---|---:|---:|
| 17 | 3 distinct supports | 960 | 0 |
| 17 | 1 complete support and 1 extra root | 180 | 3 |
| 16 | 2 complete supports | 45 | 6 |
| 16 | 1 complete support and 2 single roots | 1440 | 3 |
| 16 | 4 distinct supports, omitted graph a 4-edge star | 80 | 1 |
| 16 | 4 distinct supports, omitted graph a triangle plus disjoint edge, omitted triangle sign product +1 | 80 | 1 |
| 16 | Other 4-distinct-support patterns | 3200 | 0 |

The sign product uses the +/- signs in x_{ij}^{+/-}; it is switching invariant. In total, 960 of 1140 seventeen-line subsystems and 3200 of 4845 sixteen-line subsystems have injective L_S.

**Exact spectral certificates:** For every injective 17-line subsystem, L_S^T L_S > (2/17) I_85. For every injective 16-line subsystem, L_S^T L_S > (1/11) I_80. These bounds are certified using integer fraction-free positive-definiteness elimination on each full-rank orbit representative.

The 1920 Weyl(D5) actions split the 1140 omitted triples into 7 orbits and the 4845 omitted quadruples into 17 orbits. Every representative's rank is computed exactly. A complete doubled-support D3 triangle exists in every 17-line subset and in 4685/4845 sixteen-line subsets. The 160 exceptions have doubled-support graph K_{2,3}. Only 80 of those 160 have Walsh nullity one; triangle sign parity distinguishes the other 80.

## Sharper full-D5 nonlinear Walsh stress

For twenty feasible endpoint pairs u_i^{+/-}=m_i +/- y_i, let A=sum ||m_i||^2, Delta_i=y_i-x_i, epsilon^2=sum ||Delta_i||^2, and c_ij=y_i.m_j+sigma_ij m_i.y_j. Each template contact obeys

|c_ij| <= d_ij - m_i.m_j, where d_ij=1/2-sigma_ij y_i.y_j.

Let V be the 20x5 integer-root matrix. V^T V=8I_5. The signed contact matrix S=VV^T-2I has spectrum 6 (multiplicity 5), -2 (multiplicity 15). Thus sum_j sigma_ij x_j=6x_i and, using ||y_i||^2=1-||m_i||^2,

sum_C d_ij = 3A+3 epsilon^2-sum_C sigma_ij Delta_i.Delta_j <=3A+4 epsilon^2.

The unsigned contact adjacency has smallest eigenvalue -4, so sum_C m_i.m_j >= -2A. Consequently the new exact inequality is

**sum_C |c_ij| <= 5A+4 epsilon^2.**

This improves the earlier 5A+A^2/2+(4+epsilon)^2 epsilon^2/2 bound and does not need the Q-frame potential.

For a complete 6-line D3 triangle, the analogous exact inequality on its 12 contacts is

**sum_{C_D3} |c_ij| <= 2 A_D3+2 epsilon_D3^2.**

## Improved conditional midpoint gap

The earlier exact full-20 Walsh operator has smallest squared singular value lambda_*=0.348434647877..., the smallest root of t^3-24t^2+146t-48. The perturbation bound ||L_y-L|| <= sqrt(26) epsilon and the new stress give

(sqrt(lambda_*)-sqrt(26) epsilon) sqrt(A) <= sqrt(2)(5A+4 epsilon^2).

**If epsilon^2 <= A**, then A=0 or

A >= lambda_*/(sqrt(26)+9sqrt(2))^2 > 1/913.

The final strict rational check uses sqrt(lambda_*)>5902/10000, sqrt(26)<50991/10000, sqrt(2)<141422/100000, and 913(5902/10000)^2>(50991/10000+9*141422/100000)^2. This improves the previous conditional A>1/2500.

## Limitations

These are exact D5 results. The Type-E geometry has only conditional rounded 16/17-line D5 subsystems, not a justified full-20 alignment; epsilon^2<=A is not established. Positive local triangle stresses do not automatically imply injectivity of the full 16-line Walsh operator. The six exceptional F3 pairings are not identified with Q-kernel directions. Residual Type E, Types C and D, generic e>=27, and non-isolated branches remain open. Retain M(F3)<=89, matching M(P)>=S/2-28/3, and A<=383/504. Global proved range: 40<=tau_5<=44.

**Verifier:** tau5_D5_Walsh_subframe_atlas_2026-10-28_verify.py (exact integer ranks, orbit classification, positive-definiteness pivots, and rational gap checks).