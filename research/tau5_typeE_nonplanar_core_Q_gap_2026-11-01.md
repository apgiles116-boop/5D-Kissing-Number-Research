# Type E: noncoplanar four-core Q gap and stronger coplanar tomography (2026-11-01)

**[PROVED EXACTLY — standalone tensor lemmas; Type-E applications conditional on retained inputs.]** No Type-E elimination. Global proved range **40 <= tau_5 <= 44**.

## 1. Noncoplanar core Q spectral gap

Let the four projected core vectors satisfy `t_i=||z_i||²=1-a_i>=3/4`, and retain the six-core raw defect ceiling
`D_C=sum_{i<j}(|z_i.z_j|-1/2)_+ <= D*=1780062775/4032758016`.
Write `Q_i=z_i z_i^T-(t_i/5)I_5` and `K_C=(<Q_i,Q_j>_F)`.

**[EXACT, CONDITIONAL ON D*]** `lambda_3(K_C)>1/2500`, with eigenvalues decreasingly ordered, **without core coplanarity**. In particular `rank(K_C)>=3`. This improves the earlier coplanar-only `7/100000` threshold by a factor `40/7`, but does not imply rank exactly three.

**Proof: close pairs.** Set `delta=5/18` and let `theta_ij` be projective angles. If `theta_ij<=delta`, then `|z_i.z_j|>=3 cos(delta)/4`. Two such pairs force
`D_C >= (3/2)(1-delta²/2)-1=191/432>D*`.
The exact margin is `2939033/4032758016>0`. Hence at most one pair is close; at least two of the four triples have all three angles `>delta`.

**Proof: quantitative three-projector independence.** For three unit vectors `u_i` with pairwise projective angles `>=delta`, set `P_i=u_i u_i^T` and `s=sin(delta)`. For each `i`, with other indices `j,k`, choose unit covectors `ell_j,ell_k` orthogonal to `u_j,u_k` and satisfying `ell_j.u_i=sin(theta_ij)`, `ell_k.u_i=sin(theta_ik)`. Then
`F_i=sym(ell_j tensor ell_k)/(sin(theta_ij)sin(theta_ik))`
obeys `<F_i,P_h>=delta_ih` and `||F_i||_F<=1/s²`. The dual operator has norm at most `sqrt(3)/s²`, so
`||sum beta_i P_i||_F >= (s²/sqrt(3))||beta||_2`.

For weighted `z_i=sqrt(t_i)u_i`, `t_i>=3/4`, put `X=sum alpha_i z_i z_i^T`. Since `rank(X)<=3`, `(tr X)²<=3||X||_F²`. Therefore
`||X-(tr X/5)I_5||_F² >= (2/5)||X||_F² >= (3/40)s^4||alpha||²`.
Thus the traceless-projector Q-Gram of any separated triple has smallest eigenvalue at least `(3/40)sin(delta)^4`.

**Exact threshold.** `sin(5/18)>5/18-(5/18)^3/6=9595/34992`, and
`(3/40)(9595/34992)^4-1/2500=59970773847862061/2498755783880540160000>0`.
Principal-submatrix interlacing gives `lambda_3(K_C)>=lambda_3(K_T)>1/2500`. QED.

## 2. Improved coplanar safe tomography

**[EXACT, ADDITIONALLY CONDITIONAL]** Assume the four core directions span a plane `W`, and retain the separately proved `S_I=sum_{i=1}^{16}z_i z_i^T>(73/200)I_5` and harmonic midpoint cap `A<569/1000`. Let `D_ic=(z_i.z_c)²` be the fully safe 16-by-4 squared-correlation matrix.

Factor `D=BC` through `Sym²(W)` in Frobenius-orthonormal coordinates. The sharp planar quadratic-lift theorem gives `sigma_2(B)²>=(73/200)²/16`. The five-dimensional traceless metric on `Sym²(W)` is `M=diag(3/5,1,1)<=I`, so `K_C=C^TMC` and the rank-three Q-gap implies `CC^T>(1/2500)I_3`. Hence

**`sigma_2(D)>73/40000=0.001825`.**

Also `sum_c||z_c||²=4-A_C>343/100`, so `sum_ic D_ic> (73/200)(343/100)`, giving `sigma_1(D)>25039/160000`. Cauchy-Binet yields

**`sum_{i<j,c<d}(D_ic D_jd-D_id D_jc)²>3341024655409/40960000000000000000 ≈ 8.1567984751e-8`.**

The new squared-minor floor is `40/7` times the previous label-free coplanar result. **The Q-gap itself is noncoplanar; the tomography transfer still requires coplanarity.**

## 3. Bonus: sharp quadratic-lift theorem in every dimension

**[PROVED EXACTLY — standalone]** For any `d>=2` and `w_1,...,w_n in R^d` with `sum_i w_iw_i^T >= c I_d`, their symmetric quadratic-lift matrix satisfies `sigma_2(B)²>=c²/n`. The constant is sharp uniformly in dimension, attained in dimension two by equally spaced projective directions.

**Proof.** A top eigenmatrix `X` of the quadratic-lift operator can be chosen PSD: replacing `X` by `|X|` preserves Frobenius norm and weakly increases each `|w_i^TXw_i|`. Diagonalize `X`; choose two coordinate axes `p,q`. Write `A_i=w_ip²`, `B_i=w_iq²`, `a=sum A_i²`, `b=sum B_i²`, `h=sum A_i B_i`, and `t=c²/n`. Then `a,b>=t` and covariance Cauchy gives `h>=t-sqrt((a-t)(b-t))`. If `h>=t/2`, the unit off-diagonal matrix on `p,q` is orthogonal to `X` and has Rayleigh quotient `2h>=t`. Otherwise `(a-t)(b-t)>h²`, so the diagonal-sector Gram `[[a,h],[h,b]]>=tI_2`; choose a unit diagonal matrix on `p,q` orthogonal to `X`. Its Rayleigh quotient is at least `t`. Courant-Fischer gives `lambda_2(B^TB)>=t`. QED.

This dimension-free lift theorem **alone does not prove noncoplanar tomography**: the core tensor span need not align with the well-conditioned isolated quadratic-lift directions.

## Status

**[VERIFIED EXACT ARITHMETIC]** Companion rational verifier checks the close-pair contradiction, Taylor/eigenvalue margin, and tomography fractions. The analytic arguments, not a numerical search, establish the lemmas.

**[OPEN]** Need an F3-incidence-sensitive *upper* bound incompatible with the safe-minor floor, or a noncoplanar alignment theorem. Type E, C, D, generic e>=27, and non-isolated branches remain open. Sparse e=23/e=24 classification requires delta(G)>=1. Retain star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504 and the stronger conditional harmonic cap, and the Musin/Boyvalenkov 21-line boundary exclusion. **Global range unchanged: 40<=tau_5<=44.**
