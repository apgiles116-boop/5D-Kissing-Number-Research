# Sharp quadratic-lift theorem and improved label-free Type-E tomography (2026-11-01)

**Proof status:** [PROVED EXACTLY — standalone linear algebra]; [PROVED EXACTLY, CONDITIONAL on retained Type-E isolated-frame/core-Q certificates and core coplanarity]. **Type E remains OPEN; global proved range 40 <= tau_5 <= 44.**

## Sharp universal theorem

Let (w_1,\ldots,w_n\in\mathbb R^2), (n\ge2), satisfy (S=\sum_iw_iw_i^T\succeq cI_2), (c>0). Let (B) be the (n\times3) matrix of Frobenius-orthonormal coordinates of (w_iw_i^T). Then

[
\boxed{\sigma_2(B)^2\ge c^2/n.}\tag{1}
]

This improves the previous (c^2/(4n)) lemma by a factor four. The coefficient is sharp for every (n\ge3): choose projective angles (\theta_i=i\pi/n), all vectors of squared length (2c/n). Then (S=cI_2) and the squared singular values of (B) are (2c^2/n,c^2/n,c^2/n).

### Exact analytic proof

The positive operator (T(X)=\sum_i\langle w_iw_i^T,X\rangle_Fw_iw_i^T) has matrix (B^TB). Its top eigenvalue has a positive semidefinite unit eigenmatrix (X): replacing any top eigenmatrix by its spectral absolute value preserves Frobenius norm and weakly increases each (|w_i^TXw_i|). Diagonalize (X), and write (w_i=(x_i,y_i)), (A_i=x_i^2), (B_i=y_i^2), (a=\sum A_i^2), (b=\sum B_i^2), (d=\sum A_iB_i), (t=c^2/n). Since (S\succeq cI), (\sum A_i,\sum B_i\ge c) and (a,b\ge t). Covariance Cauchy–Schwarz yields

[
d\ge\frac{(\sum A_i)(\sum B_i)}n-
\sqrt{\left(a-\frac{(\sum A_i)^2}n\right)
\left(b-\frac{(\sum B_i)^2}n\right)}
\ge t-\sqrt{(a-t)(b-t)}.\tag{2}
]

If (d\ge t/2), the unit off-diagonal symmetric matrix (Z=(e_1e_2^T+e_2e_1^T)/\sqrt2), orthogonal to (X), has Rayleigh quotient (\sum(w_i^TZw_i)^2=2d\ge t). If (d<t/2), (2) gives (\sqrt{(a-t)(b-t)}>d), so the diagonal-sector Gram matrix (\begin{pmatrix}a&d\\d&b\end{pmatrix}\succeq tI_2). The unit diagonal symmetric matrix orthogonal to (X) then has Rayleigh quotient at least (t). In either case Courant–Fischer gives (\lambda_2(B^TB)\ge t). QED.

## Type-E application [CONDITIONAL]

Assume the four selected F3 projected core vectors span a plane (W). Retain (\lambda_{\min}(S_I)>c=73/200) for the 16 isolated projected vectors and (\lambda_3(K_C)>\epsilon=7/100000) for the coplanar four-core traceless-Q Gram. These are upstream certificates, not re-proved here.

With (w_i=P_Wz_i), let (B) be the 2D quadratic-lift matrix, and let (C) be the (3\times4) matrix of the core tensors (z_cz_c^T). The fully safe (16\times4) squared-correlation matrix is (D=BC), (D_{ic}=(z_i\cdot z_c)^2). The five-dimensional traceless projection has metric (M=\operatorname{diag}(3/5,1,1)\preceq I) on (\operatorname{Sym}^2(W)); hence (K_C=C^TMC), and the core certificate gives (CC^T>\epsilon I_3). By (1),

[
\boxed{\sigma_2(D)^2>\epsilon c^2/16
=\frac{37303}{64000000000},\quad
\sigma_2(D)>\frac{73}{800}\sqrt{\frac7{100000}}
\approx0.0007634522742>\frac3{4000}.}\tag{3}
]

The retained scalar harmonic cap is (A\le A_*=1/2+r+s_1<57/100). For a rational certificate, the increasing polynomial (D_{\rm mass}(t)=196t-644t^2+896t^3-448t^4) satisfies (D_{\rm mass}(7/250)>1245/256), (D_{\rm mass}(41/1000)>41/6); hence (r<7/250), (s_1<41/1000), (A_*<569/1000<57/100). The four core squared lengths sum to (4-A_C>343/100). Consequently

[
\sum_{i,c}D_{ic}=\sum_c z_c^TS_Iz_c>\frac{343}{100}c,
\qquad \sigma_1(D)>\frac{343c}{800}=\frac{25039}{160000}.\tag{4}
]

Cauchy–Binet gives, **without any rank-two assumption**,

[
\boxed{\sum_{i<j,c<d}(D_{ic}D_{jd}-D_{id}D_{jc})^2
>\frac{23387172587863}{1638400000000000000000}
\approx1.4274397331\cdot10^{-8}.}\tag{5}
]

The minor floor is (117649/22500\approx5.22884) times the previous label-free certificate; the singular-value floor doubles. No isolated-Q rank-13, two-ray factorization, D5 labeling, or four ambiguous completion assumption enters. **Core coplanarity is still an explicit hypothesis.**

**[VERIFIED LOCALLY]** Companion exact Fraction/SymPy verifier checks the sharp n=3 equality family, root brackets, rational constants and factor. The analytic argument proves the universal claim; finite tests alone do not.

**[OPEN]** This is a stronger necessary lower obstruction, not a Type-E exclusion. An F3-incidence-sensitive *upper* bound on safe minors or (\sigma_2(D)) remains missing. Noncoplanar Type E, Types C/D, generic (e\ge27), and non-isolated branches remain open. Sparse (e=23/24) classification still requires (\delta(G)\ge1). Preserve (M(F3)\le89), (M(P)\ge S/2-28/3), (A\le383/504) and its stronger conditional refinement, the six-core defect ceilings, and Musin/Boyvalenkov boundary exclusion. **Global proved range: (40\le\tau_5\le44).**
