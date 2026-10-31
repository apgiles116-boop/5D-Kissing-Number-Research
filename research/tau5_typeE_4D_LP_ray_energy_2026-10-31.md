# Type E: exact 4D harmonic-polynomial bounds on isolated ray energies

Date: 2026-10-31. Status: **PROVED EXACTLY** under the stated sixteen-isolated-safe-edge hypotheses. Type E remains **OPEN**; the global proved range is **40 <= tau_5 <= 44**.

## Theorem (rank-free, small isolated midpoint energy)

For sixteen isolated selected deep edges, write a_i=||m_i||^2, A_I=sum_i a_i, ||z_i||^2=1-a_i. The endpoint inequalities imply |z_i.z_j|+m_i.m_j<=1/2 for every i!=j. Let Z_I=sum_i z_i z_i^T. Then, for every unit p in R^5, X=p^T Z_I p satisfies the following **strict** lower bounds:

| Hypothesis | Conclusion | Exact rational contradiction upper bound |
| --- | --- | --- |
| A_I<=1/8 | X>1/12 | 10399806/5603803 < 2 |
| A_I<=3/20 | X>1/16 | 1406739590/750891141 < 2 |
| A_I<=1/5 | X>1/50 | 119537125/63352692 < 2 |
| A_I<=9/40 | X>1/400 | 4287685855250/2154561514983 < 2 |

Thus Z_I is strictly positive definite with explicit frame lower bounds. No D5 labeling, Q-rank assumption, or generic SDP is required.

## Analytic proof

**Step 1 (exact 4D LP).** For sixteen unit vectors n_i in R^4, use f(t)=t^4-t^2/4. With U_2(t)=4t^2-1 and U_4(t)=16t^4-12t^2+1, the exact identity

f(t)=1/16 + U_2(t)/8 + U_4(t)/16

has nonnegative dimension-four Gegenbauer coefficients. The spherical-harmonic addition theorem gives sum_{i,j} f(n_i.n_j)>=16^2/16=16. Since f(1)=3/4, the diagonal contributes 12. Hence

sum_{i<j} f(n_i.n_j)>=2. (LP)

**Step 2 (projection).** Fix a unit p. Put x_i=p.z_i, X=sum x_i^2, d_i=a_i+x_i^2, b_i=1-d_i. Suppose A_I<=a0 and X<=x0 for one of the table rows. Set beta=1-a0-x0>0, and n_i=(z_i-x_i p)/sqrt(b_i), unit vectors in the four-plane p-perp. With c_ij=m_i.m_j, the endpoint inequality gives

|n_i.n_j| <= [1/2-c_ij+|x_i x_j|]/sqrt(b_i b_j).

Because -c_ij<=sqrt(a_i a_j)<=a0/2 and |x_i x_j|<=x0/2, all absolute correlations are bounded by

B=[1/2+(a0+x0)/2]/beta.

For all four rows, 1/2<B<1. The factorization f(t)=t^2(t+1/2)(t-1/2) for t>=0 gives

f(n_i.n_j) <= B^2(B+1/2)(|n_i.n_j|-1/2)_+.

**Step 3 (aggregate excess).** From the projection bound,

(|n_i.n_j|-1/2)_+ <= beta^(-1)[(1-sqrt(b_i b_j))/2+(-c_ij)_++|x_i x_j|].

The following three estimates are exact:

sum_{i<j}(1-sqrt(b_i b_j))/2 <= [15/(2(1+beta))](A_I+X),

sum_{i<j}(-c_ij)_+ <= 4 A_I,

sum_{i<j}|x_i x_j| <= (15/2) X.

For the first, use 1-sqrt(b_i)=d_i/(1+sqrt(b_i))<=d_i/(1+beta), then sum over 15 partners. For the second, use sum |c_ij|<=15 A_I/2 and sum c_ij=(||sum m_i||^2-A_I)/2>=-A_I/2. The third follows from 2|x_i x_j|<=x_i^2+x_j^2.

Let q=15/[2(1+beta)]. Combining the three bounds with (LP) forces

2 <= [B^2(B+1/2)/beta][(4+q)A_I+(15/2+q)X]
  <= [B^2(B+1/2)/beta][(4+q)a0+(15/2+q)x0].

Exact rational arithmetic gives the four strict upper bounds displayed in the theorem, each <2. Contradiction. Therefore X>x0 for every unit p. QED.

## New absolute safe-minor gap in the rank-13 two-ray branch

**[PROVED EXACTLY — CONDITIONAL]** Add the earlier hypotheses: isolated Q-rank 13, rank-two missing Q matrix, and four genuinely ambiguous core completions. The missing-plane axes p,q have ray energies X=p^T Z_I p and Y=q^T Z_I q. The prior exact core-wedge and Cauchy–Binet theorem gives

sum_{i<j,c<d} (D_ic D_jd-D_id D_jc)^2 >= (81/131072) X^2 Y^2,

sigma_2(D)>=XY/(128 sqrt(2)), where D_ic=(z_i.z_c)^2 is entirely safe data.

In the A_I<=1/8 region the new theorem gives X,Y>1/12. Consequently,

sum squared 2-by-2 safe minors > 1/33554432,

sigma_2(D) > 1/(18432 sqrt(2)).

For the other energy tiers, replace 1/12 by the corresponding x0. This establishes an **absolute**, rather than merely nonzero, two-ray minor gap on the region A_I<=9/40, without any D5 proximity hypothesis. It does not eliminate the branch.

## Verification and proof-status ledger

Companion exact Python verifier checks the 4D polynomial identity, all four rational margins, D4 sharp equality (12 projective lines), and a 16-line D5 projection example. Universal positivity follows analytically from the addition theorem; the examples are supplementary, not Type-E feasibility witnesses.

**[OPEN]** No proof places every Type-E candidate in A_I<=9/40. The larger-A_I region, rank-13 cases without four genuine ambiguities, other Q-ranks, Types C/D, generic e>=27, and non-isolated branches remain open.

**[RETAINED, NOT REPROVED HERE]** The stronger broom M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, six-exception raw/homogeneous defect caps, Musin/Boyvalenkov zero-midpoint exclusion, and D5 Q-kernel results. The e=23/e=24 sparse graph classification remains conditional on delta(G)>=1. **Global proved range unchanged: 40<=tau_5<=44.**
