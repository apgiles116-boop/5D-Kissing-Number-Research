# Type E: quantitative five-vector charts and exact Q/safe-slack identity

**2026-10-25. Proof status:** [PROVED EXACTLY, CONDITIONAL ON RETAINED FRAME GAPS] for quantitative chart bounds; [PROVED ALGEBRAICALLY] for Gram elimination and the Q/slack identity. [OPEN] Type-E elimination. Global range remains 40 <= tau_5 <= 44.

## Hypotheses

Let O be the sixteen selected outside-core deep edges in H=16K2 ⊔ F3, and C the four selected core edges. Write x_i^±=m_i±z_i, a_i=||m_i||², A=Σa_i<=B=383/504. The 184 outside-core pairings have |z_i·z_j|<=1/2. **Retain, but do not reprove here,** the 2026-10-25 deletion-robust frame results:

Z_O=Σ_{i∈O} z_i z_iᵀ ≻ (5/88)I₅; for each k∈O, Z_{O\{k}} ≻ (1/65)I₅.

No D5 labeling is assumed.

## Theorem 1: explicit nondegenerate basis charts

**[PROVED EXACTLY UNDER THE RETAINED FRAME GAPS]** Some five-element subset I⊂O has Gram determinant

det((z_i·z_j)_{i,j∈I}) > η₁₆ = 52019375/1452233797926912 ≈ 3.582024814×10⁻⁸.

For **every** k∈O, some I_k⊂O\{k}, |I_k|=5, has determinant

det((z_i·z_j)_{i,j∈I_k}) > η₁₅ = 464489/1756113784425000 ≈ 2.644982370×10⁻¹⁰.

**Proof.** For a positive definite 5×5 matrix with eigenvalues λ_j>g and trace T≥T₀, repeatedly applying (x−g)(y−g)≥0 gives det Z>g⁴(T₀−4g). Since tr Z_O≥16−B and tr Z_{O\{k}}≥15−B, the exact determinant lower bounds are

det Z_O > (5/88)⁴(16−B−20/88) = 52019375/332471107584,

det Z_{O\{k}} > (1/65)⁴(15−B−4/65) = 464489/584786475000.

Cauchy–Binet expresses each determinant as the sum of the five-column Gram determinants. There are binom(16,5)=4368 and binom(15,5)=3003 summands, so one exceeds the respective average. QED.

**Quantitative conditioning corollary [PROVED UNDER RETAINED FRAME GAPS].** The certified five-vector basis Gram matrix also satisfies

λ_min(G_I) > (4/5)⁴η₁₆ = 83231/5672788273152 ≈ 1.467197364×10⁻⁸.

Indeed tr G_I≤5 since each ||z_i||²≤1. By AM–GM the product of the four largest eigenvalues is at most (5/4)⁴; combine this with det G_I>η₁₆. This supplies a conservative explicit conditioning guarantee for interval/KKT calculations.

## Theorem 2: exact rank-five polynomial coordinates

**[PROVED ALGEBRAICALLY]** Choose a certified five-vector outside basis V=[z_{i₁} ... z_{i₅}], with G=VᵀV and d=det G>η₁₆. For any midpoint or projected vector u, set y_u=Vᵀu. Then

d(u·v) = y_uᵀ adj(G)y_v.                                    (1)

In particular, for the four core midpoints, d C_m=Y_mᵀ adj(G)Y_m. With y_i^σ=y_{m_i}+σy_{z_i}, all endpoint kissing inequalities become polynomial constraints of degree at most six:

2(y_i^σ)ᵀadj(G)y_j^τ ≤ d for distinct endpoints;
2(y_i^σ)ᵀadj(G)y_j^τ < −d for a prescribed deep contact.

The unit-norm equations are (y_i^σ)ᵀadj(G)y_i^σ=d. Within-edge orthogonality gives y_{m_i}ᵀadj(G)y_{z_i}=0, and the energy budget becomes Σ_i y_{m_i}ᵀadj(G)y_{m_i}≤(383/504)d. For zero-contact pairings impose both −d≤2(y_i^σ)ᵀadj(G)y_j^τ≤d.

Impose G≻0, d>η₁₆ and y_{z_{i_j}}=Ge_j. Because d>0, clearing denominators preserves all inequality signs. Conversely, any such chart solution has an exact R⁵ realization: choose V with VᵀV=G and recover u=V⁻ᵀy_u. Every Type-E configuration lies in at least one of 4368 charts. **This is a finite exact reduction, not an infeasibility certificate.**

## Theorem 3: exact Q/safe-slack conservation law

**[PROVED ALGEBRAICALLY]** For the 184 safe pairings define h_ij=1/2−|z_i·z_j|, L₁₈₄=Σh_ij and H₁₈₄=Σh_ij². Let S_C be the sum of six core squared correlations, s=Σa_i², and R²=||Σz_i z_iᵀ−(20−A)I₅/5||_F². The safe squared-correlation sum equals 46−L₁₈₄+H₁₈₄, while the exact frame trace identity gives total squared-correlation sum 30−3A+A²/10−s/2+R²/2. Therefore

L₁₈₄−H₁₈₄ = 16+3A−A²/10+s/2+S_C−R²/2.                 (2)

For each core pair let d_ij=(|z_i·z_j|−1/2)_+, h^C_ij=(1/2−|z_i·z_j|)_+, and D=Σd_ij, Q=Σd_ij², L_C=Σh^C_ij, H_C=Σ(h^C_ij)². Since S_C=3/2+D+Q−L_C+H_C, equivalently

(L₁₈₄+L_C)−(H₁₈₄+H_C)
= 35/2+3A−A²/10+s/2+D+Q−R²/2.                            (3)

These identities couple the six core defects, all safe slacks, midpoint energies and frame variance. They must be retained as **equalities**, not weakened by setting R=0.

## Status and next step

**[RETAINED, NOT REPROVED]** The capped-energy Q floor 8790283/317520≈27.6841868, six-core Q<19/250, safe-mass floor >12938492114773/504094752000, M(F3)≤89, matching mass ≥S/2−28/3, A≤383/504, and source-audited zero-midpoint exclusion. Do not regress to older constants.

**[OPEN]** Finite polynomial/KKT infeasibility certificate for these charts, Type E, Types C/D, generic e≥27, and non-isolated branches. Sparse e=23,24 classification requires δ(G)≥1. Global range: 40≤τ₅≤44.

The accompanying exact verifier checks rational constants, Cauchy–Binet on a rational example, adjugate reconstruction, and (2)–(3); it does not verify the retained spectral theorems or Type-E infeasibility.
