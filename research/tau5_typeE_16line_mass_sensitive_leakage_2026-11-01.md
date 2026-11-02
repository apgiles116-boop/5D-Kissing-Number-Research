> **[AUDIT CORRECTION — 2026-11-01]** The assertion that four two-sided-safe cross-edge endpoint contacts imply |z_i.z_j|<=1/2 is **false** without the extra assumption m_i.m_j>=0. The correct consequence is |z_i.z_j|<=1/2-m_i.m_j<=1/2+sqrt(a_i*a_j). An exact rational counterexample (even with total midpoint mass <11/400) and repaired, unconditional-on-sign spectral bounds are in [the safe-pair audit](tau5_typeE_safe_pair_audit_repaired_leakage_2026-11-01.md). The stronger numerical leakage results below remain standalone lemmas under their extra |z_i.z_j|<=1/2 premise, but **their Type-E applications and downstream two-ray constants are not established from the retained Type-E hypotheses**. Under the retained x<11/400 certificate the corrected Type-E bounds are lambda_4+lambda_5>93/80 and lambda_5>83/200. The global kissing-number range is unchanged.

# Type E: mass-sensitive 16-line leakage (2026-11-01)

**[PROVED EXACTLY — universal geometric lemma with explicit assumptions; Type-E application conditional on retained upstream inputs].** No Type-E exclusion. Global proved range: **40 <= tau_5 <= 44**.

## Theorem

Let z_1,...,z_16 be vectors in R^5 with ||z_i||^2=1-a_i, 0<=a_i<=1/4, x=sum_i a_i<11/400, and |z_i.z_j|<=1/2 for distinct i,j. For every 3-plane W and every 4-plane W respectively,

    L(W)=sum_i ||P_(W^perp)z_i||^2 > 59/50 = 1.18      (T3)
    L(W)>429/1000=0.429                                (T4).

Equivalently, the ordered eigenvalues of S_I=sum_i z_i z_i^T obey lambda_4+lambda_5>59/50 and lambda_5>429/1000.

For Type E, the retained isolated-center harmonic theorem plus M(F3)<=89 gives x<11/400 (see tau5_typeE_small_isolated_mass_harmonic_spectral_gap_2026-11-01.md). The 16 isolated-isolated pairings are two-sided safe and imply |z_i.z_j|<=1/2. Thus the theorem strengthens the previous >531/500 and >73/200 leakage bounds **conditional on those retained upstream certificates**. No D5 labeling, core coplanarity, or rank-13 hypothesis is used in the theorem.

## Harmonic lower bound

For d=3 or 4 fix W and set ell_i=||P_(W^perp)z_i||^2, L=sum ell_i, w_i=P_W z_i, b_i=a_i+ell_i, r_i=||w_i||^2=1-b_i, B=x+L, s_ij=sqrt(ell_i ell_j). We have |w_i.w_j|<=1/2+s_ij.

The polynomial f(t)=t^4-t^2/4 has positive harmonic expansions

    d=3: f=(7/60)P0+(17/42)P2+(8/35)P4,
    d=4: f=(1/16)U0+(1/8)U2+(1/16)U4.

Applying harmonic PSD to normalized w_i with weights r_i^2 (zero r_i harmless), and bounding sum r_i^2>=16-2B+B^2/16 and sum r_i^4<=M(B), yields

    sum_(i<j) F_ij >= H_d(B)
      =alpha_d/2*(16-2B+B^2/16)^2-(3/8)M(B),

where F_ij=(w_i.w_j)^4-(r_i r_j/4)(w_i.w_j)^2, alpha_3=7/60, alpha_4=1/16, and M(B)=15+(1-B)^4 for B<=1 or 14+(2-B)^4 for 1<=B<=2. The fourth-power envelope is capped-simplex concentration of b_i in [0,1].

## New mass-sensitive upper bound

The scalar quadratic v(v-r_i r_j/4), 0<=v<=(1/2+s_ij)^2, has its maximum at the right endpoint, where it is nonnegative. Since r_i r_j>=1-b_i-b_j,

    F_ij <= (b_i+b_j)/16+(b_i+b_j)s_ij/4
       +(b_i+b_j)s_ij^2/4+s_ij/4
       +(5/4)s_ij^2+2s_ij^3+s_ij^4.

The key improvement is retaining total isolated midpoint mass x, not using the loose a_i+a_j<=1/2:

    sum_(i<j)(a_i+a_j)s_ij
      =sum_i a_i sqrt(ell_i)sum_(j!=i)sqrt(ell_j)
      <=sqrt(15)/2*x*L < 2*x*L,
    sum_(i<j)(a_i+a_j)s_ij^2
      =sum_i a_i ell_i(L-ell_i) <=x*L^2/4.

These use Cauchy and ell_i(L-ell_i)<=L^2/4. The remaining universal leakage-moment inequalities, proved in the preceding refined-leakage note, are

    sum s<=15L/2, sum s^2<=15L^2/32,
    sum (ell_i+ell_j)s<=2L^2,
    sum (ell_i+ell_j)s^2<=L^3/4,
    sum s^3<=L^3/8, sum s^4<=L^4/16.

Consequently every feasible realization satisfies the exact polynomial inequality

    H_d(x+L)<=U(x,L),
    U(x,L)=15(x+L)/16+15L/8+xL/2
           +139L^2/128+xL^2/16+5L^3/16+L^4/16.     (1)

## Exact rational contradiction

U is increasing in x and L. For 0<=B<=5/4,

    H_3'(B)<=-(7/60)*(27/2)*(59/32)+3/2<0.

For 0<=B<=1/2,

    H_4'(B)<=-(1/16)*15*(31/16)+3/2=-81/256<0.

If d=3 and L<=59/50, then B<483/400<5/4; monotonicity and (1) would require H_3(483/400)<=U(11/400,59/50). But

    H_3(483/400)-U(11/400,59/50)
      =2132463706807/786432000000000>0.

If d=4 and L<=429/1000, then B<913/2000<1/2; similarly,

    H_4(913/2000)-U(11/400,429/1000)
      =315704614065217/131072000000000000>0.

Both are exact contradictions, proving (T3)-(T4).

## Conditional two-ray tomography

**[PROVED EXACTLY — ADDITIONALLY CONDITIONAL on retained rank-13/two-missing-ray/four-ambiguous-coplanar-core hypotheses].** For orthonormal missing-plane axes p,q put X=p^T S_I p, Y=q^T S_I q. Then X,Y>429/1000, X+Y>59/50, and

    XY>322179/1000000.

Using the retained core-wedge/two-ray factorization for the safe 16x4 squared-correlation matrix D,

    sum_(i<j,c<d)(D_ic D_jd-D_id D_jc)^2
       >=(81/131072)*X^2*Y^2
       >8407743951321/131072000000000000.

If rank(D)=2 and ||D||_F^2<=4, then sigma_2(D)>2899611*sqrt(2)/1024000000, approximately 0.00400456. These are necessary conditions, not a Type-E contradiction.

## Status and audit

**[VERIFIED EXACT ARITHMETIC]** The companion Fraction/SymPy script checks harmonic identities, derivative signs, exact margins and tomography constants. Analytic PSD, convexity and Cauchy arguments are given above.

**[AUDIT CORRECTION]** The repo already contains the stronger universal 21-line quartic bound P>1/58 (2026-10-29); the subsequently reported P>1/64 is weaker and must not be presented as an improvement. The 2026-10-31 superadditive raw-defect note correctly uses P>1/58.

**[RETAINED/OPEN]** Preserve star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504 (and stronger separately conditional harmonic refinements), raw/homogeneous six-core defect bounds and Musin/Boyvalenkov antipodal boundary exclusion. Type E, C, D, generic e>=27 and non-isolated branches remain open; sparse e=23/24 classification requires delta(G)>=1. Global proved range **40<=tau_5<=44**.