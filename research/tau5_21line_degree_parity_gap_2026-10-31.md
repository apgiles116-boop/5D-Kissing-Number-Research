# Improved quantitative 21-line projective obstruction (2026-10-31)

**[PROVED EXACTLY, analytic]** For any 21 unit vectors $u_i\in\mathbb R^5$, let $b_{ij}=(u_i\cdot u_j)^2$, $P=\sum_{i<j}[b_{ij}(b_{ij}-1/4)]_+$, and $D=\sum_{i<j}(|u_i\cdot u_j|-1/2)_+$. Then

$
\boxed{P>71/5000,\qquad D>71/7500.}
$

This improves the earlier $P>1/103$, $D>2/309$ without assuming D5 uniqueness. It does not eliminate Type E.

## Exact proof

Let $T=\sum_i u_iu_i^\top$, $B=T-(21/5)I_5$, $V=\operatorname{tr}(B^2)$. The positive Gegenbauer decomposition

$
t^4-t^2/4=1/28+P_2(t)/3+(8/21)P_4(t)
$

gives $F=\sum_{i<j}b_{ij}(b_{ij}-1/4)=(5/24)V+(4/21)H_4\ge(5/24)V$. Round $b_{ij}$ to $k_{ij}/4$, $k_{ij}\in\{0,1\}$, at $b=1/8$. The scalar bounds on the rounding error give

$
E=\sum|b_{ij}-k_{ij}/4|\le12P-(5/3)V.
$

Assume $P\le p=71/5000$. Then $V\le(24/5)p=213/3125$, and $2E\le B_0(V)=213/625-(10/3)V$. Because $2\sum_{i<j}b_{ij}=67+1/5+V$, the half-integer $\frac12\sum_{i<j}k_{ij}$ can only be (67) or (67.5); hence $\sum k_{ij}=134$ or (135).

Set $k_i=\sum_{j\ne i}k_{ij}$, $d_i=u_i^\top B u_i$, $c_i=k_i/4-16/5$. Then $\sum k_i=268$ or (270), $\sum_i|d_i-c_i|\le B_0(V)$, and by Cauchy–Schwarz

$
\sum_i d_i^2\le\operatorname{tr}$B^2T$\le\bigl$21/5+\sqrt{4V/5}\bigr$V.
$

**Integer-degree lemma.** The function $c\mapsto\min_{\|e\|_1\le B}\|c+e\|_2^2$ is convex and symmetric, hence Schur-convex. Among integer degree vectors with a fixed sum, the balanced vector minimizes it. For sum (268), the balanced degrees are five 12s and sixteen 13s; for sum (270), three 12s and eighteen 13s. For $B\le9/20$, the exact minima are

$
g_{134}(B)=(1-B)^2/5+1/25,\quad
g_{135}(B)=(3/5-B)^2/3+9/200.
$

The trace-rounding error forces, respectively,

$
V\le v_{134}=264/8125,\qquad V\le v_{135}=153/8750.
$

Both are less than (1/25), so $\|T\|_{op}<22/5$. On the respective intervals $h_j(V)=g_j(B_0(V))-(22/5)V$ is strictly decreasing, but exact rational endpoint calculations give

$
h_{134}$v_{134}$=4900821/330078125>0,
$

$
h_{135}$v_{135}$=254481/153125000>0.
$

Contradiction. Therefore $P>71/5000$. Since $s^2(s^2-1/4)\le(3/2)(s-1/2)$ for $s\in[1/2,1]$, $P\le(3/2)D$ and $D>71/7500$.

## Type-E consequence

**[PROVED EXACTLY, conditional on the retained isolated-center and safe-Walsh construction]** For $a_i=\|m_i\|^2$, $t_i=1-a_i$, $a_0=0$, define

$
T(a)=\frac12\sum_{0\le i<j\le20}$(t_it_j)^{-1/2}-1$
$

and let $K\ge0$ be the previously defined contact-sensitive safe-Walsh correction. The previous identity $D_{norm}\le(4/3)D_C+T(a)-K$, combined with the improved gap, yields

$
\boxed{D_C+\tfrac34T(a)>71/10000+\tfrac34K.}
$

Using the already proved sharp mass-only bound $\tfrac34T(a)\le(18\sqrt3-53/2)A$,

$
\boxed{D_C+$18\sqrt3-53/2$A>71/10000+\tfrac34K
\ge71/10000+\tfrac34[A_I^2/5-U_I]_+.}
$

The previous right-hand constant was (1/206). This is a strict improvement, but still no Type-E contradiction.

**[VERIFIED LOCALLY]** Rational branch margins and Gegenbauer algebra checked with a standalone SymPy/Fraction verifier. **[OPEN]** Type E, C, D, generic $e\ge27$, and non-isolated cases. Retain $M(F_3)\le89$, $M(P)\ge S/2-28/3$, $A\le383/504$, the six-core defect ceilings, and the Musin/Boyvalenkov zero-midpoint theorem. Sparse $e=23/24$ classification remains conditional on $\delta(G)\ge1$. **Global proved range: $40\le\tau_5\le44$.**
