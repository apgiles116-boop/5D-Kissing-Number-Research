# Type E / F3: canonical four-cycle Gram improvement

**2026-11-06. [PROVED EXACTLY — standalone eight-endpoint F3 theorem].**
This strengthens the earlier dimension-free endpoint-excess bound **only for the
canonical matching** `P0=(04),(17),(23),(56)`. Type E remains OPEN;
the global proved range remains `40 <= tau_5 <= 44`.

## 1. Bipartite four-cycle Gram inequality

Let `u_0,u_2,u_7,u_5` be unit vectors. Suppose the four edges
`02,27,75,50` are strict deep, with correlations `-x_e<-1/2`.
The opposite diagonal pairs `07,25` are safe and satisfy
`u_0.u_7 <=1/2`, `u_2.u_5 <=1/2`.

The squared norm of their sum is nonnegative:

```
0 <= ||u_0+u_2+u_7+u_5||^2
   = 4+2(u_0.u_7+u_2.u_5)-2 sum_(e in C4) x_e.
```

Therefore

```
sum_(e in C4) x_e <= 2+u_0.u_7+u_2.u_5 <=3.      (1)
```

For each `x in [1/2,1]`, the elementary exact factorization

```
(3*x/2-1/2)-x*x = (x-1/2)*(1-x) >=0
```

implies `x*x<=3*x/2-1/2`. Summing four edges and using (1),

```
sum_(e in C4) (x_e*x_e-1/4)
   <= (3/2)*3-2-1 = 3/2.                        (2)
```

This is a dimension-independent exact Gram bound on the **four-edge cycle**.
No D5 template, harmonic SDP, or numerical optimization is used.

## 2. Canonical six-cross-deep excess

The exact F3 deep graph is
`02,04,05,14,17,23,27,36,56,57`, and all other endpoint pairs
are two-sided safe. Under canonical matching `P0`, the six
unmatched strict-deep contacts are

```
C(P0)={02,05,27,57,14,36}.
```

The first four form precisely the cycle `0-2-7-5-0`.
The two remaining edges `14,36` each have squared-contact excess
strictly less than `3/4` because every endpoint has at least two
strict deep neighbors and the deep graph is triangle-free: equality
`|u_i.u_j|=1` would force a forbidden positive contact to another
deep neighbor.

Combining with (2) proves

```
X_P0 := sum_(uv in C(P0)) [(u_u.u_v)^2-1/4] < 3. (3)
```

This **strict canonical bound X_P0<3** improves the prior uniform
`X_P<7/2`. For the two alternative F3 matchings the earlier
`X_P<7/2` remains the proved bound; (3) must not be transferred
to those matchings without a new argument.

## 3. Full Type-E endpoint conservation

For a twenty-edge matching in the isolated-center Type-E branch,
the 760 cross-endpoint contacts contain exactly six deep contacts
and 754 safe contacts. Write `H` for the sum of safe contact
slacks `1/4-c^2`, `A=sum a_i`, `U=sum a_i^2`, and
`Delta=||sum_i(m_i m_i^T+z_i z_i^T)-4I_5||_F^2`.
The retained exact Walsh identity reads

```
H-X_P=70-4A+4U-2Delta.
```

In the canonical-selected branch (3) now supplies the exact necessary
inequality

```
H < 73-4A+4U-2Delta.                            (4)
```

This remains far from a Type-E contradiction; notably it does
**not** bound the homogeneous projected defect by 3.

## Proof ledger

- **[PROVED EXACTLY]** Four-cycle Gram inequality (1)-(2) and strict
  canonical six-cross-contact squared excess (3), in any dimension.
- **[RETAINED]** Star `<=70/3`, broom `M(F3)<=89`,
  matching `M(P)>=S/2-28/3`, twenty-edge mass `>=2137/6`,
  midpoint `A<=383/504`, audited Musin/Boyvalenkov boundary,
  universal Q-frame correlation floor.
- **[OPEN]** No Type-E exclusion; two locally feasible canonical
  three-defect paths still require coupling to the sixteen isolated
  deep edges. Types C/D, generic `e>=27`, non-isolated branch remain
  open; sparse `e=23,24` classification assumes `delta(G)>=1`.

**Next:** Seek a rank-five extension obstruction involving the sixteen
outside deep edges. The inequality here is purely local and cannot
exclude the existing rational three-dimensional F3 witnesses.
