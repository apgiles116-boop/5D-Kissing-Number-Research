# Type E: label-free isolated-center fourth-moment gap (2026-10-27)

**Status:** [PROVED EXACTLY, conditional on the retained isolated-center Type-E hypotheses]. Does not eliminate Type E. Global range remains 40 <= tau_5 <= 44.

For twenty selected deep edges write endpoints m_i ± z_i, a_i=||m_i||^2, and u_i=z_i/sqrt(1-a_i). The isolated center x_0 has both endpoint inner products in [-1/2,1/2], hence
|x_0·m_i|+|x_0·z_i| <= 1/2.
The deep-edge condition gives 0<=a_i<=1/4; the retained mass theorem gives A=sum a_i<=383/504. Therefore

T_U(x_0):=sum_i (x_0·u_i)^4 <= (1/16)sum_i (1-a_i)^(-2).

Since (1-a)^(-2) is increasing and convex on [0,1/4], the maximum under the sum constraint is at three a_i=1/4, one a_i=5/504, and sixteen zeros. Thus the **label-free exact quartic cap** is

T_U(x_0) <= (16+3*(4/3)^2+(504/499)^2)/16
          = 1043632/747003 = 1.39709211341855...

A useful endpoint-mixing correction is
T_U(x_0) <= 1043632/747003 - (1/8)sum_i |x_0·m_i|/(1-a_i)^2,
using (1/2-t)^4 <= 1/16-t/8 for 0<=t<=1/2.

For the twenty D5 projective roots d_ij^±=(e_i±e_j)/sqrt(2), every unit x satisfies
T_D(x)=sum_(i<j,±)(x·d_ij^±)^4
      = 3/2+(1/2)sum_j x_j^4 >= 8/5.

Consequently, for **every** rotation, relabeling and sign choice of a D5 template,

sup_(||x||=1)|T_U(x)-T_D(x)|
  >= T_D(x_0)-T_U(x_0)
  >= 8/5-1043632/747003
   = 757864/3735015 > 0.2029078865.

This is a rotation/permutation-invariant quartic-operator separation; it does not require a matching between the twenty lines.

**[PROVED EXACTLY, conditional Type E] Sharpened projective Q displacement.**
For any proposed matching of u_i to D5 lines d_i, put theta_i=arccos|u_i·d_i|. The rank-one projector identity gives
|(x_0·u_i)^2-(x_0·d_i)^2| <= sin(theta_i).
The exact D5 quartic-excess inequality is
sum_i [((x·d_i)^2-c)_+]^2 >= 10*(2/5-c)^2, 0<=c<=2/5.
A self-contained polynomial certificate is
(y-c)_+^2 >= (1-25c^2/4)y^2+c(5c-2)y;
for y>=c the difference is c^2(5y-2)^2/4, while for 0<=y<=c the quadratic minorant is nonpositive. Sum using sum_i(x·d_i)^2=4 and sum_i(x·d_i)^4>=8/5. At c=1/4 this gives 9/40.

As (x_0·u_i)^2<=1/[4(1-a_i)], Minkowski gives
sqrt(sum_i sin^2(theta_i))
  >= 3/sqrt(40) - sqrt(sum_i [a_i/(4(1-a_i))]^2).
The summand is increasing and convex. The same exact vertex allocation yields
sum_i [a_i/(4(1-a_i))]^2
 <= 3*(1/12)^2+(5/1996)^2 = 62269/2988012.
Hence

sum_i sin^2(theta_i)
 >= (3/sqrt(40)-sqrt(62269/2988012))^2
 ~= 0.10888834858344,
sum_i ||Q(u_i)-Q(d_i)||_F^2 >= 0.21777669716688,
and some theta_i >= 4.23148893 degrees.

**[OPEN]** To eliminate Type E without assuming D5 labeling, seek a uniform lower bound min_(||x||=1) T_U(x) > 1043632/747003 from the six-exception constraints and rank-14 Q-Gram identities. The retained squared-correlation floor alone does not imply it. No such lower bound has been proved.

Preserve M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, and the previously established label-free A>1/49. Types C, D, generic e>=27 and non-isolated branches remain open; e=23/e=24 sparse classification assumes delta(G)>=1.
