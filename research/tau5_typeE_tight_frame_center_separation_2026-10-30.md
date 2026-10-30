# Type E: label-free separation from every 20-vector unit-norm tight frame

**Date:** 2026-10-30. **Global proved range unchanged: 40 <= tau_5 <= 44.**

## Proof status

- **[PROVED EXACTLY — standalone]** Let twenty selected deep edges be (x_i^\pm=m_i\pm z_i), with (m_i\cdot z_i=0), (a_i=\|m_i\|^2\in[0,1/4]), (A=\sum a_i), and isolated unit center (v) satisfying (|v\cdot x_i^\pm|\le1/2). Put (u_i=z_i/\sqrt{1-a_i}) and (s=\sum_{i,\pm}(v\cdot x_i^\pm)^2). For **any** twenty unit vectors (f_i\in\mathbb R^5) satisfying (\sum_i f_if_i^T=4I), define (d=\max_i\|u_iu_i^T-f_if_i^T\|_F). Whenever (L=s/2+A/3<4),
  [
  \boxed{d\ge \frac{\sqrt{10-L/2}-\sqrt{2L}}5.}
  ]
  This uses **no** D5 labeling, exceptional-pairing identification, interval enumeration, or uniqueness theorem.
- **[CONDITIONAL — retained Type-E center harmonic q bound]** If (q=s-36/5<-983/5000) and (A\le383/504), then **(d>1/46)**.
- **[CONDITIONAL — additionally retained 2026-10-28 harmonic (A<567/1000)]** Then **(d>1/37)**.
- **[CONDITIONAL — additionally retained signed-Gram atlas exclusion (s\ge209/30)]** If (s<209/30) and (A<567/1000), then **(d>1/34)**, stronger than the earlier (1/150) support-plane radius and valid for *every* twenty-vector unit-norm tight frame.
- **[OPEN]** Type E and the other unresolved branches remain open. The upstream harmonic and signed-Gram certificates are retained inputs, not re-proved by the terminal rational verifier.

## 1. Isolated-center contact bound

Write (p_i=v\cdot m_i), (r_i=v\cdot z_i). The two safe center contacts imply (|p_i\pm r_i|\le1/2), hence (|r_i|\le1/2). Since (1-a_i\ge3/4),
[
\begin{aligned}
\sum_i(v\cdot u_i)^2
 &=\sum_i\frac{r_i^2}{1-a_i}\\
 &=\frac s2-\sum_i p_i^2+\sum_i\frac{a_i r_i^2}{1-a_i}\\
 &\le\frac s2+\frac A3=L.\tag{1}
\end{aligned}
]
Thus the normalized frame (F_u=\sum_i u_iu_i^T), with trace 20, satisfies the **label-free variance floor**
[
\boxed{\|F_u-4I\|_F^2\ge\frac54(4-L)^2}\qquad(L<4).\tag{2}
]

## 2. Exact tight-frame comparison

Choose signs of (f_i) so (u_i\cdot f_i\ge0), and write
(u_i=\cos\theta_i f_i+\sin\theta_i g_i) with (g_i\perp f_i), (\|g_i\|=1). Then (\sin\theta_i\le d/\sqrt2), (\cos\theta_i\ge\sqrt{1-d^2/2}). Let (c_i=v\cdot f_i), (b_i=v\cdot g_i). Tightness gives
[
\sum_i c_i^2=4,\qquad \sum_i b_i^2\le\sum_i(1-c_i^2)=16.
]
Reverse triangle inequality in (\mathbb R^{20}) yields, for (d<\sqrt{2/5}),
[
\sqrt{\sum_i(v\cdot u_i)^2}
\ge 2\sqrt{1-d^2/2}-2\sqrt2\,d.
]
By (1),
[
L\ge4(\sqrt{1-d^2/2}-\sqrt2\,d)^2.\tag{3}
]
Solving this inequality gives the boxed formula. If (d\ge\sqrt{2/5}), that formula is automatic.

## 3. Three rational consequences

| Inputs | Exact upper bound for L | Certified exclusion |
|---|---:|---:|
| (q<-983/5000), (A\le383/504) | (7096963/1890000) | (d>1/46) |
| same q, (A<567/1000) | (36907/10000) | (d>1/37) |
| (s<209/30), (A<567/1000) | (11017/3000) | **(d>1/34)** |

In the last row, (2) also gives
[
\boxed{\left\|\sum_i(u_iu_i^T-I/5)\right\|_F^2>
\frac{966289}{7200000}\approx0.13420680556.}\tag{4}
]
The inequalities apply to any rotated/relabelled D5 root template and to its entire ten-support-plane fibre, since each is a 20-vector unit-norm tight frame.

**Exact verification:** For (n=46,37,34), set (x=1/(2n^2)). Using the rational bounds (\sqrt2<99/70) and (\sqrt{1-x}\ge1-x/2-x^2) (the latter follows by squaring and (x^2(7/4-x-x^2)\ge0)), the companion verifier proves
[
4(1-x/2-x^2-99/(70n))^2>L_{\rm cap}
]
using only `fractions.Fraction`. This rules out (d\le1/n) by (3), without floating-point certification decisions.

**Next proof target:** derive a matching upper bound on tight-frame distance or normalized Q-frame variance from the 184 safe Walsh pairings and six exceptional F3 contacts. No Type-E elimination or change in the global kissing-number range is claimed. Preserve (M(F_3)\le89), the stronger matching theorem (M(P)\ge S/2-28/3), and (A\le383/504); sparse graph classifications remain conditional on (\delta(G)\ge1).
