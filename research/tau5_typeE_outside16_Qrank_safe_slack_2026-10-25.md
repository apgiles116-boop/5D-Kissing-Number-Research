# Type E: uniform 16-line squared-slack gap from the rank-14 Q-space

**2026-10-25. [PROVED EXACTLY — universal R5 vector theorem]. [CONDITIONAL TYPE-E APPLICATION]. [OPEN] Type E elimination and improvement to 40 <= tau_5 <= 44.**

## Theorem

Let z_1,...,z_16 in R^5 satisfy b_i=||z_i||^2 in [3/4,1] and r_ij=|z_i.z_j|<=1/2 for i!=j. Write h_ij=1/2-r_ij. Then

    SUM_{i<j} h_ij^2 > 25/224 = 0.111607142857...

No D5 labeling, midpoint-energy sum bound, or generic SDP is needed.

## Exact proof

Let Q_i=z_i z_i^T-(b_i/5)I. Their 16x16 Frobenius Gram K has rank <=14, because the trace-free symmetric 5x5 matrices have dimension 14:

    K_ij = (z_i.z_j)^2-b_i b_j/5.

Define K0 by replacing all off-diagonal raw squared correlations with 1/4:

    K0=diag(b_i^2-1/4)+(1/4)11^T-(1/5)bb^T.

**Claim [PROVED EXACTLY]: K0 >= (5/16) I_16.** Put t_i=b_i-3/4 in [0,1/4]. For any real x put S=sum x_i, T=sum t_i x_i, and D=sum [(3/2)t_i+t_i^2]x_i^2. Direct expansion gives the identity

    x^T(K0-(5/16)I)x
      = D+(11/80)(S-(12/11)T)^2-(4/11)T^2.

Weighted Cauchy yields

    T^2 <= [sum t_i/(3/2+t_i)] D
        <= (2/3)(sum t_i)D <= (8/3)D.

Consequently

    x^T(K0-(5/16)I)x
      >= D/33+(11/80)(S-(12/11)T)^2 >= 0.

The comparison constant 5/16 is sharp: take b_1=b_2=3/4, the other b_i=1, and x=e_1-e_2. This has total midpoint energy 1/2, within the retained Type-E budget 383/504.

Now let E=K0-K. It has zero diagonal and

    E_ij=1/4-r_ij^2=h_ij(1-h_ij)>=0 (i!=j);
    tr(E)=0.

On the at-least-two-dimensional kernel of K, x^T E x=x^T K0 x >= (5/16)||x||^2. By min-max, the two largest eigenvalues of E are >=c=5/16. The other fourteen eigenvalues sum to at most -2c. Thus, by Cauchy,

    tr(E^2) >= 2c^2+(2c)^2/14 = (16/7)c^2.

On the other hand,

    tr(E^2)=2 sum_{i<j} h_ij^2(1-h_ij)^2
           <2 sum_{i<j} h_ij^2.

Strictness follows because E cannot be zero: otherwise K=K0 would have rank 16. Therefore

    sum_{i<j} h_ij^2 > (8/7)(5/16)^2 = 25/224.

**Support corollary [PROVED EXACTLY]:** the graph of pairs with h_ij>0 contains two vertex-disjoint edges. Otherwise it is a weighted star or triangle (plus isolates), whose symmetric weighted adjacency has at most one positive eigenvalue; E has at least two positive eigenvalues.

## Type-E consequence and proof ledger

In H=16K2 disjoint union F3, all 120 outside-outside pairings are raw-safe and each selected deep edge has b_i=1-a_i>3/4. Thus, with H_OO the sum of outside-outside squared safe slacks and H_184 the full 184-safe sum,

    H_184 >= H_OO > 25/224.

This is a new **uniform** positive second-order slack floor, complementary to the retained energy-dependent mixed-frame and outside-16 spectral inequalities. It is **not** a contradiction or Type-E elimination.

**[RETAINED, NOT REPROVED]** M(F3)<=89; matching mass >=S/2-28/3; twenty-edge mass >=2137/6; A<=383/504; six possible exceptional core pairings; audited Musin--Boyvalenkov zero-midpoint exclusion. **[OPEN]** Type E, Types C/D, generic e>=27, non-isolated branches; e=23/24 graph classification conditional on delta(G)>=1. Global proved range: 40<=tau_5<=44.

Verifier: research/tau5_typeE_outside16_Qrank_safe_slack_2026-10-25_verify.py.


## Same-day stronger 17-line theorem and general n=15..19 extension

**[PROVED EXACTLY]** The comparison-matrix argument applies to any n in {15,16,17,18,19} pairwise raw-safe vectors in R5 with b_i=||z_i||^2 in [3/4,1]. The sharper pointwise estimate t_i/(3/2+t_i)<=1/7 for t_i=b_i-3/4 in [0,1/4] gives T^2<=(n/7)D. Therefore

    x^T(K0-(5/16)I_n)x
       >= (1-4n/77)D+(11/80)(S-(12/11)T)^2 >=0

for n<=19, since 1-4n/77>=1/77>0.

The Q-Gram rank remains <=14, so the trace-zero slack matrix E has at least k=n-14 eigenvalues >=c=5/16. Its other fourteen eigenvalues sum to at most -kc. Cauchy and the strict off-diagonal comparison imply the **general exact bound**

    SUM_{i<j}(1/2-|z_i.z_j|)^2
      > (n(n-14)/28)*(5/16)^2
      = 25*n*(n-14)/7168.

For n=15,16,17,18,19 the rational constants are respectively 375/7168, 25/224, 1275/7168, 225/896, 2375/7168.

**[CONDITIONAL TYPE-E IMPROVEMENT]** The sixteen outside-core vectors together with **any one** of the four F3-core vectors form a pairwise raw-safe 17-vector set: exceptional pairings are only core-core. Therefore

    H_184 > 1275/7168 = 0.177873883928571...

This strictly improves the preceding 16-vector application H_184>25/224. It does not eliminate Type E or imply A>383/504; no D5 labeling is assumed. The 16-vector theorem remains useful for outside-only estimates.

Verifier updated with exact n=15..19 rational constants and a 17-line D5 test.
