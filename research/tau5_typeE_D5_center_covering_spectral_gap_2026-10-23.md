# Type E: D5 center-covering and signed-Gram separation (2026-10-23)

**[PROVED EXACTLY, conditional on the isolated-center twenty-pair reduction]** If u is an isolated unit center and z_1,...,z_20 are the projective half-differences of twenty deep endpoint pairs, then for EVERY independently signed, permuted and rotated D5 template W=(w_i),

    rho := max_i ||z_i-w_i|| >= sqrt(2/5)-1/2 > 0.13245,
    ||Z^T Z-W^T W||_op > 1/5.

**[PROVED EXACTLY: fourth-moment/variance bridge]** Let A=sum_i ||m_i||^2, S=sum_i z_i z_i^T, V=||S-(20-A)I/5||_F^2, and Delta4(W,Z)=sup_{||v||=1} |sum_i (v.z_i)^4-sum_i (v.w_i)^4|. Then

    Delta4(W,Z)+sqrt(V)/4 >= 3/5 + A/20.

**[OPEN]** D5 labeling/proximity, Type-E exclusion, C/D/generic branches, and tau_5=40. Global proved range remains 40<=tau_5<=44.

## 1. Exact isolated-center condition

For each endpoint pair x_i^+ = m_i+z_i, x_i^- = m_i-z_i, the isolated center u satisfies both -1/2<=u.x_i^+<=1/2 and -1/2<=u.x_i^-<=1/2. Thus

    |u.m_i|+|u.z_i|<=1/2, and hence |u.z_i|<=1/2.    (C)

This uses neither the midpoint-energy ceiling nor a D5 labeling.

## 2. Sharp D5 projective covering constant

For the twenty D5 unit lines w_ab^+ = (e_a+e_b)/sqrt(2), w_ab^- = (e_a-e_b)/sqrt(2), the maximum absolute correlation with a unit vector u is (a+b)/sqrt(2), where a>=b are the two largest absolute coordinates of u. If s=a+b, then the other three absolute coordinates are at most b, and

    1<=a^2+4b^2=(s-b)^2+4b^2<=5s^2/4

for 0<=b<=s/2 (convexity; check endpoints). Therefore

    max_i |u.w_i|>=sqrt(2/5).

Equality occurs when all five absolute coordinates are 1/sqrt(5). Combining this with (C) and the triangle inequality gives

    sqrt(2/5)<=max_i|u.w_i|<=1/2+rho.

This proves the first bound, superseding the older local rho>1/525 exclusion in the isolated-center setting only.

## 3. Exact signed-Gram spectral separation

Write F0=W^T W, F=Z^T Z, eps=||F-F0||_op. The D5 frame is tight: WW^T=4I_5, so P=F0/4 is an orthogonal projector of rank 5. Its range obeys

    ||y||_infty >= ||y||_2/sqrt(10), for every y in range(P),

by the D5 covering bound and ||W^T v||_2=2||v||.

Suppose eps<=1/5. Weyl's inequalities imply rank(F)=5 and the five nonzero eigenvalues lie in [4-eps,4+eps]. Set c=Z^T u, so ||c||_2>=sqrt(4-eps)>=sqrt(19/5). Since c belongs to range(F), (I-P)F0=0, and the inverse of F on its range has norm <=1/(4-eps),

    ||(I-P)c||_2 <= eps/(4-eps)||c||_2 <= ||c||_2/19.

Orthogonality gives ||Pc||_2>=sqrt(1-1/19^2)||c||_2. Consequently,

    ||c||_infty
      >= ||Pc||_infty-||(I-P)c||_2
      >= [sqrt(1-1/19^2)/sqrt(10)-1/19]||c||_2
      = (5/19)||c||_2
      >= sqrt(5/19) > 1/2,

contradicting (C). Thus eps>1/5, and the Frobenius signed-Gram gap also exceeds 1/5.

**Caution:** This is an ordinary signed-Gram theorem, NOT a theorem about the sign-invariant traceless Q-Gram. Such a translation remains open.

## 4. Fourth-moment / Q-frame variance bridge

The exact D5 quartic identity, valid for every v in R^5, is

    sum_i (v.w_i)^4 = (3/2)||v||^4+(1/2)sum_{a=1}^5 v_a^4.

For unit v, this is >=8/5. At the isolated center u, (C) implies

    sum_i (u.z_i)^4 <= (1/4)sum_i(u.z_i)^2
       = (1/4)u^T S u <= 1-A/20+sqrt(V)/4.

Taking the difference at u yields

    Delta4(W,Z)+sqrt(V)/4 >= 3/5+A/20.

The quartic tensor Frobenius distance ||sum z_i^(tensor 4)-sum w_i^(tensor 4)||_F dominates Delta4, so it obeys the same separation. This supplies a degree-four frame target in the six-exception problem, but it is not by itself a Type-E contradiction.

## Proof ledger

- **[PROVED EXACTLY]** Sharp D5 projective covering constant, conditional center-covering radius, ordinary signed-Gram spectral gap >1/5, and quartic/variance separation. The proofs are analytic; the companion checker verifies their exact rational/polynomial identities.
- **[CONDITIONAL]** Applying these to Type E uses the retained isolated-center endpoint reduction, twenty selected deep pairs, and center nonedge constraints.
- **[NOT PROVED]** A D5 labeling or proximity theorem for arbitrary Type E; any Q-Gram spectral gap deduced from the signed-Gram gap; Type-E elimination.
- **[RETAINED]** M(F3)<=89, matching mass S/2-28/3, A<=383/504, six exceptional core pairings, 40<=tau_5<=44. Types C, D, generic e>=27, and non-isolated branches remain open.

Next: combine the exact quartic tensor separation with the six-exception endpoint inequalities and Q-kernel constraints; do not replace the tensor by its scalar squared-correlation trace.
