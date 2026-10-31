# Type E: affine endpoint majorant, core centroid, and exceptional-correlation budget

Date: 2026-10-31. **Proof ledger:** standalone geometric statements below are [PROVED EXACTLY]; Type-E numerical consequences are [CONDITIONAL] on retained bounds. Type E remains [OPEN]. The global proved range remains **40 <= tau_5 <= 44**.

## 1. Exact two-edge theorem

Let two distinct selected deep edges have endpoints m_i +/- z_i and m_j +/- z_j, with m_i perpendicular to z_i, ||m_i||^2<=1/4, and all cross-endpoint contacts <=1/2. Put c=m_i.m_j, d=|z_i.z_j|, and epsilon=(d-1/2)_+.

**[PROVED EXACTLY]**
    
    d^2 <= 1/4 + epsilon/2 - 3c/4.                          (1)

Proof: averaging two opposite cross-endpoint contacts gives c+d<=1/2; Cauchy gives |c|<=1/4. For c>=0, epsilon=0 and d^2<=(1/2-c)^2<=1/4-3c/4. For c<0 and d<=1/2 the bound is immediate. For c<0 and d>1/2, 0<epsilon<=-c<=1/4, so d^2=1/4+epsilon+epsilon^2<=1/4+5epsilon/4<=1/4+epsilon/2-3c/4.

The coefficients are Pareto-optimal among affine bounds d^2<=1/4+alpha*epsilon-beta*c: exact rational five-dimensional endpoint witnesses (m_i=m_j=e0/2, z_i=(e1+e2+e3)/2, z_j=(e1+e2-e3)/2) force beta<=3/4, while (m_i=e0/2, m_j=-e0/2, z_i=z_j=(e1+e2+e3)/2) force alpha+beta>=5/4. Both witnesses have unit endpoints, deep contact -1/2 and cross contacts <=1/2. The choice alpha=1/2,beta=3/4 saturates both. No simultaneous four-core sharpness is claimed.

## 2. Four-core centroid theorem

For the four selected F3 core edges define A_C=sum_j ||m_j||^2, s_C=||sum_j m_j||^2, delta=sum_(j<k)(|z_j.z_k|-1/2)_+, and Q_6=sum_(j<k)(z_j.z_k)^2.

**[PROVED EXACTLY]** Summing (1) and using 2sum_(j<k)m_j.m_k=s_C-A_C gives

    Q_6 <= 3/2 + delta/2 + 3(A_C-s_C)/8.                  (2)

This is a sign-sensitive second-order centroid penalty, independent of D5 alignment, isolated Q-rank, and lower endpoint-contact bounds.

## 3. Exact global-Q bridge

For twenty selected deep edges put a_i=||m_i||^2, A=sum a_i, U=sum a_i^2, and V_z=||sum_i (z_i z_i^T-(1-a_i)I/5)||_F^2. The frame trace identity is exact:

    Q = sum_(i<j)(z_i.z_j)^2
      = 30-3A+A^2/10-U/2+V_z/2.                           (3)

Splitting Q=Q_safe+Q_6, (2) gives

    Q_safe >= 57/2-3A+A^2/10-U/2+V_z/2
              -delta/2-3A_C/8+3s_C/8.                    (4)

This is the requested direct interface between global squared-correlation mass, the six exceptional defects, and second-order midpoint geometry. It does not yet force A>383/504.

## 4. Exact rational Type-E consequences

**[PROVED CONDITIONALLY]** Use the retained raw defect cap D=1780062775/4032758016, the retained midpoint cap A<=383/504, and s_C>=0. Then (2) gives

    Q_6 <= 3/2+D/2+3(383/504)/8
         = 16176768847/8065516032 = 2.005670657998...

This improves the prior exact core bound 1051426055/504094752=2.085770682651... by 646048033/8065516032=0.08010002465...

With the retained universal Type-E Q floor 17456771/635040,

    Q_safe >= 1027690941349/40327580160 = 25.483575688688...

**[FURTHER CONDITIONAL — retained historical center-variance theorem, not independently re-audited here]** If V_z>47602076041/317520000000, maximize U under 0<=a_i<=1/4 and sum a_i=A. On A in [k/4,(k+1)/4], U<=k/16+(A-k/4)^2; the resulting Q floor is decreasing in A<=383/504. At A=383/504, k=3, giving

    Q > 5876056025347/211680000000,
    Q_safe > 64910958829119229/2520473760000000
           = 25.753475342317...

For each safe pair |z_i.z_j|<=1/2. If K_r counts the 184 safe pairings with |z_i.z_j|>r, then

    K_r >= (Q_safe-184r^2)/(1/4-r^2), 0<=r<1/2.

The baseline floor forces K_(1/5)>=87 and K_(1/3)>=37, improving the previous 86 and 36. The additional retained center-variance floor forces K_0>=104, K_(1/8)>=98, K_(1/5)>=88, K_(1/4)>=77, K_(1/3)>=39. These are distributional necessities, not exclusions.

## 5. Verification and open work

The companion exact-Fraction verifier checks 1,681 admissible scalar contact pairs, two rational five-dimensional equality witnesses, the global frame identity, capped-simplex constants, exact rational comparisons, and integer ceilings. Finite checks supplement the analytic proof; the upstream Type-E defect and center-variance certificates are retained dependencies.

**[OPEN]** Next combine (4), retaining s_C, with the four rank-free Q residuals and the 184 safe Walsh blocks in one finite polynomial/KKT system. Type E, Types C/D, generic e>=27, and non-isolated branches remain open. Sparse e=23/24 classification requires delta(G)>=1. Preserve M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, and the Musin/Boyvalenkov zero-midpoint exclusion. **40<=tau_5<=44 remains proved.**
