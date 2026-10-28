# Type E high-center: exact D5 Q-kernel classification and quantitative Gram-kernel stability (2026-10-28)

**[NEW — EXACT ALGEBRA; TYPE-E CONSEQUENCES CONDITIONAL ON THE PRECEDING HIGH-CENTER CERTIFICATES]**

The rounded isolated-center-plus-sixteen-direction Gram has now been classified as a 17-line subset of D5, *without* assuming uniqueness of an optimal projective packing. This note determines **all** traceless-tensor Q-relations for such a subset and derives an exact operator-gap estimate controlling the true versus rounded 17-vector Gram kernels.

## 1. D5 support decomposition of Q

Use the unit D5 root lines

```
r_ij^+/- = (e_i +/- e_j)/sqrt(2), 1 <= i < j <= 5,
Q(r) = rr^T - I_5/5.
```

Define the traceless diagonal support sum `S_ij=E_ii+E_jj-(2/5)I_5` and off-diagonal basis tensor `O_ij=E_ij+E_ji`. Direct expansion gives the **exact identities**

```
Q(r_ij^+) + Q(r_ij^-) = S_ij,
Q(r_ij^+) - Q(r_ij^-) = O_ij.
```

The ten `O_ij` are linearly independent and orthogonal to the four-dimensional traceless diagonal subspace. For any set of retained root lines, the coefficient of a singly retained support must vanish in every Q-kernel relation, because its off-diagonal `O_ij` coordinate occurs nowhere else. For a doubly retained support, the two Q-coefficients must be equal, leaving a relation among its `S_ij` tensors.

Let `F` be the graph on coordinate vertices `{1,...,5}` consisting of supports `ij` for which **both** root lines are retained. The remaining Q-kernel relations correspond exactly to edge weights `c_ij` on `F` satisfying

```
sum_{j:ij in F} c_ij = (2/5) sum_{ab in F} c_ab
    for every coordinate vertex i.
```

Equivalently, the five weighted vertex degrees are all equal.

## 2. Classification of the 17-line Q-rank

Exactly three of the twenty D5 lines are absent. There are only two possibilities.

**Case I: three absent lines on three distinct supports.** Seven supports remain double, three remain single, and none are empty. The double-support graph `F` is `K5` with three edges removed: it has seven edges, is connected (disconnecting K5 needs at least four deletions), and is nonbipartite (a bipartite graph on five vertices has at most six edges). Its `S_ij` span the full four-dimensional traceless diagonal space. The ten off-diagonal coordinates are all present. Thus

```
rank(Q_17) = 10+4 = 14,   nullity(Q_17)=17-14=3.
```

**Case II: both lines of one support and one line of another support are absent.** Eight supports remain double, one remains single, and one is empty. The double-support graph `F` is `K5` with two edges removed, hence connected and nonbipartite. Its `S_ij` span four dimensions, and nine independent off-diagonal coordinates remain. Thus

```
rank(Q_17) = 9+4 = 13,   nullity(Q_17)=17-13=4.
```

The kernel dimensions and descriptions are **exact**, not numerical. An independent modular-rank enumeration over all `C(20,3)=1140` omitted triples confirms **960** subsets of Q-rank 14 and **180** of Q-rank 13. The 180 special triples are precisely the ten choices of a fully omitted support times eighteen choices of the third omitted line.

These are relations for the **rounded D5 Q-vectors**, not yet relations for the true Type-E `z_i`.

## 3. Sharp rounded-frame gap and true Gram-kernel stability

The full D5 20-line unit-vector frame satisfies `sum_20 rr^T=4I_5`. Let `H=Ghat` be the Gram of any 17 retained lines, and let `T` be the three omitted unit roots. Since their mutual absolute correlations are at most `1/2`, their 3-by-3 Gram has largest eigenvalue at most 2 by Gershgorin. Therefore

```
F_17 = 4I_5 - sum_{r in T} rr^T >= 2I_5.
```

The five nonzero eigenvalues of `H` equal those of `F_17`, hence are all **at least 2**. The constant is sharp for a positively signed triangle of omitted roots.

Let `G=Gram(v,z_1,...,z_16)` be the true high-center Gram. The retained rounding certificate gives

```
||G-H||_op <= ||G-H||_F < 1/9.
```

Weyl's inequality then gives `lambda_5(G)>2-1/9=17/9`. Since the true vectors lie in R5, **rank(G)=5**. Write `P_G` and `P_H` for the orthogonal projections onto their respective five-dimensional column spaces. For any `w in ker(H)`,

```
||P_G w|| <= ||G w||/lambda_5(G) < (1/17)||w||.
```

For any `u in ker(G)`,

```
||P_H u|| <= ||H u||/lambda_5(H) < (1/18)||u||.
```

Thus the twelve-dimensional true and rounded Gram nullspaces are quantitatively close, with **exact rational constants 1/17 and 1/18**. This supplies a concrete second-order stability framework for transporting the rounded D5 support/Q relations into the Type-E midpoint and safe-pair inequalities.

## 4. Proof status and next task

**[PROVED EXACTLY]** D5 Q-support decomposition, 17-line Q-rank 13/14 dichotomy, 960/180 subset counts, sharp rounded-frame gap `>=2`, and the conditional Gram-kernel perturbation bounds.

**[CONDITIONAL]** The D5 identification and `||G-H||_F<1/9` depend on the earlier Type-E high-center mass/harmonic and rounding certificates. The present Q relations apply exactly to the rounded root frame only.

**[OPEN]** A second-order *lower* bound on the actual midpoint energy has not yet been obtained. Next: choose an exact integer basis of the 3- or 4-dimensional rounded Q-kernel, quantify its perturbation for the true `Q(z_i)`, and couple those residuals to the 184-safe Walsh blocks and six exceptional F3 pairings. The low-center branch, Types C and D, generic e>=27, and non-isolated cases remain unresolved.

**[GLOBAL PROVED RANGE — UNCHANGED]** `40 <= tau_5 <= 44`. Retain `M(F3)<=89`, `M(P)>=S/2-28/3`, and `A<=383/504`.

Companion verifier: [tau5_typeE_high_center_D5_Qkernels_2026-10-28_verify.py](tau5_typeE_high_center_D5_Qkernels_2026-10-28_verify.py).
