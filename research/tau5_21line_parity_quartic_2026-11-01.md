# Quantitative parity obstruction for 21 projective lines in R^5 (2026-11-01)

**[PROVED EXACTLY — standalone].** This is an independent quantitative derivation of the classical antipodal 21-line obstruction; no novelty claim relative to the literature. **[CONDITIONAL]** A weak six-exception transfer is recorded below. No Type-E exclusion; global range remains 40 <= tau_5 <= 44.

## Theorem

For any 21 unit vectors u_0,...,u_20 in R^5, put

    f(t)=t^4-t^2/4,
    E=sum_{i<j} max(f(u_i.u_j),0).

Then

    E > 1/341.

In particular, at least one |u_i.u_j|>1/2. The linear positive defect Delta=sum_{i<j}(|u_i.u_j|-1/2)_+ satisfies Delta>2/1023, since f(t)_+ <= (3/2)(|t|-1/2)_+ for |t|<=1. This concerns antipodal/projective packings, not the unrestricted kissing number.

## Exact proof

The normalized Gegenbauer polynomials for S^4 are

    P2(t)=(5t^2-1)/4, P4(t)=(21t^4-14t^2+1)/8,

and the exact positive-coefficient identity is

    f(t)=1/28+(1/3)P2(t)+(8/21)P4(t).

Let S=sum_i u_i u_i^T, B=S-(21/5)I_5, b^2=tr(B^2). Gegenbauer positivity gives sum_{ij}P4(u_i.u_j)>=0, and sum_{ij}P2(u_i.u_j)=5b^2/4. The diagonal cancellation 21*f(1)=21^2/28 yields

    sum_{i<j}f(u_i.u_j) >= 5b^2/24.

Writing N=sum_{i<j}max(-f(u_i.u_j),0), we have

    E-N>=5b^2/24, N<=E, b^2<=24E/5, E+N<=2E.  (1)

For x_ij=(u_i.u_j)^2, round each unordered pair symmetrically to q_ij=0 if x_ij<1/8 and q_ij=1/4 otherwise. For all x in [0,1],

    min(x,|x-1/4|) <= 8|x(x-1/4)|.                 (2)

Let k_i=4 sum_{j!=i}q_ij be the degree in the rounded contact graph. The target row sum is

    sum_{j!=i}x_ij = 16/5 + u_i^T B u_i.

The closest quarter-integer to 16/5 is 13/4, at distance 1/20. But 21 vertices cannot all have degree 13: 21*13 is odd while the sum of graph degrees is even. At least one degree differs from 13, and its distance to 16/5 is at least 1/5. Therefore

    6/5 <= sum_i |16/5-k_i/4|
        <= sum_i |u_i^T B u_i| +16(E+N)
        <= sum_i |u_i^T B u_i| +32E.               (3)

For trace-free symmetric 5x5 B,

    tr|B| <= sqrt(24/5)*||B||_F.                   (4)

Proof: if p eigenvalues are positive and q negative, their sums have common magnitude T; Cauchy gives ||B||_F^2>=T^2(1/p+1/q), while pq/(p+q)<=6/5 for p,q>=1 and p+q<=5. Thus (tr|B|)^2=4T^2<=24||B||_F^2/5.

Since |u_i^T B u_i|<=u_i^T|B|u_i,

    sum_i |u_i^T B u_i|
      <= tr(|B|S)
      = (21/5)tr|B|+tr(|B|B)
      <= (21/5)sqrt(24/5)*b+b^2
      <= (504/25)sqrt(E)+(24/5)E.                (5)

Combining (3)-(5) proves the **universal quantitative parity-stability inequality**

    6/5 <= (504/25)sqrt(E)+(184/5)E.             (6)

The right side is strictly increasing. At E=1/341 it is strictly less than 6/5: the exact positive square margin is

    (6/5-184/(5*341))^2 - (504/25)^2/341
      = 56644/72675625 > 0,

and the first parenthesis is positive. Thus E>1/341.

The strict theorem gives a self-contained quantitative version of the 21-line integrality/equality obstruction cited in the retained Musin/Boyvalenkov boundary ledger. It does not establish D5 uniqueness.

## Conditional transfer to Type E

**[PROVED EXACTLY — conditional on the retained 20-edge Type-E decomposition and center safety].** Write each deep edge as m_i +/- z_i, with a_i=||m_i||^2<=1/4 and ||z_i||^2=1-a_i. Normalize u_0=x_0 and u_i=z_i/sqrt(1-a_i) for i=1,...,20. Among these 210 normalized pairings, the raw center and isolated pairings are safe; only six core pairings can exceed raw threshold 1/2.

Let A=sum_{i=1}^{20}a_i, A_C=sum_{four core}a_i, and D_raw=sum_{six core}(|z_i.z_j|-1/2)_+.

For a raw safe pair, with p=(1-a_i)(1-a_j)>=9/16 and v=|z_i.z_j|<=1/2,

    f_+(v/sqrt(p)) <= (1-p)/(16p^2)
                   <= (16/81)(a_i+a_j).

For an exceptional pair, f_+(t)<=(3/2)(|t|-1/2)_+, p^(-1/2)<=4/3 and p^(-1/2)-1<=(2/3)(a_i+a_j) (the latter is separately convex in a_i,a_j and holds at all four corners of [0,1/4]^2). Hence

    f_+(v/sqrt(p)) <= 2(v-1/2)_+ +(a_i+a_j)/2.

Each a_i occurs in 20 of the 210 pairs, and the six exceptional core pairings count each core mass three times. Summation gives the exact bridge

    1/341 < E <= (320/81)A+(49/54)A_C+2D_raw.  (7)

**[OPEN]** This bound is far too weak to contradict the retained A and D_raw ceilings; Type E remains open. To improve it, retain the rowwise rounded-degree parity and the specific six exceptional incidences rather than summing all masses. Do not replace the stronger harmonic/Q-frame or F3 matching certificates with (7).

## Status

**[PROVED EXACTLY, STANDALONE]** Theorem E>1/341 and Delta>2/1023.

**[PROVED EXACTLY, CONDITIONAL TYPE E]** Bridge (7).

**[RETAINED, NOT REPROVED]** Star <=70/3; F3 broom <=89; matching M(P)>=S/2-28/3; twenty-edge mass >=2137/6; A<=383/504; conditional harmonic/Q-frame refinements; Musin/Boyvalenkov antipodal exclusion. Types C,D, generic e>=27, non-isolated branches remain open. Sparse e=23/24 classification requires delta(G)>=1. Global range 40<=tau_5<=44.
