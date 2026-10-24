# Type E: isolated-center two-sided cap and D5 fourth-moment audit

**2026-10-24.** **[PROVED EXACTLY]** Isolated-center two-sided cap, fourth-moment upper bound, and D5 moment identities. **[TEMPLATE CONDITIONAL]** D5 covering exclusion and projector separation. **[OPEN]** Type E elimination and an intrinsic, labeling-free Q-Gram contradiction.

## 1. Critical logical correction [PROVED EXACTLY]

In the isolated-center branch of the deep graph, the center u has no deep neighbors. Therefore every other kissing-code point x satisfies

$$-\frac12<u\cdot x\le\frac12.$$

For the endpoints of a selected deep edge, $x_i^\pm=m_i\pm z_i$, this gives

$$|u\cdot m_i|+|u\cdot z_i|\le\frac12.$$

Write $a_i=\|m_i\|^2\le1/4$, $t_i=(u\cdot z_i)^2$, and $v_i=z_i/\sqrt{1-a_i}$. Then

$$t_i\le\frac14,\qquad q_i=(u\cdot v_i)^2=\frac{t_i}{1-a_i}\le\frac1{4(1-a_i)}\le\frac13.$$

Equality in the first inequality is allowed if one center-to-endpoint contact is exactly $+1/2$. The one-sided center-hinge $(t_i-1/4)_+$ is therefore **identically zero** for actual isolated-center Type E. Although its previously optimized coefficient is correct in a larger one-sided subsystem, that route cannot produce a positive Type-E energy lower bound. Its polynomial Q-corollary is likewise vacuous here.

The previously quoted counterexample $u=(1,0)$, $m=(-1/4,\sqrt3/4)$, $z=(3/4,\sqrt3/4)$ has $u\cdot(m-z)=-1$; the center has a deep neighbor and is **not isolated**. It does not refute the two-sided cap. The earlier D5 hinge result based on $|u\cdot z_i|\le1/2$ can be restored as applicable to the isolated-center branch, subject to its remaining hypotheses.

## 2. Labeling-free fourth-moment upper bounds [PROVED EXACTLY]

For twenty selected edges,

$$\sum_i t_i^2\le\frac14\sum_i t_i,\qquad
\sum_i q_i^2\le\frac13\sum_i q_i.$$

In intrinsic Q notation, $t_i=(1-a_i)/5+\langle Q_i,U\rangle$ with $U=uu^T-I/5$. These are exact necessary constraints on the center fourth moment. They point in the **opposite direction** to the fourth-moment lower bound required for a Type-E contradiction.

## 3. D5 covering and moment gap [PROVED EXACTLY, TEMPLATE CONDITIONAL]

For the twenty normalized D5 lines $w_{ij}^\pm=(e_i\pm e_j)/\sqrt2$, put $p_{ij}^\pm=(u\cdot w_{ij}^\pm)^2$. The exact moments are

$$\sum p=4,\qquad
\sum p^2=\frac32+\frac12\sum_{j=1}^5u_j^4\ge\frac85.$$

Thus

$$\sum p^2-\frac13\sum p
=\frac4{15}+\frac12\sum_j(u_j^2-\tfrac15)^2\ge\frac4{15}.$$

In particular $\max p\ge(\sum p^2)/(\sum p)\ge2/5$ (sharp at balanced $|u_j|=1/\sqrt5$). An actual isolated-center deep edge has $q_i\le1/3$. Therefore the twenty normalized projected directions cannot coincide with any rotated/relabelled D5 template: a D5 line with $p\ge2/5$ would require

$$a_i\ge1-\frac1{4p}\ge\frac38>\frac14.$$

This excludes **exact normalized D5 labeling**, not arbitrary Type E.

## 4. Sharp D5 cap-hinge SOS [PROVED EXACTLY, TEMPLATE CONDITIONAL]

For $0\le p\le1$,

$$(p-\tfrac13)_+^2\ge\frac{11}{36}p^2-\frac19p.$$

The nonnegative remainder is $p(4-11p)/36$ for $p\le1/3$ and $(5p-2)^2/36$ for $p\ge1/3$. Hence

$$\sum_{\mathrm{D5}}(p_i-\tfrac13)_+^2
=\frac2{45}+\frac{11}{72}\sum_j(u_j^2-\tfrac15)^2+\sum_i R(p_i)
\ge\frac2{45}.$$

Equality holds for balanced u (ten $p_i=2/5$ and ten $p_i=0$). If $P_i=v_iv_i^T$ are any actual normalized projectors obeying $q_i\le1/3$ and $P_i^0=w_iw_i^T$ are an aligned D5 template, the rank-two projector norm identity yields

$$\sum_i\|P_i-P_i^0\|_F^2
\ge2\sum_i(p_i-\tfrac13)_+^2\ge\frac4{45}.$$

The SOS lower bound $2/45$ is sharp; the projector separation $4/45$ is not claimed sharp and is **extrinsic**, not intrinsic Q-Gram separation.

## 5. Proof ledger and next obligation

- **[PROVED EXACTLY]** Two-sided center cap, normalized cap $q_i\le1/3$, and fourth-moment upper bounds.
- **[PROVED EXACTLY, TEMPLATE CONDITIONAL]** D5 moment gap $4/15$, exact D5 exclusion, sharp SOS $2/45$, and projector separation $4/45$.
- **[OPEN]** Derive a labeling-free fourth-moment lower bound exceeding $(1/3)\sum q_i$ using the 184 safe pairings, six exceptional core pairings, and rank-five geometry. No global D5 labeling is assumed.
- **[RETAINED]** $M(F_3)\le89$, $M(P)\ge S/2-28/3$, $A\le383/504$, Types C/D and generic $e\ge27$ open, and $40\le\tau_5\le44$ unchanged.

The crucial correction is to impose **both** inequalities at an isolated center before optimizing any center hinge.