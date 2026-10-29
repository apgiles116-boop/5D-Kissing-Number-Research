# F3 double-matching leaf-concentration obstruction (2026-10-29)

**[PROVED EXACTLY — standalone eight-vector theorem]** The argument assumes only unit endpoints and the canonical F3 deep/safe contact inequalities. **[CONDITIONAL TYPE-E APPLICATION]** uses the retained Type-E graph and matching classification. **[OPEN]** No Type-E exclusion; global range remains 40 <= tau_5 <= 44.

Let F3 have edges 02,04,05,14,17,23,27,36,56,57 and take matching P1=02|14|36|57. Denote its pairs A=02, B=14, C=36, D=57. Write endpoints u0=mA+zA, u2=mA-zA; u1=mB+zB, u4=mB-zB; u3=mC+zC, u6=mC-zC; u5=mD+zD, u7=mD-zD. Put a_i=||m_i||², R=sqrt(a_A+a_C+a_D), E=z_C-z_A-z_D. All deep edges have dot <= -1/2; safe nonedges have dot <= 1/2.

## Exact three-pair frustration identity

For edges 05,27,23,56 put eta_ij=-1/2-u_i·u_j >=0 and eta=(eta05+eta27)/2+eta23+eta56. Expanding the four edge products gives

\[
\boxed{\|E\|^2+\|m_A+m_C+m_D\|^2+2\eta
=2(m_D-m_A)\cdot z_C+2(z_A-z_D)\cdot m_C.}\tag{1}
\]

Cauchy-Schwarz implies ||E||² <= (4+2sqrt(2))R < 7R. In particular, if mA=mC=mD=0, then E=0 and eta=0. Therefore these three pairs cannot all be antipodal in a *strict* F3 deep-edge configuration: the four indicated contacts would all have to be at the boundary -1/2.

## Robust leaf concentration

The deep edges 04 and 17, together with the two safe pairs 13 and 46, give the exact linear slack inequality

\[
\boxed{\tfrac12\le (z_A+z_D-z_C+m_A-m_D)\cdot z_B
+(z_D-z_A-m_A-m_C-m_D)\cdot m_B.}\tag{2}
\]

Using (1), ||z_i||<=1, ||m_D-m_A||<=sqrt(2)R, ||m_A+m_C+m_D||<=sqrt(3)R, and ||z_D-z_A||<=2 yields

\[
\boxed{(2+2R)\sqrt{a_B}+\sqrt{7R}+\tfrac32 R\ge\tfrac12.}\tag{3}
\]

**[PROVED EXACTLY]** If a_B <= 1/100 then a_A+a_C+a_D > 1/8100. Otherwise R<=1/90 would make the left side of (3) at most
91/450+sqrt(7/90)+1/60 < 91/450+7/25+1/60 = 449/900 < 1/2.
The same conclusion holds with B and C exchanged by an F3 automorphism preserving P1, and for the equivalent double-pattern matching P3.

## Sharp one-active weak-boundary theorem

If mA=mC=mD=0, (1) gives z_C=z_A+z_D, while the deep contacts give z_A·z_D=-1/2. Thus ||z_D-z_A||=sqrt(3). From (2),

\[
\tfrac12\le(z_D-z_A)\cdot m_B\le\sqrt3\,\|m_B\|,
\qquad\boxed{a_B\ge1/12.}
\]

This is sharp **for the weak-contact boundary system**, not a claim of strict feasibility with the other three midpoints zero. An exact three-dimensional equality witness is: a=(1,0,0), d=(-1/2,sqrt(3)/2,0), c=a+d, e=(0,0,1); zA=a, zC=c, zD=d, mA=mC=mD=0, mB=(d-a)/6, zB=c/2+sqrt(2/3)e. The eight endpoints are unit; all ten F3 edges have dot <= -1/2 and all other pairs <=1/2. The companion SymPy checker tests all 28 pairings exactly.

## Scope

The pointwise deep-edge cap a_i<1/4 and retained A<=383/504 have a convex fourth-moment envelope whose boundary has three a_i=1/4, one residual 5/504, and the rest zero. The new theorem **rules out the incidence subcase** in which that residual is the B or C *leaf* midpoint and the other three F3 core midpoints vanish. It does not rule out a capped *hub* midpoint or other cap-envelope incidence patterns, and therefore **does not improve the unconditional Q floor** or settle Type E.

**[RETAINED, NOT REPROVED]** M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, the zero-midpoint exclusion, and conditional center/harmonic/atlas estimates. **[OPEN]** Extend the incidence obstruction to hub-cap patterns and obtain a positive safe-pair/Q-frame gap. Types C, D, generic e>=27, and non-isolated branches remain open. **40<=tau_5<=44 unchanged.**
