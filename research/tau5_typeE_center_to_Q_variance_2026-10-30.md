# Type E: isolated-center harmonic gap forces macroscopic Q-frame anisotropy (2026-10-30)

**[PROVED EXACTLY — conditional on Type E graph and retained M(F3)≤89]** The isolated-center harmonic second-moment row satisfies **q < -983/5000**.

**[PROVED EXACTLY — using retained A≤383/504]** The projected Q-frame variance satisfies **V_z > 47602076041/317520000000 > 0.1499**. The full twenty-edge frame variance satisfies **V_edge > 24830289/80000000 > 0.3103**.

**[PROVED CONDITIONALLY — using stronger 2026-10-28 harmonic A<567/1000 cap]** The projected Q-frame variance satisfies

\[
\boxed{V_z>\frac{14814801}{80000000}=0.1851850125.}
\]

Thus the weighted Petersen residual \(E_Q=V_z+12C_z\) exceeds the same value, independently of D5 labeling. This is a *lower* bound, not a Type-E exclusion.

## Exact proof of the rational q cap

Let \(v\) be the isolated center and \(x_i^\pm=m_i\pm z_i\) the twenty selected deep-edge endpoint pairs. Set

\[
T=\sum_{x\in X}xx^\top-\frac{41}{5}I,\quad
s=\sum_{x\ne v}(v\cdot x)^2,\quad q=v^\top Tv=s-\frac{36}{5},
\]

and \(N_0=\sum_{x\ne v}7(v\cdot x)^2(1-4(v\cdot x)^2)\ge0\).
The degree-four Delsarte identity and Type-E mass ceiling give

\[
M_{\rm deep}=410+N+E_h=336-D_I+M(F_3)\le425-D_I,
\]

where \(E_h=(35/6)\|T\|_F^2+14K_4\), \(D_I\ge0\), \(N\ge N_0\). Hence \(E_h+N_0\le15\).

The exact isolated-center harmonic row estimate (2026-10-28) gives, whenever \(q\ge-12/7\),

\[
E_h\ge f(q)=10+\frac{35}{64}(5q+4)^2.
\]

If \(q\ge-39/200\), then \(f(q)\ge307287/20480>15\).
If \(-983/5000\le q\le-39/200\), then \(s=7+r\) with \(17/5000\le r\le1/200\). Capped-simplex concentration gives

\[
N_0\ge7r(1-4r)\ge\frac{5831}{250000}.
\]

Since \(f\) is increasing on this interval,

\[
E_h+N_0\ge f(-983/5000)+\frac{5831}{250000}
=15+\frac{72851}{64000000}>15,
\]

a contradiction. The case \(q<-12/7\) already satisfies the cap. Therefore **\(q<-983/5000\)**.

## Exact transfer to frame variance

Let \(S=\sum_i(m_im_i^\top+z_iz_i^\top)\), \(M=\sum_i m_im_i^\top\succeq0\), \(Z=S-M\), and \(A=\operatorname{tr}M\). Opposite-sign endpoint pairing gives

\[
v^\top S v=s/2=18/5+q/2.
\]

Define \(B_{\rm edge}=S-4I\), \(B_z=Z-(20-A)I/5=\sum_iQ_i\). Both are trace-free, and

\[
v^\top B_{\rm edge}v=q/2-2/5,\qquad
v^\top B_zv=q/2-2/5+A/5-v^\top Mv.
\]

For every trace-free symmetric \(5\times5\) matrix \(B\), Cauchy against \(vv^\top-I/5\) gives

\[
\|B\|_F^2\ge\frac54(v^\top Bv)^2.
\]

Inserting \(q<-983/5000\) gives

\[
V_{\rm edge}=\|B_{\rm edge}\|_F^2>
\frac54(4983/10000)^2=\frac{24830289}{80000000}.
\]

With historical \(A\le383/504\),

\[
V_z=\|B_z\|_F^2>
\frac54(218179/630000)^2
=\frac{47602076041}{317520000000}.
\]

With stronger retained \(A<567/1000\),

\[
V_z>\frac54(3849/10000)^2
=\frac{14814801}{80000000}.
\]

## Walsh and squared-correlation consequences

The previously verified six-deep/474-safe Walsh identity has \(V_{\rm edge}/2\) on its nonnegative right-hand side. The new strict offset is

\[
V_{\rm edge}/2>\frac{24830289}{160000000}=0.15518930625.
\]

The exact projected correlation identity is

\[
\sum_{i<j}(z_i\cdot z_j)^2
=30-3A+A^2/10-U/2+V_z/2.
\]

The retained 2026-10-28 joint scalar minimum \(28.2677055569326959\ldots\) therefore gives

\[
\sum_{i<j}(z_i\cdot z_j)^2>28.36029806318\ldots.
\]

A simpler exact rational bound, using \(A<567/1000\), \(U<129/1000\), is

\[
\sum_{i<j}(z_i\cdot z_j)^2>
\frac{36299829}{1280000}=28.35924140625.
\]

These are necessary conditions, not a D5 proximity theorem.

**[OPEN]** Type E remains open. The stronger strategy is now to seek an *upper* bound on \(V_z\) below \(0.1851850125\) using the 184 safe Walsh blocks and six exceptional core pairings, or an incompatible center-conditional safe-contact slack bound. No identification between six exceptional pairings and six Q-kernel modes is assumed.

**[RETAINED]** M(F3)≤89, matching \(M(P)\ge S/2-28/3\), historical \(A\le383/504\), stronger conditional harmonic cap, Musin/Boyvalenkov zero-midpoint exclusion, sparse graph classification conditional on \(\delta(G)\ge1\). Types C,D, generic e≥27, and non-isolated branches remain open. **Global proved range: \(40\le\tau_5\le44\)**.
