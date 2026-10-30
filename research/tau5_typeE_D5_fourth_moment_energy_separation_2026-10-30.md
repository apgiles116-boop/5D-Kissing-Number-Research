# Type E: energy-sensitive D5 fourth-moment separation (2026-10-30)

**[PROVED EXACTLY — conditional on the retained isolated-center and midpoint hypotheses]**

Let the 20 normalized projected directions be \(u_i=z_i/\sqrt{1-a_i}\), where \(0\le a_i\le1/4\), \(A=\sum_i a_i\le383/504\), and the isolated unit center \(v\) satisfies \(|v\cdot z_i|\le1/2\). For any orthogonal transform, relabeling, and signs of the twenty D5 root lines \(r_i=(e_p\pm e_q)/\sqrt2\), put

\[
d=\max_i\|u_i u_i^T-r_i r_i^T\|_F.
\]

**Theorem.** Every such comparison satisfies

\[
\boxed{d\ge\sqrt2\left(\frac3{20}-\frac A{30}-\frac{A^2}{60}\right)
\ge\frac{1753391\sqrt2}{15240960}>0.16269.}
\]

This improves the previous exact-D5-template separation \(\sqrt2/15\), but **does not improve the full support-plane-fibre separation**: a pair of orthonormal lines can rotate within its support plane. Type E remains open.

## Proof

Write \(s_i=(v\cdot r_i)^2\), \(s_i'=(v\cdot u_i)^2\), and \(\varepsilon=d/\sqrt2\). Rank-one projector differences have operator norm equal to their Frobenius norm divided by \(\sqrt2\), hence \(|s_i-s_i'|\le\varepsilon\). Center safety gives \(s_i'\le1/[4(1-a_i)]\). For \(0\le a\le1/4\),

\[
\frac14+\frac a3-\frac1{4(1-a)}
=\frac{a(1-4a)}{12(1-a)}\ge0.
\]

Thus \(s_i\le1/4+a_i/3+\varepsilon\), and multiplication by \(s_i\ge0\) gives

\[
\sum_i s_i^2\le(1/4+\varepsilon)\sum_i s_i+\frac13\sum_i a_i s_i.
\]

The exact D5 moments are \(\sum_i s_i=4\) and
\(\sum_i s_i^2=3/2+\frac12\sum_{j=1}^5p_j^2\), where \(p_j=v_j^2\) and \(\sum p_j=1\). Sort \(p_1\ge\cdots\ge p_5\), and set \(t=p_1+p_2\). The largest squared D5 contact is
\(M=(\sqrt{p_1}+\sqrt{p_2})^2/2\le t\), so
\(\sum_i a_i s_i\le AM\le At\). By Cauchy–Schwarz,
\(\sum p_j^2\ge t^2/2+(1-t)^2/3\). Therefore

\[
\begin{aligned}
\varepsilon
&\ge\frac18+\frac18\left(\frac{t^2}{2}+\frac{(1-t)^2}{3}\right)-\frac{At}{12}\\
&=\frac3{20}-\frac A{30}-\frac{A^2}{60}
+\frac5{48}\left(t-\frac{2(1+A)}5\right)^2.
\end{aligned}
\]

Discard the nonnegative square. The remaining bound decreases with \(A\ge0\); at \(A=383/504\) it equals \(1753391/15240960\). QED.

**[OPEN]** To leverage this for general Type E, strengthen inverse Q-kernel stability from the full ten-angle support-plane fibre to the rigid D5 root template, using the 184 safe Walsh pairings. The six exceptional pairings are not identified with the six Q-kernel relations.

**[RETAINED]** Global \(40\le\tau_5\le44\). Type E, Types C/D, generic \(e\ge27\), and non-isolated branches remain open; sparse \(e=23,24\) classification requires \(\delta(G)\ge1\). Preserve \(M(F_3)\le89\), matching mass \(\ge2137/6\), and \(A\le383/504\).

Companion: tau5_typeE_D5_fourth_moment_energy_separation_2026-10-30_verify.py.
