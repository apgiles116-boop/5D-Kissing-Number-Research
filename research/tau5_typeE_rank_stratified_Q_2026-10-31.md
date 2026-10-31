# Type E: rank-stratified Q completion and midpoint-independent D5 separation

Date: 2026-10-31. **Proof ledger: global proved range 40 <= tau_5 <= 44; Type E remains OPEN.**

## Theorem A — safe-data reconstruction by isolated Q-rank

**[PROVED EXACTLY — universal linear algebra, Type-E partition]**

For the sixteen isolated Type-E half-difference vectors and four F3 core half-difference vectors, set
`Q_i=z_i z_i^T-(||z_i||^2/5)I` in the 14-dimensional real inner-product space `Sym_0(5)`. The 16-by-16 isolated Q-Gram and the 16-by-4 isolated-core Q-Gram use only safe pairings. Write `r=rank(Q_i:i isolated)`. Choose `r` independent isolated Q columns as a matrix `B`, put `G=B^T B`, `Y=B^T F_C`, where `F_C` has the four core Q columns.

Then the exact orthogonal projection identity is

`K_CC=Y^T G^{-1}Y+R,`
`R=F_C^T(I-BG^{-1}B^T)F_C >= 0,` `rank R <= 14-r.` (1)

All entries of `G,Y` are safe. Each core diagonal is known: `(K_CC)_{jj}=4 w_j^2/5` with `w_j=||z_j||^2=1-a_j`. Therefore

`rho_j=4w_j^2/5-y_j^T G^{-1}y_j >=0` (2)

is safe-only, and multiplication by `det G` gives the polynomial safe-only inequality

`(4/5)w_j^2 det G-y_j^T adj(G)y_j >=0.` (3)

If `r=14`, `R=0` and all six exceptional squared core correlations are uniquely reconstructed from safe data.

If `r=13`, `R=tt^T` with `t_j^2=rho_j`. Thus, for each core pair `j<k`,

`(z_j.z_k)^2=w_j w_k/5+y_j^T G^{-1}y_k+sigma_j sigma_k sqrt(rho_j rho_k).` (4)

There are **at most eight coherent sign patterns**, because simultaneous reversal of all four signs does not change the Gram matrix. The six off-diagonal residuals cannot choose their signs independently. Polynomially, `R_jk^2=rho_j rho_k` and `R_ij R_jk R_ki=rho_i rho_j rho_k` for every distinct triple. If some `rho_j=0`, there are fewer distinct completions. The eight patterns have not been tested against the Type-E endpoint constraints and are not claimed feasible.

If `r=12`, `R` is PSD of rank at most two, so its four principal 3-by-3 determinants vanish. If `r=11`, `det R=0`. For `r<=10`, the residual rank cap alone imposes no extra four-by-four rank restriction.

## Theorem B — safe-only polynomial rank detector

**[PROVED EXACTLY]** For the PSD isolated Gram matrix `K_II`, define `e_k(K_II)=sum_{|B|=k} det((K_II)_{BB})`. Every summand is nonnegative. Its rank is exactly the largest `k` with `e_k>0`. In particular, `e_14>0` is the full-rank branch; `e_14=0,e_13>0` is rank thirteen. No D5 labeling is needed to form these polynomials.

For the exact sixteen D5 reference lines (delete four positive star roots), the rational characteristic polynomial is

`lambda^2 (lambda-1)^6 (4lambda^2-7lambda+2)^3 (20lambda^2-31lambda+6)/1280`.

Consequently **`e_14=3/80`** at D5. This is a reference value, not a Type-E lower bound.

## Theorem C — sharp spectral rank-obstruction for a common D5 comparison

**[PROVED EXACTLY — conditional only on a specified common D5 labeling/rotation]**

For the normalized isolated projected lines `u_i=z_i/sqrt(1-a_i)`, let `P_i=u_i u_i^T` and `E2=sum_{i isolated} ||P_i-P_i^D5||_F^2` for *any* common D5 labeling and rotation. Since `1-a_i>=3/4>0`, scaling Q columns does not change rank. The normalized Q synthesis `F` has rank `r` and satisfies `||F-F_D5||_F^2=E2` exactly.

The nonzero D5 Q-Gram eigenvalues, in increasing order, begin with `lambda_1=(31-sqrt(481))/40`, then three copies of `lambda_2=(7-sqrt(17))/8`, then six copies of 1. Eckart–Young–Mirsky gives

`E2 >= sum of the smallest (14-r) positive D5 Q-Gram eigenvalues.` (5)

In particular:

| Isolated Q-rank | Necessary E2 |
|---|---|
| <=13 | >= (31-sqrt(481))/40 = 0.2267071950... |
| <=12 | >= (31-sqrt(481))/40+(7-sqrt(17))/8 = 0.5863189918... |
| <=11 | >= (31-sqrt(481))/40+2(7-sqrt(17))/8 = 0.9459307886... |
| <=10 | >= (31-sqrt(481))/40+3(7-sqrt(17))/8 = 1.3055425854... |

These thresholds need **no midpoint cap** and improve the earlier conditional rank-deficiency separation `E2>0.2249872`. They are sharp for unrestricted matrix low-rank approximation, but are not claimed sharp within realizable rank-one projectors. They do not assert that arbitrary Type E is D5-close.

## Verification and next step

**[VERIFIED LOCALLY — exact SymPy]** The D5 Q-Gram characteristic polynomial, rank 14, `e_14=3/80`, and all spectral thresholds were checked with exact arithmetic. Synthetic rational 14-dimensional Gram examples verified the rank-13 residual decomposition, six pair-square equations, four triple sign equations, eight distinct completions, and rank-12 residual minors. Synthetic examples test algebra, not Type-E feasibility.

**[OPEN]** Split the finite Type-E problem using safe-only `e_14,e_13`. On rank 14 substitute the unique core reconstruction into the six F3 endpoint contacts. On rank 13 test the eight coherent signs with the full signed four-core midpoint Gram PSD and the retained defect cap. On ranks 12 and 11 add the residual-minor equations. The 184 safe Walsh constraints must be enforced with the same labeling. No contradiction or new upper bound on safe squared-correlation energy has yet been established.

Retain the exact broom `M(F3)<=89`, matching `M(P)>=S/2-28/3`, 20-edge mass `>=2137/6`, midpoint energy `A<=383/504`, Musin/Boyvalenkov zero-midpoint exclusion, and the minimum-degree qualification `delta(G)>=1` for sparse graph classification. **Global proved range remains 40 <= tau_5 <= 44.**
