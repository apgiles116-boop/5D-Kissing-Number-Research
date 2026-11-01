# Type E: coplanar four-core Q-minor gap and midpoint-mass floor

Date: 2026-11-01. **[PROVED EXACTLY — conditional on coplanar four-core Type-E geometry and the retained six-core raw-defect ceiling.]** This is not a Type-E elimination. The global proved range remains **40 <= tau_5 <= 44**.

## Hypotheses

Four selected core projected vectors z_1,...,z_4 lie in a common two-plane of R^5. Write t_i=||z_i||^2=1-a_i, with 0<=a_i<=1/4, q_ij=z_i.z_j, and

D_C=sum_{i<j} (|q_ij|-1/2)_+ <= D_* = 1780062775/4032758016.

Define Q_i=z_i z_i^T-(t_i/5)I_5 and K_ij=<Q_i,Q_j>=q_ij^2-t_i*t_j/5.

## Theorem 1: at most one close core pair

**[PROVED EXACTLY]** Define the projective angle delta_ij=acos(|q_ij|/sqrt(t_i*t_j)) in [0,pi/2]. At most one of the six pairs has delta_ij<=5/18 radians.

For epsilon=5/18, a close pair has |q_ij|>=(3/4)cos(epsilon)>=(3/4)(1-epsilon^2/2). Two such pairs would give

D_C >= 2[(3/4)(1-epsilon^2/2)-1/2] = 191/432 > D_*.

The exact positive margin is 2939033/4032758016. Consequently at least two of the four index triples have all three projective separations >5/18.

## Theorem 2: exact coplanar Q-triple identity

**[PROVED EXACTLY]** For any three planar projected vectors indexed by T={i,j,k},

det(K_T) = (6/5) product_{r<s in T}(t_r*t_s-q_rs^2).     (1)

Proof: In orthonormal trace/difference/off-diagonal coordinates of Sym^2(R^2), the rank-one matrices z_r z_r^T have coordinate rows (t_r/sqrt(2))(1,cos(2theta_r),sin(2theta_r)). The traceless 5D embedding induces metric diag(3/5,1,1). The squared determinant of the three rows is 2 product(t_r*t_s*sin^2(theta_r-theta_s)), by the double-angle Vandermonde identity. Multiplication by 3/5 gives (1).

## Theorem 3: uniform core Q spectral gap

**[PROVED EXACTLY]** Put epsilon=5/18, s0=epsilon-epsilon^3/6=9595/34992, and

d0=(6/5)(3/4)^6*s0^6
  =156062970888364764003125/1719070799748422591028658176
  >9/100000.

For each of at least two well-separated core triples, every factor in (1) exceeds (3/4)^2 sin^2(epsilon), and sin(epsilon)>s0. Hence at least two principal 3x3 Q-Gram determinants are >d0.

The four Q_i belong to the three-dimensional image of Sym^2 of their common plane, so rank(K)<=3. The positive minors prove rank(K)=3 exactly. Write its eigenvalues lambda_1>=lambda_2>=lambda_3>lambda_4=0. The sum of the four 3x3 principal minors equals lambda_1 lambda_2 lambda_3 and exceeds 2d0. Also tr(K)=sum(4/5)t_i^2<=16/5, hence lambda_1 lambda_2<=(tr K/2)^2<=64/25. Therefore

lambda_3(K)>(25/32)d0
=3901574272209119100078125/55010265591949522912917061632
>7/100000.                                                       (2)

This is a label-free conditioning certificate for the three-dimensional core Q span, not a D5 kernel identification.

## Theorem 4: core midpoint-energy floor

**[PROVED EXACTLY]** With A_C=sum_i a_i,

D_C >= 1/2-(8-4sqrt(3))A_C,                              (3)
A_C >= (1/2-D_*)/(8-4sqrt(3)) >1/19.                    (4)

Proof: Order the four unit projective directions around a half-circle; their four cyclic gaps g_r sum to pi. The chord inequality (|cos g|-1/2)_+ >= (3/(2pi))(pi/3-g), valid for 0<=g<=pi, shows that the unscaled four cyclic defects sum to at least 1/2. Scaling directions i,j by sqrt(1-a_i)sqrt(1-a_j) decreases a raw defect by at most 1-sqrt(1-a_i)sqrt(1-a_j), which is at most (4-2sqrt(3))(a_i+a_j) for a_i,a_j<=1/4. Every index occurs in two cyclic pairs, giving (3). For (4), use sqrt(3)>19/11, so 8-4sqrt(3)<12/11, and the exact rational margin

(11/12)(1/2-D_*)-1/19 = 996996505/919468827648 >0.

The earlier mass-sensitive four-line bound is stronger at larger A_C; (3) is complementary, not a replacement.

## Status and next task

**[VERIFIED LOCALLY]** Exact rational margins, the Q-triple determinant identity on rational planar examples, four-core rank, and the eigenvalue constant were checked in SymPy/Fraction. The analytic arguments above establish the universal statements.

**[OPEN]** Type E is not excluded. The new Q spectral gap can be used in finite core reconstruction or KKT stability, but a signed F3/184-safe-block upper certificate is still missing. Coplanarity is a branch hypothesis, not assumed for all Type E. Types C,D, generic e>=27, and non-isolated cases remain open; sparse e=23/24 classification still requires delta(G)>=1. Retain M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, both six-core defect caps, and the Musin/Boyvalenkov zero-midpoint boundary theorem. **40<=tau_5<=44.**
