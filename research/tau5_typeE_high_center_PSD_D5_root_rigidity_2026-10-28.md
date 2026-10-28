# Type E high-center: exact PSD rigidity and justified D5 labeling of the rounded 17 lines (2026-10-28)

**[NEW — EXACT FINITE CERTIFICATE; TYPE-E CONSEQUENCE CONDITIONAL ON THE RETAINED HIGH-CENTER GEOMETRIC INPUTS]**

The preceding exact atlas theorem proves `rank(M)<=5` for the rounded integer Gram `M=2Ghat` of the isolated center and sixteen isolated selected-edge directions. A second, independent **small-rank integral star-complement classification** now proves that **every symmetric integer matrix of order at least 13, diagonal 2 and off-diagonal 0 or +/-1, with rank at most five is necessarily PSD of rank five**.

Consequently the high-center rounded `Ghat` is not merely rank five: it is **PSD and is the Gram of seventeen distinct lines from the D5 root system**. This is a classification of the *rounded* matrix, not of the true 17-vector Gram, and does not assert uniqueness of an arbitrary optimal (5,20) projective packing.

## 1. Exact universal small-rank rigidity lemma

Let `M` be symmetric integral with diagonal 2 and all off-diagonal entries in `{-1,0,1}`. Suppose `rank(M)=r`. There is a nonsingular principal `r x r` block `B`. Write

```
M = [ B  C ; C^T  D ].
```

Rank `r` forces `D=C^T B^{-1} C`. Every outside column `c` belongs to `{-1,0,1}^r`, satisfies `c^T B^{-1}c=2`, and every two distinct columns `c,d` must have `c^T B^{-1}d in {-1,0,1}`. Identical or opposite columns cannot be used twice: they would have mutual inner product +/-2.

Enumerate all unlabeled support graphs on `r` vertices and all switching-normalized signs, as in the preceding rank-five note. Form the exact compatibility graph of admissible outside columns; its maximum clique number bounds `n-r`.

**[VERIFIED EXACTLY]** The companion integer/rational verifier obtains:

| Rank `r` | Atlas supports | Signed representatives | Eligible nonsingular bases | Maximum compatible outside clique | Maximum total order |
|---|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 | 1 |
| 2 | 2 | 2 | 2 | 1 | 3 |
| 3 | 4 | 5 | 4 | 3 | 6 |
| 4 | 11 | 24 | 20 | 8 | 12 |
| 5, **indefinite only** | 34 | 220 | 164 | 5 | 10 |

For the rank-five row, retain only nonsingular bases with at least one negative eigenvalue. Their inertia is decided exactly by the sign variations of the real-rooted integer characteristic polynomial at zero. Any rank-five indefinite full matrix has a nonsingular principal five-block of the **same inertia**, by the zero Schur complement and Sylvester's law of inertia. Thus it is covered by this row.

The maximum-clique results were independently checked with NetworkX maximal-clique enumeration for the largest cases. No floating-point eigenvalue tests are used.

Therefore a matrix of order `n>=13` with these entries and rank at most five cannot have rank 1,2,3,4 (all allow at most twelve vertices), and cannot have rank five with a negative eigenvalue (at most ten vertices). Hence it is **PSD of rank exactly five**.

## 2. Conditional high-center consequence: D5 root subsystem

The previous exact clique certificate supplies `rank(M)<=5` for the high-center rounded 17-by-17 matrix. The universal lemma gives

```
M = 2Ghat >= 0,       rank(M)=5.
```

Choose vectors `r_0,...,r_16` with Gram `M`. Each has squared norm 2, and distinct nonopposite roots have integral mutual inner products 0,+/-1. The lattice they span is positive definite and integral, hence discrete. Reflection in any root preserves the lattice and root length. The finite reflection closure is a reduced, crystallographic, **simply-laced** root system of rank five.

By the standard ADE classification (e.g. Humphreys or Bourbaki), the rank-five irreducible possibilities are `A5` (15 projective root lines) and `D5` (20); reducible systems of rank five have at most 13 projective root lines (the largest is `D4+A1`). Seventeen distinct root lines therefore force **type D5**. After a common orthogonal transformation and individual sign switches, the rounded unit vectors are **17 of the 20** standard D5 lines

```
z_ij^+/- = (e_i +/- e_j)/sqrt(2),   1 <= i < j <= 5.
```

This is a justified D5 labeling of the *rounded high-center subsystem only*. It does not invoke the conjectural uniqueness of optimal projective packings or identify the six exceptional F3 pairings with the six Q-Gram null directions.

## 3. Exact D5 support and frame consequences

Every line in the full D5 20-line system has exactly **12** other lines with absolute inner product `1/2`, and 7 orthogonal lines. The full nonorthogonality graph has 120 edges. The rounded 17-line subsystem is obtained by deleting exactly three D5 lines. If `e_miss` is the number of nonorthogonality edges among the three deleted lines, then

```
e_17 = 120 - 3*12 + e_miss = 84 + e_miss,
0 <= e_miss <= 3.
```

Thus the rounded 17-vertex graph has **at least 84 high edges** (improving the earlier 82). Its center degree `k_I` is between 9 and 12; combined with the retained high-center geometric restriction `10<=k_I<=14`, this gives

```
k_I in {10,11,12}.
```

Among the sixteen isolated-edge rounded directions alone, the number of high pairings is

```
e_I = 84 + e_miss - k_I >= 84-k_I.
```

In particular `e_I>=74` if `k_I=10`, `e_I>=73` if `k_I=11`, and `e_I>=72` if `k_I=12`.

The full 20-line D5 unit-vector frame obeys `sum_20 rr^T = 4 I_5`. Removing three unit lines yields the stronger exact frame bound

```
F_17 = sum_17 rr^T = 4 I_5 - sum_3 rr^T >= 2 I_5.
```

The three removed unit roots have mutual absolute correlations at most 1/2. Their 3-by-3 Gram has diagonal 1 and off-diagonal absolute values at most 1/2, so Gershgorin gives its largest eigenvalue at most 2. The nonzero eigenvalues of their frame operator agree with those of this Gram. Therefore the five nonzero eigenvalues of the **rounded** 17-by-17 Gram `Ghat` are all at least **2**. This bound is sharp when the three removed lines form a positively signed triangle. The stronger gap supplies a quantitative kernel-perturbation input.

## 4. Proof-status boundaries and next step

**[PROVED EXACTLY AS FINITE/ROOT-SYSTEM MATHEMATICS]** The universal PSD rigidity lemma, small-rank clique counts, and D5 support/frame conclusions.

**[CONDITIONAL]** Their application to Type E assumes the retained high-center harmonic resource, contact quantization, Frobenius rounding, and preceding rank-five reduction. The current pass does not independently rederive those upstream geometric certificates.

**[OPEN]** The **true** vectors `v,z_1,...,z_16` are only close to a D5-labeled rounded frame. They are not proved equal to D5 roots, and no 21-line Type-E contradiction has yet been derived. The next priority is to use the rounded frame's eigenvalue gap `>=1` and its exact integer nullspace to quantify the perturbation of the true Gram and feed the 184-safe/homogeneous-defect inequalities. The low-center Type E, Types C and D, generic `e>=27`, and non-isolated branches remain open.

**[GLOBAL PROVED RANGE — UNCHANGED]** `40 <= tau_5 <= 44`. Retain `M(F3)<=89`, `M(P)>=S/2-28/3`, `A<=383/504`; do not regress to weaker historical claims.

Companion exact verifier: [tau5_typeE_high_center_PSD_D5_root_rigidity_2026-10-28_verify.py](tau5_typeE_high_center_PSD_D5_root_rigidity_2026-10-28_verify.py).
