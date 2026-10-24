# Type E: full D5 Q-kernel projection and a ternary exact certificate

2026-10-23. **Status: exact finite verification + analytic proof, conditional on retained isolated-center Type-E hypotheses. NOT a Type-E elimination.**

## Hypotheses and frame lemma

Twenty deep edges have endpoints x_i^±=m_i±z_i in R^5. Let a_i=||m_i||^2 in [0,1/4], A=sum a_i<=B=383/504, ||z_i||^2=1-a_i. For the isolated unit center u, q_i=(u.z_i)^2<=1/4. Define Q_i=z_i z_i^T-(1-a_i)I/5, G_ij=tr(Q_i Q_j), and G0 the twenty-line D5 Q-Gram in any order. Let d=||G-G0||_op.

Let U project onto ran G0, which has dimension 14; its orthogonal complement is the **full six-dimensional kernel**. For v=uu^T-I/5, ||v||_F^2=4/5, and b_i=<Q_i,v>=q_i+a_i/5-1/5. The feature map F with columns Q_i has rank<=14. If d<1, its restriction to ran G0 is square and has minimum squared singular value >=1-d. Therefore ||Ub||^2>=(4/5)(1-d). For d>=1 the desired conclusion is immediate. Since U1=0,

    d >= 1-(5/4)||U(q+a/5)||^2.                       (1)

This retains all five additional D5 kernel directions beyond the all-ones relation.

## Exact projector

Index the ten K5 supports in lexicographic order, with two signed D5 lines per support. U=M/30, where M is the symmetric integer matrix with diagonal 21; off-diagonal -9 for the two lines on the same support; +1 for lines on different intersecting supports; and -4 for disjoint supports. Direct integer identities M^2=30M, M1=0, tr(M)=420 show U is an orthogonal projector of rank 14. The checker verifies U=(5/3)G0-(2/3)G0^2 and the spectrum of G0: 3/2 (4), 1 (10), 0 (6).

## Exact finite scalar optimization

For fixed a, the PSD quadratic ||U(q+a/5)||^2 is convex in q, so its maximum over q_i in [0,1/4] occurs at q=x/4 for binary x. Then

    ||U(q+a/5)||^2
      = (x^T M x)/480+(x^T M a)/300+(a^T U a)/25.  (2)

Let t1>=t2>=t3>=t4>=0 be the four largest positive parts of the entries of Mx. Capped-simplex linear maximization with B=3/4+5/504 gives

    (x^T M a)/300 <= (t1+t2+t3)/1200+t4/30240.

Define the integer

    N(x)=315(x^T M x)+126(t1+t2+t3)+5t4.

Swapping the two signed indices within any support preserves M and N. Hence only the 3^10=59049 support occupancies s_e=x_(e,+)+x_(e,-) in {0,1,2} need enumeration. The standalone pure-Python integer verifier checks every case and obtains

    max N(x)=52995 (21 maximizing occupancy patterns);
    max [quadratic x term + linear a term]=3533/10080. (3)

No floating-point search is used.

For nonnegative a, since U_ii=7/10 and U_ij<=1/30,

    a^T U a <= (2/3)sum a_i^2 + A^2/30.

At A<=B, the capped-simplex maximum is three a_i=1/4 and one a_i=5/504, yielding

    a^T U a <= 52369/362880.                         (4)

Combining (2)-(4),

    ||U(q+a/5)||^2 <= 3533/10080+52369/(25*362880)
                       = 3232069/9072000.             (5)

This bound is **sharp for the relaxed scalar constraints**: take binary mask x=28443 (index 0 is least significant bit), a_0=a_8=a_10=1/4, a_13=5/504, other a_i=0. This is NOT asserted to be physically realizable as Type E.

## Improved conditional gap

From (1) and (5), for every D5 labeling/permutation,

    ||G-G0||_op >= 4025531/7257600
                 = 0.5546642140652557... .            (6)

The previous bound 56198549/101606400=0.5531004838277904... is strictly weaker. If G-G0=R+E under a chosen D5 labeling and E is supported on six exceptional core-core entries with eta=max|E_ij|, then ||R||_op+3eta>=4025531/7257600. This is only a **necessary** tradeoff, not a Type-E contradiction.

## Proof-status ledger

**ANALYTIC EXACT:** frame inequality, D5 projector, capped-simplex quadratic bound.
**FINITE EXACT:** 59,049 integer cases for max N=52995, checked by companion script.
**CONDITIONAL ON RETAINED TYPE-E HYPOTHESES:** Q-Gram gap (6).
**OPEN:** global D5 proximity/labeling; upper safe/exceptional perturbation bound; Type E, C, D, generic e>=27, non-isolated branches.
**UNCHANGED:** 40<=tau_5<=44, M(F3)<=89, matching mass >=S_F3/2-28/3, A<=383/504, and conditional sparse graph classification for delta(G)>=1.
