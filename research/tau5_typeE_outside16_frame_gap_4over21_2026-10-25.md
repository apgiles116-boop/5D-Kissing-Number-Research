# Type E: outside-sixteen frame gap improved to 4/21 (25 October 2026)

**[PROVED EXACTLY]** Standalone theorem under the vector hypotheses below. **[CONDITIONAL ON RETAINED TYPE-E CERTIFICATES]** Application to Type E. **[OPEN]** Exclusion of Type E, and determination of tau_5.

## Theorem

For z_1,...,z_16 in R^5 with ||z_i||^2=1-a_i, 0<=a_i<=1/4, sum a_i<=383/504, and |z_i.z_j|<=1/2 (i!=j),

    F_O=sum_i z_i z_i^T  > (4/21) I_5

in the positive-definite sense. This improves the prior 3/16 gap without any D5 labeling or generic SDP.

## New exact mixed-projection lemma

For q_i>=0, B=sum_i q_i, p_ij=sqrt(q_i q_j),

    sum_{i<j} (q_i+q_j) p_ij <= sqrt(n-1) B^2/2.

Indeed the left side is sum_i q_i^(3/2) sum_{j!=i} sqrt(q_j). Cauchy gives sum_{j!=i}sqrt(q_j)<=sqrt((n-1)(B-q_i)), while sqrt(q_i(B-q_i))<=B/2. For n=16, sqrt(15)/2<31/16, so the sum is <=(31/16)B^2. This improves the previous 3B^2 estimate.

## Weighted Gegenbauer proof

Suppose some unit x has B=sum_i(x.z_i)^2<=4/21. Write q_i=(x.z_i)^2, c_i=1-a_i, w_i=z_i-(x.z_i)x, b_i=||w_i||^2=c_i-q_i>=47/84>0. The polynomial f(t)=t^4-t^2/4 has nonnegative Gegenbauer coefficients on S^3:

    f(t)=C_0^(1)(t)/16+C_2^(1)(t)/8+C_4^(1)(t)/16.

Applying it to w_i/sqrt(b_i) with weights b_i^2 gives

    sum_{i<j}[(w_i.w_j)^4-(b_i b_j/4)(w_i.w_j)^2]
       >= R(b):=(sum b_i^2)^2/32-(3/8)sum b_i^4.

Coordinate differentiation gives R(b)>=R(c)-(8/9)B. Also |w_i.w_j|<=1/2+p_ij. Expanding the quartic at this upper endpoint, using Delta_ij=c_i q_j+c_j q_i-q_i q_j<=q_i+q_j, and discarding only nonpositive terms yields the pairwise bound (5) in the preceding 3/16 note.

The exact deficit-coupled spectral lemma in that note gives

    sum_{i<j}(a_i+a_j)p_ij <= (27/25) B.

The other aggregate bounds are sum(q_i+q_j)=15B, sum p_ij<=15B/2, sum p_ij^2<=B^2/2, sum(q_i+q_j)p_ij^2<=B^3, sum p_ij^3<=B^3/4, sum p_ij^4<=B^4/8. Replacing only the mixed-projection bound gives the necessary inequality

    D(a):=R(c)-sum_{i<j}(1-c_i c_j)/16
       <= (14297/3600)B+(79/64)B^2+(3/4)B^3+(1/8)B^4.

The exact symmetric expansion is

    32D(a)=64-46A+5A^2-4A S2-41S2+S2^2+48S3-12S4,

where A=sum a_i and Sk=sum a_i^k. Its partial derivatives show D decreases as deficits increase and is Schur-concave at fixed A. Hence its minimum on the capped simplex occurs at

    a*=(1/4,1/4,1/4,5/504,0,...,0),

and is exactly D(a*)=1665618603949/2064772104192. The right side of the necessary inequality increases with B>=0. At B=4/21 the exact contradiction margin is

    1665618603949/2064772104192
     -[(14297/3600)(4/21)+(79/64)(4/21)^2
       +(3/4)(4/21)^3+(1/8)(4/21)^4]
     =4997736421/51619302604800 >0.

Therefore B>4/21 for every unit x, proving F_O>(4/21)I_5.

## Type-E application [CONDITIONAL]

For the 16 outside-core selected deep edges in H=16K2 disjoint_union F3, let A=sum_{i=1}^{20}||m_i||^2 and H_184 be the 184 graph-safe squared projective slacks. Retained two-sided endpoint inequalities give

    2 H_184 >= tr(T_O F)+tr(T_C F_O)
            >= tr(T F_O) > (4/21) A  (A>0).

Thus H_184 >= (2/21)A, strictly for A>0. The earlier absolute Q-rank lower bound on H_184 is stronger numerically. This is a frame-coercivity improvement, not a Type-E exclusion.

**[UNCHANGED]** 40<=tau_5<=44; M(F3)<=89; M(P)>=S/2-28/3; A<=383/504. Types C,D, generic e>=27, and non-isolated cases remain open. The 21-line zero-midpoint exclusion uses the audited Musin/Boyvalenkov result; sparse e=23/24 classification remains conditional on delta(G)>=1.
