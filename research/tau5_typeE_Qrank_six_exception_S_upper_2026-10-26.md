# Type E: an exact complementary upper bound on 20-line squared-correlation mass (2026-10-26)

**Status:** [PROVED EXACTLY] Rank-14 fourth-moment inequality and algebraic deductions. [CONDITIONAL ON RETAINED TYPE-E CERTIFICATES] Application to the 184 safe/six exceptional pairing split and collective core defect budgets. [OPEN] Type E exclusion.

## Assumptions

Twenty vectors z_i in R^5 satisfy ||z_i||^2=1-a_i, 0<=a_i<=1/4, A=sum a_i<=383/504. Partition indices into sixteen outside O and four core C. Every pair except six core-core pairs satisfies |z_i.z_j|<=1/2. Put A_C=sum_{i in C}a_i and delta_ij=(|z_i.z_j|-1/2)_+ on core pairs. Retain the endpoint-derived bounds sum delta<=A_C, sum delta^2<=A_C^2/4, and delta<=sqrt(a_i a_j)<=A_C/2.

Write S=sum_{i<j}(z_i.z_j)^2, T=sum_{i<j}(z_i.z_j)^4, r_i=1-a_i, B=sum r_i^2, C4=sum r_i^4, H=sum_{i<j}r_i r_j(z_i.z_j)^2.

## Exact lower fourth moment and row correction

The rank-14 Q-Gram inequality gives
T >= (2/5)H+B^2/350-(3/10)C4.

For outside i, row sum R_i=sum_{j!=i}(z_i.z_j)^2 <=19/4. For core i, at most three pairs exceed 1/2 in absolute value, each by at most A_C/2, so
R_i <=19/4+(3/2)A_C+(3/4)A_C^2.
Consequently sum_{i<j}(a_i+a_j)(z_i.z_j)^2=sum_i a_i R_i <= (19/4)A+(3/2)A_C^2+(3/4)A_C^3.
Since r_i r_j=1-a_i-a_j+a_i a_j,
H >= S-(19/4)A-(3/2)A_C^2-(3/4)A_C^3.

## Six-exception quartic upper bound

For safe pairs, Z^4<=Z^2/4. For a core pair with delta>0, |Z|=1/2+delta and
Z^4-Z^2/4=delta/4+(5/4)delta^2+2delta^3+delta^4.
Using the collective budgets and delta<=A_C/2 yields
T <= S/4+p(A_C), with
p(t)=t/4+5t^2/16+t^3/4+t^4/16.

Combining these inequalities gives the **two-parameter exact upper bound**
(3/20)S <= (19/10)A+(3/5)A_C^2+(3/10)A_C^3+(3/10)C4-B^2/350+p(A_C).

Because C4<=20-4A+6A^2, B>=20-2A, and A_C<=A, we obtain the closed scalar bound
**S <= U(A)=(20/3)[34/7+(33/28)A+(7563/2800)A^2+(11/20)A^3+A^4/16].**
All coefficients are positive, so U increases for A>=0. At A=0, S<=680/21. For A<=1/40,
**S<=66741643/2048000 = 32.58869287109375.**

The retained center-frame result in this low-energy regime gave S>3001691/100000=30.01691. The bounds are compatible: the exact remaining gap is 131675283/51200000. Thus this is a new *complementary upper bound* but **not** a Type-E contradiction.

**Next step [OPEN]:** retain the negative midpoint/mixed endpoint terms in the safe-row upper bound, and optimize the six core fourth moments jointly with the PSD four-core Gram. No improvement to 1/99<A<=383/504 is claimed. Retain M(F3)<=89, matching M(P)>=S/2-28/3, and selected-edge mass >=2137/6. Global proved range 40<=tau_5<=44; Types C,D,generic e>=27 and non-isolated branches remain open.
