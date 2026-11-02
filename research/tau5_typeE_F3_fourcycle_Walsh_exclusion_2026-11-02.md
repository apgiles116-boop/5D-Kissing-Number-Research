# Type E / F3: exact exclusion of all four-defect quotient cycles

**2026-11-02. [PROVED EXACTLY — standalone eight-unit-vector F3 theorem].** The global proved range remains `40 <= tau_5 <= 44`. Type E is **OPEN**. This proof is independent of the withdrawn endpoint-Perron argument.

## Contact incidence

The F3 strict deep edges are `02,04,05,14,17,23,27,36,56,57`; all other endpoint pairs are two-sided safe. Its three perfect matchings and switching signs are:

- `P0=(04),(17),(23),(56)`, `g=(+,-,+,+)`.
- `P1=(02),(14),(36),(57)`, `g=(+,-,-,+)`.
- `P2=(05),(14),(27),(36)`, `g=(+,-,+,+)`.

Orient each matched pair as `(A_i,B_i)`, reversing its displayed order when `g_i=-`. Thus `w_i=(A_i-B_i)/2=g_i z_i`. For quotient pairs `01,02,03,12,13,23`, the counts `k_ij` of strict deep contacts among `A_i·A_j,B_i·B_j` are:

- `P0: 1,1,1,1,1,1`
- `P1: 1,1,2,0,1,1`
- `P2: 1,2,1,1,0,1`.

All opposite-sign contacts `A_i·B_j,B_i·A_j` are safe. **For each of the three perfect matchings F of the four quotient vertices, `sum_(ij in F) k_ij=2`**, so its four same-sign endpoint contacts comprise exactly two strict deep and two safe.

## Exact four-cycle identity

Let `E=K4\\F` be any quotient four-cycle. Define

```
N = ||sum_i A_i||^2 + ||sum_i B_i||^2 >= 0,
L_F = sum_(ij in F) [b(A_i,A_j)-A_i·A_j
                    +b(B_i,B_j)-B_i·B_j] > 0,
L_E = sum_(ij in E) [1/2-A_i·B_j+1/2-B_i·A_j] >= 0,
```

where `b=-1/2` for a strict deep pair and `b=+1/2` for a safe pair. Strict positivity of `L_F` follows from the two strict deep contacts.

The **exact identity**, valid for all three F3 matchings and all nine four-cycle cases, is

```
sum_(ij in E) (w_i·w_j+1/2)
    = N/8 + (L_F+L_E)/4 > 0.                    (1)
```

To prove it, expand `4w_i·w_j=A_i·A_j+B_i·B_j-A_i·B_j-B_i·A_j`. The all-pair sums among A and B total `(N-8)/2`. Removing F removes `-L_F`, since the four F contact upper bounds sum to zero. The eight opposite-sign E contacts sum to `4-L_E`. Substitution yields (1) exactly.

The independently audited F3 sign-switching lemma says a positive projected defect has `w_i·w_j=-1/2-delta_ij` with `delta_ij>0`. Four positive defects on E would make the left side of (1) negative. **[PROVED EXACTLY] No F3 matching admits a four-cycle of positive defects.** Combined with the previously proved triangle-free support theorem, every F3 matching has **at most three positive-defect quotient pairs**, including the alternative double-contact branches.

This uses genuine endpoint contacts; it does not substitute their opposite-contact average and does not revive the withdrawn Perron proof.

## Consequences

**[CONDITIONAL — canonical matching selected]** All six canonical quotient pairs are singleton-contact. With the retained exact singleton cap `delta<1/8`,

```
D_raw < 3/8 = 0.375.
```

This improves the earlier conditional `0.40192375` ceiling and **does not require the stronger harmonic cap** `A<0.567`. For an alternative matching with no double-contact defect, the same `3/8` cap applies; when the double defect is positive, retain the global raw cap `1780062775/4032758016`.

The six canonical core projected pairs contribute `Q_core<3/2+3/8+3/64=123/64`. With the separately audited baseline frame bound `Q_total>8790283/317520`, the 184 fully safe pairings satisfy

```
Q_safe > 32720197/1270080 = 25.762311822877...
```

and at least **39 of 184** have `|z_i·z_j|>1/3`.

**[FURTHER CONDITIONAL]** If the separately retained center-sensitive certificate `Q_total>28.3626` applies, then `Q_safe>26.440725`, forcing **at least 44 of 184** such high-correlation safe pairs. The center-sensitive certificate is not re-proved here.

**[VERIFIED EXACT ARITHMETIC]** Companion checker tests all ten deep contacts, all three switching vectors, all nine complementary C4 patterns, the incidence `k(F)=2`, and (1) symbolically with 28 independent Gram variables.

**[WITHDRAWN — STILL WITHDRAWN]** Earlier endpoint-Perron spectral inference and its 45/46 safe-pair counts.

**[OPEN]** Type E three-defect support, alternative double-positive branch, Types C and D, generic `e>=27`, non-isolated branch. The sparse `e=23/24` classification still assumes `delta(G)>=1`. Preserve star `<=70/3`, broom `M(F3)<=89`, matching `M(P)>=S/2-28/3`, twenty-edge mass `>=2137/6`, `A<=383/504`, and the Musin/Boyvalenkov zero-midpoint exclusion. Global `40<=tau_5<=44` unchanged.

Next: exact small Gram/SOS optimization on remaining three-defect star and path supports, coupled to the sixteen isolated edges.
