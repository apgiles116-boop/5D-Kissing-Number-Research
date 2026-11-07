# Type E: isolated-16 Welch floor and independent safe-pair count (2026-11-07)

**[PROVED EXACTLY — conditional on the retained Type-E midpoint cap]** The sixteen isolated matched deep edges already force a substantial amount of squared projected correlation among themselves. This result is independent of the six exceptional F3 pairs, and is not a Type-E exclusion. Global proved range remains `40 <= tau_5 <= 44`.

Let `I` be the sixteen isolated matched edges, `z_i` their half-differences, `a_i=||m_i||^2`, `B=sum_I a_i`, `U_I=sum_I a_i^2`, and `Q_{II}=sum_{i<j in I}(z_i.z_j)^2`. Since the selected deep edges are unit endpoint pairs, `||z_i||^2=1-a_i`, `0<=a_i<1/4`, and `B<=A<=383/504`. All 120 isolated-isolated pairings are fully safe, hence `|z_i.z_j|<=1/2`.

The exact trace/Welch identity in R5 is

```
Q_II = 88/5 - (11/5)B + B^2/10 - U_I/2
       + (1/2)||Z_I - ((16-B)/5) I_5||_F^2,
Z_I = sum_{i in I} z_i z_i^T.                 (1)
```

The cap `a_i<=1/4` and total `B<=383/504=3/4+5/504` give the sharp scalar majorization bound

```
U_I <= 3/16 + (5/504)^2.
```

The scalar expression in (1), using this uniform U bound, is strictly decreasing in `B` throughout `[0,383/504]`; thus

```
Q_II >= 5046067/317520 = 15.892123330813806... . (2)
```

This lower bound does not assume D5 labeling, canonical F3 matching, or any exceptional defect budget. It does not claim that the scalar majorization extremizer is realizable by a five-dimensional frame.

For a threshold `0<t<1/2`, let `N_t^{II}` count isolated-isolated pairings with `|z_i.z_j|>t`. As all 120 pairs have squared correlation at most 1/4,

```
Q_II <= 120*t^2 + N_t^{II}*(1/4-t^2).
```

Exact rational comparisons with (2) force:

| t | N_t^{II} at least |
|---|---:|
| 1/5 | 53 |
| 1/4 | 45 |
| 3/10 | 32 |
| 1/3 | 19 |
| 7/20 | 10 |

**[PROVED EXACTLY]** These counts apply to the sixteen isolated lines alone, regardless of which F3 perfect matching is chosen. They are additional *localized* necessary conditions, not improvements of the global 184-safe-pair count by themselves. A useful next step is to couple their near-tight frame operator to the four selected core vectors using `tr(Z_I Z_C)` and signed endpoint Walsh constraints. Merely adding these counts to the 184-safe-pair counts would double count.

**[RETAINED, NOT REPROVED]** Star `<=70/3`, broom `M(F3)<=89`, matching `M(P)>=S/2-28/3`, mass `>=2137/6`, `A<=383/504`, Musin/Boyvalenkov antipodal exclusion, and six-exception defect ceilings. Types C, D, E, generic `e>=27` and non-isolated configurations remain open; sparse `e=23,24` classification assumes `delta(G)>=1`.

Verifier: `research/verify_typeE_isolated16_Welch_counts_2026_11_07.py`.
