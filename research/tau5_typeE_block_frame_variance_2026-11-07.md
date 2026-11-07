# Type E: exact isolated/core frame-variance coupling (2026-11-07)

**[PROVED EXACTLY — universal linear algebra, conditional Type-E application].** This is a structural identity and a rank-four core anisotropy floor, **not** a Type-E exclusion. The proved global range remains `40 <= tau_5 <= 44`.

## Block decomposition

For the twenty projected half-differences `z_i in R^5`, partition into sixteen isolated matched edges `I` and four matched F3 core edges `C`. Set

```
Z_I = sum_(i in I) z_i z_i^T,  T_I = tr Z_I,
Z_C = sum_(i in C) z_i z_i^T,  T_C = tr Z_C,
E_I = Z_I - (T_I/5) Id, E_C = Z_C - (T_C/5) Id,
V_I = ||E_I||_F^2, V_C = ||E_C||_F^2,
Delta = ||E_I+E_C||_F^2.
Q_II = sum_(i<j in I) (z_i.z_j)^2,
Q_CC = sum_(i<j in C) (z_i.z_j)^2,
Q_IC = sum_(i in I,j in C) (z_i.z_j)^2.
```

The following are **exact identities**:

```
V_I = 2 Q_II + sum_(i in I) ||z_i||^4 - T_I^2/5,
V_C = 2 Q_CC + sum_(i in C) ||z_i||^4 - T_C^2/5,
Q_IC = T_I*T_C/5 + (Delta - V_I - V_C)/2.       (1)
```

They follow by expanding Frobenius squares and `tr(Z_I Z_C)=Q_IC`.
Cauchy-Schwarz gives the **exact block stability constraints**

```
|Q_IC - T_I*T_C/5| <= sqrt(V_I V_C),             (2)
(sqrt(V_I)-sqrt(V_C))^2 <= Delta
                          <= (sqrt(V_I)+sqrt(V_C))^2.  (3)
```

Equation (1) retains the signed isolated/core covariance discarded by a standalone Welch bound on the sixteen isolated lines. No D5 line labeling or correspondence between six exceptional pairings and Q-kernel modes is assumed.

## Core rank forces nonzero anisotropy

Since `Z_C` is the sum of only four rank-one PSD matrices in `R^5`, its rank is at most four. If `T_C>0`, one eigenvalue is zero and Cauchy-Schwarz on the other four eigenvalues yields

```
tr(Z_C^2) >= T_C^2/4,
V_C = tr(Z_C^2)-T_C^2/5 >= T_C^2/20.           (4)
```

Write `C_m=sum_(i in C)||m_i||^2`, so `T_C=4-C_m`.
Under the retained Type-E total midpoint cap `A<=383/504`, we have
`0<=C_m<=A`, hence `T_C>=4-383/504=1633/504`. Therefore

```
V_C >= (1633/504)^2/20
    = 2666689/5080320 > 0.5249.               (5)
```

This floor is **matching-independent**: it applies to each of the three F3 perfect matchings, provided its four selected core edges are part of the twenty-edge Type-E matching satisfying the stated mass cap.

**[PROVED EXACTLY — conditional stability consequence]** Combining (3) and (5), if a future argument establishes `Delta <= d < 2666689/5080320`, then

```
sqrt(V_I) >= 1633/(504*sqrt(20)) - sqrt(d),
V_I >= (1633/(504*sqrt(20))-sqrt(d))^2.        (6)
```

The hypothesis `Delta<=d` is **not** presently established; (6) is not a new numerical lower bound on `Q_II` in the existing ledger.

## Why this is useful and what remains open

The earlier sixteen-line Welch floor discards `V_I`, while the full twenty-line Q-frame floor retains only `Delta`. Identity (1) couples both through the **64 isolated/core safe pairings**. Their endpoint constraints may provide a useful upper bound on `Q_IC`, which, combined with (1), would force nonzero `Delta` or `V_I`. Any such bound must be proved; the present identities alone do not yield a contradiction.

**[OPEN]** Type E (all matching branches), Types C and D, generic `e>=27`, and non-isolated branches. Sparse `e=23,24` classification retains its `delta(G)>=1` hypothesis. Preserve the star `<=70/3`, broom `M(F3)<=89`, matching `M(P)>=S/2-28/3`, twenty-edge mass `>=2137/6`, and `A<=383/504`; the Musin/Boyvalenkov zero-midpoint boundary remains source-audited.

Companion exact rational checker: `research/verify_typeE_block_frame_variance_2026_11_07.py`.
