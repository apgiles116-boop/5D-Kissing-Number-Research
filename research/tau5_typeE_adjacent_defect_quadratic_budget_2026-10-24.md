# Type E: adjacent raw-defect exclusion and quadratic six-exception budget

**2026-10-24.** [PROVED EXACTLY] universal three-edge inequality. [CONDITIONAL TYPE E] exact six-exception budget and safe-correlation floor. [OPEN] Type E elimination, global D5 labeling, and tau_5.

## Retained inputs

Twenty selected deep edges have endpoints x_i^±=m_i±z_i on S^4, m_i.z_i=0, a_i=||m_i||² in [0,1/4], ||z_i||²=1-a_i, and m_i.m_j+|z_i.z_j|<=1/2 for distinct edges. Define d_ij=(|z_i.z_j|-1/2)_+. Only six core pairs may have positive d_ij. Retain D=sum_core d_ij<=D0=1780062775/4032758016 and A=sum a_i<=B=383/504. The previously verified capped frame floor is L=8790283/317520 for the sum of all 190 squared projected correlations.

## Theorem 1: universal adjacent-defect exclusion [PROVED EXACTLY]

For any distinct i,j,k,

    d_ij+d_ik² <= 1/4,    d_ik+d_ij² <= 1/4.     (1)

Thus two adjacent positive defects a,b obey a+b+a²+b²<=1/2 and a+b<=sqrt(2)-1. In particular d_ij=1/4 forces every other defect incident to i or j to vanish.

**Proof.** When d_ij>0, let s=sign(z_i.z_j). The endpoint inequality gives m_i.m_j<=-d_ij and |z_i.z_j|=1/2+d_ij. Consequently

    ||m_i+m_j||²+||z_i-s z_j||²
      =2+2m_i.m_j-2|z_i.z_j| <=1-4d_ij.

Adding the endpoint inequalities for (i,k),(j,k), and using
|z_j.z_k|>=|z_i.z_k|-|(z_i-s z_j).z_k|, yields

    2d_ik <= |(z_i-s z_j).z_k|-(m_i+m_j).m_k
            <=sqrt(1-4d_ij)*sqrt(||m_k||²+||z_k||²)
            =sqrt(1-4d_ij).

Squaring proves the first inequality; exchange the two pairs for the second. If d_ij=0 the first inequality is immediate from d_ik<=1/4.

For disjoint core pairings ij,kl, Cauchy and the midpoint-energy ceiling also give

    d_ij+d_kl <= (a_i+a_j+a_k+a_l)/2 <= B/2.    (2)

## Theorem 2: quadratic budget [CONDITIONAL TYPE E; EXACT PROOF]

Put alpha=(sqrt(2)-1)/2, so alpha+alpha²=1/4. Then

    sum_six d_ij² <= alpha D0 = 0.091417107145425... .    (3)

**Proof.** Let t=max d_ij. If t<=alpha, sum d²<=tD<=alpha D0. Otherwise t in [alpha,1/4]. Each of the other five core edges is either adjacent to the maximizer or its unique disjoint edge, so its defect is at most h(t)=max(sqrt(1/4-t),B/2-t). Thus sum d²<=max(F_s(t),F_d(t)), where

    F_s(t)=t²+(D0-t)sqrt(1/4-t),
    F_d(t)=t²+(D0-t)(B/2-t).

Set s=sqrt(1/4-t). The derivative of F_s with respect to s is

    4s³+3(s-1/6)²+D0-1/3 >0.

Hence F_s decreases as t increases and F_s(t)<=F_s(alpha)=alpha D0. F_d is convex (second derivative 4); at t=alpha it is <=alpha D0 since B/2<=2alpha. At t=1/4, use D0<9/20, B/2-1/4<13/100, D0>11/25 and alpha>207/1000 to get

    F_d(1/4)<177/2000< (207/1000)(11/25)<alpha D0.

This proves (3). The bound is certified but not claimed sharp.

## Theorem 3: safe squared-correlation floor [CONDITIONAL TYPE E]

For six exceptional candidates, |z_i.z_j|²<=(1/2+d_ij)²=1/4+d_ij+d_ij². Combining (3) with the capped frame floor yields

    sum_184_safe (z_i.z_j)² >= K_new
      = L-3/2-(1+alpha)D0
      = 1047044579149/40327580160
        -1780062775*sqrt(2)/8065516032
      = 25.651368875925075... .                     (4)

The previous bound was K_old=2067388216673/80655160320=25.632435773..., so the exact improvement is D0*(1/4-alpha)=0.018933102806... . The previously retained nonnegative frame-variance, concentration, and unused-energy corrections remain available.

**At most two positive defects:** Adjacent defects obey sum(d+d²)<=1/2 by (1). Disjoint defects obey sum(d+d²)<=5B/8<1/2 by (2). Thus in this branch sum_184_safe (z_i.z_j)² >=L-2=25.684186822877... .

## Next finite polynomial problem [OPEN]

For six variables d_ij indexed by edges of K4, maximize sum(d_ij+d_ij²) subject to 0<=d_ij<=1/4, sum d<=D0, adjacent inequalities d_ij+d_ik²<=1/4 in both orientations, and opposite-edge inequalities d_ij+d_kl<=B/2. This is a necessary six-variable quadratic relaxation, not a full rank-five geometric feasibility test.

## Status ledger

[PROVED EXACTLY] (1), (2), and the algebraic optimization of (3). [CONDITIONAL TYPE E] (3), (4), the two-defect branch. [OPEN] Type E, C, D, generic e>=27, global D5 labeling, and non-isolated branches. [UNCHANGED] 40<=tau_5<=44, M(F3)<=89, matching M(P)>=S_F3/2-28/3, A<=383/504; e=23/24 graph classification remains conditional on delta(G)>=1.

Companion exact checker: tau5_typeE_adjacent_defect_quadratic_budget_2026-10-24_verify.py.
