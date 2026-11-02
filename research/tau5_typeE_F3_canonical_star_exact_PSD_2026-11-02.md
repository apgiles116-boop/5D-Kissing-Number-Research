# Type E / F3: exact canonical three-defect star exclusion

**2026-11-02. [PROVED EXACTLY — standalone eight-endpoint theorem].** This proof does not use the withdrawn endpoint-Perron argument, a rank-five hypothesis, or any midpoint-energy bound. **[CONDITIONAL TYPE-E APPLICATION]** The improved canonical defect ceilings additionally require the independently retained F3 triangle-free/C4-exclusion and singleton mass-defect lemmas. **[OPEN]** Type E and the global kissing-number problem remain unresolved; the global proved range is `40 <= tau_5 <= 44`.

## F3 geometry

Let eight unit endpoints `u_0,...,u_7` have strict-deep pairs (inner product `< -1/2`) `02,04,05,14,17,23,27,36,56,57`; all other pairs are safe in `[-1/2,1/2]`. Select canonical matching `P0=(04),(17),(23),(56)` and orient

```
(A0,B0)=(u0,u4), (A1,B1)=(u7,u1),
(A2,B2)=(u2,u3), (A3,B3)=(u5,u6),
w_i=(A_i-B_i)/2.
```

All six quotient pairs have exactly one strict deep cross-contact, always between same-sign endpoints. Writing `h=m_i.m_j` and `d=w_i.w_j`, the same-sign endpoint bounds imply `h+d<0`, while opposite-sign safe contacts imply `h-d>=-1/2`. Hence `d>1/2` is impossible; every positive raw projective defect has `d<-1/2`.

Suppose three defects form a star centered at 0, so `w0.wj<=-1/2` for `j=1,2,3`.

## Exact PSD/SOS certificate

Let `G=(u_i.u_j)` be the 8-by-8 Gram matrix (PSD, diagonal 1). Define the symmetric integer matrix

```
T =
[ 299  115  145 -145    0  146 -146  209
  115  131    0    0  209    0    0    0
  145    0  187    0 -145  188    0  268
 -145    0    0  283  145    0  280    0
    0  209 -145  145  531 -146  146 -209
  146    0  188    0 -146  195    0  268
 -146    0    0  280  146    0  283    0
  209    0  268    0 -209  268    0  387 ].
```

Its leading principal minors, computed **exactly**, are

```
299, 25944, 2097253, 78473174,
776559545, 4645182931, 20057485321, 40545532209.
```

All are positive, so `T` is positive definite (Sylvester). In particular `tr(TG)>=0`.

Define eight nonnegative slacks under the assumed endpoint contacts and star:

```
s1 =  1/2-u0.u1,   s2 =  1/2-u2.u5,
s3 = -1/2-u2.u7,   s4 = -1/2-u3.u6,
s5 = -1/2-u5.u7,
s6 = -1/2-w0.w1,   s7 = -1/2-w0.w2,
s8 = -1/2-w0.w3.
```

The first two are safe upper bounds, the next three strict-deep upper bounds, and the last three are the hypothesized defects. For **every** eight unit endpoints, expanding the 28 independent off-diagonal Gram variables gives the exact identity

```
(81*s1+47*s2+67*s3+70*s4+67*s5
 +209*s6+145*s7+146*s8)/500
 + tr(T*G)/4000 = -1/500.                   (SOS)
```

Indeed all variable coefficients cancel; the weighted slack constants equal `-288/500` and `tr(T)/4000=287/500`. The left side is nonnegative, but the right side is negative. Contradiction.

The deep graph has canonical-matching-preserving automorphisms mapping the selected edge `04` to each of `04,17,23,56`, represented by the endpoint permutations

```
(0,1,2,3,4,5,6,7)
(7,4,2,3,1,5,6,0)
(2,6,0,4,3,7,1,5)
(5,3,0,4,6,7,1,2).
```

The exact verifier checks all four. Thus **no canonical three-positive-defect star exists**, at any center, even in the unrestricted-rank Gram relaxation.

## Conditional canonical Type-E consequences

Retain the independent exact triangle-free and four-cycle exclusions, singleton inequality `delta_ij <= (a_i+a_j)(1-a_i-a_j)/2`, and baseline `A<=383/504`. The positive-defect support is now either at most two edges or a three-edge path `P4` (the star is eliminated). The prior exact concavity/reflection **path-only** optimization therefore gives

```
D_raw < 366383/1016064 = 0.360590474615772...
D_raw + sum(delta_ij^2)
      < 834099607777/2064772104192
      = 0.403966910480615...
```

The formerly conditional high-defect star branch `D+S>=0.405` is now excluded. The six exceptional canonical pairs contribute `Q_core<1.903966910481`. With the baseline frame floor `Q_total>8790283/317520`, the 184 safe pairings satisfy `Q_safe>25.780219912397`, forcing at least 39 with `|z_i.z_j|>1/3`. **[FURTHER CONDITIONAL]** With the separately retained center-sensitive `Q_total>28.3626`, `Q_safe>26.458633089519`, forcing at least 44 of 184; the integer count does not improve.

**[OPEN]** Three canonical path-support orbits and smaller supports; alternative F3 matchings, especially double-positive branches; Types C and D, generic `e>=27`, non-isolated branches. Sparse `e=23/24` classification remains conditional on `delta(G)>=1`. Retain the Type-E star `<=70/3`, broom `M(F3)<=89`, matching `M(P)>=S/2-28/3`, twenty-edge mass `>=2137/6`, and audited Musin/Boyvalenkov zero-midpoint exclusion.

Companion exact checker: `research/verify_typeE_F3_star_PSD_SOS_2026_11_02.py`.
