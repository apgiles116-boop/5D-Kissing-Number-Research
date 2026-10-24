# Type E: capped Welch floor and six-exception safe-correlation mass

2026-10-24. **[PROVED EXACTLY]** five-dimensional frame and capped-simplex algebra. **[CONDITIONAL TYPE E]** consequences assuming the retained isolated-center 20-edge reduction and six-exception raw-defect bound. **[OPEN]** Type E elimination and the global upper bound.

## Inputs

For twenty selected deep edges, x_i^±=m_i±z_i, a_i=||m_i||² in [0,1/4], ||z_i||²=1-a_i, A=sum a_i<=B=383/504. Of 190 pairs, 184 are projectively safe, |z_i.z_j|<=1/2; only six four-core pairs are potentially exceptional. Let delta_ij=(|z_i.z_j|-1/2)_+ and D_raw=sum_exception delta_ij<=D0=1780062775/4032758016. The endpoint inequality implies delta_ij<=(-m_i.m_j)_+<=sqrt(a_i a_j)<=1/4. Projective safety is NOT the stronger graph-safe four-endpoint condition.

## Theorem 1: sharpened global squared-correlation floor [PROVED EXACTLY]

Set Q_i=z_i z_i^T-(1-a_i)I/5, T=sum Q_i. The exact frame identity is

sum_{i<j}(z_i.z_j)^2 = 30-3A+A²/10-(1/2)sum a_i²+(1/2)||T||_F². (1)

For A in [0,B], write k=floor(4A), r=A-k/4, and g(A)=k/16+r². Capped-simplex concentration gives sum a_i²<=g(A): move mass from a smaller nonzero entry to a larger unsaturated entry to increase the square sum. On each quarter-grid interval,

f(A)=30-3A+A²/10-g(A)/2, f'(A)=-3+A/5-r<=-57/20.

Thus f(A)>=f(B)+(57/20)(B-A). With B=3/4+5/504,

L=f(B)=8790283/317520=27.684186822877... . (2)

Hence

sum_{i<j}(z_i.z_j)^2 >= L+(57/20)(B-A)+(g(A)-sum a_i²)/2+||T||_F²/2. (3)

The old floor 17456771/635040 is improved by exactly 131/672. This is 92.28% of the D5 squared-correlation mass 30; no D5 proximity follows.

## Theorem 2: exact six-exception translation [CONDITIONAL TYPE E]

Since delta_ij<=1/4,

|z_i.z_j|² <= (1/2+delta_ij)² <= 1/4+(5/4)delta_ij.

Summing the six potential exceptions bounds their squared mass by 3/2+(5/4)D_raw. Subtracting from (3), the 184 projectively safe pairs S satisfy

sum_S (z_i.z_j)² >= K+(57/20)(B-A)+(g(A)-sum a_i²)/2+||T||_F²/2+(5/4)(D0-D_raw), (4)

K=L-3/2-(5/4)D0=2067388216673/80655160320=25.6324357731188... .

Thus the global frame floor has been translated into the retained six-exception raw-defect language, with four explicit nonnegative slacks. This is a NECESSARY lower bound, not an upper bound on safe data.

## Corollary: exact safe-pair contact density [CONDITIONAL TYPE E]

At least 76 of the 184 safe pairs have |z_i.z_j|>1/4. Otherwise their squared mass would be at most 75/4+109/16=409/16<K. Likewise at least 38 safe pairs have |z_i.z_j|>1/3; otherwise their squared mass would be at most 37/4+147/9=307/12<K. These are modest necessary density counts, not a D5 contact classification.

## K2,2 branch correction [CONDITIONAL TYPE E]

If the four core midpoint negative-product graph is K2,2 with parts {1,2}|{3,4}, put C=sum_core a_i, D_mid=sum_cross(-m_i.m_j), eps=C-D_mid. The previously proved exact identity yields p+q=m1.m2+m3.m4>=C/2-eps, with p,q>=0. Since p,q<=1/4 and |z1.z2|<=1/2-p, |z3.z4|<=1/2-q,

|z1.z2|²+|z3.z4|² <= 1/2-3C/8+3eps/4.

The four cross-core squared correlations contribute at most 1+(5/4)D_raw. Thus (4) gains Gamma=3C/8-3eps/4. In the sharp near-saturation branch eps/C<1-sqrt(3)/2, Gamma>3(sqrt(3)-1)C/8>0. No Type-E contradiction follows.

## Status and next target

**[PROVED EXACTLY]** (1)-(3), concentration, rational constants. **[CONDITIONAL TYPE E]** (4), 76/38 density counts, K2,2 correction. **[OPEN]** any opposing upper bound on safe squared mass below K, a global D5 labeling, a six-exception/Q-kernel identification, Type E, C, D, generic e>=27, and non-isolated branches. Sparse e=23/e=24 classification still requires delta(G)>=1.

Global retained range: 40<=tau_5<=44. Type E retained broom M(F3)<=89, matching M(P)>=S_F3/2-28/3, and A<=383/504.

Companion exact checker: tau5_typeE_capped_frame_safe_mass_2026-10-24_verify.py.
