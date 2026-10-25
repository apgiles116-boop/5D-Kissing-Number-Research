# Type E: a D5-free spectral gap for the 16 outside-core projected vectors

**Date:** 2026-10-25. **Status:** [PROVED EXACTLY] the conditional vector theorem and rational certificate; [CONDITIONAL ON RETAINED TYPE-E MODEL] the application to 16K2 + F3; [OPEN] Type E exclusion and tau_5.

## Theorem

Let z_1,...,z_16 in R^5 satisfy ||z_i||^2=1-a_i, 0<=a_i<=1/4, sum a_i<=383/504, and |z_i.z_j|<=1/2 for i!=j. Then

    F_O = sum_i z_i z_i^T  ≻  (1/27) I_5.

The constant is certified, not claimed sharp. No D5 labeling is assumed.

## Exact proof

Suppose a unit x has B=sum_i(x.z_i)^2<=delta=1/27. Put q_i=(x.z_i)^2, d_i=a_i+q_i, w_i=z_i-(x.z_i)x in x^perp=R^4, b_i=||w_i||^2=1-d_i>=77/108, and u_i=w_i/sqrt(b_i).

For S^3, the polynomial f(t)=t^4-t^2/4 has Gegenbauer expansion

    f=(1/16) C_0^(1)+(1/8) C_2^(1)+(1/16) C_4^(1).

All coefficients are nonnegative. The addition theorem gives sum_{i,j} f(u_i.u_j)>=16^2/16=16. As 16 f(1)=12, this yields

    sum_{i<j} f(|u_i.u_j|)>=2.                          (1)

For i!=j, |w_i.w_j|<=1/2+p_ij, p_ij=sqrt(q_i q_j). Since b_i>=77/108 and p_ij<=delta/2, the upper normalized correlation v_ij=(1/2+p_ij)/sqrt(b_i b_j) is between 1/2 and 8/11. On this interval f is increasing and f' increasing. Since f<=0 below 1/2, one obtains

    f(|u_i.u_j|) <= g(d_i,d_j)+K p_ij,
    g(d,e)=[1-(1-d)(1-e)]/[16(1-d)^2(1-e)^2],
    K=f'(8/11)/(77/108)=168912/102487.                (2)

The function g is increasing and jointly convex on [0,1)^2. In variables u=1-d, v=1-e, its Hessian has diagonal entry (3-uv)/(8u^4v^2)>0 and determinant (uv-2)(3uv-10)/(256u^6v^6)>0. Hence G=sum_{i<j}g(d_i,d_j) is convex and increasing. We have

    0<=d_i<=c=31/108,
    sum d_i<=D=1205/1512.

The maximum over this capped simplex occurs at the vertex (c,c,r,0,...,0), with r=D-2c=337/1512. Thus

    G <= g(c,c)+2g(c,r)+26g(c,0)+13g(r,0)
      = 14734618533396/9706633446125 < 38/25.

AM-GM gives sum_{i<j}p_ij <= (15/2)B <= 15delta/2. Consequently (2) gives

    sum_{i<j}f(|u_i.u_j|)
    <= 14734618533396/9706633446125 + 46920/102487
     = 1743495708036/882421222375 < 2,

contradicting (1). Exact margin: 21346736714/882421222375>0. Hence B>1/27 for every unit x and F_O≻I/27.

## Type E corollary

In the retained Type-E 16K2 + F3 graph, the 16 outside-core selected edges satisfy the two-sided endpoint bounds, so |z_i.z_j|<=1/2 for outside i!=j. Their midpoint-energy sum is <=A<=383/504. The theorem applies.

Let F=F_O+F_C, T_O=sum_{i in O}m_i m_i^T, T_C=sum_{i in C}m_i m_i^T, A=tr(T_O+T_C). Then

    tr(T_O F)+tr(T_C F_O) >= A/27,

strict if A>0. The previously proved 184-safe endpoint inequality bounds this trace by 2 H_184, so

    H_184 >= A/54.                                    (3)

This is weaker numerically than the retained Q-rank floor H_184>=13808395/21337344, but is a new *structural*, D5-free coercivity estimate: outside-core projected vectors have no near-zero frame direction.

**[OPEN]** Optimize the spectral constant and combine it with endpoint Gram/KKT constraints. No Type E contradiction has been proved.

**[UNCHANGED]** 40<=tau_5<=44; M(F3)<=89; matching M(P)>=S/2-28/3; total selected-edge mass >=2137/6; A<=383/504; Type C,D, e>=27 and non-isolated branches open; e=23/24 classification conditional on delta(G)>=1.
