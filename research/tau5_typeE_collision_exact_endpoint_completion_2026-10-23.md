# Type E: endpoint completion across all D5 core support collisions
2026-10-23. PROVED EXACTLY (conditional on fixed D5 labels): The six missing core-core Q-Gram entries are uniquely determined by all other entries and the diagonals, EVEN when four core supports repeat, if the Q-Gram is PSD of rank at most 14 and the missing squared correlations obey the sharp zero-midpoint bound 0 <= q_ij^2 <= 1/4. This is an exact-boundary theorem, not a global D5 labeling/proximity result or a Type-E exclusion.

## Theorem
Let w_ab^s=(e_a+s e_b)/sqrt(2), Q_i=w_i w_i^T-I/5, and G0_ij=tr(Q_i Q_j)=|w_i.w_j|^2-1/5. Choose ANY four labels J among the 20 D5 lines, O=J^c. Suppose G is a PSD 20x20 matrix with rank(G)<=14, and G_ij=G0_ij whenever i=j or either index is in O. Suppose also -1/5<=G_ij<=1/20 for all six distinct core pairs i,j in J. Then G=G0.

## Proof
For support s={a,b}, decompose Q_s^±=D_s±U_s, where D_s=(E_aa+E_bb)/2-I/5 and U_s=(E_ab+E_ba)/2. We have ||D_s||^2=3/10, ||U_s||^2=1/2; the ten U_s are orthogonal, and the D_s span the four-dimensional traceless diagonal space.

Let h be the number of supports with both signs in J (h=0,1,2). The complete support pairs retained in O include at least six supports; their D_s span the diagonal space for every four-support deletion. Hence the template O-vectors span precisely the diagonal space and all U_s except those on the h doubled supports, so rank G0[O,O]=14-h. An isometric Gram realization of G identifies its O-span with the template O-span. All core projections are fixed; the only nonzero residuals are on doubled supports, each of squared norm 1/2. Rank(G)<=14 places the residuals in a space of dimension <=h.

For h=0, there are no residuals, hence G=G0. For h=1, the two residuals of the doubled support lie on one line, with dot product ±1/2. Their squared correlation is 1/2 plus that dot product, either 0 or 1. The endpoint upper bound 1/4 forces 0, recovering G0.

For h=2, denote the two doubled-support residual pairs by u1,u2 and v1,v2. Each vector has squared norm r^2=1/2. The same-support bounds imply u1.u2<=-r^2/2 and v1.v2<=-r^2/2. For two different supports s,t, the squared correlation is b_st+u_i.v_j, with b_st=1/4 if supports meet and b_st=0 if disjoint. In the first case, the upper bound 1/4 implies all u_i.v_j<=0. In the second case, nonnegativity implies all u_i.v_j>=0; replace v1,v2 by their negatives to reduce to <=0.

Planar opposite-cone lemma: If two equal-norm vectors make an angle >=120 degrees and are not antipodal, their common nonpositive-dot half-plane intersection is a pointed cone of aperture <=60 degrees. Two nonzero vectors in that cone cannot themselves make an angle >=120 degrees. Consequently u2=-u1. The cross inequalities then place v1,v2 on the line perpendicular to u1, and their within-pair negative dot forces v2=-v1. Thus all cross residual products vanish and both same-support squared correlations are 0. All six missing entries match G0. QED.

## Exact finite check
The accompanying verifier uses the integer matrix 20*G0 and modular rank arithmetic. It checks all C(20,4)=4845 choices, with complementary ranks:
- h=0: 3360 cases, rank 14.
- h=1: 1440 cases, rank 13.
- h=2: 45 cases, rank 12.
It also checks diagonal spanning for all 210 four-support deletions and the rational D5 Gram entries. The planar lemma is an analytic proof, not a numerical test.

## Uniform qualitative corollary for actual Type-E Q-Grams
For genuine Type-E vectors z_i with a_i=||m_i||^2<1/4, define G_ij=tr(Q_i Q_j) and split G-G0=R+E, where E is supported on the six core off-diagonal pairs. If ||R||_op tends to zero under any fixed D5 labeling, then max_core |E_ij| tends to zero, even for repeated supports. Proof: G_ii=(4/5)(1-a_i)^2 tending to 4/5 forces a_i->0. The Q-Grams are bounded, PSD, rank<=14. Every subsequential limit has R=0 and core squared correlations in [0,1/4] by the endpoint inequalities, so the theorem forces E=0. There are finitely many core choices, making the qualitative modulus uniform across all 4845 choices. No explicit modulus/radius is claimed.

## Status
PROVED EXACTLY: all-support exact-boundary completion under the sharp endpoint bound; 4845 complementary rank checks; qualitative conditional continuity.
OPEN: an explicit nonzero-R collision stability bound; global D5 labeling/proximity; Type E/C/D/generic e>=27; tau_5=40.
RETAINED: 40<=tau_5<=44; M(F3)<=89; M(P)>=S/2-28/3; 20-edge mass>=2137/6; A<=383/504. The sparse e=23/e=24 classification requires delta(G)>=1.
