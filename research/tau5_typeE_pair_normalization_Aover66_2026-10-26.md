# Type E: pairwise normalization, a universal 21-line gap, and A > 1/66

Date: 2026-10-26. Builds on the consolidated 2026-09-05 ledger and the 2026-10-26 rounded-Gershgorin certificate.

**[PROVED EXACTLY — UNIVERSAL]** For any 21 unit vectors in R^5, with s_ij=(u_i.u_j)^2 and P=sum_{i<j}[s_ij(s_ij-1/4)]_+, **P>1/59**.

**[PROVED EXACTLY — CONDITIONAL TYPE E]** For 20 disjoint deep edges, a_i=||m_i||^2, A=sum a_i, C=sum of the four F3 matching-core a_i, and k_i the rounded degree (s_ij>=1/8) of the 21 normalized directions including the isolated center, the new independently derived defect bound is

    P <= [sum_i k_i*a_i + 4C + 9C^2 + 5C^3 + C^4]/[16(1-A)^2].

Consequently **1/66 < A <= 383/504**. This does not eliminate Type E.

## Universal proof

Set F=sum_i u_i u_i^T, H=F-(21/5)I, V=tr(H^2), E=sum_{s<=1/4}s(1/4-s). Degree-four harmonic positivity gives P-E>=5V/24. Round s_ij to b_ij/4 at s=1/8. With K=sum b_ij, k_i=sum_j b_ij, c_i=k_i/4-16/5, e_i=u_i^T H u_i, d_i=e_i-c_i:

    R=sum_{i<j}|s_ij-b_ij/4| <=12P-5V/3,
    sum_i|d_i|<=24P-10V/3,
    sum_i d_i=V+336/5-K/2,
    |c_i|<=12P+3/25.

For P<=1/59, these imply K=134 or 135, all k_i in {12,13,14}, and V<=v_K(P), with v_134(P)=3(24P-1/5)/13 and v_135(P)=3(24P-3/10)/7.

For Q_i=u_i u_i^T-I/5, the PSD Q-Gram B has B_ii=4/5, B_ij=s_ij-1/5, B*1=e, 1^T B 1=V. Rounded Gershgorin gives sum_i e_i^2 <=(3+12P-5V/3)V.

For lambda>=0 and eta real, define g(c)=min_t[t^2-eta*t+lambda*|t-c|]. It is convex, and its minimizer is clip(c, (eta-lambda)/2,(eta+lambda)/2). Hence

    sum_i e_i^2 >= sum_i g(c_i)-24lambda*P+(10lambda/3+eta)V.

Discrete convexity gives the minimum degree-cost patterns (n12,n13,n14)=(5,16,0) for K=134 and (3,18,0) for K=135. Put p=1/59, B_K=3+12p-10lambda/3-eta. The two bounds would require

    0 >= C_K-24lambda*p-B_K*V+(5/3)V^2.

The right side decreases on 0<=V<=v_K(p), yet at its right endpoint it is strictly positive:

| K | lambda | eta | C_K | v_K(p) | positive margin |
|---|---|---|---|---|---|
| 134 | 3/10 | 0 | 91/400 | 183/3835 | 969259/235315600 |
| 135 | 1/2 | -3/7 | 2841/9800 | 27/590 | 2091/34113800 |

Therefore P>1/59.

## Four-core Gram budgets and new normalization

For the four core midpoints m_i, C=sum||m_i||^2. Endpoint upper bounds imply delta_ij=(|z_i.z_j|-1/2)_+ <=(-m_i.m_j)_+. Both functionals sum(-G_ij)_+ and sum(-G_ij)_+^2 are convex on the PSD 4x4 Gram matrices of trace C, so their maxima occur at rank one G=vv^T. Partitioning v into positive/negative coordinates proves

    sum delta_ij<=C, sum delta_ij^2<=C^2/4, max delta_ij<=C/2.

Thus the raw core quartic excess and squared excess obey

    E4=sum_core [(z_i.z_j)^2*((z_i.z_j)^2-1/4)]_+
       <= C/4+5C^2/16+C^3/4+C^4/16,
    sum_core [ (z_i.z_j)^2-1/4 ]_+ <= C+C^2/4.

Take y_0=x_0 and y_i=z_i, r_i=||y_i||^2=1-a_i, a_0=0, u_i=y_i/sqrt(r_i). For each pair write x=(y_i.y_j)^2 and d=r_i*r_j. Only six core pairs can have raw x>1/4. Crucially,

    d=(1-a_i)(1-a_j)>=1-a_i-a_j>=1-A.

For every normalized-positive pair x/d>1/4 (hence b_ij=1), use the identity

    x(x-d/4)=x(x-1/4)+(1-d)x/4.

Its positive numerator is bounded by [x(x-1/4)]_+ +(1-d)/16 +(1-d)[x-1/4]_+/4. The first term sums to E4. The second is at most sum_i k_i*a_i/16. The third occurs only in the core and is at most C(C+C^2/4)/4. Divide by d^2>=(1-A)^2 and combine the core bounds to obtain the stated new defect inequality.

If k_i<=k, it yields the increasing scalar bound

    P<=U_k(A):=[(k+4)A+9A^2+5A^3+A^4]/[16(1-A)^2].

## Exact Type-E bootstrap

Suppose A<=a=1/66. Initially k_i<=20:

    P<=U_20(a)=533803/22651200<7/240,
    9/20-12U_20(a)-3/25=17821/377520>0.

Therefore K in {134,135} and all k_i in {12,13,14}. Then P<=p14=U_14(a)=5214463/294465600. If any degree 14 occurs, convexity raises the minimum Huber degree cost. Using the full quadratic frame bound as above gives:

| K | lambda | eta | min degree cost with degree 14 | positive margin |
|---|---|---|---|---|
| 134 | 3/10 | 0 | 131/400 | 506645887636151/5653544845520000 |
| 135 | 1/5 | -1/10 | 99/400 | 41873920448669/1639193475920000 |

Both are positive, so all k_i<=13. But then

    P<=U_13(a)=4926967/294465600,
    1/59-U_13(a)=3774547/17373470400>0,

contradicting the universal theorem. Hence **A>1/66**.

**[OPEN]** Type E, Types C and D, generic e>=27, and non-isolated graph branches. Retain M(F3)<=89, M(P)>=S/2-28/3, 20-edge mass>=2137/6, A<=383/504. The e=23/24 sparse classification requires delta(G)>=1. Global proved range remains 40<=tau_5<=44. No D5 labeling or new generic SDP is used.

Companion exact verifier: `tau5_typeE_pair_normalization_Aover66_2026-10-26_verify.py`.
