# Type E: explicit isolated-center spectral gap for the D5 Q-Gram

23 October 2026. **PROVED (exact algebra) under the retained isolated-center Type-E endpoint and midpoint-energy hypotheses.** This is a necessary separation theorem, not an exclusion of Type E or a proof of a D5 labeling. The global range remains `40 <= tau_5 <= 44`.

## Theorem

For twenty selected deep-edge pairs `x_i^+ = m_i+z_i`, `x_i^- = m_i-z_i` in `R^5`, assume the retained Type-E facts:

* `a_i=||m_i||^2` satisfies `0 <= a_i <= 1/4` and `A=sum a_i <= B=383/504`;
* `||z_i||^2=1-a_i`;
* there is an isolated unit center `u` with `|u.z_i| <= 1/2` for all twenty indices.

Set `Q_i=z_i z_i^T-(1-a_i)I/5` and `G=(tr(Q_i Q_j))_{i,j=1}^{20}`. Let `G0` be the twenty-line D5 Q-Gram matrix, in **any fixed permutation of its twenty indices**. Then

    BOXED: ||G-G0||_op > 2/7,
    hence ||G-G0||_F > 2/7.

A slightly sharper exact threshold is

    ||G-G0||_op >= [(-30+sqrt(900+160*(30-3B)))/80]^2
                     = (-3/8+sqrt(588210)/840)^2
                     = 0.289480506914... .

The weak `>=` at the algebraic root is rigorous. The clean `>2/7` bound is strict. The bound holds for every permutation of the D5 template, without assuming an actual D5 labeling exists.

## Proof

Write `d=||G-G0||_op`. If `d>=1`, the conclusion is immediate, so assume `d<1`.

**(1) D5 feature spectrum.** Exact rational arithmetic gives the spectrum of `G0`:

    3/2 (multiplicity 4), 1 (multiplicity 10), 0 (multiplicity 6),
    G0*1=0.

Each `Q_i` lies in the fourteen-dimensional real Hilbert space `Sym_0(5)`. The nonzero eigenvalues of its 20-by-20 Gram matrix `G` coincide with the eigenvalues of its 14-by-14 frame operator `T=sum_i |Q_i><Q_i|`. Since `rank(G)<=14`, Weyl's inequality and `d<1` imply `T >= (1-d) I_14`.

**(2) Lower bound on the center's traceless fourth moment.** Set `v=uu^T-I/5`, so `||v||_F^2=4/5`, and put

    q_i=(u.z_i)^2 <=1/4,
    b_i=tr(Q_i v)=q_i-(1-a_i)/5.

The frame bound gives

    sum_i b_i^2 >= (4/5)(1-d).                                      (L)

**(3) Upper bound using the isolated-center band.** Since `q_i^2<=q_i/4`, `a_i>=0`, and `a_i<=1/4`,

    sum_i b_i^2
      <= 4/5-(3/20)sum_i q_i + A/50 + (1/25)sum_i a_i^2.           (U1)

Moreover `G0*1=0`, so

    ||sum_i Q_i||_F^2 = 1^T G 1 = 1^T(G-G0)1 <=20d.

Cauchy-Schwarz against `v` yields

    |sum_i q_i - (20-A)/5| = |tr(v sum_i Q_i)| <=4 sqrt(d),
    sum_i q_i >= 4-A/5-4 sqrt(d).                                  (U2)

Substitute (U2) in (U1), then use `sum_i a_i^2<=A/4` and `A<=B`:

    sum_i b_i^2 <= 1/5 + (3B)/50 + (3/5)sqrt(d).                   (U)

**(4) Explicit contradiction at `d<=2/7`.** Comparing (L) and (U) forces

    40d + 30sqrt(d) >= 30-3B = 4657/168.                          (*)

But at `d=2/7` the left side is strictly smaller, as the rational square comparison shows:

    (4657/168-80/7)^2 - 900*(2/7) = 33367/4032 >0,
    4657/168-80/7 >0.

The left side of (*) is increasing for `d>=0`, so `d>2/7`. Solving (*) as a quadratic in `sqrt(d)` gives the stated sharper algebraic threshold. QED.

## Scope and next step

**[PROVED EXACTLY, CONDITIONAL TYPE-E APPLICATION]** This supplies an explicit *20-by-20 Q-Gram* separation constant, improving the previous compactness-only positive gap. It uses no physical O(5) reconstruction theorem and is valid for any D5 index permutation.

**[OPEN]** Type-E elimination: the six-exception and homogeneous-defect bounds have not yet been converted into an upper bound on `||G-G0||_op` below `2/7`. Such a conversion would require a justified global D5 labeling and quantitative control of the remaining 184 entries, or a new label-free certificate.

**[RETAINED]** `M(F3)<=89`, selected matching mass `>=S/2-28/3`, `A<=383/504`; C, D, generic `e>=27`, and non-isolated branches remain open. Sparse `e=23/24` classification still assumes `delta(G)>=1`.

Verifier: `tau5_typeE_explicit_QGram_center_gap_2026-10-23_verify.py` (SymPy exact rational spectrum and squared comparison).


## Exact six-exception tradeoff (conditional on a chosen D5 labeling)

If `G-G0=R+E` and `E` has nonzero entries only on the six off-diagonal core-core pairs among four indices, put `eta=max_core |E_ij|`. Every row of the symmetric `E` has absolute row sum at most `3 eta`, hence `||E||_op<=3 eta`. The theorem therefore implies

    BOXED: ||R||_op + 3 eta > 2/7.

For example, if `||R||_op<=1/7`, then `eta>1/21`. This is a necessary safe-versus-exceptional perturbation tradeoff, not a bound on `R` from the retained scalar positive-defect estimate; establishing such a bound remains open.
