# Type E safe-pair audit and repaired 16-line leakage (2026-11-01)

**[PROVED EXACTLY — rational counterexample and corrected standalone theorem].** **[CONDITIONAL TYPE E]** The Type-E application assumes the retained isolated-center/F3 certificate x=sum_I a_i<11/400; it is not re-proved here. **[OPEN]** No Type-E exclusion; 40<=tau_5<=44.

## 1. An invalid implication in the earlier 16-line notes

For a deep edge with unit endpoints u_i^s=m_i+s*z_i, s=+/-1, one has m_i.z_i=0, a_i=||m_i||^2, ||z_i||^2=1-a_i. Four safe cross-edge endpoint products imply

    m_i.m_j + |z_i.z_j| <= 1/2,
    |z_i.z_j| <= 1/2 + sqrt(a_i*a_j).                       (1)

They do NOT imply |z_i.z_j|<=1/2 without the extra, unproved condition m_i.m_j>=0.

**[EXACT RATIONAL COUNTEREXAMPLE]** In R^5 let

    z1=(9,3,3,0,0)/10; z2=(1,7,7,0,0)/10;
    m1=(0,0,0,1,0)/10; m2=(0,0,0,-1,0)/10.

Then ||z1||^2=||z2||^2=99/100, a1=a2=1/100, z1.z2=51/100>1/2, and m1.m2=-1/100. Every cross-edge endpoint product equals -1/100 +/- 51/100 and is <=1/2. Each within-edge product is -49/50<-1/2. The total midpoint mass is 1/50<11/400. Hence the inference fails even in the small-mass regime.

**[AUDIT]** The earlier stronger 16-line spectral inequalities proved under the extra hypothesis |z_i.z_j|<=1/2 remain valid *as standalone conditional lemmas*, but their claimed Type-E applications (including 59/50, 429/1000 and the earlier 531/500, 73/200, and downstream two-ray constants) have a missing premise and are **not presently established for Type E**. This is not a counterexample to those numerical bounds themselves.

## 2. Repaired theorem

**[PROVED EXACTLY — standalone].** Suppose z_1,...,z_16 in R^5 satisfy ||z_i||^2=1-a_i, 0<=a_i<=1/4, x=sum a_i<11/400, and |z_i.z_j|<=1/2+sqrt(a_i*a_j) for i!=j. For every 3-plane W and every 4-plane W respectively,

    L(W)=sum_i ||P_(W^perp)z_i||^2 > 93/80 = 1.1625,
    L(W) > 83/200 = 0.415.                                (2)

Equivalently, for S_I=sum_i z_i z_i^T with ordered eigenvalues lambda_1>=...>=lambda_5,

    lambda_4+lambda_5>93/80, lambda_5>83/200.              (3)

No D5 labeling, core coplanarity, rank-13 hypothesis, or new SDP is required.

## 3. Proof

For a d-plane W, d=3 or 4, put ell_i=||P_(W^perp)z_i||^2, L=sum ell_i, w_i=P_W z_i, b_i=a_i+ell_i, B=sum b_i=x+L, r_i=||w_i||^2=1-b_i. Cauchy and (1) imply

    |w_i.w_j| <= 1/2+sqrt(a_i*a_j)+sqrt(ell_i*ell_j)
               <= 1/2+q_ij, q_ij=sqrt(b_i*b_j).             (4)

Define F_ij=(w_i.w_j)^4-(r_i*r_j/4)*(w_i.w_j)^2. Convexity in v=(w_i.w_j)^2 and r_i*r_j>=1-b_i-b_j give

    F_ij <= (b_i+b_j)/16 + q_ij/4 + (b_i+b_j)*q_ij/4
            + 5*q_ij^2/4 + (b_i+b_j)*q_ij^2/4
            + 2*q_ij^3 + q_ij^4.                            (5)

For 16 nonnegative b_i of sum B, the elementary moment bounds are

    sum_(i<j)(b_i+b_j)=15B,
    sum q<=15B/2, sum q^2<=15B^2/32,
    sum (b_i+b_j)q<=2B^2, sum (b_i+b_j)q^2<=B^3/4,
    sum q^3<=B^3/8, sum q^4<=B^4/16.                       (6)

The mixed q bound follows from Cauchy:
sum_i b_i^(3/2) sum_(j!=i)sqrt(b_j)
<=sqrt(15) sum_i b_i sqrt(b_i(B-b_i))
<=sqrt(15)*B^2/2<2B^2.
The q^2 mixed bound follows from b_i(B-b_i)<=B^2/4, and q^3 from q_ij<=(b_i+b_j)/2. For q^4, maximize sum_(i<j)b_i^2*b_j^2 on the simplex. For two coordinates with fixed sum, its dependence on their product p is p^2-2Rp+constant (R=sum of squares of remaining coordinates), a strictly convex function. Hence at a maximizer all positive coordinates are equal; k equal positive coordinates give (k-1)B^4/(2k^3), maximized at k=2, yielding B^4/16.

Thus

    sum F_ij <= U(B)=45B/16+139B^2/128+5B^3/16+B^4/16.   (7)

The positive harmonic expansions for f(t)=t^4-t^2/4 are

    d=3: f=(7/60)P0+(17/42)P2+(8/35)P4,
    d=4: f=(1/16)U0+(1/8)U2+(1/16)U4,

where P are Legendre and U are Chebyshev second-kind polynomials. Positive-definite harmonic kernels, applied to normalized w_i with weights r_i^2, give

    sum F_ij >= H_d(B)
      =alpha_d/2*(16-2B+B^2/16)^2-(3/8)M(B),              (8)

where alpha_3=7/60, alpha_4=1/16, and M(B)=15+(1-B)^4 for 0<=B<=1, M(B)=14+(2-B)^4 for 1<=B<=2. These use sum r_i^2>=16-2B+B^2/16 and the capped-simplex maximum sum r_i^4<=M(B). Therefore H_d(B)<=U(B).

H_3 decreases on [0,119/100] and H_4 decreases on [0,177/400]; U increases. Indeed differentiating H, the negative term has magnitude >3/2 on each indicated interval and the positive term is <=3/2. If d=3 and L<=93/80, then B<11/400+93/80=119/100, yet

    H_3(119/100)-U(119/100)
      =43441740007/3072000000000 >0.                     (9)

If d=4 and L<=83/200, then B<11/400+83/200=177/400, yet

    H_4(177/400)-U(177/400)
      =666696943297/209715200000000 >0.                  (10)

Both contradict H_d(B)<=U(B). Ky Fan min-max gives (3).

## 4. Proof ledger

**[PROVED EXACTLY]** The counterexample, correct safe-pair implication (1), and repaired geometric theorem (2)-(3); exact fractions independently checked by the companion Python verifier.

**[CONDITIONAL TYPE E]** Using the separately retained x<11/400, the sixteen isolated deep edges satisfy (1), so (2)-(3) apply. Any conditional two-ray or singular-value bound must be recalculated using the repaired constants.

**[OPEN]** This does not force A>383/504 or exclude Type E. Preserve star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, 20-edge mass >=2137/6, global Q-frame correlation floor, and Musin/Boyvalenkov zero-midpoint exclusion. Types C,D, generic e>=27 and non-isolated branches remain open. Sparse e=23/e=24 classification requires delta(G)>=1. Global range 40<=tau_5<=44.

Verifier: research/verify_safe_pair_leakage_2026-11-01.py.
