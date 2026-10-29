# Type E: shifted fourth-moment D5 angular-exclusion theorem (2026-10-29)

**[PROVED EXACTLY — standalone geometric theorem; conditional Type-E application].** This strengthens the earlier D5 max-angle exclusion from 2/25 to **16/125 radians** (~7.334 degrees) under the retained isolated-center and midpoint-cap hypotheses. It does not eliminate Type E.

## Theorem

Let the twenty projective D5 roots be r_ij^±=(e_i±e_j)/sqrt(2) in R^5. Suppose unit vectors u_1,...,u_20 have weights 0<=a_i<=1/4, sum A<=383/504, z_i=sqrt(1-a_i)u_i, and there is a unit v satisfying |v·z_i|<=1/2 for all i. For every rotation, bijection and projective sign matching between u_i and the twenty D5 lines, **some matched projective angle exceeds 16/125 radians**.

## Exact proof

For a putative D5 matching with maximum angle theta, put s_i=(v·r_i)^2. The exact D5 moment identities give

    sum_i s_i=4,
    sum_i s_i^2=3/2+(1/2)sum_{k=1}^5 v_k^4 >=8/5.

Consequently, for every t0,

    sum_i s_i(s_i-t0)>=8/5-4t0.                         (1)

The center inequality gives |v·u_i|<=b(a_i), b(a)=1/(2sqrt(1-a)). Define h(a)=sqrt(1-b(a)^2) and q(a)=b(a)cos(theta)+h(a)sin(theta). Since b(a)<=1/sqrt(3)<cos(theta), the spherical triangle inequality yields s_i<=q(a_i)^2.

For 0<=a<=1/4 the rational derivative bounds are

    1/2<=b<=3/5; 1/4<=b'<=2/5; 3/8<=b''<=4/5;
    h>=4/5; -3/10<=h'<=0; -73/80<=h''<=0.

The last line follows from h'=-bb'/h and h''=-(b'^2+bb'')/h-b^2*b'^2/h^3. At theta=16/125,

    q'>=(1/4)(1-theta^2/2)-(3/10)theta>0,
    q''>=(3/8)(1-theta^2/2)-(73/80)theta>0.

Thus q^2 is increasing and convex. Write q0=q(0), q1=q(1/4), t0=q0^2. The convex secant inequality gives

    0<=q(a_i)^2-q0^2<=4a_i(q1^2-q0^2).

Since 0<=s_i<=q1^2, we obtain the shifted pointwise estimate

    s_i(s_i-q0^2)<=4a_i q1^2(q1^2-q0^2).

Summing and using A<=B=383/504 in (1) yields the necessary inequality

    8/5-4q0^2 <=4B q1^2(q1^2-q0^2).                  (2)

For T=16/125, set C+=1-T^2/2+T^4/24, C-=1-T^2/2, S-=T-T^3/6 and the rational enclosures

    q0+ = C+/2+(866026/1000000)T,
    q0- = C-/2+(866025/1000000)S-,
    q1+ = (577351/1000000)C++(816497/1000000)T.

These use the rational square-root bounds
866025/1000000<sqrt(3)/2<866026/1000000,
577350/1000000<1/sqrt(3)<577351/1000000, and
816496/1000000<sqrt(2/3)<816497/1000000,
together with alternating Taylor bounds for sine and cosine.

Exact rational arithmetic proves

    8/5-4(q0+)^2 >1273/10000,
    4B(q1+)^2*((q1+)^2-(q0-)^2) <1265/10000.

This contradicts (2), proving the theorem. The attached verifier checks the D5 polynomial identity, radical intervals, convexity and rational inequalities without floating-point tests.

## Q-template orbit-distance corollary

For Q(u)=uu^T-I/5, ||Q(u)-Q(r)||_F^2=2sin^2(projective angle). Therefore, for every rotation R and line bijection pi,

    sum_i ||Q(u_i)-R Q(r_pi(i)) R^T||_F^2 >1/32,

since 2(T-T^3/6)^2>1/32. This is a lower bound on distance to the D5 orbit, **not** on unaligned frame variance.

## Optional stronger-cap corollary

**[CONDITIONAL ON A SEPARATE, NOT REPROVED CENTER-HARMONIC CERTIFICATE]** The repository also retains A<=0.5669250570031576. If accepted, this implies A<=567/1000. The same rational argument with theta=27/200 yields

    8/5-4(q0+)^2 >1/10
      >4(567/1000)(q1+)^2*((q1+)^2-(q0-)^2),

so the max angle exceeds **27/200 radians** (~7.735 degrees) and the Q-template squared distance exceeds **9/250**. The baseline 16/125 theorem does not depend on this stronger harmonic input.

## Proof ledger

- **[PROVED EXACTLY — standalone]** Shifted D5 fourth-moment/energy bridge and angular exclusion under explicit hypotheses.
- **[RETAINED, NOT REPROVED]** Type-E matching reduction, isolated-center safety, midpoint cap A<=383/504, stronger conditional center-harmonic cap, and other upstream mass/graph certificates.
- **[OPEN]** No Type-E contradiction or D5 alignment upper bound. Types C,D, generic e>=27 and non-isolated branches remain open; sparse e=23,24 graph classification assumes delta(G)>=1.
- **[GLOBAL PROVED RANGE — UNCHANGED]** 40<=tau_5<=44.
