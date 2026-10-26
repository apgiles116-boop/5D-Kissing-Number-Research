# Type E: exact degree-four harmonic balance and sharp scalar deficit (2026-10-26)

**Status:** [PROVED EXACTLY] the harmonic PSD kernel, balance identity, and scalar bound. [CONDITIONAL ON RETAINED TYPE-E ENDPOINT HYPOTHESES] the nonnegative endpoint slack and six-exception inequality. [OPEN] Type E exclusion and the value of tau_5.

Let y_0=x be the unit isolated center, y_i=z_i (1<=i<=20), r_i=||y_i||^2, r_0=1, r_i=1-a_i, 0<=a_i<=1/4, A=sum a_i<=383/504. Define R=sum r_i=21-A, B=sum r_i^2, C=sum r_i^4, t_ij=y_i.y_j, S=sum_{i<j}t_ij^2, T4=sum_{i<j}t_ij^4, W=sum_{i<j}r_i*r_j*t_ij^2, D=S-W, F=sum y_i*y_i^T, V=||F-(R/5)I||_F^2. Write A_k=sum_{i=1}^{20}a_i^k.

For the retained 184 safe edge-edge pairs let M=m_i.m_j, Z=z_i.z_j, X=m_i.z_j, Y=z_i.m_j; for 20 safe center-edge pairs let b_i=|x.m_i| and t_i=x.z_i. Define

    J=sum_safe Z^2*(M^2+X^2+Y^2)+sum_center t_i^2*(b_i-b_i^2),
    E4=sum_six_core [Z^4-Z^2/4]_+.

Define endpoint slack

    eps=sum_safe Z^2*(1/4-M^2-Z^2-X^2-Y^2)
        +sum_center t_i^2*((1/2-b_i)^2-t_i^2)
        +sum_six_core [Z^2*(1/4-Z^2)]_+.

Under the retained endpoint constraints every summand in eps and J is nonnegative: the four safe endpoint dots lie in [-1/2,1/2], so M^2+Z^2+X^2+Y^2<=1/4; and |t_i|+b_i<=1/2. Exactly,

    eps=S/4-J+E4-T4.                                         (1)

**[PROVED EXACTLY] Homogeneous harmonic positivity.** In dimension five

    h4(y,z)=[21(y.z)^4-14||y||^2||z||^2(y.z)^2
             +||y||^4||z||^4]/8

is the degree-four spherical-harmonic reproducing kernel (up to positive scale). Thus H=sum_{i,j}h4(y_i,y_j)>=0. Expansion gives

    8H=7C+42T4-28W+B^2.                                    (2)

The frame-trace identity is S=(R^2/5-B+V)/2. Combining it with (1)-(2) yields the **exact balance identity**

    (5/24)V+J+Hdef(a)+eps+(4/21)H=(2/3)D+E4,               (3)

where

    Hdef(a)=(4/3)A-(53/24)A_2+(2/3)A_3-(1/6)A_4
            -(3/56)A^2+(2/21)A*A_2-(1/42)A_2^2.           (4)

**[PROVED EXACTLY] Sharp scalar bound.** For 0<=a_i<=1/4 and A<=383/504,

    Hdef(a)>=(51/64)A.                                      (5)

The constant is sharp for the *closed scalar domain*: a_1=a_2=a_3=1/4, all others zero, A=3/4. To prove (5), write Hdef=sum h(a_i)-3A^2/56+A_2(4A-A_2)/42 with h(t)=4t/3-53t^2/24+2t^3/3-t^4/6. At fixed A the Hessian is negative definite: h''(t)=-53/12+4t-2t^2<=-41/12 and the other term contributes at most 4A/21<1 in the positive direction. Thus the minimum is attained with k=floor(4A) entries 1/4, one entry A-k/4, all others zero. For k=0,1,2,3 the resulting polynomial p_k(A)=Hdef-51A/64 has negative second derivative on its interval. Its endpoint values are respectively (0,1/256), (1/256,1/256), (1/256,0), and (0,759861745/169375836672) on [0,1/4], [1/4,1/2], [1/2,3/4], [3/4,383/504]. Concavity proves p_k>=0. For A>0, equality in (5) requires the scalar boundary pattern above, excluded exactly by strict deep-edge a_i<1/4; equality also holds trivially at A=0, which is independently excluded by the retained 21-line boundary theorem.

**[CONDITIONAL ON TYPE E]** Nonnegativity in (3) gives

    (5/24)V+J+eps+(4/21)H+(51/64)A<=(2/3)D+E4.           (6)

Equivalently,

    D+(3/2)E4 >= (5/16)V+(3/2)J+(3/2)eps+(2/7)H
                  +(153/128)A.                            (7)

With the retained four-core bound E4<=p(A_C)=A_C/4+5A_C^2/16+A_C^3/4+A_C^4/16, one gets

    D+(3/2)p(A_C)>=(5/16)V+(153/128)A.                    (8)

This translates harmonic/frame coercivity into the six-exception weighted squared-correlation deficit D without any D5 labeling. It is **complementary**, not uniformly stronger than, the earlier Q-rank inequality: the coefficient of V increases from 3/40 to 5/24, but the coefficient of D increases from 2/5 to 2/3.

**[OPEN]** No contradiction with 1/99<A<=383/504 has been obtained. Need a joint upper bound on D and lower control of J+eps+H. Global proved range remains 40<=tau_5<=44. Types C,D, generic e>=27, and non-isolated branches remain open. Retain M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass>=2137/6; sparse e=23,24 classification requires delta(G)>=1.
