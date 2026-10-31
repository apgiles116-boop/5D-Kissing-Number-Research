# Type E: sharp two-plane Walsh pinching and 78-pair one-well stability
Date: 2026-10-30. **Global proved range unchanged: 40 <= tau_5 <= 44.**

## Proof-status ledger
- **[PROVED EXACTLY — universal geometry]** Sharp Bessel/two-plane bound on midpoint/mixed Walsh energy, attained by coplanar orthogonal frames.
- **[PROVED EXACTLY — conditional on Type-E 16K2+F3 incidence]** Midpoint-sensitive safe-block slack and a one-well reduction for 78 isolated-isolated safe meeting-support pairs in the critical x<=1/250 strip. No D5 geometric alignment is assumed.
- **[OPEN]** A sufficiently small global upper bound on the 114-pair safe squared-contact slack is missing; Type E is not eliminated.

## 1. Sharp geometric theorem
For selected deep-edge endpoints m_i +/- z_i and m_j +/- z_j, let
a=||m_i||^2, b=||m_j||^2 in [0,1/4], w=1-a, v=1-b, h=z_i.z_j, d=|h|,
T=(m_i.m_j)^2+(z_i.m_j)^2+(m_i.z_j)^2, W=T+d^2.
Then, **without any safe-contact assumption**,

\[
\boxed{T\le av+bw-\frac{av+bw-ab}{wv}d^2,}
\qquad
\boxed{W\le a+b-2ab+\frac{(1-2a)(1-2b)}{wv}d^2.} \tag{1}
\]

These inequalities are sharp for any a,b,d with d^2<=wv: put both normalized orthogonal pairs in the same 2-plane with relative rotation cos(theta)=d/sqrt(wv).

**Proof:** For a,b>0, write P=(m_i.m_j)^2, B=(z_i.m_j)^2, C=(m_i.z_j)^2. Bessel in both orthonormal 2-frames gives
P/a+B/w<=b, C/a+d^2/w<=v, P/b+C/v<=a, B/b+d^2/v<=w.
Let P0=ab d^2/(wv). For P<=P0, use B<=b(w-d^2/v), C<=a(v-d^2/w), and maximize at P=P0. For P>=P0, use B<=w(b-P/a), C<=v(a-P/b); the resulting bound wb+va+P(1-w/a-v/b) decreases with P because a,b<=1/4. Thus the maximum again occurs at P0, proving (1). The zero-midpoint cases follow by continuity. The coplanar rotation realizes P=P0, B=wb(1-d^2/wv), C=av(1-d^2/wv).

Writing c=(av+bw-ab)/(wv), one also has c>=a+b, since
(c-a-b)wv=a^2(1-b)+b^2(1-a)-ab >= (3/4)(a^2+b^2)-ab >= ab/2.
Hence T<=(a+b)(1-d^2)-2ab.

For a fully safe four-contact block, s=1/4-W>=0 and the new exact necessary bound is
\[
s\ge\frac14-a-b+2ab-\frac{(1-2a)(1-2b)}{wv}d^2. \tag{2}
\]
It can be combined by taking the maximum with the retained sharp cube profile
Phi(d)=d(1-4d) for d<=1/4, and Phi(d)=(2d-1/2)(1-2d) for 1/4<=d<=1/2.

## 2. Critical isolated-strip theorem
Let I be the sixteen isolated selected deep edges, x=sum_{i in I}a_i<=1/250. Every isolated-isolated pairing has a+b<=x; if safe, d<=1/2. Maximizing (1) at fixed t=a+b and p=ab gives
f(t,p)=t-2p+d^2(1-2t+4p)/(1-t+p).
Its p derivative is -2+d^2(3-2t)/(1-t+p)^2<0 for t<=1/250,d^2<=1/4. At p=0, the t derivative is 1-d^2/(1-t)^2>0. Therefore
\[
\boxed{W\le x+\frac{1-2x}{1-x}d^2.} \tag{3}
\]
At x<=1/250, this implies
\[
\boxed{s\ge\frac14-\frac1{250}-\frac{248}{249}d^2.} \tag{4}
\]
Consequently:
- d<=1/4 forces s>=22877/124500 (about 0.1837510);
- d<=3/8 forces s>=8793/83000 (about 0.1059398);
- d<=7/16 forces s>=55141/996000 (about 0.05536245).

These constants are **sharp for a single safe pair** with a+b<=1/250. Take a=1/250,b=0 and coplanar frames with h=r. The four contacts are +/-[r +/- sqrt(x(1-r^2/(1-x)))]. The exact positive safety-square margins at r=1/4,3/8,7/16 are respectively 14629/249000, 4047/332000, 2689/3984000. For s<1/4-x, inversion gives
d^2 >= [(1-x)/(1-2x)](1/4-x-s).
This eliminates the near-zero and near-quarter projected-correlation wells whenever safe squared-contact slack is small.

## 3. Exact 78-pair aggregate
Fix **one** arbitrary combinatorial K5 labeling with four core edges on distinct star supports, without geometric D5 alignment. The 120 isolated-isolated pairs split into 42 same/disjoint-support and 78 meeting-support pairs. All 78 meeting pairs are safe. The remaining 36 of the 114 safe meeting-support pairs are core-isolated.

The induced 78-pair graph has degree 9 on four unused star-sign slots and degree 10 on twelve nonstar slots. Write x_star+x_nonstar=x for their midpoint-energy sums, Q_RII=sum_RII d_ij^2, S_RII=sum_RII(1/4-W_ij), S_114 for all 114 safe meeting blocks. The exact identity 1/4-d^2=s+T and (1) imply
\[
\boxed{
Q_{RII}\ge\frac{39}{2}-S_{RII}-9x_{\rm star}-10x_{\rm nonstar}
+2\sum_{RII}a_i a_j+\sum_{RII}c_{ij}d_{ij}^2,} \tag{5}
\]
where c_ij=(a_i(1-a_j)+a_j(1-a_i)-a_i a_j)/[(1-a_i)(1-a_j)]>=0. In particular,
\[
\boxed{Q_{RII}\ge39/2-S_{114}-10x,\qquad
\sum_{RII}(1/2-d_{ij})\le2S_{114}+20x.} \tag{6}
\]
If K_r of the 78 pairs have d<=r, the thresholds in (4) give
K_(1/4)<=S_114/(22877/124500),
K_(3/8)<=S_114/(8793/83000),
K_(7/16)<=S_114/(55141/996000).
These are **same-label** finite-state bounds; they do not separately optimize any Q residual or Walsh energy.

## 4. Interface and limitations
The retained six-deep/474-safe frame conservation identity is
W_70+X_6=A-U+V_edge/2+S_114, and its Petersen consequence is
T_70+E_Q/4+M_extra/28 >= A-U+V_edge/2+S_114.
The new theorem gives explicit second-order penalties for the 78 isolated meeting pairs and narrows a prospective finite KKT analysis to 36 core-isolated safe meeting pairs and six exceptional core pairs, **provided** S_114 can be bounded sharply. That upper bound is not yet available. Do not claim a Type-E exclusion.

**Retained:** star <=70/3, M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, Musin/Boyvalenkov 21-line zero-midpoint exclusion. Types C,D, generic e>=27, non-isolated branches open; sparse e=23,24 classification conditional on delta(G)>=1. **40<=tau_5<=44.**

The companion local exact-Fraction verifier checks all three sharp rational safe examples, derivative inequalities, and K5 incidence counts. The universal proof is the Bessel argument above, not finite sampling.