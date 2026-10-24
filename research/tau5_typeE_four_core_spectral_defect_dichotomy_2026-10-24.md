# Type E: sharp four-core spectral threshold and raw-defect support hierarchy

2026-10-24. **[PROVED EXACTLY]** four-vector inequalities. **[CONDITIONAL TYPE-E APPLICATION]** to the four selected F3 matching edges. Not a Type-E elimination or a global D5 labeling.

## Definitions and exact spectral reduction

For four Euclidean vectors m1,...,m4 put C=sum ||mi||^2>0, D=sum_{i<j}(-mi.mj)_+, and epsilon=C-D. Let N be the graph of strictly negative pairwise products, B its adjacency matrix, and X=(mi.mj) its PSD Gram matrix. Then

D=-(1/2)tr(BX) <= -(1/2)lambda_min(B) C. (1)

## Theorem 1: optimal K2,2 threshold [PROVED EXACTLY]

Among all 64 labeled simple graphs on four vertices, exactly the three C4=K2,2 graphs have lambda_min(B)<-sqrt(3), with lambda_min=-2. Every other graph satisfies lambda_min(B)>=-sqrt(3); equality is attained by K1,3. The exact verifier tests all principal minors of B+sqrt(3)I using integer-pair arithmetic in Z[sqrt(3)].

Consequently,

**D/C>sqrt(3)/2, equivalently epsilon/C<1-sqrt(3)/2, forces N=K2,2.**

The transition 1-sqrt(3)/2=0.1339745962... is sharp: collinear (-sqrt(3)v,v,v,v) has negative graph K1,3 and D/C=sqrt(3)/2. This improves the sign-graph condition epsilon/C<=1/64 in the earlier K2,2 theorem, but does not replace its common-normal bound.

## Theorem 2: exact within-part margins [PROVED EXACTLY]

If N=K2,2 with parts {1,2},{3,4}, set s=m1+m2 and t=m3+m4. Since D=-s.t, the exact sum-of-squares identity

C/2 + m1.m2 + (s.t)/sqrt(2)
= (1/2)||s+t/sqrt(2)||^2 + (1/4)||m3-m4||^2 >=0 (2)

and its part-swapped version give

m1.m2, m3.m4 >= D/sqrt(2)-C/2.

If D/C>sqrt(3)/2, both products are strictly greater than

**((sqrt(6)-2)/4) C = 0.1123724357... C.** (3)

The limiting margin is sharp within K2,2: use collinear m3=m4=1, m1=-1/sqrt(2)+b, m2=-1/sqrt(2)-b and let D/C decrease to sqrt(3)/2. Identity (2) remains an equality.

## Theorem 3: five/six negative pairings [PROVED EXACTLY]

If N has exactly five edges, relabel so {1,2} is the missing edge. The four cross products and m3.m4 are negative, and D=-s.t-m3.m4. The exact identity

C/sqrt(2)+s.t+sqrt(2)(m3.m4)
= (||s+sqrt(2)t||^2+||m1-m2||^2)/(2sqrt(2)) >=0 (4)

and m3.m4<0 yield **D<=C/sqrt(2)**. This constant is sharp as a supremum: for orthogonal unit u,v use m1=m2=-u/2, m3=(u+(1+h)v)/(2sqrt(2)), m4=(u-(1+h)v)/(2sqrt(2)), h>0 tending to zero.

If all six pairings are negative, then

D=(C-||m1+m2+m3+m4||^2)/2 <= C/2. (5)

Equality is attained by a centered regular tetrahedron.

## Conditional Type-E consequences

For the four distinguished F3 matching edges, x_i^±=m_i±z_i and endpoint kissing constraints imply

mi.mj+|zi.zj|<=1/2,
delta_ij=(|zi.zj|-1/2)_+ <=(-mi.mj)_+.

Thus **[CONDITIONAL ON THE RETAINED FOUR-CORE MODEL]**:

- If D/C>sqrt(3)/2, at most four of six core pairings can have positive raw projective defect, and the other two have |zi.zj|<1/2-((sqrt(6)-2)/4)C.
- If at least five core pairings have positive raw defect, the total core raw defect is <=C/sqrt(2).
- If all six have positive raw defect, their total is <=C/2.

These are local necessary conditions, not an upper bound on the full 20x20 Q-Gram perturbation or a Type-E contradiction.

## Proof-status ledger

**[PROVED EXACTLY]:** sharp four-vertex spectral threshold, within-part margin, five/six-negative-pair bounds and sharpness constructions.

**[EXACT FINITE VERIFICATION]:** 64 graphs and all principal minors of B+sqrt(3)I, exact characteristic polynomials for five-/six-edge graphs.

**[CONDITIONAL TYPE-E]:** raw-defect support and budget hierarchy for the four selected matching edges.

**[OPEN]:** convert this local dichotomy to a global Q-Gram or energy contradiction; Type E, Type C, Type D, generic e>=27, and non-isolated branches.

**[UNCHANGED]:** 40<=tau_5<=44; M(F3)<=89; matching M(P)>=S_F3/2-28/3; A<=383/504. Sparse e=23/24 classification conditional on delta(G)>=1.

Companion exact verifier: tau5_typeE_four_core_spectral_defect_dichotomy_2026-10-24_verify.py.
