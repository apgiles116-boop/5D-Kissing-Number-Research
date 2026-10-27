# Type E: complete center-adapted O(4) fourth-harmonic decomposition

Date: 2026-10-27. **[PROVED EXACTLY — universal algebra]** for all identities. **[PROVED EXACTLY — conditional on retained Type-E certificates]** for the defect-budget corollary. **[OPEN]** Type E remains unresolved.

## Notation

Fix a unit vector x in R^5, P=I-xx^T, and write z_i=c_i*x+w_i, c_i=x.z_i, w_i=P*z_i, q_i=||w_i||^2, r_i=c_i^2+q_i. Thus w_i belongs to the 4-space x-perp. Define

    R2=sum_i r_i^2, S4=sum_i r_i^4,
    F=sum_i r_i*z_i*z_i^T, E=F-(R2/5)I, W=||E||_F^2,
    D_raw=sum_{i<j} (z_i.z_j)^2*((z_i.z_j)^2-r_i*r_j/4).

STF_k means the orthogonal symmetric trace-free projection in dimension FOUR. Define five harmonic moments:

    h=sum_i (8*c_i^4-12*c_i^2*q_i+q_i^2)/21,
    L=sum_i c_i*(2*c_i^2-q_i)*w_i,
    B=sum_i (8*c_i^2-q_i)*STF_2(w_i^tensor2),
    T3=sum_i c_i*STF_3(w_i^tensor3),
    T4=sum_i STF_4(w_i^tensor4).

## [PROVED EXACTLY] Five-sector harmonic identity

For s=w_i.w_j, the trace-free Gram kernels are

    STF2: s^2-q_i*q_j/4
    STF3: s^3-q_i*q_j*s/2
    STF4: s^4-(3/4)*q_i*q_j*s^2+q_i^2*q_j^2/16.

The degree-four harmonic kernel in R^5 is

    H4(z,v)=(z.v)^4-(2/3)||z||^2||v||^2(z.v)^2+(1/21)||z||^4||v||^4.

Its O(4) branching under the stabilizer of x has dimensions 1+4+9+16+25=55. Direct polynomial expansion proves the exact pairwise identity

    H4(z_i,z_j)
       =(21/8)*h_i*h_j+(2/3)*L_i.L_j+(1/12)*B_i:B_j
        +4*T3_i:T3_j+T4_i:T4_j,

where the subscripted quantities are the individual summands. Summing both indices gives

    K:=sum_{i,j}H4(z_i,z_j)
      =(21/8)*h^2+(2/3)||L||^2+(1/12)||B||_F^2
       +4||T3||_F^2+||T4||_F^2.                         (1)

Every term is nonnegative and there is NO hidden residual. In particular the previous evaluation-plus-tangent remainder equals (1/12)||B||^2+4||T3||^2+||T4||^2.

Combining (1) with the established raw harmonic identity gives the exact polynomial decomposition

    D_raw=R2^2/56-(3/8)S4+(5/24)W
          +(21/16)h^2+(1/3)||L||^2+(1/24)||B||^2
          +2||T3||^2+(1/2)||T4||^2.                    (2)

No D5 contact labeling or generic SDP is assumed.

## [PROVED EXACTLY] Fully completed center/frame SOS

Set d=x^T E x, b=P E x, C=P E P, p=sum_i c_i^3*w_i. Then L=3p-b, tr(C)=-d, and

    W=(5/4)d^2+2||b||^2+||C+(d/4)P||_F^2.

The vector-square identity

    (5/12)||b||^2+3||p-b/3||^2
      =(5/3)||p||^2+(3/4)||b-(4/3)p||^2

therefore yields the **exact complete sum-of-squares identity**

    D_raw=R2^2/56-(3/8)S4
          +(25/96)d^2+(21/16)h^2+(5/3)||p||^2
          +(3/4)||b-(4/3)p||^2
          +(5/24)||C+(d/4)P||_F^2
          +(1/24)||B||^2+2||T3||^2+(1/2)||T4||^2.   (3)

## [PROVED EXACTLY — conditional Type E] Defect budget

The retained exact six-exception positive raw-defect certificate gives

    D_raw <= P_raw <= 1780062775/4032758016.

Thus (2) gives the necessary, denominator-free semialgebraic constraint

    (5/24)W+(21/16)h^2+(1/3)||L||^2+(1/24)||B||^2
      +2||T3||^2+(1/2)||T4||^2
      <= 1780062775/4032758016 - R2^2/56 + (3/8)S4.  (4)

Here r_i=1-a_i, 0<=a_i<=1/4, sum a_i=A<=383/504. The six individual exceptional correlations have NOT yet been inserted in (4). Their incorporation, together with endpoint-mixing constraints, is the next finite polynomial/KKT task.

## [PROVED EXACTLY] D5 sanity check

For all twenty D5 lines z_ij^+/-=(e_i+/-e_j)/sqrt(2), with x=e_1, exact evaluation gives

    R2=S4=20, W=0, h=2/7,
    ||L||^2=||B||^2=||T3||^2=0, ||T4||^2=1/2.

Hence K=(21/8)*(2/7)^2+1/2=5/7 and D_raw=-5/14+K/2=0. At this alignment the fourth tangent sector supplies 1/2 of K, so discarding it can destroy sharp D5 stability information.

## Verification and ledger

Companion SymPy verifier checks the exact polynomial kernel identity, the second tangent Hessian feature norm 64/3, the D5 specialization and the raw identity on twenty rational vectors. Positivity is exact from STF tensor norms.

**[OPEN]** No positive uniform lower bound on ||T3|| or ||T4|| has been proved under the actual Type-E constraints; (4) is necessary, not a contradiction. The five D5 Q-cycle relations still require a justified D5 labeling.

**[RETAINED]** 40<=tau_5<=44; 1/49<A<=383/504; M(F3)<=89; matching M(P)>=S/2-28/3; twenty-edge mass>=2137/6; raw correlation floor>=8790283/317520; Musin/Boyvalenkov zero-midpoint exclusion. Types C,D,E, generic e>=27 and non-isolated branches remain open. Sparse e=23,24 classification remains conditional on delta(G)>=1.
