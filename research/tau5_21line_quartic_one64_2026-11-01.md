# Exact 21-line quartic-defect bound E > 1/64 (2026-11-01)

**[PROVED EXACTLY — standalone]** For any 21 unit vectors u_i in R^5, put x_ij=(u_i·u_j)^2 and E=sum_{i<j}[x_ij(x_ij-1/4)]_+. Then **E>1/64**, and consequently sum_{i<j}(|u_i·u_j|-1/2)_+>1/96. This supersedes the earlier 27/2000 and 9/1000 bounds. It does not prove tau_5=40 or exclude Type E.

## Proof

Set S=sum_i u_i u_i^T, B=S-(21/5)I, t=tr(B^2)>=0, and N=sum_{i<j}[-x_ij(x_ij-1/4)]_+. The Gegenbauer expansion

    s^4-s^2/4 = 1/28 + (1/3)P_2(s) + (8/21)P_4(s)
    P_2=(5s^2-1)/4,  P_4=(21s^4-14s^2+1)/8

and positive definiteness of the harmonic kernels imply

    E-N>=5t/24,   0<=N<=E-5t/24.                   (1)

The frame trace identity gives sum_{i<j} x_ij=168/5+t/2.

Assume E<=1/64. Round each x_ij to q_ij=0 if x_ij<1/8, otherwise q_ij=1/4. Write e for the number of rounded edges. For negative quartic terms y=x(1/4-x), the absolute rounding error equals g(y)=(1-sqrt(1-64y))/8. The function g is increasing, convex, g(0)=0, hence superadditive on sums <=1/64. Their total error is <=g(N). Positive quartic terms contribute at most 4E, because x-1/4<=4x(x-1/4) when x>=1/4. Thus

    R=sum_{i<j}|x_ij-q_ij|<=4E+g(N),
    -g(N)<=168/5+t/2-e/4<=4E+g(N).                (2)

If e<=133, the middle expression is >=7/20+t/2>3/16>=4E+g(N), contradiction. If e>=135, (2) and g'(y)=4/sqrt(1-64y)>=4 give

    3/20-t/2<=g(N)<=g(E-5t/24)
             <=g(E)-5t/6<=1/8-5t/6,

which would force 1/40<=-t/3. Thus **e=134**.

Equation (2) now yields

    1/10+t/2<=1/16+g(1/64-5t/24)
             =3/16-(1/8)sqrt(40t/3),

hence

    t/2+sqrt(40t/3)/8<=7/80.                     (3)

At t=27/1000 the left side equals 177/2000>175/2000=7/80, so **t<27/1000**.

Let k_i be the rounded degrees. Since sum_i k_i=268 and for every integer k>=0,

    |16/5-k/4|>=1/20+(3/20)(13-k),

we have the **integer discrepancy lower bound**

    sum_i|16/5-k_i/4|>=21/20+(3/20)(273-268)=9/5. (4)

But sum_{j!=i}x_ij=16/5+u_i^T B u_i, so

    sum_i|16/5-k_i/4|
      <=sum_i|u_i^T B u_i|+2R
      <=(21/5)tr|B|+t+8E+2g(N).                   (5)

The second inequality uses |u_i^T B u_i|<=u_i^T|B|u_i and tr(|B|B)<=t. For trace-free symmetric 5x5 B, tr|B|<=sqrt(24/5)sqrt(t): if p is the positive eigenvalue sum and k the number of positive eigenvalues, then tr|B|=2p and t>=p^2(1/k+1/(5-k))>=5p^2/6.

Combining (1), (5), E<=1/64, and g(N)<=1/8-sqrt(40t/3)/8 gives

    sum_i|16/5-k_i/4|
      <=[(21/5)sqrt(24/5)-(1/4)sqrt(40/3)]sqrt(t)+t+3/8.

Exact comparisons (21/5)sqrt(24/5)<93/10, sqrt(40/3)/4>9/10, sqrt(27/1000)<33/200, and t<27/1000 yield

    sum_i|16/5-k_i/4|
       <(42/5)(33/200)+27/1000+3/8
       =447/250=1.788<9/5,

contradicting (4). Therefore **E>1/64**. Finally x(x-1/4)<= (3/2)(sqrt(x)-1/2) for x in [1/4,1], giving the linear excess >1/96. QED.

## Proof status and Type-E relevance

**[PROVED EXACTLY — standalone]** The harmonic positivity, rounding, degree count, and rational contradiction are analytic; the companion verifier checks the polynomial identity and rational margins. No D5 labeling, uniqueness claim, or generic SDP is used.

**[CONDITIONAL TYPE E]** Under the previously retained normalized-21-line/six-exception transfer, the improved necessary condition is

    1/64 < (320/81)A+(49/54)A_C+2D_raw.

This does **not** contradict the existing Type-E bounds. The quartic E here is not the Type-E graph label and not D_raw.

**[OPEN]** Type E, C global/boundary, D, generic e>=27, and non-isolated branches. The e=23/e=24 classification requires delta(G)>=1. Preserve M(F3)<=89, M(P)>=S/2-28/3, A<=383/504 and Musin/Boyvalenkov. **Global proved range remains 40<=tau_5<=44.**
