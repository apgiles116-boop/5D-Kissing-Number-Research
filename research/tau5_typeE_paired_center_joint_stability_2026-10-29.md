# Type E: joint paired-center/frame stability (2026-10-29)

**Proof status: [EXACT NEW ALGEBRA; CONDITIONAL TYPE-E APPLICATION].** This note assumes the retained isolated-center mass/harmonic certificates, the *conditional* signed-Gram-atlas exclusion \(s\ge209/30\), and the retained large-\(x\) monotonicity \(L'(x)>27/56\). Those upstream certificates are not reverified here. This is **not** a Type-E exclusion. Global proved range remains \(40\le\tau_5\le44\).

For the twenty selected deep edges \(u_i^\pm=m_i\pm z_i\), set \(A=\sum\|m_i\|^2\), \(U=\sum\|m_i\|^4\), \(Q=\sum_{i<j}(z_i\cdot z_j)^2\). For the isolated-center unit vector \(v\), put \(p_i=v\cdot m_i\), \(q_i=v\cdot z_i\), \(B_v=\sum p_i^2\), and \(s=2\sum(p_i^2+q_i^2)\). The 40 center contacts are nondeep.

Define
\[
D(x)=196x-644x^2+896x^3-448x^4,\quad
E(s)=10+\frac{35}{64}(5s-32)^2,\quad s_0=\frac{209}{30},
\]
\[
c(x)=D^{-1}\!\left(\frac{43}{3}-\frac{2595/256+D(x)}2\right),\
a(x)=\frac12+x+c(x),\quad u(x)=\frac18+x^2+c(x)^2,
\]
\[
h(x,s)=4-\frac{a(x)}5-\frac s2,\quad
F(x,s)=30-3a(x)+\frac{a(x)^2}{10}-\frac{u(x)}2+\frac58h(x,s)^2.
\]
The retained certificates yield \(A\le a(x)\), \(U\le u(x)\), and \(D(x)+E(s)+N_0\le15\), with \(N_0=7\sum_{40}t_j^2(1-4t_j^2)\).

## New result

Let \(x_2\) be the unique small root \(D(x_2)=2509/6400\), so \(0.002013442<x_2<0.002013443\). Then, **conditional on the stated upstream certificates**,
\[
\boxed{Q>\frac{283965067}{10000000}=28.3965067.}
\]
The exact relaxed critical value is \(F(x_2,s_0)=28.39650678133767366\ldots\). This improves the preceding conditional \(Q>28.39644\).

Moreover, on \(x_2\le x\le1/250,\ 69/10\le s\le s_0\),
\[
\boxed{Q\ge F(x_2,s_0)+\frac23(x-x_2)+\frac1{10}(s_0-s)+\frac{29}{40}B_v^2.}
\]
For \(0\le x\le x_2,\ s\le s_0\),
\[
\boxed{Q\ge F(x_2,s_0)+\frac12(x_2-x)+\frac14(s_0-s).}
\]
These are scalar stability inequalities, not a full geometric Type-E contradiction.

## Proof

For each selected edge, \(s_i=(p_i+q_i)^2+(p_i-q_i)^2=2(p_i^2+q_i^2)\in[0,1/2]\). Expansion gives the exact paired-center identity
\[
N_0=7\sum_{i=1}^{20}\left[s_i(1-2s_i)-16s_ip_i^2+32p_i^4\right].
\]
Concavity on the capped simplex, \(s_i\le1/2\), and Cauchy–Schwarz give
\[
N_0\ge n_2(s)-56B_v+\frac{56}{5}B_v^2,\quad
n_2(s)=7\rho(1-2\rho),\quad \rho=s-\frac{\lfloor2s\rfloor}{2}.
\]
In \(69/10\le s\le s_0\), \(\rho=s-13/2\), \(n_2(s_0)=49/225\), \(E(s_0)=33155/2304\), and \(15-E(s_0)-n_2(s_0)=2509/6400\).

Let \(T=\sum z_i z_i^T\) and \(V=\|T-(20-A)I_5/5\|_F^2\). The global frame identity is
\[
Q=30-3A+\frac{A^2}{10}-\frac U2+\frac V2.
\]
Cauchy–Schwarz with \(vv^T-I_5/5\), whose squared Frobenius norm is \(4/5\), yields
\[
V\ge\frac54\left(4-\frac A5-\frac s2+B_v\right)^2.
\]
Using \(A\le a(x),U\le u(x)\), and the relevant monotonicity,
\[
Q\ge F(x,s)+\frac54h(x,s)B_v+\frac58B_v^2.
\]
For \(x\le1/250,\ s\le s_0\), rational bounds give \(h>2/5\), hence \(Q\ge F+\frac12B_v+\frac58B_v^2\). The center resource gives
\[
D(x)+E(s)+n_2(s)-56B_v+\frac{56}{5}B_v^2\le15.
\]
Therefore, defining \(J=F+[D+E+n_2-15]/112\), we obtain the exact quadratic coercivity
\[
\boxed{Q\ge J(x,s)+\frac{29}{40}B_v^2.}
\]
On \(0\le x\le1/250,\ 69/10\le s\le s_0\), exact rational bounds give \(-1<F_x<-1/2,\ F_s<-1/4,\ D'(x)>190,\ E'(s)+n_2'(s)<16\). Thus
\[
J_x>-1+\frac{190}{112}>\frac23,\qquad
J_s<-\frac14+\frac{16}{112}<-\frac1{10}.
\]
These yield the two stability inequalities and the minimum at \((x_2,s_0,B_v=0)\) in the relaxed narrow region. For \(x_2\le x\le1/250,\ s\le69/10\), the retained scalar bound \(F(1/250,69/10)\) is stronger. For \(x\ge1/250\), the retained large-\(x\) certificate gives \(L(1/250)>28.39759\).

Exact rational enclosures \(2013442/10^9<x_2<2013443/10^9\) and \(c(x_2)<55694237/10^9\) establish \(F(x_2,s_0)>283965067/10^7\). A companion Python verifier checks the rational inequalities; it does **not** recertify the upstream mass/harmonic/atlas inputs.

Using separately retained six-core squared-correlation caps, the 184 safe pairings satisfy
\[
S_{\rm safe}>\frac{530977009}{20000000}=26.54885045\quad(P_1/P_3),
\]
\[
S_{\rm safe}>\frac{266152567}{10000000}=26.6152567\quad(P_2).
\]

**[OPEN]** No incompatible safe-pair upper bound yet. Type E, Type C, Type D, generic \(e\ge27\), and non-isolated branches remain unresolved. Do not regress to \(M(F_3)\le94\) or the old matching estimate.