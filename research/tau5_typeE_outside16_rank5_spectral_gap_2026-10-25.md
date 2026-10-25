# Type E: sixteen outside-core projected vectors span R^5, with an exact spectral gap

Date: 2026-10-25. **[PROVED EXACTLY UNDER RETAINED TYPE-E HYPOTHESES]** Results below. **[OPEN]** Type-E elimination; global bound remains 40 <= tau_5 <= 44.

## Setup
For the 16 selected deep edges belonging to the 16K2 component of H=16K2 ⊔ F3, write x_i^±=m_i±z_i, a_i=||m_i||²<1/4, b_i=||z_i||²=1-a_i. All cross-endpoint contacts between these edges are nondeep, so |z_i·z_j|<=1/2 for i≠j. Set A_O=Σ_{i∈O}a_i<=A<=B=383/504 and Z_O=Σ_{i∈O}z_i z_i^T.

**Theorem [PROVED EXACTLY]:** Z_O ≻ (1/500) I_5. In particular, the 16 outside-core projected vectors span R^5. No D5 labeling, six-exception identification, or SDP is used.

## Dimension-four polynomial obstruction
For unit v_i∈R^4, let f(t)=t⁴-t²/4. The normalized spherical Gegenbauer polynomials are P₂(t)=(4t²-1)/3 and P₄(t)=(16t⁴-12t²+1)/5, both positive-definite kernels by the harmonic addition theorem. As f=(1+6P₂+5P₄)/16, for 16 unit vectors,
Σ_{i≠j}f(v_i·v_j) >= 16²/16 - 16 f(1) = 4.

For v_i=z_i/sqrt(b_i) with |z_i·z_j|<=1/2,
f(v_i·v_j) <= [1-b_i b_j]/[16 b_i² b_j²].
The sharp two-energy inequality on 0<=a,b<=1/4 is
[1-(1-a)(1-b)]/[(1-a)²(1-b)²] <= (224/81)(a+b).
Indeed the ratio to a+b is h/[(1-a)²(1-b)²], h=1-ab/(a+b)>=7/8. Its derivative in a has the sign of 2h-(1-a)b²/(a+b)² >=7/4-1>0; similarly for b. The maximum at a=b=1/4 is 224/81.

Summing over 16*15 ordered pairs gives
4 <= Σ_{i≠j}f(v_i·v_j) <= (140/27) A_O.
Thus if the 16 z_i lay in a four-dimensional subspace, A_O>=27/35. But 27/35-383/504=203/17640>0, contradiction.

General form: n>12 raw-safe vectors in a four-dimensional subspace with a_i<=1/4 require Σa_i >=81n(n-12)/[448(n-1)].

## Quantitative spectral gap
Assume λ=λ_min(Z_O)<=1/500. Take a unit eigenvector w, set t_i=w·z_i, s_i=t_i², so Σs_i=λ. Project y_i=z_i-t_i w into w⊥≅R^4 and put β_i=||y_i||²=b_i-s_i>=c=187/250. Define u_i=y_i/sqrt(β_i) and v_i=z_i/sqrt(b_i).

For i≠j, |r_ij|=|z_i·z_j|<=1/2. By |t_i t_j|<=(s_i+s_j)/2 and the derivative bound for g(x,y)=1/sqrt(xy) on [c,1]²,
|u_i·u_j-v_i·v_j| <= [1/(2c)+1/(4c²)](s_i+s_j)
= (39000/34969)(s_i+s_j) < (9/8)(s_i+s_j).

Both inner products have absolute value <67/100: the original is <=2/3, and the projected is <= (1/2+λ/2)/c <=501/748<67/100. On this interval, |f'(t)|=|4t³-t/2|<22/25, as checked at the endpoints and the interior critical point t=1/sqrt(24). Thus
f(u_i·u_j) <= f(v_i·v_j)+(99/100)(s_i+s_j).
Summing over ordered pairs yields
4 <= (140/27)A_O+(297/10)λ.
But the right side is <= (140/27)(383/504)+(297/10)(1/500)
=4-329/1215000<4. Contradiction. Therefore λ_min(Z_O)>1/500.

## Frame-independent safe-slack corollary
For all 20 selected edges let M=Σm_i m_i^T. For the 184 zero-contact pairings outside the F3 core, h_ij=1/2-|z_i·z_j| satisfies |m_i·z_j|<=h_ij. Denote by H_OO and H_OC the sums of h_ij² on outside/outside and outside/core pairings. Since m_i·z_i=0,
tr(M Z_O) = Σ_i Σ_{j∈O}(m_i·z_j)² <= 2H_OO+H_OC.
The spectral gap gives tr(M Z_O)>A/500 for A>0; positivity of A follows from the retained 21-line zero-midpoint boundary exclusion. Consequently 2H_OO+H_OC>A/500 and H_184>A/1000. This is independent of the unknown anisotropy of the full projected frame. The matrix gap itself is the main new rank-five constraint for future finite Gram/KKT work.

**[RETAINED]** M(F3)<=89, matching mass >=S/2-28/3, A<=383/504, the six-exception raw-defect results, and source-audited Musin--Boyvalenkov zero-midpoint exclusion. **[OPEN]** Type E, C, D, generic e>=27, non-isolated cases; e=23/24 classification conditional on δ(G)>=1. Global range 40<=tau_5<=44.

Companion exact verifier: research/tau5_typeE_outside16_rank5_spectral_gap_2026-10-25_verify.py.