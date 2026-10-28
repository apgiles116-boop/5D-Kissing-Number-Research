# Type E: improved high-center contact quantization and rank-seven reduction (2026-10-28)

**[NEW, EXACT ALGEBRA — CONDITIONAL ON RETAINED TYPE-E HIGH-CENTER CERTIFICATES]** In the high-center branch \(s\ge7\), the previously constructed rounded 17-by-17 signed Gram matrix \(\widehat G\) has **rank at most seven**, improving the rank-eight result in [the preceding note](tau5_typeE_high_center_binary_rank8_2026-10-28.md). Equivalently, its integer signed adjacency matrix \(S=2\widehat G-2I\) has eigenvalue \(-2\) with multiplicity at least **ten**. This is not a Type-E exclusion; \(\widehat G\) has not been proved PSD.

## 1. Strengthened pointwise contact quantization

Use the previous note's conditional high-center inputs: \(N=\sum_{\mathrm{nondeep}}f(t)\le5/64\), \(x=\sum_{i=1}^{16}\|m_i\|^2<1/2500\), \(f(t)=7t^2(1-4t^2)\), and the exact nondeep alternative \(|t|<1/9\) or \(12/25<|t|\le1/2\). Set \(\rho(t)=\min(|t|,1/2-|t|)\).

**[EXACT]** On these two intervals,
\[
 f(t)\ge\frac{539}{81}\rho(t)^2.
\]
For the low interval, \(f/\rho^2=7(1-4t^2)\ge539/81\). For \(u=|t|>12/25\), \(f/\rho^2=28u^2(1/2+u)/(1/2-u)>28(12/25)^2(49/50)/(1/50)>539/81\). Endpoints where \(\rho=0\) follow directly. Hence
\[
 \sum_{\mathrm{nondeep}}\rho(t)^2\le\frac{81}{539}N\le\frac{405}{34496}.
\]

## 2. Stronger Frobenius estimate

The previously proved Walsh/center rounding identity bounds the true rank-five PSD Gram \(G=\operatorname{Gram}(v,z_1,\ldots,z_{16})\) against the rounded \(\widehat G\):
\[
\|G-\widehat G\|_F^2\le
 \sum_{\mathrm{center}}\rho(t)^2+
 \tfrac12\sum_{\mathrm{isolated-isolated}}\rho(t)^2+
 \sum_{i=1}^{16}\|m_i\|^4.
\]
Since \(\sum\|m_i\|^4\le x^2\), we obtain
\[
\boxed{\|G-\widehat G\|_F^2<
 E:=\frac{405}{34496}+\frac1{6250000}
 =\frac{158205281}{13475000000}<\frac1{81}.}
\]
Thus the Frobenius perturbation is strictly below \(1/9\), improving \(1/8\).

## 3. Integral rank-seven lemma

Let \(B\) be any \(k\times k\) principal submatrix of \(\widehat G\), \(8\le k\le17\), and \(A\) the corresponding principal submatrix of \(G\). Then \(A\succeq0\), \(\operatorname{rank}A\le5\), \(\operatorname{tr}B=k\), and \(\|A-B\|_F<1/9\). Let \(p\ge1\) be the number of positive eigenvalues of \(B\), and \(q=\min(p,5)\).

The final \(k-q\) eigenvalues of \(B\) have squared sum \(<1/81\). For \(p\ge5\), this follows from Hoffman–Wielandt and the zero eigenvalues of \(A\) after position five. For \(p<5\), they are all nonpositive, and the squared norm of the negative part of \(B\) is at most \(\|A-B\|_F^2\), since \(A\) is PSD.

Their sum in absolute value is \(<\sqrt{k-q}/9\). Since \(\operatorname{tr}B=k\), the sum of the first \(q\) positive eigenvalues is \(<k+(k-q)/9\). AM–GM applied separately to the positive and remaining eigenvalues gives
\[
 |\det B|<
 \left(\frac{k+(k-q)/9}{q}\right)^q
 \left(\frac1{81(k-q)}\right)^{(k-q)/2}.
\]
For all integers \(8\le k\le17\), \(1\le q\le5\), the right side is \(<2^{-k}\). The companion exact Fraction verifier checks all **50** squared rational inequalities
\[
 2^{2k}\left(\frac{k+(k-q)/9}{q}\right)^{2q}
 \left(\frac1{81(k-q)}\right)^{k-q}<1.
\]
The largest left side is \(640000000000/847288609443<1\), at \((k,q)=(8,5)\).

Since \(2B\) is integral, \(\det B\) is an integer multiple of \(2^{-k}\), and must vanish. All principal minors of orders \(8,\ldots,17\) vanish. The principal-rank theorem for symmetric matrices now yields
\[
\boxed{\operatorname{rank}\widehat G\le7,\quad
\operatorname{nullity}\widehat G\ge10,\quad
\operatorname{mult}_{S}(-2)\ge10.}
\]

## Status and next target

**[EXACTLY VERIFIED, CONDITIONAL]** This upgrade relies on the previously retained high-center resource inequality, contact dichotomy, and Walsh rounding structure. The new arithmetic and determinant comparisons are exact.

**[OPEN]** The high-center branch is not excluded. The low-center branch remains open. The rounded matrix is not known to be PSD or rank five, and no \(D_5\) labeling is justified. The next finite target is a signed-graph classification on 17 vertices with at least 81 nonzero edges and eigenvalue \(-2\) of multiplicity at least 10, plus a nearby rank-five PSD Gram.

**[GLOBAL PROVED RANGE UNCHANGED]** \(40\le\tau_5\le44\). Retain \(M(F_3)\le89\), \(M(P)\ge S/2-28/3\), and \(A\le383/504\); do not replace global claims with conditional Type-E conclusions.


## 4. Binary alternating-rank corollary and finite star complement

**[NEW, EXACT — CONDITIONAL ON THE RANK-SEVEN REDUCTION]** Let \(M=2\widehat G=2I+S\). It is integral with diagonal 2 and off-diagonal entries in \(\{-1,0,1\}\), and \(\operatorname{rank}_{\mathbb Q}M\le7\). Reducing modulo 2 gives the **unsigned adjacency matrix** \(A_{\mathrm{bin}}=M\bmod2\) of the 17-vertex support graph: signs disappear and the diagonal is zero. Since reduction modulo a prime cannot increase matrix rank,
\[
\operatorname{rank}_{\mathbb F_2}A_{\mathrm{bin}}\le7.
\]
A zero-diagonal symmetric matrix in characteristic two is alternating, hence has **even rank**. Therefore
\[
\boxed{\operatorname{rank}_{\mathbb F_2}A_{\mathrm{bin}}\le6,\qquad
\operatorname{nullity}_{\mathbb F_2}A_{\mathrm{bin}}\ge11.}
\]
Equivalently, the underlying unsigned support graph has a representation by vectors \(u_1,\ldots,u_{17}\in\mathbb F_2^6\) with adjacency \(A_{ij}=u_i^TJu_j\) for an alternating bilinear form \(J\) (allowing lower rank). This is a necessary condition, not an exclusion.

For an exact finite classification, choose a nonsingular principal block \(T=M_{BB}\) of order \(r=\operatorname{rank}M\le7\), which exists because \(M\) is symmetric. For the remaining vertices, write the block decomposition
\[
 M=\begin{pmatrix}T&C\\C^T&D\end{pmatrix}.
\]
Rank \(r\) is **equivalent** to the exact Schur complement condition \(D=C^TT^{-1}C\). Each column \(c\) of \(C\) has entries in \(\{-1,0,1\}\), must satisfy \(c^TT^{-1}c=2\), and every distinct pair \(c,d\) must satisfy \(c^TT^{-1}d\in\{-1,0,1\}\). The known high-center degree range \(10\le k_I\le14\), at least 71 isolated-isolated support edges, and the binary rank-six condition provide exact combinatorial pruning. The remaining geometric filter is a PSD rank-five Gram within Frobenius distance \(1/9\). No classification is claimed yet.
