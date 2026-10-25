# Type E: two-sided safe endpoint constraints and exact frame/defect bridge

**Date:** 2026-10-25. **Status:** [PROVED EXACTLY] the algebraic statements below under their explicit hypotheses; [CONDITIONAL ON RETAINED TYPE-E GRAPH MODEL] their application to 184 safe edge pairings; [OPEN] Type-E exclusion and the value of tau_5.

## 1. Stronger two-sided inequalities on the 184 safe pairings

Let the 20 selected deep edges have endpoints `p_i^s=m_i+s z_i`, `s=±1`, with `m_i·z_i=0`, `a_i=||m_i||²`, `||z_i||²=1-a_i`, and `A=sum a_i<=383/504`. Split their indices into 16 outside-core edges `O` and four core matching edges `C`.

For each of the 120 outside/outside and 64 outside/core pairings, **all four** cross-endpoint inner products lie in `[-1/2,1/2]`, since no cross-pair endpoint is adjacent in the deep graph `16K2 ⊔ F3`. This *does not* automatically hold for the six core/core pairings.

Set `M=m_i·m_j`, `Z=z_i·z_j`, `X=m_i·z_j`, `Y=z_i·m_j`. The four endpoint inner products are
`M+Z+X+Y, M+Z-X-Y, M-Z+X-Y, M-Z-X+Y`.
Their two-sided bounds are equivalent to

```
|M+Z|+|X+Y| <= 1/2,
|M-Z|+|X-Y| <= 1/2.                           (1)
```

Using `|u+v|+|u-v|=2 max(|u|,|v|)` gives

```
max(|M|,|Z|)+max(|X|,|Y|) <= 1/2.             (2)
```

Hence, writing `h_ij=1/2-|Z|`, every one of the 184 graph-safe pairings obeys **all three** constraints

```
|m_i·m_j| <= h_ij,
|m_i·z_j| <= h_ij,
|z_i·m_j| <= h_ij.                            (3)
```

The previously established *one-sided* inequality remains valid on all 190 pairs. The new two-sided conclusion must **not** be imposed on potentially deep core/core endpoint pairings.

## 2. Exact aggregate and frame inequalities

Let `H_184=sum_safe h_ij²`. Define PSD frame matrices
`F=sum z_i z_i^T`, `T=sum m_i m_i^T`, and their restrictions `F_O,F_C,T_O,T_C`.

Summing (3) gives

```
sum_safe (m_i·m_j)² <= H_184,                 (4)
tr(T_O F)+tr(T_C F_O) <= 2 H_184.             (5)
```

The trace in (5) counts precisely the 368 directed mixed squares on the 184 safe pairs, because `m_i·z_i=0`. Define `D_C=tr(T_C F_C)`. Then

```
tr(T F) <= 2 H_184 + D_C,                    (6)
0<=D_C<=3 A_C-A_C²+sum_(i in C) a_i²<=3A_C, (7)
```

where `A_C=sum_(i in C) a_i`. Equation (7) follows from `(m_i·z_j)²<=a_i(1-a_j)` for `i!=j`.

Put `V=||F-((20-A)/5)I||_F²`, `W=||F+T-4I||_F²`, and `U=tr(T²)`. Since `tr(F+T)=20`, polarization gives the **exact identity**

```
tr(T F)=4A-A²/10 + W/2-V/2-U/2.             (8)
```

Therefore the 184-safe Type-E model must satisfy the **quartic necessary inequality**

```
2H_184 + D_C + V/2 + U/2 + A²/10 >= 4A + W/2.      (9)
```

Replacing `D_C` with its upper bound yields

```
2H_184 +3A_C-A_C²+sum_(i in C)a_i²
          +V/2+U/2+A²/10 >=4A+W/2.          (10)
```

Keeping the exact `D_C` and the nonnegative total-endpoint-frame variance `W` is preferable in a finite polynomial/KKT calculation.

## 3. Explicit bridge to the six-exception defect notation

For all 190 pairs write `r_ij=|z_i·z_j|`. Define `L=sum_(r<=1/2)(1/4-r²)`, `P=sum_(r>1/2)(r²-1/4)`. Only the six core pairs can contribute to `P`. Then `L-P=190/4-sum_(i<j)(z_i·z_j)²`.

The previously retained exact Q/frame identity is

```
L+V/2 = 35/2+3A+(1/2)sum_i a_i²-A²/10+P. (11)
```

Eliminating `V` from (9) yields

```
L-P+A+W/2 <= 35/2+2H_184+D_C
                    +(1/2)sum_i a_i²+U/2. (12)
```

This directly connects the global squared-correlation deficit, positive defects on at most six core pairs, safe squared slack, midpoint energy, and two frame variances. **It is a necessary condition, not a Type-E contradiction.** There is still no opposing upper bound on `H_184` sufficient to prove `A>383/504`.

## 4. Proof status

**[PROVED EXACTLY]** Equations (1)-(3) for any pair with all four cross-endpoint dots in `[-1/2,1/2]`; equations (4)-(12) under the 184-safe graph decomposition.

**[OPEN]** Type E, Type C, Type D, generic `e>=27`, non-isolated cases, and a global D5 proximity theorem. The e=23/24 graph classification remains conditional on `delta(G)>=1`.

**[UNCHANGED]** `40<=tau_5<=44`; `M(F3)<=89`; matching mass `M(P)>=S/2-28/3`; selected-edge mass `>=2137/6`; `A<=383/504`. Musin/Boyvalenkov 21-line zero-midpoint boundary exclusion retained. No identification of the six exceptional core pairings with six D5 Q-kernel relations is asserted.
