# Type E: adjacent-defect ellipse and a sharper six-core square budget

**2026-10-24. [PROVED EXACTLY, conditional on retained Type-E hypotheses].** No Type-E elimination; global proved range remains 40 <= tau_5 <= 44.

## Setup

For the 20 disjoint deep edges write x_i^±=m_i±z_i, a_i=||m_i||²<=1/4, A=sum a_i<=B=383/504, ||z_i||²=1-a_i, m_i·z_i=0. Let r_ij=|z_i·z_j| and δ_ij=(r_ij-1/2)_+. Only the six pairings among four distinguished core edges can have δ_ij>0; D=sum δ_ij<=D0=1780062775/4032758016.

Averaging the four cross-endpoint kissing inequalities x_i^σ·x_j^τ<=1/2 gives

    m_i·m_j + |z_i·z_j| <= 1/2.                       (1)

Thus if δ_ij>0, m_i·m_j<=-δ_ij and δ_ij<=sqrt(a_i a_j)<=1/4.

## Adjacent-defect ellipse [PROVED EXACTLY]

For any three distinct selected edges i,j,k,

    δ_ik² + (3/2)δ_ij <= 3/8.                         (2)

If δ_ij=d>0, reorient z_j so z_i·z_j=1/2+d. Then a_i+a_j>=2d and m_i·m_j<=-d, whence

    ||m_i+m_j||² <= (1-4d)/2,
    ||z_i-z_j||² <= 1-4d.

If δ_ik=e>0, applying (1) to ik and jk and the reverse triangle inequality gives

    2e <= sqrt(1-4d) [sqrt(a_k/2)+sqrt(1-a_k)]
       <= sqrt(3/2) sqrt(1-4d).

Squaring proves (2). If d=0 or e=0, (2) follows from δ<=1/4. Interchanging j,k gives δ_ij²+(3/2)δ_ik<=3/8. Adding and using d²+e²>=(d+e)²/2 gives

    δ_ij+δ_ik <= (sqrt(15)-3)/2 = 0.4364916731... . (3)

For four distinct edges, AM-GM and the midpoint budget give

    δ_ij+δ_kl <= (a_i+a_j+a_k+a_l)/2 <= B/2
               = 383/1008.                           (4)

Therefore **at most one of the six raw exceptional defects can exceed**

    t_*=(sqrt(15)-3)/4 = 0.218245836551854... .      (5)

These are exact second-order semialgebraic incidence constraints; no D5 labeling or SDP is assumed. Sharpness for realizable Type E is not asserted.

## Exact six-core square budget [PROVED EXACTLY]

The old convex-only estimate was sum δ² <= 1/16+(D0-1/4)² = 0.0991342814787...

Combining (2),(4), δ<=1/4 and D<=D0 gives the stronger bound

    sum_{six core pairings} δ_ij² < 12/125 = 0.096. (6)

An exact rational case certificate follows. Let x=max δ. For x<=27/125, sum δ²<=xD0<12/125. For 27/125<x<=219/1000, the capped-simplex maximum is 2x²+(D0-2x)², increasing and <12/125 at the right endpoint.

For the remaining intervals (l,h], every other defect is at most the displayed rational cap c:

| l | h | c |
|---|---|---|
| 219/1000 | 11/50 | 27/125 |
| 11/50 | 223/1000 | 1061/5000 |
| 223/1000 | 9/40 | 101/500 |
| 9/40 | 23/100 | 97/500 |
| 23/100 | 6/25 | 87/500 |
| 6/25 | 1/4 | 7/50 |

Indeed c²>(3/8)(1-4l) by (2), and c>B/2-l by (4). Moreover c<D0-h<=D0-x<=D0-l<2c. The capped-simplex maximum for the other five defects is c²+(D0-x-c)². Hence in each row

    sum δ² <= h²+c²+(D0-l-c)² < 12/125.

All inequalities are exact rational comparisons in the companion checker.

## Strengthened 184-safe mass transfer [PROVED EXACTLY]

Retain the earlier exact frame identity and floor

    S_raw=sum_{i<j}(z_i·z_j)²
         >= F0 + (1/2)||Delta-W||_F²,
    F0=8790283/317520,

where v_i=z_i/sqrt(1-a_i), Delta=sum_i(v_iv_i^T-I/5), W=sum_i a_i(v_iv_i^T-I/5).

Since each of the six designated core squared correlations obeys r_ij²<=1/4+δ_ij+δ_ij², (6) gives

    S_core < 3/2+D0+12/125
           = 1027043071067/504094752000
           = 2.0374008398068...

and therefore

    S_safe > 12928410219733/504094752000
             + (1/2)||Delta-W||_F²
           = 25.6467859830705... + (1/2)||Delta-W||_F². (7)

This improves the preceding safe floor by 0.0031342814787..., but does not increase the retained >=76 count of raw-safe pairs with |z_i·z_j|>1/4. With C0=133562881183/362948221440 and T=||Delta||_F²/2, the second-order remainder in (7) is at least (sqrt(2T)-sqrt(C0))_+²/2.

**[OPEN]** Type E elimination, Types C/D, generic e>=27, and any reduction of 40<=tau_5<=44. Retain M(F3)<=89, M(P)>=S/2-28/3, A<=383/504 and the audited Musin--Boyvalenkov zero-midpoint exclusion. Next step: add the adjacent polynomial cuts to the four-core rank-five Gram/KKT problem.
