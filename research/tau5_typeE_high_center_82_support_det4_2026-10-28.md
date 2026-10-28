# Type E high-center: 82-support theorem and determinant-4 star-complement restriction (2026-10-28)

**[NEW — EXACT, CONDITIONAL ON PREVIOUSLY RETAINED HIGH-CENTER CERTIFICATES]** In the high-center branch `s>=7` of the hypothetical Type-E 41-code, the rounded 17-by-17 signed Gram has **at least 82 nonzero off-diagonal unordered pairings**, improving the previous 81. Moreover, every nonsingular principal 7-by-7 block of its integer double has determinant **+/-2 or +/-4**. Thus a rank-seven candidate must have unsigned adjacency rank **exactly six over F_2**; if that binary rank is at most four, the rounded Gram actually has rank at most six. These are necessary conditions, **not** a Type-E exclusion.

## Inputs (retained, not independently reproved here)

Let `v` be the isolated center and `z_1,...,z_16` the projected half-differences of the sixteen isolated deep edges. Put `a_i=||m_i||^2` and `x=sum a_i<1/2500`. The previously proved conditional high-center resource certificate gives

- `N=sum_nondeep 7t^2(1-4t^2)<=5/64`;
- each nondeep `|t|<1/9` (low) or `12/25<|t|<=1/2` (high);
- the two center contacts for an isolated edge are both low or both high, and all four endpoint contacts for an isolated-isolated edge pairing are simultaneously low or high;
- `f(t)=7t^2(1-4t^2)>=(539/81)t^2` on the low interval;
- the true 17-vector Gram `G=Gram(v,z_1,...,z_16)` is PSD of rank at most five, and its rounded half-integral matrix `Ghat` satisfies `||G-Ghat||_F<1/9` and `M=2Ghat=2I+S` with off-diagonal entries `0,+/-1`;
- `rank_Q(M)<=7` and `rank_F2(M mod 2)<=6`, the latter even because `M mod 2` is alternating.

All statements below are conditional on these inputs. See the preceding [rank-seven proof](tau5_typeE_high_center_rank7_2026-10-28.md).

## 1. Seventeen-vector Welch support count

Consider the seventeen vectors `y_0=v`, `y_i=z_i` for `1<=i<=16`. Their squared norms are `1,1-a_1,...,1-a_16`, so

```
trace(F)=17-x,   sum_i ||y_i||^4 = 17-2x+U_I,
U_I=sum a_i^2 <= x^2.
```

The rank-five frame inequality `trace(F^2)>=(trace F)^2/5` implies

```
Q_17 := sum_{0<=i<j<=16} (y_i.y_j)^2
 >= ((17-x)^2/5 - (17-2x+U_I))/2
 >= 102/5 - (12/5)x - (2/5)x^2
 > L := 318734999/15625000 = 20.399039936.
```

Let `h` count high pairings among the 16 center-isolated pairings and the 120 isolated-isolated pairings. Each high pairing has projected squared correlation at most `1/4`. For a low center-isolated pairing, the two endpoint contacts `t_+,t_-` give

```
(v.z_i)^2 = ((t_+-t_-)/2)^2 <= (t_+^2+t_-^2)/2.
```

For a low isolated-isolated pairing, the four endpoint contacts give, by Walsh/Cauchy,

```
(z_i.z_j)^2 <= (t_++^2+t_+-^2+t_-+^2+t_--^2)/4.
```

All these endpoint contacts are distinct nondeep pairs. With `c=539/81`, their **combined** low squared-correlation mass is therefore bounded by

```
Q_low <= N/(2c) <= 405/68992 = 0.0058702458256...
```

Thus `Q_17<=h/4+405/68992`. But the exact rational gap

```
318734999/15625000 - 81/4 - 405/68992
= 19292115751/134750000000 > 0
```

rules out `h<=81`. Hence

```
BOX: h>=82.
```

Equivalently, the 17-vertex rounded signed support graph has at least **82 of 136** possible edges. If `k_I` is the number of high center-isolated pairings and `e_I` the number of high isolated-isolated pairings, then `e_I+k_I>=82`. In particular, `k_I=10` forces `e_I>=72`, improving the previous uniform `e_I>=71` in that subbranch.

## 2. Seven-by-seven determinant restriction

Let `B` be any principal 7-by-7 block of `Ghat`, and `A` the corresponding PSD rank-at-most-five block of `G`. We have `trace(B)=7` and `||A-B||_F<1/9`. If `p` is the number of positive eigenvalues of `B` and `q=min(p,5)`, then the same inertia-sensitive Hoffman-Wielandt/PSD argument as in the preceding rank-seven note yields

```
|det(2B)|^2 <
R_q := 2^14 * ((7+(7-q)/9)/q)^(2q)
                * (1/(81*(7-q)))^(7-q),  1<=q<=5.
```

The five rational inequalities `R_q<25` hold exactly; the worst case is

```
R_5 = 564668382613504/22876792454961 < 25.
```

If `p=0`, `B` has no positive eigenvalues but trace seven, which is impossible. Consequently `|det(2B)|<5` for every principal 7-block.

The integer matrix `2B` has even diagonal and its reduction modulo two is symmetric zero-diagonal of **odd order seven**, hence alternating and singular. Therefore `det(2B)` is even. If nonzero it must lie in

```
BOX: det(2B) in {-4,-2,+2,+4}.
```

If `rank(Ghat)=7`, symmetry guarantees a nonsingular principal 7-block. Such a block has binary rank **six**, not four or less: an integer 7-by-7 matrix of binary rank at most four has determinant divisible by `2^(7-4)=8` (Smith normal form), inconsistent with its nonzero determinant of absolute value at most four. Since the full support adjacency already has binary rank at most six, we obtain the dichotomy

```
BOX: rank(Ghat)=7  ==>  rank_F2(A_support)=6.
BOX: rank_F2(A_support)<=4  ==>  rank(Ghat)<=6.
```

For a rank-seven star-complement enumeration, only nonsingular 7-vertex bases with determinant `+/-2` or `+/-4` and binary rank six need be retained. This is a finite, exact pruning rule; it does **not** prove PSD of `Ghat`.

## 3. D5 template sanity check (not an inference about Type E)

The exact D5 20-line template has 120 high pairings, with degree 12 at every line. Removing any three lines leaves `120-3*12+e_removed=84+e_removed>=84` high pairings. Thus an actual 17-line D5 subset satisfies the stronger template-specific count 84. Our universal conditional high-center count is **82**, and we do not assume a D5 labeling or uniqueness for arbitrary rounded candidates.

## Proof ledger

**[EXACT, CONDITIONAL]** The support-82 inequality, 7-block determinant restriction, and rank/binary-rank dichotomy follow by exact rational arithmetic from the preceding high-center certificates.

**[OPEN]** Classification of the remaining signed matrices, their nearby rank-five PSD realizability, the low-center Type-E branch, Type C, Type D, generic e>=27, non-isolated branches, and sparse classification without delta(G)>=1.

**[GLOBAL PROVED RANGE — UNCHANGED]** `40<=tau_5<=44`. Retain `M(F3)<=89`, `M(P)>=S/2-28/3`, `A<=383/504`, and the Musin/Boyvalenkov zero-midpoint exclusion. Do not promote conditional Type-E restrictions to a global proof.

Companion exact verifier: [tau5_typeE_high_center_82_support_det4_2026-10-28_verify.py](tau5_typeE_high_center_82_support_det4_2026-10-28_verify.py).
