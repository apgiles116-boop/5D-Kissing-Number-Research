# Type E: rank-13 two-ray safe-correlation bridge (2026-10-31)

**Status:** exact conditional structural theorem, NOT Type-E elimination. Global proved range remains 40 <= tau_5 <= 44.

## Theorem 1: rank-two safe cross-block and nonzero minors

Take 16 isolated selected-edge projected vectors z_i and four F3 core projected vectors z_c. Assume the isolated traceless Q_i = z_i z_i^T - ||z_i||^2 I/5 span rank 13 in Sym_0(5), their missing matrix S has rank two, and all four core projectors have genuinely distinct rank-one completions with the same isolated safe measurements and norms.

Orthogonally choose p,q so S is proportional to pq^T+qp^T. Then every isolated z_i=x_i p+y_i q+w_i satisfies x_i y_i=0, and every ambiguous core z_c=u_c p+v_c q has u_c v_c != 0. Define r_c=u_c^2, s_c=v_c^2, t_c=r_c+s_c, and the 16x4 SAFE matrix

D_ic = (z_i.z_c)^2 = <Q_i,Q_c>+||z_i||^2 t_c/5.

Each row of D is either x_i^2 r, y_i^2 s, or zero. Consequently rank(D)<=2 and rank([D;t_C])<=2.

For any two distinct selected deep edges a_i=||m_i||^2<1/4, the endpoint inequalities give m_i.m_j+|z_i.z_j|<=1/2. Parallel z_i,z_j would make the left side at least sqrt((1-a_i)(1-a_j))-sqrt(a_i a_j)>3/4-1/4=1/2. Thus the four core lines are distinct. If r and s were proportional, their four directions would occupy at most two projective lines (same absolute coordinate slope), a contradiction. Hence r,s are independent.

The 13 isolated Q matrices span the full hyperplane of traceless symmetric matrices with pq entry zero. Its p-W and q-W blocks (W=span(p,q)^perp) each have dimension three, so at least three isolated rows of each type are active. Rows with x_i=y_i=0 span at most six Q dimensions, hence at least seven rows are active. Thus rank(D)=2.

Define Delta_ij^cd=D_ic D_jd-D_id D_jc. For opposite-type active rows it equals x_i^2 y_j^2(r_c s_d-r_d s_c), while same-type pairs have all minors zero. The graph of row pairs having any nonzero minor is complete bipartite on the active rows. Each absolute core slope can occur for at most two core directions, so at least four of the six core-column determinants are nonzero. There are at least 3*4=12 opposite-type active row pairs; hence at least 48 nonzero two-by-two minors, counted by row and column pair. This is a nonvanishing result, NOT a uniform magnitude gap.

## Theorem 2: recovery and eight coherent signs

Choose a nonzero safe minor Delta=Delta_ij^cd. Put

alpha=(t_c D_jd-t_d D_jc)/Delta,
beta=(D_ic t_d-D_id t_c)/Delta.

After swapping p and q if needed, alpha=1/x_i^2>0 and beta=1/y_j^2>0. For every core k,

r_k=alpha D_ik, s_k=beta D_jk, t_k=r_k+s_k.

All six exceptional core squared correlations are then reconstructed up to at most eight sign patterns (one global sign irrelevant):

(z_c.z_d)^2=r_c r_d+s_c s_d+2 eps_c eps_d sqrt(r_c s_c r_d s_d).

The retained raw-defect ceiling becomes an explicit eight-sign test by summing (sqrt((z_c.z_d)^2)-1/2)_+ over the six core pairs. Its upper bound is 1780062775/4032758016. Homogeneous defect is a separately defined certificate and is not identified with this raw sum.

## Theorem 3: exact sign cancellation in the 184-safe Q energy

Let A=sum_20 ||m_i||^2, U=sum_20 ||m_i||^4, T=sum_20 z_i z_i^T, V=||T-(20-A)I/5||_F^2. Put Rp=sum_C r_c, Rq=sum_C s_c, h=sum_C u_c v_c.

The universal frame identity is

Q_all = 30-3A+A^2/10-U/2+V/2.

The six exceptional core pairs have squared energy

Q_6=(Rp^2+Rq^2-sum_C t_c^2)/2+h^2.

All isolated vectors satisfy x_i y_i=0, so T_pq=h and V=2h^2+V_rest with V_rest>=0. Subtraction gives the EXACT safe-only identity

Q_safe = 30-3A+A^2/10-U/2
         -(Rp^2+Rq^2-sum_C t_c^2)/2+V_rest/2.

The sign-sensitive h^2 term cancels. The missing-plane variance alone therefore cannot select among the eight signs; signed F3/Walsh endpoint constraints or the remaining variance components must enter.

## Verification, scope, next target

An exact SymPy synthetic rational example verifies rank 13, safe rank 2, the complete-bipartite minors, reconstruction, eight sign completions, and the exact frame cancellation with h nonzero. The example is NOT a Type-E kissing configuration.

**OPEN:** impose the six F3 signed endpoint constraints on the eight reconstructed sign patterns under a common labeling and combine with the 184 safe blocks. No Type-E contradiction. Preserve M(F3)<=89, M(P)>=S/2-28/3, 20-edge mass >=2137/6, A<=383/504, the Musin/Boyvalenkov zero-midpoint theorem, and the conditional sparse classification requiring delta(G)>=1. Types C,D,E, generic e>=27 and non-isolated branches remain open.
