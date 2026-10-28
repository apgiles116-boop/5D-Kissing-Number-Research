# Type E: diagonal interference eliminates the large P1/P3 quartic envelope

Date: 2026-10-27.

**[PROVED EXACTLY — conditional on the retained Type-E F3 endpoint graph, the endpoint-charge switching, and the signed-triangle lemma]** For each of the two matchings P1/P3, the total fixed-threshold quartic positive defect is at most **45/256**, rather than the previous 0.253429412... combinatorial envelope. The corrected weighted-harmonic positive contribution is at most **215/1024**. For P2, the retained bounds **225/2048** and **9/64** remain. **[OPEN]** No Type-E exclusion or global improvement to 40 <= tau_5 <= 44.

## 1. Four unit-vector Gram representation

Use the four selected F3 deep edges and the globally antibalanced orientation signs \(\varepsilon_i\) from [endpoint-charge note](tau5_typeE_F3_endpoint_charge_2026-10-27.md). Write endpoints \(p_i^\pm=m_i\pm z_i\), where \(\|m_i\|^2+\|z_i\|^2=1\). In \(\mathbb R^{10}\) introduce unit vectors
\[
q_i=(\varepsilon_i z_i,m_i),\qquad
c_{ij}=-q_i\cdot q_j
=-\varepsilon_i\varepsilon_j z_i\cdot z_j-m_i\cdot m_j.
\]
The endpoint-charge inequality implies, for any pair with \(k\) F3 cross-contacts,
\[
c_{ij}\ge (k-1)/2.
\]
For an active exceptional pair, \(d_{ij}=|z_i\cdot z_j|-1/2>0\), it also implies
\[
c_{ij}\ge 1/2+2d_{ij}.
\]
These are exact necessary inequalities; all Gram matrices of the \(q_i\) are PSD.

For P1/P3, relabel the four edges so that the two-contact diagonal is \(03\), the zero-contact pair is \(12\), and the four one-contact pairs are \(01,02,13,23\). Thus
\[
c_{03}\ge1/2,\quad c_{12}\ge-1/2,\quad
c_{01},c_{02},c_{13},c_{23}\ge0.
\]
If diagonal \(03\) is active, let \(d_0=d_{03}>0\). The signed-triangle obstruction forbids both \(01\) and \(13\) being active, and likewise forbids both \(02\) and \(23\). Hence there can be at most two active one-contact pairs, and when two are active they meet *different* vertices from \(\{1,2\}\).

## 2. Exact diagonal-interference inequalities

Put \(S=q_0+q_3\). Then
\[
\|S\|^2=2(1-c_{03})\le1-4d_0.
\]
If one one-contact pair involving vertex 1 is active with defect \(s>0\), the other charge from vertex 1 to the diagonal is nonnegative. Consequently
\[
-S\cdot q_1=c_{01}+c_{13}\ge1/2+2s.
\]
Cauchy–Schwarz gives
\[
(1/2+2s)^2\le1-4d_0,\qquad
\boxed{d_0\le3/16-s/2-s^2.}\tag{1}
\]
In particular \(d_0\le3/16\).

If two one-contact pairs are active, one meets vertex 1 and the other vertex 2. Let their total excess be \(s=d_1+d_2\), with \(0<s<1/4\). Since all four one-contact charges are nonnegative,
\[
-S\cdot(q_1+q_2)\ge1+2s.
\]
Also \(\|q_1+q_2\|^2=2(1-c_{12})\le3\). Therefore
\[
(1+2s)^2\le3(1-4d_0),\qquad
\boxed{d_0\le1/6-s/3-s^2/3.}\tag{2}
\]
These are rank-free PSD/Cauchy consequences of the *actual* F3 contact pattern; no D5 labeling, numerical optimizer, or SDP is used.

## 3. Exact quartic envelopes

Let
\[
f(d)=(1/2+d)^2(d+d^2).
\]
It is nonnegative, increasing and convex for \(d\ge0\), with \(f(0)=0\). Each one-contact excess satisfies \(0<d<1/8\). If the diagonal is inactive, the preceding endpoint-charge result gives \(P_{\rm fixed}\le225/2048\).

If the diagonal is active:
* No one-contact pair active: \(P_{\rm fixed}\le f(1/4)=45/256\).
* Exactly one active: (1) and the individual cap imply
  \(P_{\rm fixed}\le f(3/16)+f(1/8)=10497/65536<45/256\).
* Exactly two active: put \(s=d_1+d_2\le1/4\). Convexity and \(f(0)=0\) imply \(f(d)\le f(b)d/b\) for \(0\le d\le b\). With \(f(1/6)/(1/6)=14/27\) and \(f(1/8)/(1/8)=225/512\), equation (2) gives
\[
P_{\rm fixed}\le
\frac7{81}+\frac{11057}{41472}s-\frac{14}{81}s^2.
\]
This polynomial increases on \([0,1/4]\), hence
\[
P_{\rm fixed}\le7867/55296<45/256.
\]

Therefore, for both P1 and P3,
\[
\boxed{P_{\rm fixed}\le45/256=0.17578125.}\tag{3}
\]
This replaces the older 0.253429412... envelope. It is a necessary bound for full Type E, not an existence statement or a claim of sharpness for the full configuration.

## 4. Corrected moving-threshold harmonic budget

For \(g(d)=d+d^2\), define \(h(d)=f(d)+(7/64)g(d)\). Since each \(a_i\le1/4\), \(1-(1-a_i)(1-a_j)\le7/16\), so
\[
P_{\rm fixed}+\frac14\sum_K(1-r_ir_j)\delta_{ij}
\le\sum_K h(d_{ij}).
\]
The same three-case proof works with \(h\): diagonal-only gives \(h(1/4)=215/1024\); diagonal plus one gives
\(h(3/16)+h(1/8)=13101/65536<215/1024\); diagonal plus two gives, by the secant bounds and (2),
\[
\sum h(d)\le
\frac{2233}{20736}+
\frac{3599}{10368}s-\frac{2233}{10368}s^2
\le\frac{10009}{55296}<\frac{215}{1024}.
\]
(The displayed middle polynomial is equivalent to
\(h(1/6)(6d_0)+h(1/8)(8s)\); the exact verifier checks its endpoint.) The diagonal-inactive bound is \(9/64\). Thus
\[
\boxed{
P_{\rm fixed}+\tfrac14\sum_K(1-r_ir_j)\delta_{ij}
\le
\begin{cases}
215/1024,&P_1,P_3,\\
9/64,&P_2.
\end{cases}}\tag{4}
\]
This must be used in the *audited* fixed-versus-weighted harmonic comparison, not in the withdrawn comparison that omitted the midpoint correction.

## 5. Ledger and next task

**[PROVED EXACTLY]** The four-core quotient Gram PSD supplies new diagonal-versus-one-contact tradeoffs and the branchwise bounds (3),(4).

**[RETAINED]** Global 40<=tau_5<=44; Type-E 1/49<A<=383/504; M(F3)<=89; matching mass >=S/2-28/3; twenty-edge mass >=2137/6; 184 safe pairings; zero-midpoint Musin/Boyvalenkov exclusion. The e=23/e=24 sparse graph classification requires delta(G)>=1.

**[OPEN]** Type E, C, D, generic e>=27, non-isolated branches. Next: insert (4) into the exact frame/mixing coercivity inequality while retaining the endpoint-charge square slacks, the isolated-center row and the rank-five projected/midpoint cross-Gram constraints. The diagonal-only case now dominates the P1/P3 relaxed quartic envelope; it should be isolated as a separate finite polynomial branch.
