# Type E: exact isolated-center / D5 midpoint-energy dual theorem (2026-10-24)

**Proof status:** [PROVED EXACTLY] universal center-to-normalized-line inequality, quartic dual minorant, sharp D5-template center-only energy theorem, and a second-order stability identity. [CONDITIONAL] D5-template application. [OPEN] Type E elimination.

## Universal center constraint

Let u be a unit center and x_i^+ = m_i + z_i, x_i^- = m_i - z_i be unit endpoints, with m_i dot z_i = 0, a_i = ||m_i||^2 <= 1/4, and ||z_i||^2 = 1-a_i. Assume u dot x_i^+ <= 1/2 and u dot x_i^- <= 1/2. Define v_i = z_i/sqrt(1-a_i) and q_i = (u dot v_i)^2.

The center inequalities and Cauchy-Schwarz in the orthogonal complement of v_i imply

    sqrt(1-a_i)*sqrt(q_i) - sqrt(a_i)*sqrt(1-q_i) <= 1/2.       (1)

By angle addition, necessarily

    q_i <= ((sqrt(1-a_i)+sqrt(3*a_i))/2)^2 <= 3/4.             (2)

Define g(q) = 0 for 0 <= q <= 1/4, and

    g(q) = (1+2q-2sqrt(3q(1-q)))/4, for 1/4 <= q <= 1.

Then a_i >= g(q_i). This is sharp for an individual center/endpoint-pair subsystem. In particular, ((q_i-1/4)_+)^2 <= a_i, sharply, since (q_i-1/4)_+ <= sqrt(a_i)*(sqrt(a_i)+sqrt(3(1-a_i)))/2 <= sqrt(a_i).

**Proof-status audit:** The actual isolated-center constraints imply u dot m_i + |u dot z_i| <= 1/2, NOT automatically |u dot z_i| <= 1/2. Earlier Type-E applications assuming the latter raw cap need an additional proof.

## Exact quadratic dual certificate

Let alpha = 25(sqrt(2)-1)/16 > 0, beta = 7/4 - 11sqrt(2)/8 < 0, and p(q) = alpha*q^2 + beta*q.

**[PROVED EXACTLY]** g(q) >= p(q) for 0 <= q <= 1, with equality precisely at q=0 and q=2/5.

For q <= 1/4, p(q) <= 0 = g(q), since alpha/4 + beta = (87-63sqrt(2))/64 < 0. For q >= 1/4, g''(q) = sqrt(3)/(8(q(1-q))^(3/2)) >= sqrt(3) > 2alpha = p''(q). The two functions have matching values and first derivatives at q=2/5. Strict convexity proves the claim.

Therefore, with no D5 hypothesis,

    A = sum_i a_i >= alpha*sum_i (u dot v_i)^4
                    + beta*sum_i (u dot v_i)^2.              (3)

This is a universal quartic center-energy inequality in the normalized projectors.

## Sharp D5-template consequence

**[PROVED EXACTLY, CONDITIONAL ON NORMALIZED D5 LINES]** Suppose the twenty v_i are exactly the D5 projective template (e_j +/- e_k)/sqrt(2). For any unit u, put q_jk^+ = (u_j+u_k)^2/2 and q_jk^- = (u_j-u_k)^2/2. Then

    sum q_i = 4,
    sum q_i^2 = 3/2 + (1/2)sum_j u_j^4 >= 8/5.

Inserting these into (3) gives the sharp center-only bound

    A >= 9/2 - 3sqrt(2) = 0.257359312880714854...           (4)

For equality in the center-only subsystem, take u=(1,1,1,1,1)/sqrt(5). Ten D5 lines have q=2/5, ten have q=0. For the first ten, choose a=g(2/5)=9/20-3sqrt(2)/10, z=sqrt(1-a)*v, and m=-sqrt(a)*(u-(u dot v)v)/sqrt(1-q). For the others choose a=0, m=0, z=v. Every endpoint has norm one and satisfies the center inequalities, and total A equals (4). This does NOT establish pairwise feasibility of the forty endpoints or a Type-E code.

## Exact second-order stability

Let R(q)=g(q)-p(q) >= 0. The D5 moment identities give the exact decomposition

    A-(9/2-3sqrt(2))
      = sum_i(a_i-g(q_i)) + sum_i R(q_i)
        + (alpha/2)*sum_j(u_j^2-1/5)^2.                     (5)

All terms on the right are nonnegative. Thus the energy excess controls center-coordinate imbalance and deviations from the two D5 equality values q=0 and q=2/5.

For arbitrary normalized lines v_i and any attempted D5 labeling w_i, let E=sum_i ||v_i v_i^T-w_i w_i^T||_F^2. Since |q_i-q_i^0| <= ||v_i v_i^T-w_i w_i^T||_F and max_{[0,1]} |p'(q)| = K=(14sqrt(2)-11)/8,

    A + K*sqrt(20E) >= 9/2-3sqrt(2).                        (6)

This is a columnwise/template comparison, not an intrinsic Q-Gram estimate.

## Ledger

[PROVED EXACTLY] (1)-(3), the D5-template implication (4), identity (5), and conditional comparison (6).
[CONDITIONAL TYPE E] (4)-(6) require a D5 normalized-line labeling or alignment, not yet established.
[OPEN] A labeling-free lower bound from the six-exception structure; Type E elimination.
[UNCHANGED] 40 <= tau_5 <= 44; M(F3) <= 89; M(P) >= S/2-28/3; A <= 383/504; audited 21-line zero-midpoint exclusion. Types C, D, and generic e>=27 remain open.

**Next step:** insert (3) as a center-row quartic constraint in the rank-five endpoint Gram polynomial problem, and seek a labeling-free lower bound from six-exception geometry.
