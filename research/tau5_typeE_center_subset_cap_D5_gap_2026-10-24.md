# Type E: labeling-free center/subset cap and strict D5-template energy gap (2026-10-24)

**Proof status:** [PROVED EXACTLY] universal subset inequality. [PROVED EXACTLY, CONDITIONAL ON NORMALIZED D5 TEMPLATE] strict energy gap. [OPEN] Type E elimination.

## 1. Universal center/subset cap

Let u be an isolated unit center and x_i^± = m_i ± z_i be unit endpoints of k distinct selected deep edges, with m_i·z_i=0, a_i=||m_i||²≤1/4 and ||z_i||²=1-a_i. Assume all distinct endpoints satisfy pairwise inner product ≤1/2, including the center. Orient z_i so u·z_i≥0 and choose the actual endpoints y_i=m_i-z_i. The center inequalities give u·y_i ≤1/2-2|u·z_i|. The kissing inequalities give ||Σ y_i||² ≤ k+k(k-1)/2 = k(k+1)/2. Since u·Σy_i ≥ -||Σy_i||, we obtain

**2 Σ_(i∈I) |u·z_i| ≤ k/2 + sqrt(k(k+1)/2).** (1)

This holds for every subset I, without D5 labeling, SDP, or a rank-five template. At k=10 the right side is 5+sqrt(55). No sharpness claim for k>1.

## 2. Ten aligned D5 lines

Assume additionally the twenty normalized projected lines v_i=z_i/sqrt(1-a_i) are exactly the D5 lines (e_j±e_l)/sqrt(2) after one orthogonal transformation and relabeling. For each j<l choose the line with representative v_jl=(sgn(u_j)e_j+sgn(u_l)e_l)/sqrt(2). Put c_jl=u·v_jl=(|u_j|+|u_l|)/sqrt(2), so Σ_(j<l)c_jl=2sqrt(2)||u||_1.

For 0≤a≤1/4, sqrt(1-a)≥1-κa with κ=1/(1+sqrt(3)/2)=4-2sqrt(3). Applying (1) to these ten lines yields

**2κ c_max A ≥ 4sqrt(2)||u||_1 - 5 - sqrt(55),** (2)

where c_max=max c_jl and A is the total midpoint energy of all twenty edges.

## 3. Exact positive energy gap

Reuse the previously established center-only D5 stability identity

A ≥ B0+(α/2)T, B0=9/2-3sqrt(2), α=25(sqrt(2)-1)/16,
T=Σ_j(u_j²-1/5)². (3)

We prove the stronger full-endpoint necessary condition

**A ≥ 9/2-3sqrt(2)+(sqrt(2)-1)/640 = 0.2580065215719228...** (4)

If T≥1/500, (3) proves (4). Otherwise each u_j² lies between 1/5±sqrt(T); sqrt(1/500)<9/200 gives u_j²>31/200 and c_max<7/10. Taylor's theorem for sqrt(x), with f''(x)=-1/(4x^(3/2)), yields

||u||_1 ≥ sqrt(5)-T/[8(1/5-sqrt(T))^(3/2)] > 2236/1000-5/1209 = 674581/302250.

Here sqrt(31/200)>39/100. Also sqrt(2)>1414/1000, sqrt(55)<7417/1000, and κ<27/50. Substitution in (2) gives the exact rational bound

A > [4(1414/1000)(674581/302250)-5-7417/1000]/[2(27/50)(7/10)]
  = 31195943/114250500 > 27/100.

Since the right side of (4) is <27/100, (4) follows in both cases. The exact verifier checks every rational/square comparison.

The center-only equality witness from the preceding D5 energy note is therefore incompatible with *all* endpoint kissing constraints. This gap is small but strictly positive and requires no numerical optimization.

## Status and limitations

[PROVED EXACTLY] (1), universally. [PROVED EXACTLY, D5-TEMPLATE CONDITIONAL] (2) and (4). [REUSED] Prior center-only D5 stability identity (3). [OPEN] D5 labeling of arbitrary Type E, Type E elimination, C/D and generic e≥27. The new lower bound is far below the retained Type E upper bound A≤383/504; no global contradiction follows. The proved global range remains 40≤tau_5≤44; F3 broom M(F3)≤89 and matching M(P)≥S/2-28/3 are unchanged.
