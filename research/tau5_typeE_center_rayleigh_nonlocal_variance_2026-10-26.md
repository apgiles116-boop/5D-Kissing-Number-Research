# Type E: center-Rayleigh nonlocal frame bridge (2026-10-26)

**Proof ledger:** [PROVED EXACTLY] the center-Rayleigh inequalities and the transverse-frame identity below. [CONDITIONAL ON RETAINED TYPE-E ENDPOINT CERTIFICATES] the low-energy rational corollary. [OPEN] Type E, other graph branches, and the exact value of tau_5.

## Setup

Let x be a unit vector in R^5 and z_1,...,z_20 have ||z_i||^2=1-a_i>0. Set A=sum a_i, t_i=x.z_i, T=sum t_i^2, q=sum a_i t_i^2/(1-a_i)>=0. Define F_z=sum z_i z_i^T, V_z=||F_z-(20-A)I/5||_F^2. Normalize u_i=z_i/sqrt(1-a_i), append u_0=x, and set F_u=sum_{i=0}^{20}u_i u_i^T, V_u=||F_u-21I/5||_F^2. Write P=sum_{i<j}[s_ij(s_ij-1/4)]_+ with s_ij=(u_i.u_j)^2.

The dimension-five Gegenbauer identity f(t)=t^4-t^2/4=P_0/28+P_2/3+8P_4/21 (normalized P_k(1)=1), together with harmonic positivity, yields V_u<=24P/5 for any 21 unit vectors in R^5.

## Theorem 1 [PROVED EXACTLY]: center-Rayleigh two-well separation

The exact identities are

    x^T(F_z-(20-A)I/5)x = T-4+A/5,
    x^T(F_u-21I/5)x = T+q-16/5.

For every traceless symmetric 5x5 H, |x^T H x|<=sqrt(4/5)||H||_F, since ||xx^T-I/5||_F^2=4/5. Therefore

    (T-4+A/5)^2 <= 4V_z/5,
    (T+q-16/5)^2 <= 4V_u/5 <= 96P/25.

Their center-Rayleigh values differ by (4-A)/5+q. The triangle inequality proves

    sqrt(V_z)+sqrt(24P/5)
      >= (4-A+5q)/(2sqrt(5)) >= (4-A)/(2sqrt(5)).       (1)

This sharpens the earlier 2(1-A)/sqrt(5) bound by 3A/(2sqrt(5)) even if q=0. It exploits the *positive* center-Rayleigh contribution from normalization instead of subtracting the full correction norm.

The two squared inequalities are polynomial constraints upon introducing beta_i=t_i^2/(1-a_i), with (1-a_i)beta_i=t_i^2 and q=sum a_i beta_i. They require no D5 labeling or new SDP.

## Theorem 2 [PROVED EXACTLY]: transverse-frame identity

Set v_i=z_i-t_i x in x^perp, B=sum v_i v_i^T (4x4), and b=sum t_i v_i. In the decomposition R^5=x^perp plus Rx,

    F_z=[[B,b],[b^T,T]], tr B=20-A-T.

Orthogonal decomposition into transverse trace and traceless parts gives the exact identity

    V_z=(5/4)(T-(20-A)/5)^2
        +||B-(20-A-T)I_4/4||_F^2+2||b||^2.             (2)

The exact frame-trace identity is

    S_z:=sum_{i<j}(z_i.z_j)^2
       =30-3A+A^2/10-(1/2)sum_i a_i^2+V_z/2.         (3)

Equations (2)-(3) retain center-direction, transverse-anisotropy and mixed-block remainders. The squared-correlation floor by itself does not identify D5.

## Theorem 3 [CONDITIONAL ON RETAINED TYPE-E HYPOTHESES]

Assume 184 safe edge-edge pairings, 20 safe center-edge pairings and six possibly exceptional core pairings. Split A=A_O+A_C (16 outside and four core edges). The retained two-sided endpoint and negative-Gram estimates imply for A<=t

    P<=K_O(t)A_O+K_C(t)A_C<=K_C(t)A,
    K_O(t)=20/[16(1-t)^2],
    K_C(t)=[17+(1+t)^2(7+t)]/[16(1-t)^2].

These use |z_i.z_j|<=1/2 for safe pairs and sum_core delta<=A_C, sum_core delta^2<=A_C^2/4 for delta=(|z_i.z_j|-1/2)_+.

**Exact low-energy certificate:** If A<=t=1/40, then

    K_C(t)=1560361/973440,
    K_C(t)t=1560361/38937600,
    (1-t/2)^2-24K_C(t)t=8693/648960>0.

By (1), sqrt(V_z)>1/sqrt(5), hence V_z>1/5. By (3), sum a_i^2<=A^2 and monotonicity of 30-3A-2A^2/5,

    S_z>30-3/40-(2/5)(1/40)^2+1/10
       =120099/4000=30.02475.

This strengthens the earlier low-energy V_z>576/3125 and S_z>3001691/100000. It does NOT contradict the available safe-pair upper estimates and does NOT exclude Type E.

## Status and next task

[PROVED EXACTLY] Theorem 1 and the identity (2)-(3) are universal linear-algebra consequences, supplemented by Gegenbauer positivity.

[CONDITIONAL] The low-energy bound inherits the Type-E safe/core endpoint partition and four-core negative-Gram budgets.

[OPEN] A<=383/504 is still compatible. Retain T, q, the transverse anisotropy, b, and six individual core defects in the next finite polynomial/KKT certificate.

Global ledger unchanged: 40<=tau_5<=44. Retain M(F3)<=89, matching mass M(P)>=S/2-28/3, 20-edge mass>=2137/6, A<=383/504. Types C,D, generic e>=27 and non-isolated branches remain open; e=23/24 graph classification requires minimum degree>=1.
