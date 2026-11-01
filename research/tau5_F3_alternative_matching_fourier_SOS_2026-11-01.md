# Type E / F3: exact positive midpoint floor for both alternative perfect matchings

Date: 2026-11-01. **[PROVED EXACTLY — standalone eight-unit-vector theorem]**. Type-E application is conditional on the retained F3 deep/safe incidence. **Not a Type-E exclusion.** The established global range remains **40 <= tau_5 <= 44**.

## Theorem

Let eight unit vectors `u_0,...,u_7` have deep contacts `u_i.u_j < -1/2` precisely on the ten F3 edges

    02, 04, 05, 14, 17, 23, 27, 36, 56, 57,

and let every other pairing of these eight vectors be safe, i.e. have scalar product in `[-1/2,1/2]`. For a perfect matching `P` of F3, define

    C(P) = sum_{ij in P} ||(u_i+u_j)/2||^2.

The three perfect matchings are

    P0 = 04|17|23|56 (canonical all-singleton),
    P1 = 02|14|36|57 (alternative),
    P2 = 05|14|27|36 (alternative).

Then **C(P1) >505/63488>1/128 and C(P2) >505/63488>1/128**. Together with the previously proved canonical bound `C(P0)>2-(sqrt(6)+sqrt(2))/2 >505/63488>1/128`, this yields the first uniform exact statement in this proof ledger:

    EVERY perfect matching P of F3 satisfies C(P) >505/63488>1/128.

In particular this applies to the F3 matching *selected by the retained mass theorem*, without assuming which of the three it selects. This is a positive-energy transfer, **not** a new contradiction or a strengthening of the retained total Type-E midpoint cap by itself.

## Proof for P1: symmetrize and Fourier-diagonalize

Average the eight-endpoint Gram matrix over the Klein-four group of F3 automorphisms preserving P1. This preserves PSD, unit diagonals, all deep/safe inequalities, and the objective C(P1). The group has two four-vertex regular orbits, with ordered labels

    A=(0,2,5,7), B=(1,6,3,4),

corresponding to group elements `(e,a,b,ab)`. The ten off-diagonal pair orbits are represented by `x0,...,x9`, with their precise vertex lists in the verifier. The essential ones are:

    x0: 16,34          (safe, so x0>=-1/2)
    x3: 02,57          (matching deep, so x3>=-1)
    x4: 05,27          (deep, so x4<-1/2)
    x6: 04,17,23,56    (deep, so x6<-1/2)
    x7: 14,36          (matching deep, so x7>=-1)

The matching energy is exactly

    C(P1)=2+x3+x7.

For characters `(r,s)` in `{+1,-1}^2`, the averaged Gram matrix splits into four `2 x 2` PSD blocks

    [[A_rs,R_rs],[R_rs,B_rs]],

where

    A_rs=1+r*x3+s*x4+r*s*x5,
    B_rs=1+r*x0+s*x2+r*s*x7,
    R_rs=x8+r*x1+s*x9+r*s*x6.

Consequently `A_rs>=0`, `B_rs>=0` and, for every rational `lambda` and sign `epsilon`,

    q_rs(lambda,epsilon)
       = A_rs+lambda^2 B_rs+2 epsilon lambda R_rs >= 0.

## Exact rational sum-of-squares certificate

A direct expansion gives the following identity, with no numerical optimization:

    C(P1)-505/63488
      = (1/496) q_--(16,+)
      + (2/31) q_-+(1/2,-)
      + (121/248) q_+-(1/16,-)
      + (7/496) q_+-(1/8,-)
      + (1/31) q_++(1,+)
      + (33/62) A_++
      + (29831/63488) B_++
      + (889/31744)(x0+1/2)
      + (1/8)(-1/2-x4)
      + (8/31)(-1/2-x6).

The exact rational floor satisfies `505/63488 - 1/128 = 9/63488 > 0`.

Every coefficient is positive. Every right-hand summand is nonnegative by Fourier-block PSD or by the indicated endpoint inequalities. The last two are **strictly positive** because their corresponding pairs are deep. Thus `C(P1) >505/63488>1/128`.

An explicit F3 graph automorphism

    (0,1,2,3,4,5,6,7) -> (0,1,5,6,4,2,3,7)

maps P1 to P2, proving `C(P2) >505/63488>1/128` without a separate certificate.

The exact verifier checks all three matchings, every Klein-four automorphism and pair orbit, the matching-exchange automorphism, and the full rational polynomial identity. It checks the arithmetic of the certificate; the analytic proof of nonnegativity is the PSD argument above.

## Proof ledger and limitations

**[PROVED EXACTLY]** The two alternative F3 perfect matchings each have midpoint energy>505/63488>1/128. Together with the earlier sharp canonical theorem, **every** F3 perfect matching has midpoint energy>505/63488>1/128. No ambient dimension, D5 labeling, core coplanarity, or rank-13 hypothesis is needed.

**[CONDITIONAL TYPE-E APPLICATION]** Under the retained Type-E F3 graph and mass-selected perfect matching theorem, its four core midpoints satisfy `A_C >505/63488>1/128`. This is weaker numerically than some separately conditional core estimates but closes the previously missing *all-matchings* transfer for an elementary unconditional F3 bound.

**[NOT CLAIMED]** The constant 505/63488 is not asserted sharp. Numerical PSD reconnaissance suggests the alternative optimum may be larger; no exact optimality or rank-five realization is claimed. This does not force `A>383/504`, eliminate Type E, or change the global proved range.

**[OPEN]** Type E, Type C C7 global/boundary proof, Type D, generic e>=27, and non-isolated branches. Sparse e=23/e=24 classification remains conditional on delta(G)>=1. Retain star<=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, the stronger conditional harmonic/Q-frame refinements, and the Musin/Boyvalenkov zero-midpoint boundary theorem. Do not revert to superseded F3<=94 or matching S/2-343/32.
