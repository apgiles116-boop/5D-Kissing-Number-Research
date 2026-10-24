# Type E: four-core K2,2 sign stability under near-saturated raw defect

2026-10-24. **[PROVED EXACTLY — four-vector theorem]**; **[CONDITIONAL TYPE-E APPLICATION]**. No Type-E elimination or D5 labeling is claimed.

## Theorem

For four Euclidean vectors m_1,...,m_4, set C=sum ||m_i||^2>0, d=sum_{i<j}(-m_i.m_j)_+, and epsilon=C-d.

**(i)** If 0<=epsilon<=C/64, there is a unit v for which t_i=m_i.v has exactly two positive and two negative values, and every pair satisfies

    sign(m_i.m_j)=sign(t_i*t_j),
    |m_i.m_j| > (1057/20000) C.

Thus the negative midpoint Gram graph is exactly K2,2: only four of the six pairings have negative midpoint dot product.

**(ii)** If also m_i.z_i=0 and ||z_i||<=1, then epsilon<=C/100 implies that the same principal-axis v can be chosen with

    sum_i (v.z_i)^2 < 1600/4961 < 1/3.

## Self-contained proof

Write b_i=||m_i||, bbar=(sum b_i)/4, M=sum m_i, T=sum m_i m_i^T. The retained exact negative-Gram slack identity is

    epsilon=sum_i(b_i-bbar)^2+||M||^2/4
      +(1/2)sum_{i<j}b_i*b_j*(1-|cos(m_i,m_j)|).

The weighted angular terms involving zero vectors are zero. Thus the length variance is <=epsilon, ||M||<=2sqrt(epsilon), and tr(T^2)>=C^2-4C epsilon. Choose a unit top eigenvector v of T, set t_i=m_i.v and r_i=m_i-t_i v. Since lambda_max(T)>=tr(T^2)/C,

    sum_i ||r_i||^2=C-lambda_max(T)<=4epsilon.

The four deviations b_i-bbar sum to zero, hence |b_i-bbar|<=sqrt(3epsilon/4). Also sqrt(C-epsilon)/2<=bbar<=sqrt(C)/2. Therefore

    (sqrt(C-epsilon)-sqrt(3epsilon))/2 <= b_i
      <= (sqrt(C)+sqrt(3epsilon))/2.

If epsilon/C<=1/64, use the exact square comparisons sqrt(63)>79/10 and sqrt(3)<87/50 to obtain

    b_i>(77/200)sqrt(C),  b_i<(61/100)sqrt(C).

Since ||r_i||^2<=4epsilon<=C/16, it follows that

    |t_i|^2>[(77/200)^2-1/16]C>(29/100)^2 C.

Also |sum_i t_i|<=||M||<=sqrt(C)/4. A 3-versus-1 sign split would imply |sum_i t_i|>[3(29/100)-61/100]sqrt(C)=(26/100)sqrt(C)>sqrt(C)/4, and a 4-versus-0 split is still worse. Thus the split is exactly 2+2.

For every pair, |r_i.r_j|<=(||r_i||^2+||r_j||^2)/2<=2epsilon<=C/32. Consequently m_i.m_j=t_i*t_j+r_i.r_j has the sign of t_i*t_j and

    |m_i.m_j|>[(29/100)^2-1/32]C=(1057/20000)C.

If epsilon/C<=1/100, the exact comparisons sqrt(99)/10>99/100 and sqrt(3)/10<9/50 instead give b_i>(81/200)sqrt(C), whence

    |t_i|^2>[(81/200)^2-1/25]C=(4961/40000)C.

Orthogonality 0=m_i.z_i=t_i(v.z_i)+r_i.z_i and ||z_i||<=1 yield

    sum_i(v.z_i)^2<=sum_i||r_i||^2/min_i t_i^2
      <(C/25)/[(4961/40000)C]=1600/4961<1/3.

All inequalities are exact and dimension-independent.

## Conditional Type-E consequence

For a selected F3 matching, endpoint kissing inequalities imply

    m_i.m_j+|z_i.z_j|<=1/2,
    delta_ij=(|z_i.z_j|-1/2)_+<=(-m_i.m_j)_+.

**[CONDITIONAL ON epsilon/C<=1/64 FOR THIS CORE]** At least two of the six distinguished pairings have delta_ij=0. All positive raw projective defects are confined to a K2,2; for the two within-part pairings,

    |z_i.z_j|<1/2-(1057/20000)C.

If the separately retained matching-uniform C>1/117 applies to this same core, then the gap is >1057/2340000.

This does **not** establish that the two within-part pairings are graph-safe in the stronger sense of all four cross-endpoint products. Nor does the retained Type-E energy ceiling imply epsilon/C<=1/64.

## Proof ledger

- **[PROVED EXACTLY]** Four-core K2,2 sign theorem and common-normal bound.
- **[PROVED CONDITIONALLY]** At most four positive raw projective core defects in the near-saturation branch.
- **[OPEN]** Prove near saturation for actual Type E, or handle epsilon>C/64 using the positive slack; couple K2,2 geometry to the six-exception Q-Gram/KKT system.
- **[UNCHANGED]** 40<=tau_5<=44; M(F3)<=89; matching mass >=S_F3/2-28/3; selected A<=383/504; Types C/D/E, generic e>=27 and non-isolated branches open. Sparse e=23/24 classification remains conditional on delta(G)>=1.

Companion checker: tau5_typeE_core_K22_sign_stability_2026-10-24_verify.py.
