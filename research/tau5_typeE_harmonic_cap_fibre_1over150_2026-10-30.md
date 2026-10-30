# Type E: exact 1/150 D5 support-fibre separation (2026-10-30)

**Proof status:** [PROVED BY EXACT FINITE CERTIFICATE, CONDITIONAL ON RETAINED TYPE-E MASS/GRAPH INPUTS] Every core-star-labeled D5 ten-support-plane model is at projective Frobenius distance **strictly greater than 1/150** from the twenty normalized projected directions of a hypothetical Type-E 41-code. The previous certified radius was 1/360.

**[PROVED CONDITIONALLY]** For each such labeling, the weighted Petersen Q residual satisfies **E=V_z+12C_z>1/101300²**, improving the previous 1/245700² floor by a factor >5.88. **[OPEN]** No incompatible upper bound on E is known; Type E remains open.

## Stronger mass input and its provenance

The repo's 2026-10-28 isolated-center harmonic theorem proves the exact gap B=2595/256 for the nondeep center slack plus degree-2/degree-4 harmonic remainder. The polynomial F(t)=28t⁴−7t² has positive harmonic expansion F=1+(35/3)H₂+28H₄. With T=Σxxᵀ−(41/5)I, q=Σ_{x≠v}(v·x)²−36/5, and center slack N₀=Σ7t²(1−4t²), the harmonic Cauchy estimates imply

(35/6)||T||²+14K₄ >= 10+(35/64)(5q+4)²

for q≥−12/7; for smaller q the quadratic term alone exceeds 150/7. Capped-simplex concentration yields N₀≥(7/2)dist(32/5+q+4/5,(1/4)Z), and the one-variable minimum is B=2595/256.

With D(a)=196a−644a²+896a³−448a⁴, the retained F3 mass/matching inequalities imply D_I+Xi≤15−B=1245/256 and D_C+(D_I+Xi)/2≤169/3−B/2, Xi≥0. Write x=Σ_I a_i, y=Σ_C a_i, r=D⁻¹(1245/256), s(x)=D⁻¹(43/3−(B+D(x))/2). Concavity gives x≤r and y≤1/2+s(x) (the y≤1/2 case is immediate). Since D'(s)>129, D'(x)≤196, we have s'(x)>−98/129>−1; hence A≤1/2+r+s(r). Exact rational brackets D(17/625)>1245/256 and D(199/5000)>41/6 give **A<567/1000**. This is stronger than the historical A≤383/504, and is conditional on the retained mass theorems.

## Robust 24-safe-block estimate

Let ε=1/150, u_i=z_i/sqrt(1−a_i), and compare with an arbitrary support-plane model f_i (ten orthonormal pairs on the ten K5 coordinate supports, with four core indices on star supports). Suppose all sign-aligned vector distances are ≤ε. Of thirty meeting-support blocks, discard six star-star blocks; the remaining 24 are fully safe, with support degrees 3 (four star supports) and 6 (six nonstar supports).

For each fully safe block choose the model pair with largest contact. With t_e=|cos2θ_e|, w_i=1−a_i≥3/4, c=(1+4ε)²=(77/75)², the Walsh safety constraint gives w_iw_j(1+t_e)(1+t_f)≤c. Since 1/((1−a)(1−b))≤1+(14/9)(a+b) for a,b∈[0,1/4], summing the 24 inequalities gives

**T_C+2T_N ≤ 8(c−1)+(28c/9)A < 3222689/1406250.**

Each support also has t_e≤(16/9)c−1<15/17=2κ/(1+κ²), κ=3/5. Therefore sqrt(1−t_e²)≥1−κt_e.

For isolated unit center v, put p_j=(v·e_j)² sorted decreasing, Σp_j=1. The center cap |v·z_i|≤1/2 implies p₁+p₂≤2/3+3ε=103/150. For every support ij the center's two squared model contacts yield

t_ij ≥ [ (sqrt(p_i)+sqrt(p_j))²−103/150 ]₊ / [p_i−p_j+(6/5)sqrt(p_i p_j)].

Let F(p) be the sum of these ten terms. **[EXACT FINITE CERTIFICATE]** On the sorted simplex with p₁+p₂≤103/150, F(p)≥7/3. The accompanying verifier subdivides the rational simplex by longest-edge bisection. On each cell, if l_i≤Dp_i≤h_i, it lower-bounds a positive summand by

[150(l_i+l_j+2 floor(sqrt(l_i l_j)))−103D]₊ / [150(h_i−l_j)+180 ceil(sqrt(h_i h_j))].

It prunes only when 150(l₁+l₂)>103D or when the sum of exact lower bounds reaches 7/3. **Executed:** 759,391 cells; 44,395 domain prunings; 335,301 function-bound prunings; maximum depth 34; zero unresolved cells. All pruning decisions are integer/rational.

Thus T_C+T_N≥7/3, contradicting the previous upper bound with exact gap

**7/3−3222689/1406250=58561/1406250>0.**

The comparison assumption is impossible. Sign-aligned vector distance is no greater than rank-one-projector Frobenius distance, proving the projective radius >1/150. The actual Type-E vectors were **not** assumed D5-aligned.

## Weighted Q residual corollary

Retain the exact weighted Petersen identity E=V_z+12C_z and the inverse-Q rounding lemma from the 2026-10-30 research notes. Put b=1−A/20>19433/20000, ρ²=2C_u+V_u/10, δ=sqrt(3)(2sqrt(O_u)+5ρ+ρ²), h=ρ+22δ. Weighted Q-SOS gives ρ<(sqrt(2)/b)sqrt(E) and sqrt(O_u)≤(sqrt(2)/3)sqrt(E). For sqrt(E)≤1/1000, exact rational upper bounds sqrt(2)<99/70 and sqrt(3)<26/15 give h<(3151/10)sqrt(E). If E≤1/101300², then h<1/10 and the retained inverse-rounding theorem constructs a model with vector distance ≤(15/7)h<1/150, contradiction. Hence **E>1/101300²**.

**Limitations:** This is a positive necessary *lower* bound, not a Type-E exclusion. No one-to-one identification between six exceptional core pairings and six Q-kernel modes is assumed. Types C,D, generic e≥27 and non-isolated branches remain open; e=23/24 classification requires δ(G)≥1. Retain M(F3)≤89, M(P)≥S/2−28/3, the Musin/Boyvalenkov zero-midpoint boundary, and the global proved **40≤τ₅≤44**.

Verifier: `research/tau5_typeE_harmonic_cap_fibre_1over150_2026-10-30_verify.py`.
