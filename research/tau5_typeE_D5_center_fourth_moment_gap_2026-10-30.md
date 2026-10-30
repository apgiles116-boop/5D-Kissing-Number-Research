# Type E: exact D5 center covering and fourth-moment separation
Date: 2026-10-30

**[PROVED EXACTLY — conditional on D5 geometry]** Twenty normalized projected directions exactly forming the D5 root-line system cannot coexist with an isolated center when the deep-edge midpoint energies satisfy \(a_i\le1/4\). This does **not** eliminate general Type E.

**[PROVED EXACTLY — universal quantitative separation]** Any normalized twenty-line configuration compatible with an isolated center and \(a_i\le1/4\) is at projective Frobenius max-distance at least \(\sqrt2/15\) from every rotated, relabeled D5 template.

## 1. Isolated-center consequence

Write \(x_i^\pm=m_i\pm z_i\), \(\|x_i^\pm\|=1\), \(a_i=\|m_i\|^2\), \(w_i=\|z_i\|^2=1-a_i\), \(u_i=z_i/\sqrt{w_i}\). A deep selected edge has \(x_i^+\cdot x_i^-=2a_i-1\le-1/2\), so \(a_i\le1/4\), \(w_i\ge3/4\).

If \(v\) is the isolated center, both \(v\cdot x_i^\pm\in(-1/2,1/2]\), hence
\[
|v\cdot m_i|+|v\cdot z_i|=\max(|v\cdot x_i^+|,|v\cdot x_i^-|)\le1/2.
\]
In particular, for all twenty directions,
\[
t_i=(v\cdot u_i)^2\le\frac{1}{4w_i}\le\frac13. \tag{1}
\]

## 2. D5 second and fourth moments

For the twenty D5 projective lines choose
\[
r_{pq}^{\pm}=(e_p\pm e_q)/\sqrt2,\qquad 1\le p<q\le5.
\]
For any unit \(v=(v_1,\ldots,v_5)\), put \(s_{pq}^{\pm}=(v\cdot r_{pq}^{\pm})^2\). Exact expansion yields
\[
\sum s_i=4,\qquad
\sum s_i^2=\frac32+\frac12\sum_{p=1}^5v_p^4\ge\frac85. \tag{2}
\]
Equality in the last inequality requires \(|v_p|=1/\sqrt5\) for every \(p\).

Consequently, the fourth-moment polynomial obeys
\[
\Phi_{D5}(v)=\sum_i(s_i^2-s_i/3)
=\frac16+\frac12\sum_pv_p^4\ge\frac4{15}. \tag{3}
\]
But for any center-compatible normalized directions satisfying (1),
\[
\Phi_u(v)=\sum_i(t_i^2-t_i/3)\le0. \tag{4}
\]
Thus the exact D5 configuration is incompatible with an isolated center even if all twenty projected lengths are allowed to shrink to \(\sqrt{3/4}\). The polynomial gap is at least \(4/15\).

## 3. Sharp D5 covering constant

**[PROVED EXACTLY]** For every unit \(v\),
\[
\max_{p<q,\pm}|v\cdot r_{pq}^{\pm}|\ge\sqrt{2/5}. \tag{5}
\]
The bound is sharp for \(|v_p|=1/\sqrt5\).

Proof: Sort the coordinate magnitudes \(x_1\ge\cdots\ge x_5\ge0\). The maximum D5 correlation is \((x_1+x_2)/\sqrt2\). Let \(s=x_1+x_2\), \(t=x_2\in[0,s/2]\). Then
\[
1=\sum x_p^2\le(s-t)^2+4t^2
\le\max\{s^2,5s^2/4\}=5s^2/4,
\]
where the last inequality is convexity in \(t\). Thus \(s\ge2/\sqrt5\).

If \(u_i=r_i\), the root attaining (5) satisfies
\[
|v\cdot z_i|^2=w_i|v\cdot r_i|^2\ge(3/4)(2/5)=3/10>1/4,
\]
contradicting isolated-center safety. The squared excess is at least \(1/20\).

## 4. Uniform projective distance from D5

Fix any ambient rotation, sign choices and bijective labeling of the D5 roots \(r_i\). For the actual isolated center \(v\), choose \(k\) with \((v\cdot r_k)^2\ge2/5\). Equation (1) gives \((v\cdot u_k)^2\le1/3\), so
\[
\left|v^T(r_kr_k^T-u_ku_k^T)v\right|\ge1/15.
\]
For unit rank-one projectors the Frobenius norm of their difference is \(\sqrt2\) times its operator norm. Hence
\[
\boxed{\max_i\|u_iu_i^T-r_ir_i^T\|_F\ge\sqrt2/15.} \tag{6}
\]
This holds for **every** rotated/relabelled D5 template, not just a preferred labeling.

There is also an aggregate displacement certificate. Since \(f(t)=t^2-t/3\) is \(5/3\)-Lipschitz on \([0,1]\), (3)-(4) imply
\[
\sum_i|s_i-t_i|\ge4/25,\qquad
\sum_i\|u_iu_i^T-r_ir_i^T\|_F\ge4\sqrt2/25. \tag{7}
\]

## 5. What is and is not proved

**[PROVED EXACTLY]** Equations (1)-(7), sharp D5 covering, the \(4/15\) fourth-moment gap, and uniform projective separation \(\sqrt2/15\).

**[VERIFIED BY EXACT ARITHMETIC]** SymPy expansion of all twenty roots, sharp equality examples, and 3124 nonzero integer-vector test directions. The algebraic proofs, not the finite tests, establish the universal statements.

**[OPEN]** To eliminate Type E, derive a quantitative *inverse* Q-kernel/Walsh stability estimate controlling the distance to D5 by the actual raw safe constraints, midpoint budget \(A\le383/504\), and the global/cycle Q residuals. The six Q-kernel relations plus the 184 *normalized* projective constraints characterize D5 in the earlier exact-fibre theorem; those normalized \(1/2\) constraints are **not** automatically available for nonzero midpoints. No contradiction with \(A\le383/504\) is claimed.

**[RETAINED]** Global \(40\le\tau_5\le44\). Type E \(M(F_3)\le89\), matching \(M(P)\ge S/2-28/3\), twenty-edge mass \(\ge2137/6\), \(A\le383/504\); zero-midpoint 21-line exclusion by Musin/Boyvalenkov. Types C, D, generic \(e\ge27\), non-isolated branches remain open; sparse \(e=23,24\) classification is conditional on \(\delta(G)\ge1\).
