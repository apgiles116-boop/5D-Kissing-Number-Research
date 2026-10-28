> **STRENGTHENING (2026-10-27; conditional on retained F3 mass certificates):** The earlier scalar ceiling A<=383/504 can be sharpened to A<=0.65103701309... by the 2026-10-14 mass-concavity argument. Joint control of U=sum a_i^2 then raises the global raw squared-correlation floor from 27.6841868... to **28.01979372338...**, and gives new 184-safe-pair floors. See [joint mass/Q safe-pair bridge](tau5_typeE_mass_concavity_joint_Q_safe_bridge_2026-10-27.md). The exact harmonic identities below remain valid; the old floor is retained only as a weaker bound requiring fewer inherited mass inputs. No Type-E exclusion is claimed.

# Type E: capped-energy correlation floor and raw fourth-harmonic identity

Date: 2026-10-27. Status: **[PROVED EXACTLY — conditional on retained Type-E hypotheses]** for the new raw squared-correlation floor; **[PROVED EXACTLY — universal algebra]** for the harmonic identities. **[OPEN]** Type E is not eliminated; the global range remains 40 <= tau_5 <= 44.

## 1. Improved raw squared-correlation floor

For twenty deep-edge pairs m_i +/- z_i put a_i=||m_i||^2, r_i=||z_i||^2=1-a_i, A=sum a_i. Retain 0<=a_i<=1/4 and A<=383/504. Let F_z=sum z_i z_i^T and V_z=||F_z-((20-A)/5)I||_F^2. The exact identity is

    sum_{i<j}(z_i.z_j)^2
      =30-3A+A^2/10-(1/2)sum a_i^2+V_z/2.

For fixed A, the sharp cap on sum a_i^2 is Phi(A)=q/16+(A-q/4)^2 with q=floor(4A), by convexity on the capped simplex. The function f(A)=30-3A+A^2/10-Phi(A)/2 decreases on [0,383/504], since f'(A)=-3+A/5-(A-q/4)<0 on each interval.

At A=383/504=3/4+5/504, Phi(A)=3/16+(5/504)^2=47653/254016. Therefore

    sum_{i<j}(z_i.z_j)^2 >= 8790283/317520
                           = 27.684186822877...

This improves the prior 17456771/635040 by exactly 131/672. The mass is at least 92.28% of the D5 value 30, but this alone does NOT establish D5 proximity.

There is an exact stability decomposition:

    sum_{i<j}(z_i.z_j)^2-f(A)
       = [V_z+Phi(A)-sum a_i^2]/2.

## 2. Denominator-free weighted fourth harmonic

The following holds for arbitrary z_i in R^5, without a D5 labeling. Put r_i=||z_i||^2, R2=sum r_i^2, S4=sum r_i^4, w_ij=(z_i.z_j)^2,

    D_raw=sum_{i<j} w_ij*(w_ij-r_i*r_j/4),
    F_r=sum_i r_i*z_i*z_i^T,
    W=||F_r-(R2/5)I||_F^2.

The degree-four harmonic kernel in dimension five is

    h4(v,w)=(v.w)^4-(2/3)||v||^2||w||^2(v.w)^2
              +(1/21)||v||^4||w||^4.

Set K=sum_{i,j}h4(z_i,z_j). By the harmonic addition theorem, K>=0. Expanding and using tr(F_r^2)=S4+2 sum_{i<j}r_i*r_j*w_ij proves the exact identity

    D_raw=R2^2/56-(3/8)S4+(5/24)W+K/2.

For any unit center x let h=sum_i h4(x,z_i). Harmonic Cauchy-Schwarz and h4(x,x)=8/21 give K>=(21/8)h^2. Hence

    D_raw>=R2^2/56-(3/8)S4+(5/24)W+(21/16)h^2.

For the isolated center x0, endpoint safety gives |x0.z_i|<=1/2. Put t0=sum_i(x0.z_i)^2 and tr=sum_i r_i*(x0.z_i)^2. Since sum_i(x0.z_i)^4<=t0/4 and W>=(5/4)(tr-R2/5)^2, a further exact, denominator-free bound is

    D_raw >= R2^2/56-(3/8)S4
             +(25/96)*(tr-R2/5)^2
             +(21/16)*[(2/3)*tr-t0/4-R2/21]_+^2.

These are polynomial constraints directly on the raw projected vectors, center moments and six potentially exceptional core pairings. They avoid normalization denominators and make no unproved identification between six exceptional pairs and six D5 Q-kernel relations.

## 3. Limitations and next step

The harmonic lower bound needs a compatible *upper* bound on the signed raw defect, preserving all 184 safe pair constraints, the six exceptional core pairs and Gram/PSD realizability. No such contradiction has been established. At zero-midpoint D5, K=5/7 cancels the baseline -5/14 exactly, so dropping K loses essential information.

Retain: 1/49<A<=383/504, M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, and the Musin/Boyvalenkov 21-line zero-midpoint exclusion. Types C,D, generic e>=27 and non-isolated branches remain open. Sparse e=23,24 classification still requires delta(G)>=1.

The companion verifier checks the raw identity on a rational twenty-vector instance, its center consequence, the exact rational constants, and monotonicity. Universal PSD follows from the harmonic addition theorem, not from numerical sampling.
