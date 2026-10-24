# Sharp D5 center hinge-square theorem and second-order stability

Date: 2026-10-24. Status: **[PROVED EXACTLY]** D5-template theorem and projector/Q-column consequences; **[CONDITIONAL TYPE E]** application under isolated-center and midpoint bounds; **[OPEN]** global D5 labeling, intrinsic Gram strengthening, Type E elimination.

## Theorem: sharp D5 center excess

For the twenty D5 projective lines v_ij^±=(e_i±e_j)/sqrt(2), 1<=i<j<=5, and every unit u in R^5, set q_ij^±=(u·v_ij^±)^2 and h(q)=(q-1/4)_+^2. Then

    sum_{i<j,±} h(q_ij^±) >= 9/40.                    (1)

The constant is sharp. Equality holds exactly when |u_1|=...=|u_5|=1/sqrt(5); then ten q's are 2/5 and ten are 0.

**Exact polynomial certificate.** For 0<=q<=1,

    h(q) >= p(q):=39q^2/64-3q/16.

For q<=1/4, p(q)=q(39q-12)/64<=0. For q>=1/4, h(q)-p(q)=(5q-2)^2/64>=0. The D5 moments are

    sum q=4,   sum q^2=3/2+(1/2)sum_{i=1}^5 u_i^4.

Cauchy-Schwarz gives sum u_i^4>=1/5, proving (1).

**Exact SOS/stability identity.** Define R(q)=q(12-39q)/64 for q<=1/4 and R(q)=(5q-2)^2/64 for q>=1/4. Then

    sum h(q)-9/40
      = (39/128)sum_i (u_i^2-1/5)^2 + sum R(q).       (2)

Both terms on the right are nonnegative. This is a quantitative second-order stability statement about the D5 template's center direction.

## Projector separation

Let z_1,...,z_20 be arbitrary projected vectors, paired with any common orthogonal rotation and ordering of the D5 template. Suppose a unit isolated center u obeys (u·z_i)^2<=1/4. Put P_i=z_i z_i^T and P_i^0=v_i v_i^T. For each q_i^0=(u·v_i)^2>1/4,

    u^T(P_i^0-P_i)u >= q_i^0-1/4.

Consequently,

    sum_i [u^T(P_i^0-P_i)u]^2 >= 9/40,
    sum_i ||P_i-P_i^0||_F^2 >= 9/40.                 (3)

These hold for every *attempted* D5 labeling/alignment. They do not establish that a global D5 labeling exists.

## Trace-free Q-column consequence

For Type E let a_i=||m_i||^2, Q_i=P_i-(1-a_i)I/5, and Q_i^0=P_i^0-I/5. Retain A=sum a_i<=383/504 and a_i<=1/4, which imply sum a_i^2<=S=47653/254016. With V=uu^T-I/5, ||V||_F^2=4/5, (3) and Minkowski yield

    sqrt(9/40)
      <= sqrt(4/5) sqrt(sum_i ||Q_i-Q_i^0||_F^2) + sqrt(S)/5.

Therefore

    sum_i ||Q_i-Q_i^0||_F^2
      >= (5/4)(sqrt(9/40)-sqrt(47653/254016)/5)^2
       = 1476493/5080320 - sqrt(476530)/6720
       > 1879/10000.                               (4)

At zero midpoint energy, the right-hand lower bound improves to 9/32.

## Proof-status limitations

- **[PROVED EXACTLY]** (1)-(4), using only elementary polynomial inequalities, D5 moments, and Hilbert-Schmidt Cauchy-Schwarz.
- **[CONDITIONAL TYPE E]** The center cap (u·z_i)^2<=1/4 and midpoint cap are retained isolated-center inputs.
- **[NOT PROVED]** D5 labeling/proximity or a conversion of column separation (4) into an intrinsic Q-Gram separation. Do not confuse column differences with Gram differences.
- **[UNCHANGED]** The retained intrinsic spectral result ||G_Q-G_D5||_op>139/250 remains available. Type E, Types C/D, and generic e>=27 remain open. Global range remains 40<=tau_5<=44; F3 broom M(F3)<=89 and matching M(P)>=S/2-28/3 unchanged.

The value of (2) is as an explicit SOS penalty in future labeled second-order or finite KKT analysis, not as a standalone Type-E contradiction.
