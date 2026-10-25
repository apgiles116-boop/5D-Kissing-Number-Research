# Type E: exact D5-free outside-sixteen frame gap 1/14

**2026-10-25.** **[PROVED EXACTLY]** The 16-vector theorem below. **[CONDITIONAL ON RETAINED TYPE-E CERTIFICATES]** Its application to the 16 outside-core deep edges. **[OPEN]** Type E and tau_5.

## Theorem

Let z_1,...,z_16 in R^5 obey ||z_i||^2=1-a_i, 0<=a_i<=1/4, sum a_i<=383/504, and |z_i.z_j|<=1/2 for i!=j. Then

    F_O = sum_i z_i z_i^T  >  (1/14) I_5

in the positive-definite order. This strengthens the previous exact 1/27 bound without any D5 identification.

## Proof: 4D polynomial obstruction

Suppose some unit x satisfies B=sum_i(x.z_i)^2<=delta=1/14. Put q_i=(x.z_i)^2, b_i=1-a_i-q_i, u_i=(z_i-(x.z_i)x)/sqrt(b_i) in S^3, p_ij=sqrt(q_i q_j), and v_ij=(1/2+p_ij)/sqrt(b_i b_j). Since b_i>=3/4-delta, |u_i.u_j|<=v_ij.

For f(s)=s^4-s^2/4, the exact S^3 Gegenbauer expansion is

    f = (1/16) C_0^(1) + (1/8) C_2^(1) + (1/16) C_4^(1).

All coefficients are nonnegative; f(1)=3/4. The addition theorem for 16 unit vectors gives

    sum_{i<j} f(|u_i.u_j|) >= (16^2/16 - 16*(3/4))/2 = 2.    (1)

Because v_ij>=1/2, f is convex and increasing on [1/2,infinity), while f(s)<=0 for 0<=s<=1/2. Thus f(|u_i.u_j|)<=f(v_ij).

For fixed q, the function sum_{i<j} f(v_ij) is convex and increasing in a: reciprocal geometric means are log-convex, and f is convex and increasing on the relevant range. Its maximum over 0<=a_i<=1/4, sum a_i<=383/504 is therefore attained at a permutation of

    a*=(1/4,1/4,1/4,5/504,0,...,0).

Label the three entries 1/4 as H, the one 5/504 as M, and the remaining twelve as L.

Let g(d,e)=[1-(1-d)(1-e)]/[16(1-d)^2(1-e)^2], and G(d)=sum_{i<j}g(d_i,d_j). The identity f(1/(2sqrt(b_i b_j)))=g(a_i+q_i,a_j+q_j) holds. The Hessian of g has positive leading entry and determinant (uv-2)(3uv-10)/(256u^6v^6)>0, where u=1-d and v=1-e. Thus G is increasing and convex. Jensen's inequality on the simplex sum q_i<=delta yields

    G(a*+q) <= G0 + sum_i c_i q_i,

where G0=9105610/6723027 and the exact coordinate secant slopes obey

    c_H=27586331276/7281038241 < 379/100,
    c_M=74735317440/53378095369 < 141/100,
    c_L=226951305/168324676 < 135/100.                 (2)

Set h=(1+delta)/2 and D_IJ=(1-a*_I-delta)(1-a*_J-delta). The mean-value theorem, p_ij<=delta/2, and f'(s)=4s^3-s/2 imply

    f(v_ij) <= g(a_i+q_i,a_j+q_j) + K_IJ sqrt(q_i q_j),
    K_IJ=4h^3/D_IJ^2 - h/(2D_IJ).                        (3)

Exact rational upper bounds are K_HH<232/100, K_HM<116/100, K_HL<113/100, K_ML<54/100, K_LL<52/100.

Write t_i=sqrt(q_i)>=0. Equations (2)-(3) imply

    sum_{i<j} f(v_ij) <= G0 + t^T B' t,

where B' is symmetric, with diagonal (379/100,141/100,135/100) by class and off-diagonal entries one-half the respective K ceiling.

**Rational spectral certificate:** 9I_16-B' is positive definite. On the H- and L-sum-zero subspaces the eigenvalues of B' are respectively 379/100-232/200 and 135/100-52/200, both <9. On the group-constant subspace, congruence with diag(3,1,12) yields the symmetric matrix

    [ 867/100    -87/50     -1017/50 ]
    [ -87/50     759/100    -81/25   ]
    [ -1017/50   -81/25     1437/25  ].

Its leading principal minors are 867/100, 627777/10000, 18501129/125000, all strictly positive. By Sylvester's criterion, t^T B' t <9 sum_i q_i<=9/14 when t!=0. Hence

    sum_{i<j} f(|u_i.u_j|) <= G0+9/14
        = 2 - 258973/94122378 < 2,

contradicting (1). Therefore F_O > I_5/14. QED.

## Conditional Type-E consequence

For H=16K2 disjoint_union F3, the outside sixteen projected vectors satisfy the theorem's hypotheses. With midpoint energy A=sum_i ||m_i||^2 and the retained two-sided safe-pair estimate,

    2 H_184 >= tr(T_O F)+tr(T_C F_O) >= tr(T_O F_O)+tr(T_C F_O) >= A/14,

with strict inequality when A>0. Thus **H_184>=A/28** (strict if A>0). This improves the earlier *coercivity* consequence A/54, but remains weaker than the retained Q-rank safe-slack floor 13808395/21337344; it does not exclude Type E.

**[OPEN]** Type E, C, D, generic e>=27, non-isolated cases. **[UNCHANGED]** 40<=tau_5<=44; M(F3)<=89; M(P)>=S/2-28/3; twenty-edge mass >=2137/6; A<=383/504. No correspondence of the six exceptional core pairings with the six D5 Q-kernel relations is assumed.

The companion exact-rational Python verifier checks all rational constants, the 3-class positive-definite certificate, and the strict contradiction margin.