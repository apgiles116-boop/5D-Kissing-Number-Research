# Type E: exact D5-free outside-sixteen frame gap 1/13

**2026-10-25. [PROVED EXACTLY]** Standalone 16-vector theorem and rational certificate. **[CONDITIONAL ON RETAINED TYPE-E CERTIFICATES]** Application to Type E. **[OPEN]** Type E and tau_5.

## Theorem

For z_1,...,z_16 in R^5 with ||z_i||^2=1-a_i, 0<=a_i<=1/4, sum a_i<=383/504, and |z_i.z_j|<=1/2 for i!=j, the frame F_O=sum_i z_i z_i^T satisfies

    F_O > (1/13) I_5.

The improvement over the previous 1/14 certificate uses q_i+q_j<=delta, not the separate worst-case assumptions q_i=q_j=delta.

## Proof

Suppose a unit x satisfies B=sum_i (x.z_i)^2<=delta=1/13. Put q_i=(x.z_i)^2, w_i=z_i-(x.z_i)x, b_i=||w_i||^2=1-a_i-q_i, and u_i=w_i/sqrt(b_i) in S^3. All b_i>=3/4-delta>0. Then

    |u_i.u_j| <= v_ij=(1/2+sqrt(q_i q_j))/sqrt(b_i b_j).

The degree-four polynomial f(t)=t^4-t^2/4 has 4D Gegenbauer expansion

    f(t)=(1/16)C_0^(1)(t)+(1/8)C_2^(1)(t)+(1/16)C_4^(1)(t).

By positive definiteness and f(1)=3/4, for sixteen points in S^3,

    sum_{i<j} f(|u_i.u_j|) >= (16^2/16-16*3/4)/2=2.    (1)

Since v_ij>=1/2, f(|u_i.u_j|)<=f(v_ij): below 1/2, f<=0; above 1/2, f increases.

For fixed q, the sum of f(v_ij) is jointly convex and increasing in a, because reciprocal square-root products are positive log-convex and f is convex increasing on [1/2,infinity). Its maximum over 0<=a_i<=1/4, sum a_i<=383/504 is at a capped-simplex vertex, necessarily a permutation of

    a*=(1/4,1/4,1/4,5/504,0,...,0).

Let H, M, L be its classes of sizes (3,1,12). Define

    g(d,e)=[1-(1-d)(1-e)]/[16(1-d)^2(1-e)^2],
    G(d)=sum_{i<j}g(d_i,d_j).

Writing u=1-d,v=1-e, the Hessian of g has positive leading diagonal (3-uv)/(8u^4v^2) and determinant (uv-2)(3uv-10)/(256u^6v^6)>0. Thus G is jointly convex and increasing. Exactly,

    G0=G(a*)=9105610/6723027.

For delta=1/13 the coordinate secants [G(a*+delta e_i)-G0]/delta are, by class,

    c_H=13569181756/3529589175 < 385/100,
    c_M=12624681311424/8913311757289 < 142/100,
    c_L=2347319377/1721094912 < 137/100.

Jensen's inequality for q/delta in the simplex gives

    G(a*+q)<=G0+sum_i c_i q_i.                         (2)

**Sharper joint-budget step.** Put c_i*=1-a_i*. Since q_i+q_j<=delta,

    b_i b_j=(c_i*-q_i)(c_j*-q_j)
      >= c_i*c_j* - delta*max(c_i*,c_j*) = D_ij >0.

Here c_i*c_j* denotes the product of the two starred c-values, not a new variable. Let h=(1+delta)/2. The mean-value theorem and monotonicity of f' on [1/2,infinity) yield

    f(v_ij)<=g(a_i*+q_i,a_j*+q_j)+K_ij sqrt(q_i q_j),
    K_ij=4h^3/D_ij^2-h/(2D_ij).                       (3)

The five exact K_ij values (HH, HM, HL, ML, LL) are

    5608/2925, 81104688/80925325, 318/325,
    211307796/465351757, 413/936,

respectively, and are strictly below

    192/100, 101/100, 98/100, 46/100, 45/100.

With t_i=sqrt(q_i), (2)-(3) imply sum f(v_ij)<=G0+t^T B't, where B' has diagonal ceilings 385/100,142/100,137/100 by class and off-diagonal entries half the corresponding K ceiling.

**Exact spectral certificate.** B'<(83/10)I_16. On the H-sum-zero and L-sum-zero subspaces, its eigenvalues are 289/100 and 229/200, respectively. On the three-dimensional group-constant subspace, congruence by class sizes (3,1,12) reduces (83/10)I-B' to

    [ 759/100   -303/200   -441/25 ]
    [-303/200    172/25    -69/25 ]
    [ -441/25    -69/25    2673/50].

Its leading principal minors are

    759/100, 1996959/40000, 645502959/2000000,

all positive. Hence t^T B't <= (83/10)sum q_i <= 83/130, and

    sum_{i<j}f(|u_i.u_j|) <= G0+83/130
        = 2 - 6246479/873993510 <2,

contradicting (1). QED.

## Type E consequence [CONDITIONAL]

The sixteen outside-core projected directions in H=16K2 disjoint_union F3 meet the theorem's assumptions under the retained graph, endpoint, and A<=383/504 certificates. The two-sided safe-pair estimate gives

    2H_184 >= tr(T_O F)+tr(T_C F_O) > A/13  (A>0),

so H_184>=A/26 (strict when A>0). This is a stronger *coercivity* estimate than A/28, but weaker numerically than the retained energy-sensitive Q-rank safe-slack floor. It is not a contradiction.

**[UNCHANGED]** 40<=tau_5<=44; M(F3)<=89; matching mass >=S/2-28/3; total twenty-edge mass >=2137/6; A<=383/504. Types C,D, generic e>=27 and remaining non-isolated cases are open. No D5 identification or new generic SDP is used.

The companion _verify.py checks every rational constant, spectral minor and contradiction margin.