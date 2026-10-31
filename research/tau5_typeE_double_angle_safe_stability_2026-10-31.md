# Type E: uniform double-angle core gap and sixteen-line safe leakage

**Date:** 2026-10-31. **Global proved range unchanged:** 40 <= tau_5 <= 44. **Type E remains OPEN.**

## Theorem A — uniform four-core wedge [PROVED EXACTLY, conditional on coplanarity and the retained Type-E midpoint cap]

For four distinguished deep pairs, let \(a_c=\|m_c\|^2\le 1/4\), \(t_c=\|z_c\|^2=1-a_c\ge3/4\), \(A_C=\sum a_c\le383/504\), and assume the four projected vectors \(z_c\) lie in a two-plane. Their six endpoint inequalities are \(m_c\cdot m_d+|z_c\cdot z_d|\le1/2\).

For **every** orthonormal basis \(p,q\) of that plane, put \(r_c=(p\cdot z_c)^2\), \(s_c=(q\cdot z_c)^2\). Then
\[
\boxed{\sum_{c<d}(r_cs_d-r_ds_c)^2\ge\frac{81}{2048}.}
\]
Equivalently, for the unit double-angle vectors \(\omega_c=(\cos2\theta_c,\sin2\theta_c)\),
\[
\boxed{\sum_{c<d}(\omega_c-\omega_d)(\omega_c-\omega_d)^\top\succeq\frac12 I_2.}
\]
Neither conclusion assumes a D5 labeling or a Q-rank hypothesis.

### Proof

Set \(b_c=1/4-a_c\ge0\). Cauchy–Schwarz and the endpoint inequalities give
\[
\sin^2(\theta_c-\theta_d)\ge
\frac{3/4-a_c-a_d-\sqrt{a_ca_d}}{(1-a_c)(1-a_d)}
\ge\frac32(b_c+b_d).
\]
Let \(x_c=\cos2\theta_c\). When \(\sin2\theta_c\) and \(\sin2\theta_d\) have the same sign (zero can be assigned either sign), the two double-angle points lie on one semicircle, where
\[
1-\omega_c\cdot\omega_d\le|x_c-x_d|.
\]
It follows that every same-sign pair satisfies
\[
|x_c-x_d|\ge3(b_c+b_d). \tag{1}
\]

For a triple \(T\) of the same sign, the same semicircle inequality gives
\[
|z_c\cdot z_d|\ge\frac34\left(1-\frac{|x_c-x_d|}{2}\right).
\]
Summing over its three pairs and using
\(\sum_{c<d\in T}m_c\cdot m_d=(\|\sum_Tm_c\|^2-A_T)/2\ge-A_T/2\), one obtains
\[
\sum_{c<d\in T}|x_c-x_d|\ge2-\frac43 A_T\ge1
\]
because \(A_T\le3/4\). Three real numbers therefore have range at least \(1/2\), so their squared pairwise differences sum to at least \(3/8\). Adding a fourth real number increases the total squared-difference sum to at least \(4/3\) times the triple sum. Thus any sign partition with a class of size three or four gives
\[
\sum_{c<d}(x_c-x_d)^2\ge1/2.
\]

In the remaining 2+2 partition, write \(B_1=b_1+b_2\), \(B_2=b_3+b_4\). Equation (1) and the exact four-point variance identity give
\[
\sum_{c<d}(x_c-x_d)^2
\ge2\big[(x_1-x_2)^2+(x_3-x_4)^2\big]
\ge18(B_1^2+B_2^2)\ge9(1-A_C)^2.
\]
Since \(1-A_C\ge121/504\), this is at least
\(14641/28224=1/2+529/28224>1/2\).
Hence for **every** choice of planar axes,
\(\sum_{c<d}(x_c-x_d)^2\ge1/2\), proving the double-angle PSD statement. Finally
\[
r_cs_d-r_ds_c=\frac{t_ct_d}{2}(x_c-x_d),
\]
and \(t_c\ge3/4\) gives the wedge bound \(81/2048\). QED.

## Theorem B — safe sixteen-line leakage [PROVED EXACTLY, no Q-rank assumption]

For the sixteen isolated selected deep pairs, all 120 pairings are safe. Define \(A_I=\sum_Ia_i\), \(Z_I=\sum_Iz_iz_i^\top\), \(s_I=\|\sum_I m_i\|^2\),
\(V_m=A_I^2-\|\sum_I m_im_i^\top\|_F^2\ge0\), and
\[
R_I=\sum_{i<j\in I}\big[(1/2-m_i\cdot m_j)^2-(z_i\cdot z_j)^2\big]\ge0.
\]
Expanding the 120 endpoint squares gives the **exact identity**
\[
\boxed{\|Z_I\|_F^2=76-A_I+A_I^2-s_I-V_m-2R_I.} \tag{2}
\]

For any three-dimensional subspace \(W\subset\mathbb R^5\), let
\(L=\sum_I\|P_{W^\perp}z_i\|^2\).
The three-dimensional frame block has trace \(16-A_I-L\), so its squared Frobenius norm is at least \((16-A_I-L)^2/3\). The two complementary diagonal entries contribute at least \(L^2/2\). Equation (2) therefore gives
\[
\boxed{\frac{L^2}{2}+\frac{(16-A_I-L)^2}{3}\le76-A_I+A_I^2.} \tag{3}
\]
For \(A_I\le383/504\), this implies
\[
\boxed{L\ge\frac{7681-\sqrt{55944906}}{1260}
=0.159815281750\ldots>\frac3{20}.}
\]
Indeed, for \(L\le3/20\) the difference (left minus right) in (3) decreases in both \(L\) and \(A_I\); at \(L=3/20\), \(A_I=383/504\), it equals the positive rational \(92579/952560\). The sharper radical is the smaller quadratic root at the maximal allowed \(A_I\), with the same monotonicity argument.

## Theorem C — conditional rank-13 two-ray safe-minor gap [PROVED EXACTLY]

Assume additionally that the sixteen isolated Q-projectors have rank 13, their missing traceless matrix has rank two, and all four core lines have genuinely ambiguous rank-one completions. The retained phase-retrieval theorem supplies axes \(p,q\) such that each isolated vector has \((p\cdot z_i)(q\cdot z_i)=0\), and every core vector lies in \(\mathrm{span}(p,q)\). Put
\(X=\sum_I(p\cdot z_i)^2\), \(Y=\sum_I(q\cdot z_i)^2\).
Then \(X,Y>0\) and Theorem B gives \(X+Y>3/20\).

The **safe** matrix \(D_{ic}=(z_i\cdot z_c)^2\) has rank two. Its rows are scalar multiples of \(r=(r_c)\) or \(s=(s_c)\). Let \(\rho=\sum_{p\text{-active}}(p\cdot z_i)^4\), \(\sigma=\sum_{q\text{-active}}(q\cdot z_i)^4\). Exact Cauchy–Binet gives
\[
\sum_{i<j,c<d}(D_{ic}D_{jd}-D_{id}D_{jc})^2
=\rho\sigma\sum_{c<d}(r_cs_d-r_ds_c)^2.
\]
There are at most sixteen active rows, so the two group sizes have product at most 64. Consequently
\[
\boxed{\sum\text{(safe minors)}^2\ge\frac{81}{131072}X^2Y^2.}
\]
Each \(D_{ic}\le9/16\), hence \(\|D\|_F^2\le81/4\). Using the product of the two nonzero squared singular values,
\[
\boxed{\sigma_2(D)\ge\frac{XY}{128\sqrt2}.}
\]

**[OPEN / LIMITATION]** The leakage lower bound on \(X+Y\) does **not** imply a uniform lower bound on \(XY\). This prevents claiming a uniform safe-minor gap or excluding Type E from these results alone. Next: combine the exact core wedge gap with the F3 signed endpoint/Walsh constraints or obtain a lower bound on both ray energies.

**Retained inputs (not independently reproved):** \(M(F_3)\le89\), \(M(P)\ge S/2-28/3\), twenty-edge mass \(\ge2137/6\), \(A\le383/504\), raw/homogeneous defect ceilings, and the Musin/Boyvalenkov zero-midpoint exclusion. Sparse e=23/e=24 graph classification remains conditional on \(\delta(G)\ge1\). Types C, D, E, generic e>=27, and non-isolated branches remain open. **Global proved range remains 40<=tau_5<=44.**
