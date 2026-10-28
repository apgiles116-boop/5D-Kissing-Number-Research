# Type E: exact Delsarte safe-contact slack feeds back into mass, Q-frame stability (2026-10-28)

**[PROVED EXACTLY — universal harmonic/algebraic statements]** The Delsarte polynomial records a nonnegative slack on *every* nondeep pair, including the isolated-center row and the 184 fully safe selected-edge pairings. The two- and four-endpoint Walsh formulas and the contact-quantization inequality below are exact.

**[PROVED EXACTLY — CONDITIONAL TYPE E]** Assuming the retained 41-code graph structure, the F3 broom bound `S<=89`, the matching mass theorem `M(P)>=S/2-28/3`, and the retained 184-safe/six-core classification, the new quantitative bounds are

    A + (r/15)*N <= Astar,
    U + (r^2/15)*N <= Ustar,                            (T1)

where `N` is the total nondeep Delsarte slack, `r=D^{-1}(15)`, `Astar=1/2+r+s1`, `Ustar=1/8+r^2+s1^2`, `s1=D^{-1}(41/6)`. They strengthen the scalar mass bounds by a **positive explicit penalty on the isolated-center and 184-safe contact rows**. In particular `r/15=0.00741701379646...`, `r^2/15=0.00082518140485...`.

**[OPEN]** These are necessary inequalities, not a Type-E contradiction or a proof that tau_5=40.

## 1. Full Delsarte slack, not just the deep mass 410

Let `F(t)=7t^2(4t^2-1)=28t^4-7t^2`. Its positive-definite harmonic expansion (as in the 2026-10-27 mass-concavity note) gives `sum_{u,v} F(u.v)>=41^2`. The 41 diagonal terms contribute `41F(1)=861`. Call a pair *deep* when its scalar product is `<-1/2`, and *nondeep* otherwise. Kissing feasibility gives `t<=1/2`; hence all nondeep pairs have `|t|<=1/2` and `F(t)<=0`.

Define the **nondeep polynomial slack**

    N := sum_{unordered nondeep {u,v}} [-F(u.v)] >= 0.

Writing `Mdeep=sum_{unordered deep}F(u.v)`, the harmonic inequality gives exactly

    Mdeep >= 410 + N.                                  (1)

For the Type-E graph `H=16 K2 + F3`, there are 26 deep edges and `C(41,2)-26=794` nondeep pairs. With 20 selected deep edges (16 isolated edges plus four matching edges of F3), the 794 nondeep pairs partition as:

* 40 pairs between the isolated center and the 40 selected endpoints: `N0`;
* 736 contacts from the 184 entirely safe distinguished-edge pairings: `NR`;
* 18 remaining safe contacts among the six exceptional core pairings: `NKsafe`.

Thus `N=N0+NR+NKsafe`, with every summand nonnegative. This is an exact partition; the six other F3 cross-contacts are deep.

## 2. Strengthened F3 scalar mass inequalities

For a selected deep edge `m_i +/- z_i`, put `a_i=||m_i||^2`, `D(a)=21-F(2a-1)=196a-644a^2+896a^3-448a^4`. Set

    DI=sum_{16 isolated selected edges}D(a_i),
    DC=sum_{4 selected F3 matching edges}D(a_i),
    x=sum_I a_i, y=sum_C a_i, A=x+y,
    U=sum_i a_i^2, S=M(F3).

Since the 16 isolated deep edges have mass `336-DI`, (1) gives

    S >= 74+DI+N.

Using `S<=89` and `84-DC=M(P)>=S/2-28/3` gives

    DI+N <= 15,
    DC+(DI+N)/2 <= 169/3.                             (2)

These retain the *entire* nondeep slack, rather than discarding it as in the old mass-410 argument.

The polynomial D is increasing and strictly concave on `[0,1/4]`, `D(0)=0`, `D(a)>=84a`. Thus `x<=5/28<1/4` and `DI>=D(x)`. For fixed `N in [0,15]`, define

    rN=D^{-1}(15-N),
    sN(x)=D^{-1}(43/3-(D(x)+N)/2),
    s1=D^{-1}(41/6).

Equation (2) gives `0<=x<=rN`. For `y>1/2`, capped-simplex concavity gives `DC>=42+D(y-1/2)` and `y<3/4`; hence `y<=1/2+sN(x)`. For `y<=1/2`, the same bound is automatic. Moreover

    U <= 1/8 + x^2 + sN(x)^2.                         (3)

The functions `sN(x)`, `x+sN(x)`, and `x^2+sN(x)^2` are convex on `[0,rN]`. Their maxima are therefore at the endpoints. At `x=rN`, `sN(rN)=s1`; at `x=0`, `sN(0)=D^{-1}(43/3-N/2)`.

## 3. Endpoint comparison and sharp linear slack coefficients

For completeness, the A endpoint at `x=rN` dominates. Write `r=rN`, `s=s1`, so `D(s)=41/6`. We need

    D(s+r) >= D(s)+D(r)/2.

This follows by integration from `2D'(s+t)>D'(t)` for `0<=t<=r<=r0:=D^{-1}(15)<9/80`. Indeed `s<1/25` and `D'` decreases, so

    2D'(s+t)-D'(t) > 2D'(t+1/25)-D'(t)
      = -1792t^3+(56448/25)t^2-(546952/625)t
        +1583316/15625
      >= 82341/250000 > 0

on `[0,9/80]`, by dropping the positive quadratic and bounding the two negative terms at `9/80`. Consequently

    A <= 1/2+rN+s1.                                  (4)

Since `D^{-1}` is convex, `rN=D^{-1}(15-N)` lies below the chord joining `(N,rN)=(0,r0),(15,0)`, giving `rN<=r0*(1-N/15)`. This proves the first bound (T1).

For U, convexity of `x^2+sN(x)^2` gives

    U <= 1/8 + max{ rN^2+s1^2, sN(0)^2 }.

Both expressions inside the maximum are convex functions of N. Their maximum is convex, so it lies below the chord between its endpoint values `r0^2+s1^2` at N=0 and `s1^2` at N=15. (At N=0, `r0^2+s1^2>sN(0)^2`, checked by exact rational root brackets.) This proves the second bound (T1). These coefficients are optimal for this scalar endpoint-envelope argument; no full code realizing equality is asserted.

## 4. Explicit center and 184-safe Walsh polynomials

Let `u=x0` be the isolated-center unit vector, `b_i=u.m_i`, `t_i=u.z_i`. Both center-endpoint products `b_i +/- t_i` lie in `[-1/2,1/2]`. Their exact nonnegative contribution to N0 is

    -F(b_i+t_i)-F(b_i-t_i)
      =14(b_i^2+t_i^2)-56(b_i^4+6b_i^2*t_i^2+t_i^4). (5)

For a fully safe selected-edge pairing i,j, write

    B=m_i.m_j, X=m_i.z_j, Y=z_i.m_j, Z=z_i.z_j.

The four endpoint products are `B+tau X+sigma Y+sigma*tau Z`. Define `L2=B^2+X^2+Y^2+Z^2` and

    L4=B^4+X^4+Y^4+Z^4
       +6*(B^2*X^2+B^2*Y^2+B^2*Z^2
           +X^2*Y^2+X^2*Z^2+Y^2*Z^2)+24*B*X*Y*Z.

Walsh orthogonality gives `sum endpoint_products^2=4L2` and `sum endpoint_products^4=4L4`. Therefore the exact nonnegative 4-contact slack is

    N_ij = 28*L2 - 112*L4 >=0.                       (6)

Summing (6) over the 184 fully safe pairings gives NR. Equations (5)-(6) are ready for direct coupling to the existing frame-mixing and quartic harmonic identities; they involve precisely the previously retained variables B,X,Y,Z.

## 5. Quantitative contact-quantization and Q-frame bridge

For any `|t|<=1/2`, set `rho(t)=min(|t|,1/2-|t|)`. The elementary sharp bound

    -F(t)=7t^2(1-4t^2) >= (21/4)*rho(t)^2            (7)

holds: on `[0,1/4]` use `1-4t^2>=3/4`; on `[1/4,1/2]` divide by `(1/2-t)^2` and use monotonicity. Equality occurs at `|t|=1/4` and `t=0, +/-1/2`.

Combining (7) with (T1) yields a **second-order contact stability inequality**

    A + (7*r0/20)*sum_{794 nondeep pairs}rho(u.v)^2 <= Astar.   (8)

The coefficient `7*r0/20=0.0389393224314...` is exact. In particular, scalar near-saturation forces all 40 center and 736 fully safe cross-endpoint contacts toward the discrete set `{0,+/-1/2}` in aggregate square distance.

Finally let `w_ij=(z_i.z_j)^2`, `Vz=||sum z_i z_i^T-((20-A)/5)I||_F^2`, and `Lstar=30-3Astar+Astar^2/10-Ustar/2`. The exact Q-frame identity gives

    sum_{i<j}w_ij-Lstar
      =(Astar-A)*(3-(Astar+A)/10)+(Ustar-U)/2+Vz/2.

By (T1),

    sum_{i<j}w_ij >= Lstar + cN*N + Vz/2,           (9)

    cN=(r0/15)*(3-Astar/5)+r0^2/30
      =0.02169788199019... >0.

For the six core pairings K and 184 safe pairings R, let `CK=473/256` for P1/P3 and `CK=57/32` for P2, using the previously retained F3 endpoint lemmas. Then

    sum_R w_ij >= Lstar-CK+cN*(N0+NR+NKsafe)
                  +Vz/2+(CK-sum_K w_ij).            (10)

All extra terms displayed on the right are nonnegative. This is a direct, quantitative bridge between the 184-safe polynomial slack, isolated-center row, and global Q/frame lower bound. It is **not yet a contradiction** with the available upper bound on the safe squared-correlation mass.

## Proof-status ledger

**[PROVED EXACTLY — conditional Type E]** (T1), (8)-(10), using the retained F3 mass/graph inputs and the exact polynomial identities proved here. No D5 labeling or generic SDP is needed.

**[RETAINED]** `M(F3)<=89`, matching mass `>=S/2-28/3`, older `A<=383/504`, rigorous Musin/Boyvalenkov zero-midpoint exclusion, and the branchwise core mass caps (conditional on prior endpoint lemmas). The new `Astar,Ustar` remain stronger conditional scalar ceilings.

**[OPEN]** Type E, Types C and D, generic `e>=27`, and non-isolated branches. The sparse `e=23,24` classification still assumes `delta(G)>=1`. Global proved range remains **40<=tau_5<=44**.

Companion verifier: `tau5_typeE_Delsarte_safe_slack_mass_stability_2026-10-28_verify.py`.
