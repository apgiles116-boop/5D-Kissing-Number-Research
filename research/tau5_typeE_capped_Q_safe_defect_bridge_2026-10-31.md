# Type E: capped Q energy and six-defect-to-safe bridge (2026-10-31)

**Status: PROVED EXACTLY**, under the retained twenty-disjoint-deep-edge Type-E hypotheses and previously certified midpoint/defect caps. **Type E remains OPEN; 40 <= tau_5 <= 44 remains the global proved range.**

Write a_i=||m_i||^2, A=sum a_i<=383/504, U=sum a_i^2, ||z_i||^2=1-a_i, and q_ij=z_i.z_j. Deepness gives 0<=a_i<=1/4. There are sixteen isolated selected pairs I and four core pairs C. For any distinct selected pairs, the four cross-endpoint inequalities imply m_i.m_j+|q_ij|<=1/2. The retained raw positive defect cap on the six core pairs is

D_C=sum_{i<j in C} (|q_ij|-1/2)_+ <= D_*=1780062775/4032758016.

## Theorem 1: sharper exact global squared-correlation floor

Put Z=sum_i z_i z_i^T and V=||Z-(20-A)I_5/5||_F^2>=0. Traceless-projector positivity gives the **exact identity**

sum_{i<j} q_ij^2 = 30-3A+A^2/10-U/2+V/2.                       (1)

For fixed A, U is maximized by filling as many a_i=1/4 as possible and placing the remainder in one entry (convexity). The resulting U_max(A) is continuous, nondecreasing and piecewise quadratic. Therefore F(A)=30-3A+A^2/10-U_max(A)/2 is strictly decreasing on 0<=A<=383/504, since F'(A)=-3+A/5-U_max'(A)/2<0 wherever differentiable.

At A_*=383/504, U_max=3/16+(A_*-3/4)^2=47653/254016. Consequently

**sum_{i<j} q_ij^2 >= 8790283/317520 = 27.684186822877...**     (2)

This is 92.2806227429...% of the exact D5 total 30, improving the earlier 17456771/635040 floor by **exactly 131/672**. No D5 labeling is assumed.

## Theorem 2: capped concentration of the six exceptional defects

For core i<j, let d_ij=(|q_ij|-1/2)_+, D_C=sum d_ij and E_C=sum(q_ij^2-1/4)_+. The identity

E_C=D_C+sum d_ij^2                                               (3)

is exact. From the cross-endpoint inequality, d_ij<=(-m_i.m_j)_+<=sqrt(a_i a_j)<=1/4. Convexity therefore gives sum d_ij^2<=Phi(D_C), where

Phi(d)=d^2 for 0<=d<=1/4,
Phi(d)=1/16+(d-1/4)^2 for 1/4<=d<=1/2.

Since 1/4<D_*<1/2,

sum_{i<j in C} q_ij^2 <= 3/2+D_*+Phi(D_*)
= **2.0405351212855467...**.                                     (4)

The capped square contribution Phi(D_*) is 0.0991342814787..., versus the uncapped D_*^2 about 0.1948. No claim is made that all six defects can simultaneously attain the scalar extremizer in genuine geometry.

## Theorem 3: safe squared-correlation lower bound

Let S_safe=sum q_ij^2 over the 184 pairs not both in C. Equations (2),(4) imply

**S_safe >= 2085231131661776940907/81315686078061281280
=25.643651701591754...**.                                       (5)

The mass-sensitive version uses the centroid estimate

D_C<=sum_{i<j in C}(-m_i.m_j)_+
<=A_C-||sum_{i in C}m_i||^2/4<=A_C,

where A_C=sum_{i in C}a_i. Thus with d=min(D_*,A_C),

S_safe >= 8790283/317520 - 3/2-d-Phi(d).                         (6)

For instance A_C<=1/3 implies S_safe>=8186113/317520=25.781409045....

## Theorem 4: exact second-order frame-variance bridge

Let U_I=sum_{i in I}a_i^2, U_C=sum_{i in C}a_i^2,
M_C=sum_{i in C}m_i m_i^T and V_m=A_C^2-||M_C||_F^2>=0.
Since d_ij^2<=(m_i.m_j)^2,

sum_{i<j in C}d_ij^2 <= (A_C^2-V_m-U_C)/2.                         (7)

Writing B_C=sum_{i<j in C}(1/4-q_ij^2)_+>=0, (1),(3),(7) yield

**S_safe >= 57/2-3A+A^2/10-(U_I+A_C^2)/2+(V+V_m)/2-D_C.**          (8)

This is a sign-free, second-order connection of global Q-frame variance and core midpoint rank-dispersion to the six-exception language. Both variances have positive coefficients. The defect-free corollary substitutes D_C<=A_C-||sum_C m_i||^2/4.

**OPEN:** Neither (5) nor (8) gives a contradiction with A<=383/504. The next step requires an upper bound on safe squared-correlation mass or a strictly positive residual tied to the actual F3 signed endpoint/Walsh constraints. No one-to-one identification between six core pairings and the six D5 Q-kernel relations is asserted.

**Retained without regression:** star <=70/3; broom M(F3)<=89; matching M(P)>=S/2-28/3; 20-edge mass >=2137/6; Musin/Boyvalenkov antipodal 40-point boundary theorem; homogeneous defect cap; Type C partial results. Types C, D, E, generic e>=27 and non-isolated branches remain open. Sparse e=23/e=24 classification is conditional on delta(G)>=1. Global range remains 40<=tau_5<=44.

An exact rational verifier and expanded note are included in the corresponding local research package.