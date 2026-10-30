# Type E: label-free analytic separation from every 20-vector unit-norm tight frame

**Date:** 2026-10-30. **Global proved range unchanged: \(40\le\tau_5\le44\).**

## Proof status

- **[PROVED EXACTLY — standalone]** Let the twenty selected deep edges be \(x_i^\pm=m_i\pm z_i\), with \(m_i\cdot z_i=0\), \(a_i=\|m_i\|^2\in[0,1/4]\), \(A=\sum a_i\), and isolated unit center \(v\) satisfying \(|v\cdot x_i^\pm|\le1/2\). Set \(u_i=z_i/\sqrt{1-a_i}\), \(s=\sum_{i,\pm}(v\cdot x_i^\pm)^2\). For **any** twenty unit vectors \(f_i\in\mathbb R^5\) satisfying \(\sum_i f_if_i^T=4I\), define \(d=\max_i\|u_iu_i^T-f_if_i^T\|_F\). Whenever \(L=s/2+A/3<4\),
  \[
  \boxed{d\ge\frac{\sqrt{10-L/2}-\sqrt{2L}}5.}
  \]
  No D5 labeling, exceptional-pairing identification, interval enumeration, or uniqueness theorem is used.
- **[CONDITIONAL — retained Type-E center harmonic \(q\) bound]** With \(q=s-36/5<-983/5000\) and historical \(A\le383/504\), **\(d>1/46\)**.
- **[CONDITIONAL — additionally retained harmonic \(A<567/1000\)]** Then **\(d>1/37\)**.
- **[CONDITIONAL — additionally retained signed-Gram-atlas exclusion of \(s\ge209/30\)]** With \(s<209/30\), \(A<567/1000\), **\(d>1/34\)**, stronger than the earlier \(1/150\) support-plane radius and valid for *every* twenty-vector unit-norm tight frame.
- **[OPEN]** Type E and the other unresolved branches remain open. The upstream harmonic and signed-Gram certificates are retained inputs, not independently re-proved here.

## 1. Center-contact bound and normalized Q-frame anisotropy

Write \(p_i=v\cdot m_i\), \(r_i=v\cdot z_i\). The two safe center contacts give \(|p_i\pm r_i|\le1/2\), hence \(|r_i|\le1/2\). Since \(1-a_i\ge3/4\),

\[
\begin{aligned}
\sum_i(v\cdot u_i)^2
 &=\sum_i\frac{r_i^2}{1-a_i}\\
 &=\frac{s}{2}-\sum_i p_i^2+\sum_i\frac{a_i r_i^2}{1-a_i}\\
 &\le\frac{s}{2}+\frac{A}{3}=:L. \tag{1}
\end{aligned}
\]

The normalized frame operator \(F_u=\sum_i u_iu_i^T\) has trace 20. Trace-free matrix Cauchy gives, when \(L<4\),

\[
\boxed{\|F_u-4I\|_F^2\ge\frac54(4-L)^2.}\tag{2}
\]

## 2. Exact tight-frame comparison

Choose the sign of each \(f_i\) so \(u_i\cdot f_i\ge0\), and write
\(u_i=\cos\theta_i f_i+\sin\theta_i g_i\), with \(g_i\perp f_i\), \(\|g_i\|=1\). Then \(\sin\theta_i\le d/\sqrt2\), \(\cos\theta_i\ge\sqrt{1-d^2/2}\). Let \(c_i=v\cdot f_i\), \(b_i=v\cdot g_i\). Tightness gives

\[
\sum_i c_i^2=4,\qquad\sum_i b_i^2\le\sum_i(1-c_i^2)=16.
\]

The reverse triangle inequality in \(\mathbb R^{20}\) gives, for \(d<\sqrt{2/5}\),

\[
\sqrt{\sum_i(v\cdot u_i)^2}
\ge2\sqrt{1-d^2/2}-2\sqrt2\,d.
\]

Combining with (1) yields

\[
L\ge4\big(\sqrt{1-d^2/2}-\sqrt2\,d\big)^2. \tag{3}
\]

Solving (3) gives the boxed formula. If \(d\ge\sqrt{2/5}\), the formula holds trivially.

## 3. Three exact rational Type-E consequences

| Retained inputs | Exact strict cap for \(L\) | Excluded distance |
|---|---:|---:|
| \(q<-983/5000,\ A\le383/504\) | \(7096963/1890000\) | \(d>1/46\) |
| same \(q,\ A<567/1000\) | \(36907/10000\) | \(d>1/37\) |
| \(s<209/30,\ A<567/1000\) | \(11017/3000\) | **\(d>1/34\)** |

The third row also gives the **label-free normalized Q-variance floor**

\[
\boxed{\left\|\sum_i(u_iu_i^T-I/5)\right\|_F^2
>\frac{966289}{7200000}\approx0.13420680556.}\tag{4}
\]

Every rotated, relabeled or internally rotated D5 support-plane model is a twenty-vector unit-norm tight frame, so all three bounds apply to that entire fibre.

**Rational verification.** For \(n=46,37,34\), put \(x=1/(2n^2)\). The exact inequalities \(\sqrt2<99/70\) and \(\sqrt{1-x}\ge1-x/2-x^2\) (verified by \(x^2(7/4-x-x^2)\ge0\)) imply that the right side of (3) at \(d=1/n\) is at least

\[
4\big(1-x/2-x^2-99/(70n)\big)^2.
\]

The companion verifier uses only rational arithmetic to check that this strictly exceeds the corresponding \(L\)-cap. Thus \(d\le1/n\) is impossible; no floating-point certification decisions occur.

**Next step:** Obtain an incompatible upper bound on distance to a tight frame, or on normalized Q-frame variance, from the 184 safe Walsh pairings and six exceptional F3 contacts. No Type-E exclusion is claimed. Preserve \(M(F_3)\le89\), \(M(P)\ge S/2-28/3\), \(A\le383/504\), and the Musin/Boyvalenkov zero-midpoint theorem. Types C,D, generic \(e\ge27\), non-isolated branches remain open; sparse \(e=23,24\) classification retains \(\delta(G)\ge1\).
