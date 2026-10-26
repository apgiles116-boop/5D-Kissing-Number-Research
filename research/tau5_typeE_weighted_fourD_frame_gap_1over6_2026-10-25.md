# Type E: weighted four-dimensional LP improves outside-sixteen frame gap to 1/6

**Date:** 2026-10-25. **[PROVED EXACTLY]** standalone theorem below. **[CONDITIONAL ON RETAINED TYPE-E RESULTS]** application to Type E. **[OPEN]** Type-E exclusion and full five-dimensional kissing number.

## Theorem [PROVED EXACTLY]

For sixteen vectors z_i in R^5 satisfying ||z_i||^2=1-a_i, 0<=a_i<=1/4, sum a_i<=383/504, and |z_i.z_j|<=1/2 (i!=j),

**F_O=sum_i z_i z_i^T is strictly greater than I_5/6.**

This more than doubles the previous certified 1/13 constant, without a D5-template assumption or a new SDP.

## Proof

Suppose a unit x has B=sum_i (x.z_i)^2<=delta=1/6. Put q_i=(x.z_i)^2, c_i=1-a_i, w_i=z_i-(x.z_i)x, and b_i=||w_i||^2=c_i-q_i>=7/12. Then u_i=w_i/sqrt(b_i) lie on S^3.

The polynomial f(t)=t^4-t^2/4 has the positive Gegenbauer expansion

f(t)=(1/16)C_0^(1)(t)+(1/8)C_2^(1)(t)+(1/16)C_4^(1)(t).

Applying the Gegenbauer positive-definite kernel to the u_i with positive weights b_i^2 gives the **weighted** lower bound

sum_(i<j) [(w_i.w_j)^4-(b_i b_j/4)(w_i.w_j)^2] >= R(b),

R(b)=(sum b_i^2)^2/32-(3/8)sum b_i^4. (1)

Unlike the previous normalized argument, this quartic has no normalization denominators.

For i!=j, |w_i.w_j|<=1/2+p_ij, where p_ij=sqrt(q_i q_j)<=delta/2. For h(t)=t^4-(b_i b_j/4)t^2, convexity in t^2 and h(1/2+p_ij)>=0 give

h(w_i.w_j) <= (1-b_i b_j)/16
 + (1/2-b_i b_j/4)p_ij
 + (3/2-b_i b_j/4+2p_ij+p_ij^2)p_ij^2. (2)

The constant term is at most (1-c_i c_j+c_i q_j+c_j q_i)/16. Since b_i>=(1-delta-a_i), the linear-p coefficient is at most

47/144+(5/24)(a_i+a_j).

The quadratic-p coefficient is at most 241/144. From sum a_i^2<=A/4<=383/2016<49/256, Cauchy-Schwarz yields

sum_(i<j) p_ij <= (15/2)B,
sum_(i<j) (a_i+a_j)p_ij <= 4 sqrt(sum a_i^2) B <= (7/4)B,
sum_(i<j) q_i q_j <= B^2/2.

Summing (2) therefore gives

sum_(i<j) h(w_i.w_j) <= U(c)+(15/4)B+(241/288)B^2, (3)

where U(c)=sum_(i<j)(1-c_i c_j)/16. The linear coefficients combine exactly as 15/16+235/96+35/96=15/4.

Next, partial R/partial b_i=(b_i/8)sum_j b_j^2-(3/2)b_i^3 <= 2b_i-(3/2)b_i^3 <= 8/9 for 0<=b_i<=1. Integrating coordinatewise gives

R(b)>=R(c)-(8/9)B. (4)

Thus any counterexample must satisfy

D(a):=R(c)-U(c) <= (167/36)B+(241/288)B^2. (5)

We minimize D exactly over the midpoint deficits. With A=sum a_i and S_k=sum a_i^k,

32D=64-46A+5A^2-4AS_2-41S_2+S_2^2+48S_3-12S_4. (6)

D decreases strictly as any a_i increases: writing C_1=sum c_i>=12 and C_2=sum c_i^2>=9,

partial D/partial c_i = C_2 c_i/8+C_1/16-c_i/16-(3/2)c_i^3
 >= (17/16)c_i+3/4-(3/2)c_i^3 >=5/16>0

for 3/4<=c_i<=1. At fixed A, D is strictly Schur-concave, since

(partial_i D-partial_j D)/(a_i-a_j)
=[-8A+4S_2-82+144(a_i+a_j)-48(a_i^2+a_i a_j+a_j^2)]/32
<=-9/32<0,

using S_2<=1/4 and a_i+a_j<=1/2. Therefore D is minimized at the concentrated vertex

a*=(1/4,1/4,1/4,5/504,0,...,0),

where exact arithmetic gives

D(a)>=D(a*)=1665618603949/2064772104192.

For B<=1/6, the right side of (5) is at most

167/216+241/10368=8257/10368.

The exact positive contradiction margin is

D(a*)-8257/10368 = 21249076141/2064772104192 >0.

This proves F_O strictly greater than I_5/6. QED.

## Type-E consequence [CONDITIONAL]

For H=16K2 disjoint-union F3, the retained Type-E results ensure the sixteen outside-core projected vectors satisfy the theorem. The retained two-sided safe-endpoint inequalities imply

2H_184 >= tr(T_O F)+tr(T_C F_O) >= tr((T_O+T_C)F_O)>A/6 when A>0.

Hence **H_184 >= A/12**, strict for A>0. This improves the former coercivity inequality A/26 but is weaker numerically than the separate energy-sensitive Q-rank absolute safe-slack floor.

**[OPEN]** This does not force A>383/504 and does not eliminate Type E. Types C and D, generic e>=27, and non-isolated cases remain open.

**[UNCHANGED]** 40<=tau_5<=44; M(F3)<=89; M(P)>=S/2-28/3; A<=383/504. Sparse e=23/24 classification remains conditional on minimum degree >=1. The audited Musin/Boyvalenkov 21-line zero-midpoint exclusion is retained.

An expanded mathematical note and exact symbolic/rational verifier were generated with this result.