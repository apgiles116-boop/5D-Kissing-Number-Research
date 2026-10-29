# Type E: sharpened pair normalization and conditional A > 1/86 (2026-10-29)

**[PROVED EXACTLY under explicit Type-E endpoint hypotheses and the retained 21-line P>1/58 theorem]**. **[CONDITIONAL TYPE-E CONSEQUENCE]**. No Type-E elimination. Global proved range remains 40 <= tau_5 <= 44.

Let x_i^±=m_i±z_i for the twenty selected deep edges, a_i=||m_i||², w_i=||z_i||²=1-a_i, A=sum a_i, r=1-A, u_i=z_i/sqrt(w_i). Add isolated center u_0. Among the 190 edge pairings, 184 are two-sided safe and the remaining six lie in the four-edge F3 core. Its three perfect matchings have deep-core incidence K4 or K4 minus one edge; each core pair has two safe endpoint contacts with equal sign product, giving |z_i.z_j|<=1/2+sqrt(a_i*a_j). All these hypotheses are essential.

Define P=sum_{0<=i<j<=20}[t_ij²(t_ij²-1/4)]_+, t_ij=|u_i.u_j|. The retained independent universal theorem gives P>p=1/58.

## New exact pair-normalization inequalities

For a safe pair with e=z_i.z_j and W=w_i*w_j=1-(a_i+a_j)+a_i*a_j >= r,

    [t²(t²-1/4)]_+ <= e²*(1-W)/(4W²)
                       <= (a_i+a_j)*e²/(4r²).          (1)

The previous bridge used r^4 rather than r². For a core pair,

    T=(1+A)/(2sqrt(r)),
    t<=T,
    [t-1/2]_+ <= [sqrt(a_i*a_j)+(a_i+a_j)/(2(1+sqrt(r)))]/sqrt(r). (2)

Here 1-sqrt(W)=(1-W)/(1+sqrt(W)). This halves the leading linear normalization loss in the core. Center contribution is <=A/(16r²).

## New frame-feedback bridge

Put Z=sum_i z_i z_i^T, lambda=lambda_max(Z). From the 21-line Gegenbauer/frame inequality,

    lambda<=21/5+(4sqrt(6)/5)sqrt(P).

For A<=1/86, lambda>2 and sum_{i<j}(a_i+a_j)(z_i.z_j)² <= A(lambda-1). Every deep-incidence core pair satisfies |z_i.z_j| >= 1/2-sqrt(2A)-A/2; set c=(1/2-sqrt(2A)-A/2)²>0.

Let k=T²(T+1/2)/(2sqrt(r)), d=c/(4r²). With four core variables x_i=sqrt(a_i), the core quadratic has off-diagonal entries k and diagonal entries -d*deg_E(i). The worst E is K4 minus one edge, with exact largest eigenvalue k-5d/2+sqrt(4k²+d²/4). Thus its total contribution is at most yR, y=sum_core a_i, where

    R=k*(1+3/(1+sqrt(r)))-5d/2+sqrt(4k²+d²/4).

Here R>0 on A<=1/86: k>=1/8 and 0<=d<=1/(16r0²), while sqrt(4k²+d²/4)>=2k, so R>=3k-5d/2>=3/8-5/(32r0²)>0 (r0=85/86). Hence yR<=AR. Combining the 184 safe blocks, six core pairs, and twenty center pairs proves

    P <= A*[4/(5r²)+1/(16r²)+R]
         + A*sqrt(6)/(5r²)*sqrt(P).                   (3)

This requires neither D5 alignment nor a new SDP.

## Exact rational exclusion of A<=1/86

Set a0=1/86, r0=85/86, s=99/100, U=153/1000, q=27/100, h=161/500. Exact inequalities give s²<r0, U²>2a0, h²>6p. Define

    c0=(1/2-U-a0/2)²,
    T0=(1+a0)/(2s),
    k0=T0²(T0+1/2)/(2s), d0=c0/4.

Then q²>4k0²+d0²/4 exactly. Monotonicity in A, k and d bounds R by

    R0=k0*(1+3/(1+s))-5d0/2+q.

Set C0=a0*[4/(5r0²)+1/(16r0²)+R0], D0=a0/(5r0²). Equation (3) implies P<=C0+sqrt(6)*D0*sqrt(P). Since P>p, necessarily p<C0+D0*sqrt(6p). But exact Fraction arithmetic gives

    p-C0-D0*h
      = 9329200545913122660407 / 324578490573724679952000000 > 0,

contradicting h>sqrt(6p). Therefore

    **[CONDITIONAL TYPE-E THEOREM] 1/86 < A <= 383/504.**

The prior floor was A>1/98. This is an exact ~14% increase in the lower endpoint, but far short of excluding Type E.

**[RETAINED, NOT REPROVED]** Universal P>1/58; 16K2+F3 reduction; star sum<=70/3; broom M(F3)<=89; matching M(P)>=S/2-28/3; A<=383/504; Musin/Boyvalenkov zero-midpoint exclusion.

**[OPEN]** Types C, D, generic e>=27 and non-isolated branch. Sparse e=23/e=24 classification still conditional on delta(G)>=1. Need a stronger global 184-block weighted inequality to force A>383/504.

Companion exact Fraction verifier: research/tau5_typeE_sharpened_normalization_A_gt_1over86_2026-10-29_verify.py.
