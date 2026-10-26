# Quantitative 21-line integrality stability in R^5

Date: 2026-10-26. **[PROVED EXACTLY]** For ANY 21 unit vectors u_0,...,u_20 in R^5, put s_ij=(u_i.u_j)^2 and

    P = sum_{i<j} [s_ij(s_ij-1/4)]_+.

Then **P>1/80**. This supplies a self-contained quantitative strengthening of the 21-line zero-midpoint exclusion. It does not use D5 labeling, SDP, or packing uniqueness.

## 1. Harmonic identity

Let F=sum u_i u_i^T, H=F-(21/5)I, V=||H||_F^2, S=sum_{i<j}s_ij and T=sum_{i<j}s_ij^2. Frame trace gives S=168/5+V/2. Positivity of the dimension-five degree-four spherical harmonic P4(t)=(21t^4-14t^2+1)/8 yields T>=(2/3)S-14. Let E=sum_{s<=1/4}s(1/4-s). Since T-S/4=P-E,

    P-E >= (5/24)V,    V <= (24/5)P,    E<=P-(5/24)V.  (1)

## 2. Rounded contact graph

Choose b_ij=1 for s_ij>=1/8, otherwise 0; let K=sum_{i<j}b_ij and k_i=sum_{j!=i}b_ij, so sum k_i=2K. Set

    e_i=u_i^T H u_i,
    c_i=k_i/4-16/5,
    d_i=sum_{j!=i}(s_ij-b_ij/4)=e_i-c_i.

Then sum e_i=V and sum d_i=V+336/5-K/2. Pointwise rounding gives |s-b/4|<=8s(1/4-s) for s<=1/4, and <=4s(s-1/4) for s>1/4. Thus

    L:=sum_i |d_i| <=16E+8P <=24P-(10/3)V.           (2)

For every integer k, |k/4-16/5|>=(40-3k)/20, with equality at k=12,13. Hence

    sum_i |c_i| >= (840-6K)/20.                       (3)

## 3. Q-Gram spectral control

Q_i=u_i u_i^T-I/5 has Gram matrix G_ij=s_ij-1/5 (diagonal 4/5). Every off-diagonal absolute value is <=1/5+(s_ij-1/4)_+. Since sum(s_ij-1/4)_+<=4P, Gershgorin yields lambda_max(G)<=24/5+4P. Because H is traceless, e_i=tr(Q_i H), so

    sum_i e_i^2 <= (24/5+4P)V.                       (4)

## 4. Exact rational contradiction

Suppose P<=1/80. By (1)-(2), 0<=V<=3/50 and L<=3/10-(10/3)V. From |V+336/5-K/2|<=L, K<=133 and K>=136 are impossible. If K=135, the same inequality forces V=0; then e_i=0 and L=sum|c_i|>=3/2 by (3), contradicting L<=3/10. Therefore K=134.

For K=134, (2) gives V+1/5<=3/10-(10/3)V, hence V<=3/130. Also sum|c_i|>=9/5, so

    sum|e_i| >=9/5-L >=3/2+(10/3)V.

By Cauchy-Schwarz,

    sum e_i^2 >=[3/2+(10/3)V]^2/21
               >=3/28+(10/21)V.

But (4) and P<=1/80 give sum e_i^2<=(97/20)V. Therefore

    V >=45/1837 >3/130,

an exact contradiction (45*130=5850>5511=3*1837). Thus **P>1/80**.

## 5. Type E status

For the Type-E normalized 21-vector system (isolated center and z_i/sqrt(1-a_i)), the universal inequality applies. The previously retained *conditional* endpoint estimate P<=K_C(t)A for A<=t, with K_C(t)=[17+(1+t)^2(7+t)]/[16(1-t)^2], implies A>1/125, since at t=1/125 the exact margin is 1/80-t*K_C(t)=939499/3844000000>0. **This is weaker than the already retained A>1/99 and does not strengthen the Type-E energy interval.**

**[PROVED EXACTLY]** Universal theorem and zero-defect 21-line corollary.
**[CONDITIONAL]** Type-E normalized defect cap and its A>1/125 corollary.
**[OPEN]** Type E, C, D, generic e>=27, and non-isolated branches. Retain 40<=tau_5<=44; F3 star<=70/3, M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass>=2137/6, A<=383/504. Sparse e=23/24 classification requires delta(G)>=1.
