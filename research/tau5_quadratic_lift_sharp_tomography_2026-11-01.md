# Sharp quadratic-lift spectral inequality and stronger label-free Type-E tomography

**Date:** 2026-11-01. **Status:** [PROVED EXACTLY — standalone sharp linear-algebra theorem]; [PROVED EXACTLY, CONDITIONAL ON RETAINED TYPE-E HARMONIC/CORE-Q CERTIFICATES AND CORE COPLANARITY] for the geometric application. **Type E remains OPEN.** The globally proved range remains **40 <= tau_5 <= 44**.

## 1. Sharp universal theorem

Let \(w_1,\ldots,w_n\) be vectors in \(\mathbb R^2\), \(n\ge2\), with \(S=\sum_i w_iw_i^T\succeq cI_2\), \(c>0\). Let \(B\) be the \(n\times3\) matrix whose rows are the Frobenius-orthonormal coordinates of the symmetric tensors \(w_iw_i^T\). Then

\[
\boxed{\sigma_2(B)^2\ge c^2/n.}\tag{1}
\]

The coefficient \(1\) is **optimal uniformly over \(n\ge3\)**: take \(n\) equally spaced projective directions \(\theta_i=i\pi/n\), each of squared norm \(2c/n\). Then \(S=cI_2\) and the three squared singular values of \(B\) are \(2c^2/n,c^2/n,c^2/n\). This improves the previous \(c^2/(4n)\) estimate by a factor of four and needs no bound on individual vector norms.

### Proof [EXACT]

Define the positive semidefinite operator on \(\operatorname{Sym}^2(\mathbb R^2)\)

\[
T(X)=\sum_i \langle w_iw_i^T,X\rangle_F w_iw_i^T.
\]

Its matrix is \(B^TB\). The top eigenvalue has a positive semidefinite unit eigenmatrix \(X\): if \(X\) is any top eigenmatrix, replacing it by the matrix absolute value \(|X|\) preserves its Frobenius norm and weakly increases every \(|w_i^TXw_i|\); hence \(|X|\) also attains the top Rayleigh quotient.

Choose orthonormal coordinates diagonalizing this top PSD matrix \(X\). Write \(w_i=(x_i,y_i)\) and set

\[
A_i=x_i^2,\quad B_i=y_i^2,\quad
a=\sum_i A_i^2,\quad b=\sum_i B_i^2,\quad
d=\sum_i A_iB_i,\quad t=c^2/n.
\]

Since \(S\succeq cI\), both \(\sum_i A_i\ge c\) and \(\sum_i B_i\ge c\); Cauchy gives \(a,b\ge t\). The covariance Cauchy–Schwarz inequality gives

\[
d\ge \frac{(\sum A_i)(\sum B_i)}n
-\sqrt{\left(a-\frac{(\sum A_i)^2}n\right)
       \left(b-\frac{(\sum B_i)^2}n\right)}
\ge t-\sqrt{(a-t)(b-t)}.\tag{2}
\]

There are two cases. If \(d\ge t/2\), the Frobenius-unit off-diagonal matrix \(Z=(e_1e_2^T+e_2e_1^T)/\sqrt2\) is orthogonal to the top eigenmatrix \(X\), and its Rayleigh quotient is \(\sum_i(w_i^TZw_i)^2=2d\ge t\).

If \(d<t/2\), (2) implies \(\sqrt{(a-t)(b-t)}\ge t-d>d\). Therefore the diagonal-sector Gram matrix \(\begin{pmatrix}a&d\\d&b\end{pmatrix}\succeq tI_2\). The Frobenius-unit diagonal matrix orthogonal to \(X\) has Rayleigh quotient at least \(t\).

In either case there exists a unit symmetric matrix orthogonal to a top eigenmatrix whose Rayleigh quotient is at least \(t\). By Courant–Fischer, \(\lambda_2(B^TB)\ge t\), proving (1). The equality family above proves sharpness.

## 2. Stronger Type-E coplanar-core application

Assume the four selected F3 core projected vectors span a two-plane \(W\). Let \(D\) be the **fully safe** \(16\times4\) squared-correlation matrix \(D_{ic}=(z_i\cdot z_c)^2\). Retain, without reproving, the separately established certificates

\[
\lambda_{\min}(S_I)>c=73/200,\qquad S_I=\sum_{i\in I}z_iz_i^T,
\qquad\lambda_3(K_C)>\epsilon=7/100000,
\]

where \(K_C\) is the four-core traceless-Q Gram, as in the 2026-11-01 small-isolated-mass and coplanar-Q-minor notes. No D5 labeling, isolated-Q rank-13 assumption, or two-ray factorization is used.

Let \(w_i=P_Wz_i\), and let \(B\) be their 2D quadratic-lift matrix. In the Frobenius-orthonormal basis of \(\operatorname{Sym}^2(W)\), let \(C\) be the \(3\times4\) matrix of the core tensors \(z_cz_c^T\). Then \(D=BC\). The five-dimensional traceless projection has metric \(M=\operatorname{diag}(3/5,1,1)\) on this three-space, so \(K_C=C^TMC\) and \(0<M\preceq I\). The rank-three core certificate implies \(CC^T>\epsilon I_3\). Therefore

\[
\boxed{\sigma_2(D)^2>\epsilon c^2/16
=\frac{37303}{64000000000},\qquad
\sigma_2(D)>\frac{73}{800}\sqrt{\frac7{100000}}
\approx0.0007634522742>\frac3{4000}.}\tag{3}
\]

This **doubles** the earlier label-free singular-value lower bound, while retaining exactly the same core-coplanarity hypothesis.

## 3. Stronger all-minor certificate

The retained scalar harmonic theorem gives \(A\le A_*<57/100\). For an elementary exact bracket, \(D_{\rm mass}(t)=196t-644t^2+896t^3-448t^4\) is increasing on \([0,1/4]\) and

\[
D_{\rm mass}(7/250)>1245/256,\qquad
D_{\rm mass}(41/1000)>41/6.
\]

Thus its retained roots satisfy \(r<7/250\), \(s_1<41/1000\), and \(A_*=1/2+r+s_1<569/1000<57/100\). Consequently the four core squared norms sum to \(4-A_C>343/100\). Since \(S_I>cI\), the sum of all 64 nonnegative entries of \(D\) is

\[
\sum_{i,c}D_{ic}=\sum_c z_c^TS_Iz_c>(343/100)c.
\]

Testing against the two normalized all-ones vectors yields

\[
\sigma_1(D)>(343/800)c=\frac{25039}{160000}.\tag{4}
\]

Cauchy–Binet gives the sum of squared \(2\times2\) minors as the second elementary symmetric function of the squared singular values; this is at least \(\sigma_1(D)^2\sigma_2(D)^2\), even if \(\operatorname{rank}(D)=3\). Equations (3)-(4) give

\[
\boxed{\sum_{i<j,\;c<d}(D_{ic}D_{jd}-D_{id}D_{jc})^2
>\frac{23387172587863}{1638400000000000000000}
=1.427439733145935\ldots\times10^{-8}>10^{-8}.}\tag{5}
\]

This is \(117649/22500=5.22884444\ldots\) times the previous label-free lower bound, using the sharp lift inequality and the retained stronger midpoint cap. This is a **necessary lower bound**, not an incompatible upper certificate.

## 4. Proof ledger and next task

- **[PROVED EXACTLY — STANDALONE]** Sharp quadratic-lift inequality (1), including a constructive equality family.
- **[PROVED EXACTLY — CONDITIONAL TYPE E]** Singular-value floor (3) and minor floor (5), assuming only the retained isolated-frame and coplanar core-Q certificates, core coplanarity, and the retained scalar midpoint cap. Neither rank 13 nor a two-ray model is inferred.
- **[VERIFIED LOCALLY]** Companion exact SymPy/Fraction verifier checks the equality family, rational root brackets, transfer constants and improvement factor. The universal proof is analytic; finite checks are not its justification.
- **[OPEN]** No Type-E elimination. The missing step is still a signed F3-incidence-sensitive **upper** certificate on the safe \(16\times4\) minors or \(\sigma_2(D)\) that contradicts (3) or (5). Noncoplanar Type E, Types C/D, generic \(e\ge27\), and non-isolated branches remain open. Sparse \(e=23/24\) classification retains \(\delta(G)\ge1\). Preserve \(M(F3)\le89\), \(M(P)\ge S/2-28/3\), \(A\le383/504\) (and its stronger conditional refinement), both six-core defect ceilings, and the Musin/Boyvalenkov zero-midpoint exclusion. **Global proved range: \(40\le\tau_5\le44\).**
