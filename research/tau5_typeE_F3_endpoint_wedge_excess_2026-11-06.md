# Type E / F3: dimension-free wedge bound for exceptional endpoint squared excess

**2026-11-06. [PROVED EXACTLY — standalone contact-graph theorem].** The global proved range remains `40 <= tau_5 <= 44`; Type E remains **OPEN**. No D5 labeling or harmonic/SDP assumption is used.

## 1. Local Gram wedge inequality

Let `u,v,w` be unit vectors in any Euclidean dimension with strict deep contacts
`u.v < -1/2`, `u.w < -1/2`, and safe opposite endpoints `v.w <= 1/2`.
Write `x=-u.v > 1/2`, `y=-u.w > 1/2`, and `c=v.w <= 1/2`.
The 3-by-3 Gram determinant is nonnegative, hence

```
x^2 + y^2 <= 1 + 2*c*x*y - c^2.                (1)
```

If `x*y <= 1/2`, completing the square in `c` yields
`x^2+y^2 <= 1+(x*y)^2 <= 5/4`.

If `x*y >= 1/2`, the concave function `2*c*x*y-c^2` is increasing for
`c<=1/2`, so (1) implies

```
x^2+y^2 <= 3/4+x*y <= 3/4+(x^2+y^2)/2,
```

hence `x^2+y^2 <= 3/2` in both cases. Therefore

```
[(u.v)^2-1/4] + [(u.w)^2-1/4] <= 1.             (2)
```

This local wedge bound is sharp in isolation: take `u=(-1,0)`,
`v=(sqrt(3)/2,1/2)`, `w=(sqrt(3)/2,-1/2)`; then both deep magnitudes
are `sqrt(3)/2`, the opposite contact equals `1/2`, and (2) is equality.

An individual deep contact has squared excess at most `3/4`.
If its endpoint belongs to another strict deep contact while the other two
endpoints are safe, equality `|u.v|=1` is impossible: `u=-v` would
turn the second deep contact into a forbidden positive correlation `>1/2`.
Thus that individual's excess is **strictly** less than `3/4`.

## 2. Exact F3 incidence and all three perfect matchings

The eight endpoint vertices are `0,...,7`. Their ten strict deep pairs are

```
02 04 05 14 17 23 27 36 56 57
```

and every other endpoint pair is two-sided safe.
The graph is triangle-free and every vertex has deep degree at least two.

For any of the three perfect matchings `P`, define the six unmatched
strict-deep cross contacts `C(P)=E(F3)\\P`. The following exact edge
partitions supply two **edge-disjoint wedges** and two leftover edges:

| Selected perfect matching P | Wedge 1 | Wedge 2 | Unpaired cross edges |
|---|---|---|---|
| 04,17,23,56 | (02,27), center 2 | (05,57), center 5 | 14,36 |
| 02,14,36,57 | (04,05), center 0 | (17,27), center 7 | 23,56 |
| 05,14,27,36 | (02,04), center 0 | (17,57), center 7 | 23,56 |

In each wedge its two outer endpoints are nonadjacent in the strict-deep graph,
so (2) applies. The finite edge-incidence claims are checked by the companion
pure-Python verifier.

Define the cross-endpoint squared excess

```
X_P = sum_{uv in C(P)} [(u.v)^2-1/4]
    = sum_{uv in C(P)} (d_uv+d_uv^2),
d_uv := -1/2-u.v > 0.
```

Two wedges contribute at most `1` each; the two remaining cross contacts
contribute strictly less than `3/4` each (all F3 vertices have another deep
neighbor, and the F3 graph is triangle-free). Consequently, uniformly across
**all three F3 perfect matchings**,

```
                    0 < X_P < 7/2.             (3)
```

The earlier generic twelve-cross-contact upper bound `X<=9` was valid
but discarded the actual F3 incidence. Even merely counting gives six
cross-deep contacts and `X<9/2`; the Gram wedge inequalities give (3).

## 3. Exact interface with the full twenty-edge Walsh frame

Under the retained isolated-center Type-E hypothesis, distinguish a perfect
matching consisting of sixteen isolated `K2` edges and one F3 perfect
matching. The twenty matched deep edges contribute 40 endpoints. Excluding
the twenty matched contacts, there are `4 * binom(20,2)=760` cross-endpoint
contacts: **six deep** (exactly `C(P)`) and **754 safe**.

Let `h(c)=1/4-c^2 >= 0` for each safe cross contact and
`H=sum_safe h(c)`. Write `a_i=||m_i||^2`,
`A=sum_i a_i`, `U=sum_i a_i^2`, and
`Delta=||sum_i(m_i*m_i^T+z_i*z_i^T)-4 I_5||_F^2`.
The exact Walsh/endpoint identity is

```
H-X_P = 70 - 4*A + 4*U - 2*Delta.               (4)
```

Combining (3) and (4) gives a legitimate strict **endpoint-excess cap**
at the six-exception interface. It does **not** upper-bound the *raw projected*
positive defect `sum(max(|z_i.z_j|-1/2,0))`, which is a different quantity;
such a substitution would be invalid.

## 4. Proof ledger and strategy

- **[PROVED EXACTLY]** 3-vector Gram wedge bound (1)-(2), exact F3 edge
  partitions, six-deep / 754-safe count, and `X_P<7/2` for every F3
  matching, independent of dimension.
- **[RETAINED, NOT REPROVED]** Twenty-edge mass `>=2137/6`,
  `A<=383/504`, star `<=70/3`, broom `M(F3)<=89`,
  matching `M(P)>=S/2-28/3`, Musin/Boyvalenkov zero-midpoint exclusion,
  and the previously derived full Walsh identity (4).
- **[OPEN]** No Type-E exclusion or stronger bound on `A`. In
  particular, the two canonical three-defect path orbits have exact local
  rational R3 witnesses (2026-11-02), so excluding them requires
  coupling to the sixteen outside edges. The next meaningful goal is a
  **rank-five extension obstruction**, not another core-only Gram PSD bound.
  Types C, D, generic `e>=27`, and the non-isolated branch remain open;
  sparse `e=23,24` classification remains conditional on `delta(G)>=1`.

**Verification:** `research/verify_typeE_F3_endpoint_wedge_excess_2026_11_06.py`
checks all F3 matching incidence and rational bound exactly. The continuous
Gram inequality is an analytic proof, not claimed to be certified by sampling.
