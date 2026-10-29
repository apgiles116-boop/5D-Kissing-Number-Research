# Universal 21-line quartic defect: exact improvement to P > 1/58

Date: 2026-10-29.

**[PROVED EXACTLY — STANDALONE]** For any 21 unit vectors \(u_0,\ldots,u_{20}\in\mathbb R^5\), put \(s_{ij}=(u_i\cdot u_j)^2\) and \(P=\sum_{i<j}[s_{ij}(s_{ij}-1/4)]_+\). Then

\[
\boxed{P>1/58.}
\]

This improves the previous exact \(P>1/61\) certificate. It uses a frame/Bessel bound and a signed Huber dual, not a new SDP or D5 labeling.

## 1. Harmonic and two-well rounding

Write \(F=\sum_i u_iu_i^T\), \(\Delta=F-(21/5)I\), \(V=\operatorname{tr}\Delta^2\), and \(N=\sum_{i<j}[-s_{ij}(s_{ij}-1/4)]_+\). The positive-definite Gegenbauer decomposition

\[
t^4-t^2/4=1/28+\tfrac13P_2^{(5)}(t)+\tfrac8{21}P_4^{(5)}(t)
\]

implies \(P-N\ge5V/24\). Assume \(P\le p=1/58\); then \(0\le V\le12/145\).

Round every \(s_{ij}\) to its nearest element \(r_{ij}\in\{0,1/4\}\). Let \(K\) count the pairs rounded to \(1/4\), and \(L=\sum_{i<j}|s_{ij}-r_{ij}|\). A positive quartic pair has rounding error at most four times its positive quartic contribution. A negative quartic pair with negative mass \(h=s(1/4-s)\) has rounding error \(g(h)=1/8-\sqrt{1/64-h}\). Convex concentration of negative mass gives

\[
L\le L_0(V):=4p+G(p-5V/24),
\]
\[
G(E)=\begin{cases}
1/8-\sqrt{1/64-E},&0\le E\le1/64,\\
1/4-\sqrt{1/32-E},&1/64\le E<1/32.
\end{cases}
\]

The branch crossing is \(v_*=9/1160\). The function \(L_0\) is decreasing and convex on each of \([0,v_*]\), \([v_*,12/145]\). Also \(2L_0<37/58<7/10\).

Let \(k_i\) be the rounded degree of vertex \(i\), \(c_i=k_i/4-16/5\), \(e_i=u_i^T\Delta u_i\), and \(d_i=e_i-c_i\). The exact trace/degree identities are

\[
\sum_i|d_i|\le2L_0(V),\qquad
\sum_i d_i=D_K(V):=V+336/5-K/2. \tag{1}
\]

Since \(V\le12/145<1/10\), (1) excludes \(K\le133\) and \(K\ge136\). Only \(K=134,135\) remain.

## 2. Sharper frame/Bessel inequality

For unit \(u_i\), Cauchy gives \(e_i^2\le u_i^T\Delta^2u_i\). Thus

\[
\sum_i e_i^2\le\operatorname{tr}(F\Delta^2)
\le\lambda_{\max}(F)V.
\]

Because \(\Delta\) is traceless and \(5\times5\), its largest eigenvalue is at most \(\sqrt{4V/5}\) (the other four eigenvalues sum to its negative). Therefore

\[
\boxed{\sum_i e_i^2\le B(V):=(21/5+\sqrt{4V/5})V.} \tag{2}
\]

This improves the previous Q-Gram Gershgorin estimate in the relevant interval. \(B(V)\) is convex for \(V\ge0\).

## 3. Signed Huber dual

For \(\lambda\ge0\) and real \(\eta\), define the convex function

\[
h_{\lambda,\eta}(c)=\min_e\{e^2+\lambda|e-c|+\eta(e-c)\}.
\]

Writing \(\alpha=\lambda+\eta,\ \beta=\lambda-\eta\), its three branches are \(-\alpha c-\alpha^2/4\) for \(c<-\alpha/2\), \(c^2\) for \(-\alpha/2\le c\le\beta/2\), and \(\beta c-\beta^2/4\) for \(c>\beta/2\).

Since \(h\) is convex, balancing the integer rounded degrees minimizes \(\sum_i h(k_i/4-16/5)\) at fixed \(\sum k_i=2K\). For \(K=134\), the minimizing degrees are sixteen 13s and five 12s; for \(K=135\), eighteen 13s and three 12s. Calling the corresponding lower bound \(H_K(\lambda,\eta)\), (1) and (2) imply

\[
H_K(\lambda,\eta)\le B(V)+2\lambda L_0(V)+\eta D_K(V). \tag{3}
\]

The signed term \(\eta D_K(V)\) is essential; the old unsigned Huber bound discarded it. The right side of (3) is convex on each branch of \(L_0\).

## 4. Exact finite certificate

For \(K=134\), choose \(\lambda=1/3,\eta=-1/40\). Then \(H_{134}=13219/57600\), and take \(v_{134}=179/5000\).

For \(K=135\), choose \(\lambda=1/3,\eta=1/4\). Then \(H_{135}=131/800\), and take \(v_{135}=23/1000\).

In both cases \(0<v_*<v_K<12/145\). Exact rational/surd comparisons show

\[
D_{134}(v_{134})-2L_0(v_{134})>0,\quad
-D_{135}(v_{135})-2L_0(v_{135})>0,
\]

and for each \(K\), the right side of (3) is strictly smaller than \(H_K\) at \(V=0,v_*,v_K\). The smallest positive margin is the \(K=134\) Huber comparison at \(v_{134}\):

\[
-\frac{9245417}{208800000}
-\frac{179\sqrt{1790}}{1250000}
+\frac{\sqrt{1768710}}{26100}>0
\quad(\approx0.000617738878).
\]

The signed trace margins are

\[
-\frac{22059}{145000}+\frac{\sqrt{1768710}}{8700}>0,
\quad
-\frac{3217}{29000}+\frac{\sqrt{38454}}{1740}>0.
\]

The companion verifier uses exact Fraction arithmetic and integer-square-root enclosing intervals for all eight strict comparisons, without floating-point tolerances.

For \(V\le v_K\), piecewise convexity makes the right side of (3) no larger than the maximum of its values at \(0,v_*,v_K\), contradicting (3). For \(V\ge v_K\), (1) is impossible: \(D_{134}(V)-2L_0(V)\) is increasing, and \(-D_{135}(V)-2L_0(V)\) is increasing because \(G'(E)\ge4\) on each branch (derivative at least \(2/3\) for the latter). Both \(K\) values are impossible. Thus \(P>1/58\).

## Proof ledger and Type-E scope

- **[PROVED EXACTLY]** Universal normalized quartic gap \(P>1/58\), with no D5 or Type-E hypothesis.
- **[CONDITIONAL ON THE RETAINED SIX-EXCEPTION NORMALIZATION BRIDGE]** The earlier bridge now reads \(P_{\rm raw}>81/14848-(5/4)A-(9/16)A_C\). This is generally vacuous near \(A=383/504\), so it is **not** a Type-E elimination or a stronger midpoint ceiling.
- **[OPEN]** Need a weighted 184-safe-Walsh inequality coupling the 16+4 geometry to the six exceptional core pairings. Types C, D, E, generic \(e\ge27\), and non-isolated branches remain open. Sparse \(e=23/e=24\) classification remains conditional on \(\delta(G)\ge1\). Preserve star \(70/3\), broom \(M(F_3)\le89\), matching \(M(P)\ge S/2-28/3\), and \(A\le383/504\). **Global proved range remains \(40\le\tau_5\le44\).**
