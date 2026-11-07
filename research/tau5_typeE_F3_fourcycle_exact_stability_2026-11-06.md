# Type E / F3: exact four-cycle squared-excess stability identity

**2026-11-06. [PROVED EXACTLY — local four-cycle Gram identity].**
This refines the previously proved canonical F3 four-cycle cap by retaining
every nonnegative term discarded in that proof. It is not a Type-E exclusion.
Global proved range: `40 <= tau_5 <= 44`.

## Exact identity

Let `v0,v1,v2,v3` be unit vectors in any real Euclidean space.
Assume the four cyclic contacts `v0.v1=-x0`, `v1.v2=-x1`,
`v2.v3=-x2`, `v3.v0=-x3` satisfy `1/2 <= xj <= 1`,
and the two opposite contacts `c=v0.v2 <= 1/2`,
`d=v1.v3 <= 1/2` are safe.

Define the four-cycle squared-contact excess
`X4=sum_j (xj^2-1/4)`, and the vector sum `s=v0+v1+v2+v3`.
Then the following identity holds **exactly**:

```
3/2 - X4
  = (3/2)*(1-c-d)
    + (3/4)*||s||^2
    + sum_j (xj-1/2)*(1-xj).                    (1)
```

Proof: `||s||^2=4+2(c+d)-2 sum_j xj`, so
`3-sum_j xj=1-c-d+||s||^2/2`. Also
`(3/2)*x-1/2-x^2=(x-1/2)*(1-x)`.
Summing four scalar identities and substituting proves (1).
Every term on the right is nonnegative.

## Rigidity / quantitative consequences

**[PROVED EXACTLY]** `X4<=3/2`, with equality only if:

1. Both opposite contacts are exactly `c=d=1/2`;
2. The four vectors sum to zero;
3. Every cyclic magnitude is in the two-point set `{1/2,1}`.

In particular, if every cyclic contact is strictly deep (`xj>1/2`)
and no cyclic magnitude equals 1, then `X4<3/2`.

Writing `eta=3/2-X4>=0`, (1) gives simultaneous stability bounds

```
1-c-d <= (2/3)*eta,
||s||^2 <= (4/3)*eta,
sum_j (xj-1/2)*(1-xj) <= eta.                 (2)
```

Thus a near-extremal cycle must have both safe diagonals close to their
positive threshold, nearly zero vector sum, and every deep magnitude
near either 1/2 or 1. This is **quantitative second-order control** at
the local four-cycle level, not a D5 global stability theorem.

The upper bound is sharp for the weak-contact four-cycle relaxation.
An exact planar equality witness is

```
v0=(1,0), v1=(-1,0),
v2=(1/2,sqrt(3)/2), v3=(-1/2,-sqrt(3)/2).
```

Its cyclic magnitudes are `(1,1/2,1,1/2)`, both diagonals are
`1/2`, and `s=0`. This witness does not satisfy strict deep
inequalities on two edges and is **not** an F3 or Type-E realization.

## Application to canonical F3

For canonical matching `P0=(04),(17),(23),(56)`, use the F3
four-cycle `0-2-7-5-0`. The diagonals `07,25` are safe. The
identity applies directly to the four unmatched deep contacts.
The two remaining unmatched F3 deep contacts are `14,36`.

With `X_P0=X4+[(u1.u4)^2-1/4]+[(u3.u6)^2-1/4]`, each
remaining term is at most `3/4`. Therefore

```
X_P0 <= 3
 - (3/2)*(1-u0.u7-u2.u5)
 - (3/4)*||u0+u2+u7+u5||^2
 - sum_(e in C4) (x_e-1/2)*(1-x_e).           (3)
```

The previously established strict `X_P0<3` is recovered using
the full F3 incidence. Equation (3) preserves the geometric penalties
that the scalar `X_P0<3` discarded. A potential future
rank-five extension certificate would need to lower-bound at least
one of these penalties using the sixteen isolated deep edges.

## Proof status

**[PROVED EXACTLY]** Identity (1), nonnegative stability terms,
equality characterization, weak-contact equality witness, and
canonical F3 specialization (3). No numerical optimizer, D5 labeling,
or SDP required.

**[OPEN]** No uniform positive stability gap from the present local
hypotheses, no Type-E exclusion, no change to the global range.
The two canonical three-defect paths have exact local R3 witnesses,
so the next essential task remains coupling to the sixteen isolated
edges. Preserve `M(F3)<=89`, matching `M(P)>=S/2-28/3`,
twenty-edge mass `>=2137/6`, `A<=383/504`,
the audited Musin/Boyvalenkov boundary, and the six-exception budgets.
