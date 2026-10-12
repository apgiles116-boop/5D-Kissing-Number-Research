# Type E: conditional support-plane rigidity and Q-kernel counterexample

**Research note:** 2026-10-13 (draft prepared 2026-10-12)  
**Proof status:** **[PROVED EXACTLY — under specified extra hypothesis]**, **[VERIFIED — FINITE EXACT]**, **[OPEN]** for unrestricted Type E and the five-dimensional kissing number.

## Setup and scope

For the **one mass-selected** set of twenty deep edges in the isolated-center Type-E case, write

\[
x_r^\pm=m_r\pm z_r,\quad a_r=\|m_r\|^2\in[0,1/4),\quad
y_r=z_r/\sqrt{1-a_r},\quad A=\sum_{r=1}^{20}a_r\le383/504.
\]

Let \(c\) be the isolated center, \(\|c\|=1\). Non-deep endpoint contacts imply

\[
(c\cdot y_r)^2\le\frac1{4(1-a_r)}.\tag{1}
\]

These are retained Type-E hypotheses; this note does not independently certify the upstream mass theorem.

### Additional hypothesis (SP) — **NOT established for Type E**

After a rotation and relabeling, the twenty unit \(y_r\) form ten *orthonormal pairs*, one on each coordinate plane \(\operatorname{span}(e_i,e_j)\), \(1\le i<j\le5\). Each pair may be freely rotated within its plane. This is **not** an assumption of exact D5 geometry. However, we have **not proved (SP)** from Type-E contacts or the six-dimensional Q-Gram kernel.

At most four supports contain any of the four selected F3 core edges. All other supports are *clean* (both directions arise from isolated \(K_2\) edges). Every pair of distinct selected edges with at least one isolated \(K_2\) edge is safe.

## 1. A weighted support-angle inequality — [PROVED EXACTLY]

For two safe deep edges, all four cross-endpoint dot products lie in \([-1/2,1/2]\). Averaging simultaneous sign reversals gives

\[
|m_r\cdot m_s|+|z_r\cdot z_s|\le\tfrac12,\qquad
|y_r\cdot y_s|\le[2\sqrt{(1-a_r)(1-a_s)}]^{-1}.\tag{2}
\]

Consider two adjacent coordinate supports \(p=ij\), \(q=ik\), with all four cross-line pairs safe. Put \(\delta_p=|\cos(2\theta_p)|\), where \(\theta_p\) is the rotation of the orthonormal pair on support \(p\). Select the two lines on \(p\) and \(q\) having largest absolute \(i\)-coordinate; let their energies be \(a_r,a_s\). Their absolute inner product equals the product of those coordinates, hence

\[
\frac{\sqrt{(1+\delta_p)(1+\delta_q)}}2
\le[2\sqrt{(1-a_r)(1-a_s)}]^{-1}.
\]

Since \(\delta_q\ge0\) and \((1-a_r)(1-a_s)\ge1-a_r-a_s\), we obtain

\[
\boxed{\delta_p\le\frac{a_r+a_s}{1-a_r-a_s}.}\tag{3}
\]

Each of the ten supports (edges of \(K_5\)) has six adjacent supports. At most four are non-clean, so each support has at least two clean neighbors. Equation (3) therefore implies, for every support,

\[
\boxed{\delta_p\le\frac{A}{1-A}.}\tag{4}
\]

This is *conditional on (SP)*, but is an exact analytic inequality under that hypothesis.

## 2. Quantitative incompatibility for \(A\le5/23\) — [PROVED EXACTLY, CONDITIONAL ON (SP)]

**Theorem.** Under (1)–(4), the safe-contact structure and hypothesis (SP),

\[
\boxed{A>\frac5{23}.}\tag{5}
\]

**Proof.** Suppose \(A\le5/23\). Then every support satisfies \(\delta_p\le5/18\). Match each rotated orthonormal support pair to the two projective D5 directions \((e_i\pm e_j)/\sqrt2\). Its two projective angles equal \(\phi_p\in[0,\pi/4]\), and \(\delta_p=\sin(2\phi_p)\). Write \(s=\max_p\sin\phi_p\).

For the matched D5 directions \(v_r\), set \(H_r=(c\cdot v_r)^2\), \(h_r=(c\cdot y_r)^2\). The difference of the rank-one projectors has operator norm \(\sin\phi_r\), so \(|H_r-h_r|\le s\). Moreover, (1) yields
\[
H_r\le\tfrac14+s+\frac{a_r}{4(1-a_r)},\qquad H_r\le\tfrac13+s.
\]
Using \(a_r/[4(1-a_r)]\le a_r/3\), the exact D5 identities
\[
\sum_r H_r=4,\qquad \sum_rH_r^2\ge8/5
\]
give
\[
\frac85\le\sum_r H_r^2
\le4(\tfrac14+s)+(\tfrac13+s)\frac A3
=1+4s+\frac A9+\frac{As}{3}.
\]
Thus
\[
s\ge\frac{3/5-A/9}{4+A/3}\ge\frac{596}{4215}.
\]
Since \(\delta_p=\sin(2\phi_p)\) is monotone for \(\phi_p\in[0,\pi/4]\),
\[
\max_p\delta_p=2s\sqrt{1-s^2}
\ge2\frac{596}{4215}\sqrt{1-(596/4215)^2}.
\]
But the exact rational certificate reads
\[
(5/18)^2-4(596/4215)^2[1-(596/4215)^2]
=-\frac{1535336051479}{1262555003002500}<0,
\]
contradicting \(\max_p\delta_p\le5/18\). This proves (5).

**Interpretation:** This does not eliminate Type E, even under (SP), because \(5/23<A\le383/504\) is nonempty.

## 3. Q-Gram nullity six does not imply the support-plane hypothesis — [VERIFIED FINITE EXACT]

The quadratic lifts \(Q(y)=yy^\top-I_5/5\) lie in the 14-dimensional space of traceless symmetric \(5\times5\) matrices. Thus every twenty-vector Q-Gram matrix has nullity at least 6. This dimensional fact alone cannot force ten D5-like support planes.

The attached script \`tau5_Qkernel_nullity_counterexample_2026-10-13.py\` uses exact rational stereographic projections of fixed integer tuples and verifies:

- 20 unit vectors in \(\mathbb Q^5\);
- **no** pair among their 190 pairs is orthogonal;
- the traceless quadratic lifts have rank **exactly 14**, so their Q-Gram matrix has nullity **exactly 6**.

This is a counterexample to the abstract implication “Q-nullity six implies D5 support-plane structure”; it is **not** a counterexample to Type E, and the vectors are **not claimed to satisfy Type-E contact inequalities**.

## 4. Proof boundaries and next work

- **[PROVED EXACTLY — CONDITIONAL]** Equations (3)–(5) under (SP) and the specified endpoint inequalities.
- **[VERIFIED FINITE EXACT]** Rational threshold comparison and explicit Q-nullity counterexample, via companion scripts.
- **[OPEN]** Whether Type E forces (SP), a weaker approximate support decomposition, or additional structured Q-kernel relations.
- **[OPEN]** Types C/D/E and generic higher-edge cases remain unresolved.

**Retained Type-E inputs:** \(M(F_3)\le89\), some matching \(P\) has \(M(P)\ge S/2-28/3\), twenty selected edges have mass \(\ge2137/6\), and \(A\le383/504\). Matching-specific bounds must not be silently applied to all three matchings.

**Global proved range:** \(40\le\tau_5\le44\); sparse \(e(G)=23,24\) graph classifications still require \(\delta(G)\ge1\).
