# Type E: robust disjoint-pair Gram obstruction and exact exclusion box

**2026-10-24. Status:** [PROVED EXACTLY] universal inequality and rational exclusion box; [CONDITIONAL TYPE E] application to selected F3 core; [OPEN] global quadratic-budget improvement and Type E elimination.

## Setup

For four selected deep edges write x_i^±=m_i±z_i, a_i=||m_i||²≤1/4, ||z_i||²=1-a_i, and assume m_i·m_j+|z_i·z_j|≤1/2. Let δ_ij=(|z_i·z_j|-1/2)_+. Suppose α=δ_12>0, β=δ_34>0, γ=δ_13>0. Put C=Σ_{i=1}^4 a_i and t=C-2(α+β)≥0.

## Theorem [PROVED EXACTLY]

For any 0≤k≤1, let L=(1-k)/2+(1+k)γ-(k/2)√t. If L>0, then

L² ≤ [1-β+√(βt+t²/4)] × [(1+k²)(1-α+√(αt+t²/4))-k(1+2α)]. (R)

This is dimension-independent and uses no D5 labeling or SDP.

**Proof.** Orient z_2,z_3 so z_1·z_2=1/2+α and z_1·z_3=1/2+γ. From m_1·m_2≤-α and a_1+a_2≤2α+t, ||m_1+m_2||²≤t. Since m_1·m_3≤-γ, m_2·m_3≥γ-√(t a_3). Endpoint feasibility gives z_2·z_3≤1/2-γ+√(t a_3). Therefore (z_1-kz_2)·z_3≥(1-k)/2+(1+k)γ-k√(t a_3)≥L, since a_3≤1/4. Cauchy–Schwarz yields L²≤||z_1-kz_2||²||z_3||² when L>0. From a_1a_2≥α² and a_1+a_2≤2α+t, each a_1,a_2≥α-√(αt+t²/4). Similarly a_3≥β-√(βt+t²/4). Substitute into ||z_1-kz_2||²=(1-a_1)+k²(1-a_2)-k(1+2α) and ||z_3||²=1-a_3. QED.

## Saturation-only Bessel refinement [PROVED EXACTLY]

At t=0, m_1=-m_2, m_3=-m_4, and a_1=a_2=α, a_3=a_4=β. The orthogonal vectors z_1+z_2 and z_1-z_2 have squared norms 3 and 1-4α. With x=z_1·z_3=1/2+γ and y=z_2·z_3≤1/2-γ, Bessel gives

(x+y)²/3+(x-y)²/(1-4α)≤1-β.

If 0<α<1/4 and α+3γ/2≥1/4, minimization over y≤1/2-γ yields

4γ²≤(1-4α)(2/3-β). (S)

## Exact rational exclusion box [PROVED EXACTLY]

Use retained B=383/504, D0=1780062775/4032758016 and the prior *scalar-only* witness

α0=244473/1000000,
β0=B/2-α0=8535701/63000000,
γ0=D0-B/2=247774759/4032758016.

Let h=1/100000. No endpoint-feasible four-edge geometry can satisfy simultaneously |δ_12-α0|≤h, |δ_34-β0|≤h, |δ_13-γ0|≤h, and 0≤C-2(δ_12+δ_34)≤h.

**Certificate.** Apply (R) at k=6/7. The three radicals are bounded above by 1/300, 1/600, 1/800 respectively (verify by squaring rational bounds). Set

Lmin=(1-k)/2+(1+k)(γ0-h)-k/(2·300),
U3=1-(β0-h)+1/800,
U12=(1+k²)(1-(α0-h)+1/600)-k(1+2(α0-h)).

Then Lmin>0 and

Lmin²-U3·U12 =
311094683363205057250829161/194554131729736464000000000000 >0,

contradicting (R). At exact saturation the scalar witness also violates (S) by 4γ0²-(1-4α0)(2/3-β0)≈0.00335643809258.

**Scope.** This eliminates a near-sharp scalar defect witness and an explicit neighborhood *as physical endpoint geometry*. It does not prove that every high-quadratic-defect assignment lies in this box, so the global certified Σδ²<819/10000 remains unchanged. The global proved range remains 40≤τ5≤44. Type E/C/D, generic e≥27 and non-isolated branches remain open. Retained F3 bounds M(F3)≤89 and A≤383/504 are unchanged.

Companion exact verifier: `tau5_typeE_robust_disjoint_pair_gram_obstruction_2026-10-24_verify.py`.
