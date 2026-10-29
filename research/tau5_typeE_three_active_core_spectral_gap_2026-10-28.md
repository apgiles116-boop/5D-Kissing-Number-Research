# Type E: three-active core spectral gap with Walsh-mixing penalty

Date: 2026-10-28. **[PROVED EXACTLY — standalone four-vector PSD theorem]**. **[CONDITIONAL TYPE E]** Application uses the retained F3 endpoint-charge theorem (at most three active core pairings) and retained matching-specific midpoint-energy floors. **[OPEN]** No Type-E exclusion or improvement to 40 <= tau_5 <= 44.

## Sharp three-active spectral theorem

For four Euclidean vectors m_i, put G_ij=m_i·m_j, C=tr G, and let E be any set of at most three pairs. Suppose nonnegative e_ij satisfy e_ij <= -G_ij on E. Let B_E be the adjacency matrix of E. Since G is PSD,

    sum_E e_ij <= -(1/2)tr(B_E G)
               <= -(lambda_min(B_E)/2) C
               <= (sqrt(3)/2) C.                         (1)

The last constant is sharp for this PSD relaxation: among all four-vertex graphs with at most three edges, the worst minimum adjacency eigenvalue is -sqrt(3), attained by K_{1,3}. The three-edge path has minimum eigenvalue -(1+sqrt(5))/2, and a triangle plus isolated vertex has -1. With one active edge the bound improves to C/2; with two, to C/sqrt(2).

The **exact nonnegative spectral remainder** is

    sqrt(3)*C/2-sum_E e_ij
      = (1/2)tr((B_E+sqrt(3)*I)G)+sum_E(-G_ij-e_ij).     (2)

A sharp rank-one Gram witness for (1) is m_i=sqrt(C/6)*(sqrt(3),-1,-1,-1)_i e_1, with E the three center-leaf pairs. This is NOT an F3 endpoint realization.

## Exact centroid refinement

Put M=sum_i m_i and b_i=||m_i||. For any six e_ij<=(-G_ij)_+,

    sum e_ij <= C-||M||^2/4.                             (3)

Indeed sum_{i<j} G_ij=(||M||^2-C)/2 and sum |G_ij|<=sum b_i b_j<=3C/2. The exact SOS-like remainder is

    C-||M||^2/4-sum e_ij
      = (1/4)sum_{i<j}(b_i-b_j)^2
        +(1/2)sum_{i<j}(b_i*b_j-|G_ij|)
        +sum_{i<j}((-G_ij)_+-e_ij) >=0.                (4)

The previously known quadratic negative-Gram inequality, with W=sum b_i m_i, is

    sum e_ij^2 <= (C^2-||W||^2)/4.                      (5)

The quadratic remainder follows from (-t)_+^2 <= (1-t)/2 for -1<=t<=1, weighted by b_i^2 b_j^2. No D5 labeling is used.

## Conditional F3 core and Walsh consequences

For four selected F3 matching edges write endpoints m_i +/- z_i, all unit. For a core pair define d_ij=(|z_i·z_j|-1/2)_+. On E={ij:d_ij>0}, let sigma_ij=sign(z_i·z_j), c_ij=m_i·z_j+sigma_ij z_i·m_j and q_ij=|c_ij|. The two relevant cross-endpoint kissing inequalities imply

    d_ij+q_ij <= -m_i·m_j.                              (6)

The retained F3 endpoint-charge and signed-triangle result gives |E|<=3. Hence (1), (3), (5) yield

    d+sum_E q_ij <= min(sqrt(3)*C/2, C-||M||^2/4),       (7)
    d2+sum_E(2*d_ij*q_ij+q_ij^2)
       <= (C^2-||W||^2)/4,                              (8)

where d=sum_E d_ij and d2=sum_E d_ij^2. In particular the old slack epsilon=C-d satisfies

    epsilon_raw >= (1-sqrt(3)/2) C+sum_E q_ij.          (9)

With the retained uniform F3 matching floor C>9/1000, epsilon_raw>0.00120577136594... . For P2, the retained C>=17/250 gives epsilon_raw>=0.00911027254265... . The earlier epsilon_neg>1/4250 implies epsilon_raw>1/4250; the new result improves the lower bound on **epsilon_raw**, NOT on the distinct epsilon_neg. These are conditional necessary bounds, not a contradiction.

## Direct 184-safe Q/Walsh bridge

For the twenty selected deep edges let a_i=||m_i||^2, A=sum a_i, U=sum a_i^2 and V=||sum z_i z_i^T-(20-A)I_5/5||_F^2. Let S_safe be the sum of (z_i·z_j)^2 over the 184 noncore pairings, and hminus=sum_core [1/4-(z_i·z_j)^2]_+. The global frame identity gives exactly

    S_safe=57/2-3A+A^2/10-U/2+V/2-d-d2+hminus.         (10)

Substituting (7)-(8) proves the new **incidence-sensitive second-order lower bound**

    S_safe >= 57/2-3A+A^2/10-U/2+V/2
              -sqrt(3)*C/2-C^2/4+||W||^2/4+hminus
              +sum_E ((1+2*d_ij)*q_ij+q_ij^2).          (11)

An additional nonnegative term

    [||M||^2/4-(1-sqrt(3)/2)*C]_+

may be added on the right of (11), using (3). This retains the exceptional Walsh mixing rather than discarding it. If a separate core squared-correlation cap C_K is used, the bound S_core<=3/2+sqrt(3)*C/2+C^2/4 beats C_K for C<sqrt(4*C_K-3)-sqrt(3): 0.363331019... for P1/P3 (C_K=473/256), and 0.298958793... for P2 (C_K=57/32). Those caps are retained, not independently recertified.

## Verification and ledger

The companion exact SymPy verifier checks all 42 labeled active graphs with at most three edges, the sharp star witness, the centroid identity, and the rational thresholds. **[RETAINED]** F3 <=89, matching M(P)>=S/2-28/3, selected mass >=2137/6, A<=383/504, and the Musin/Boyvalenkov zero-midpoint exclusion. **[OPEN]** The safe-pair upper bound needed to contradict (11), residual Type E, Types C/D, generic e>=27, and non-isolated branches. Sparse e=23/24 classification still requires delta(G)>=1. **Global proved range remains 40<=tau_5<=44.**
