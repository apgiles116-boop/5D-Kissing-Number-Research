# A quantitative 21-line integrality gap in dimension five

Date: 2026-10-31. **Status: PROVED EXACTLY** for the statements below. **Type E remains OPEN. Global proved range: 40 <= tau_5 <= 44.**

## Theorem A (universal 21-line positive-defect gap)

For any 21 unit vectors u_0,...,u_20 in R^5, let b_ij=(u_i·u_j)^2 and

P = sum_{i<j} [ b_ij (b_ij - 1/4) ]_+,
D = sum_{i<j} (|u_i·u_j| - 1/2)_+.

Then **P > 1/103** and **D > 2/309**. These are explicit conservative constants, not asserted optimal.

### Exact proof

In dimension five, the normalized positive-definite spherical polynomials are

P_2(t)=(5t^2-1)/4,
P_4(t)=(21t^4-14t^2+1)/8.

The identity

t^4-t^2/4 = 1/28 + P_2(t)/3 + 8P_4(t)/21

and the spherical-harmonic addition theorem imply the following. Write T=sum_i u_i u_i^T, B=T-(21/5)I, V=||B||_F^2, and H_4=sum_{i,j}P_4(u_i·u_j)>=0. Since sum_{i,j}P_2(u_i·u_j)=5V/4 and 21^2/28=21*(3/4), the off-diagonal sum is

F=sum_{i<j} b_ij(b_ij-1/4) = 5V/24+4H_4/21 >=5V/24.     (1)

Let N be the total negative part of this sum, so F=P-N. In particular V<=24P/5.

Round b_ij to k_ij/4 with k_ij=0 if b_ij<=1/8 and k_ij=1 otherwise. The elementary inequalities

|b-k/4| <= 8[-b(b-1/4)] for 0<=b<=1/4,
|b-1/4| <= 4b(b-1/4) for b>1/4,

give, for E=sum_{i<j}|b_ij-k_ij/4|,

E <=8N+4P =12P-8F <=12P-5V/3.                  (2)

Assume P<=1/103. Then 0<=V<=24/515<1/20. The exact trace identity is

2 sum_{i<j} b_ij =336/5+V=67+1/5+V,

whereas 2 sum_{i<j} k_ij/4 is a half-integer. Because V<1/20, its nearest half-integer is 67. Therefore

1/5+V <=2E <=24P-10V/3,

which implies

0<=V <= (3/13)(24P-1/5) <= v_*=51/6695.        (3)

For each i, let k_i=sum_{j!=i}k_ij be an integer, e_i=sum_{j!=i}|b_ij-k_ij/4|, and d_i=u_i^T B u_i. Since

sum_{j!=i} b_ij =16/5+d_i

and 16/5 is at least 1/20 away from every integer multiple of 1/4,

sum_i |d_i| >=21/20-sum_i e_i >=21/20-24P+10V/3
            >= L_0+10V/3,   L_0=1683/2060.     (4)

Cauchy-Schwarz, the positivity of T, and the trace-zero spectral inequality ||B||_op<=sqrt(4V/5) give

sum_i |d_i| <=sqrt(21 sum_i d_i^2)
 <=sqrt(21 tr(B^2 T))
 <=sqrt(21(21/5+sqrt(4V/5))V).

By (3), sqrt(4V/5)<1/12. Thus

sum_i |d_i| < sqrt((1799/20)V).                 (5)

But h(V)=(L_0+10V/3)^2-(1799/20)V is strictly decreasing on [0,v_*], and

h(v_*)=17500837/717168400>0.

This contradicts (4)-(5). Hence P>1/103. For s in [1/2,1], s^2(s^2-1/4)<=(3/2)(s-1/2), so P<=(3/2)D, proving D>2/309.

In particular, 21 projective lines in RP^4 cannot all have coherence <=1/2. This supplies an independent explicit integrality/equality-case proof of the zero-midpoint boundary, consistent with the previously audited Musin/Boyvalenkov theorem.

## Theorem B (midpoint/defect tradeoff for twenty selected deep pairs)

Let x_0 be a unit vector and z_i the half-differences of twenty selected disjoint deep edges, with ||z_i||^2=1-a_i, 0<=a_i<=1/4 and A=sum_{i=1}^{20}a_i. Set z_0=x_0. Define the raw defect over ALL 210 pairs

D_raw=sum_{0<=i<j<=20}(|z_i·z_j|-1/2)_+.

Then

**D_raw+5A>1/206.**                                  (6)

Proof: For 0<=a,b<=1/4, the exact elementary bound is

1/sqrt((1-a)(1-b)) <=1+2(a+b)/3.                 (7)

For s=a+b<=1/4, use (1-a)(1-b)>=1-s and
(1+2s/3)^2(1-s)-1=-s(4s^2+8s-3)/9>=0.
For 1/4<=s<=1/2, use (1-a)(1-b)>=15/16-3s/4 and
(1+2s/3)^2(15/16-3s/4)-1=-(2s-1)(8s^2+18s-3)/48>=0.

With u_i=z_i/sqrt(1-a_i) and a_0=0, (7) implies pairwise

(|u_i·u_j|-1/2)_+ <= (4/3)(|z_i·z_j|-1/2)_+ +(a_i+a_j)/3.

Each of the twenty nonzero a_i occurs in exactly twenty pairs, so D<=(4/3)D_raw+(20/3)A. Apply D>2/309 to obtain (6).

In the retained Type-E labeling, only six of the 190 selected-edge pairings can exceed the raw 1/2 threshold. Writing D_C for their defect and D_0 for the twenty center-to-edge raw defects gives

**D_C+D_0+5A>1/206.**                               (8)

The center defects cannot be discarded without an additional proof. If all 210 raw correlations are <=1/2, then A>1/1030. This is a quantitative boundary separation, NOT an exclusion of Type E.

## Theorem C (coplanar core mass/defect/variance bridge)

Suppose the four Type-E core projected vectors lie in a plane, and retain the certified Type-E raw defect cap D_C <= 1780062775/4032758016 < 1/2. Write A_C=sum_C a_c, U_C=sum_C a_c^2, and V_z=||sum_C z_c z_c^T-(4-A_C)P_plane/2||_F^2. For the six core raw defects d_cd=(|z_c·z_d|-1/2)_+, let D_C=sum d_cd and

Phi(d)=d^2 for 0<=d<=1/4;
Phi(d)=1/16+(d-1/4)^2 for 1/4<=d<=1/2.

The exact rank-two frame identity and d_cd<=1/4 imply

**D_C+Phi(D_C) >= 1/2-A_C+A_C^2/4-U_C/2+V_z/2
               >= 1/2-(9/8)A_C+A_C^2/4+V_z/2.**    (9)

Indeed sum_{c<d}(z_c·z_d)^2=2-A_C+A_C^2/4-U_C/2+V_z/2, whereas it is at most 3/2+D_C+sum d_cd^2 <=3/2+D_C+Phi(D_C). Use U_C<=A_C/4.

In particular D_C=0 implies A_C>1/2. Equality A_C=1/2 would require two a_c=1/4, two a_c=0, and all six |z_c·z_d|=1/2. The Gram determinant for a triple of projected squared lengths (3/4,1,1) and these correlations is 1/16+eta/4, eta=+1 or -1, hence either 5/16 or -3/16, never zero. This is impossible for three planar vectors.

## Ledger

**PROVED EXACTLY:** Theorems A-C, with explicit rational and algebraic certificates. Companion Python/SymPy verification checks polynomial identities, margins, and rational samples; it does not certify Type-E feasibility.

**OPEN:** None of these bounds contradicts A<=383/504 or D_C<=1780062775/4032758016. The most useful next target is a contact-sensitive replacement for the coarse 5A normalization penalty, coupled to signed F3/Walsh constraints.

**RETAINED, NOT REPROVED:** M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, the exact raw/homogeneous defect ceilings, D5/Q facts, and Musin/Boyvalenkov. Sparse e=23/24 classification remains conditional on delta(G)>=1. Types C, D, E, generic e>=27 and non-isolated branches remain open. Global proved range **40<=tau_5<=44**.