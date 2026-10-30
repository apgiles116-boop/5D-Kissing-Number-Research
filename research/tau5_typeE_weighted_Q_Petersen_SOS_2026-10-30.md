# Type E: exact weighted-Q Petersen-graph sum-of-squares and zero-kernel classification

Date: 2026-10-30. **[PROVED EXACTLY]** The identities and zero-kernel classification below. **[CONDITIONAL TYPE-E COROLLARY]** A positive weighted-Q residual floor, dependent on the retained Type-E graph/energy reduction and the previously certified support-plane fibre exclusion. **[OPEN]** Type E and the global kissing number.

## Definitions

Label the twenty selected deep edges by the two signs of the ten supports pq of K5, assigning the four F3 core edges to one sign of each of the four star supports 0p. This is a combinatorial labeling, NOT an assumption of D5 geometric alignment. Let a_i=||m_i||² in [0,1/4], w_i=||z_i||²=1-a_i, A=sum a_i<=383/504. Let Q_i=z_i z_i^T-(w_i/5)I, K_ij=tr(Q_i Q_j), V=||sum Q_i||_F² and C=tr(P_c K)>=0. Here P_0 is the rational rank-six D5 Q-kernel projector, P_g=11^T/20 and P_c=P_0-P_g (rank five). P_0 entries are 3/10 for diagonal or same support, -1/30 for meeting distinct supports, and 2/15 for disjoint supports.

Let O be the sum of (z_i.z_j)² over the ten same-support pairs, D the corresponding sum over sixty disjoint-support pairs. These seventy pairings are all among the 184 nonexceptional Type-E pairings.

## New exact local sum-of-squares theorem

For **any** twenty vectors assigned these labels, with a_i=1-||z_i||²,

\[
\boxed{V+12C=8O+4D+\frac25\left(2\sum_{\rm same}(a_i-a_j)^2+
\sum_{\rm disjoint}(a_i-a_j)^2\right).}\tag{1}
\]

All terms on the right are nonnegative. The six exceptional core pairings are meeting-support pairings and disappear from (1) **algebraically**, not by imposing any safety on them.

Proof: P_c has entries 1/4 on diagonal/same support, -1/12 on meeting supports, +1/12 on disjoint supports. Expand V=sum_ij K_ij and C=tr(P_c K). The 120 meeting-support squared correlations cancel, leaving

\[
V+12C=8O+4D+\frac45
(4\sum_i w_i^2-2\sum_{\rm same}w_iw_j-\sum_{\rm disjoint}w_iw_j).
\]

Every index has one same-support partner and six disjoint-support partners. Substitution w_i=1-a_i cancels constants and linear terms and gives (1).

The weighted graph with weight two on each same-support edge and weight one on each disjoint-support edge is a twofold blow-up of the Petersen graph KG(5,2), with the ten twin edges added. Its Laplacian L has exact spectrum 0^(1),4^(5),10^(14), and

\[
L=4P_c+10(I-P_0).
\]

Consequently, writing P_perp=I-P_0, equation (1) is equivalently

\[
\boxed{V+12C=8O+4D+\frac85\|P_ca\|^2+4\|P_{\perp}a\|^2.}\tag{2}
\]

Set E=V+12C. Immediate exact bounds:

\[
O\le E/8,\quad D\le E/4,\quad
\sum_i(a_i-A/20)^2\le5E/8.
\]

Another exact positive decomposition is

\[
O+2C+V/10=(9/5)O+(2/5)D+(4/5)C+
(4/25)\|P_ca\|^2+(2/5)\|P_\perp a\|^2.
\]

## Zero-kernel classification [PROVED EXACTLY]

If E=0 and 3/4<=w_i<=1, then O=D=0 and a_i=A/20 for every i. Normalize u_i=z_i/sqrt(w_i). All six normalized Q-kernel relations vanish. For each support pq let S_pq=u_pq^+u_pq^{+T}+u_pq^-u_pq^{-T}. The rank-five incidence reconstruction gives S_pq=B_p+B_q, sum B_p=I, tr B_p=1. O=0 makes each S_pq a rank-two orthogonal projector. The exact identity

\[
B_p^2-B_p=\sum_{q\ne p}D_{pq}-\frac13\sum_{r<s}D_{rs},
\quad D_{pq}=(B_p+B_q)^2-(B_p+B_q)=0
\]

forces all B_p to be symmetric rank-one orthogonal projectors, mutually orthogonal because they sum to I. Hence the twenty normalized directions form ten orthonormal pairs spanning the ten coordinate two-planes of one common orthonormal basis. Ten independent within-plane rotations remain possible: this is NOT a rigid-D5-root classification. It rules out exotic non-support-plane configurations in the exact weighted Q-kernel fibre without requiring the 184 safe constraints.

## Quantitative weighted-Q gap [CONDITIONAL TYPE E]

Let b=1-A/20>=9697/10080>24/25 and u_i=z_i/sqrt(w_i). From (2),

\[
\|W_uP_0\|_F\le b^{-1}(\sqrt{E/12}+\sqrt{E/2})<b^{-1}\sqrt E,
\]

where W_z and W_u have columns Q(z_i),Q(u_i). Thus normalized rho²=2C_u+V_u/10 and O_u obey

\[
\rho<(165/112)\sqrt E,\qquad \sqrt{O_u}<(33/70)\sqrt E.
\]

Using the established inverse-rounding theorem, delta=sqrt(3)(2sqrt(O_u)+5rho+rho²), h=rho+22delta, and if h<1/10 a common support-plane model exists at sign-aligned vector distance at most 15h/7. Exact rational enclosures yield, for sqrt(E)<=1/1000,

\[
h<[(891297/2800)+(259545/3136)\sqrt E]\sqrt E
 <(637/2)\sqrt E.
\]

The prior exact Type-E interval certificate excludes Euclidean vector distance <=1/360 from every core-star-labeled support-plane model. It was rerun this pass: **988,525 subdivisions, zero unresolved**. If E<=1/245700², the inverse theorem gives distance <(15/7)(637/2)/245700=1/360, contradiction. Therefore

\[
\boxed{V_z+12C_z>1/245700^2=1/60368490000.}\tag{3}
\]

This is a positive lower bound on the **weighted Q-kernel residual itself**, not an elimination of Type E. It depends on the retained Type-E hypotheses and prior exact fibre certificate.

## Independent cap-aware global frame improvement [PROVED EXACTLY]

The frame identity gives sum_{i<j}(z_i.z_j)² >=30-3A+A²/10-U/2, U=sum a_i². For fixed A and 0<=a_i<=1/4, U<=k/16+(A-k/4)² where k=floor(4A). The resulting lower bound decreases on 0<=A<=383/504. At A=383/504, k=3 and remainder 5/504, giving

\[
\boxed{\sum_{i<j}(z_i.z_j)^2\ge8790283/317520
=27.684186822877\ldots.}
\]

This improves the earlier 17456771/635040 and retains at least 92.28% of D5's total squared-correlation mass 30.

## Ledger

**[PROVED EXACTLY]** Local Petersen-graph SOS (1), spectral decomposition (2), zero weighted-Q fibre classification, weighted-to-normalized estimates, and cap-aware correlation floor. **[CONDITIONAL TYPE-E]** Positive weighted residual floor (3), dependent on the exact 1/360 fibre certificate. **[OPEN]** Need an upper bound on V_z+12C_z from all 184 safe Walsh blocks and the six exceptional core pairings. Type C, D, generic e>=27, and non-isolated branches remain open. Sparse e=23,24 classification still assumes delta(G)>=1. Retain M(F3)<=89, matching >=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, and the Musin/Boyvalenkov zero-midpoint exclusion. **Global proved range remains 40<=tau_5<=44.**
