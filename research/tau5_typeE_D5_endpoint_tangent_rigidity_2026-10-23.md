# Type E / D5: endpoint tangent rigidity despite six exceptional core pairs

2026-10-23. **[PROVED EXACTLY, conditional local geometric theorem]** Full endpoint constraints restore first-order rigidity at the zero-midpoint D5 boundary even when up to six pairings inside four fixed core indices are not two-sided safe. **[PROVED — nonquantitative]** The D5 orbit is locally isolated in that restricted feasible set. **[NEGATIVE EXACT RESULT]** Deleting the six corresponding *projective* D5 contact inequalities can destroy one-sided infinitesimal rigidity. **[OPEN]** Global Type-E exclusion, D5 labeling/proximity, and tau_5=40. The proved range remains 40<=tau_5<=44.

## Exact D5 positive stress and rank

Let v_ab^±=e_a±e_b, w_i=v_i/sqrt(2), for 1<=a<b<=5. There are 20 lines and 120 contact pairs E={ij:|v_i.v_j|=1}, each vertex having 12 neighbors. Write s_ij=v_i.v_j=±1. The exact equilibrium equation is

    sum_{j~i} s_ij v_j = 6 v_i.                    (1)

For tangent velocities u_i.v_i=0, put D_ij=s_ij(u_i.v_j+v_i.u_j). If D_ij<=0 on every contact, then summing over E gives sum D_ij=6 sum u_i.v_i=0, so all 120 derivatives vanish. The 120 integer contact rows and 20 tangency rows form a 140x100 matrix of **exact rank 90**. The verifier obtains rank 90 modulo 3 and 101, proving rational rank >=90; ten independent skew-rotation velocities give real rank <=90. Therefore

    D_ij<=0 for all E, u_i.v_i=0
       => u_i=Omega v_i for a single skew Omega.   (2)

## Deleted-K4 counterexample [PROVED EXACTLY]

Select the four lines v_j=e_1+e_j for j=2,3,4,5, forming a contact K4. Delete their six mutual contact inequalities. Put u_j=(e_1+e_2+e_3+e_4+e_5)-2e_j on these four lines and u_i=0 on the other 16. This is tangent and **not** rotational. Direct exact enumeration yields signed derivatives D_ij=+4 on all six deleted edges, -2 on twelve retained edges, and 0 on the remaining 102 retained edges. Thus all 114 retained projective inequalities are satisfied to first order, although the six deleted contacts open. Even after deletion, the equality matrix still has rank 90. **Equality rank alone does not imply one-sided rigidity.** A universal six-deletion projective rigidity assertion is false.

## Full endpoint first-order theorem [PROVED EXACTLY under hypotheses]

Let x_i^±(t)=m_i(t)±z_i(t) be C^1 unit endpoint pairs, with all cross endpoint upper inner products <=1/2. Suppose m_i(0)=0 and z_i(0)=w_i after labeling/orientation/rotation. Fix four core indices J. Every pairing not entirely within J is *safe*: all four cross endpoint inner products lie in [-1/2,1/2]. No lower bound is required for the six core-core pairings.

**Theorem:** z_i'(0)=Omega w_i for one skew Omega, and m_i'(0)=0 for all i.

**Projective part.** Unit endpoint norms give w_i.z_i'(0)=w_i.m_i'(0)=0. For *every* pair, including exceptions, the upper endpoint inequalities imply

    m_i.m_j + |z_i.z_j| <= 1/2.                 (3)

At a D5 contact |z_i(0).z_j(0)|=1/2 and m_i(t).m_j(t)=O(t^2), so its signed projective derivative is <=0. All 120 contact derivatives are constrained, not merely the safe ones. Equation (2) forces z_i'(0)=Omega w_i.

**Midpoint part.** At each safe pairing set a=m_i.m_j, b=z_i.m_j, c=m_i.z_j, d=z_i.z_j. The four two-sided endpoint inequalities imply

    b^2+c^2 <= (1/2-|d|)^2+a^2
             <= 2(1/2-|d|)^2.                (4)

At a safe D5 contact, the rotation-only projective derivative gives |d(t)|=1/2+o(t), and a(t)=O(t^2). Hence b(t),c(t)=o(t), so w_j.m_i'(0)=0 for every safe D5 neighbor j of i. Each vertex has at least nine such neighbors, because only its at most three other core indices can be exceptions. The retained-neighbor projectors span R^5: an exhaustive exact rational certificate for the 220 possible three-neighbor deletions proves

    sum_{j~i, ij safe} w_j w_j^T > (3/8) I_5. (5)

Thus m_i'(0)=0 for all i.

## Nonquantitative local isolation [PROVED]

There exists some epsilon>0 such that any feasible configuration under these fixed-four-core safety hypotheses with

    min_{R in O(5)} (sum_i ||z_i-Rw_i||^2+sum_i ||m_i||^2) < epsilon^2

is exactly m_i=0, z_i=Rw_i. Otherwise take a sequence of distinct feasible configurations approaching the D5 orbit, align optimally, divide all deviations by their combined nonzero norm, and extract a nonzero normalized limiting tangent. The endpoint constraints imply the same first-order inequalities as above (midpoint products are quadratic). Thus the limit is (u_i,p_i)=(Omega w_i,0). Optimal alignment makes u orthogonal to all rotational velocities, so u=0, contradiction. No differentiable curve assumption is needed. This establishes existence of a radius, **not an explicit numerical radius**.

## Status and next target

- **[PROVED EXACTLY]** Signed stress (1), full contact+tangency rank 90, deleted-K4 flex, safe-contact quadratic inequality (4), 220-case safe-neighbor spanning, and full endpoint first-order rigidity.
- **[PROVED, NONQUANTITATIVE]** Restricted D5 local isolation modulo rotations.
- **[CONDITIONAL ON TYPE-E REDUCTIONS]** Twenty selected pairs and the four-core/six-exception safety pattern. This local result does not force a Type-E candidate into the D5 neighborhood.
- **[OPEN]** Type E, C, D, generic e>=27, non-isolated branches, and a global D5 proximity theorem. Sparse e=23/e=24 classification still requires delta(G)>=1.
- **[RETAINED]** M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504; 40<=tau_5<=44.

The companion exact verifier checks all twenty stress equations, rank 90 over two finite fields, 220 rational Sylvester tests, and the deleted-K4 flex. The endpoint and local-isolation deductions are analytic proofs, not numerical extrapolations.
