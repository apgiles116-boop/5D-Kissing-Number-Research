# Exact D5 Walsh-midpoint coercivity (2026-10-28)

**[PROVED EXACTLY — standalone complete D5 result].** Application to the actual Type-E branch is **[CONDITIONAL/OPEN]**: the retained rounding certificates justify only certain 16/17-line D5 subsystems, not a full aligned 20-line frame. No Type-E branch is eliminated. The global proved range remains 40 <= tau_5 <= 44.

Let x_i=(e_p +/- e_q)/sqrt(2) be the 20 projective D5 root representatives, v_i=sqrt(2)x_i, and C the 120 pairs with |x_i.x_j|=1/2 (70 other pairs are orthogonal). Write sigma_ij=2 x_i.x_j in {+1,-1} for contacts. Suppose 40 unit endpoints u_i^+ = m_i+y_i and u_i^- = m_i-y_i satisfy all cross-pair kissing inequalities. Set A=sum ||m_i||^2, epsilon^2=sum ||y_i-x_i||^2, and c_ij=y_i.m_j+sigma_ij m_i.y_j. Endpoint norms imply m_i.y_i=0 and ||m_i||^2+||y_i||^2=1.

## Exact linear spectral theorem

Define L on 20 vectors w_i in R^5 by 20 orthogonality rows v_i.w_i and 120 contact rows v_i.w_j+sigma_ij w_i.v_j. An exact 100-by-100 integer characteristic-polynomial calculation gives

det(tI-L^T L) =
(t-2)^20 (t-4)^10 (t-8)^10
(t^3-16t^2+74t-96)^15
(t^3-24t^2+146t-48)^5.

The smallest eigenvalue is the unique root of the last cubic in (1/3,7/20), approximately 0.348434647877. The other roots of this cubic lie in (10,11), (13,14), and the roots of the first cubic lie in (2,3), (4,5), (8,9). Consequently L has full column rank and ||Lw||^2 > (1/3)||w||^2 for all nonzero w.

## Nonlinear 120-contact Walsh stress inequality

For every contact, the two active-sign endpoint inequalities give

m_i.m_j + sigma_ij(y_i.y_j) + |c_ij| <= 1/2.

Let d_ij=1/2-sigma_ij(y_i.y_j), a_i=||m_i||^2, and R=sum_i Q(y_i), where Q(y)=yy^T-(||y||^2/5)I. The exact trace identity is

sum_(i<j)(y_i.y_j)^2
=30-3A+A^2/10-(1/2)sum a_i^2+(1/2)||R||_F^2.

If N is the squared-correlation sum on the 70 D5 orthogonal pairs, then

sum_C(d_ij-d_ij^2)
=3A-A^2/10+(1/2)sum a_i^2-(1/2)||R||_F^2+N.

The contact adjacency spectrum is {12:1, 2:4, -4:5, 0:10}, so sum_C m_i.m_j >= -2A. Since d_ij>=m_i.m_j+|c_ij|, it follows that

sum_C |c_ij| <= 5A+A^2/2+N+sum_C d_ij^2.

The final two terms are exactly the sum of squared off-diagonal Gram perturbations, bounded by (4+epsilon)^2 epsilon^2/2 because XX^T=4I_5. Therefore

**sum_C |c_ij| <= 5A + A^2/2 + (4+epsilon)^2 epsilon^2/2.**  (S)

This retains the first-order mixed midpoint terms lost by the averaged safe-pair inequality.

## Quantitative nonlinear gap

Let L_y replace each v_i in L by sqrt(2)y_i, retaining the D5 contact signs. Its matrix difference has Frobenius norm at most sqrt(26)epsilon. Orthogonality makes the 20 diagonal rows of L_y(m) vanish, and its contact rows equal sqrt(2)c_ij. Thus

(sqrt(lambda_min)-sqrt(26)epsilon)sqrt(A)
<=sqrt(2)[5A+A^2/2+(4+epsilon)^2 epsilon^2/2].  (G)

**[PROVED EXACTLY, CONDITIONAL ON THE ALIGNMENT HYPOTHESIS]** If epsilon^2<=A, then A=0 or A>1/2500. For 0<A<=1/2500, epsilon<=1/50. Rational estimates sqrt(lambda_min)>57/100, sqrt(26)<51/10, sqrt(2)<3/2 imply the left of (G) is > (117/250)sqrt(A), while the right is <=(98103/5000)A <= (98103/250000)sqrt(A), a contradiction.

For any differentiable feasible path through the full D5 antipodal configuration, m_i(t)=t w_i+o(t), y_i(t)=x_i+O(t), the stress inequality makes every c_ij(t)=O(t^2). Together with m_i.y_i=0, this gives Lw=0 and hence w=0: no nonzero first-order midpoint splitting of the complete D5 configuration.

**[OPEN]** The full-20 alignment and epsilon^2<=A are not established for Type E. In particular, sparse positive eight-line Q circuits do not automatically make all 120 full-D5 contact constraints active in a 16-line subsystem. The next step is a coupled 16-isolated-plus-4-core Walsh operator and a justified positive stress covering its contacts. Do not identify six exceptional core pairings with six Q-kernel dimensions without proof.

**[RETAINED]** Type E M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, rigorous Musin/Boyvalenkov zero-midpoint exclusion. Types C/D, generic e>=27, non-isolated branches remain open. Sparse e=23/24 classification requires delta(G)>=1.

Verifier: research/tau5_D5_full20_Walsh_midpoint_coercivity_2026-10-28_verify.py
