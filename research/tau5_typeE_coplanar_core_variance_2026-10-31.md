# Type E: exact four-core coplanar frame-variance identity

2026-10-31. **Global proved range: 40 <= tau_5 <= 44. Type E remains OPEN.**

## New theorem [PROVED EXACTLY]

For four distinguished deep-edge pairs write the unit endpoints as m_i +/- z_i, with a_i=||m_i||^2, ||z_i||^2=1-a_i, and c_ij=m_i.m_j. Assume all four z_i lie in one two-plane P and the cross-endpoint inequalities give c_ij+|z_i.z_j|<=1/2. Define A=sum a_i, Z=sum z_i z_i^T, M=sum m_i m_i^T, and four nonnegative residuals:

- V_z=||Z-(4-A)P/2||_F^2 (planar frame variance);
- V_m=A^2-||M||_F^2 (midpoint rank dispersion);
- s=||sum m_i||^2 (midpoint centroid energy);
- R=sum_{i<j}[(1/2-c_ij)^2-(z_i.z_j)^2] (endpoint slacks).

Then the **exact identity** is

    A^2+6A-2 = 2(V_z+V_m+s)+4R.

In particular **A>sqrt(11)-3=0.316624790355...**. This requires no D5 labeling, Q-rank assumption, raw-defect cap, or generic SDP.

## Algebraic proof

Let U=sum a_i^2 and Q=sum_{i<j}(z_i.z_j)^2. Planar frame algebra gives

    Q=2-A+A^2/4-U/2+V_z/2.

Midpoint Gram algebra gives

    sum_{i<j}c_ij=(s-A)/2,
    sum_{i<j}c_ij^2=(A^2-V_m-U)/2.

Expanding the endpoint residual,

    R=3/2+(A-s)/2+(A^2-V_m-U)/2-Q.

Substitution proves the identity. All residuals are nonnegative: Z is a positive semidefinite operator on P, M is positive semidefinite, and each endpoint inequality gives 0<=|z_i.z_j|<=1/2-c_ij.

To prove **strictness**, equality at A=sqrt(11)-3 would force V_z=V_m=s=R=0. Thus m_i=b_i v with sum b_i=0, b_i^2=a_i; all six correlations obey |z_i.z_j|=1/2-b_i b_j; and Z=(4-A)P/2. For fixed i, the six endpoint equalities yield

    sum_{j!=i}(z_i.z_j)^2=3/4+a_i(1+A)-a_i^2.

The planar tight-frame identity gives the same sum as

    (1-a_i)(1-A/2+a_i).

Hence a_i(1+A/2)=1/4-A/2 for every i, so all a_i=A/4. The four equal-length planar z_i form a tight frame. Writing their directions as angles theta_i, tightness gives sum exp(2i theta_i)=0. Four unit complex numbers summing to zero split into two antipodal pairs; therefore some z_i.z_j=0. But R=0 then requires b_i b_j=1/2, contradicting |b_i b_j|=A/4<1/4. Strictness follows.

## Conditional Type-E consequence [PROVED CONDITIONALLY]

Under the retained Type-E cap A_I+A_C<=383/504, if all four F3 core projected vectors are coplanar then

    A_I < 1895/504-sqrt(11) = 0.443295844565...

Thus the large-isolated-energy branch A_I>=1895/504-sqrt(11) is excluded for four coplanar cores, including the rank-13/rank-two-null case with all four core completions genuinely ambiguous. This does not assume D5 proximity and complements the separately retained small-A_I near-D5 exclusion. The intervening region remains OPEN.

## Exact local witness [PROVED EXACTLY; NOT A TYPE-E 41-CODE]

Let a=1/6, t=5/6, and choose orthogonal coordinate subspaces with

    m_1=m_3=+sqrt(a)e_3, m_2=m_4=-sqrt(a)e_3;
    z_1=sqrt(t)(1,0), z_2=sqrt(t)(3/5,4/5),
    z_3=sqrt(t)(0,1), z_4=sqrt(t)(-3/5,4/5).

All eight endpoints m_i +/- z_i have unit norm; the four selected deep pairs have within-pair inner product -2/3. The six cross-pair endpoint maxima, ordered (12,13,14,23,24,34), are (1/3,1/6,1/3,1/2,2/5,1/2), all <=1/2. The raw positive defect is delta=1/3<1780062775/4032758016 and A_C=2/3<383/504. The exact residuals are V_z=49/450, V_m=s=0, R=167/300, so 22/9=2(49/450)+4(167/300).

Therefore **coplanarity plus the two scalar caps alone does not exclude the four-core relaxation**. The sixteen isolated edges, F3 graph contacts, or joint Q/Walsh constraints are indispensable. The witness does not assert a realization of the full Type-E graph.

## Next target [OPEN]

Couple this four-term nonnegative identity with the sixteen isolated-core endpoint constraints and the rank-13 missing-plane incidence equations. Quantitatively lower-bound V_z, V_m, s, or R from safe Walsh/Q measurements to force A_C>383/504 or eliminate the intermediate isolated-energy region.

Preserve the exact Type-E broom M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, raw/homogeneous defect caps, and Musin/Boyvalenkov zero-midpoint boundary. Sparse e=23/24 classification remains conditional on delta(G)>=1. **40<=tau_5<=44 remains unchanged.**
