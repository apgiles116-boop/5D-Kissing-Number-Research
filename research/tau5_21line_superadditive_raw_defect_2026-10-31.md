# Sharp 21-line quartic-to-raw defect bridge (2026-10-31)

**Status: PROVED EXACTLY (algebra), conditional on the previously proved universal quartic gap P>1/58. Type E remains OPEN. Global proved range: 40<=tau_5<=44.**

## Ledger correction

The 2026-10-29 theorem `tau5_21line_quartic_gap_1over58_2026-10-29.md` establishes P>1/58 for 21 unit vectors in R^5. This is strictly stronger than the later 2026-10-31 P>3/196 certificate: 1/58-3/196=11/5684>0. Do not regress to the weaker constant.

## Exact scalar theorem

For any finite family of absolute correlations s_ij in [0,1], define d_ij=(s_ij-1/2)_+, D=sum d_ij and P=sum [s_ij^2(s_ij^2-1/4)]_+. Then

    P <= g(D),   g(t)=t(1+t)(t+1/2)^2
                       =t/4+(5/4)t^2+2t^3+t^4.

Indeed for s=1/2+d the quartic summand equals g(d), while it is zero below threshold. Since g has only positive nonconstant coefficients, g(x+y)>=g(x)+g(y) for all x,y>=0. Induction proves the claim. This is sharp as a scalar allocation inequality when one d_ij carries all the defect; no geometric sharpness is claimed.

## Universal 21-line consequence

**[PROVED EXACTLY, using the retained P>1/58 theorem]** Every 21 unit vectors u_0,...,u_20 in R^5 satisfy

    D=sum_{i<j} (|u_i.u_j|-1/2)_+ > rho > 1/19,

    rho=sqrt((1+sqrt(61/29))/8)-1/2
       =0.0534355150799747759...

The unique positive root of g(rho)=1/58 is rho. Since g is strictly increasing, P>1/58 and P<=g(D) imply D>rho. The rational comparison is exact:

    g(1/19)=2205/130321,
    1/58-g(1/19)=2431/7558618>0.

This supersedes the weaker raw gap D>1/98 in the 2026-10-31 trace-aware note. The old linear conversion P<=(3/2)D lost a factor >5 in the raw defect conclusion.

## Type-E Walsh corollary

**[PROVED CONDITIONALLY on the retained 204-safe-block center/Walsh normalization lemma]** Let A=sum_{i=1}^{20}a_i<=383/504, a_0=0, D_C the six-core raw positive defect, and

    T(a)=(1/2)sum_{0<=i<j<=20}((1-a_i)^(-1/2)(1-a_j)^(-1/2)-1).

For safe selected-edge pairs set c_ij=m_i.m_j; for center pairs set c_0i=x_0.m_i. Define

    K_safe=sum_safe min((1-sqrt((1-a_i)(1-a_j)))/2,|c_ij|)
                    /sqrt((1-a_i)(1-a_j)) >=0.

The retained Walsh lemma states D_norm<=(4/3)D_C+T(a)-K_safe. Hence the new universal D_norm>rho gives

    D_C+(3/4)T(a) > (3/4)rho+(3/4)K_safe.

Using the retained sharp mass-simplex estimate (3/4)T(a)<=C_* A with C_*=18sqrt(3)-53/2 yields

    D_C+C_* A > (3/4)rho+(3/4)K_safe
              > 3/76+(3/4)K_safe.

Here (3/4)rho=0.04007663630998108..., versus the old 3/392=0.00765306... . The retained second-order estimate K_safe>=[A_I^2/5-U_I]_+ remains valid.

**[OPEN]** This necessary inequality still does not contradict A<=383/504 or D_C<=1780062775/4032758016. It does not eliminate Type E or any other unresolved graph branch. Retain M(F3)<=89, M(P)>=S/2-28/3, Musin/Boyvalenkov boundary exclusion, and the sparse e=23/24 classification's delta(G)>=1 qualification. No identification of six core pairings with D5 Q-kernel relations is claimed.

Companion exact verifier: `research/tau5_21line_superadditive_raw_defect_2026-10-31_verify.py`. It also checks the eight exact Huber endpoint/trace comparisons from the prior P>1/58 certificate, but does not independently re-prove the analytic convexity/majorization argument of that prior theorem.
