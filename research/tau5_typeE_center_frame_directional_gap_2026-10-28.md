# Type E: isolated-center directional frame gap (2026-10-28)

**[PROVED EXACTLY — CONDITIONAL TYPE E]** Retaining the isolated-center second moment in the projected 20-vector frame operator improves the earlier global squared-correlation floor from 28.2677055569... to **28.3885724064...**, with two explicit additional stability penalties. The proof uses the already-audited isolated-center harmonic estimate and retained F3 broom/matching certificates; it does not assume a D5 labeling or run a new SDP.

**[OPEN]** The stronger floor does not yet exclude Type E. Global proved range remains 40 <= tau_5 <= 44.

## Definitions and retained inputs

For a hypothetical 41-code with isolated center unit vector v, select the 20 disjoint deep edges m_i +/- z_i of Type E (16 isolated edges I and four F3 matching edges C). Write

- a_i=||m_i||^2, A=sum a_i, U=sum a_i^2;
- x=sum_{i in I} a_i, and B_v=sum_i (v.m_i)^2 >=0;
- D(t)=196t-644t^2+896t^3-448t^4;
- B=2595/256, r=D^{-1}(15-B), c(x)=D^{-1}(43/3-(B+D(x))/2);
- a(x)=1/2+x+c(x), u(x)=1/8+x^2+c(x)^2.

The retained mass-concavity argument proves 0<=x<=r, A<=a(x), U<=u(x). Here D^{-1}(w) denotes its increasing inverse on [0,1/4]. Its exact expression is

D^{-1}(w)=(1-sqrt((7+sqrt(2401-112w))/56))/2.

The 41-code Delsarte identity and F3 broom bound give

D_I+N+E<=15,

where D_I=sum_{i in I}D(a_i)>=D(x), N>=0 is the nondeep Delsarte slack, and E=(35/6)||T||_F^2+14 K_4>=0 is the degree-2/4 harmonic remainder. The isolated-center harmonic estimate gives, for q=sum_{40 center contacts}(v.w)^2-36/5,

E >= 10+(35/64)(5q+4)^2

whenever q>=-12/7. The alternative q<-12/7 forces E>150/7>15 and is impossible under the displayed mass bound.

## 1. New exact directional-frame inequality

Let s=sum_{40 center contacts}(v.w)^2. Since 5q+4=5s-32, the preceding bounds imply

(5s-32)^2 <= (64/35)(5-D(x)),

and therefore

s <= 32/5+(8/5)*sqrt((5-D(x))/35).                         (1)

In particular, the upper center second moment falls from (32+8/sqrt(7))/5 at x=0 to 13/2 at x=r. The latter follows exactly from 5-D(r)=35/256.

Let F_z=sum_i z_i z_i^T and V_z=||F_z-((20-A)/5)I||_F^2. Since the 40 endpoints are m_i +/- z_i,

s=2*sum_i[(v.m_i)^2+(v.z_i)^2],

and hence

v^T(F_z-((20-A)/5)I)v=s/2-B_v-4+A/5.

Define the positive function

b(x)=7/2-x-c(x)-4*sqrt((5-D(x))/35).

Using (1) and A<=a(x) yields

v^T(F_z-((20-A)/5)I)v <= -b(x)/5-B_v.                    (2)

The frame deviation is trace-free. Cauchy-Schwarz against vv^T-I/5, whose Frobenius norm squared is 4/5, gives the **exact directional frame gap**

V_z >= (5/4)*(b(x)/5+B_v)^2.                           (3)

In particular, b(x)>9/5 on [0,r] by the rational root brackets r<3/100, c(x)<=c(0)<3/50, and 4/sqrt(7)<8/5.

## 2. Joint scalar/frame lower bound and monotonicity

The exact Q-frame identity is

sum_{i<j}(z_i.z_j)^2
 = 30-3A+A^2/10-U/2+V_z/2.

Because A<=a(x)<0.57, U<=u(x), and the scalar expression decreases in A, (3) implies

sum_{i<j}(z_i.z_j)^2 >= L(x)+(b(x)/4)B_v+(5/8)B_v^2,   (4)

where

L(x)=30-3a(x)+a(x)^2/10-u(x)/2+b(x)^2/40.

**[PROVED EXACTLY]** L'(x)>27/56 throughout [0,r]. Here is a rational derivative certificate:

- D is strictly increasing and concave on [0,1/4]. Exact root brackets give r<7/250, c(0)<3/50, c(r)>7/250, D'(7/250)>160, and D'(3/50)>128.
- c'(x)=-D'(x)/(2D'(c(x))), so -1<c'(x)<-1/2 and 0<a'(x)=1+c'(x)<1/2.
- For L_base=30-3a+a^2/10-u/2, one has L_base'=(-3+a/5)a'-x-c c'>-3/2-r>-153/100.
- b'=-a'+2D'(x)/sqrt(35*(5-D(x))) > -1/2+320/14=313/14, using sqrt(175)<14. Also b>9/5.
- Consequently L'=L_base'+bb'/20 > -153/100+(9/5)*(313/14)/20 = 27/56.

Thus L(x)>=L(0)+(27/56)x. The **new quantitative Type-E stability inequality** is

BOX:
sum_{i<j}(z_i.z_j)^2
 >= L_0+(27/56)x+(9/20)B_v+(5/8)B_v^2,               (5)

with the exact algebraic constant

L_0=30-3a_0+a_0^2/10-u_0/2+b_0^2/40,
a_0=1/2+c_0, u_0=1/8+c_0^2,
b_0=7/2-c_0-4/sqrt(7),
c_0=D^{-1}(43/3-B/2).

Numerically, L_0=28.3885724064515... . This improves the preceding conditional Q-floor 28.2677055569327... by 0.1208668495189... . The minimum of this **scalar/frame relaxation** occurs at x=0; this does not assert that a Type-E code attains equality.

## 3. 184-safe-pair corollary

Assuming the previously retained F3 endpoint lemmas that bound the six core squared correlations by C_K=473/256 (P1/P3) or 57/32 (P2), the 184 fully safe projected pairings satisfy

sum_{R}(z_i.z_j)^2
 >= 26.5409161564515...+(27/56)x+(9/20)B_v+(5/8)B_v^2  [P1/P3],

sum_{R}(z_i.z_j)^2
 >= 26.6073224064515...+(27/56)x+(9/20)B_v+(5/8)B_v^2  [P2].

The decimals are evaluations of exact algebraic constants. These are necessary conditions, not contradictions with any established safe-pair upper bound.

## Proof-status ledger

**[PROVED EXACTLY — conditional Type E]** (1)-(5) follow from the retained mass/center harmonic certificates, endpoint decomposition, trace-free matrix Cauchy-Schwarz, and rational derivative bounds. The 184-safe corollary additionally depends on the previously retained six-core caps.

**[NOT CLAIMED]** D5 uniqueness, a mapping of six exceptional pairs to six Q-kernel relations, a Type-E exclusion, or tau_5=40.

**[OPEN]** Type E, Types C and D, generic e>=27, non-isolated branches, and sparse e=23/24 classification without delta(G)>=1.

Companion verifier: tau5_typeE_center_frame_directional_gap_2026-10-28_verify.py.
