# Type E: six-exception-robust D5 contact-frame stability (2026-10-23)

**[PROVED EXACTLY — conditional geometric theorem]** Let x_i^±=m_i±z_i be twenty unit endpoint pairs in R^5. Write A=sum_i ||m_i||^2, so m_i.z_i=0 and ||z_i||<=1. Call a pairing {i,j} *safe* if all four cross endpoint inner products lie in [-1/2,1/2]. Assume every pairing is safe except at most six, all among four distinguished core indices. This is the retained Type-E exceptional-pair pattern, but the theorem itself does not assume the full Type-E mass argument.

Let w_i be the twenty unit D5 projective representatives (e_a±e_b)/sqrt(2), after an arbitrary bijection, independent orientations, and a common orthogonal transformation. **Assume**, without claiming this labeling exists for Type E, that ||z_i-w_i||<=rho for every i. Let E_D5={{i,j}:|w_i.w_j|=1/2}; this graph has 120 edges.

**Theorem [EXACT, under the stated hypotheses]:** for 0<=rho<1/64,

    (3/8-24*rho)*A
       <= 2*sum_{{i,j} in E_D5, safe} (1/2-|z_i.z_j|)^2
       <= 960*rho^2,

and consequently

    A <= 960*rho^2/(3/8-24*rho).                         (T)

## Safe-contact Hadamard lemma [PROVED EXACTLY]

For a safe pairing set a=m_i.m_j, b=z_i.m_j, c=m_i.z_j, d=z_i.z_j. The four endpoint products are a+sigma*b+tau*c+sigma*tau*d. Their absolute values are <=1/2, hence

    |a+d|+|b+c|<=1/2,  |a-d|+|b-c|<=1/2.

Putting X=|a|, Y=|d| gives X+Y<=1/2 and

    b^2+c^2 <= (1/2-max(X,Y))^2+min(X,Y)^2
             <= (1/2-Y)^2+X^2 <= 2(1/2-Y)^2.            (H)

Thus exact safe projective contact |d|=1/2 forces a=b=c=0; nearby contacts control mixed midpoint/projective products quadratically.

## Exact D5 local spectral certificate

Each D5 line has twelve contact neighbors. Signed coordinate permutations act transitively. For the representative (e_1-e_2)/sqrt(2), the sum of its twelve neighbor projectors is diag(3,3,2,2,2).

After removing ANY three neighbors, the remaining projector sum S satisfies S-(3/8)I positive definite. The companion exact rational script checks all binom(12,3)=220 cases by Sylvester's criterion; the minimum leading principal minors across cases are

    9/8, 189/64, 13/512, 169/4096, 2197/32768.

Deleting fewer neighbors only increases S in PSD order. Since the at-most-six exceptional pairs lie among four core vertices, any vertex loses at most three D5 contact neighbors. Also ||z_j z_j^T-w_j w_j^T||_op<=2*rho. Therefore, for every vertex i,

    sum_{j~i, safe} z_j z_j^T >= (3/8-24*rho)I.

Summing m_i^T( ... )m_i gives the first inequality in (T) after applying (H). For each safe D5 contact, ||z_i.z_j|-1/2|<=2*rho and safety makes the difference nonnegative. Its mixed energy is <=8*rho^2; there are at most 120 contacts, giving the second inequality.

## Explicit forbidden neighborhood [CONDITIONAL ON RETAINED TYPE-E REDUCTIONS]

The earlier retained 21-line row-integrality theorem gives A>5313/500000 for Type E. At rho=1/525 the right side of (T) is exactly 512/48405 and

    5313/500000 - 512/48405 = 235153/4840500000 > 0.

Hence, **conditional on that earlier energy lower bound**, no Type-E configuration admits a D5 labeling with max_i||z_i-w_i||<=1/525. This does NOT show Type E is close to D5; the Type-E case remains OPEN.

Infinitesimal consequence: if z_i(t)=w_i+O(t^2) and m_i(t)=t*u_i+O(t^2) while the safety/exception pattern persists, then (T) gives A(t)=O(t^4), forcing every u_i=0. This is a quantitative second-order obstruction, not a proof of D5-labeling rigidity.

## Global Q-frame / six-exception bridge [EXACT IDENTITY; CONDITIONAL APPLICATION]

For twenty z_i put a_i=1-||z_i||^2, A=sum a_i, V=||sum z_i z_i^T-(20-A)I/5||_F^2, q_ij=z_i.z_j. Then

    sum_{i<j}q_ij^2=30-3A+A^2/10-(1/2)sum_i a_i^2+V/2.

For the six exceptional core pairings use the retained |q_ij|<=1/2+delta_ij, delta_ij=(-m_i.m_j)_+. Put C=sum_core a_i, d=sum delta_ij, d2=sum delta_ij^2, eps=C-d, eps2=C^2/4-d2>=0. (The eps2 identity follows by writing b_i=||m_i||, t_ij=(m_i.m_j)/(b_i b_j), W=sum b_i m_i: eps2=||W||^2/4+sum_{i<j}a_i*a_j*((1-t_ij)/2-max(-t_ij,0)^2), each summand nonnegative.) Then

    sum_safe q_ij^2 >= 28.5-3A-C+A^2/10-C^2/4
                     -(1/2)sum a_i^2+V/2+eps+eps2.

Under a_i<=1/4, A<=B=383/504, the sharp convex cap sum a_i^2<=3/16+(B-3/4)^2=47653/254016 yields

    sum_safe q_ij^2 >= 128429963/5080320 + V/2+eps+eps2.

If the separately retained matching-uniform eps>1/4250 applies, then

    sum_safe q_ij^2 > 54583242307/2159136000 + V/2+eps2.

This retains both global frame variance and squared core-defect slack, but does not exclude Type E.

**[OPEN]** Justifying a D5-type labeling/proximity for Type E; first-order rigidity after up to six core-core contact deletions; Type E/C/D and generic e>=27; non-isolated 41-code branches. Global proved range remains 40<=tau_5<=44. Preserve M(F3)<=89, M(P)>=S/2-28/3, selected mass >=2137/6, A<=383/504, and the delta(G)>=1 qualification on sparse e=23/e=24 classification.
