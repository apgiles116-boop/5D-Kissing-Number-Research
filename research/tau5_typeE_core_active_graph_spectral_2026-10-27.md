# Type E: exact four-core active-graph spectral midpoint obstruction

Date: 2026-10-27. **[PROVED EXACTLY — conditional on retained Type-E endpoint hypotheses]**. **[OPEN]** No general Type-E exclusion.

## 1. Endpoint sign lemma

For any two distinct selected deep edges, write their unit endpoints as `m_i ± z_i` and `m_j ± z_j`, with `m_i·z_i=0`. Set
`B=m_i·m_j`, `X=m_i·z_j`, `Y=z_i·m_j`, `Z=z_i·z_j`, `d_ij=(|Z|-1/2)_+`.
All four cross-endpoint kissing inequalities have upper bound 1/2. Pairing the two inequalities with the same sign as Z gives, for nonzero Z and `sigma=sign(Z)`,

```
B + |Z| + |X+sigma Y| <= 1/2.                           (1)
```

Thus on every active exceptional core pair (`d_ij>0`),

```
d_ij + |X+sigma Y| <= -m_i·m_j.                         (2)
```

An exceptional raw projective violation requires a negative midpoint correlation. The extra absolute-value term is an exact mixing penalty, valid even where the 184-pair Walsh absolute-value safety inequality does not apply.

## 2. Exact active-graph spectral theorem

Let C be the four core indices, `A_C=sum_C ||m_i||²`, and J the graph consisting of the k core pairs with `d_ij>0`. Let `Adj(J)` be its 4-by-4 adjacency matrix. Summing (2) and applying the Rayleigh inequality coordinatewise gives

```
sum_J (d_ij+|X_ij+sign(Z_ij)Y_ij|)
 <= -sum_J m_i·m_j
 <= [-lambda_min(Adj(J))/2] A_C.                        (3)
```

All 64 labeled simple graphs on four vertices were classified using exact symbolic principal-minor PSD tests. The maximum coefficient `c_k=max_{|E(J)|=k}[-lambda_min(Adj(J))/2]` is:

| k active pairs | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| c_k | 0 | 1/2 | sqrt(2)/2 | sqrt(3)/2 | 1 | (sqrt(17)-1)/4 | 1/2 |

The maximizing graph types are empty, one edge, two-edge path, three-star, four-cycle, K4 minus one edge, and K4. This nonmonotonicity matters: six active defects impose a stronger energy charge than four.

If all six are active, the exact identity `sum_{i<j}m_i·m_j=(||sum_C m_i||²-A_C)/2` strengthens (3) to

```
sum_{i<j in C}(d_ij+|X_ij+sign(Z_ij)Y_ij|)
 <= (A_C-||sum_C m_i||²)/2 <= A_C/2.                  (4)
```

The table is sharp for unconstrained four-vector quadratic forms, not necessarily for full Type E.

## 3. Exact Type-E consequences

Retain `A_C<=A<=383/504`. In the six-active branch,

```
sum_Cpairs d_ij <= 383/1008 = 0.37996031746...
mean_Cpairs d_ij <= 383/6048 = 0.06332671957... .     (5)
```

If all six defects are equal, the common core correlation obeys `|z_i·z_j|<=3407/6048=0.56332671957...`. This is an *average* bound, not an individual bound for unequal defects.

The previously verified rational D5 six-exception flex has six equal correlations `491137/821762`, i.e. defects `40128/410881`. Any Type-E endpoint extension with those *fixed projected core vectors* would require

```
A_C >= 12*(40128/410881) = 481536/410881
    = 1.1719597645... > 383/504.                     (6)
```

Thus that particular flex cannot extend to Type E even without the isolated-center covering theorem. This is not a general six-exception exclusion.

For the retained individual defect cap `0<=d_ij<=1/4`, let `f(d)=(1/2+d)^2(d+d²)`. Increasing convexity and (5) give the relaxed six-active quartic positive-defect envelope

```
P_fixed = sum_Cpairs f(d_ij)
 <= f(1/4)+f(383/1008-1/4)
 = 241638909745/1032386052096
 = 0.234058673356... .                                (7)
```

This improves the previous general six-exception envelope 0.284790046861... *in the six-active branch*. The capped-simplex maximizer need not be feasible with six strictly active pairs, so (7) is not claimed sharp for actual Type E. For other active graphs, intersect `sum_J d_ij<=c_k A_C` with the retained global linear defect cap `1780062775/4032758016`.

## 4. Proof ledger and next step

**[PROVED EXACTLY — conditional Type E]** (1)-(7) and the 64-graph exact PSD classification. **[RETAINED]** Global `40<=tau_5<=44`; Type-E `1/49<A<=383/504`; `M(F3)<=89`; `M(P)>=S/2-28/3`; twenty-edge mass `>=2137/6`; 184 safe/six potentially exceptional core pairings; Musin/Boyvalenkov zero-midpoint exclusion; the fixed-versus-weighted harmonic threshold correction. **[OPEN]** Type E in general, Types C/D, generic `e>=27`, and non-isolated branches; sparse e=23/24 classification requires `delta(G)>=1`.

The next finite KKT/SOS problem should branch by the 11 unlabeled four-core active graphs, retain the four-by-four midpoint Gram PSD constraint and (1), then couple them to the 184 safe-pair Walsh mixing penalties and isolated-center row.

Companion exact verifier: `research/tau5_typeE_core_active_graph_spectral_2026-10-27_verify.py`.
