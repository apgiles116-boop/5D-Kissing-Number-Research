# Type E: rational six-exception flex retaining the exact D5 covering radius

Date: 2026-10-27. **[PROVED EXACTLY — finite twenty-line geometry]** This strengthens the earlier six-exception flex note. **[OPEN]** It is not a Type-E elimination.

Start with the twenty D5 projective roots $(e_i\pm e_j)/\sqrt2$, $1\le i<j\le5$. Deform only the four roots $r_j=(e_1-e_j)/\sqrt2$, $j=2,3,4,5$, by
$$
w_j=(e_1+e_j-\sum_{k=2,k\ne j}^5e_k)/\sqrt2,\qquad
u_j(t)=(r_j+t w_j)/\sqrt{1+5t^2/2}.
$$
Keep the other sixteen roots fixed. Choose the rational normalization point
$$
t=32/639,\qquad \sqrt{1+5t^2/2}=641/639.
$$
There are **exactly six** projective threshold violations, the four-core K4, and all other **184** pairs have coherence at most $1/2$. The six common core correlations are $491137/821762$. The exact homogeneous positive defect is $108588534912/168823196161\approx0.6432086193$, and the raw positive defect is $6548310868293483692832/28501271562015485137921\approx0.2297550428$. Both are below the retained Type-E necessary caps $5792292955405/4129544208384$ and $1780062775/4032758016$, respectively.

## [PROVED EXACTLY] Sharp covering radius

For these twenty unit directions,
$$
\boxed{\min_{\|x\|=1}\max_i |x\cdot u_i|=\sqrt{2/5}.}
$$
This equals the original D5 covering radius, **despite** the nonzero six-exception deformation.

**Exact polytope certificate:** Write $v_i=\sqrt2 u_i$ and $P=\{x:|v_i\cdot x|\le1\ \forall i\}$. The geometry is invariant under permutations of coordinates 2--5. Restrict to $x=(s,y_1,y_2,y_3,y_4)$ with $y_1\le y_2\le y_3\le y_4$. All forty inequalities reduce exactly to fourteen:

- Three order constraints $y_j-y_{j+1}\le0$.
- Three D4 constraints $-y_1-y_2\le1,\ y_3+y_4\le1,\ y_4-y_1\le1$.
- Four constraints $|s+y_1|\le1,\ |s+y_4|\le1$.
- Four constraints $|671s-32\sum y_k-575y_1|\le641,\ |671s-32\sum y_k-575y_4|\le641$.

The reduction is exact because the forms are monotone in ordered $y_j$, and $2t-1<0$. Exhaustive rational enumeration of all $\binom{14}{5}=2002$ five-facet systems gives 800 nonsingular systems and **26 distinct feasible vertices**. Their squared norms are at most $5/4$, with equality at six vertices, including $(1/2,1/2,1/2,1/2,1/2)$. The polytope is bounded; the convex squared norm attains its maximum at a vertex. Permutation invariance proves $\max_P\|x\|^2=5/4$, hence the exact covering radius above. The companion SymPy script verifies all assertions without floating-point arithmetic.

## [PROVED EXACTLY — conditional on isolated-center safety]

In a genuine isolated-center Type-E realization, both kissing upper bounds and the center's absence of deep edges give $|x_0\cdot z_i|\le1/2$. Writing $z_i=\sqrt{1-a_i}u_i$ with $a_i\le1/4$ gives $|x_0\cdot u_i|\le1/\sqrt3$. But the covering theorem forces some $|x_0\cdot u_i|\ge\sqrt{2/5}>1/\sqrt3$. Therefore **this specific rational twenty-line deformation cannot be extended to a valid isolated-center Type E**, even though it obeys the 184 safe pairings and both defect budgets. More quantitatively, an extension would require $a_i\ge3/8$ for at least one edge, contradicting $a_i\le1/4$.

## [OPEN] Proof ledger

This is a reduced-system counterexample and conditional obstruction, **not a label-free Type-E theorem**. Retain $40\le\tau_5\le44$; Type E $1/49<A\le383/504$, $M(F_3)\le89$, matching $M(P)\ge S/2-28/3$, twenty-edge mass $\ge2137/6$, raw squared-correlation floor $\ge8790283/317520$. Types C, D, E, generic $e\ge27$, and non-isolated branches remain open. Sparse $e=23,24$ classification assumes $\delta(G)\ge1$.

Companion exact verifier: research/tau5_typeE_rational_flex_exact_covering_2026-10-27_verify.py.
