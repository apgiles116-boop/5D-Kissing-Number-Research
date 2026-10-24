# Type E: isolated-center Q-frame spectral tradeoff and intrinsic D5 Gram gap

**2026-10-24.** **[PROVED EXACTLY]** Energy-sensitive center fourth-moment inequality, intrinsic Q-frame spectral tradeoff, and normalized Q-Gram separation from D5. **[OPEN]** Type E elimination and global improvement of the kissing-number bound.

## Correct two-sided isolated-center hypothesis

For the isolated deep-graph center u, every other kissing-code endpoint x satisfies $-1/2<u\cdot x\le1/2$. With $x_i^\pm=m_i\pm z_i$, $a_i=\|m_i\|^2\le1/4$, $A=\sum a_i\le B=383/504$, and $v_i=z_i/\sqrt{1-a_i}$, we have

$$|u\cdot m_i|+|u\cdot z_i|\le\frac12,\quad
q_i=(u\cdot v_i)^2\le\frac1{4(1-a_i)}\le\frac13.$$

The earlier one-sided positive hinge $((u\cdot z_i)^2-1/4)_+$ is identically zero here; see [audit](tau5_typeE_isolated_center_two_sided_audit_2026-10-24.md).

## 1. Energy-sensitive fourth-moment cap [PROVED EXACTLY]

For each selected deep edge,

$$q_i^2\le\frac{q_i}{4(1-a_i)}
=\frac{q_i}4+\frac{a_iq_i}{4(1-a_i)}
\le\frac{q_i}4+\frac{a_i}{16(1-a_i)^2}
\le\frac{q_i}4+\frac{a_i}{9}.$$

The final inequality uses $a_i\le1/4$. Therefore

$$\boxed{\sum_{i=1}^{20}(u\cdot v_i)^4
\le\frac14\sum_{i=1}^{20}(u\cdot v_i)^2+\frac A9.}\tag{1}$$

This is labeling-free and stronger than the uniform $\sum q_i^2\le(\sum q_i)/3$ when A is small.

## 2. Q-frame spectral tradeoff [PROVED EXACTLY]

Define the **normalized** trace-free columns $\widehat Q_i=v_iv_i^T-I/5$, their frame operator $F=\sum_i\widehat Q_i\otimes\widehat Q_i$ on $\mathrm{Sym}_0(5)$, $\Delta=\sum_i\widehat Q_i=\sum_i v_iv_i^T-4I$, and $U=uu^T-I/5$. Put $d=\langle\Delta,U\rangle=u^T\Delta u$. Then

$$\|U\|_F^2=\frac45,\quad \sum_iq_i=4+d,\quad
\sum_iq_i^2=\frac45+\frac25d+\langle U,FU\rangle.$$

Applying (1) yields the exact intrinsic inequality

$$\boxed{\langle U,FU\rangle+\frac3{20}\langle\Delta,U\rangle
\le\frac15+\frac A9.}\tag{2}$$

Consequently, with $\lambda_{\min}(F)$ the bottom eigenvalue on the 14-dimensional trace-free space,

$$\boxed{\lambda_{\min}(F)\le
\frac14+\frac{5A}{36}+\frac3{8\sqrt5}\|\Delta\|_F
\le\frac{6451}{18144}+\frac3{8\sqrt5}\|\Delta\|_F.}\tag{3}$$

Here $\|\Delta\|_F^2=2\sum_{i<j}(v_i\cdot v_j)^2-60$. Thus (3) directly couples the squared-correlation mass and normalized Q-frame spectrum. In particular, if $\Delta=0$, then $\lambda_{\min}(F)\le6451/18144\approx0.355545$, versus the exact D5 value 1.

## 3. Intrinsic normalized D5 Q-Gram separation [PROVED EXACTLY]

Let $K=(\langle\widehat Q_i,\widehat Q_j\rangle)_{i,j=1}^{20}$ and let $K_0$ be the D5 normalized Q-Gram under any relabeling. Its exact spectrum is $0^6,1^{10},(3/2)^4$, and $K_0\mathbf1=0$. Set $\varepsilon=\|K-K_0\|_{\rm op}$.

$$\boxed{\varepsilon>\frac13.}\tag{4}$$

**Proof.** The case $\varepsilon\ge1$ is immediate. For $\varepsilon<1$, Weyl and $\mathrm{rank}(K)\le14$ give $\mathrm{rank}(K)=14$ and $\lambda_{\min}(F)\ge1-\varepsilon$. Decompose coefficient space as $N=\ker K_0$ (dimension 6) and $R=N^\perp$ (dimension 14). Write

$$K=\begin{pmatrix}E&B^T\\ B&C\end{pmatrix}.$$

Then $C\succeq(1-\varepsilon)I$, $\|B\|_{\rm op}\le\varepsilon$, and the rank-14 Schur complement vanishes: $E=B^TC^{-1}B$. Since $\mathbf1\in N$,

$$\|\Delta\|_F^2=\mathbf1^TK\mathbf1
\le\frac{20\varepsilon^2}{1-\varepsilon}.$$

Using (3) gives

$$1-\varepsilon\le\frac{6451}{18144}
+\frac34\frac{\varepsilon}{\sqrt{1-\varepsilon}}.$$

If $0\le\varepsilon\le1/3$, the left side is at least $2/3$, while the right side is at most $6451/18144+\sqrt6/8<2/3$. The strict comparison is exact:

$$\left(\frac23-\frac{6451}{18144}\right)^2-\frac6{64}
=\frac{1003081}{329204736}>0.$$

Contradiction. Thus (4) holds for **every labeling**, without assuming the actual directions have D5 contact structure. This is an intrinsic Gram separation, not an elimination of Type E. Any independently audited stronger intrinsic gap remains stronger.

## Proof-status ledger

**[PROVED EXACTLY]** (1)–(4), all exact-rational spectral comparisons, and the rank-14 Schur complement argument.

**[RETAINED TYPE E]** $M(F_3)\le89$, $M(P)\ge S/2-28/3$, $A\le383/504$, 184 safe plus six exceptional pairings. No regression to older constants.

**[OPEN]** A six-exception polynomial/rank-five inequality that conflicts with (3), Type E elimination, Types C/D and generic $e\ge27$. Global proved range remains $40\le\tau_5\le44$.

**Next:** exploit the safe-pair/core structure to bound the normalized Q-frame bottom eigenvalue and tight-frame variance, then combine with (3). Distinguish normalized $\widehat Q_i$ from the unnormalized $Q_i=z_iz_i^T-(1-a_i)I/5$.