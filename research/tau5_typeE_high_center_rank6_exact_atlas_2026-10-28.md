# Type E high-center: exact finite rank-six reduction (2026-10-28)

**[NEW — EXACT FINITE CERTIFICATE, CONDITIONAL ON THE RETAINED HIGH-CENTER GEOMETRIC INPUTS]** In the high-center branch `s >= 7` of hypothetical Type E, the rounded 17-by-17 half-integral Gram matrix `Ghat` has **rank at most six**, improving the previous rank-seven result. Equivalently, the signed adjacency matrix `S = 2 Ghat - 2 I` has eigenvalue `-2` with multiplicity at least **eleven**. This does not eliminate Type E; the low-center branch is untouched and `Ghat` is not proved PSD.

## 1. Retained inputs and the exact threshold

Use the previously established conditional high-center certificate:

- `G = Gram(v,z_1,...,z_16)` is PSD of rank at most five.
- `M = 2 Ghat` is a symmetric integer 17-by-17 matrix, diagonal 2, off-diagonal in `{-1,0,1}`.
- `||G-Ghat||_F^2 < E = 158205281/13475000000`.
- The preceding determinant/integrality argument gives `rank(M) <= 7` and every nonsingular principal seven-by-seven block has determinant `+/-2` or `+/-4`.

Therefore, for every principal block `B` of `M`, its squared Frobenius distance to the cone of PSD rank-at-most-five matrices is strictly less than

`T = 4 E = 158205281/3368750000 = 0.0469626066048...`.

The proof below is a **finite exact spectral enumeration**, not a numerical eigenvalue assertion.

## 2. Exhaustive seven-vertex signed-basis enumeration

Assume `rank(M)=7`. A real symmetric rank-seven matrix has a nonsingular principal seven-by-seven block `B`. Its determinant is `+/-2` or `+/-4`.

The NetworkX seven-vertex graph atlas contains all 1044 unlabeled simple graphs on seven vertices. On each support, switching vertex signs makes all spanning-forest edges positive. Enumerating signs on the remaining edges gives exactly **197629** normalized signings. Characteristic polynomials are computed with the integer Faddeev–LeVerrier recurrence, not floating-point determinants.

- **13812** signings have determinant `+/-2` or `+/-4`.
- They give **4802** distinct exact integer characteristic polynomials.
- Exact Descartes/Fourier sign-variation counts at `-1/4` and `+1/4` leave **111** polynomials with no eigenvalue below `-1/4` and at least two eigenvalues between those thresholds.
- For these 111, exact rational bisection of their seven real roots to width `1/100000`, followed by rational lower/upper bounds on the squared distance to PSD rank five, leaves **exactly two** characteristic polynomials. No unresolved borderline case remains.

The two polynomials, written in descending powers of `x`, are

```
P_1 = x^7 - 14x^6 + 77x^5 - 210x^4 + 292x^3 - 186x^2 + 37x - 2
P_2 = x^7 - 14x^6 + 76x^5 - 202x^4 + 271x^3 - 166x^2 + 33x - 2.
```

Each has exactly one normalized signing in the enumeration. Their support graphs have respectively seven and eight edges. Exact Sylvester principal-minor tests show that both surviving seven-by-seven blocks are **positive definite**, with determinant 2.

The sign-variation method is exact because characteristic polynomials of real symmetric matrices are real-rooted. For a real-rooted polynomial `p`, the number of roots strictly above a rational `a` is the number of sign changes in the nonzero coefficients of `p(x+a)`; all coefficients are evaluated with integers.

## 3. Exhaustive eighth-vertex obstruction

Let `B` be either surviving positive-definite basis and choose any eighth vertex of the full 17-vertex matrix. Its column to the basis is `c in {-1,0,1}^7`. Since the full matrix has rank seven, its eight-by-eight principal block has zero Schur complement, requiring

`c^T B^{-1} c = 2.`

An exact rational enumeration of all `3^7 = 2187` columns gives **112** admissible columns for each basis. For every one of the 224 possible eight-vertex blocks, exact characteristic-polynomial sign-variation checks establish:

- all seven nonzero eigenvalues are strictly greater than `1/12`;
- at least six nonzero eigenvalues are strictly greater than `21/100`.

Each eight-vertex block is PSD of rank seven, because `B` is positive definite and its Schur complement is zero. Its squared Frobenius distance to PSD matrices of rank at most five is therefore the sum of squares of its two smallest nonzero eigenvalues, strictly greater than

`1/144 + 441/10000 = 2297/45000`.

But the exact rational gap is

`2297/45000 - T = 123756221/30318750000 > 0.`

This contradicts the retained global perturbation bound for **every** possible eighth vertex. Thus no rank-seven full matrix exists:

`BOX: rank(Ghat) <= 6,  nullity(Ghat) >= 11,  mult_S(-2) >= 11.`

## 4. Certification, limitations, and next target

**[VERIFIED EXACTLY]** The companion verifier checks the 1044-graph atlas count, all 197629 switching-normalized signings, 13812 determinant-filtered cases, 4802 exact characteristic polynomials, 111 rational coarse survivors, the two rationally isolated spectral survivors, exact positive definiteness, both 112-column Schur-complement enumerations, and all 224 rational spectral threshold tests. The integer matrix operations use `numpy.int64` within safe small-matrix bounds; no floating-point eigenvalue computation is used.

**[CONDITIONAL]** The theorem depends on the previously retained high-center resource inequality and Frobenius rounding certificate. This verifier does **not** independently establish those upstream geometric inputs.

**[OPEN]** The next target is rank-six signed star-complement classification, with the same 17-vertex support-density and center-degree constraints. For a nonsingular principal six-block, the rank-five PSD perturbation bound gives `|det(2 Ghat_B)|<19`. A binary-rank-six block has odd determinant, hence its determinant is among the odd integers of absolute value at most 17. No rank-six exclusion is claimed. The low-center Type-E branch, Types C and D, generic `e>=27`, and non-isolated branches remain open.

**[GLOBAL PROVED RANGE — UNCHANGED]** `40 <= tau_5 <= 44`. Retain `M(F3)<=89`, `M(P)>=S/2-28/3`, `A<=383/504`, and the Musin/Boyvalenkov zero-midpoint boundary exclusion.

Companion verifier: [tau5_typeE_high_center_rank6_exact_atlas_2026-10-28_verify.py](tau5_typeE_high_center_rank6_exact_atlas_2026-10-28_verify.py).
