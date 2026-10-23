# Type E: degree-counted 21-line integrality obstruction (2026-10-23)

**Status:** [PROVED EXACTLY] universal 21-vector lemma and vector inequalities; [CONDITIONAL ON RETAINED TYPE-E REDUCTIONS] energy corollary; [OPEN] Type E exclusion. Global range remains `40 <= tau_5 <= 44`.

## Universal 21-line gap [PROVED EXACTLY]

For 21 unit vectors `y_0,...,y_20 in R^5`, put `v_ij=(y_i.y_j)^2`, `phi(v)=7v(4v-1)`, and `P=sum_{i<j}[phi(v_ij)]_+`. Then

```
P > p0=(7 sqrt(15)-21)/20 = 0.3055441711725959...
```

Proof: the exact Gegenbauer identity `phi(t^2)=1+(28/3)P2(t)+(32/3)P4(t)`, with `P2=(5t^2-1)/4` and `P4=(21t^4-14t^2+1)/8`, gives `P-N >= (35/6)V >=0` and `sum v_ij=168/5+V/2`, where `N=sum[-phi(v_ij)]_+` and `V=||sum y_i y_i^T-(21/5)I||_F^2`. Hence `N<=P`, `V<=6P/35`. Also `P>0`, because otherwise `N=V=0`, all `v_ij in {0,1/4}`, and `sum v_ij=168/5` could not be a quarter-integer.

Round every `v<=1/4` to the nearer of 0 and 1/4, with distance `d=min(v,1/4-v)`; round every `v>1/4` to 1/4, with excess `delta=v-1/4`. Put `D_-=sum d`, `D_+=sum delta`. Then `N>=7D_--28D_-^2`, `D_-<=2P/7`, and `P>7D_+` (strict because `P>0`). If `P<=p0`, then `D_-<=2p0/7<1/8`, on which `g(D)=7D-28D^2` is increasing. Setting `d0=1/10-p0/7`, the identity `g(d0)=p0` implies `D_-<=d0`. Therefore the sum of squared correlations lies strictly within 1/10 of some quarter-integer. But it lies in `[168/5,168/5+3p0/35] subset [33.6,33.65)`, every point of which is at least 1/10 from every quarter-integer. Contradiction.

## Degree-counted Type-E bound [EXACT VECTOR LEMMA; CONDITIONAL APPLICATION]

For one selected matching of `H=16K2+F3`, let `x_i^+-x_i^-` be 20 deep pairs, `x_i^±=m_i±z_i`, `a_i=||m_i||^2`, `A=sum a_i<1`. Four core pairs form `J`, `C=sum_{J}a_i`, `M=sum_J m_i`, `W=sum_J sqrt(a_i)m_i`. Normalize `y_0=u` (isolated center) and `y_i=z_i/sqrt(1-a_i)`. Assume `|u.z_i|<=1/2`, `|z_i.z_j|<=1/2` on 184 safe pairs, and `(|z_i.z_j|-1/2)_+<=delta_ij=(-m_i.m_j)_+` on six core pairs.

For a safe pair, `[phi((z_i.z_j)^2/((1-a_i)(1-a_j)))]_+ <= 7(a_i+a_j)/[4(1-A)^2]`; for a center pair replace `a_i+a_j` by `a_i`. The exact total of these 204 weights is **`20A-3C`**: the 4 core vertices have safe degree 16 and the 16 outer vertices have safe degree 19. This replaces the earlier coarse `20A` upper bound.

For a core pair, `delta<=sqrt(a_i a_j)<=A/2` gives `[phi((z_i.z_j)^2/((1-a_i)(1-a_j)))]_+ <= 7(1+A)^2/(1-A)^2 * (delta+delta^2+[1-(1-a_i)(1-a_j)]/4)`. The four-vector Gram bounds are

```
sum_core delta <= C-||M||^2/4,
sum_core delta^2 <= (C^2-||W||^2)/4,
sum_core [1-(1-a_i)(1-a_j)] <= 3C.
```

Therefore, **exactly as a vector inequality**,

```
P <= 7/[4(1-A)^2] *
     {20A-3C+(1+A)^2(7C+C^2-||M||^2-||W||^2)}.
```

Define `fstar(A)=7A[17+(1+A)^2(7+A)]/[4(1-A)^2]`. An explicit nonnegative stability remainder is

```
P <= fstar(A) - 7/[4(1-A)^2] *
 {(A-C)[(1+A)^2(7+A+C)-3]+(1+A)^2(||M||^2+||W||^2)}.
```

The coefficient of `A-C` is at least 4. Thus the refinement penalizes midpoint energy on the sixteen isolated outer pairs as well as two core Gram sums.

Since `fstar` is strictly increasing on `[0,1)` and `P>p0`, exact rational comparison at `a=71393/10000000`, `q=fstar(a)`, gives `735-(20q+21)^2>0`, hence

```
BOXED (conditional Type E): A > 71393/10000000 = 0.0071393.
```

The scalar threshold root `fstar(A)=p0` is approximately `0.00713936313394748`. This improves the earlier `A>1/158` but remains far below the retained `A<=383/504`; it **does not exclude Type E**. If `A<=1/125`, the two-variable bound also forces `C>1/350`.

**Scope:** One fixed mass-selected F3 matching only. Do not transfer constraints between matchings. Retain `M(F3)<=89`, `M(P)>=S/2-28/3`, 20-edge mass `>=2137/6`, `A<=383/504`, and Musin/Boyvalenkov's 21-line zero-midpoint exclusion. Type C, D, E, generic `e>=27`, and non-isolated branches remain open; the sparse `e=23/24` classification is conditional on `delta(G)>=1`. No D5 labeling or six-exception/Q-kernel identification is asserted.

Companion exact rational/SymPy verifier: `research/tau5_typeE_degree_counted_integrality_2026-10-23_verify.py`.
