# Type E: sharp D5 quartic-excess theorem and isolated-center Q-tensor separation

Date: 2026-10-27. Continuation of the consolidated 2026-09-05 ledger and the 2026-10-27 D5 covering obstruction.

## Proof status

**[PROVED EXACTLY — ABSTRACT D5]** For the 20 D5 projective root lines $d_{pq}^{\pm}=(e_p\pm e_q)/\sqrt2$, every unit $x\in\mathbb R^5$, and every $0\le c\le2/5$,

$$
\boxed{\sum_{i=1}^{20}\left[((x\cdot d_i)^2-c)_+\right]^2\ge10(2/5-c)^2.}\tag{1}
$$

This is **sharp**, with equality at $x=(\pm1,\ldots,\pm1)/\sqrt5$. At $c=1/4$ the right side is $9/40$; at $c=1/3$ it is $2/45$.

**[PROVED EXACTLY — TYPE-E ISOLATED CENTER]** Let $u_i=z_i/\sqrt{1-a_i}$ be the 20 normalized selected deep-edge directions, with $a_i=\|m_i\|^2\le1/4$, $A=\sum_i a_i\le383/504$, and isolated center $x_0$. Compare the $u_i$ with **any** rotated, relabeled, projectively signed D5 template $d_i$. Define $\theta_i=\arccos|u_i\cdot d_i|$. Then

$$
\boxed{\sqrt{\sum_i\sin^2\theta_i}\ge\frac3{\sqrt{40}}-\frac{\sqrt A}{6},
\qquad \sum_i\sin^2\theta_i>\frac1{10}.}\tag{2}
$$

For $Q(v)=vv^T-I_5/5$, it follows that

$$
\boxed{\sum_i\|Q(u_i)-Q(d_i)\|_F^2>\frac15.}\tag{3}
$$

At $A=383/504$, the stronger bound in (2) is $\sum\sin^2\theta_i\ge0.108275616377598\ldots$, forcing some angular mismatch of at least $4.2195448718\ldots^\circ$. This strengthens the earlier pointwise $3.9671^\circ$ D5 separation and supplies an aggregate second-order Q-tensor barrier.

## Exact proof of the sharp D5 inequality

For $t_i=(x\cdot d_i)^2$, direct expansion over the two signs of each root pair yields

$$
\sum_i t_i=4,\qquad
\sum_i t_i^2=\frac32+\frac12\sum_{p=1}^5x_p^4\ge\frac85.\tag{4}
$$

Set $h=2/5$ and, for $0\le c\le h$, define

$$
q_c(t)=(1-c^2/h^2)t^2-2c(1-c/h)t.
$$

For $t\ge c$, $(t-c)^2-q_c(t)=(c^2/h^2)(t-h)^2\ge0$. For $0\le t\le c$, convexity and $q_c(0)=0$, $q_c(c)=-(c^2/h^2)(c-h)^2\le0$ imply $q_c(t)\le0$. Thus $[(t-c)_+]^2\ge q_c(t)$ for all $t\ge0$. Sum and use (4) to obtain (1). The equal-absolute-coordinate unit vector has ten $t_i=2/5$ and ten $t_i=0$, establishing equality. For $c=1/4$ the pointwise certificate is

$$
[(t-1/4)_+]^2\ge\frac{39}{64}t^2-\frac3{16}t.
$$

## Exact isolated-center separation

The two endpoints $m_i\pm z_i$ both have correlations with the isolated center $x_0$ in $[-1/2,1/2]$. Hence $|x_0\cdot z_i|+|x_0\cdot m_i|\le1/2$. With $s_i=(x_0\cdot u_i)^2$,

$$
s_i\le\frac1{4(1-a_i)}\le\frac14+\frac{a_i}{3}.\tag{5}
$$

For $t_i=(x_0\cdot d_i)^2$, the rank-one projector identity gives

$$
|t_i-s_i|\le\|u_iu_i^T-d_id_i^T\|_{\mathrm{op}}=\sin\theta_i.
$$

Therefore $(t_i-1/4)_+\le\sin\theta_i+a_i/3$. Apply (1) at $c=1/4$, the Euclidean triangle inequality, and $\sum a_i^2\le A/4$ to prove (2). Since $A\le383/504<9/10$, its right-hand side is strictly greater than $1/\sqrt{10}$. Finally, $\|Q(u_i)-Q(d_i)\|_F^2=2\sin^2\theta_i$, proving (3).

## Interpretation and unchanged ledger

**[OPEN]** This is a *necessary D5 separation*, not an exclusion of Type E. No upper bound on the optimally aligned Q-tensor distance has been obtained from the six-exception/homogeneous-defect constraints. The squared-correlation floor is a Welch/frame lower bound, not a D5-closeness theorem. No identification of the six exceptional pairings with the six D5 Q-kernel relations is asserted.

Retain Type E $H=16K_2+F_3$, star $\le70/3$, $M(F_3)\le89$, $M(P)\ge S/2-28/3$, twenty-edge mass $\ge2137/6$, and $1/49<A\le383/504$. Retain the Musin/Boyvalenkov zero-midpoint exclusion. Type C C7, Type D, generic $e\ge27$, and non-isolated branches remain open; sparse $e=23,24$ classification requires $\delta(G)\ge1$. **Global proved range: $40\le\tau_5\le44$.**
