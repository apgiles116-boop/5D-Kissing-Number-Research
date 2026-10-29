# Type E: three-zone center-contact coercivity (2026-10-29)

**[PROVED EXACTLY — standalone paired-contact lemma]; [CONDITIONAL TYPE-E COROLLARY].** No Type-E exclusion; global proved range remains **40 <= tau_5 <= 44**.

## Standalone lemma

For twenty selected deep-edge pairs and isolated-center unit vector v, write p_i=v.m_i, q_i=v.z_i and y_i=2(p_i²+q_i²), sorted decreasing. All forty center endpoint contacts are nondeep, so |p_i+q_i|,|p_i-q_i|<=1/2, hence 0<=y_i<=1/2. Suppose 69/10<=s=sum y_i<=209/30, rho=s-13/2 in [2/5,7/15]. Define delta as the L1 distance of sorted y to (1/2 repeated 13 times, rho, 0 repeated 6 times), B=sum p_i², B_H=sum_{i<=13}p_i², B_R=p_14², B_T=sum_{i>=15}p_i², c=15/172 and h=1/2-rho-delta/2.

If delta<=1/30 and B<=1/16, the earlier exact endpoint-cap estimate gives B_H<=c delta². **New exact three-zone inequality:**

    mix := sum_i (1/2-y_i)p_i²
         >= h B_R + (1/2-delta/2) B_T
         >= h (B-c delta²)_+ + rho B_T.             (1)

**Proof.** Let D=sum_{i<=13}(1/2-y_i), E=sum_{i>=15}y_i. Then y_14=rho+D-E and delta=2 max(D,E). Hence y_14<=rho+delta/2 and every tail y_i<=E<=delta/2. Their mixing weights are at least h and h+rho respectively, while the high-zone weights are nonnegative. The previous exact cap argument gives B_H<=c delta², and B-B_H>=max(0,B-c delta²). QED.

The paired-center harmonic identity (proved in the earlier note) is

    R_N/112 = gap/16 + mix + 2(sum_i p_i^4-B²/20),
    gap = sum_i y_i(1-2y_i)-rho(1-2rho)
        >= (1-2rho)delta-delta².

Consequently **[PROVED EXACTLY — under the standalone hypotheses]**

    R_N/112 >= ((1-2rho)delta-delta²)/16
               + h(B-c delta²)_+ + rho B_T.         (2)

## Conditional Type-E application

Retain the mass, harmonic, conditional signed-Gram, and derivative certificates from tau5_typeE_tensor_contact_stability_2026-10-29.md. These upstream inputs are **not independently recertified**. On x_2<=x<=1/250 and 69/10<=s<=209/30, put F_*=F(x_2,209/30), Q=sum_{i<j}(z_i.z_j)² and epsilon=Q-F_*>=0. The tensor/frame identity and (2) give

    epsilon >= B/160 + h(B-c delta²)_+ + rho B_T
               + ((1-2rho)delta-delta²)/16,         (3)

in addition to the separately retained nonnegative x,s, B², and frame-anisotropy penalties.

If 0<=epsilon<=1/57600, the earlier tensor estimate first yields delta<=480epsilon<=1/120<1/30 and B<=160epsilon<=1/360<1/16, so the sharp quantization theorem applies:

    delta <= (2-sqrt(3))/60 < 1/220.

Using epsilon>=delta/240-delta²/16 and delta<1/220 gives

    delta <= (10560/41)epsilon < 260epsilon.

Thus h>=1/30-delta/2>41/1320>31/1000 and
delta²<=67600epsilon²<=(169/144)epsilon.

If B>=c delta², (3) implies

    epsilon >= (149/4000)B-(465/172000)delta²,

hence

    B <= (8282195/307536)epsilon < 27epsilon.      (4)

If B<c delta², B<=(845/8256)epsilon, so (4) still holds.

Furthermore, the high-zone and direct tail-weight bounds yield

    B_H <= (253500/43)epsilon²,                     (5)
    B_T < 2epsilon for epsilon>0; B_T=0 if epsilon=0. (6)

As epsilon->0+, delta=O(epsilon), B_H=O(epsilon²), and h>=1/30-O(epsilon), so

    limsup B/epsilon <= 480/19 = 25.2631578947... . (7)

The new finite-range coefficient 27 improves the preceding 45 on the narrower range epsilon<=1/57600. The asymptotic coefficient improves from 480/11 to 480/19. Near-maximal B/epsilon requires concentration in the single residual center-contact pair: the six tail pairs contribute <2epsilon.

**[PROVED EXACTLY]** (1)-(2), the algebra and rational constants. **[CONDITIONAL]** (3)-(7), dependent on the retained upstream certificates. **[OPEN]** No positive epsilon gap, no Type-E exclusion; still need an incidence-sensitive contradiction with the 184 safe pairings. Types C, D, generic e>=27, and non-isolated branches remain open. Never regress to M(F3)<=94 or M(P)>=S/2-343/32.

Verifier: research/tau5_typeE_three_zone_center_coercivity_2026-10-29_verify.py.
