# Type E: rank-14 Schur kernel suppression improves the Q-Gram center gap

23 October 2026. **EXACT THEOREM; conditional application to retained isolated-center Type-E assumptions.** No Type-E exclusion or global D5 labeling is claimed.

## Rank-constrained quadratic kernel theorem

Let G0 be an n-by-n PSD matrix of rank r and smallest nonzero eigenvalue gamma>0. Let G be PSD with rank at most r, and d=||G-G0||_op<gamma. If P projects onto ker(G0), then

    0 <= P G P <= d^2/(gamma-d) P.

Proof: in ran(G0) ⊕ ker(G0), write G=[[H,B],[B^T,C]], with H >= (gamma-d)I. Since rank(G)<=r and H is invertible, the Schur complement vanishes: C=B^T H^{-1}B. As ||B||<=d, the claimed bound follows.

## Type-E consequence

For the 20 D5 projective lines, G0 is the Gram matrix of Q(w)=ww^T-I/5, with exact spectrum 3/2 (4), 1 (10), 0 (6), and G0*1=0. For Type E, Q_i=z_i z_i^T-(1-a_i)I/5, a_i=||m_i||^2 in [0,1/4], A=sum a_i<=383/504. G=Gram(Q_i) is PSD of rank <=14. For d=||G-G0||_op<1, the theorem gives

    V=||sum Q_i||_F^2=1^T G 1 <= 20 d^2/(1-d).  (1)

This also controls each of the other five D5 kernel relations under any fixed template labeling.

Let u be the isolated unit center and q_i=(u.z_i)^2<=1/4. Define v=uu^T-I/5, b_i=q_i-(1-a_i)/5. The physical 14-dimensional Q-frame has lower spectral bound 1-d, so

    sum b_i^2 >= (4/5)(1-d).  (2)

Introduce the nonnegative slack

    S=sum_i [q_i(1/4-q_i)+(2/5)a_i(1/4-q_i)+(1/25)a_i(1/4-a_i)] >=0.

The following is an exact expansion, with t=<v,sum Q_i>:

    sum b_i^2 = 1/5+3A/50-(3/20)t-S.  (3)

By Cauchy-Schwarz and (1), |t|<=4d/sqrt(1-d). Combining (2),(3) gives the strengthened necessary inequality

    40d+30d/sqrt(1-d) >= 30-3A+50S >= 4657/168.  (4)

The left side is increasing on [0,1). At d=5/14, (4) is false: the positive remainder is 2257/168 and its square minus (25 sqrt(14)/7)^2 equals 54049/28224>0. Thus

    BOXED: ||G-G0||_op > 5/14 = 0.357142857...

The root of equality in (4) is approximately 0.35795636754720327, an additional algebraic refinement. This holds for **every permutation** of G0, without assuming D5 proximity.

## Six-exception tradeoff

If under a chosen labeling G-G0=R+E, where E is supported on the six core-core off-diagonal entries and eta=max |E_ij|, then ||E||_op<=3eta. Therefore

    BOXED: ||R||_op+3eta > 5/14.

For example, ||R||_op<=1/7 forces eta>1/14. No bound on ||R|| is inferred from the scalar homogeneous-defect estimate.

## Proof status

* **PROVED EXACTLY:** rank-constrained Schur kernel theorem and rational 5/14 comparison.
* **CONDITIONAL TYPE-E CONSEQUENCE:** Q-Gram spectral separation and slack-retaining inequality.
* **OPEN:** global D5 labeling, six-exception operator-norm upper bound, Type E exclusion.
* **UNCHANGED:** 40<=tau_5<=44; Type E M(F3)<=89, matching M(P)>=S_F3/2-28/3, A<=383/504; C,D,generic e>=27 and non-isolated branches open; e=23/24 classification requires delta(G)>=1.

Companion exact checker: `tau5_typeE_rank14_kernel_quadratic_gap_2026-10-23_verify.py`.
