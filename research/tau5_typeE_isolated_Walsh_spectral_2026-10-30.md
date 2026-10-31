# Type E: isolated-edge Walsh spectral bound and K5 label averaging (2026-10-30)

**Global proved range unchanged: 40 <= tau_5 <= 44.**

## Status

**[PROVED EXACTLY — universal linear algebra]** For sixteen deep edges with all 120 isolated-isolated pairings safe, the total midpoint/mixed Walsh energy admits an exact trace identity and rank-five spectral bound.

**[PROVED EXACTLY — conditional on retained Type-E 16K2+F3 incidence]** There exists a combinatorial K5 labeling with the four core matching edges on distinct star supports such that the 42 isolated-isolated nominally orthogonal pairings have midpoint/mixed Walsh energy
$
T_{42}\le \frac{14}{5}x+\frac7{40}(x^2-U_I),
$
where (x=\sum_{i\in I}\|m_i\|^2\le1) and (U_I=\sum_{i\in I}\|m_i\|^4). In the critical strip (x\le1/250),
$
\boxed{T_{42}<\frac{26817}{2500000}=0.0107268.}
$
No D5 geometric alignment is assumed.

**[OPEN]** The 28 core-isolated nominally orthogonal pairings, six exceptional core pairings, and labeling-dependent Q residual are not jointly controlled. This does not eliminate Type E.

## Exact trace and spectral proof

For isolated edge (i), write its endpoints (m_i\pm z_i), with (m_i\perp z_i), (a_i=\|m_i\|^2\in[0,1/4]), and (\|z_i\|^2=1-a_i). Set
$
M_I=\sum_{i\in I}m_im_i^T,\quad Z_I=\sum_{i\in I}z_iz_i^T,\quad
x=\operatorname{tr}M_I,\quad U_I=\sum_{i\in I}a_i^2,
$
and (T_{ij}=(m_i\cdot m_j)^2+(m_i\cdot z_j)^2+(z_i\cdot m_j)^2). Direct expansion gives
$
\boxed{T_{II}:=\sum_{i<j\in I}T_{ij}
=\frac{\operatorname{tr}(M_I^2)-U_I}{2}
+\operatorname{tr}(M_IZ_I).}
$
Since (M_I\succeq0), (\operatorname{tr}M_I=x),
$
T_{II}\le\frac{x^2-U_I}{2}+x\lambda_{\max}(Z_I).
$

All four endpoint contacts are safe for each isolated pair, so Walsh inversion gives (|z_i\cdot z_j|\le1/2). Therefore
$
\operatorname{tr}Z_I=16-x,\qquad
\operatorname{tr}(Z_I^2)\le76-2x+U_I.
$
For a PSD (5\times5) matrix with trace (t), squared trace (p), and largest eigenvalue (\lambda), Cauchy on the other four eigenvalues gives (p\ge\lambda^2+(t-\lambda)^2/4). Consequently
$
\lambda_{\max}(Z_I)
\le\frac{16-x+2\sqrt{124+22x+5U_I-x^2}}5
\le\frac{16-x+2\sqrt{124+22x+4x^2}}5.
$
For (0\le x\le1) this is strictly below 8, equivalent after squaring positive sides to (15x^2/4+10x-20<0). For (0\le x\le1/250), it is strictly below (383/50), equivalent to (-129/400+217x/20+15x^2/4<0). Both are exact rational polynomial checks.

## K5 combinatorial averaging

Assign the four F3 core edges to one sign of supports 01,02,03,04. Distribute the sixteen isolated edges among the remaining sixteen sign slots. Among the 70 same-support/disjoint-support pairings there are exactly **42 isolated-isolated, 28 core-isolated, and 0 core-core**. The induced isolated graph has degrees (6^4,5^{12}).

A uniformly random bijection of the sixteen physical isolated edges to the slots includes any particular isolated-isolated physical pair with probability
$
\frac{42}{\binom{16}{2}}=\frac7{20}.
$
Thus some labeling satisfies
$
T_{42}\le\frac7{20}T_{II}
\le\frac7{20}\left(\frac{x^2-U_I}{2}+x\lambda_{\max}(Z_I)\right).
$
For (x\le1) this gives (T_{42}\le14x/5+7(x^2-U_I)/40); for (x\le1/250) the sharper rational spectral cap gives
$
T_{42}\le\frac{2681}{1000}x+\frac7{40}(x^2-U_I)
<\frac{26817}{2500000}.
$
The last strict inequality holds also at (x=0), where (T_{42}=0).

For all labelings averaged jointly,
$
\mathbb E[T_{70}]=\frac7{20}T_{II}+\frac7{16}T_{CI},
$
where (T_{CI}\) sums the 64 physical core-isolated midpoint/mixed energies. With (M_C=\sum_Cm_im_i^T) and (S_C=\sum_C(m_im_i^T+z_iz_i^T)),
$
T_{CI}=\operatorname{tr}(M_CZ_I)+\operatorname{tr}(M_IS_C).
$
This isolates the remaining core-isolated KKT problem. **Do not optimize the 42-pair term and the labeling-dependent Q residual under different labelings.**

## Ledger and next step

The retained exact Petersen/Walsh inequality is
$
T_{70}+E_Q/4+M_{\rm extra}/28
\ge A-U+V_{\rm edge}/2+\sum_{114\,\rm safe}\Phi(|z_i\cdot z_j|).
$
The new bound makes the isolated-isolated portion of (T_{70}) negligible in the small-(x) critical region for a suitable labeling. The remaining task is a **joint** bound on (T_{28}), (E_Q), and the six exceptional core contacts, preferably via a small exact polynomial/KKT certificate.

Retain (M(F_3)\le89), (M(P)\ge S/2-28/3), selected-edge mass (\ge2137/6), (A\le383/504), and the Musin/Boyvalenkov zero-midpoint 21-line exclusion. Types C,D, generic e>=27, and non-isolated branches remain open; sparse e=23/e=24 classification is conditional on delta(G)>=1.

Companion checker: `research/tau5_typeE_isolated_Walsh_spectral_2026-10-30_verify.py`.
