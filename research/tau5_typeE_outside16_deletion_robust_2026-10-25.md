# Type E: deletion-robust outside-16 frame (exact)

**2026-10-25 — [PROVED EXACTLY UNDER RETAINED TYPE-E HYPOTHESES].** Type E remains open; global proved range stays 40 <= tau_5 <= 44.

## Results

For the 16 outside-core selected deep edges in H=16K2 ⊔ F3, write x_i^±=m_i±z_i, a_i=||m_i||², Z_O=Σ_{i∈O}z_i z_iᵀ. Retain 0<=a_i<=1/4, Σ_{i∈O}a_i<=B=383/504, and |z_i·z_j|<=1/2 (i≠j).

**(A) Robust one-deletion spectral gap:** For *every* k∈O,

    Σ_{i∈O\{k}} z_i z_iᵀ ≻ (1/65) I_5.

In particular, every 15 of the 16 outside-core vectors span R⁵.

**(B) Improved full-frame spectral gap:**

    Z_O ≻ (5/88) I_5,

strictly improving the previous >1/18 bound.

**(C) Independent rank-four energy obstruction:** If 15 such vectors lie in a four-dimensional subspace, their midpoint energy E obeys

    E >= 3/4+(604-3√37727)/199 = 0.857019178655... > B.

No D5 labeling or new SDP is assumed.

## Proof

On S³ let f(t)=t⁴-t²/4. The normalized Gegenbauer expansion f=(1+6P₂+5P₄)/16 and positivity of the P₂,P₄ kernels give, for n unit vectors u_i∈R⁴,

    Σ_{i≠j} f(u_i·u_j) >= n(n-12)/16.                 (1)

The right side is 45/16 for n=15, and 4 for n=16.

Define

    F_n(c)=(1/8)Σ_{i<j}[(1-c_i)^(-2)(1-c_j)^(-2)
                         -(1-c_i)^(-1)(1-c_j)^(-1)].

If |u_i·u_j|<=1/[2√((1-c_i)(1-c_j))], then Σ_{i≠j}f(u_i·u_j)<=F_n(c), because f(t)<=f(C) for |t|<=C and C>=1/2. F_n is increasing and Schur-convex: for g(a,b)=x²y²-xy with x=(1-a)^(-1), y=(1-b)^(-1), we have ∂_a g=2x³y²-x²y>0, ∂²_aa g=2x³y(3xy-1)>0, and ∂_a g-∂_b g=xy(x-y)(2xy-1)>=0 when a>=b. The remaining third-index terms obey the same derivative ordering by convexity. Thus F_n preserves weak majorization.

Suppose the minimum eigenvalue of a selected n-vector frame is λ<=L. Choose a unit minimum-eigenvector w, set s_i=(w·z_i)², Σs_i=λ<=L, and normalize the projections y_i=z_i-(w·z_i)w to u_i=y_i/√(1-a_i-s_i)∈R⁴. All denominators are positive for L<=5/88. Since |z_i·z_j|<=1/2,

    |y_i·y_j| <= 1/2+√(s_i s_j)
               <= 1/2√((1+2s_i)(1+2s_j)),

where the second inequality follows by squaring: the difference is 2(√s_i-√s_j)²>=0. Therefore the normalized u_i satisfy the F_n correlation cap with **improved effective energy**

    c_i=(a_i+3s_i)/(1+2s_i)
       =a_i+(3-2a_i)s_i/(1+2s_i).                   (2)

For any subset S of k indices, with T=Σ_{i∈S}s_i<=L, concavity of s/(1+2s) and a_i<=1/4 give, for k=1,2,3,

    Σ_{i∈S}c_i <= k/4+(5/2)L/(1+2L/k).             (3)

For 4<=k<=n, using Σa_i<=B gives

    Σ_{i∈S}c_i <= B+3L/(1+2L/n).                   (4)

Let p₀=0, p_k=k/4+(5/2)L/(1+2L/k) (k=1,2,3), and p₄=B+3L/(1+2L/n). The decreasing, nonnegative vector

    v=(p₁,p₂-p₁,p₃-p₂,p₄-p₃,0,...,0)

weakly majorizes c. Hence F_n(c)<=F_n(v).

**n=15, L=1/65:** Exact rational evaluation yields

    v=(77/268,554/2211,3253/13002,1737245/97004376,0,...,0),
    45/16-F_15(v)
      =5866345701401123500770801473878609
       /1382413759409611499364656376631907344 >0.

This contradicts (1). The subset of 15 was arbitrary, proving (A).

**n=16, L=5/88:** Exact rational evaluation yields

    v=(37/98,2341/9114,6433/25482,2071375/48955032,0,...,0),
    4-F_16(v)
      =2348317102745552158431009828140393
       /272294670071050190567861135193103682 >0.

Again (1) is contradicted, proving (B).

For (C), if the n=15 vectors lie in R⁴, use c_i=a_i directly. By Schur-convexity, the capped vector (1/4,1/4,1/4,u,0,...,0), u=E-3/4∈[0,1/4], maximizes F_15 for fixed E∈[3/4,1]. Direct calculation gives

    45/16-F_15=(199u²-1208u+127)/[432(1-u)²].

The smaller root is (604-3√37727)/199. For E<=3/4 the capped maximum is already below 45/16; E>=1 trivially exceeds the claimed threshold. Thus (C) follows.

## Type-E consequence and proof ledger

For any core midpoint m_i and any outside index k, the 15-vector spectral bound implies Σ_{j∈O\{k}}(m_i·z_j)² > a_i/65 when a_i>0. The retained zero-contact endpoint slack inequality |m_i·z_j|<=h_ij=1/2-|z_i·z_j| transfers this to the same leave-one-out sum of h_ij².

The full-frame improvement yields H_184 > (5/176)(A+A_C) >= (5/176)A when A>0, by the previously established safe-slack transfer.

**[RETAINED, NOT REPROVED]** M(F3)<=89, matching bound S/2-28/3, 20-edge mass >=2137/6, A<=383/504, and the Musin–Boyvalenkov zero-midpoint exclusion.

**[OPEN]** Four-core Gram contradiction; Type E; Types C, D; generic e>=27; non-isolated branches. Sparse e=23,24 classification still assumes δ(G)>=1.

Companion exact checker: `research/tau5_typeE_outside16_deletion_robust_2026-10-25_verify.py`.
