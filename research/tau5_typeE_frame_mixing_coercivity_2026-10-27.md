# Type E: exact frame–mixing coercivity and a sharpness barrier for the four-core relaxation

Date: 2026-10-27.

**[PROVED EXACTLY — universal algebra]** The frame/mixing identity in Section 1.
**[PROVED EXACTLY — conditional on retained Type-E hypotheses]** The coercive bound and corrected harmonic-budget corollary in Section 2.
**[PROVED EXACTLY — for a RELAXED midpoint Gram problem only]** The sharpness construction in Section 3.
**[OPEN]** No Type-E exclusion or improvement of the global kissing-number bound.

## 1. A complete frame–safe-mixing identity

Take twenty selected deep edges with unit endpoints `m_i ± z_i`, `m_i·z_i=0`, `a_i=||m_i||²`, `r_i=||z_i||²=1-a_i`. Let `C` be the four exceptional core indices, `K=binom(C,2)` its six pairs, and `R` the remaining 184 pairs. Set

```
A=sum_i a_i,  U=sum_i a_i²,  U_C=sum_{i in C} a_i²,
R2=sum_i r_i²=20-2A+U,
F_z=sum_i z_i z_i^T,       F_w=sum_i r_i z_i z_i^T,
E=F_w-(R2/5)I,             W=||E||_F²,
B=sum_i a_i m_i m_i^T,    B0=B-(U/5)I.
X_ij=m_i·z_j, Y_ij=z_i·m_j, h_ij=1-r_i r_j,
T_R=sum_{ij in R} h_ij (X_ij²+Y_ij²).
```

Define three explicit nonnegative slacks:

```
J1=sum_{ij in R} [(h_ij-a_i)X_ij²+(h_ij-a_j)Y_ij²] >= 0,
J2=tr(B(F_z-F_w))=sum_{i,j} a_i a_j(m_i·z_j)² >= 0,
J3=3U_C-sum_{ij in K}[a_i X_ij²+a_j Y_ij²] >= 0.
```

The last inequality uses `(m_i·z_j)²<=a_i r_j<=a_i` and the fact that every core vertex has three core neighbors. The first uses `h_ij-a_i=a_j(1-a_i)>=0`.

**Exact identity (no D5 labeling, no SDP):**

```
(5/24)W+(1/4)T_R
 = U*R2/20 - (3/4)U_C - (3/40)||B0||_F²
   + (5/24)||E+(3/5)B0||_F² + (J1+J2+J3)/4.          (1)
```

Proof: `T_R=tr(BF_z)-3U_C+J1+J3=tr(BF_w)-3U_C+J1+J2+J3`. Since `tr(B)=U` and `tr(E)=0`, `tr(BF_w)=U R2/5+tr(B0 E)`. Complete the matrix square
`(5/24)||E||²+(1/4)tr(B0 E)=(5/24)||E+3B0/5||²-(3/40)||B0||²`.
Every equality is polynomial in the original vectors.

## 2. Exact second-order coercivity and corrected Type-E interface

Since `B` is PSD with trace `U`, `||B0||²=tr(B²)-U²/5<=4U²/5`. From (1), using `U_C<=U`,

```
(5/24)W+(1/4)T_R
 >= U*R2/20 - 3U_C/4 - 3U²/50
 >= U*(1/4-A/10-U/100).                              (2)
```

Under the retained Type-E bounds `A<=383/504` and `0<=a_i<=1/4`, we have `U<=A/4`. Thus

```
(5/24)W+(1/4)T_R >= (34697/201600)*U
                            = 0.1721081349206...*U. (3)
```

This is a **strictly positive second-order penalty whenever U>0**, even if the frame is tight (`W=0`); conversely, if safe mixing vanishes, the frame variance must pay the penalty. It is independent of any proposed D5 contact labeling.

To insert it into the corrected fourth-harmonic inequality, write `w_ij=(z_i·z_j)²`, `delta_ij=[w_ij-1/4]_+`, and let `H4plus` be the sum of the five nonnegative O(4) harmonic-sector squares from `tau5_typeE_center_O4_harmonic_branching_2026-10-27.md` **excluding** its `5W/24` term. The exact threshold audit bounds

```
(5/24)W + H4plus + sum_R (w_ij+h_ij/4)*(B_ij²+X_ij²+Y_ij²)
 <= P_fixed - R2²/56 + 3*S4/8 + 19*A/16
    -(A²-U)/32 + (1/4)sum_K h_ij*delta_ij,           (4)
```

where `B_ij=m_i·m_j`, `S4=sum r_i^4`, and `P_fixed=sum [w_ij(w_ij-1/4)]_+`. Since the safe mixing term in (4) is at least `T_R/4`, (3) gives the new **valid necessary Type-E inequality**

```
H4plus + (34697/201600)*U
 <= P_fixed - R2²/56 + 3*S4/8 + 19*A/16
    -(A²-U)/32 + (1/4)sum_K h_ij*delta_ij.           (5)
```

This corrects for the moving harmonic threshold; it does NOT use the withdrawn implication `D_weighted<=P_fixed`. Inequality (5) has not yet been shown contradictory.

## 3. Exact sharpness barrier for a core-only midpoint SDP

The prior all-six-active spectral inequality gives `D=sum_K d_ij<=A_C/2<=Dmax=383/1008`, with `d_ij=(|z_i·z_j|-1/2)_+` in an actual Type-E realization. Consider instead the **relaxed** constraints `G=(m_i·m_j)_{i,j in C} PSD`, `a_i=G_ii<=1/4`, `tr G<=383/504`, and `0<=d_ij<=-G_ij`. No projected vectors or isolated center are imposed in this relaxation.

Put `b=Dmax-1/4=131/1008` and, for `0<t<131/2016`, define

```
G(t) = [[1/4, -(1/4-2t), -t, -t],
        [-(1/4-2t), 1/4, -t, -t],
        [-t, -t, b, -(b-2t)],
        [-t, -t, -(b-2t), b]].
```

Its exact eigenvalues are `0, 4t, 1/2-2t, 2b-2t`; hence it is PSD of rank three. It has `G(t)1=0`, trace `383/504`, and six strictly negative off-diagonal entries. Choose `d_ij=-G_ij`. Then all six defects are strictly active and

```
sum_K d_ij=(1/4-2t)+(b-2t)+4t=Dmax=A_C/2.
```

For the convex increasing quartic function `f(d)=(1/2+d)²(d+d²)`, capped-simplex convexity gives `sum_K f(d_ij)<=f(1/4)+f(Dmax-1/4)`. The above PSD family approaches equality as `t->0+`:

```
sup_relaxed sum_K f(d_ij)
 = 241638909745/1032386052096
 = 0.2340586733561665... .                           (6)
```

Thus the previously reported six-active quartic envelope is **the exact supremum of the midpoint-Gram relaxation**. No stricter uniform bound can follow from that relaxation alone. The limiting Gram geometry consists of two antipodal midpoint pairs; the four cross defects tend to zero. This is **not** a construction of four projected directions, eight endpoint code vectors, or a Type-E code. Any genuine improvement must use projected Gram rank/contact data, endpoint mixing, the isolated-center row, or the 184 safe pairings.

## 4. Proof ledger

**[RETAINED]** `40<=tau_5<=44`; Type-E `1/49<A<=383/504`; `M(F3)<=89`; matching `M(P)>=S/2-28/3`; twenty-edge mass `>=2137/6`; 184 safe and six potentially exceptional pairings; Musin/Boyvalenkov zero-midpoint exclusion; exact fixed-versus-weighted threshold audit. The sparse e=23/24 classification requires `delta(G)>=1`.

**[OPEN]** Type E, C, D, generic e>=27 and non-isolated branches. The next finite polynomial task is to retain the `J1,J2,J3` slacks and the core projected/midpoint cross-Gram rank <=5, rather than further optimizing the already-sharp core-only spectral envelope.

Companion exact regression verifiers: `research/tau5_typeE_frame_mixing_coercivity_2026-10-27_verify.py` and `research/tau5_typeE_core_spectral_sharpness_2026-10-27_verify.py`.
