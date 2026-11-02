# Type E / F3: exact canonical midpoint floor via radical SOS (2026-11-02)

**[PROVED EXACTLY — standalone eight-unit-vector F3 theorem].** **[OPEN]** Type E; global proved range 40 <= tau_5 <= 44.

For F3 deep edges 02,04,05,14,17,23,27,36,56,57 (strict inner products < -1/2), all remaining pairs safe in [-1/2,1/2], and canonical matching P0=(04),(17),(23),(56), write

    C0 = sum_(ij in P0) ||(u_i+u_j)/2||^2.

Then the **exact strict lower bound** is

    C0 > 2-(sqrt(6)+sqrt(2))/2 = 0.0681483474218634... .       (T)

This is sharp for the **weak-deep convex relaxation**, not asserted sharp for strict five-dimensional Type E.

## Gram symmetrization

Average the eight-point Gram matrix over the Klein-four F3 automorphisms preserving P0:

    identity
    (0 2)(1 6)(3 4)(5 7)
    (0 5)(1 3)(2 7)(4 6)
    (0 7)(1 4)(2 5)(3 6).

The ten pair orbits are

    x0:16,34          x1:06,12,37,45
    x2:13,46          x3:02,57
    x4:05,27          x5:07,25
    x6:04,17,23,56   x7:14,36
    x8:01,26,35,47   x9:03,15,24,67.

The averaging preserves all deep/safe inequalities, PSD and C0. In particular C0=2+2*x6 and x3,x4,x7<-1/2.

Fourier diagonalization gives four PSD 2x2 blocks M_(r,s) with r,s in {+1,-1}:

    M_(r,s) = [[A,R],[R,B]]
    A = 1+r*x3+s*x4+r*s*x5
    B = 1+r*x0+s*x2+r*s*x7
    R = x8+r*x1+s*x9+r*s*x6.

Define the following four **positive-semidefinite exact radical matrices**:

    Z_(++) = [[(2*sqrt(6)-sqrt(2))/8, 1/4],
              [1/4, sqrt(2)/4]]
    Z_(+-) = Z_(-+) =
             [[sqrt(6)/8,-1/4],[-1/4,sqrt(6)/12]]
    Z_(--) = [[sqrt(2)/8,1/4],[1/4,sqrt(2)/4]].

Their determinants are respectively (sqrt(3)-1)/8,0,0,0; diagonal entries are positive. Put

    lambda=(sqrt(6)-sqrt(2))/4 > 0
    mu=(3*sqrt(2)-sqrt(6))/6 > 0.

The **exact SOS identity**, verified by symbolic coefficient comparison, is

    C0 - [2-(sqrt(6)+sqrt(2))/2]
      = sum_(r,s) tr(Z_(r,s) M_(r,s))
        + lambda*(-1/2-x3)
        + lambda*(-1/2-x4)
        + mu*(-1/2-x7).                                  (SOS)

Every trace is nonnegative by PSD; all three deep-contact slacks are strictly positive. This proves (T) without numerical optimization or D5 uniqueness.

**[PROVED EXACTLY — quantitative contact-margin version].** If the six noncanonical deep contacts 02,05,14,27,36,57 all obey inner product <=-1/2-epsilon, then

    C0 >= 2-(sqrt(6)+sqrt(2))/2 + sqrt(6)*epsilon/3,

because 2*lambda+mu=sqrt(6)/3.

## Exact equality witness in the weak-deep relaxation

Set

    x0=x2=-1/4, x1=x9=sqrt(2)/4,
    x3=x4=x7=-1/2, x5=0,
    x6=-(sqrt(6)+sqrt(2))/4,
    x8=(sqrt(6)-sqrt(2))/4.

The four Fourier blocks become

    [[0,0],[0,0]],
    [[1,sqrt(6)/2],[sqrt(6)/2,3/2]],
    [[1,sqrt(6)/2],[sqrt(6)/2,3/2]],
    [[2,-sqrt(2)],[-sqrt(2),1]].

They are PSD with ranks 0,1,1,1; the eight-point Gram has rank 3. All weak deep/safe constraints hold and C0 attains the bound. Strictness is essential for (T).

## Proof-status ledger

**[PROVED EXACTLY]** The standalone canonical F3 lower bound, radical SOS, margin stability and weak-deep sharpness. The verifier independently checks the F3 graph automorphisms, all 28 pair orbits, Fourier congruence, dual PSD, exact SOS identity and rank-three equality witness.

**[CONDITIONAL TYPE-E]** If the retained Type-E mass-selected matching is P0, then 0.0681483474<C0<=A<=383/504. This is compatible with the existing cap and does not eliminate Type E. Do not apply the canonical floor to alternative P1/P2 matching energies.

**[RETAINED]** Star <=70/3; broom M(F3)<=89; M(P)>=S/2-28/3; twenty-edge mass >=2137/6; A<=383/504; Musin/Boyvalenkov zero-midpoint exclusion; previous Q-frame and six-exception bounds. The invalid endpoint-Perron argument remains withdrawn. The independent four-cycle Walsh exclusion is unaffected.

**[OPEN]** Type E (three-defect trees, alternative double-positive cases), Types C and D, generic e>=27, and non-isolated branches. Sparse e=23/24 classification requires delta(G)>=1. Global proved range unchanged 40<=tau_5<=44.

Companion exact checker: research/tau5_typeE_F3_canonical_radical_SOS_2026-11-02_verify.py.
