# Type E: quantitative PSD incompatibility of concentrated core defects

Date: 2026-10-31. **Global proved range: 40 <= tau_5 <= 44. Type E OPEN.**

## Theorem and status

**[PROVED EXACTLY — universal four-vector argument; numerical Type-E consequence conditional on retained caps]**

For four core midpoint vectors (m_i) with (a_i=\|m_i\|^2\le1/4), (A_C=\sum a_i\le383/504), write
(c_{ij}=m_i\cdot m_j), (d_{ij}=|z_i\cdot z_j|),
(\epsilon_{ij}=(d_{ij}-1/2)_+), (\delta=\sum_{i<j}\epsilon_{ij}),
(E_2=\sum\epsilon_{ij}^2), (Q_6=\sum d_{ij}^2).
Assume the upper endpoint-contact inequalities and the retained Type-E cap
(\delta\le D=1780062775/4032758016).

Then
[
Q_6\le\frac{32436090936603055633}{16263137215612256256}
       -\frac{27}{80000}
=\frac{20269126329870491560321}{10164460759757660160000}
\approx1.994117229526.
]
The improvement over the previous (1.994454729526) bound is **exactly 27/80000**. It uses no D5 alignment, full Q-rank assumption, or numerical optimizer.

**[PROVED CONDITIONALLY — retained global Q floor]**
[
Q_{\rm safe}\ge
\frac{259144239476339336023679}{10164460759757660160000}
\approx25.495129117161.
]
With the separately retained center-derived variance floor, (Q_{\rm safe}>25.765028770790).

## Proof

1. Endpoint upper contacts give (c_{ij}+d_{ij}\le1/2), (0\le\epsilon_{ij}\le(-c_{ij})_+\le1/4). Put (N=\sum_{c_{ij}<0}(-c_{ij})), (s_C=\|\sum_i m_i\|^2). For (c\ge0), the affine endpoint majorant loses at least (c(1/4-c)); for (c<0), it loses at least ((3/4)(-c-\epsilon)+\epsilon(1/4-\epsilon)). Summing and polarizing gives the exact necessary inequality
[
Q_6\le\frac32+\frac\delta4+E_2+\frac38(A_C-s_C)
-\frac34(N-\delta)
-\sum_{c_{ij}>0}c_{ij}(1/4-c_{ij}). \tag{1}
]
All discarded terms are nonnegative.

2. For (1/4\le t\le1/2), let (F(t)=1/16+(t-1/4)^2). Capped-simplex convexity gives (E_2\le F(\delta)); for (\delta<1/4), use (E_2\le\delta^2). Let (B=3/2+D/4+F(D)+3(383/504)/8), the old upper bound. If (\delta\le D-1/1000), monotonicity gives
(B-Q_6\ge(2D-251/1000)/1000>27/80000).
If (\delta>D-1/1000) but (E_2\le F(\delta)-1/2000), the loss is at least (1/2000).

3. In the remaining case, sort the six defects (p\ge q\ge\cdots). Majorization shows (p>6/25): otherwise
(E_2\le(6/25)^2+(\delta-6/25)^2), whose difference from (F(\delta)) is (49/5000-\delta/50>1/1250).
Similarly (q>9/50): otherwise majorization by ((1/4,9/50,1/50,0,0,0)) gives (E_2\le953/10000), whereas (E_2>981/10000).

4. These two defects cannot be on disjoint pairs: their sum exceeds (21/50), whereas disjoint defects sum to at most (A_C/2<19/50). Relabel them as edges ((1,2),(1,3)). If (N-\delta\ge1/1000), (1) loses at least (3/4000). Otherwise, writing (u=-c_{12}\ge p), (v=-c_{13}\ge q), we have
[
u-v>p-q-1/1000\ge2p-\delta-1/1000
>12/25-D-1/1000>3/80. \tag{2}
]
The (3\times3) Gram Schur complement, (a_i\le1/4), (u>6/25), and (v>9/50) imply
[
c_{23}\ge
\frac{uv-\sqrt{(a_1a_2-u^2)(a_1a_3-v^2)}}{a_1}
>3/25,
]
using (\sqrt{(1/16-(6/25)^2)(1/16-(9/50)^2)}<13/1000).
Conversely Cauchy gives
[
(u-v)^2\le a_1(a_2+a_3-2c_{23})
\le1/8-c_{23}/2,
]
hence (c_{23}<791/3200). The positive pair ((2,3)) contributes the additional loss
[
c_{23}(1/4-c_{23})>
(3/25)(9/3200)=27/80000.
]
Every case loses at least (27/80000) from (B), proving the theorem.

5. Subtract the new (Q_6) cap from the retained (Q_{\rm all}\ge17456771/635040) to obtain the safe floor. The stronger conditional floor uses (Q_{\rm all}>5876056025347/211680000000).

## Ledger

**[PROVED EXACTLY]** Four-vector Gram, endpoint and convexity argument under its stated hypotheses.
**[PROVED CONDITIONALLY]** Numerical Type-E bounds using the supplied exact (A_C\le383/504) and (\delta\le D) certificates; their upstream derivations are not independently re-audited here.
**[OPEN]** Type E, C, D, generic (e\ge27), and non-isolated branches. Sparse (e=23,24) classification still assumes (\delta(G)\ge1). Preserve (M(F_3)\le89), (M(P)\ge S/2-28/3), twenty-edge mass (\ge2137/6), and Musin/Boyvalenkov's zero-midpoint exclusion.

The next target is a stronger joint bound retaining the centroid, unused negative-correlation mass, four-core Gram minors and the four rank-free Q-residuals under one common labeling. This result does **not** eliminate Type E.
