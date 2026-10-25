# Type E: sharp 20-vector Q-comparison and strengthened six-core tradeoff

**25 October 2026.** **[PROVED EXACTLY — universal theorem]** Sharp comparison spectral floor `5/16` for twenty vectors, improving `13/44`. **[CONDITIONAL ON RETAINED TYPE-E INPUTS]** Improved safe/core slack tradeoff. **[OPEN]** Type E and the global problem.

## 1. Sharp 20-vector comparison lemma [PROVED EXACTLY]

For arbitrary \(b_i\in[3/4,1]\), \(i=1,\ldots,20\), define
\[
K_0=\operatorname{diag}(b_i^2-1/4)+\tfrac14\mathbf1\mathbf1^T-\tfrac15bb^T.
\]
Then
\[
\boxed{K_0\succeq (5/16)I_{20}.}\tag{1}
\]
This is sharp: \(b_1=b_2=3/4\), other \(b_i=1\), and \(x=e_1-e_2\) attain equality. Total norm deficit in this example is \(1/2<383/504\).

**Proof.** Put \(a_i=1-b_i\), \(A=\sum a_i\), and split at \(A=7/32\).

*If \(A\le7/32\)*, use the exact identity
\[
K_0=\operatorname{diag}(b_i^2-1/4)+\tfrac1{20}(\mathbf1+4a)(\mathbf1+4a)^T-aa^T.
\]
Since \(a_i\le A\) and \(\sum a_i^2\le A^2\),
\[
K_0\succeq [(1-A)^2-1/4-A^2]I=(3/4-2A)I\succeq(5/16)I.
\]

*If \(A\ge7/32\)*, put \(t_i=b_i-3/4=1/4-a_i\), \(S=\sum x_i\), \(T=\sum t_i x_i\), and \(D=\sum_i t_i(3/2+t_i)x_i^2\). Direct expansion yields
\[
x^T(K_0-\tfrac5{16}I)x=D+\tfrac{11}{80}(S-\tfrac{12}{11}T)^2-\tfrac4{11}T^2.\tag{2}
\]
Weighted Cauchy gives \(T^2\le P D\), where \(P=\sum_i t_i/(3/2+t_i)\). Since \(f(t)=t/(3/2+t)\) satisfies \(f(1/4)=1/7\) and \(f'(t)\ge24/49\) on \([0,1/4]\),
\[
P\le20/7-(24/49)A\le20/7-(24/49)(7/32)=11/4.
\]
The negative term in (2) is therefore canceled by \(D\), proving (1). The two certificates are exact and require no Type-E midpoint-energy assumption.

## 2. Universal signed quartic Q-rank theorem [PROVED EXACTLY]

Let \(z_1,\ldots,z_{20}\in\mathbb R^5\) with \(3/4\le b_i=\|z_i\|^2\le1\), without assuming any pairwise correlation cap. Put
\[
Q_i=z_i z_i^T-(b_i/5)I_5,\qquad K_{ij}=\langle Q_i,Q_j\rangle=(z_i\cdot z_j)^2-b_i b_j/5.
\]
Then \(K\succeq0\) and \(\operatorname{rank}K\le14\). For \(E=K_0-K\), \(E_{ii}=0\), \(E_{ij}=1/4-(z_i\cdot z_j)^2\), and \(\operatorname{tr}E=0\). By (1), at least six eigenvalues of \(E\) are at least \(5/16\); the remaining fourteen sum to at most \(-6(5/16)\). Hence
\[
\operatorname{tr}(E^2)\ge6(5/16)^2+[6(5/16)]^2/14,
\]
and
\[
\boxed{\sum_{i<j}\big(1/4-(z_i\cdot z_j)^2\big)^2\ge375/896
\approx0.418526785714286.}\tag{3}
\]
This improves the earlier \(2535/6776\) by exactly \(4815/108416\). Sharpness is proved for the **comparison constant**, not asserted for (3).

## 3. Type-E application [CONDITIONAL ON RETAINED INPUTS]

In Type E, 184 of the 190 distinguished-edge pairings are raw-safe; only six core pairings can exceed \(r_{ij}=|z_i\cdot z_j|=1/2\). Let \(H_{184}=\sum_{\rm safe}(1/2-r_{ij})^2\), \(H_C^-=\sum_{\rm core:r\le1/2}(1/2-r_{ij})^2\), and \(T_C^+=\sum_{\rm core:r>1/2}(d_{ij}+d_{ij}^2)^2\), with \(d_{ij}=r_{ij}-1/2\).

For each safe pair, \((1/4-r^2)^2=(1/2-r)^2(1/2+r)^2\le(1/2-r)^2\). Thus (3) implies
\[
\boxed{H_{184}+H_C^-+T_C^+\ge375/896.}\tag{4}
\]

The exact six-defect square budget \(\sum d_{ij}^2<819/10000\), individual cap \(d_{ij}\le1/4\), and convex concentration estimate \(T_C^+<12286461/100000000\) were established in `tau5_typeE_lifted_triangle_defect_budget_2026-10-24.md` and `tau5_typeE_leave_one_core_out_Qrank_2026-10-25.md`. Consequently
\[
\boxed{H_{184}+H_C^->206963523/700000000\approx0.295662175714286.}\tag{5}
\]

If all six core pairings have \(r>1/2\), then \(H_C^-=0\) and the lower bound applies directly to \(H_{184}\). Otherwise **no** such direct conclusion is warranted. The complementary 19-vector weighted inequality is
\[
H_{184}+\tfrac12H_C^->755723921/2800000000+\tfrac14H_{OC}.
\]
No contradiction with \(A\le383/504\) is obtained.

**[OPEN]** Type E, Types C and D, generic \(e\ge27\), and non-isolated branches. **[UNCHANGED]** \(40\le\tau_5\le44\); \(M(F_3)\le89\); \(M(P)\ge S/2-28/3\); \(A\le383/504\); sparse \(e=23/24\) classification conditional on \(\delta(G)\ge1\).

Exact verifier: `tau5_typeE_sharp20_Qcomparison_2026-10-25_verify.py`.


## 4. Exact frame-variance / homogeneous-defect bridge [PROVED EXACTLY]

Write \(a_i=1-\|z_i\|^2\), \(A=\sum a_i\), and
\[
V=\left\|\sum_{i=1}^{20}\left(z_i z_i^T-\frac{\|z_i\|^2}{5}I\right)\right\|_F^2\ge0.
\]
Across all 190 pairings, let \(h_{ij}=1/2-r_{ij}\) when \(r_{ij}\le1/2\), and \(d_{ij}=r_{ij}-1/2\) when \(r_{ij}>1/2\). Set
\[
L=\sum_{r_{ij}\le1/2}h_{ij}(1-h_{ij}),\qquad
P=\sum_{r_{ij}>1/2}(d_{ij}+d_{ij}^2).
\]
The two exact evaluations
\[
\sum_{i<j}r_{ij}^2=\frac{95}{2}-L+P
=30-3A+\frac{A^2}{10}-\frac12\sum_i a_i^2+\frac V2
\]
give the **exact identity**
\[
\boxed{L+\frac V2=\frac{35}{2}+3A-\frac{A^2}{10}+\frac12\sum_i a_i^2+P.}\tag{6}
\]
Under Type E, \(P\) is supported on at most six core pairings, while \(L\) covers all safe pairings, including raw-safe core pairs. This translates the global squared-correlation/frame-variance relation into the six-exception language. Retaining the positive frame variance \(V/2\) may help a future second-order stability argument. At exact \(D_5\), \(A=P=V=0\) and \(L=35/2\) (70 zero-correlation pairings). **[OPEN]** No contradiction with \(A\le383/504\) follows from this identity alone.
