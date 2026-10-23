# Type E: balanced quotient triangle in every F3 perfect matching (2026-10-23)

**Status: [PROVED EXACTLY] finite graph certificate and Euclidean vector lemma; [CONDITIONAL ON RETAINED TYPE-E REDUCTION] application to selected F3 deep edges; [OPEN] Type E exclusion.** Global proved range remains 40 <= tau_5 <= 44.

## Exhaustive F3 matching certificate

For F3 edges `02,04,05,14,17,23,27,36,56,57`, all perfect matchings (oriented first endpoint +, second -) are:

| Matching | Three unmatched edges representing quotient triangle | Endpoint-sign products |
|---|---|---|
| P1 = 02 / 14 / 36 / 57 | 04,05,17 | -,+,- |
| P2 = 04 / 17 / 23 / 56 | 14,02,27 | -,+,- |
| P3 = 05 / 14 / 27 / 36 | 04,02,17 | -,+,- |

These are **quotient** triangles on three matched-pair indices, not triangles in F3. The product of their three endpoint-sign products is +1. Thus there exist signs eta_i such that beta_ij=eta_i eta_j on the triangle. The companion checker exhausts the 210 four-edge subsets and confirms exactly three perfect matchings and the balanced triangles.

## Exact all-matching vector obstruction

Write the unit endpoints of four matched deep edges as x_i^+ = m_i+z_i and x_i^- = m_i-z_i, with m_i.z_i=0, a_i=||m_i||^2<=1/4, ||z_i||^2=1-a_i. Put

    C=sum_i a_i<=1, d=sum_{i<j}(-m_i.m_j)_+,
    epsilon=C-d, M=sum_i m_i,
    E_ij=a_i+a_j-2|m_i.m_j|>=0.

The exact four-core identity is

    4epsilon=||M||^2+sum_{i<j}E_ij.                   (1)

Fix any balanced quotient triangle on matched-pair indices I, omitting pair h. For its three *actual* F3 cross edges, with endpoint signs sigma_ij,tau_ij and beta_ij=sigma_ij*tau_ij=eta_i*eta_j, expand:

    sum_{ij in triangle} x_i^{sigma_ij}.x_j^{tau_ij}+3/2
      = (1/2)||sum_{i in I}m_i||^2
       +(1/2)||sum_{i in I}eta_i z_i||^2+T,        (2)
    T=sum_{ij in triangle}(sigma_ij z_i.m_j+tau_ij m_i.z_j).

For each cross edge, m_i.z_i=m_j.z_j=0 yields

    |sigma_ij z_i.m_j+tau_ij m_i.z_j|
       <=sqrt(E_ij)(||z_i||+||z_j||)<=2sqrt(E_ij).

Cauchy-Schwarz and (1) imply |T|<=4sqrt(3epsilon). All three actual cross edges are deep (<-1/2), so (2) implies

    (1/2)||sum_{i in I}m_i||^2 < 4sqrt(3epsilon). (3)

Write b_i=||m_i||. Since (b_i-b_h)^2<=E_ih, the triangle inequality in R^4 gives sqrt(C)<=2b_h+2sqrt(epsilon). Also ||M||<=2sqrt(epsilon). Thus

    ||sum_{i in I}m_i||=||M-m_h||
       >=sqrt(C)/2-3sqrt(epsilon).                  (4)

If C=0, (2) immediately contradicts the three strict deep contacts. So C>0. Suppose epsilon<=C^2/4608. As C<=1,

    sqrt(epsilon)<=C/(48sqrt(2))<=sqrt(C)/(48sqrt(2)).

Equations (3)-(4) would force

    (1/2)*(1/2-1/(16sqrt(2)))^2 < sqrt(6)/24,

which is false. Indeed the difference is

    129/1024-sqrt(2)/64-sqrt(6)/24
      >129/1024-(10/7)/64-(49/20)/24
      =169/107520>0,

using sqrt(2)<10/7 and sqrt(6)<49/20.

**Therefore, for EVERY F3 perfect matching in the Type-E deep-endpoint setting,**

    BOXED: C-d > C^2/4608.                           (5)

This is a *second-order* strict slack, not a Type-E exclusion. The previously established all-singleton-specific C-d>1/96 for P2 is stronger, but (5) also covers P1 and P3. No assumption about which matching the mass theorem selects is required.

## Consequence for six-exception 21-line defect estimate

The retained degree-counted estimate contains 4d<=4C-||M||^2. Equation (5) separately gives 4d<4C-C^2/1152. Hence one may use the stronger-of-two penalty, **not their sum**:

    4d<=4C-max(||M||^2,C^2/1152).

With A=sum_{20}||m_i||^2, W=sum_{core}sqrt(a_i)m_i and the retained squared-core defect bound, the previous upper estimate improves to

    P <= 7/[4(1-A)^2] * {
       20A-3C+(1+A)^2[
          7C+C^2-max(||M||^2,C^2/1152)-||W||^2
       ]
    }.                                                (6)

This is an exact, small quadratic tightening valid for the *one mass-selected matching*. It does not contradict the retained A<=383/504, nor the separately retained stronger ceiling A<0.651038.

**Still open:** Type E; Type C/D; generic e>=27; non-isolated 41-code cases; a justified D5 labeling; any six-exception/Q-kernel identification. Sparse e=23/e=24 graph classification still requires delta(G)>=1. Preserve F3 mass <=89, matching mass >=S/2-28/3, and selected 20-edge mass >=2137/6.

Next: insert the matching-uniform slack (5) into the finite polynomial/KKT core optimization without transferring P2-only constraints to P1 or P3.
