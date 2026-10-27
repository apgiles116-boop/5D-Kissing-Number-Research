# Type E: sharp D5 quartic-excess theorem and isolated-center Q-tensor separation

Date: 2026-10-27. Continuation of the consolidated 2026-09-05 ledger and the 2026-10-27 exact-D5 covering obstruction. Full working note and exact SymPy verifier are also available as conversation artifacts.

## Proof-status ledger

**[PROVED EXACTLY — ABSTRACT D5]** For the 20 D5 projective root lines (d_{pq}^{\pm}=(e_p\pm e_q)/\sqrt2), every unit (x\in\mathbb R^5), and every (0\le c\le2/5),

[
\sum_{i=1}^{20}\big[((x\cdot d_i)^2-c)_+\big]^2\ge10(2/5-c)^2. \tag{1}
]

This is **sharp**, with equality at (x=(\pm1,\ldots,\pm1)/\sqrt5). In particular, the right side is (9/40) for (c=1/4) and (2/45) for (c=1/3).

**[PROVED EXACTLY — TYPE-E ISOLATED CENTER]** For the 20 normalized selected deep-edge directions (u_i=z_i/\sqrt{1-a_i}), where (a_i=\|m_i\|^2\le1/4), (A=\sum a_i\le383/504), and (x_0) is an isolated center, compare (u_i) with **any** rotated, relabeled, sign-chosen D5 template (d_i). Put (θ_i=\arccos|u_i\cdot d_i|). Then

[
\sqrt{\sum_i\sin^2\theta_i}\ge\frac3{\sqrt{40}}-\frac{\sqrt A}{6},
\quad
\sum_i\sin^2\theta_i>\frac1{10}. \tag{2}
]

Consequently, for (Q(v)=vv^T-I_5/5),

[
\sum_i\|Q(u_i)-Q(d_i)\|_F^2>\frac15. \tag{3}
]

At the maximal permitted (A=383/504), (2) yields (\sum\sin^2\theta_i\ge0.108275616377598\ldots), so some line differs by at least (4.2195448718\ldots^\circ). This strengthens the previous single-line (3.9671^\circ) separation and provides an aggregate second-order Q-tensor barrier.

## Exact derivation

Let (t_i=(x\cdot d_i)^2). The D5 identities are

[
\sum_i t_i=4,\qquad
\sum_i t_i^2=\frac32+\frac12\sum_{p=1}^5x_p^4\ge\frac85. \tag{4}
]

Write (h=2/5). For (0\le c\le h) define

[
q_c(t)=(1-c^2/h^2)t^2-2c(1-c/h)t.
]

For (t\ge c), ((t-c)^2-q_c(t)=(c^2/h^2)(t-h)^2\ge0). For (0\le t\le c), convexity and (q_c(0)=0), (q_c(c)=-(c^2/h^2)(c-h)^2\le0) imply (q_c(t)\le0). Thus ([(t-c)_+]^2\ge q_c(t)) for all (t\ge0). Sum over (4) to obtain (1). The all-equal-absolute-coordinate vector has ten (t_i=2/5) and ten (t_i=0), proving sharpness.

For the isolated center, both endpoints (m_i\pm z_i) have correlations with (x_0) in ([-1/2,1/2]), so (|x_0\cdot z_i|+|x_0\cdot m_i|\le1/2). Therefore, for (s_i=(x_0\cdot u_i)^2),

[
s_i\le\frac1{4(1-a_i)}\le\frac14+\frac{a_i}{3}. \tag{5}
]

Let (t_i=(x_0\cdot d_i)^2). The rank-one projector difference satisfies
(|t_i-s_i|\le\|u_iu_i^T-d_id_i^T\|_{op}=\sin\theta_i). Hence
((t_i-1/4)_+\le\sin\theta_i+a_i/3). Apply (1) at (c=1/4), Minkowski, and (∑a_i^2\le A/4) to get (2). Since (A\le383/504<9/10), the right side of (2) is strictly greater than (1/\sqrt{10}). Finally (‖Q(u_i)-Q(d_i)‖_F^2=2\sin^2\theta_i), proving (3).

## Interpretation and limitations

**[OPEN]** No upper bound on the optimally aligned D5 Q-tensor distance has been derived from the six-exception/homogeneous-defect constraints. The global squared-correlation floor is a frame/Welch lower bound and does not establish D5 proximity. No identification between the six exceptional pairings and the six D5 Q-kernel relations is asserted.

Retain: Type E (H=16K_2+F_3), exact star bound (70/3), (M(F_3)\le89), (M(P)\ge S/2-28/3), 20-edge mass (\ge2137/6), and (1/49<A\le383/504). Musin/Boyvalenkov zero-midpoint boundary exclusion remains. Type C C7, Type D, generic (e\ge27), and non-isolated branches remain open. Sparse (e=23,24) classification remains conditional on (\delta(G)\ge1). **Global proved range (40\le\tau_5\le44)**.
