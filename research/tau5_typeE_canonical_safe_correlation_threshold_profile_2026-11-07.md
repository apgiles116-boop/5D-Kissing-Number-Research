# Type E: exact canonical safe-correlation threshold profile (2026-11-07)

**[PROVED EXACTLY — conditional on the retained canonical matching and frame certificates].** No Type-E exclusion is claimed; global proved range remains `40 <= tau_5 <= 44`.

## Input ledger

For the canonical F3 matching, the independently retained endpoint-charge theorem gives
`D_raw <= 1/4`, at most three active singleton projected defects, and each
`delta < 1/8`. Therefore the six core projected squared correlations obey

```
Q_core <= 6/4 + D_raw + sum(delta^2) <= 3/2+1/4+1/32 = 57/32.
```

The previously audited global projected-frame floor is
`Q_total >= 8790283/317520`, conditional on the Type-E midpoint-energy
and capped-mass majorization hypotheses. Hence

```
Q_safe >= 16449401/635040 = 25.902936822877...
```

for the **184 fully safe projected pairings**. Their correlations satisfy
`|z_i.z_j| <= 1/2`.

## Exact threshold-count theorem

For any rational `0 <= t < 1/2`, let `N_t` be the number of those 184
safe pairs with `|z_i.z_j| > t`. Each of the other `184-N_t` squared
correlations is at most `t^2`, and each counted correlation is at most
`1/4`. Therefore

```
Q_safe <= 184*t^2 + N_t*(1/4-t^2).
N_t >= ceil((16449401/635040-184*t^2)/(1/4-t^2)).
```

The ceiling is truncated below at zero when necessary. Since the rational
lower bound is nonintegral for the thresholds below, the integer counts are
unambiguous even if the global Q bound is stated non-strictly.

| t | exact lower bound on N_t |
|---|---:|
| 1/10 | 101 |
| 1/5 | 89 |
| 1/4 | 77 |
| 3/10 | 59 |
| 1/3 | 40 |
| 7/20 | 27 |

This is a **necessary multiscale concentration profile**, not an independent
new frame theorem or a proof of Type E impossibility. It may be used as an
integer cardinality constraint when coupling the sixteen isolated deep edges
to the four core pairs in rank five. A scalar pair-count alone does not
establish the required rank-five obstruction.

**[FURTHER CONDITIONAL]** The separately retained center-sensitive
`Q_total > 28.3626` would improve these thresholds, but it has not been
re-audited in this note and is deliberately excluded from the table.

**[OPEN]** Rank-five extension obstruction for the two locally realizable
canonical three-defect paths and alternative-selected double-contact cases.
Types C, D, generic `e>=27`, and non-isolated branches remain open.
Sparse `e=23,24` classification still requires `delta(G)>=1`.
Retain star `<=70/3`, broom `M(F3)<=89`, matching
`M(P)>=S/2-28/3`, twenty-edge mass `>=2137/6`,
`A<=383/504`, and Musin/Boyvalenkov's antipodal zero-midpoint exclusion.
