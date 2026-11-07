# Type E: canonical F3 midpoint floor improves isolated-16 Welch energy

**2026-11-07. [PROVED EXACTLY — conditional on the canonical F3 perfect matching being the mass-selected matching and retained standalone radical SOS].** Type E remains OPEN. Global proved range `40 <= tau_5 <= 44`.

## Canonical-to-isolated mass transfer

Let the selected twenty-edge matching consist of sixteen isolated edges I and canonical F3 matching P0=(04),(17),(23),(56). Let `C=sum_(i in P0) a_i`, `B=sum_(i in I) a_i`, and `A=B+C<=383/504`. The previously proved exact F3 radical SOS theorem gives

```
C > 2-(sqrt(6)+sqrt(2))/2 > 1/15.
```

The last comparison is exact: `sqrt(6)+sqrt(2)<58/15` is equivalent after squaring to `sqrt(3)<391/225`, and `391^2>3*225^2`. Thus

```
B < 383/504-1/15 = 1747/2520.                (1)
```

This is a **canonical-selected branch** statement only. It must not be applied to either alternative F3 perfect matching without a separate core mass floor.

## Isolated-16 frame inequality

Write `U_I=sum_(i in I) a_i^2`, `Z_I=sum_(i in I) z_i z_i^T`, and
`Q_II=sum_(i<j in I)(z_i.z_j)^2`. The exact five-dimensional frame identity is

```
Q_II = 88/5 - 11*B/5 + B^2/10 - U_I/2
       + (1/2)||Z_I - ((16-B)/5)I_5||_F^2.   (2)
```

For `0<=a_i<=1/4`, capped convex majorization gives `U_I<=Umax(B)`, where
`Umax(B)=k/16+(B-k/4)^2` when `k/4<=B<=(k+1)/4` (k integer).
The scalar function

```
F(B)=88/5-11*B/5+B^2/10-Umax(B)/2
```

is strictly decreasing for `0<=B<=1747/2520`: on the k-th interval,
`F'(B)=-11/5+B/5-(B-k/4)=-11/5-4B/5+k/4<0` (here k<=2).
At `b=1747/2520`, `1/2<b<3/4`, hence
`Umax(b)=1/8+(b-1/2)^2`. Equations (1)-(2) imply the **strict** exact bound

```
Q_II > F(b) = 254678471/15876000
            = 16.0417278281683... .           (3)
```

This improves the prior matching-independent floor
`5046067/317520=15.8921233308138...` by exactly
`113101/756000=0.149604497...`.

## Exact threshold profile

All 120 isolated-isolated pairs are safe, `|z_i.z_j|<=1/2`.
For `N_t` pairs with `|z_i.z_j|>t`,

```
Q_II <= 120*t^2 + N_t*(1/4-t^2).
```

The strict floor (3) forces simultaneously

| t | N_t at least | previous all-matching count |
|---|---:|---:|
| 1/5 | 54 | 53 |
| 1/4 | 46 | 45 |
| 3/10 | 33 | 32 |
| 1/3 | 20 | 19 |
| 7/20 | 11 | 10 |

These are exact integer consequences; a pure-Python Fraction verifier checks the radical comparison, rational energy, and every threshold.

## Limitations and next step

**[PROVED EXACTLY, CONDITIONAL TYPE E]** The canonical-selected core mass floor transfers to an improved isolated-only frame floor and five stronger simultaneous safe-pair counts. No numerical optimizer or D5 uniqueness is used.

**[OPEN]** These necessary conditions do not eliminate Type E. The sixteen-isolated block's frame variance was discarded; next derive a *cross-block* lower bound for `tr(Z_I Z_C)` using the four core vectors and the signed endpoint contacts. The alternative F3 matchings require their own core mass certificates. Do not double-count these isolated-isolated pairs in the 184-safe-pair tally.

**[RETAINED]** Star <=70/3; broom M(F3)<=89; M(P)>=S/2-28/3; twenty-edge mass >=2137/6; A<=383/504; Musin/Boyvalenkov zero-midpoint exclusion; six-exception bounds. Types C, D, E, generic e>=27, non-isolated branch OPEN. Sparse e=23/24 classification conditional on delta(G)>=1. Global proved 40<=tau_5<=44.

Verifier: `research/verify_typeE_canonical_isolated16_mass_transfer_2026_11_07.py`.
