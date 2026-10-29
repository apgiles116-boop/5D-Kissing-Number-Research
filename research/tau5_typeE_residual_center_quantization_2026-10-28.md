# Type E: residual-center quantization improves the conditional Q-floor

**Date:** 2026-10-28. **Status: [NEW EXACT ALGEBRA — CONDITIONAL TYPE E].** This uses retained Type-E mass and isolated-center harmonic certificates, the earlier conditional exclusion of center moment s >= 209/30 (finite signed-Gram atlases), and the previously verified L'(x)>27/56 certificate. Those upstream results are not independently re-proved here. **[OPEN]** No Type-E exclusion and no improvement to 40 <= tau_5 <= 44.

## Statement and retained inputs

For the twenty selected deep edges u_i^± = m_i ± z_i let A = sum ||m_i||², U = sum ||m_i||⁴, Q = sum_{i<j}(z_i.z_j)², x = sum over the sixteen isolated edges ||m_i||², and s = sum of squared scalar products of the forty contacts with isolated center v. Set N0 = sum_center 7t²(1-4t²).

Write D(x)=196x-644x²+896x³-448x⁴, B=2595/256,
c(x)=D^{-1}(43/3-(B+D(x))/2),
a(x)=1/2+x+c(x), and u(x)=1/8+x²+c(x)².
The retained mass/harmonic certificates imply 0 <= x <= r=D^{-1}(15-B), A <= a(x), U <= u(x), and

\[
D(x)+N_0+10+\frac{35}{64}(5s-32)^2\le15. \tag{1}
\]

The center-directional frame variance inequality gives

\[
Q\ge F(x,s):=30-3a(x)+\frac{a(x)^2}{10}-\frac{u(x)}2+
\frac58\left(4-\frac{a(x)}5-\frac s2\right)^2. \tag{2}
\]

The conditional near-seven exclusion leaves s < s0=209/30. The new exact rational bound is

\[
\boxed{Q>\frac{709911}{25000}=28.39644.} \tag{3}
\]

It strengthens the preceding conditional 28.395623511729... floor by more than 0.00081648. With the *separately retained* six-core squared-correlation caps 473/256 (P1/P3) and 57/32 (P2), the 184-safe-pair consequences are

\[
\boxed{S_{\rm safe}>21239027/800000=26.54878375\quad(P1/P3),}
\]
\[
\boxed{S_{\rm safe}>2661519/100000=26.61519\quad(P2).}
\]

## Center-contact quantization and the new resource threshold

Each isolated-center contact is nondeep, so t_j² in [0,1/4]. Concavity of 7y(1-4y) gives, at fixed s=sum t_j²,

\[
N_0\ge n(s)=7\rho(1-4\rho),\qquad
\rho=s-\lfloor4s\rfloor/4. \tag{4}
\]

For 69/10 <= s <= s0, floor(4s)=27, hence
n(s)=7(s-27/4)(1-4(s-27/4)) and n(s0)=91/450.

The old relaxation minimizer (x0,s0), D(x0)=1405/2304, saturated (1) with N0 discarded. But (4) forces N0>=91/450 at s0, excluding that minimizer. Define x1 by

\[
D(x_1)=15-10-\frac{35}{64}(5s_0-32)^2-n(s_0)
=\frac{23477}{57600}. \tag{5}
\]

D is strictly increasing on [0,1/4], and exact rational evaluation gives x1<2094/10^6 (numerically x1~0.0020938883768744).

## Exact three-region minimization

On 0<=x<=1/250 and 69/10<=s<=s0, the rational bounds
27/500<c(x)<3/50, 190<D'(x)<=196, and
128<D'(c(x))<135 imply

\[
15/64<a'(x)<8/27,\quad 3/8<h<1/2,\quad
-2<F_x(x,s)<0,\quad -F_s=(5/8)h>15/64, \tag{6}
\]
where h=4-a(x)/5-s/2.

**Region I (0<=x<=x1).** F decreases in s; F(x,s0) decreases in x. Thus F(x,s)>=F(x1,s0). With xhi=2094/10^6 and chi=111271/2000000, exact rational checks give x1<xhi, c(xhi)<chi, and

\[
F(x_1,s_0)>F(xhi,\chi,s_0)
=\frac{8178176057733869}{288000000000000}
>\frac{709911}{25000}. \tag{7}
\]
Here F(x,chi,s) means substitution of chi for c(x).

**Region II (x1<=x<=1/250).** If s<=69/10, F(x,s)>=F(1/250,69/10)>709911/25000. Otherwise 69/10<=s<=s0, and (1),(4) imply s<=sq(x), where sq is the unique root in [69/10,s0] of

\[
D(x)+10+\frac{35}{64}(5sq-32)^2+n(sq)=15. \tag{8}
\]

In this strip, 0<E'(s)+n'(s)<16 and D'(x)>190. Implicit differentiation gives -sq'(x)>190/16. Hence

\[
\frac{d}{dx}F(x,sq(x))
=F_x+F_s\,sq'(x)
>-2+\frac{15}{64}\frac{190}{16}>0. \tag{9}
\]

The minimum in Region II is again at (x1,s0).

**Region III (x>=1/250).** Dropping N0 gives s<=smax(x) and Q>=L(x)=F(x,smax(x)). The *retained exact* certificate L'(x)>27/56 implies L(x)>=L(1/250). Exact rational enclosures
c(1/250)<5427/100000 and smax(1/250)<69561/10000 yield
L(1/250)>28.3975901776>709911/25000.
This proves (3) conditional on the stated upstream certificates.

## Additional exact paired-center identity (not used in the floor)

For each selected edge put p_i=v.m_i, q_i=v.z_i, and
s_i=(p_i+q_i)^2+(p_i-q_i)^2=2(p_i²+q_i²).
Direct expansion gives the *exact* identity

\[
\boxed{N_0=7\sum_{i=1}^{20}
\left[s_i(1-2s_i)-16s_ip_i^2+32p_i^4\right].} \tag{10}
\]

Because 0<=s_i<=1/2 and sum s_i=s, let
B_v=sum p_i² and rho2=s-floor(2s)/2. The capped-simplex inequality and Cauchy give

\[
\boxed{N_0\ge7\rho_2(1-2\rho_2)-56B_v+\frac{56}{5}B_v^2.} \tag{11}
\]

This couples center-contact parity/quantization to the *same* B_v that appears with a positive penalty in the frame-variance bound. Joint optimization is **[OPEN]**.

## Strict ledger

**[NEW EXACT, CONDITIONAL]** (3), the three-region rational proof, and the safe-pair corollaries. **[EXACT STANDALONE ALGEBRA]** (10)-(11), assuming the center contacts are nondeep. **[RETAINED, NOT REPROVED]** F3 star/broom/matching mass, M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, harmonic center resource, conditional s<209/30 atlas exclusion, L'(x)>27/56, and F3 core caps. **[OPEN]** Residual Type E, Types C/D, generic e>=27, and non-isolated branches. Global proved range remains 40<=tau_5<=44.

Companion: tau5_typeE_residual_center_quantization_2026-10-28_verify.py (exact rational arithmetic).
