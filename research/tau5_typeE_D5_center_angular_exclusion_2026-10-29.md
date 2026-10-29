# Type E: exact D5 center angular-exclusion theorem (2026-10-29)

**[PROVED EXACTLY — standalone algebra; CONDITIONAL TYPE-E APPLICATION]** The conclusion assumes twenty selected deep edges, an isolated center, and the retained midpoint-energy cap \(A\le383/504\). No Type-E exclusion or global improvement is claimed.

## Theorem

Let \(r_{ij}^{\pm}=(e_i\pm e_j)/\sqrt2\), \(1\le i<j\le5\), be the 20 projective D5 roots. Let \(u_1,\ldots,u_{20}\in S^4\), \(0\le a_i\le1/4\), \(A=\sum_i a_i\le383/504\), and \(z_i=\sqrt{1-a_i}\,u_i\). Suppose some unit center \(v\) satisfies \(|v\cdot z_i|\le1/2\) for every \(i\). For **every** rotation, bijection and projective sign matching between these 20 directions and the D5 lines, **at least one projective angular error is strictly greater than \(2/25\) radians** (about \(4.584^\circ\)).

For an isolated center in a hypothetical 41-code, the condition follows from both endpoint correlations \(v\cdot(m_i\pm z_i)\in[-1/2,1/2]\). The deep-edge condition implies \(a_i<1/4\). This theorem uses no six-core or 184-Walsh hypothesis.

## Exact D5 moment

For \(s_r=(v\cdot r)^2\) over the 20 D5 roots, direct expansion gives
\[
\sum_r s_r=4,\qquad
\sum_r s_r^2=\frac32+\frac12\sum_{k=1}^5v_k^4.
\]
Therefore, for \(f(s)=s(s-1/4)\),
\[
\sum_r f(s_r)=\frac12+\frac12\sum_kv_k^4\ge\frac35. \tag{1}
\]

## Angular-energy envelope

Assume every angular error is at most \(\theta=2/25\). Write
\[
b(a)=\frac1{2\sqrt{1-a}},\quad h(a)=\sqrt{1-b(a)^2},\quad
X_\theta(a)=b(a)\cos\theta+h(a)\sin\theta.
\]
Since \(|v\cdot u_i|\le b(a_i)\le1/\sqrt3<\cos\theta\), spherical triangle inequality yields \(|v\cdot r_i|\le X_\theta(a_i)\). Moreover \(X_\theta(a)\ge1/2\), so
\[
f(s_{r_i})\le [f(s_{r_i})]_+\le F_\theta(a_i),
\quad F_\theta(a)=X_\theta(a)^4-\tfrac14X_\theta(a)^2. \tag{2}
\]
On \(0\le a\le1/4\), elementary derivatives give
\[
\tfrac12\le b\le\tfrac35,\quad
\tfrac14\le b'\le\tfrac25,\quad
\tfrac38\le b''\le\tfrac45,\quad
h\ge\tfrac45,\quad -\tfrac3{10}\le h'\le0,\quad
-\tfrac{73}{80}\le h''\le0.
\]
Indeed \(h'=-bb'/h\) and \(h''=-(b'^2+bb'')/h-b^2b'^2/h^3\). Using \(\cos\theta\ge623/625\) and \(\sin\theta\le2/25\) proves \(X_\theta'>0\), \(X_\theta''>0\); \(X_\theta\ge1/2\) follows since \(X_\theta\) increases with \(\theta\) on this interval and \(X_0=b\ge1/2\). As \(x^4-x^2/4\) is increasing and convex for \(x\ge1/2\), \(F_\theta\) is increasing and convex. Its secant at \(a=0,1/4\) gives, with \(B=383/504\),
\[
\sum_iF_\theta(a_i)
\le(20-4A)F_\theta(0)+4AF_\theta(1/4)
\le(20-4B)F_\theta(0)+4BF_\theta(1/4). \tag{3}
\]

## Exact terminal certificate

Set \(\theta=2/25\), \(C=1-\theta^2/2+\theta^4/24\), and rational upper enclosures
\[
q_0=\tfrac12 C+\tfrac{17321}{20000}\theta,\quad
q_1=\tfrac{577351}{1000000}C+\tfrac{816497}{1000000}\theta.
\]
They dominate \(X_\theta(0)\) and \(X_\theta(1/4)\), using \(\cos\theta\le C\), \(\sin\theta\le\theta\), and exact rational bounds on \(\sqrt3/2\), \(1/\sqrt3\), \(\sqrt{2/3}\). Put \(U=(20-4B)f(q_0)+4Bf(q_1)\). Exact Fraction arithmetic gives
\[
\frac35-U=
\frac{354233594839339286756640083873782082234484437099}
{79208984971046447753906250000000000000000000000000}>0.
\]
Equations (1)–(3) would force \(3/5\le U<3/5\), a contradiction.

## Exact projective Q-matrix distance corollary

For unit \(u\), define the traceless projector \(Q(u)=uu^T-I/5\). Then
\[
\|Q(u)-Q(r)\|_F^2=2(1-(u\cdot r)^2)=2\sin^2(\operatorname{angle}_{\rm proj}(u,r)).
\]
Since at least one projective angle exceeds \(\theta=2/25\), every rotation \(R\) and line matching \(\pi\) satisfies
\[
\boxed{\sum_{i=1}^{20}\|Q(u_i)-RQ(r_{\pi(i)})R^T\|_F^2>\frac1{80}.}
\]
The exact rational certificate is
\[
2\sin^2(\theta)\ge2(\theta-\theta^3/6)^2
=\frac1{80}+\frac{9587387}{35156250000}>\frac1{80}.
\]
Thus the D5 **Q-template orbit** is quantitatively separated from any candidate under the retained hypotheses. This is not a lower bound on the unaligned global frame variance.

**[VERIFIED EXACTLY]** The companion SymPy/Fraction checker independently expands the 20-root moments and verifies all rational enclosures and the terminal positive fraction. The analytic derivative and angular steps are written above.

**[OPEN]** This is a lower bound on D5 angular deviation, not an upper bound and not an elimination of Type E. A future D5-rounding argument must prove an upper error at most \(2/25\) to create a contradiction. Types C, D, generic \(e\ge27\), and non-isolated branches remain open. Sparse \(e=23,24\) classifications still require \(\delta(G)\ge1\).

**[GLOBAL PROVED RANGE — UNCHANGED]** \(40\le\tau_5\le44\). Preserve the retained Type-E star \(70/3\), broom \(M(F_3)\le89\), matching \(M(P)\ge S/2-28/3\), and cap \(A\le383/504\).
