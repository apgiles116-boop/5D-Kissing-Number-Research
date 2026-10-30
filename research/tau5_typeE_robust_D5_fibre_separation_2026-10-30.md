# Type E: certified robust separation from the D5 support-plane fibre
Date: 2026-10-30

**[PROVED EXACTLY, WITH FINITE INTEGER-ARITHMETIC CENTRE CERTIFICATE; CONDITIONAL ON THE RETAINED TYPE-E REDUCTION]**

Let the 20 selected Type-E deep edges have midpoint energies a_i in [0,1/4], total A <= 383/504, and normalized projected directions u_i=z_i/sqrt(1-a_i). Assume the 184 raw-safe pairings and the isolated centre v, so |v.z_i|<=1/2.

Define F_star to be the geometric *comparison model* of ten orthonormal pairs, each in one of the ten coordinate 2-planes of a common R^5 orthonormal basis, with the four F3 core directions occupying four K5 star supports. For every labeled model f_i in F_star,

    max_i ||u_i u_i^T - f_i f_i^T||_F >= 1/650.

This excludes a **neighbourhood** of the support-plane fibre, not all Type E. It makes no assumption that the actual Type-E vectors are D5-aligned.

**[STRENGTHENED EXACT-FIBRE COROLLARY]** If u_i lie in F_star exactly, then

    A >= 143/175 = 0.817142857... > 383/504,
    exact margin = 103/1800.

This strengthens the earlier exact-fibre energy bound A >= 11/14.

## Proof

Set epsilon=1/650. If all projector Frobenius distances were <epsilon, choose independent line signs so ||u_i-f_i||<epsilon. This is legitimate because for unit vectors with nonnegative dot product c, 2(1-c) <= 2(1-c^2).

The ten support planes are the edges of K5. There are 30 meeting-support pairs; discard six star-star pairs containing the six possibly exceptional core line pairings. The other 24 support pairs are fully safe (safe degrees 3 on four star supports and 6 on six nonstar supports). Let t_e in [0,1] be the squared-coordinate imbalance of the orthonormal model pair on support e. For meeting supports e,f,

    max_{s,t}|f_e^s . f_f^t| = sqrt((1+t_e)(1+t_f))/2.

For the maximizing *safe* line pair, w_i=1-a_i>=3/4 and vector perturbation imply

    sqrt(w_i*w_j*(1+t_e)*(1+t_f)) <= 1+4*epsilon.          (1)

Every support has a safe meeting neighbour. Therefore

    t_e <= (16/9)*(1+4*epsilon)^2-1
        = 84471/105625 < 4/5.                             (2)

For 0<=a<=1/4, -log(1-a)<=7a/6, by the elementary power series. For 0<=t<=4/5, log(1+t)>=11t/15: the ratio log(1+t)/t decreases, and at t=4/5 the lower atanh-series bound is

    log(9/5) > 2*(2/7+(2/7)^3/3) = 604/1029 > 44/75.

Taking logarithms in (1), summing over 24 safe support blocks, and writing T_C and T_N for the sums of t_e on star and nonstar supports, respectively, yields

    T_C+2*T_N <= (35/11)*A+(960/11)*epsilon.              (3)

For the isolated centre write p_k=v_k^2, sorted p_1>=...>=p_5>=0, sum p_k=1. Since |v.u_i|<=1/sqrt(3), each model line satisfies |v.f_i|<=1/sqrt(3)+epsilon. Thus its squared projection is <=1/3+(6/5)*epsilon+epsilon^2, and each orthonormal model pair gives

    p_1+p_2 <= 2/3+3*epsilon.                              (4)

The difference of the two squared model projections on support {i,j}, together with sqrt(1-t^2)>=1-t/2 for t<=4/5, gives

    t_ij >= [ (sqrt(p_i)+sqrt(p_j))^2-2/3-3*epsilon ]_+
             / (p_i-p_j+sqrt(p_i*p_j)).                   (5)

A zero denominator contributes zero. Define F_eta(p) by summing the ten right sides, with eta=3*epsilon.

**[FINITE EXACT CENTRE LEMMA]** For eta=3/650 and p in the sorted simplex satisfying (4),

    F_eta(p) >= 13/5.                                     (6)

The companion verifier proves (6) by exact rational longest-edge simplex bisection. Starting vertices are (1/k,...,1/k,0,...,0), k=1,...,5. If simplex vertex coordinate bounds with common denominator D are l_i,h_i, a lower bound for each summand is

    [3*(l_i+l_j+2*floor(sqrt(l_i*l_j)))-(2+3*eta)*D]_+
    / [3*(h_i-l_j+ceil(sqrt(h_i*h_j)))].

Infeasibility is certified only when 3*(l_1+l_2)>(2+3*eta)*D. The exact certificate terminates after 92,685 bisections, 77,956 lower-bound prunings, and 14,730 domain prunings, with no unresolved simplex.

Equations (5)-(6) give T_C+T_N>=13/5. Since T_N>=0, (3) yields

    A >= 143/175-(192/7)*epsilon.                         (7)

At epsilon=1/650 the right side is 1763/2275, exceeding 383/504 by 2461/163800. Equivalently, (3) is at most 131387/51480 while (6) is 13/5, an exact gap of 2461/51480. Contradiction.

At epsilon=0, (6) remains true by monotonicity of its domain and summands, and (7) gives A>=143/175.

## Proof ledger

- **[PROVED ANALYTICALLY]** 24 safe support incidences, perturbation and log estimates, contradiction from the finite lemma.
- **[PROVED BY EXACT FINITE CERTIFICATE]** F_(3/650)(p)>=13/5, using integer square roots and rational comparisons only.
- **[OPEN]** A Q-kernel inverse stability theorem that places arbitrary Type E inside the forbidden 1/650 neighbourhood. This theorem is a distance lower bound, not a Q-residual lower bound. No six-exception/six-kernel correspondence is assumed.
- **[RETAINED]** 40<=tau_5<=44, M(F3)<=89, 20-edge mass >=2137/6, A<=383/504, Musin/Boyvalenkov zero-midpoint boundary. Type C, Type D, generic e>=27 and non-isolated branches remain open. Sparse e=23,24 classification remains conditional on delta(G)>=1.

Verifier: research/tau5_typeE_robust_D5_fibre_separation_2026-10-30_verify.py.
