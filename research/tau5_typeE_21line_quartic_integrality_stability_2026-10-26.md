# Quantitative 21-line quartic integrality gap (2026-10-26)

**Status:** [PROVED EXACTLY] universal 21-line quartic defect gap and 21-line boundary exclusion. [CONDITIONAL ON RETAINED TYPE-E HYPOTHESES] positive Type-E midpoint energy floor. [OPEN] Type E exclusion and tau_5.

## The 21-line boundary argument [PROVED EXACTLY]

For unit vectors in R^5 let f(t)=t^4-t^2/4. With Gegenbauer parameter 3/2, C_0=1, C_2=(15t^2-3)/2, C_4=(315t^4-210t^2+15)/8, the exact positive-definite expansion is

f(t)=(1/28)C_0(t)+(1/18)C_2(t)+(8/315)C_4(t).

Since f(t)<=0 for |t|<=1/2 and f(1)=3/4, the addition theorem yields N^2/28 <= 3N/4, hence N<=21. If N=21, equality implies each off-diagonal squared inner product is 0 or 1/4 and the degree-two moment vanishes. Therefore the frame F=sum_i u_i u_i^T equals (21/5)I. For each i, if d_i counts its 1/4 squared correlations, then 21/5=u_i^T F u_i=1+d_i/4, forcing d_i=64/5, impossible for an integer. Thus N<=20. This is a self-contained independent proof of the projective 20-line bound, consistent with the previously source-audited Musin/Boyvalenkov result; no uniqueness of D5 is assumed.

## Quantitative stability [PROVED EXACTLY]

For ANY 21 unit vectors u_0,...,u_20 in R^5, set s_ij=(u_i.u_j)^2, f_ij=s_ij(s_ij-1/4), P=sum_{i<j}(f_ij)_+, Nminus=sum_{i<j}(-f_ij)_+, F=sum_i u_i u_i^T, and V=||F-(21/5)I||_F^2.

The exact harmonic identity and positive-semidefiniteness of the degree-four kernel give

P-Nminus=(5/24)V+(4/315)sum_{i,j}C_4(u_i.u_j) >= (5/24)V.

Thus Nminus<=P and V<=(24/5)P. Round each s_ij to r_ij=0 when s_ij<=1/8 and r_ij=1/4 otherwise. The elementary inequalities |s-r|<=8(-f) when f<=0 and |s-r|<=4f when f>0 give sum_{i<j}|s_ij-r_ij|<=8Nminus+4P<=12P.

Let d_i=4sum_{j!=i}r_ij, an integer. Since |21/5-(1+d_i/4)|>=1/20 for every i,

21/20 <= sum_i |u_i^T(F-(21/5)I)u_i| + 2sum_{i<j}|s_ij-r_ij|.

Writing Delta=F-(21/5)I and using Cauchy-Schwarz,

sum_i |u_i^T Delta u_i| <= sqrt(21 tr(Delta^2 F)) <= sqrt(21(21/5+sqrt(V))V).

Hence

1/20 <= (24/21)P + sqrt(((21/5+sqrt(V))V)/21),  with V<=(24/5)P.

If P<=1/440, then V<=3/275 and sqrt(V)<21/200, because (21/200)^2-3/275=51/440000>0. The right side is at most 1/385+sqrt(123/55000), strictly less than 1/20 since

(1/20-1/385)^2 - 123/55000 = 631/59290000 > 0.

Therefore the universal **strict exact stability gap** is

P > 1/440.

## Type E conversion [CONDITIONAL ON RETAINED TYPE-E HYPOTHESES]

Let x_0 be the isolated center, and p_i^+/-=m_i+/-z_i be the 20 selected deep edges, with a_i=||m_i||^2<=1/4, ||z_i||^2=1-a_i, A=sum_i a_i<=383/504. Apply the universal gap to 21 unit vectors u_0=x_0 and u_i=z_i/sqrt(1-a_i). Their 210 pairs split into 184 graph-safe edge pairs, 20 center-edge pairs, and six core/core pairs.

For a safe pair |z_i.z_j|<=1/2, so its positive f-defect is <=(1-w)/(16w^2)<=(16/81)(a_i+a_j), where w=(1-a_i)(1-a_j)>=9/16. For a center-edge pair, |x_0.z_i|<=1/2 by both endpoint bounds, giving defect <=a_i/9. For a core pair, the endpoint upper bound gives |z_i.z_j|<=1/2+sqrt(a_i a_j). Set t=sqrt(a_i a_j), u=a_i+a_j<=1/2, w=(1-a_i)(1-a_j)>=9/16. As normalized squared correlation s<=1,

(f(s))_+ <= (s-1/4)_+ <= [t+u/4+3t^2/4]/w <= (3/2)u,

using t<=u/2 and t^2<=u/8.

Write A_O for the sixteen outside midpoint energies and A_C for the four core energies. Pair-incidence counts yield

P <= (16/81)(19 A_O+16 A_C)+(A_O+A_C)/9+(9/2)A_C
  = (313/81)A_O+(1259/162)A_C <= (1259/162)A.

Consequently, **A>81/276980 = 0.000292439887...**. This is a rigorously explicit, but very weak, positive midpoint-energy lower bound. It is far below 383/504 and does not eliminate Type E.

**Next target [OPEN]:** Improve the conversion from midpoint energy to quartic positive defect, especially the six core pairs, and exploit the positive degree-four harmonic remainder. The retained global working range remains 40<=tau_5<=44. No old F3<=94 or matching S/2-343/32 statements are used.