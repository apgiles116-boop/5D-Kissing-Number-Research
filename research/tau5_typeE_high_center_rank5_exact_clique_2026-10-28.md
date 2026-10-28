# Type E high-center: exact rank-five rounded-Gram reduction (2026-10-28)

**[NEW — EXACT FINITE CERTIFICATE; TYPE-E CONSEQUENCE CONDITIONAL ON UPSTREAM HIGH-CENTER GEOMETRY]**

In the high-center branch `s >= 7`, the rounded Gram matrix `Ghat` of the isolated center and sixteen isolated deep-edge directions has **rank at most five**, improving the earlier conditional rank-six ceiling. This is **not** a proof that `Ghat` is positive semidefinite, a D5 labeling, or an exclusion of Type E.

## 1. Universal integral proximity lemma

**[EXACT FINITE THEOREM]** Let `M` be a real symmetric *integer* matrix of order `n >= 17` with diagonal entries 2 and off-diagonal entries in `{-1,0,1}`. Assume `rank(M) <= 6`. If there exists a PSD matrix `P` of rank at most five with

```
||M-P||_F^2 < 1/16,
```

then **`rank(M) <= 5`**.

The proof is an exhaustive, switching-invariant classification of the possible nonsingular six-vertex principal bases, their single-vertex Schur extensions, and the compatibility graph of two-vertex extensions. It uses only exact integer arithmetic and rational real-root counts; no floating-point eigenvalue decisions.

## 2. Rational spectral screening

Assume instead `rank(M)=6`. Since `M` is symmetric, some principal six-by-six block `B` is nonsingular (the sum of principal minors of order six equals the nonzero product of the six eigenvalues). For each principal block containing `B`, its six nonzero eigenvalues must pass the following **necessary**, deliberately coarse, test:

- every nonzero eigenvalue is strictly greater than `-1/4`;
- at least one nonzero eigenvalue is at most `+1/4`.

Indeed, a negative eigenvalue `<=-1/4` alone has squared distance at least `1/16` from the PSD cone. If all six nonzero eigenvalues exceed `1/4`, their sixth positive eigenvalue alone gives squared distance at least `1/16` from the PSD rank-five cone. Principal-submatrix Frobenius error cannot exceed the global error.

For any integer characteristic polynomial `p` of a real symmetric matrix, remove its factors of `x` to get a degree-six polynomial. The exact number of its real roots strictly greater than rational `a` is the sign-variation count of the nonzero coefficients of `p(x+a)` (Descartes is exact for real-rooted polynomials). Thus the screen is exactly

```
roots_above(p, -1/4) == 6
roots_above(p, +1/4) < 6.
```

This screen admits some blocks whose actual Frobenius distance is too large, making the enumeration conservative.

## 3. Exhaustive six-basis and Schur-extension certificate

The NetworkX graph atlas contains all 156 unlabeled simple graphs on six vertices. On each support, vertex switching makes all spanning-forest signs positive; enumerate every signing of the remaining edges. The resulting integer six-by-six matrices have diagonal 2 and entries 0 or +/-1 elsewhere.

The exact verifier obtains:

| Stage | Count |
|---|---:|
| Six-vertex unsigned atlas graphs | 156 |
| Switching-normalized signed six-bases | 4,562 |
| Nonsingular six-bases passing the rational 1/4 spectral screen | 246 |
| Columns `c in {-1,0,1}^6` satisfying `c^T B^{-1}c=2` | 10,956 |
| Such columns passing the seven-vertex spectral screen | 3,010 |
| Pairs `c,d` with `c^T B^{-1}d in {-1,0,1}` tested at order eight | 27,968 |
| Pairs also passing the eight-vertex spectral screen | 14,404 |

For each basis, form a graph whose vertices are the seven-block-surviving columns. Join two columns precisely when their mutual Schur product is allowed and the corresponding eight-by-eight block passes the rational spectral screen. Any full rank-six `M` of order 17 would give **eleven distinct mutually compatible columns**, hence an eleven-clique in one of these graphs. (Identical or opposite columns cannot represent distinct outside vertices, because their Schur product would be +/-2.)

For 137 of the 246 bases, fewer than eleven columns even survive the seven-block screen. On the remaining 109 bases, exact bitset clique search with a greedy-coloring upper bound gives **maximum clique number 10**, attained by three bases. The other high maxima are four bases with clique number 9. An independent NetworkX maximal-clique calculation agrees for every case with clique number at least 9.

Therefore no eleven-clique exists, contradicting `n-6 >= 11`. This proves the universal lemma and, in particular, excludes rank six for the rounded Type-E matrix.

## 4. Conditional Type-E application

The retained high-center geometry supplies a true PSD rank-five Gram matrix `G=Gram(v,z_1,...,z_16)`, and an integer matrix `M=2Ghat` with

```
||M-2G||_F^2 < 4*(158205281/13475000000)
              = 158205281/3368750000
              < 1/16.
```

The preceding exact atlas certificate had already given `rank(M) <= 6`. Applying the universal lemma yields

```
rank(Ghat) <= 5,
nullity(Ghat) >= 12,
mult_{2Ghat-2I}(-2) >= 12.
```

**[NEW EXACT COROLLARY, CONDITIONAL]** The unsigned support adjacency `A = M mod 2` is alternating over `F_2`. Its rank is even and at most the rational rank of `M`, hence

```
rank_{F_2}(A) <= 4.
```

Because the row space contains at most `2^4=16` binary rows while there are 17 vertices, at least two rows of `A` coincide. Such vertices are **nonadjacent false twins** in the unsigned support graph.

## 5. Proof-status boundaries

**[VERIFIED EXACTLY IN THIS PASS]** All finite enumeration counts, Schur complement equations, rational root tests, and eleven-clique exclusions. The verifier uses `numpy.int64` only for exact small integer matrix products, `sympy` for integer adjugates, and `networkx` for the six-vertex atlas and an independent clique cross-check. No floating-point eigensolver is used.

**[CONDITIONAL]** The Type-E consequence depends on the earlier high-center harmonic resource inequality, contact quantization, and Frobenius rounding estimate. This pass does not independently recertify those upstream geometric claims.

**[OPEN]** Rank at most five does **not** imply PSD. The remaining finite target is to classify the rank-at-most-five half-integral signed matrices, exploiting binary rank at most four and false-twin pairs, and then to address the low-center branch. Types C, D, generic e>=27, non-isolated branches, and sparse graph classification without delta(G)>=1 remain open.

**[GLOBAL PROVED RANGE — UNCHANGED]** `40 <= tau_5 <= 44`. Retain `M(F3)<=89`, `M(P)>=S/2-28/3`, and `A<=383/504`; do not revive older weaker statements.

Companion exact verifier: [tau5_typeE_high_center_rank5_exact_clique_2026-10-28_verify.py](tau5_typeE_high_center_rank5_exact_clique_2026-10-28_verify.py).
