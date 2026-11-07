# Type E: exact radical isolated-16 frame floor and strict-margin transfer (2026-11-07)

**[PROVED EXACTLY — conditional on canonical F3 matching and retained upstream theorems].** Type E remains **OPEN**; global proved range `40 <= tau_5 <= 44`.

## Statement

For the canonical F3 matching let `C=sum_(four core) a_i`, `B=sum_(sixteen isolated) a_i`, and `A=B+C<=383/504`. The retained canonical radical SOS theorem gives

```
C > c0 = 2-(sqrt(6)+sqrt(2))/2.
```

Therefore `B < b0 = 383/504-c0 = (sqrt(6)+sqrt(2))/2-625/504`,
numerically `b0=0.691772287498772...`. The sixteen isolated projected
half-differences have `||z_i||^2=1-a_i` and all 120 pairings are safe.
Writing `Q_II=sum_(i<j isolated) (z_i.z_j)^2`, one has the **strict exact
radical improvement**

```
Q_II > F(b0),
F(b) = 1393/80 - 17*b/10 - 2*b^2/5,
F(b0) = 11497727/635040
        -(223/630)*(sqrt(6)+sqrt(2)) -(2/5)*sqrt(3)
      = 16.04506755215158... .
```

This improves the previous rational-transfer floor
`254678471/15876000 = 16.0417...`, without changing its proof-status
or claiming an excluded configuration.

## Proof

The exact five-dimensional frame identity for sixteen vectors is

```
Q_II = 88/5 - 11*B/5 + B^2/10 - U_I/2
       + (1/2)*||Z_I - (16-B)*I_5/5||_F^2,
U_I=sum_(isolated) a_i^2.
```

For `0<=a_i<1/4`, `B< b0<3/4`, capped majorization gives, when
`1/2<=B<3/4`,

```
U_I <= 1/8 + (B-1/2)^2.
```

For `B<=1/2`, the weaker bound `U_I<=B/4` gives
`Q_II >= 88/5-(93/40)*B+B^2/10 >= Q_II(B=1/2)`;
the latter is larger than `F(b0)`. For `1/2<=B<b0`,
the displayed frame identity gives `Q_II>=F(B)>F(b0)`, since
`F'(B)=-17/10-4B/5<0`. This proves the strict floor.

## Quantitative deep-contact margin

The retained canonical radical SOS theorem also says that if all six
noncanonical F3 deep endpoint contacts are at most `-1/2-epsilon`,
then

```
C >= c0 + (sqrt(6)/3)*epsilon.
```

Set `k=sqrt(6)/3`. Thus `B<=b0-k*epsilon`, and whenever
`1/2<=b0-k*epsilon` the same frame argument gives

```
Q_II >= F(b0-k*epsilon)
     = F(b0) + k*(17/10+4*b0/5)*epsilon
              -(2/5)*k^2*epsilon^2.
```

For larger margins with `B<1/2`, the preceding `B<=1/2` bound
applies instead. This is a **conditional quantitative stability transfer**
from strict endpoint contacts to isolated-frame squared correlations.
It does not control the mixed core-isolated correlations by itself.

## Ledger

**[PROVED EXACTLY, conditional on retained canonical core SOS and Type-E
mass ceiling]** The exact radical floor and margin-dependent formula.
The algebra can be checked by the companion SymPy verifier.

**[NOT CLAIMED]** No new Type-E exclusion, D5 labeling, six-exception/
Q-kernel bijection, or improvement to the global kissing-number bound.
The alternative F3 matchings are not covered by the canonical radical
core floor.

**[RETAINED]** star <=70/3; broom M(F3)<=89; matching
M(P)>=S/2-28/3; twenty-edge mass >=2137/6; A<=383/504;
Musin/Boyvalenkov zero-midpoint exclusion. Sparse e=23/24 classification
requires delta(G)>=1. Types C, D, E, generic e>=27 and the non-isolated
branch remain open.

**Next:** couple this lower bound to `tr(Z_I Z_C)` and the signed
cross-endpoint constraints; no scalar isolated-frame bound alone rules
out the exact local F3 path witnesses.
