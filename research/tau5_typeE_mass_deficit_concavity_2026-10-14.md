# Type E: mass-deficit concavity improves the midpoint-energy ceiling (2026-10-14)

**Status: PROVED EXACTLY CONDITIONAL ON THE RETAINED TYPE-E MASS/GRAPH LEMMAS.** This is not a proof of tau_5=40, nor an exclusion of Type E. The inherited global range remains 40 <= tau_5 <= 44.

## Theorem

For Type E H=16 K2 disjoint_union F3, choose the F3 perfect matching P guaranteed by the retained matching-mass theorem. Let A_I be the sum of squared midpoint norms on the 16 isolated K2 edges and A_C the corresponding sum on the four matched F3 edges. Then

    A_I <= r = (1-sqrt((7+sqrt(721))/56))/2 < 0.111256,
    A_C < 0.603545,
    A=A_I+A_C < 651038/1000000 = 0.651038.

This improves the retained A<=383/504~0.759920635. A sharper implicit ceiling is

    A <= 1/2 + r + s1 = 0.6510370130904346...,

where s1 is the unique root in [0,1/4] of D(s1)=41/6.

## Exact proof

For a deep edge with unit endpoints x^+,x^- set a=||(x^++x^-)/2||^2=(1+x^+·x^-)/2 in [0,1/4). The retained Delsarte polynomial F(t)=7t^2(4t^2-1) has F(-1)=21. Define

    D(a)=21-F(2a-1)=196a-644a^2+896a^3-448a^4.

D is strictly increasing and strictly concave on [0,1/4], since D'(1/4)=14>0 and D''(a)=-56(96a^2-96a+23)<0. Also D(0)=0, D(1/4)=21, hence D(a)>=84a.

Let S=M(F3)<=89. The retained total deep mass is >=410, so

    410 <= (336 - sum_I D(a_i)) + S,
    sum_I D(a_i) <= S-74 <=15.

Thus A_I<=15/84=5/28<1/4. Concavity and D(0)=0 imply subadditivity for sums <=1/4, so D(A_I)<=sum_I D(a_i)<=15. Hence A_I<=r=D^{-1}(15), and S>=74+D(A_I).

The inherited F3 matching theorem M(P)>=S/2-28/3, together with M(P)=84-sum_C D(a_i), yields

    sum_C D(a_i) + (1/2)sum_I D(a_i) <=169/3.

By concavity, the minimum sum_C D(a_i) for fixed A_C is attained by filling entries to 1/4, with at most one fractional entry. Thus A_C<3/4 (otherwise the core deficit is >=63>169/3). For A_C>1/2,

    sum_C D(a_i)>=42+D(A_C-1/2),
    D(A_C-1/2)<=43/3-D(A_I)/2.

Let s(x)=D^{-1}(43/3-D(x)/2), 0<=x<=r. Since D^{-1} is increasing convex and its argument is convex, s and B(x)=1/2+x+s(x) are convex. Therefore B(x) attains its maximum at an endpoint of [0,r]. The endpoint values are B(0)=1/2+s0<0.604 and B(r)=1/2+r+s1, where s0=D^{-1}(43/3) and s1=D^{-1}(41/6). The latter is larger. If A_C<=1/2, A<=1/2+r<0.612, so the same ceiling holds.

Exact rational root brackets:

    D(111256/1000000)>15,
    D(103545/1000000)>43/3,
    D(39782/1000000)>41/6.

Therefore A<1/2+111256/1000000+39782/1000000=651038/1000000. The inverse roots have exact radical expressions because F(t) is quadratic in t^2:

    s0=(1-sqrt((7+sqrt(2387/3))/56))/2,
    s1=(1-sqrt((7+sqrt(4907/3))/56))/2.

## Status and next step

**NEW EXACT CONSEQUENCES:** A_I<=r, A_C<0.603545, A<0.651038, S>=74+D(A_I), M(P)>=83/3+D(A_I)/2. In particular each of the 16 isolated deep edges has endpoint inner product < -0.777488.

**RETAINED, NOT REPROVED:** total mass >=410, F3 broom mass S<=89, matching M(P)>=S/2-28/3, and graph classification. Do not regress to F3<=94 or matching loss 343/32.

**OPEN:** Type E exclusion, C/D, generic e>=27, minimum-degree dependency, D5 reconstruction. Next: combine this substantially smaller A ceiling with the six-exception/Q-frame obstruction. No numerical SDP or D5 alignment assumption is used in this proof.
