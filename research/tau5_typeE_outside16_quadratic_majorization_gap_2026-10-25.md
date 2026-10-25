# Type E: quadratic majorization gives an exact outside-16 spectral gap > 1/18

**2026-10-25 — [PROVED EXACTLY UNDER RETAINED TYPE-E INPUTS].** This strengthens the previous >1/31 theorem. Type E and the global range remain OPEN/40 <= tau_5 <= 44.

## Hypotheses

For the 16 outside-core selected deep edges in H=16K2 disjoint-union F3, put a_i=||m_i||^2, b_i=||z_i||^2=1-a_i, with 0<=a_i<=1/4, sum a_i<=B=383/504, and |z_i.z_j|<=1/2 for i!=j. Define Z_O=sum z_i z_i^T in R^5.

**Theorem: Z_O is strictly greater than I_5/18 in the PSD order.**

## Fourth-moment obstruction

On S^3, f(t)=t^4-t^2/4=(1+6P_2(t)+5P_4(t))/16, where P_2=(4t^2-1)/3 and P_4=(16t^4-12t^2+1)/5. Gegenbauer positivity implies for 16 unit vectors u_i in R^4:

    sum_{i!=j} f(u_i.u_j) >= 4.                           (1)

For c_i in [0,1), define

    F(c)=(1/8) sum_{i<j} [(1-c_i)^(-2)(1-c_j)^(-2)
                         -(1-c_i)^(-1)(1-c_j)^(-1)].

If |u_i.u_j|<=1/[2 sqrt((1-c_i)(1-c_j))], then sum_{i!=j} f(u_i.u_j)<=F(c), since f(t)<=f(C) for |t|<=C and C>=1/2.

F is coordinatewise increasing and Schur-convex on [0,1)^16: writing x=(1-a)^(-1), y=(1-b)^(-1), g(a,b)=x^2y^2-xy, one has partial_a g=2x^3y^2-x^2y>0, partial_aa g=2x^3y(3xy-1)>0, and the two-variable derivative difference equals xy(x-y)(2xy-1)>=0 when a>=b. The remaining terms inherit the derivative ordering by convexity. Hence F respects weak majorization.

## Projection and exact effective energy

Assume lambda_min(Z_O)=lambda<=L=1/18. Choose a unit eigenvector w, set s_i=(w.z_i)^2, so sum s_i=lambda. Let y_i=z_i-(w.z_i)w in R^4 and u_i=y_i/sqrt(b_i-s_i), which is well-defined since b_i-s_i>=3/4-L>0.

The raw correlation bound and 2sqrt(s_i s_j)<=s_i+s_j imply

    |u_i.u_j| <= (1+s_i+s_j)/(2sqrt((b_i-s_i)(b_j-s_j)))
               <= (1+s_i)(1+s_j)/(2sqrt((b_i-s_i)(b_j-s_j))).

Set c_i=1-(b_i-s_i)/(1+s_i)^2. Then 0<=c_i<1 and

    |u_i.u_j| <= 1/[2sqrt((1-c_i)(1-c_j))].             (2)

## Quadratic majorization certificate

The exact identity

    (a+(3-2a)s-(7/2)s^2-c(a,s))*(1+s)^2
       = s^2[(3/2-3a)-(4+2a)s-(7/2)s^2]

has nonnegative right-hand side for a in [0,1/4], s in [0,L], because the bracket is at least 317/648. Hence

    c_i <= a_i+(3-2a_i)s_i-(7/2)s_i^2.                  (3)

For a subset I of k indices put T=sum_I s_i<=L, so sum_I s_i^2>=T^2/k. For k<=3, write d_i=1/4-a_i>=0; because s_i<=L<1/2, (3) gives

    sum_I c_i <= k/4+(5/2)T-(7/2)T^2/k
               <= k/4+(5/2)L-(7/2)L^2/k.              (4)

For 4<=k<=16, the total energy bound gives

    sum_I c_i <= B+3T-(7/2)T^2/k
               <= B+3L-(7/2)L^2/16.                   (5)

The scalar quadratics in T are increasing on [0,L]. Consequently c is weakly majorized by the decreasing vector

    v=(245/648, 331/1296, 979/3888, 8845/217728, 0,...,0).

Its first three prefix sums are the bounds (4), and its first four prefix sum equals 67199/72576, the bound (5). Schur-convexity yields F(c)<=F(v). Exact rational arithmetic gives

    F(v)=222154536100028717800410627996
         /55841664360277980735448954225

and

    4-F(v)=1212121341083205141385188904
           /55841664360277980735448954225 >0.       (6)

Equations (1), (2), and (6) contradict lambda<=1/18. Therefore

    **lambda_min(Z_O)>1/18.**

## Weighted safe-slack consequence

Let A_C be midpoint energy on the four core edges, A_O on the sixteen outside edges, A=A_C+A_O>0. Let H_OC and H_OO be the sums of h_ij^2=(1/2-|z_i.z_j|)^2 over outside/core and outside/outside pairings. All 184 such pairings have zero deep cross-contacts, so the retained endpoint theorem gives |m_i.z_j|<=h_ij.

The matrix spectral gap implies H_OC>=lambda_min(Z_O) A_C and 2H_OO>=lambda_min(Z_O) A_O. Therefore, since A>0,

    **H_184=H_OC+H_OO > A_C/18+A_O/36=(A+A_C)/36>=A/36.**

This strengthens the earlier H_184>A/62, without D5 labeling or a full-frame tightness assumption.

## Optional rank-four threshold

The same Schur-convex F argument shows that any 16 vectors with these raw correlation and per-edge energy constraints lying in R^4 must have A_O>=(889-sqrt(413553))/224=1.0978532775... . For A_O<=1, F<=100/27<4. For 1<=A_O<=5/4, the capped maximizer has four 1/4 entries and one residual u=A_O-1, giving F=(752u^2-1063u+800)/(216(1-u)^2); F=4 first occurs at u=(665-sqrt(413553))/224.

## Status

[PROVED EXACTLY UNDER RETAINED TYPE-E INPUTS] Spectral gap >1/18, weighted safe-slack floor, and rank-four energy threshold. [RETAINED, NOT REPROVED] M(F3)<=89; M(P)>=S/2-28/3; twenty-edge mass >=2137/6; A<=383/504; six exceptional core pairings; source-audited zero-midpoint boundary exclusion. [OPEN] Type E, C, D, generic e>=27, non-isolated branches, and any global improvement. Sparse e=23/24 classification remains conditional on delta(G)>=1. Global proved range remains 40<=tau_5<=44.

Exact companion checker: research/tau5_typeE_outside16_quadratic_majorization_gap_2026-10-25_verify.py.
