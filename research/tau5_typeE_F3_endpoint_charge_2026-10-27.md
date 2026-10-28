# Type E: endpoint-charge SOS excludes all four-active F3 cores

Date: 2026-10-27.

**[PROVED EXACTLY — conditional on the retained Type-E F3 graph and endpoint kissing inequalities]** Every F3 perfect matching has at most **three** exceptional projected pairings, improving the earlier four-active ceiling. For matching P2, the sum of linear correlation excesses is at most \(1/4\), the fixed-threshold quartic positive defect is at most \(225/2048\), and the sum of fixed squared-correlation excesses is at most \(9/32\). **[OPEN]** This is not a Type-E exclusion and does not improve \(40\le\tau_5\le44\).

## 1. Four-core endpoint-charge identity

Write the four selected deep edges as unit endpoints \(p_i^\pm=m_i\pm z_i\), where \(m_i\cdot z_i=0\), \(a_i=\|m_i\|^2\), \(r_i=\|z_i\|^2=1-a_i\). All distinct endpoint products are at most \(1/2\), and deep cross-contacts have product at most \(-1/2\).

The retained F3 edge set is \(02,04,05,14,17,23,27,36,56,57\), with matchings
\(P_1=(02,14,36,57)\), \(P_2=(04,17,23,56)\), \(P_3=(05,14,27,36)\).

Let \(k_{ij}\) count F3 cross-contacts between two matching edges. P2 has six \(k=1\) pairs; P1/P3 have one \(k=0\), four \(k=1\), and one \(k=2\). Direct exact enumeration shows the forced signs of all potentially exceptional correlations are globally antibalanced: endpoint orientation signs \(\varepsilon_i\in\{\pm1\}\) exist such that each forced correlation sign is \(-\varepsilon_i\varepsilon_j\). Define for all six pairs
\[
t_{ij}=-\varepsilon_i\varepsilon_j(z_i\cdot z_j),\qquad B_{ij}=m_i\cdot m_j.
\]
After these orientations, all deep cross-contacts lie in the two opposite-sign endpoint positions. The average of those two endpoint products is \(B_{ij}-t_{ij}\). Since \(k_{ij}\) of them are at most \(-1/2\) and the others at most \(+1/2\),
\[
\boxed{t_{ij}-B_{ij}\ge (k_{ij}-1)/2.}\tag{1}
\]
If the pair is active, \(d_{ij}=|z_i\cdot z_j|-1/2>0\), then \(t_{ij}=1/2+d_{ij}\). The two same-sign endpoint products average to \(B_{ij}+t_{ij}\le1/2\), hence \(B_{ij}\le-d_{ij}\) and
\[
\boxed{t_{ij}-B_{ij}\ge1/2+2d_{ij}.}\tag{2}
\]

Expanding the two squared norms gives the **exact identity**
\[
\boxed{\sum_{i<j}(t_{ij}-B_{ij})=
2-\tfrac12\left(\left\|\sum_i\varepsilon_i z_i\right\|^2+
\left\|\sum_i m_i\right\|^2\right).}\tag{3}
\]
No D5 labeling, SDP, or numerical optimization is used.

Let \(n_1\) count active \(k=1\) pairs and \(D=\sum_{\mathrm{active}}d_{ij}\). The six baseline charges \((k_{ij}-1)/2\) sum to zero for all three matchings. Replacing baseline (1) by (2) adds \(1/2+2d\) for each active \(k=1\) pair and \(2d\) for an active \(k=2\) pair. Therefore
\[
\boxed{\frac{n_1}{2}+2D+
\frac12\left(\left\|\sum_i\varepsilon_i z_i\right\|^2+
\left\|\sum_i m_i\right\|^2\right)\le2.}\tag{4}
\]
The retained F3 signed-triangle obstruction separately forbids active triangles.

## 2. Exact branch consequences

**[PROVED EXACTLY]** In P2, every potential exception has \(k=1\), so \(k/2+2D\le2\) for \(k\) active pairs. Four active would imply \(D\le0\), impossible. Three active imply \(D\le1/4\); at most two active also give \(D<1/4\) from the exact individual one-contact cap \(d<1/8\). Thus
\[
\boxed{P_2:\quad \#\mathrm{active}\le3,\qquad D\le1/4.}\tag{5}
\]

In P1/P3, if the two-contact diagonal is active, the earlier signed-triangle lemma permits at most two additional one-contact pairs. If it is inactive, four active one-contact cycle pairs would force \(2+2D\le2\) by (4), impossible. Thus
\[
\boxed{P_1,P_3:\quad\#\mathrm{active}\le3.}\tag{6}
\]

## 3. P2 quartic and corrected harmonic improvement

Put \(f(d)=(1/2+d)^2(d+d^2)\), \(g(d)=d+d^2\). Both are increasing convex on \([0,1/8]\). Under (5), the capped-simplex supremum fills two \(1/8\) caps, so
\[
\boxed{P_{\rm fixed}=\sum f(d_{ij})\le 2f(1/8)=225/2048=0.10986328125,}
\]
\[
\boxed{\sum_K\delta_{ij}=\sum g(d_{ij})\le 2g(1/8)=9/32.}\tag{7}
\]
This supersedes the earlier P2 ceiling \(0.187511443251\ldots\). These are upper bounds for a relaxation, not claimed attainable in full rank-five Type E.

Since \(h_{ij}=1-r_ir_j\le7/16\) under \(a_i\le1/4\), the positive defect contribution in the **audited moving-threshold fourth-harmonic inequality** satisfies
\[
\boxed{P_{\rm fixed}+\tfrac14\sum_K h_{ij}\delta_{ij}
\le225/2048+(7/64)(9/32)=9/64.}\tag{8}
\]
Combining with the previously proved frame/mixing coercivity, the P2 branch obeys the necessary condition
\[
H_4^++\frac{34697}{201600}U
\le \frac9{64}-\frac{R_2^2}{56}+\frac{3S_4}{8}
+\frac{19A}{16}-\frac{A^2-U}{32},\tag{9}
\]
where \(U=\sum a_i^2\), \(R_2=\sum r_i^2\), \(S_4=\sum r_i^4\), and \(H_4^+\ge0\) is the non-frame fourth-harmonic sector sum. Equation (9) is **not yet contradictory** and discards additional nonnegative safe-pair mixing slack.

For P1/P3 the previous overall quartic ceiling \(0.253429412001\ldots\) remains; the diagonal-inactive subbranch improves to \(225/2048\).

## 4. Verification and ledger

The companion exact Fraction verifier checks all F3 cross-contact counts, explicit global antibalanced switching, baseline charge cancellation, all 64 active subsets per matching with signed-triangle restrictions, and the exact rational defect envelopes. Equations (1)–(4) are analytic endpoint/PSD identities; finite enumeration checks only F3 signs and supports.

**[RETAINED]** \(40\le\tau_5\le44\); Type-E \(1/49<A\le383/504\); \(M(F_3)\le89\); matching \(M(P)\ge S/2-28/3\); twenty-edge mass \(\ge2137/6\); rigorous Musin/Boyvalenkov zero-midpoint exclusion; 184 safe pairings. Sparse \(e=23,24\) classification still requires \(\delta(G)\ge1\).

**[OPEN]** Type E, C, D, generic \(e\ge27\), and non-isolated branches. Next: retain the square slacks in (4) with the isolated-center row and 184 safe-pair mixing penalties; prioritize the P1/P3 diagonal-active three-pair case.