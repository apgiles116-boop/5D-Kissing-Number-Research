# Type E: exact D5 Q-kernel fibre classification and quantitative leakage
Date: 2026-10-30

**[PROVED EXACTLY — conditional structural theorem; Type E remains OPEN]**

## Setup

Label twenty unit directions \(u_{pq}^{\pm}\in\mathbb R^5\) by the ten edges \(pq\) of \(K_5\), two directions per edge. Put four distinguished core directions on one line of each support \(0i\), \(i=1,\ldots,4\). All 184 other line pairings are projectively safe; only the six core-core line pairings may be exceptional. This is a *combinatorial labeling*, not an assumed geometric D5 alignment.

Write \(S_{pq}=u_{pq}^+(u_{pq}^+)^T+u_{pq}^-(u_{pq}^-)^T\), \(F=\sum_{pq}S_{pq}\), \(t_{pq}=u_{pq}^+\cdot u_{pq}^-\), and \(Q_i=u_i u_i^T-I/5\). Let \(K_{ij}=\operatorname{tr}(Q_iQ_j)\), \(P_c\) be the rank-five D5 cycle projector, \(C=\operatorname{tr}(P_cK)\), and \(V=\|\sum_iQ_i\|_F^2=\|F-4I\|_F^2\). The six D5 kernel relations vanish exactly when \(C=V=0\).

## Universal exact reconstruction

For any twenty unit directions with these labels, set
\[
B_p=\frac13\sum_{q\ne p}S_{pq}-\frac{2}{15}F+\frac15I,\qquad
E_{pq}=S_{pq}-B_p-B_q.
\]
Then \(\sum_pB_p=I\), \(\operatorname{tr}B_p=1\), and the exact unsigned-incidence projection gives
\[
\boxed{\sum_{pq}\|E_{pq}\|_F^2=2C+\frac{V}{10}=:\rho^2.}\tag{1}
\]
Let \(O=\sum_{pq}t_{pq}^2\), \(R_{pq}=S_{pq}^2-S_{pq}\), and \(D_{pq}=(B_p+B_q)^2-(B_p+B_q)\). Direct expansion yields
\[
R_{pq}=t_{pq}\bigl(u_{pq}^+(u_{pq}^-)^T+u_{pq}^-(u_{pq}^+)^T\bigr),
\quad \sum\|R_{pq}\|_F^2\le4O,
\]
\[
B_p^2-B_p=\sum_{q\ne p}D_{pq}-\frac13\sum_{ij}D_{ij}.\tag{2}
\]
The \(5\times10\) coefficient matrix in (2) satisfies \(LL^T=3I-(5/9)J\), so \(\|L\|_{\rm op}=\sqrt3\). Also \(\|S_{pq}\|_{\rm op}\le2\) and
\(\|D_{pq}\|_F\le\|R_{pq}\|_F+5\|E_{pq}\|_F+\|E_{pq}\|_F^2\).
Consequently,
\[
\boxed{\left(\sum_p\|B_p^2-B_p\|_F^2\right)^{1/2}
\le\sqrt3\left(2\sqrt O+5\rho+\rho^2\right).}\tag{3}
\]
This gives an unconditional quantitative reconstruction of five approximate coordinate projections, without assuming D5 alignment.

## New exact-fibre classification

**THEOREM [PROVED EXACTLY].** If \(C=V=0\) and all 184 nonexceptional line pairs satisfy \(|u_i\cdot u_j|\le1/2\), then the twenty lines are exactly the twenty D5 root lines, up to one ambient orthogonal transformation, projective signs, and swaps within supports. In particular the six exceptional core pairings are automatically safe.

**Proof.** Equation (1) gives \(E_{pq}=0\), hence \(S_{pq}=B_p+B_q\). For each support \(e=pq\), the six meeting supports obey
\[
\sum_{f\sim e}S_f=S_e+2I,\qquad
\sum_{f\sim e}\operatorname{tr}(S_eS_f)=6+2t_e^2.\tag{4}
\]
For each nonstar support \(e=ij\), \(1\le i<j\le4\), all 24 cross-line pairings with its six meeting supports are safe. Each of the six cross-support traces is the sum of four squared correlations, at most one. Thus (4) forces \(t_e=0\), all six traces equal one, and all 24 squared correlations equal \(1/4\).

Hence each nonstar \(S_e\) is a rank-two orthogonal projector. As \(F=4I\),
\[
8=\operatorname{tr}(S_eF)=2+6+\sum_{f\perp_{\rm support}e}\operatorname{tr}(S_eS_f).
\]
Every disjoint-support term is nonnegative, hence zero. In particular complementary nonstar supports \(ij,kl\), partitioning \(\{1,2,3,4\}\), give orthogonal rank-two projectors. Their sum
\[
T=S_{ij}+S_{kl}=\sum_{r=1}^4B_r=I-B_0
\]
is a rank-four orthogonal projector; thus \(B_0\) is rank-one orthogonal projection.

For \(i=1,\ldots,4\), the identity
\(2B_i=\sum_{j\in\{1,2,3,4\},j\ne i}S_{ij}-T\)
shows \(B_i\) is supported on \(\operatorname{ran}T\). Since \(S_{0i}=B_0+B_i\) is positive semidefinite, has rank at most two, and trace two, while \(B_0\) is a rank-one projection orthogonal to \(B_i\), each \(B_i\) must also be a rank-one projection. The five projections sum to \(I\), so are mutually orthogonal.

Thus every \(S_{pq}=B_p+B_q\) is the orthogonal projector onto a coordinate two-plane, and its two unit directions form an orthonormal basis. Each support meets a nonstar support in one coordinate, and all four cross-line squared correlations for that meeting equal \(1/4\). The \(2\times2\) cross-Gram is an outer product of the two shared-coordinate component vectors. Four entries of magnitude \(1/2\) force both bases to be balanced, yielding precisely the two D5 root lines on each support. QED.

**Important scope:** The theorem concerns *unit* directions at the threshold \(1/2\). In Type E, normalized \(z_i\) need not satisfy that threshold when \(a_i>0\). It is therefore not a Type-E exclusion.

## Explicit midpoint-dependent leakage

For Type E, put \(w_i=\|z_i\|^2=1-a_i\ge3/4\), \(u_i=z_i/\sqrt{w_i}\). Define \(\rho^2=2C_u+V_u/10\) from these unit directions. For each nonstar support \(e\), all 24 raw projected correlations with its six meeting supports satisfy \(|z_i\cdot z_j|\le1/2\). Since
\(1/(w_iw_j)-1\le(16/9)(a_i+a_j)\)
and
\[
\sum_{f\sim e}S_f=S_e+2I+\sum_{f\sim e}E_f-E_e,
\]
Cauchy-Schwarz gives \(\|\sum_{f\sim e}E_f-E_e\|_F\le\sqrt7\rho\). Therefore, writing \(A_e=a_{e,+}+a_{e,-}\),
\[
\boxed{t_e^2\le\frac83 A_e+\frac49\sum_{f\sim e}A_f+\sqrt7\,\rho.}\tag{5}
\]
This is an exact quantitative leakage inequality. It forces the six nonstar within-support correlations to vanish when \(A=\rho=0\).

For the raw projected \(Q_i(z)=z_iz_i^T-\|z_i\|^2I/5\), define \(C_z=\operatorname{tr}(P_cK_z)\), \(V_z=\|\sum_iQ_i(z)\|_F^2\), and \(U=\sum_i a_i^2\). As \(Q_i(z)=(1-a_i)Q_i(u)\) and \(\|Q_i(u)\|_F^2=4/5\), the orthogonal projection triangle inequality gives
\[
\boxed{\rho\le\sqrt2\left(\sqrt{C_z+V_z/20}+\sqrt{4U/5}\right).}\tag{6}
\]
These estimates connect the raw Type-E midpoint budget to the six D5 Q-kernel residuals, without a conjectural one-to-one correspondence between kernel relations and exceptional pairings.

## Status

**[PROVED EXACTLY]** (1)-(6), exact classification of the zero Q-kernel fibre under the 184 safe constraints, and automatic safety of all six exceptional pairings in that fibre.

**[VERIFIED LOCALLY]** SymPy exact-rational checks of incidence reconstruction, residual identity, projector-defect identity, coefficient spectrum, meeting-support residual identity, rational perturbations, and normalized/raw Q comparison.

**[OPEN]** A quantitative contradiction for \(A\le383/504\). The current constants do not eliminate Type E; a lower bound on the Q-kernel residual or an upper bound on safe slack is still needed.

**[RETAINED]** \(40\le\tau_5\le44\). Type E \(M(F_3)\le89\), \(M(P)\ge S/2-28/3\), mass \(\ge2137/6\), \(A\le383/504\). Type C, D, generic \(e\ge27\), and non-isolated branches remain open. Sparse \(e=23,24\) classification remains conditional on \(\delta(G)\ge1\).
