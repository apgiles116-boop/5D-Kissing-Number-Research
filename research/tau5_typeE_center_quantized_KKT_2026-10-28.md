# Type E: isolated-center contact quantization and a two-variable exact KKT bound (2026-10-28)

**[NEW, EXACT — CONDITIONAL TYPE E]** Combining the retained isolated-center harmonic row with the exact capped-simplex quantization of its 40 nondeep contacts yields a sharp two-branch constraint. It improves the conditional projected squared-correlation floor from **28.3885724064515...** to **28.3891777096865...**. The numerical gain is small, but the high-center branch now has a strong near-integrality restriction on **all 794 nondeep contacts**.

**[OPEN]** This does not exclude Type E or change the global proved range **40 <= tau_5 <= 44**.

## 1. Inputs and notation

Assume a hypothetical 41-code with isolated center unit vector v, Type-E graph H=16K2+F3, and a selected matching of twenty deep edges m_i +/- z_i. Retain the audited F3 broom/matching mass certificates and the isolated-center harmonic identity from the previous notes.

Write a_i=||m_i||^2, x=sum_{16 isolated edges}a_i, A=sum_{20}a_i, U=sum a_i^2, B_v=sum_i(v.m_i)^2, and

    D(t)=196t-644t^2+896t^3-448t^4,
    B=2595/256, r=D^{-1}(15-B),
    c(x)=D^{-1}(43/3-(B+D(x))/2),
    a(x)=1/2+x+c(x), u(x)=1/8+x^2+c(x)^2.

The retained scalar certificates imply 0<=x<=r, A<=a(x), U<=u(x). All inverses refer to the increasing branch of D on [0,1/4].

Let s=sum_{w != v}(v.w)^2 over the forty center contacts, N0=sum_center 7t^2(1-4t^2), N=sum_all_non-deep 7t^2(1-4t^2), and E=(35/6)||T||_F^2+14K4. The retained exact mass identity and F3 broom bound imply

    D_I+N+E<=15, with D_I>=D(x).                         (1)

The exact center harmonic row, degree-2 trace-free Cauchy, and degree-4 kernel Cauchy give for s>=7

    E >= 175/24*(s-36/5)^2
       +147/4*(5/7+5/12*(s-36/5)+N0/28)^2.            (2)

No D5 labeling is assumed.

## 2. New exact center quantization polynomial

The previous directional-frame argument gives s<=32/5+(8/5)*sqrt((5-D(x))/35)<7.005. Thus, in the branch s>=7, write s=7+d with 0<=d<1/100. Convex maximization of the fourth moment of forty t_j^2 in [0,1/4] gives

    N0>=n(d)=7*d*(1-4*d).

For s>=7, the right side of (2) increases with N0. Substitute N0=n(d) into (2), add n(d), and simplify EXACTLY:

    E+N0 >= 955/64+g(d),
    g(d)=7/4*d*(d+1)*(21*d^2-49*d+20).               (3)

Let R=N-N0>=0. From (1) and (3):

    BOX: D(x)+g(d)+R <= 5/64.                         (4)

In particular, if s>=7,

    x<=xc:=D^{-1}(5/64)=0.0003991200520124...,
    N<=5/64, and d<=d*,

where d* is the unique root of g(d*)=5/64 on [0,1/100]:

    d*=0.0022394303741077... .

Thus the sixteen isolated deep-edge midpoints have total energy <0.0004 in the high-center branch, versus the general Type-E ceiling x<0.028. Also, since a'(x)>0 on [0,xc],

    A<=1/2+xc+c(xc)=0.55728513875954... .            (5)

**[EXACT NEAR-INTEGRALITY COROLLARY]** For rho(t)=min(|t|,1/2-|t|), the pointwise inequality 7t^2(1-4t^2)>=(21/4)rho(t)^2 implies

    sum_{794 nondeep pairs}rho(t)^2<=5/336.

At most **five** of these 794 scalar products can have rho(t)>=1/20: six would already contribute 6*(21/4)*(1/20)^2=63/800>5/64. This is a quantitative *necessary* near-integrality condition, not an exact discrete classification.

## 3. Two-variable frame/KKT inequality

Let F_z=sum z_i z_i^T, V_z=||F_z-(20-A)I/5||_F^2. The exact projected frame identity is

    Q:=sum_{i<j}(z_i.z_j)^2
      =30-3A+A^2/10-U/2+V_z/2.

The center row gives

    v^T(F_z-(20-A)I/5)v=s/2-B_v-4+A/5.

Trace-free Cauchy therefore implies, whenever h=4-a(x)/5-s/2>0,

    Q >= F(x,s)+(5/4)*h*B_v+(5/8)*B_v^2,            (6)

    F(x,s)=30-3a(x)+a(x)^2/10-u(x)/2
           +(5/8)*(4-a(x)/5-s/2)^2.

All the quantities here are bounded using the *joint* a(x),u(x) scalar envelope, not their separate maxima.

**Branch s<=7.** Put xc=D^{-1}(5/64). For 0<=x<=xc, F(x,7) decreases with x. For x>=xc, the previous exact directional-frame bound has s<=smax(x)<=7 and its one-variable lower envelope L(x) is strictly increasing (the audited derivative certificate gives L'(x)>27/56). Hence

    Q>=L_low:=F(xc,7)=28.3894366929011... .          (7)

**Branch s>=7.** Put d=s-7. By (4), D(x)+g(d)<=5/64. Set Fhat(x,d)=F(x,7+d). It decreases in both variables. The exact derivative certificates on 0<=x<=xc, 0<=d<=d* are:

    7/125<c(x)<29/500, 195<D'(x)<=196,
    129<D'(c(x))<133,
    1/5<a'(x)<3/10, |u'(x)|<1/10,
    -19/20<Fhat_x<0,
    -Fhat_d=(5/8)*(1/2-a(x)/5-d/2)>15/64,
    0<g'(d)<=35.

Consequently

    (-Fhat_x)/D'(x)<19/3900<3/448<(-Fhat_d)/g'(d).

On each level set D(x)+g(d)=constant, the derivative of Fhat with respect to x is strictly positive. Moving the available mass budget from x to d decreases Fhat. The minimum is therefore at x=0, d=d*. Thus

    Q>=L_high:=F(0,7+d*)=28.3891777096865525... .   (8)

The exact rational brackets

    399/10^6<xc<400/10^6,
    57184/10^6<c(0)<57185/10^6,
    56886/10^6<c(xc)<56887/10^6,
    2239/10^6<d*<2240/10^6

certify L_low>28.3894>L_high, and 28.3891<L_high<28.3892, with no reliance on floating-point optimization.

**[NEW EXACT CONDITIONAL TYPE-E FLOOR]**

    BOX: sum_{i<j}(z_i.z_j)^2 >= L_high
         = 28.3891777096865525... .                  (9)

For the previously retained six-core squared-correlation caps, this improves the 184-safe-pair floors to

    P1/P3: Q_R >= L_high-473/256 = 26.54152145968655...,
    P2:    Q_R >= L_high-57/32   = 26.60792770968655... .

These safe-pair corollaries remain conditional on the earlier F3 endpoint lemmas. They are not contradictions.

## 4. Status and next target

**[PROVED EXACTLY — CONDITIONAL TYPE E]** Equations (3)-(9), conditional on the retained mass, harmonic, F3, and prior directional derivative certificates. The polynomial and rational comparisons are independently checked in the companion Fraction/SymPy verifier.

**[NOT PROVED]** Type-E exclusion, D5 labeling/uniqueness, a six-exception-to-Q-kernel identification, or a stronger global bound on tau_5.

**[OPEN]** In the high-center branch, use the extremely small N<=5/64 to turn near-integral nondeep contacts into a finite rank-five contact-pattern obstruction. In the low-center branch, retain the directional frame variance and 184 safe-pair Walsh residuals.

Global proved range remains **40<=tau_5<=44**. Type C, Type D, generic e>=27, non-isolated branches and sparse classification without delta(G)>=1 remain open.
