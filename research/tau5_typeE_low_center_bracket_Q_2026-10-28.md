# Type E: center lower bracket and residual-branch Q floor (2026-10-28)

**[NEW EXACT ALGEBRA — CONDITIONAL TYPE E]** The retained Type-E mass/harmonic resource implies a new algebraic lower bound on the isolated-center second moment: s >= sigma = 5.827662491235... . Combined with the **previously conditional** near-seven exclusion s >= 209/30, the remaining Type-E center interval is sigma <= s < 209/30. The retained directional-frame inequality then gives a strengthened conditional projected squared-correlation floor Q >= 28.395623511729... . No Type-E branch is eliminated here; global proved range remains 40 <= tau_5 <= 44.

## 1. Exact lower bound on center second moment

For the isolated center v, set s=sum_{w!=v}(v.w)^2 and N0=sum_{w!=v}7t_w^2(1-4t_w^2). Let E=(35/6)||T||_F^2+14K4. Retained harmonic and Type-E mass certificates give

\[
E+N_0\le15,\qquad
E\ge\frac{175}{24}(s-\frac{36}{5})^2+
\frac{147}{4}\left(\frac57+\frac5{12}(s-\frac{36}{5})+\frac{N_0}{28}\right)^2.
\]

The center harmonic estimate without N0 already forces s >= 32/5-8/(5sqrt(7)) > 23/4. For 23/4 <= s <= 6, set u=s-23/4 in [0,1/4]. Capped-simplex fourth-moment maximization gives N0 >= n(u)=7u(1-4u). The harmonic right side plus N0 is increasing in N0 here, so the resource requires P(u)<=0, where

\[
P(u)=\frac{147}{4}u^4-49u^3-\frac{399}{32}u^2-\frac{35}{4}u+\frac{795}{1024}.
\]

Its derivative is

\[
P'(u)=\frac7{16}(336u^3-336u^2-57u-20)<0
\quad(0\le u\le1/4).
\]

The unique root u_* satisfies the exact rational brackets
P(582766/100000-23/4)>0 and P(582767/100000-23/4)<0. Hence s >= sigma=23/4+u_*=5.827662491235...; for s>6 this is automatic. This conclusion does **not** require any signed-Gram atlas.

## 2. Improved Q floor on the conditionally surviving interval

Assume the previously conditional near-seven exclusion s< s0=209/30, including its upstream finite-atlas certificates. Retain

\[
D(x)=196x-644x^2+896x^3-448x^4,\quad B=2595/256,
\]
\[
c(x)=D^{-1}(43/3-(B+D(x))/2),\quad
a(x)=1/2+x+c(x),\quad u(x)=1/8+x^2+c(x)^2,
\]
\[
s_{\max}(x)=32/5+(8/5)\sqrt{(5-D(x))/35}.
\]

The earlier directional frame bound, after dropping nonnegative midpoint-direction terms, reads

\[
Q=\sum_{i<j}(z_i\cdot z_j)^2\ge F(x,s)
=30-3a(x)+a(x)^2/10-u(x)/2+
\frac58(4-a(x)/5-s/2)^2.
\]

Here 0<=x<=r=D^{-1}(15-B) and s<=min(s0,smax(x)). The function F decreases with s. Define x0 by smax(x0)=s0, equivalently

\[
D(x_0)=1405/2304,\qquad x_0=0.00314359889005\ldots .
\]

For x<=x0, F(x,s0) decreases with x. Indeed c'=-D'(x)/(2D'(c)), D'(c)>128, D'(x)<=196, c<3/50, a<3/5, h=4-a/5-s0/2>0 imply a'>15/64 and

\[
\partial_x F(x,s_0)
=a'(-3+a/5-h/4)-x-cc'
<-\frac{72}{25}\frac{15}{64}+\frac3{50}\frac{49}{64}
=-2013/3200<0.
\]

For x>=x0, smax(x)<=s0 and the previously verified L(x)=F(x,smax(x)) satisfies L'(x)>27/56. Thus the scalar/frame relaxation has its minimum at x0:

\[
\boxed{Q\ge Q_*:=F(x_0,209/30)=28.395623511729077\ldots}.
\]

Exact rational brackets give 28.3956<Q_*<28.3957. Under retained six-core squared-correlation caps, the 184-safe pair floors are Q_*-473/256=26.5479672617... (P1/P3) and Q_*-57/32=26.6143735117... (P2).

## Proof status

**[NEW EXACT ALGEBRA, CONDITIONAL]** The lower center bracket uses the retained harmonic/Type-E mass resource. The Q improvement additionally uses the earlier conditional s<209/30 exclusion and directional derivative certificate. The new verifier checks rational arithmetic and monotonicity bounds, **not** upstream geometry or finite-atlas completeness.

**[OPEN]** Type E with sigma<=s<209/30; Types C and D; generic e>=27; non-isolated branches; sparse e=23/24 without delta(G)>=1. Retain M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, and the Musin/Boyvalenkov zero-midpoint exclusion. **Global proved range unchanged: 40<=tau_5<=44.**

Verifier: tau5_typeE_low_center_bracket_Q_2026-10-28_verify.py.
