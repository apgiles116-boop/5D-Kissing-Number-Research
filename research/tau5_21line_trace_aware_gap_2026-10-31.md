# Trace-aware quantitative obstruction for 21 projective lines in R^5

Date: 2026-10-31. **[PROVED EXACTLY]** Universal quartic and coherence-defect gaps. **[OPEN]** No Type-E exclusion.

## Theorem
For 21 unit vectors u_i in R^5 let b_ij=(u_i·u_j)^2, P=sum_{i<j}[b_ij(b_ij-1/4)]_+, and D=sum_{i<j}(|u_i·u_j|-1/2)_+. Then

    P > 3/196 = 0.01530612244897959...
    D > 1/98 = 0.01020408163265306...

This strengthens the earlier P>71/5000 and does not assume D5 uniqueness.

## Exact proof
Put T=sum_i u_i u_i^T, B=T-(21/5)I, V=tr(B^2), f(b)=b(b-1/4), F=sum f(b_ij), N=sum[-f(b_ij)]_+. Degree-four Gegenbauer positivity gives

    t^4-t^2/4=1/28+(1/3)P_2(t)+(8/21)P_4(t)
    P_2(t)=(5t^2-1)/4, P_4(t)=(21t^4-14t^2+1)/8
    F=(5/24)V+(4/21)sum_{i,j}P_4(u_i·u_j)>=(5/24)V.

Assume P<=p=3/196. Then N<=p. For 0<b<1/4, b(1/4-b)<=p implies b<=3/28 or b>=1/7. Round b to k/4, k=0 if b<1/8 and k=1 otherwise; b=1/8 is impossible because 1/64>p. On the allowed negative-f intervals, |b-k/4|<=7[-f(b)]_+. For b>=1/4, |b-1/4|<=4[f(b)]_+. Thus E=sum|b_ij-k_ij/4| obeys

    E<=7N+4P=11P-7F
    2E<=22p-(35/12)V=L-kappa V,
    L=33/98, kappa=35/12.

Also V<=24p/5<1/10 and 2sum b_ij=336/5+V=67+1/5+V. Since 2sum k_ij/4 is a half-integer within 2E<=L<0.337, K=sum k_ij must be 134 or 135.

Let k_i=sum_{j!=i}k_ij, c_i=k_i/4-16/5, d_i=u_i^T B u_i, delta_i=d_i-c_i. Then

    sum_i |delta_i|<=B_0(V):=L-kappa V,
    sum_i d_i=V, sum_i k_i=2K.

The unit-vector Cauchy inequality and the traceless 5x5 eigenvalue bound give

    sum_i d_i^2 <=tr(B^2 T)
      <=(21/5+sqrt(4V/5))V.                                (A)

**K=134.** The balanced integer vector with sum 268 has five 12s and sixteen 13s. Any integer vector of this sum majorizes it. The squared distance from the affine degree vector to an l1 ball is symmetric convex, hence Schur-convex, so the balanced vector minimizes the possible sum d_i^2. Its c entries are five -1/5 and sixteen 1/20. Since B_0<=L<3/4, optimal correction shrinks only the five largest absolute entries:

    sum d_i^2 >= (1-B_0(V))^2/5+1/25.                     (B)

The exact delta sum is V+1/5, requiring V+1/5<=B_0(V), hence V<=v_134=402/11515<1/20. Thus (A)<(22/5)V. The difference (B)-(22/5)V decreases with V (derivative at most 7/6-22/5<0), and at v_134 equals

    (4/5-v_134)^2/5+1/25-(22/5)v_134
      =459297/132595225>0.

Contradiction.

**K=135.** The balanced degree vector with sum 270 has three 12s and eighteen 13s. To retain the trace, minimize sum (k_i/4-16/5+delta_i)^2 subject to sum delta_i=V-3/10 and sum|delta_i|<=B_0(V). This minimum is convex symmetric in k and thus Schur-convex, so it is minimized by the balanced vector. Put q=3/10-V>0. Since sum delta=-q, total positive delta is at most (B_0-q)/2. Feasibility requires q<=B_0, giving

    V<=v_135=108/5635<1/20,
    (B_0-q)/2<=(L-3/10)/2=9/490.

On the three rows with c=-1/5, the corrected values sum to at most -3/5+9/490=-57/98. Therefore by Cauchy,

    sum_i d_i^2 >= (57/98)^2/3=1083/9604.

But (A)<(22/5)v_135, and

    1083/9604-(22/5)v_135=157029/5522300>0.

Contradiction. Hence P>3/196. Finally s^2(s^2-1/4)<=(3/2)(s-1/2) for 1/2<=s<=1, so P<=(3/2)D and D>1/98.

## Conditional Type-E consequence
Under the previously retained isolated-center selected-edge/Walsh normalization lemma, with D_C the six-core raw defect, A total midpoint energy, and K_safe>=0 the safe Walsh correction,

    D_norm <= (4/3)D_C+T(a)-K_safe,
    (3/4)T(a)<=(18sqrt(3)-53/2)A.

The universal bound D_norm>1/98 therefore gives

    D_C+(18sqrt(3)-53/2)A > 3/392+(3/4)K_safe.

With the retained midpoint-frame estimate K_safe>=[A_I^2/5-U_I]_+, the right side is at least 3/392+(3/4)[A_I^2/5-U_I]_+. This is not yet a contradiction.

## Status
**[PROVED EXACTLY]** Universal 21-line theorem. **[PROVED CONDITIONALLY]** Type-E corollary, assuming the earlier Walsh lemma. **[VERIFIED LOCALLY]** All rational margins and harmonic-polynomial identities with SymPy. **[OPEN]** Type E, C, D, generic e>=27, and non-isolated branches. Retain M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, Musin/Boyvalenkov antipodal boundary theorem, and sparse-classification condition delta(G)>=1. Global proved range remains 40<=tau_5<=44.
