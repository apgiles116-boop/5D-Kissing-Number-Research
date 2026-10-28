# Type E: isolated-center harmonic gap (2026-10-28)

**[PROVED EXACTLY — universal isolated-center theorem]** For any 41-point spherical kissing code in dimension 5 whose deep graph has an isolated vertex, the full degree-2/degree-4 harmonic slack plus its 40 center-contact Delsarte slacks is at least **2595/256 = 10.13671875**. This is an exact rational obstruction, not an exclusion of an entire graph branch.

**[PROVED EXACTLY — conditional Type E]** Under the retained F3 broom and matching mass certificates, this sharpens the selected midpoint-energy bound to **A <= 0.5669250570031576**, the fourth-energy bound to **U <= 0.1282700463200052**, and the global projected squared-correlation floor to **28.2677055569326959**. These are algebraic constants; decimals are for display.

**[OPEN]** Type E and the other surviving branches remain unresolved. The global proved range remains 40 <= tau_5 <= 44.

## 1. Exact harmonic decomposition

For a 41-code X in S^4, let

\[
F(t)=28t^4-7t^2,\quad H_2(t)=t^2-\tfrac15,\quad
H_4(t)=t^4-\tfrac23t^2+\tfrac1{21}.
\]

The degree-2 and degree-4 zonal kernels are PSD by the spherical-harmonic addition theorem, and

\[
F(t)=1+\tfrac{35}{3}H_2(t)+28H_4(t).
\]

Set \(T=\sum_{v\in X}vv^\top-\frac{41}{5}I\) and
\(K_4=\sum_{v,w\in X}H_4(v\cdot w)\ge0\).
Then \(\sum_{v,w}H_2(v\cdot w)=\|T\|_F^2\).
For unordered deep pairs \(v\cdot w<-1/2\), let \(M_{\rm deep}=\sum F(v\cdot w)\); for all other unordered pairs, let \(N=\sum[-F(v\cdot w)]\ge0\).
Because \(41F(1)=861\),

\[
\boxed{M_{\rm deep}=410+N+\tfrac{35}{6}\|T\|_F^2+14K_4.}\tag{1}
\]

## 2. Isolated-center row

Suppose \(u\in X\) has no deep neighbor, so \(t_j=u\cdot v_j\in[-1/2,1/2]\) for all 40 other points. Define

\[
s=\sum_jt_j^2,\quad q=u^\top Tu=s-\tfrac{36}{5},\quad
N_0=\sum_j7t_j^2(1-4t_j^2).
\]

Since T is trace-free, Cauchy against \(uu^\top-I/5\) yields \(\|T\|_F^2\ge\frac54q^2\).
The fourth-harmonic center row is **exactly**

\[
h=\sum_{v\in X}H_4(u\cdot v)
=\tfrac{16}{7}-\tfrac5{12}s-\tfrac{N_0}{28}
\le-\tfrac57-\tfrac5{12}q.
\]

Kernel PSD and Cauchy give \(K_4\ge h^2/H_4(1)=\frac{21}{8}h^2\), since \(H_4(1)=8/21\).
For \(q\ge-12/7\), with \(E=\frac{35}{6}\|T\|_F^2+14K_4\),

\[
E\ge\tfrac{175}{24}q^2+\tfrac{147}{4}
 (\tfrac57+\tfrac5{12}q)^2
=10+\tfrac{35}{64}(5q+4)^2.\tag{2}
\]

For \(q<-12/7\), already \(E>\frac{150}{7}\).

## 3. Exact center-contact quantization

For \(x_j=t_j^2\in[0,1/4]\) with sum s, maximizing \(\sum x_j^2\) on the capped simplex puts all but at most one \(x_j\) at 0 or 1/4. If \(r=s-\lfloor4s\rfloor/4\) and \(\delta=\operatorname{dist}(s,\frac14\mathbb Z)=\min(r,1/4-r)\), then

\[
N_0\ge7r(1-4r)=7\delta(1-4\delta)\ge\tfrac72\delta.
\]

Put \(v=q+4/5\). Then \(s=32/5+v\), and the distance from \(32/5\) to the quarter-integer lattice is 1/10. Thus
\(N_0\ge\frac72(1/10-|v|)_+\).
Combining with (2),

\[
E+N_0\ge10+\tfrac{875}{64}v^2+
\tfrac72(1/10-|v|)_+.
\]

For \(|v|\ge1/10\), the quadratic term is at least 35/256. For \(|v|\le1/10\), the expression after 10 decreases with \(|v|\), since its derivative at 1/10 is \(875/320-7/2<0\). The \(q<-12/7\) case is stronger. Therefore

\[
\boxed{N_0+\tfrac{35}{6}\|T\|_F^2+14K_4
\ge B:=\tfrac{2595}{256}.}\tag{3}
\]

This holds without an F3 assumption or a D5 labeling. No code attaining equality is claimed.

## 4. Type-E scalar consequences

Retain \(H=16K_2\sqcup F_3\), \(S=M(F_3)\le89\), and a matching \(P\) with \(M(P)\ge S/2-28/3\).
For each of the 20 selected deep edges put \(a_i=\|m_i\|^2\) and
\(D(a)=21-F(2a-1)=196a-644a^2+896a^3-448a^4\).
Let \(D_I\) and \(D_C\) sum D over the 16 isolated and four F3 matching edges. Define

\[
\Xi=N+\tfrac{35}{6}\|T\|_F^2+14K_4-B\ge0,\qquad
c=15-B=\tfrac{1245}{256}.
\]

Equation (1), \(M_{\rm deep}=336-D_I+S\), and the F3 certificates give

\[
\boxed{D_I+\Xi\le c,\qquad
D_C+\tfrac12(D_I+\Xi)\le\tfrac{169}{3}-\tfrac B2.}\tag{4}
\]

Write \(x=\sum_Ia_i\), \(y=\sum_Ca_i\).
D is increasing and concave on [0,1/4], with \(D(a)\ge84a\), so \(D_I\ge D(x)\) and \(x\le r:=D^{-1}(c)<0.028\).
For \(y>1/2\), capped-simplex concavity gives \(D_C\ge42+D(y-1/2)\); the \(y\le1/2\) case is automatically weaker. Hence

\[
y\le\tfrac12+s(x),\quad
s(x)=D^{-1}(\tfrac{43}{3}-\tfrac12(B+D(x))).
\]

Here \(D^{-1}(w)=[1-\sqrt{(7+\sqrt{2401-112w})/56}]/2\).
The function s is positive, decreasing, convex, with
\(s_0=s(0)=D^{-1}(43/3-B/2)\) and \(s_1=s(r)=D^{-1}(41/6)\).
Exact rational root brackets give \(r>0.027\), \(s_1>0.039\), \(s_0<0.058\), hence \(r+s_1>s_0\). Convexity yields

\[
\boxed{A=\sum_i a_i\le A_{\rm new}:=\tfrac12+r+s_1
=0.5669250570031576\ldots.}\tag{5}
\]

For any \(\Xi\), repeating the argument with \(c-\Xi\) and using convexity of \(D^{-1}\) gives the stronger stability form

\[
A+\frac r c\,\Xi\le A_{\rm new}.\tag{6}
\]

The fourth energy obeys \(U=\sum_i a_i^2\le1/8+x^2+s(x)^2\). This convex expression has its maximum at x=0 (NOT x=r: exact brackets give \(s_0^2>r^2+s_1^2\)). Therefore

\[
\boxed{U\le U_{\rm new}:=\tfrac18+s_0^2
=0.1282700463200052\ldots.}\tag{7}
\]

## 5. Joint Q-frame consequence

For the 20 projected vectors, let \(V_z=\|\sum_i z_i z_i^\top-\frac{20-A}{5}I\|_F^2\ge0\). The exact identity is

\[
\sum_{i<j}(z_i\cdot z_j)^2
=30-3A+\tfrac{A^2}{10}-\tfrac U2+\tfrac{V_z}{2}.
\]

The *joint* scalar expression, evaluated at \(a(x)=1/2+x+s(x)\), \(u(x)=1/8+x^2+s(x)^2\), is strictly decreasing in x. Indeed its derivative is

\[
(-3+a(x)/5)(1+s'(x))-x-s(x)s'(x)<0,
\]

because \(a(x)<0.57\), \(s(x)<0.058\), and
\(-98/129\le s'(x)<0\) (from \(D'(x)\le196\), \(D'(s)>129\)).
Thus the joint minimum occurs at x=r, even though the separate U maximum is at x=0:

\[
\boxed{\sum_{i<j}(z_i\cdot z_j)^2\ge
30-3A_{\rm new}+\tfrac{A_{\rm new}^2}{10}
-\tfrac12(\tfrac18+r^2+s_1^2)
=28.2677055569326959\ldots.}\tag{8}
\]

If the earlier conditional F3 six-core squared-mass caps are retained, the 184-safe pairings have mass at least 26.4200493069327 (P1/P3) or 26.4864555569327 (P2). These are necessary conditions, not contradictions.

## Proof ledger

**[PROVED EXACTLY]** (1)-(3), conditional only on the isolated-center property and the standard PSD spherical-harmonic kernels.

**[PROVED EXACTLY — CONDITIONAL TYPE E]** (4)-(8), using the retained F3 broom/matching inputs; the 184-safe branchwise numbers additionally use the previously retained F3 endpoint lemmas.

**[OPEN]** Type E, Types C and D, generic e>=27, non-isolated branches, and sparse e=23/24 without minimum degree. Zero-midpoint exclusion remains based on Musin/Boyvalenkov, not D5 uniqueness. Global range remains 40<=tau_5<=44.

Companion exact verifier: tau5_typeE_isolated_center_harmonic_gap_2026-10-28_verify.py.
