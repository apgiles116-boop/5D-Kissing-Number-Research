# Four-core negative-Gram defect: exact slack and rank-one stability (2026-10-23)

**[PROVED EXACTLY — dimension-free vector lemma]** For any four Euclidean vectors m_i, write a_i=||m_i||², b_i=sqrt(a_i), C=sum a_i, M=sum m_i, d=sum_{i<j}(-m_i.m_j)_+, t_ij=(m_i.m_j)/(b_i b_j) when b_i b_j>0 (zero otherwise), and bbar=(sum b_i)/4.

Then the following **exact nonnegative decomposition** holds:

    C-d = sum_i(b_i-bbar)^2 + ||M||²/4
          + (1/2)sum_{i<j}b_i b_j(1-|t_ij|).       (1)

Proof: sum the pair identity
(-m_i.m_j)_+ = (b_i b_j-m_i.m_j)/2 - b_i b_j(1-|t_ij|)/2
and use sum_{i<j}m_i.m_j=(||M||²-C)/2.

Let epsilon=C-d, T=sum m_i m_i^T. The identity forces

    sum_i(b_i-bbar)^2<=epsilon, ||M||²<=4epsilon,
    sum_{i<j}b_i b_j(1-|t_ij|)<=2epsilon.

Since b_i b_j<=C/2 and 1-t²<=2(1-|t|),

    C²-tr(T²)=2sum_{i<j}a_i a_j(1-t_ij²)<=4C epsilon.

For C>0, tr(T²)<=lambda_max(T)C, so

    lambda_max(T)>=C-4epsilon.                     (2)

Consequently **there exists a unit v** with

    sum_i ||m_i-(m_i.v)v||²<=4epsilon.             (3)

**Equality classification:** For C>0, d=C if and only if, up to rotation and permutation, the vectors are (w,w,-w,-w) with ||w||²=C/4. Indeed all three slacks in (1) vanish, forcing equal positive lengths, collinearity, and zero vector sum. Conversely the indicated configuration saturates.

**Squared-defect analogue [PROVED EXACTLY].** Set d2=sum_{i<j}(-m_i.m_j)_+², W=sum_i b_i m_i, and

    psi(t)=(1-t)/2-max(-t,0)^2
          =(1-t)/2 for t>=0,
           (1+t)(1-2t)/2 for t<0.

Then

    C²/4-d2 = ||W||²/4 + sum_{i<j}a_i a_j psi(t_ij), (4)

with psi(t)>=(1-t²)/4>=0. If epsilon2=C²/4-d2 and C>0, this gives

    C²-tr(T²)<=8epsilon2,
    min_{||v||=1}sum_i||m_i-(m_i.v)v||²<=8epsilon2/C. (5)

The identity follows by subtracting d2 from
sum_{i<j}a_i a_j(1-t_ij)/2=(C²-||W||²)/4.

**[CONDITIONAL ON RETAINED TYPE-E REDUCTIONS]** Apply (1)-(5) to the four midpoint vectors of the one mass-selected F3 matching. This sharpens the *stability information*, not the scalar bound d<=C or d2<=C²/4. In any branch where the raw six-core defect nearly saturates C, (3) quantitatively forces the core midpoints near one line. No D5 labeling, six-exception/Q-kernel identification, or Type-E exclusion follows.

**[OPEN]** Type E, C, D, generic e>=27 and non-isolated 41-code cases. Global proved range remains 40<=tau_5<=44. Preserve M(F3)<=89, matching M(P)>=S/2-28/3, and A<=383/504 (along with stronger retained ceilings).

Next target: retain the equal-length variance and angular slack in the six-core finite polynomial/KKT system, and quantify how m_i.z_i=0 constrains the four z_i if midpoint norms stay bounded below.
