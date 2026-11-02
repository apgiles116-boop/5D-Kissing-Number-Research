# Type E: small isolated midpoint mass gives a stronger 16-line spectral gap

**Date 2026-11-01. [PROVED EXACTLY, CONDITIONAL ON RETAINED ISOLATED-CENTER HARMONIC AND F3 BROOM CERTIFICATES].** This does not eliminate Type E. Global proved range: **40 <= tau_5 <= 44**.

## Theorem

In Type E, H=16K2+F3, write the 16 isolated selected deep edges as x_i^±=m_i±z_i, a_i=||m_i||² in [0,1/4], x=sum_I a_i, S_I=sum_I z_i z_i^T. All isolated-isolated pairings are two-sided safe, hence |z_i.z_j|<=1/2.

**[EXACT, WITH STATED UPSTREAM INPUTS]** x<11/400. For *every* three-plane W in R5,

    sum_I ||P_(W^perp) z_i||² > 531/500 = 1.062,

and for *every* four-plane W,

    sum_I ||P_(W^perp) z_i||² > 73/200 = 0.365.

Thus the ordered eigenvalues of S_I obey lambda_4+lambda_5>531/500 and lambda_5>73/200. This improves the earlier cap-only >4/5 and >11/250 without assuming D5 labeling, core coplanarity, rank 13, or a twenty-edge matching theorem.

## Exact small-isolated-mass certificate

Use the retained isolated-center harmonic theorem N+(35/6)||T||_F²+14K_4>=2595/256, and the F3 broom M(F3)<=89. With F(t)=28t⁴-7t² and D(a)=21-F(2a-1)=196a-644a²+896a³-448a⁴, the exact Delsarte deep-mass identity gives

    336 - sum_I D(a_i) + M(F3) >= 410 + 2595/256,

so sum_I D(a_i)<=1245/256. On [0,1/4], D is increasing, concave, D(0)=0, and D(a)>=84a. Hence x<=415/7168<1/4, and subadditivity gives D(x)<=sum_I D(a_i). The strict rational certificate

    D(11/400)-1245/256 = 23228613/400000000 > 0

forces x<11/400. The center-harmonic theorem and broom bound are **retained upstream results**, not independently re-established in this note.

## Weighted harmonic projection and exact contradictions

Fix d=3 or 4, W a d-plane, ell_i=||P_(W^perp)z_i||², L=sum ell_i, b_i=a_i+ell_i, B=x+L, r_i=1-b_i, w_i=P_W z_i. Then |w_i.w_j|<=1/2+sqrt(ell_i ell_j). The positive harmonic polynomial f(t)=t⁴-t²/4 has expansions

    d=3: f=(7/60)P0+(17/42)P2+(8/35)P4;
    d=4: f=(1/16)U0+(1/8)U2+(1/16)U4.

The previously proved exact weighted-harmonic and leakage-moment estimates give

    H_d(B) <= sum_{i<j}[(w_i.w_j)^4-r_i*r_j*(w_i.w_j)^2/4] <= U(B,L),

where alpha_3=7/60, alpha_4=1/16,

    H_d(B)=alpha_d/2*(16-2B+B²/16)²-3*M(B)/8,
    M(B)=15+(1-B)^4 for 0<=B<=1,
         14+(2-B)^4 for 1<=B<=2,
    U(B,L)=15B/16+45L/16+293L²/256+5L³/16+L⁴/16.

The proof of these universal envelopes is in the preceding 2026-11-01 refined sixteen-line leakage note. U increases in B,L. On either piece of M,

    H_d'(B)=alpha_d*(16-2B+B²/16)*(-2+B/8)
            +(3/2)*(k+1-B)^3, k=0 or 1.

For d=3, if L<=531/500, then B<2179/2000<11/10. On [0,11/10], H_3'(B)<=-11989/8000<0. But the exact endpoint margin is

    H_3(2179/2000)-U(2179/2000,531/500)
      =1042276961532727/491520000000000000 > 0,

contradicting H_3(B)<=U(B,L). For d=4, if L<=73/200, then B<157/400<2/5. On [0,2/5], H_4'(B)<=-141/400<0, whereas

    H_4(157/400)-U(157/400,73/200)
      =843766658257/209715200000000 > 0.

This proves both leakage inequalities with exact rational margins. The eigenvalue corollary follows from Ky Fan min-max.

## Conditional two-ray tomography

**[EXACT, ADDITIONALLY CONDITIONAL ON RETAINED RANK-13/TWO-MISSING-RAY/AMBIGUOUS COPLANAR-CORE HYPOTHESES].** For orthonormal missing-plane axes p,q put X=p^T S_I p, Y=q^T S_I q. Then X,Y>73/200, X+Y>531/500, so

    XY > (73/200)*(531/500-73/200) = 50881/200000.

The previously established double-angle core wedge and two-ray Cauchy-Binet factorization for the safe 16x4 squared-correlation matrix D give

    sum_(i<j,c<d)(D_ic D_jd-D_id D_jc)²
      >=(81/131072)X²Y²
      >209698969041/5242880000000000
      ~=3.9996904190e-5.

With rank(D)=2 and ||D||_F²<=4, its second singular value obeys

    sigma_2(D)>457929*sqrt(2)/204800000 ~=0.003162155285.

These improve the preceding conditional minor and singular-value floors by factors ~58.5 and ~7.65. They are **necessary lower bounds**, not contradictions. The extra rank/two-ray/core hypotheses are not derived here.

## Status and dependencies

**[VERIFIED LOCALLY]** Companion exact rational/SymPy script checks the polynomial and harmonic identities, both rational contradiction margins, monotonicity constants and tomography fractions. The analytic proofs establish the universal statements; finite checks verify algebra only.

**[OPEN]** Need an F3-incidence-sensitive *upper* bound on safe minors or sigma_2(D) incompatible with the new lower bounds. Type E, Types C/D, generic e>=27 and non-isolated branches remain open. Sparse e=23/24 classification is conditional on delta(G)>=1. Retain star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, both defect ceilings and Musin/Boyvalenkov 21-line boundary theorem. Do not identify the six exceptional core pairings with the six D5 Q-kernel modes.

Dependencies: research/tau5_typeE_isolated_center_harmonic_gap_2026-10-28.md; research/tau5_typeE_16line_refined_leakage_2026-11-01.md; and the earlier rank-13/two-ray/core-wedge result for the final section. **Global proved range unchanged: 40<=tau_5<=44.**