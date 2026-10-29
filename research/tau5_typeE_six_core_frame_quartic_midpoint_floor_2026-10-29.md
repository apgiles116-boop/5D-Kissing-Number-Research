# Type E: six-core sign pattern + 21-line frame feedback gives A > 1/98

Date: 2026-10-29. **[PROVED EXACTLY — under explicit Type-E endpoint and retained universal quartic hypotheses]**. No Type-E elimination. Global proved range remains 40 <= tau_5 <= 44.

## Assumptions and finite F3 check

For 20 selected deep edges write x_i^± = m_i ± z_i, m_i·z_i=0, a_i=||m_i||², w_i=||z_i||²=1-a_i, A=sum a_i. The Type-E graph is 16K2+F3, with an isolated center u0. The 184 pairings outside the six core-core pairings are two-sided safe. The ten F3 deep edges are 02,04,05,14,17,23,27,36,56,57, and its three perfect matchings are 02|14|36|57, 04|17|23|56, 05|14|27|36.

Exact enumeration shows: for every pair of selected F3 matching edges, both contacts of one common endpoint-sign product are safe. At least five of the six core-core pairs have a deep cross-contact. Their deep-core pair graph is K4 or K4 minus one edge (degree sequence 3,3,3,3 or 2,2,3,3).

For a core pair, let c=m_i·m_j, b=m_i·z_j, d=z_i·m_j, e=z_i·z_j. The two same-product safe contacts are c+e±(b+d), or c-e±(b-d). Hence |c±e|+|b±d|<=1/2, proving the new exact bound

    |z_i·z_j| <= 1/2+|m_i·m_j| <= 1/2+sqrt(a_i*a_j).      (1)

In particular the six raw positive excesses sum to at most 3*y/2, where y is the four-core midpoint energy.

## Frame feedback and safe-block accounting

Normalize u_i=z_i/sqrt(w_i), i=1,...,20, and include isolated center u0. Define P=sum_{i<j}[t_ij²(t_ij²-1/4)]_+, t_ij=|u_i·u_j|. The previously proved universal 21-line theorem gives **P>1/58**. Its degree-two Gegenbauer consequence gives V21<=24P/5, so

    lambda_max(Z) <= 21/5+(4*sqrt(6)/5)*sqrt(P),          (2)

where Z=sum z_i*z_i^T; this follows from PSD order Z<=sum u_i*u_i^T and the 5x5 traceless eigenvalue inequality.

Write r=1-A. Each of the 184 safe pairings has quartic contribution at most

    (a_i+a_j)*(z_i·z_j)²/(4*r^4).                         (3)

The 20 center pairs contribute at most A/(16*r²).

For each core pair with a deep cross-contact, the deep endpoint inequality gives |z_i·z_j|>1/2-sqrt(2*A)-A/2. In the strip A<=1/98 set cA=(1/2-sqrt(2*A)-A/2)²>0. Let E be the deep-core pair graph (K4 or K4 minus one edge). Subtracting these core terms from the complete frame row sum yields

    P_safe <= [A*(lambda_max(Z)-1)
               -cA*sum_{(i,j) in E}(a_i+a_j)]/(4*r^4).  (4)

Indeed sum_i a_i*sum_{j!=i}(z_i·z_j)²=sum_i a_i*(z_i^T Z z_i-w_i²), and lambda*w_i-w_i²<=lambda-1 for lambda>=2, w_i<=1.

Put T=(1+A)/(2*r), K=T²*(T+1/2). The six core quartic terms obey

    P_core <= K/r*[sum_{i<j in core}sqrt(a_i*a_j)+3*y/2]. (5)

Let k=K/(2*r), d=cA/(4*r^4), and x_i=sqrt(a_i), so sum x_i²=y. The y-dependent combination of (4),(5) is 3*k*y+x^T B_E x, where B_E has offdiagonal k and diagonal -d*degree_E(i). The worst case is K4 minus one edge. Its symmetric 2x2 block has top eigenvalue

    k-5*d/2+sqrt(4*k²+d²/4).

Therefore the total core contribution is at most y*R(A), where

    R(A)=4*k-5*d/2+sqrt(4*k²+d²/4).                     (6)

R(A)>0 in A<=1/98, so y*R(A)<=A*R(A). Combining (2)-(6) proves the exact **frame-feedback inequality**

    P <= A*[4/(5*r^4)+1/(16*r²)+R(A)]
         +A*sqrt(6)/(5*r^4)*sqrt(P).                     (7)

This requires no D5 alignment or new SDP.

## Exact rational exclusion of A<=1/98

Let a0=1/98, r0=97/98. For A<=a0, k(A)<=k0=23532201/177058562 and d(A)>=d0=4761/153664, since sqrt(2*a0)=1/7 and c(a0)=4761/38416. R increases in k and decreases in d. Exact rational squaring proves

    sqrt(4*k0²+d0²/4) < 267/1000.

Hence R(A)<=R0=4*k0-5*d0/2+267/1000. Bound (7) at a0:

    P <= C0+sqrt(6)*D0*sqrt(P),
    C0=5504307003982407/333292204171808000,
    D0=a0/(5*r0^4).

For P>=p=1/58, division by sqrt(P) gives the necessary p<=C0+D0*sqrt(3/29). But sqrt(3/29)<161/500 and exact arithmetic gives

    1/58-C0-D0*(161/500)
      =2018010242038857/48327369604912160000 > 0.

Contradiction. Thus **A>1/98** under the retained Type-E decomposition and universal quartic theorem.

## Proof-status ledger

**[PROVED EXACTLY]** F3 incidence enumeration, raw-core bound (1), analytic frame-feedback (7), exact rational contradiction. The accompanying verifier checks the finite incidence and rational inequalities.

**[RETAINED, NOT REPROVED HERE]** The universal P>1/58 theorem (its earlier exact checker passed independently), the Type-E graph/matching/mass certificates, and A<=383/504. Their upstream geometric proof obligations remain separate.

**[OPEN]** Type E is not eliminated: the allowed interval is now 1/98<A<=383/504. Type C, Type D, generic e>=27 and non-isolated branches remain open; sparse e=23/24 classification still assumes minimum degree >=1. Preserve M(F3)<=89 and M(P)>=S/2-28/3. No identification of six F3 exceptions with six D5 Q-kernel relations is claimed.
