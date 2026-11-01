# Exact sharp F3 alternative-matching midpoint infimum; correction of October 28 sharpness claim

2026-11-01. **[PROVED EXACTLY — standalone F3 eight-vector theorem]**. Type-E application conditional on the retained graph/mass reduction. Global proved range **40 <= tau_5 <= 44**.

## Theorem

Let the ten strict deep pairs (inner product < -1/2) be 02,04,05,14,17,23,27,36,56,57, with **all eighteen other pairs safe on both sides**, i.e. inner products in [-1/2,1/2]. For P1=02|14|36|57 or P2=05|14|27|36, let C(P)=sum over ij in P of ||(u_i+u_j)/2||^2.

Let s be the unique root in (1797973425701/10^12,1797973425702/10^12) of

    P(s)=s^6-s^5-23s^4+48s^3-25s^2+4s+20,

and define

    h=(9s^2-10s-10)/(s^2+6),
    p=(s-sqrt(s^2-4h))/2,
    t=(s+sqrt(s^2-4h))/2,
    Cstar=(p^2+3-t^2)/2=(3-s sqrt(s^2-4h))/2.

**[PROVED EXACTLY]** Both alternative-matching strict infima in R5 equal Cstar, with

    0.009253813 < Cstar < 0.009253814
    Cstar = 0.0092538130462245022... .

Every strictly feasible configuration has C(P)>Cstar. The boundary optimum has rank-three Gram; strict rank-four configurations approach it. Together with the previously established canonical-matching sharp floor 2-(sqrt(6)+sqrt(2))/2, this is the sharp **all-matchings** F3 energy infimum.

## Essential October 28 audit correction

The older note tau5_typeE_F3_double_matching_exact_sharp_2026-10-28.md claimed the smaller value 1-sqrt(sqrt(3)-3/4)=0.009015233432... was sharp for the full graph. Its alleged rank-three witness has

    G_16 = G_34 = -1/2 - 2v < -1/2,  v>0.

But 16 and 34 are F3 **nonedges**, which must satisfy G_ij>=-1/2. The old witness has two additional deep edges and is **not** a realization of the specified F3 graph. Its PSD stress still establishes the weaker lower bound, but the old **sharpness and strict-feasibility claims are withdrawn**. The November 1 rational near-sharp certificate was correct; this note closes its ~5e-8 gap.

## Exact Fourier primal-dual proof

Average any feasible eight-vector Gram over the Klein-four automorphisms preserving P1. The ten orbit correlations x0,...,x9 are enumerated in the previous near-sharp verifier. The four Fourier PSD blocks, indexed by r,s in {+1,-1}, are

    M_rs=[[A_rs,R_rs],[R_rs,B_rs]],
    A_rs=1+r*x3+s*x4+r*s*x5,
    B_rs=1+r*x0+s*x2+r*s*x7,
    R_rs=x8+r*x1+s*x9+r*s*x6.

They obey sum A_rs=sum B_rs=4 and C=2+x3+x7. We use only PSD and three contact inequalities x0+1/2>=0, -1/2-x4>=0, -1/2-x6>=0.

Put d=2-p-t, A=3-p^2, B=3-t^2. Exact elimination from P(s)=0 yields

    A*B=d^2,
    (p+t)*d=p*t*(6-p^2-t^2).

Rational interval arithmetic gives 0.069<p<0.071, 1.728<t<1.729, 0.202<d<0.203. Define

    gamma=4/(1/p-B/d),
    beta=gamma*(t-B/d)/4,
    alpha=gamma*(1/t-p)/4,
    lambdaA=gamma*t/8+(1-beta)/4,
    lambdaB=gamma/(8*t)+(1-alpha)/4.

The stationary identity implies 1/p-B/d=A/d-1/t. The rational brackets imply 0<gamma<2/7, 0<alpha<1/20, beta>0. Define four PSD dual blocks

    Z_--=gamma/(8d)*[[B,d],[d,A]],
    Z_-+=gamma/(8t)*[[t^2,-t],[-t,1]],
    Z_+-=gamma/(8p)*[[1,-p],[-p,p^2]],
    Z_++=[[1/2+gamma*t/8,gamma/8],
           [gamma/8,gamma/(8t)+(1-alpha)/2]].

The first three are rank-one PSD. Z_++ is positive definite: its diagonals exceed 1/2 and 19/40, and its off-diagonal entry is <1/28. Exact coefficient comparison gives the global SOS identity

    C-L=sum_rs tr(Z_rs M_rs)
        +alpha*(x0+1/2)
        +beta*(-1/2-x4)
        +gamma*(-1/2-x6),

where L=2-4lambdaA-4lambdaB-alpha/2+beta/2+gamma/2. Hence C>=L for every feasible Gram, with strict inequality when x4,x6 are strictly deep.

The boundary Fourier blocks

    M_++=0,
    M_+-=[[p^2,p],[p,1]],
    M_-+=[[1,t],[t,t^2]],
    M_--=[[A,-d],[-d,B]]

are PSD of ranks 0,1,1,1. Their inverse Fourier orbit correlations are

    x0=-1/2, x1=(1-t)/2, x2=(t^2-2)/2,
    x3=-1+p^2/2, x4=-1/2, x5=(1-p^2)/2,
    x6=-1/2, x7=(1-t^2)/2,
    x8=(p+t-1)/2, x9=(1-p)/2.

All six safe orbits lie in [-1/2,1/2]; all four deep orbits are <=-1/2. The three slacks and all four dual trace terms vanish. Therefore L=Cstar exactly.

## Strict rank-five approach

For sufficiently small delta>0, replace t by t_delta=t-delta, set q=1-delta^2, eta=delta^2, eps=(1-q^2)/2, retain p and x0=-1/2, and choose

    x2=(t_delta^2-2)/2, x7=(1-t_delta^2)/2,
    x3=-1+p^2/2, x4=-1/2-eps, x5=(1-p^2)/2+eps,
    R_++=0, R_+-=p, R_-+=q*t_delta,
    R_--=p+q*t_delta-2-4eta.

Inverse Walsh gives x6=-1/2-eta, so every prescribed deep orbit is now strictly deep; safe orbits remain safe by continuity. Fourier ++ stays zero, +- stays rank-one PSD, -+ stays rank-one PSD with block [[q^2,q*t_delta],[q*t_delta,t_delta^2]], and -- has positive determinant because its first derivative in delta is 2t(3-p^2)-2d>0, while q/eta corrections are O(delta^2). The resulting Gram is PSD rank four (realizable already in R4, hence in R5) and C(delta)->Cstar. The graph automorphism (0,1,2,3,4,5,6,7)->(0,1,5,6,4,2,3,7) exchanges P1 and P2.


## Conditional Type-E raw-excess consequence

**[PROVED EXACTLY — conditional on the retained at-most-three-active F3 estimate]** If the previously retained F3 core estimate d_core <= (sqrt(3)/2)*A_C applies to the mass-selected matching, the exact sharp floor gives

    A_C-d_core > (1-sqrt(3)/2)*Cstar
                = 0.00123977586632222... > 12397/10000000.

The last strict rational comparison follows from Cstar>9253813/10^9 and sqrt(3)<1732051/10^6. This supersedes the historical 0.001207812... local slack, but does **not** force A>383/504 or yield a global Type-E contradiction. This d_core is the retained *three-active local* quantity, not the global six-exception or homogeneous defect sum.

## Status

**[PROVED EXACTLY — standalone]** Algebraic optimum, exact PSD dual, boundary primal, strict R5 approximation, rational root/constant brackets. **[AUDIT CORRECTION]** Old 0.00901523 sharpness witness invalid under two-sided safety; its lower inequality remains valid. **[CONDITIONAL TYPE E]** The mass-selected F3 matching has A_C>Cstar; this does not eliminate Type E or force A>383/504. **[OPEN]** Type E, C, D, generic e>=27, non-isolated branches; e=23/24 classification still assumes delta(G)>=1. Retain M(F3)<=89, M(P)>=S/2-28/3, and Musin/Boyvalenkov. Global range 40<=tau_5<=44.

Exact verifier: research/tau5_F3_alternative_exact_sharp_audit_2026-11-01_verify.py.
