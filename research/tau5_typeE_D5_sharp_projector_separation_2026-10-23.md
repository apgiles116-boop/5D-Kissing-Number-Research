# Type E: sharp D5 quadratic center-covering and sign-invariant projector separation

2026-10-23. **[EXACT TEMPLATE THEOREM; CONDITIONAL TYPE-E APPLICATION]** New sharp sum-of-squares center-covering certificate. Global bound remains 40 <= tau_5 <= 44. No Type-E elimination is claimed.

## Sharp D5 quadratic covering theorem

For the twenty D5 projective representatives w_ab^s=(e_a+s e_b)/sqrt(2), 1<=a<b<=5 and s=+/-1, put q_i=(u.w_i)^2 for any unit u in R^5. Then

    sum_i max(q_i-1/4,0)^2 >= 9/40.                       (1)

The constant is attained at |u_a|=1/sqrt(5) for every a: ten q_i are 2/5 and ten are zero.

**Exact polynomial proof.** Set f(t)=max(t-1/4,0)^2 and p(t)=(39t^2-12t)/64. For 0<=t<=1/4, f(t)-p(t)=t(12-39t)/64>=0; for t>=1/4, f(t)-p(t)=(5t-2)^2/64>=0. D5 identities give sum q_i=4 and sum q_i^2=3/2+(1/2)sum_a u_a^4. Therefore

    sum_i f(q_i) >= 21/128+(39/128)sum_a u_a^4
                 >= 21/128+39/640 = 9/40,

since sum u_a^4>=1/5. Equality at equal absolute coordinates establishes sharpness. This is an analytic exact certificate, not a numerical optimization.

## Conditional isolated-center Type-E consequence

Let u be the isolated center, and z_i the twenty deep-edge half-differences. The endpoint constraints imply |u.z_i|<=1/2. For any independently signed/permuted and globally rotated D5 template w_i, put P_i=z_i z_i^T and P_i^0=w_i w_i^T. Whenever q_i=(u.w_i)^2>1/4,

    u^T(P_i^0-P_i)u >= q_i-1/4.

Hence

    sum_i [u^T(P_i^0-P_i)u]^2 >= 9/40,
    sum_i ||P_i-P_i^0||_F^2 >= 9/40,                     (2)

and the same aggregate bound holds using operator norms. The earlier pointwise D5 covering bound also gives max_i ||P_i-P_i^0||_op >= 3/20. These are **physical sign-invariant 5x5 projector** inequalities, not 20x20 Gram inequalities.

## Traceless Q-vector bound

Let a_i=||m_i||^2, A=sum a_i<=B=383/504, Q_i=P_i-(1-a_i)I/5, Q_i^0=P_i^0-I/5. With h_i=u^T(P_i^0-P_i)u, v_i=u^T(Q_i^0-Q_i)u=h_i-a_i/5, (2) and the reverse triangle inequality give

    ||v||_2 >= sqrt(9/40)-(1/5)sqrt(sum a_i^2).

Using a_i<=1/4 and A<=B, sum a_i^2<=B/4. As Q_i^0-Q_i is traceless and ||uu^T-I/5||_F=sqrt(4/5),

    (sum_i ||Q_i-Q_i^0||_F^2)^(1/2)
      >= (sqrt(5)/2)*(sqrt(9/40)-sqrt(B)/10)
      > 19 sqrt(5)/100.                                 (3)

With the retained sharp concentration cap M=47653/254016,

    sum_i ||Q_i-Q_i^0||_F^2
       >= (5/4)*(sqrt(9/40)-sqrt(M)/5)^2
       = 0.187904991801... .                             (4)

The rational simplification in (3) follows from sqrt(9/40)>47/100 and sqrt(B)/10<9/100.

## Proof-status ledger

- **[PROVED EXACTLY]** Sharp quadratic D5 covering theorem (1) and explicit degree-two polynomial minorant.
- **[CONDITIONAL ON RETAINED ISOLATED-CENTER REDUCTION]** Projector and Q-vector separation (2)-(4), valid for *every* chosen D5 labeling; none is assumed to exist.
- **[OPEN]** Conversion to a lower bound on the difference of **20x20 Q-Gram matrices**: an arbitrary O(14) isometry of Q feature vectors need not arise from physical O(5) conjugacy. Also open: D5 labeling/proximity, Type E, Types C/D, generic e>=27, non-isolated branch, and tau_5=40.
- **[RETAINED]** M(F3)<=89, matching S/2-28/3, A<=383/504, and 40<=tau_5<=44. The e=23/e=24 classification still assumes minimum degree at least one.

**Next target:** use six-exception Q-Gram/contact data to prove rank-one-preserving physical reconstruction or feed the sharp polynomial witness into a finite 21-line center-plus-twenty-lines KKT certificate. Do not equate physical Q-vector distance with Q-Gram distance.
