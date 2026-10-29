# Exact universal 21-line quartic defect improvement: P > 1/61

Date: 2026-10-29.

**[PROVED EXACTLY — standalone]** For 21 unit vectors u_0,...,u_20 in R^5, put s_ij=(u_i dot u_j)^2 and

    P = sum_{i<j} [s_ij(s_ij-1/4)]_+.

Then **P > 1/61**. This improves the retained P>1/64 (2026-10-26), without assuming D5 labeling or using a generic SDP. It is a *normalized quartic defect* bound, not a direct bound on the six raw Type-E exceptions. Global 40<=tau_5<=44 remains unchanged.

## Harmonic, rounding and Q-Gram ingredients

Let F=sum_i u_i u_i^T, Delta=F-(21/5)I, V=tr(Delta^2), and N=sum_{i<j}[-s_ij(s_ij-1/4)]_+. The positive dimension-five Gegenbauer expansion of t^4-t^2/4 gives

    P-N >= (5/24)V,        V <= (24/5)P.              (1)

Round each s_ij to its nearest well r_ij in {0,1/4}, and let K count the rounded 1/4 pairs. For negative quartic energy h=s(1/4-s) in [0,1/64], the rounding error is

    g(h)=1/8-sqrt(1/64-h).

The function g is increasing, convex, g(0)=0, g(1/64)=1/8. By convex mass transfer, the maximum sum of rounding errors with total negative energy E<2/64 is

    G(E)=g(E)                       for E<=1/64,
        =1/8+g(E-1/64)             for 1/64<=E<2/64.

Positive pairs s>1/4 have rounding error <=4s(s-1/4). Assume P<=P0=1/61. By (1), the total pair rounding error L obeys

    L <= 4P+G(N) <= 4P0+G(P0-5V/24) =: L0(V).         (2)

The frame trace gives sum_{i<j}s_ij=168/5+V/2. Let k_i be the rounded contact degree, c_i=k_i/4-16/5, e_i=u_i^T Delta u_i and d_i=e_i-c_i=sum_{j!=i}(s_ij-r_ij). Thus

    |V+336/5-K/2| <= sum_i|d_i| <= 2L0(V).           (3)

For Q_i=u_i u_i^T-I/5, the Q-Gram matrix has diagonal 4/5 and off-diagonal s_ij-1/5. Gershgorin and (s-1/4)_+<=4[s(s-1/4)]_+ imply

    sum_i e_i^2 <= (24/5+4P0)V.                      (4)

## Exact finite Huber/integer-degree certificate

Take lambda=3/10. For every e,c,

    e^2+lambda|e-c| >= h(c),
    h(c)=c^2                      if |c|<=3/20,
        =(3/10)|c|-9/400         otherwise.

The function k -> h(k/4-16/5) is convex on integer degrees. For fixed sum k_i=2K, balanced integer degrees minimize the sum. At K=134, sixteen degrees 13 and five degrees 12 yield H_134=91/400; at K=135, eighteen degrees 13 and three degrees 12 yield H_135=63/400. Combining with (2),(4),

    H_K <= (24/5+4P0)V+(3/5)L0(V).                  (5)

Since V<=24/305 and G(E)<=1/4, 2L0(V)<8/61+1/2<7/10. The integer residual in (3) excludes K<=133 (residual >=7/10) and K>=136 (residual >=4/5-24/305>7/10). Only K=134,135 remain.

Put Vstar=9/2440, where P0-5V/24=1/64. On each interval [0,Vstar] and [Vstar,24/305], L0(V) is convex (G is convex on each branch). Hence the right-hand side of (5) is convex on each branch and has its maximum on any closed subinterval at an endpoint.

For K=134 choose v134=31/1000. Exact strict inequalities hold:

    v134+1/5 > 2L0(v134),
    H_134 > (24/5+4P0)V+(3/5)L0(V)
            for V=0, Vstar, v134.                  (6)

The first gap increases with V because L0 decreases, so (3) fails for V>=v134. By piecewise convexity, (5) fails for V<=v134. Thus K=134 is impossible.

For K=135 choose v135=37/2500. Exact strict inequalities hold:

    3/10-v135 > 2L0(v135),
    H_135 > (24/5+4P0)V+(3/5)L0(V)
            for V=0, Vstar, v135.                  (7)

Here 3/10-V-2L0(V) is strictly increasing: g'(h)>=4 implies L0'(V)<=-5/6 on both branches, so its derivative is >=2/3. Hence (3) fails for V>=v135 and (5) fails for V<=v135.

The eight strict comparisons (6)-(7) are exact rational/surd comparisons. The smallest positive gap is

    sqrt(3100935)/61000 - 88007/3050000 > 0,

certified by the integer identity

    2500*3100935 - 88007^2 = 7105451 > 0.

Thus both K cases are excluded and **P>1/61**.

## Conditional six-exception raw bridge

**[CONDITIONAL ON RETAINED TYPE-E 16+4 MATCHING AND RAW SAFETY]** Add the unit isolated center z_0 and the twenty projected deep-edge directions z_i, with ||z_i||^2=b_i=1-a_i, a_0=0, A=sum a_i, and A_C the four-core energy. Assume all 210 raw pairings satisfy |z_i dot z_j|<=1/2 except possibly the six pairs among the four core indices. Define

    P_raw=sum_{i<j}[W_ij^2(W_ij^2-1/4)]_+,
    W_ij=z_i dot z_j.

After normalizing u_i=z_i/sqrt(b_i), the exact identity

    s_ij(s_ij-1/4)
      = [W_ij^2(W_ij^2-1/4)+(1-b_i*b_j)*W_ij^2/4]
        /(b_i*b_j)^2

and b_i*b_j>=9/16 give a safe-pair contribution <=(16/81)(a_i+a_j), and an exceptional-pair contribution <=(256/81)[W_ij^2(W_ij^2-1/4)]_++(64/81)(a_i+a_j). There are 20 incidences per a_i among all 210 pairs and 3 per core a_i among the six K4 exceptions. Therefore

    P <= (256/81)P_raw + (320/81)A + (16/9)A_C,

and the strengthened strict bridge is

    **P_raw > 81/15616 - (5/4)A - (9/16)A_C.**       (8)

This does not yield a Type-E contradiction at A<=383/504; the right side can be negative, and the retained stronger conditional A>1/49 remains in force. The quartic defect P_raw is not automatically the same normalization as the older raw/homogeneous defect.

**[PROOF STATUS]** Universal P>1/61 is proved exactly. (8) is conditional on the retained Type-E graph/matching/safety hypotheses. Upstream graph, mass, harmonic, signed-Gram and critical-strip certificates were not independently recertified. Type E, C, D, generic e>=27 and non-isolated branches remain open. Sparse e=23/24 classification assumes delta(G)>=1. Retain star<=70/3, M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504. **Global proved range unchanged: 40<=tau_5<=44.**
