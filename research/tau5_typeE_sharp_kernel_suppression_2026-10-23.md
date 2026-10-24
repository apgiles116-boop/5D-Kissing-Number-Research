# Type E: sharp kernel suppression and a stronger isolated-center Q-Gram gap

2026-10-23. **PROOF STATUS: exact general matrix theorem; conditional exact Type-E consequence.** No elimination of Type E or global D5 labeling is claimed.

## Theorem A: sharp quadratic kernel suppression

Let G0 be a real PSD n-by-n matrix of rank r, with smallest positive eigenvalue gamma>0. Let G be PSD with rank(G)<=r. Put d=||G-G0||_op, and let P be the orthogonal projector onto ker(G0). Then

    0 <= P G P <= (d^2/gamma) P.                         (A)

This is sharp for every 0<=d<=gamma. It improves the earlier denominator-dependent bound d^2/(gamma-d).

**Proof.** For d<gamma, use the orthogonal decomposition ran(G0) + ker(G0):

    G0 = [[D,0],[0,0]],  D>=gamma I_r,
    G  = [[H,B],[B^T,C]].

H>= (gamma-d)I, so H is invertible. The PSD rank bound makes the Schur complement zero: C=B^T H^(-1)B. For any unit kernel vector k, set h=H^(-1)Bk, c=k^TCk=h^THh. If h=0, c=0. Otherwise e=h/||h|| is a unit support vector. Compress G and G0 to span(e,k). The compression of G has rank one because G(-h,k)=0, whereas the compression of G0 is diag(alpha,0), alpha=e^TDe>=gamma. The determinant of their difference is -alpha*c. The operator norm of the compressed difference is <=d, hence alpha*c<=d^2 and c<=d^2/gamma. For d>=gamma, directly c=k^T(G-G0)k<=d<=d^2/gamma.

**Sharpness witness.** Take G0=diag(gamma,0), G=gamma*v*v^T with v=(sqrt(1-(d/gamma)^2),d/gamma). Then ||G-G0||_op=d and PGP=d^2/gamma.

## Theorem B: improved isolated-center D5 Q-Gram gap

Retain the twenty Type-E pairs x_i^±=m_i±z_i in R^5, with a_i=||m_i||^2 in [0,1/4], A=sum a_i<=B=383/504, ||z_i||^2=1-a_i, and isolated unit center u with q_i=(u.z_i)^2<=1/4. Let Q_i=z_i*z_i^T-(1-a_i)I/5, G_ij=tr(Q_i Q_j), and G0 the exact twenty-line D5 Q-Gram under any permutation. Set d=||G-G0||_op.

The D5 spectrum is 3/2 (four), 1 (ten), 0 (six), and G0*1=0. Since rank(G)<=14, Theorem A gives the stronger frame-variance estimate

    V=||sum Q_i||_F^2 = 1^T G 1 <=20d^2.               (B1)

Let v=u*u^T-I/5, ||v||_F^2=4/5, b_i=q_i-(1-a_i)/5, t=sum b_i. For d<1, Weyl's theorem gives the physical fourteen-dimensional frame bound

    sum b_i^2 >= (4/5)(1-d).                            (B2)

The following identity is exact:

    sum b_i^2 = 1/5+3A/50-(3/20)t-S,

    S=sum_i[q_i(1/4-q_i)
       +(2/5)a_i(1/4-q_i)
       +(1/25)a_i(1/4-a_i)] >=0.                        (B3)

By Cauchy-Schwarz and (B1), |t|<=sqrt(4V/5)<=4d. Combining (B2)-(B3), and noting d>=1 is automatic, yields

    70d >= 30-3A+50S.                                  (B4)

Without the concentration correction, this gives d>=4657/11760 = 0.39600340136...

## Exact concentration correction

For 0<=a_i<=1/4 and sum a_i=A, the minimum of sum a_i(1/4-a_i) occurs with as many entries 1/4 as possible and at most one fractional entry r=A-floor(4A)/4. It equals r(1/4-r). The function 30-3A+2r(1/4-r) is decreasing on each interval [k/4,(k+1)/4] (derivative -5/2-4r). At B=383/504=3/4+5/504, r_B=5/504. Therefore

    70d >=30-3B+2*(5/504)*(1/4-5/504)
         =3521297/127008.

Thus the **new exact gap** is

    BOXED: ||G-G0||_op >=3521297/8890560
            =0.396071451067199... >99/250.           (B5)

This holds for every permutation of G0. It is a necessary separation, not a Type-E contradiction.

## Six-exception tradeoff (conditional on a chosen D5 labeling)

If G-G0=R+E, with E supported on the six off-diagonal entries among four core indices and eta=max_core |E_ij|, then ||E||_op<=3eta, so

    ||R||_op+3eta >=3521297/8890560 >99/250.

No upper bound on this expression follows yet from the retained homogeneous positive-defect estimate.

## Proof ledger

- **PROVED EXACTLY:** sharp general kernel theorem (A), with explicit equality example.
- **PROVED UNDER RETAINED TYPE-E HYPOTHESES:** (B1)-(B5), including exact concentration correction.
- **CONDITIONAL ON A CHOSEN D5 LABELING:** six-exception operator-norm tradeoff.
- **OPEN:** global D5 labeling/proximity; Type-E elimination; Types C, D, generic e>=27, and non-isolated branches.
- **UNCHANGED:** global 40<=tau_5<=44; M(F3)<=89; M(P)>=S_F3/2-28/3; A<=383/504. Sparse e=23/e=24 classification requires delta(G)>=1.

Companion exact verifier: tau5_typeE_sharp_kernel_suppression_2026-10-23_verify.py.
