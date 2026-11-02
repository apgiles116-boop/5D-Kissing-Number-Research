# F3: sharp canonical-to-alternative matching transfer (2026-11-01)

**[PROVED EXACTLY — standalone eight-unit-vector theorem].** **[CONDITIONAL TYPE E]** The numerical harmonic-cap corollary relies on the retained Type-E scalar/harmonic certificates, not independently re-established here. **[OPEN]** No Type-E exclusion. Global proved range **40 <= tau_5 <= 44**.

## 1. Theorem

Use F3 deep edges 02,04,05,14,17,23,27,36,56,57 and all 18 other pairs two-sided safe. Its three perfect matchings are P0=04|17|23|56 (canonical), P1=02|14|36|57, P2=05|14|27|36. For eight unit vectors u_i define C_k=sum over ij in Pk of ||(u_i+u_j)/2||^2, and S=C_1+C_2.

**[PROVED EXACTLY — universal Gram inequality]** For every lambda>=0,

    S+lambda*C_0 >= 2*lambda+3-(3/2)*sqrt(4+2*lambda^2).      (1)

This requires only unit endpoints and the three specified pairings, not the F3 inequalities. For strict-deep F3, 0<C_0<1. Optimizing lambda yields the **sharp F3 tradeoff**

    S >= g(C_0) := 3-sqrt(9-2*(2-C_0)^2).                     (2)

Equivalently, since 0<S<2,

    (2-C_0)^2 + S^2/2 <= 3*S.                                 (3)

The sharpness in (2) is proved below on an explicit interval containing the retained harmonic cap.

## 2. Exact PSD proof

Order endpoints A=(0,2,5,7), B=(4,3,6,1). The weighted adjacency matrix of P1+P2+lambda*P0 is

    W = [[C4, lambda*I4],[lambda*I4,2J]],

where C4 is the four-cycle on A and J connects opposite indices (0,3),(1,2). If G is the endpoint Gram (PSD, diagonal one),

    S+lambda*C_0 = 4+2*lambda+tr(WG)/4.

Set y=sqrt(4+2*lambda^2)-2, so y(y+4)=2*lambda^2, and

    D=diag(-(y+4)/2*I4, -(y+2)*I4),  K=W-D.

The four Hadamard characters simultaneously diagonalize C4 and J. K has blocks

    mode 0:    [[(y+8)/2,lambda],[lambda,y+4]], det=4(y+4)>0;
    modes 1,2: [[(y+4)/2,lambda],[lambda,y]], det=0;
    mode 3:    [[y/2,lambda],[lambda,y+4]], det=0.

All diagonal entries are positive for lambda>0, so K is PSD. Hence tr(KG)>=0, and

    S+lambda*C_0 >= 4+2*lambda+tr(DG)/4
                  =2*lambda+3-(3/2)*sqrt(4+2*lambda^2).

Continuity handles lambda=0. With h=2-C_0 in (1,2), maximize lambda*h-(3/2)*sqrt(4+2*lambda^2). The maximizing lambda is 2h/sqrt(9-2h^2), and the maximum is -sqrt(9-2h^2), proving (2). Squaring the positive-root inequality proves (3).

## 3. Exact rank-three strict-F3 equality family

**[PROVED EXACTLY — sharpness with all ten deep contacts strict and all 18 nonedges two-sided safe].** For 27/50<=t<=14/25 put

    v=4*t^2*(4-t^2)/(4-t^4),  w=4-v,
    lambda=4*t/(2-t^2), y=4*t^2/(2-t^2).

Let h1=(1,1,-1,-1)/2, h2=(1,-1,1,-1)/2, h3=(1,-1,-1,1)/2. In R^3 set, for i=0,1,2,3,

    A_i=(sqrt(v/2)*h1_i, sqrt(v/2)*h2_i, sqrt(w)*h3_i),
    B_i=(-sqrt(v/2)*h1_i/t, -sqrt(v/2)*h2_i/t,
         -t*sqrt(w)*h3_i/2).

The identities v+w=4 and v/t^2+t^2*w/4=4 show all vectors are unit. The three nontrivial Hadamard modes lie in ker(K), so equality holds in (1). The seven correlation classes are:

| Pair class | Inner product | F3 status |
|---|---|---|
| A-cycle | -4(1-t^2)/(4-t^4) | four strict deep |
| A-opposite | 1-v/2 | two safe |
| B-opposite | -(t^4-2t^2+4)/(4-t^4) | two strict deep |
| B-other | -t^2(1-t^2)/(4-t^4) | four safe |
| A_i-B_i | -3t/(2+t^2) | four strict deep |
| A-B cycle-offset | 2t(1-t^2)/(4-t^4) | eight safe |
| A-B opposite-offset | t/(2-t^2) | four safe |

On the whole interval 11/10<v<6/5 and 14/5<w<29/10; rational bounds show every deep class <-1/2 and every safe class lies in [-1/2,1/2]. Summing gives

    C_0=c(t)=2-6t/(2+t^2),
    C_1=C_2=3t^2/(2+t^2),
    S=6t^2/(2+t^2)=g(c(t)).

The map c(t) is strictly decreasing on the interval. Thus equality in (2) is attained by strictly feasible rank-three F3 configurations for **every** c in [c(14/25),c(27/50)]. This includes the retained harmonic cap A_*.

For a fully rational Gram witness, t=11/20 gives exactly

    C_0=174/307, C_1=C_2=121/307, S=242/307.

The companion verifier checks the rank-three rational Gram and all 28 endpoint pairs exactly. These eight vectors are NOT a construction of the full 41-point Type-E code.

## 4. Conditional Type-E improvement

**[PROVED CONDITIONALLY — ONLY if the mass-selected F3 matching is canonical P0, and the retained stronger harmonic/scalar certificate applies].**

Retain A<=A_* where

    A_*=1/2+r+s=0.5669250570031576...,
    D(r)=1245/256, D(s)=41/6,
    D(x)=196x-644x^2+896x^3-448x^4,
    r,s are the small positive roots.

Then C_0<=A<=A_*. Rational root brackets show 0.566924<A_*<0.566926<567/1000. Since g is decreasing on [0,1],

    C_1+C_2 >= g(A_*)=0.788079473... > 7879/10000,          (4)
    max(C_1,C_2)>7879/20000=0.39395.                          (5)

Moreover f(c)=c+g(c) decreases for 0<=c<=A_*: f'(c)=1-2(2-c)/sqrt(9-2(2-c)^2)<0. Exact rational comparison at c=566926/10^6 gives

    C_0+C_1+C_2 >= A_*+g(A_*) > 271/200 = 1.355.             (6)

This improves the unconditional aggregate lower bound 1.333507310... **only** in the canonical-selected/harmonic-cap branch. The equality family at c=A_* proves (4) is sharp given *only* F3 incidence and C_0<=A_*; a stronger Type-E exclusion must use the other sixteen edges, center, or joint Walsh/Q constraints.

**[SCOPE]** No such conclusion is asserted if the mass theorem selects P1 or P2. This does not force A>383/504 or eliminate Type E. Preserve the stronger retained M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, the Musin/Boyvalenkov antipodal zero-midpoint exclusion, and the six-exception defect certificates.

**[OPEN]** Type E, C, D, generic e>=27, and non-isolated branches. Sparse e=23/24 classification remains conditional on delta(G)>=1. Global proved range: **40<=tau_5<=44**.

Verification: research/tau5_F3_canonical_alternative_tradeoff_2026-11-01_verify.py.
