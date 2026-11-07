# Type E / F3: canonical endpoint-charge audit strengthens safe-correlation count

**2026-11-07. [PROVED EXACTLY, conditional on the retained canonical F3 matching and global Type-E frame hypotheses].** This note is a **ledger reconciliation**, not a new core exclusion. The endpoint-charge theorem of 2026-10-27 already supplies a sharper canonical defect budget than several later documents used. The global proved range remains `40 <= tau_5 <= 44`; Type E is OPEN.

## Exact endpoint-charge input

In the canonical matching `P0=(04),(17),(23),(56)`, orient four selected pairs so every quotient pair has exactly one same-sign strict deep cross-contact. For its projected vectors `w_i`, let
`delta_ij=(-1/2-w_i.w_j)_+`, `D=sum delta_ij`, and `k=# {ij:delta_ij>0}`.
The exact 2026-10-27 endpoint-charge identity gives

```
k/2 + 2D + 1/2*(||sum_i w_i||^2 + ||sum_i m_i||^2) <= 2.   (1)
```

The same retained theorem proves `k<=3` and each positive singleton defect `delta<1/8`. If `k=3`, (1) implies `D<=1/4`; if `k<=2`, the individual cap implies `D<1/4`. Therefore **for every canonical branch**

```
                         D <= 1/4.                           (2)
```

This was already in `tau5_typeE_F3_endpoint_charge_2026-10-27.md`, and is **stronger** than the subsequently displayed canonical path-only ceiling `366383/1016064 ≈ 0.36059`. That latter ceiling is valid but should not be treated as best available. In particular, a later canonical conditional analysis assuming `D>=1/3` has an empty feasible hypothesis after (2); its conclusions are not evidence of a realizable high-defect branch.

## Exact transfer to 184 fully safe projected pairings

For each of six canonical core pairings `q_ij=w_i.w_j`, `q_ij^2 <= 1/4 + delta_ij + delta_ij^2`.
With `delta_ij<1/8` and `D<=1/4`, convex concentration on the capped simplex yields

```
sum delta_ij^2 <= 2*(1/8)^2 = 1/32.
Q_core <= 6/4 + 1/4 + 1/32 = 57/32.                 (3)
```

The capped-simplex bound is valid regardless of the support pattern (and can be approached only at two caps in this relaxation). No D5 labeling is used.

Retain the established global projected frame lower bound

```
Q_total >= 8790283/317520.
```

Then

```
Q_safe >= 8790283/317520 - 57/32
       = 16449401/635040 = 25.902936822877... .            (4)
```

For `K` of the 184 fully safe projected pairings with `|q_ij|>1/3`,
all other safe pairings have `q_ij^2<=1/9`, and all safe pairs have
`q_ij^2<=1/4`. Hence

```
Q_safe <= (184-K)/9 + K/4 = 184/9 + 5*K/36.        (5)
```

Combining (4)-(5) gives

```
K >= 40,                                             (6)
```

because at `K=39` the upper bound is strictly smaller than (4).
The exact gap is computed in the companion rational checker.

**[FURTHER CONDITIONAL]** If the separately retained center-sensitive
certificate `Q_total > 28.3626 = 141813/5000` applies, then
`Q_safe > 531627/20000 = 26.58135`, forcing **K>=45** by (5).
The center-sensitive certificate is **not re-proved or audited here**,
so 45 must not be called unconditional.

## Proof-status and research implications

- **[PROVED EXACTLY, with retained Type-E canonical hypotheses]** Canonical `D<=1/4`, `Q_core<=57/32`, `Q_safe>=16449401/635040`, and `K>=40`. The new contribution is recognizing and propagating the already established stronger endpoint-charge budget, not proving a new endpoint-charge lemma.
- **[FURTHER CONDITIONAL]** `K>=45` uses the separately retained center-sensitive frame certificate.
- **[OPEN]** Neither count contradicts known geometry. The two canonical three-defect path orbits have exact local R3 witnesses, and a global rank-five obstruction involving the sixteen isolated edges is still needed. No Type-E exclusion or global improvement is claimed.
- **[RETAINED]** Star `<=70/3`; broom `M(F3)<=89`; matching `M(P)>=S/2-28/3`; twenty-edge mass `>=2137/6`; `A<=383/504`; Musin/Boyvalenkov zero-midpoint boundary exclusion; general six-exception raw and homogeneous defect ceilings. Types C, D, generic `e>=27`, and non-isolated branch remain open; sparse `e=23,24` classification requires `delta(G)>=1`.

**Verifier:** `research/verify_typeE_canonical_charge_Qsafe_count_2026_11_07.py`.
