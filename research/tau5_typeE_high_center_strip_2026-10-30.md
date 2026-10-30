# Type E: two high-center branch exclusions (2026-10-30)

**Global proved range unchanged: 40 <= tau_5 <= 44.**

## Proof status

**[PROVED EXACTLY, conditional on retained Type-E resource theorem]** The region x >= 1/250, s >= 6933/1000 is impossible. This exclusion does not use the signed-Gram/D5 atlas.

**[PROVED CONDITIONALLY, using retained resource, rounding, ADE, polar alignment, and complete 16-line D5 extension atlases]** The region x >= x2, s >= 6961/1000 is impossible. Here x2 is the small root of D(x2)=2509/6400.

**[OPEN]** Remaining Type E, Types C,D, generic e>=27, and non-isolated branches remain open. The sparse e=23/24 classification still requires delta(G)>=1.

## Resource and scalar exclusion

Let x be the midpoint energy on the 16 isolated deep edges, s the sum of squared contacts with the isolated center, N0 the center nondeep degree-four mass, and R the mass of 754 other safe contacts. The retained Type-E theorem states

D(x)+E(s)+N0+R <= 15, with N0,R >= 0,

D(x)=196x-644x^2+896x^3-448x^4=28y(7-16y), y=x(1-x),

E(s)=10+(35/64)(5s-32)^2, and x<=A<=383/504.

For 27/4 <= s <= 7, capped-simplex concavity gives

N0 >= n(s):=7(7-s)(1-4(7-s)).

The derivative of E+n is (175/32)(5s-32)-7+56(7-s), decreasing with s but positive at s=7 (301/32). Hence E+n increases on [6933/1000,7]. For s>=7, E(s) is increasing and D(x2)+E(7)>15, so s>=7 is impossible whenever x>=x2.

For a in {x2,1/400,1/250}, D(x)>=D(a) on [a,383/504]. Indeed y=x(1-x) is concave and 28y(7-16y) is concave on [0,1/4]; checking the interval endpoints yields the lower bound (the upper endpoint 383/504 gives larger D than each chosen a, and D(1/2)=21). The exact enclosure x2<2094/1000000<1/400 is retained.

If x>=1/250 and s>=6933/1000, the resource left side is at least

D(1/250)+E(6933/1000)+n(6933/1000)
=15+1090526187/1000000000000>15.

This is the first, atlas-free exclusion.

## High-center strip x>=x2, s>=6961/1000

Set sd=6961/1000. From the resource theorem, s<7 and the monotonicity above,

R <= 15-D(x2)-E(sd)-n(sd)
  = 4782757/64000000 < 7/90 < 5/64,

N0 <= 15-D(x2)-E(sd)
   = 156233/512000 < 21/64,

D(x) <= 15-E(sd)-n(sd)
     = 29872757/64000000 < D(1/400).

The D monotonic-endpoint argument forces x<1/400. Thus all prior 16-line rounding tests hold: x/2+sqrt(2x)<1/8, 2sqrt(x)<1/8, and

||G16-Ghat16||_F^2 <= (81/1078)R+x^2
<55404931/9856000000
<158207437/26950000000<1/169.

For each F3 endpoint, the squared rounded-correlation error is less than

(81/1078)R <=55343331/9856000000<1/64.

The retained exact signed-Gram/ADE atlas therefore reconstructs sixteen D5 projective root lines, with polar alignment error <1/10.

For center contacts put r_t=min(t^2,1/4-t^2) and J=sum r_t. N0<21/64 implies every r_t<1/16 and

J <= (4/21)N0 <=22319/384000.

If k contacts are high, |4s-k|<=4J, forcing k=28 on sd<=s<7. Let H=sum(1/4-t^2) over high contacts and L=sum t^2 over low contacts. Then H+L=J, H-L=d=7-s, 0<d<=39/1000. Each isolated endpoint pair has a consistent high/low category (and opposite signs when high) because 2sqrt(x)<1/8. The retained center Walsh rounding lemma gives

center_error^2 <= (L+(4/3)H^2)/2
=(J-d)/4+(J+d)^2/6.

This is increasing in J and decreasing in d on the indicated box, since J+d<3/4. Hence

center_error^2 <=Jmax/4+Jmax^2/6
=13353881761/884736000000<1/64.

The previous complete 16-line D5 extension atlas now applies: the isolated center and eight F3 endpoints must occupy eight signed omitted-root neighborhoods, with no two kissing-code points allowed in the same neighborhood. Nine points cannot occupy eight neighborhoods. This excludes the entire high-center strip.

**Dependency caution:** The new rational resource/rounding inequalities are checked by the companion Fraction script. Completeness of the upstream signed-Gram/ADE/D5 extension atlas and the retained rounding lemmas is assumed, not independently rerun.

## Consequence

Within the previous critical rectangle x2<=x<=1/250 and 69/10<=s<209/30, the substrip s>=6961/1000 is now impossible. The earlier conditional Q>F_*+1/1440 gap is needed only when 69/10<=s<6961/1000. Independently, the scalar exclusion removes x>=1/250, s>=6933/1000.

Retain M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, and the source-audited Musin/Boyvalenkov zero-midpoint boundary theorem. No identification of six exceptional pairings with six Q-kernel modes is assumed.