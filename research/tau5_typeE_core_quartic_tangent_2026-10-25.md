# Type E: rational tangent certificate for the six-core quartic defect

25 October 2026. **[EXACT, CONDITIONAL ON RETAINED TYPE-E INPUTS]** Improved exceptional-core quartic ceiling and Q-rank safe-slack bounds. **[OPEN]** Type E and the global problem.

## Retained inputs (not reproved here)

For the six pairings of the four selected F3 matching edges, put d_ij=(|z_i.z_j|-1/2)_+ and T_C^+=sum(d_ij+d_ij^2)^2. We use:
- D=sum d_ij <= D0=1780062775/4032758016;
- Q=sum d_ij^2 <19/250;
- the F3 quotient patterns [1,1,1,1,1,1] or [0,1,1,1,1,2], with the double-contact and zero-contact pairings opposite; singleton-contact defects are <1/8, and a zero-contact pairing cannot have positive defect;
- adjacent positive defects x,y satisfy P(x,y)=x+y+4(x^2+y^2-xy)-1/2<=0.

Hence at most one defect exceeds 1/8. If one does, call it x: it is double-contact, its opposite defect is zero, and the other four defects y_j are <=1/8 and satisfy P(x,y_j)<=0.

## New exact theorem

**[PROVED UNDER RETAINED SCALAR INPUTS]**
\[
\boxed{T_C^+<11/100.}
\]

Let f(t)=(t+t^2)^2 and k=(1+1/8)^2=81/64. If every defect is <=1/8, T_C^+<=kQ<k(19/250)<11/100.

Otherwise there is a unique x>1/8. The other terms satisfy f(y)<=k y^2, giving
\[
T_C^+<k(19/250)+x^2((1+x)^2-k).
\]
This right side is increasing for x>=1/8, and at x=23/100 equals 43707339/400000000<11/100. Thus only x in [23/100,1/4] remains.

The adjacent lifted-triangle inequality gives y_j<=c(x), where
\[
c(x)=\frac{4x-1+\sqrt{9-24x-48x^2}}8.
\]
The function c is concave, so its tangents are upper bounds. Also
\[
\sum_j f(y_j)\le k\sum_j y_j^2\le k c(x)\sum_j y_j
\le k c(x)(D_0-x).
\]
Three exact rational tangents suffice:

| Tangency x0 | Tangent upper bound c(x)<= | Interval |
|---|---|---|
| 10/43 | (19-70x)/26 | [23/100,59/250] |
| 132/553 | (249-946x)/270 | [59/250,241/1000] |
| 9/37 | (17-66x)/14 | [241/1000,1/4] |

For each tangent alpha+beta*x, the quartic polynomial
\[
p(x)=11/100-x^2(1+x)^2-(81/64)(\alpha+\beta x)(D_0-x)
\]
has five strictly positive degree-four Bernstein coefficients on its stated interval. Their smallest coefficients, in row order, are
\[
1185418965924383/10113012000000000000,\quad
2661142247310257/21003948000000000000,\quad
31845177316137991/43563744000000000000.
\]
The companion pure-Python verifier checks all fifteen coefficients and the rational tangency equations. Hence p(x)>0 and T_C^+<11/100 throughout.

## Consequences for Type E

Retain the independently established universal 20-vector traceless-Q inequality
\[
\sum_{i<j}^{20}(1/4-(z_i\cdot z_j)^2)^2\ge375/896.
\]
The 184 outside-core pairings are raw-safe, and the six core pairings split into safe-core slack H_C^- and positive exceptional contribution T_C^+. Therefore
\[
\boxed{H_{184}+H_C^->375/896-11/100=6911/22400
\approx0.308526785714286.}
\]
This improves the prior 0.295662176 joint floor; it is NOT an unconditional bound on H_184 alone.

The four 19-vector leave-one-core-out inequalities similarly give
\[
\boxed{H_{184}+\tfrac12H_C^->49519/179200+\tfrac14H_{OC}.}
\]
This improves the previous constant 0.269901400 to approximately 0.276333705.

**[SPECIAL BRANCH, CONDITIONAL TYPE E]** If all six core defects are positive, all six are singleton contacts, so H_C^-=0. Since endpoint feasibility gives m_i.m_j<=-d_ij, PSD of ||sum_{i in C}m_i||^2 implies A_C>=2D. Thus D<=A_C/2<=A/2<=383/1008. With six caps d_ij<=1/8, convex concentration gives
\[
Q\le3(1/8)^2+(383/1008-3/8)^2=47653/1016064.
\]
Hence T_C^+<=(81/64)Q<=47653/802816 and
\[
\boxed{H_{184}\ge288347/802816\approx0.359169473453444.}
\]
This branch-specific estimate does not eliminate Type E.

## Status

**[EXACT UNDER RETAINED INPUTS]** Rational tangent/Bernstein certificate, two improved Q-rank tradeoffs, all-six-positive midpoint Gram bound.
**[RETAINED, NOT REPROVED]** D0, Q<19/250, singleton cap, F3 matching quotient, lifted triangle, Q-rank bounds, A<=383/504, M(F3)<=89, matching mass >=S/2-28/3.
**[OPEN]** Type E, Types C/D, generic e>=27, non-isolated cases; sparse e=23/24 classification remains conditional on delta(G)>=1.
**[UNCHANGED]** 40<=tau_5<=44.

Exact verifier: research/tau5_typeE_core_quartic_tangent_2026-10-25_verify.py.
