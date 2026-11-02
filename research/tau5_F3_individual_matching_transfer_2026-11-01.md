# F3: exact individual alternative-matching transfer (2026-11-01)

**[PROVED EXACTLY — standalone eight-unit-vector theorem].** Type-E applications are **conditional on retained graph/mass/harmonic certificates**. No Type-E exclusion. Global proved range **40 <= tau_5 <= 44**.

## Statement

Let eight unit vectors have the ten strict deep contacts (dot product < -1/2)

    02,04,05,14,17,23,27,36,56,57

and all other eighteen contacts two-sided safe in [-1/2,1/2]. The three perfect matchings are

    P0=04|17|23|56; P1=02|14|36|57; P2=05|14|27|36.

Set Ck=sum_(ij in Pk) ||(u_i+u_j)/2||^2. Then

    C1 > (1291-1585*C0)/2000,
    C2 > (1291-1585*C0)/2000.                           (T)

These are *individual* lower bounds, not just a bound on C1+C2. They are positive for C0<1291/1585.

## Exact rational SOS proof

Average the endpoint Gram over the Klein-four graph automorphisms preserving P0 and P1:

    identity, (0 2)(1 6)(3 4)(5 7),
    (0 5)(1 3)(2 7)(4 6), (0 7)(1 4)(2 5)(3 6).

The ten pair orbits, with averaged correlation xj, are

    x0:16,34;       x1:06,12,37,45;  x2:13,46;
    x3:02,57;       x4:05,27;        x5:07,25;
    x6:04,17,23,56; x7:14,36;        x8:01,26,35,47;
    x9:03,15,24,67.

Averaging preserves PSD, all contact inequalities, and matching energies. Thus x4<-1/2, x9<=1/2, C0=2+2*x6, C1=2+x3+x7. Fourier diagonalization gives four PSD 2-by-2 blocks M_rs, r,s=+/-1:

    M_rs=[[A_rs,R_rs],[R_rs,B_rs]],
    A_rs=1+r*x3+s*x4+r*s*x5,
    B_rs=1+r*x0+s*x2+r*s*x7,
    R_rs=x8+r*x1+s*x9+r*s*x6.

Choose rational positive-definite matrices, in order (++),(+-),(-+),(--):

    Z++=[[309/400, 1857/8000],[1857/8000,599/1000]]
    Z+-=[[109/200,-1857/8000],[-1857/8000,99/1000]]
    Z-+=[[109/400,-1313/8000],[-1313/8000,99/1000]]
    Z--=[[9/200,1313/8000],[1313/8000,599/1000]].

Their determinants are respectively 26166111/64000000, 4671/64000000, 2591/64000000, 1151/64000000, all positive, as are their diagonals.

**[EXACT POLYNOMIAL IDENTITY]**

    C1-(1291-1585*C0)/2000
      = sum_(r,s) tr(Z_rs*M_rs)
        +(91/200)*(-1/2-x4)+(34/125)*(1/2-x9).          (SOS)

All terms on the right are nonnegative, and the x4 term is strictly positive since both 05 and 27 are strict deep contacts. This proves the first strict inequality. The F3 automorphism (2 5)(3 6) preserves P0 and exchanges P1/P2, proving the second. No numerical SDP or D5 labeling is involved.

## Conditional Type-E consequences

**[CONDITIONAL — baseline retained Type-E energy cap]** If the mass-selected F3 matching is P0, then C0<=A<=383/504, hence

    C1,C2 > 43609/1008000 = 0.043262896825... .         (B)

**[CONDITIONAL — additionally retained stronger isolated-center harmonic cap]** With A<=Astar=0.566925057...<567/1000,

    C1,C2 > 78461/400000 = 0.1961525 > 49/250.        (H)

This improves the previously sharp standalone all-F3 alternative-matching floor 0.009253813... *only in the canonical mass-selected branch*. The retained aggregate tradeoff C1+C2>=g(C0) is complementary: (T) prevents either alternative from carrying arbitrarily little energy. Neither bound is a contradiction for the full 41-code.

**[VERIFIED EXACT ARITHMETIC]** Companion SymPy/Fraction checker verifies all 28 pair orbits, graph automorphisms, PSD determinants, polynomial identity and rational corollaries.

**[OPEN]** Type E, C, D, generic e>=27 and non-isolated branches. The e=23/e=24 sparse classification remains conditional on delta(G)>=1. Preserve star<=70/3, M(F3)<=89, M(P)>=S/2-28/3, selected-edge mass>=2137/6, raw/homogeneous defect caps, and the Musin/Boyvalenkov zero-midpoint exclusion. **40<=tau_5<=44**.
