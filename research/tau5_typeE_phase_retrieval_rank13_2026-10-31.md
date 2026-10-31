# Type E: rank-13 phase-retrieval refinement and quantitative isolated-frame stability

2026-10-31. **Proof status: Type E OPEN; global proved range 40 <= tau_5 <= 44.**

## Theorem A — exact norm-aware phase retrieval (PROVED EXACTLY)

Fix the sixteen isolated projected vectors \(z_i\in\mathbb R^5\). Suppose two candidate core vectors \(z,z'\) have equal norm and identical safe isolated-core squared correlations. Then
\[
 (z_i\cdot z)^2-(z_i\cdot z')^2
 =[z_i\cdot(z-z')][z_i\cdot(z+z')]=0
\]
for every isolated index. If the candidates are distinct projective lines, \(x=z-z'\) and \(y=z+z'\) are nonzero and orthogonal. Thus the sixteen isolated vectors lie in the union of two hyperplanes \(x^\perp\cup y^\perp\) with orthogonal normals.

**Corollary.** If every eight of the sixteen isolated vectors span \(\mathbb R^5\), no ambiguity exists. Alternatively, nine isolated vectors with every five linearly independent (full spark) suffice. These are *fixed-isolated-realization* uniqueness results, independent of the rank of the traceless-Q Gram matrix. Safe pairwise squares alone need not determine the isolated realization.

## Theorem B — rank-13 ambiguity is a rank-two null phenomenon (PROVED EXACTLY)

Let \(Q_i=z_i z_i^\top-\|z_i\|^2I/5\), and suppose the sixteen isolated \(Q_i\) span a 13-dimensional subspace \(W\subset\operatorname{Sym}_0(5)\). Let nonzero \(S\) span \(W^\perp\). For a core with fixed norm \(w=\|z\|^2\), its safe measurements determine \(Q=L+tS\) with \(L\in W\) and known \(t^2\). The unrestricted Gram completion permits two signs.

If both \(L+tS\) and \(L-tS\), \(t\ne0\), are genuine core rank-one projectors, then
\[
 2tS=w(P_+-P_-),\qquad P_\pm=u_\pm u_\pm^\top.
\]
The difference of distinct rank-one orthogonal projectors has rank exactly two, and image \(\operatorname{span}(u_+,u_-)\). Therefore \(\operatorname{rank}S=2\), and both core directions belong to \(E=\operatorname{im}S\).

**Consequently, if \(\operatorname{rank}S\ge3\), every actual core has a UNIQUE rank-one completion** relative to the fixed isolated realization, despite the former at-most-eight unrestricted sign patterns.

If \(\operatorname{rank}S=2\), write \(S=\gamma(pp^\top-qq^\top)\) with orthonormal \(p,q\). From \(\langle S,Q_i\rangle=0\),
\[
 (p\cdot z_i)^2=(q\cdot z_i)^2,\quad
 [z_i\cdot(p+q)][z_i\cdot(p-q)]=0.
\]
Hence the sixteen isolated lines lie in two orthogonal-normal hyperplanes. An ambiguous core line must lie in \(E=\operatorname{span}(p,q)\); conversely \(u=\alpha p+\beta q\) with \(\alpha^2\ne\beta^2\) has the distinct partner \(u'=\beta p+\alpha q\) with identical safe isolated-core squared correlations. Thus this describes the exact rank-13 ambiguity locus. No Type-E feasibility is asserted for this locus.

## Theorem C — exact quadratic rank-one sign selector (PROVED EXACTLY)

A symmetric traceless \(Q\) is a scaled rank-one projector of norm parameter \(w>0\) exactly when
\[
 Q^2=\frac{3w}{5}Q+\frac{4w^2}{25}I.
\]
For \(Q=L+tS\), let \(s=t^2\) be fixed by the safe diagonal residual, and set
\[
 B_0=L^2+sS^2-\frac{3w}{5}L-\frac{4w^2}{25}I,\qquad
 B_1=LS+SL-\frac{3w}{5}S.
\]
Then \(B_0+tB_1=0\). If \(B_1\ne0\), the only possible sign is
\[
 t=-\frac{\langle B_0,B_1\rangle_F}{\|B_1\|_F^2}.
\]
It must also pass \(t^2=s\) and the full matrix identity. Both signs can pass only if \(B_0=B_1=0\); for \(t\ne0\), Theorem B forces rank \(S=2\). These are exact polynomial tests after clearing denominators.

## Theorem D — quantitative second-order inverse estimate (PROVED CONDITIONALLY)

For every eight-element subset \(T\) of the sixteen isolated indices, assume its frame operator
\[
 F_T=\sum_{i\in T}z_i z_i^\top\succeq\lambda I_5
\]
with a common \(\lambda>0\). Then for any equal-norm \(z,z'\),
\[
 \boxed{\sum_{i=1}^{16}[(z_i\cdot z)^2-(z_i\cdot z')^2]^2
 \ge\frac{\lambda^2}{4}\|Q(z)-Q(z')\|_F^2.}
\]
Proof: for unit \(x,y\), among sixteen indices at least eight have \((z_i\cdot x)^2\le(z_i\cdot y)^2\), or the reverse. On an eight-set of the larger class, Cauchy and \(F_T\succeq\lambda I\) give \(\sum_i(z_i\cdot x)^2(z_i\cdot y)^2\ge\lambda^2/8\). Homogenize and put \(x=z-z'\), \(y=z+z'\). Use \(\|x\|^2\|y\|^2=2\|Q(z)-Q(z')\|_F^2\).

The hypothesis has an exact isolated-coordinate polynomial certificate:
\[
 d_T=\det F_T=\sum_{J\subset T,|J|=5}\det([z_j]_{j\in J})^2>0
\]
for every eight-set. One can take \(\lambda=\min_T d_T/(\operatorname{tr}F_T)^4>0\). This does **not** require full isolated Q-rank, but it is not known for all Type-E candidates. A nine-vector full-spark subset similarly gives coefficient \(2\mu^2/5\), where \(\mu\) is the minimum frame eigenvalue over its five-subsets.

## Exact negative result: trace-square shortcut cannot work (PROVED EXACTLY)

For an eight-subset define \(s_T=\operatorname{tr}F_T\), \(t_T=\operatorname{tr}(F_T^2)\). The safe-squared-data condition \(s_T^2>4t_T\) is sufficient to prove \(F_T\) has rank five *for one subset*, but it **cannot hold for all 12,870 eight-subsets of any sixteen nonzero vectors in \(\mathbb R^5\)**.

Let \(W=\sum_i w_i\), \(U=\sum_iw_i^2>0\), and \(R=\sum_{i<j}(z_i\cdot z_j)^2\). Exact averaging yields
\[
 \mathbb E_T[s_T^2/4-t_T]
 =\frac7{120}W^2-\frac{13}{30}U-\frac7{15}R.
\]
The five-dimensional frame/Welch inequality \(R\ge W^2/10-U/2\) and Cauchy \(W^2\le16U\) give
\[
 \mathbb E_T[s_T^2/4-t_T]\le\frac7{600}W^2-\frac15U
 \le-\frac{U}{75}<0.
\]
At least one eight-subset therefore fails the trace-square test. The valid determinant-based criterion above must not be replaced by this vacuous simultaneous trace criterion.

## Verification and status

Companion exact SymPy verifier constructs rank-13 isolated frames with null matrix of rank two and four. The rank-two example admits eight distinct coherent rank-one core completions; the rank-four example has a unique rank-one completion. It checks the quadratic sign selector, phase-retrieval identities and exact no-go arithmetic. These are algebraic synthetic examples, **not** Type-E endpoint-feasible codes.

**OPEN:** No rank stratum has been eliminated; no upper bound on the 184 safe correlation energy contradicts the retained floor. Next: split rank-13 by 3x3 minors of \(S\), eliminate all core signs in the rank-\(\ge3\) subbranch, and impose orthogonal-hyperplane/core-plane incidence equations in rank two. Seek a same-labeling Walsh/Q contradiction.

Retain exact \(M(F_3)\le89\), matching \(M(P)\ge S/2-28/3\), twenty-edge mass \(\ge2137/6\), \(A\le383/504\), raw defect \(\le1780062775/4032758016\), Musin/Boyvalenkov zero-midpoint exclusion, and the \(\delta(G)\ge1\) qualification on sparse \(e=23,24\). **Global proved range unchanged: \(40\le\tau_5\le44\).**
