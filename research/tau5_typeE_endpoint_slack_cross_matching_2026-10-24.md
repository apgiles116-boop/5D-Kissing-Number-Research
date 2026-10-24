# Type E: endpoint-slack refinement of cross-matching stability

**2026-10-24. Proof status:** [PROVED EXACTLY] the four-edge theorem and an endpoint-feasible equality witness. [CONDITIONAL TYPE E] the numerical energy-cap consequence. [OPEN] stronger uniform defect bounds and Type-E elimination.

For selected deep edges \(x_i^\pm=m_i\pm z_i\) with unit endpoints, put \(\delta_{ij}=(|z_i\cdot z_j|-1/2)_+\). All four endpoint inequalities read
\[
m_i\cdot m_j+st\,z_i\cdot z_j+s\,z_i\cdot m_j+t\,m_i\cdot z_j\le 1/2
\quad(s,t=\pm1).
\]
For \(\delta_{ij}>0\), let \(\sigma_{ij}=\operatorname{sign}(z_i\cdot z_j)\) and define
\(\ell_{ij}=-m_i\cdot m_j-\delta_{ij}\ge0\).
The two endpoint inequalities with \(st=\sigma_{ij}\) give the **mixed-term slack**
\[
|m_i\cdot z_j+\sigma_{ij}z_i\cdot m_j|\le\ell_{ij}. \tag{1}
\]
The usual weaker inequality \(m_i\cdot m_j+|z_i\cdot z_j|\le1/2\) discards (1).

## Strengthened four-core theorem [PROVED EXACTLY]

Assume \(p=\delta_{12}>0\) and \(q=\delta_{34}>0\). Set
\[
C=\sum_{i=1}^4\|m_i\|^2,\quad
\ell=\ell_{12}+\ell_{34},\quad
w=\min(\delta_{13}+\delta_{24},\,\delta_{14}+\delta_{23}).
\]
Then
\[
\boxed{(p+q+\ell)^2+w^2\le C^2/4.} \tag{2}
\]
In particular, writing \(b_{ij}=m_i\cdot z_j+\sigma_{ij}z_i\cdot m_j\),
\[
\boxed{p+q+|b_{12}|+|b_{34}|+w^2/C\le C/2.} \tag{3}
\]
This strengthens the previous cross-matching inequality by retaining the endpoint slacks.

**Proof.** Let \(x=m_1+m_2\), \(a=m_1-m_2\), \(y=m_3+m_4\), \(b=m_3-m_4\), and \(r=\|x\|^2+\|y\|^2\). The four cross midpoint products have the exact Walsh decomposition
\[
4m_1\cdot m_3=X+U+V+W,\quad
4m_2\cdot m_4=X-U-V+W,
\]
\[
4m_1\cdot m_4=X-U+V-W,\quad
4m_2\cdot m_3=X+U-V-W,
\]
with \(X=x\cdot y\), \(U=x\cdot b\), \(V=a\cdot y\), \(W=a\cdot b\). If \(W\ge0\), the first cross matching has total positive defect at most \((|X+U+V|+|X-U-V|)/4\); if \(W\le0\), the second is similarly bounded. Since \(m_3\cdot m_4<0\), \(\|b\|\ge\|y\|\). Cauchy–Schwarz gives
\(2w\le\|x\|\|b\|+\|a\|\|y\|\), hence \(4w^2\le r(2C-r)\).
The **exact** identity \(r=C-2(p+q+\ell)\) proves (2). Finally,
\(w^2\le C(C/2-p-q-\ell)\), and (1) proves (3).

## Conditional Type-E consequence

Under the retained \(C\le A\le B=383/504\), if \(p+q\ge B/2-h\), then
\[
\boxed{|b_{12}|+|b_{34}|+w^2/B\le h.} \tag{4}
\]
At \(h=1/1000\), this is
\(|b_{12}|+|b_{34}|+(504/383)w^2\le1/1000\).
If \(w\ge1/50\), the mixed products have total magnitude at most \(907/1915000\).

## Exact endpoint-feasible sharpness witness

In orthonormal \(e_1,\ldots,e_5\), take
\(m_1=-m_2=e_1/\sqrt{10}\), \(m_3=-m_4=e_2/\sqrt{10}\).
Put \(u=3/\sqrt{10}\), \(v=11\sqrt{10}/60\), \(t=\sqrt{203/360}\), and
\[
z_1=ue_3,\quad z_2=ve_3+te_4,\quad z_3=ue_5,\quad
z_4=ve_5+t(3e_3/5-4e_4/5).
\]
All endpoint norms equal 1, and all inter-edge endpoint products are at most \(1/2\). Here \(p=q=1/20\), \(\ell_{12}=\ell_{34}=1/20\), \(C=2/5\), \(w=0\), so (2) is **equality**. This is a four-edge witness, **not** a full Type-E configuration.

## Exact eight-class polynomial formulation [UNSOLVED]

Use the \(8\times8\) Gram matrix \(H\) of \((m_1,\ldots,m_4,z_1,\ldots,z_4)\), impose \(H\succeq0\), \(\operatorname{rank}H\le5\), diagonal unit-endpoint and orthogonality identities, \(0\le\|m_i\|^2\le1/4\), \(C\le B\), and all 24 endpoint inequalities. Alternatively factor \(H=Y^TY\) with \(Y\in\mathbb R^{5\times8}\). Switching the four \(z_i\) independently makes \(z_1\cdot z_j\ge0\) for \(j=2,3,4\); the three remaining signs on (23),(24),(34) yield exactly **eight** sign branches. For each \(y_{ij}=|z_i\cdot z_j|\), encode \(\delta_{ij}=(y_{ij}-1/2)_+\) with
\(\delta\ge0,\ \delta\ge y-1/2,\ \delta(\delta-y+1/2)=0\).
The retained raw-defect cap \(\sum\delta\le1780062775/4032758016\) can then be imposed. This is exact for the four-core *local relaxation*, not the full 20-edge Type-E configuration; no global polynomial optimum has been certified.

**Ledger:** [PROVED] (1)–(3), sharpness witness. [CONDITIONAL] (4). [OPEN] stronger uniform six-defect ceiling, safe-pair upper bound, Type E, C, D, generic \(e\ge27\). Retain \(40\le\tau_5\le44\), \(M(F_3)\le89\), \(M(P)\ge S/2-28/3\), \(A\le383/504\).
