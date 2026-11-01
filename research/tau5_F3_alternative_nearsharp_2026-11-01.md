# F3 alternative matchings: near-sharp exact midpoint floor (2026-11-01)

**[PROVED EXACTLY — standalone eight-unit-vector theorem; Type-E use conditional on the retained F3 incidence].** No Type-E exclusion. Global proved range remains **40 <= tau_5 <= 44**.

For eight unit vectors whose ten strict deep contacts (inner product < -1/2) are
02, 04, 05, 14, 17, 23, 27, 36, 56, 57, with all remaining 18 pairs safe, define
C(P)=sum over ij in P of ||(u_i+u_j)/2||^2.
The F3 perfect matchings are P0=04|17|23|56, P1=02|14|36|57, P2=05|14|27|36.

**[PROVED EXACTLY]** Both alternative matchings satisfy

\[
C(P_1),C(P_2)>\frac{2035298537}{219942800000}
=0.009253762964734468\ldots > \frac1{109}.
\]

This is 16.34% stronger than the previous exact alternative bound 505/63488. The earlier sharp canonical bound C(P0)>2-(sqrt(6)+sqrt(2))/2 is stronger still, so **every F3 perfect matching**, including a mass-selected one, satisfies the new lower bound.

## Exact Klein-four Fourier SOS

Average the Gram over the Klein-four F3 automorphisms preserving P1, using the ten pair orbits x0,...,x9 from the previous F3 alternative note and companion verifier. For characters (r,s) in {+1,-1}^2, the PSD 2-by-2 Fourier blocks have

    A_rs=1+r*x3+s*x4+r*s*x5
    B_rs=1+r*x0+s*x2+r*s*x7
    R_rs=x8+r*x1+s*x9+r*s*x6.

For lambda>0 and epsilon=+1 or -1, set
q_rs(lambda,epsilon)=A_rs+lambda^2 B_rs+2 epsilon lambda R_rs >= 0.
As C(P1)=2+x3+x7, the following identity holds **exactly over Q**:

    C(P1)-2035298537/219942800000
      = (475/199948) q_--(74/5,+)
      + (1805/29722) q_-+(11/19,-)
      + (99019/199948) q_+-(7/100,-)
      + (715/99974) q_+-(69/1000,-)
      + (15621/29722) A_++
      + (1334800019/2856400000) B_++
      + (95/2702) q_++(1,+)
      + (357799867/9997400000)(x0+1/2)
      + (95/814)(-1/2-x4)
      + (380/1351)(-1/2-x6).

Every coefficient is positive; Fourier terms are nonnegative by PSD; x0+1/2>=0 is a safe-pair slack; and the last two terms are **strictly positive** because orbits 4 and 6 are deep. This proves the strict lower bound. The F3 automorphism (0,1,2,3,4,5,6,7)->(0,1,5,6,4,2,3,7) exchanges P1 and P2.

## Exact rank-four witness and near-optimality

Define rational numbers

    p=698608951/10000000000
    t=17281125305/10000000000
    q=9999999999999/10000000000000
    eta=1/10000000000000
    eps=(1-q^2)/2
    a=p^2/2, b=(3-t^2)/2.

Choose orbit correlations

    x0=-1/2, x2=1/2-b, x3=-1+a
    x4=-1/2-eps, x5=1/2-a+eps, x7=-1+b

and Fourier cross terms

    R_++=0, R_+-=p, R_-+=q*t
    R_--=-2-4*eta+q*t+p.

Invert the four-character Walsh transform for x1,x6,x8,x9. The Fourier blocks in order (--,-+,+-,++) have ranks (2,1,1,0), so the full Gram is PSD of rank four. Exact checks establish all ten strict deep contacts and eighteen safe pairs. It realizes

\[
C(P_1)=a+b=\frac{57836333103311793}{6250000000000000000}
=0.009253813296529887\ldots.
\]

Therefore the alternative-matching infimum, **even in dimension four**, is bracketed by the exact lower and upper fractions, with gap
5.033179541955486e-8 (< 1e-7). **No sharpness claim is made.** The verifier checks the identity, full Gram, ranks, and every contact.

**[CONDITIONAL TYPE-E APPLICATION]** For the mass-selected F3 matching in Type E, its four midpoint energies satisfy A_C>2035298537/219942800000. This is compatible with A<=383/504 and does not exclude Type E.

**[OPEN]** Type E; Type C C7 global/boundary analysis; Type D; generic e>=27; non-isolated branches. Sparse e=23/24 classification still requires delta(G)>=1. Retain star<=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, midpoint cap A<=383/504, the separately conditional harmonic/Q-frame refinements, and the Musin/Boyvalenkov boundary theorem.