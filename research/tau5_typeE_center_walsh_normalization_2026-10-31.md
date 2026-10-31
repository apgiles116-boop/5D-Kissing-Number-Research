# Type E: isolated-center Walsh cancellation and sharp normalization budget

**2026-10-31 — PROVED EXACTLY, conditional on the retained Type-E selected-deep-pair model and the previously proved universal 21-line defect gap.** This is not a Type-E exclusion. Global proved range: **40 <= tau_5 <= 44**.

## Setting and the center-defect correction

Let `x_0` be an isolated deep-graph vertex, and let twenty disjoint deep edges have unit endpoints `x_i^±=m_i±z_i`. Write `a_i=||m_i||²`, `t_i=||z_i||²=1-a_i`, `0<=a_i<=1/4`, `A=sum_i a_i<=383/504`, and `a_0=0`. Type E has sixteen isolated selected edges and four F3 core selected edges. The 184 non-core selected-edge pairings are safe; the six core pairings may be exceptional. All twenty center-to-selected-edge pairings are also safe.

Because `x_0` is isolated in the deep graph, both endpoint correlations with it lie in `[-1/2,1/2]`. Therefore

```
|x_0·m_i|+|x_0·z_i|
  = max(|x_0·(m_i+z_i)|,|x_0·(m_i-z_i)|) <= 1/2.
```

**[PROVED EXACTLY]** The center's *raw* defect `D_0=sum_i (|x_0·z_i|-1/2)_+` is **zero**. This resolves the center-defect term left open in the previous 21-line quantitative-integrality note.

For two selected deep edges with no cross deep edges, all four cross-endpoint correlations are in `[-1/2,1/2]`. Put `c=m_i·m_j`, `q=z_i·z_j`, `u=m_i·z_j`, `v=z_i·m_j`. Walsh pairing gives

```
|c+q|+|u+v|<=1/2,     |c-q|+|u-v|<=1/2,
```

hence `|q|+|c|<=1/2`. The same inequality holds for center pairs with `q=x_0·z_i`, `c=x_0·m_i`. **Only the 204 safe pairs** receive this two-sided inequality, not the six core pairs.

## Contact-sensitive normalized defect

Define `u_0=x_0`, `u_i=z_i/sqrt(t_i)`, `lambda_ij=sqrt(t_i t_j)`, `kappa_ij=(1-lambda_ij)/2`, and

```
T(a) = sum_{0<=i<j<=20} kappa_ij/lambda_ij
     = (1/2)sum_{i<j}((t_i t_j)^(-1/2)-1),
K    = sum_{204 safe pairs} min(kappa_ij,|c_ij|)/lambda_ij >=0.
```

For a safe pair, `(|u_i·u_j|-1/2)_+ <= [kappa_ij-|c_ij|]_+/lambda_ij`. For a core pair, with `d_ij=(|z_i·z_j|-1/2)_+`, the normalized defect is at most `(d_ij+kappa_ij)/lambda_ij`. As `lambda_ij>=3/4`, summation gives

```
D_norm <= (4/3) D_C + T(a) - K,
D_C = sum_{six core pairs} (|z_i·z_j|-1/2)_+.
```

The retained exact 21-line theorem `D_norm>2/309` therefore implies

```
D_C+(3/4)T(a) > 1/206+(3/4)K.                  (1)
```

## Sharp normalization coefficient for the retained energy cap

**[PROVED EXACTLY; sharp for the mass-only relaxation]**

```
(3/4)T(a) <= C_* A,     C_*=18 sqrt(3)-53/2
                            =4.67691453623979...
```

Proof: `s(x)=(1-x)^(-1/2)` is increasing and convex. At fixed `x+y`, both `s(x)+s(y)` and `s(x)s(y)=[1-(x+y)+xy]^(-1/2)` are maximized by pushing the pair to its permitted extremes. Repeated pairwise transfers show that, for fixed `A`, `T` is maximized by `k=floor(4A)` masses equal to `1/4`, one remainder `r=A-k/4`, and all other masses zero. Put `h=2/sqrt(3)`. Then

```
T_k = (1/2)[binom(k,2)(h²-1)+k(21-k)(h-1)],
T_max(k/4+r)=T_k+(1/2)[kh+20-k]((1-r)^(-1/2)-1).
```

On each mass interval `T_max` is convex. The derivative of `A T'_max-T_max` is `A T''_max>=0`, so `T_max(A)/A` has no interior maximum. At `A=1/4,1/2,3/4`, the values of `(3/4)T_max(A)/A` are respectively `30(h-1)`, `1/4+(57/2)(h-1)`, and `1/2+27(h-1)`. They strictly increase since each successive difference is `1/4-(3/2)(h-1)>0` (`h<7/6`); the limit at `A=0` is `15/4`, smaller still.

For the last interval `3/4<=A<=383/504`, `r<=5/504<1/100`, and `T'_max=(3h+17)(1-r)^(-3/2)/4<(41/8)(100/99)^2<6`, while `T_3/(3/4)>6` (since `h>23/20`). Thus `T_max(A)/A` decreases there. The maximum is at `A=3/4`, with three masses `1/4`, where `(3/4)T/A=T_3=27h-53/2=C_*`. This extremal mass assignment is **not** asserted Type-E feasible.

Consequently

```
D_C + (18 sqrt(3)-53/2) A > 1/206+(3/4)K.   (2)
```

This strengthens the older `D_C+5A>1/206`, without invoking D5 alignment or a rank-13 hypothesis.

## Positive second-order midpoint-frame correction

For two selected edges, Cauchy-Schwarz gives `sqrt((1-a_i)(1-a_j))+sqrt(a_i a_j)<=1`, hence `kappa_ij>=sqrt(a_i a_j)/2>=|m_i·m_j|/2`. Thus

```
K >= (1/2)sum_{184 safe selected-edge pairs}|m_i·m_j|.
```

For the sixteen isolated selected edges, set `A_I=sum_I a_i`, `U_I=sum_I a_i²`. Their midpoint frame operator in R^5 obeys

```
sum_{i<j in I}(m_i·m_j)² >= (A_I²/5-U_I)/2.
```

Since `|m_i·m_j|<=1/4`, `|m_i·m_j|>=4(m_i·m_j)²`. Therefore

```
D_C + (18 sqrt(3)-53/2) A
  > 1/206+(3/8)sum_{184 safe}|m_i·m_j|
 >= 1/206+(3/4)[A_I²/5-U_I]_+.                (3)
```

**[OPEN]** This does not contradict `A<=383/504` or the retained core raw-defect cap. The contact term can vanish for concentrated midpoint masses. Next target: derive a positive lower bound on `K` from signed F3 endpoint/Walsh constraints, or sharpen the universal 21-line defect gap.

**Retained, not reproved:** star `<=70/3`; broom `M(F3)<=89`; matching `M(P)>=S/2-28/3`; twenty-edge mass `>=2137/6`; `A<=383/504`; raw/homogeneous defect caps; Musin/Boyvalenkov zero-midpoint exclusion. Types C, D, E, generic e>=27, and non-isolated branches remain open. Sparse e=23/e=24 classification remains conditional on `delta(G)>=1`.
