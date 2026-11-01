# Type E: midpoint-majorization stability and forced safe correlations (2026-11-01)

**Status: [PROVED EXACTLY, CONDITIONAL ON THE RETAINED 2026-10-28 TYPE-E HARMONIC/SCALAR CERTIFICATES].** This does **not** exclude Type E. The global proved range remains **40 <= tau_5 <= 44**.

## Retained stronger inputs (not new)

Use the [isolated-center harmonic theorem](tau5_typeE_isolated_center_harmonic_gap_2026-10-28.md), rather than the obsolete weaker midpoint cap 383/504. Let

\[
D(t)=196t-644t^2+896t^3-448t^4,\quad B=2595/256,\quad c=15-B=1245/256.
\]

For 16 isolated midpoint masses and four F3 core masses write \(x=\sum_I a_i\), \(y=\sum_C a_i\), \(A=x+y\), \(D_I=\sum_I D(a_i)\), \(D_C^{\rm mass}=\sum_C D(a_i)\). The established scalar inequalities are

\[
D_I+\Xi\le c,\qquad D_C^{\rm mass}+\tfrac12(D_I+\Xi)\le169/3-B/2,\qquad\Xi\ge0.
\]

Define \(r=D^{-1}(c)\), \(s(x)=D^{-1}(43/3-B/2-D(x)/2)\), \(s_1=s(r)=D^{-1}(41/6)\), and

\[
A_*=\tfrac12+r+s_1=0.5669250570031576\ldots.
\]

The retained stronger bounds are \(x<11/400\), \(A\le A_*\), \(U=\sum a_i^2\le0.1282700463200052\ldots\), and the squared-correlation floor \(L_*=28.2677055569326959\ldots\), as proved in the linked upstream note.

## New strong-concavity and concentration lemma [PROVED EXACTLY]

On \([0,1/4]\), \(D''(t)=-1288+5376t-5376t^2\le-280\). Thus \(g(t)=D(t)+140t^2\) is concave. Let \(e(v)\) be the capped extreme vector at mass \(v\): as many coordinates \(1/4\) as possible, one remainder, and zeros. Since \(e(v)\) majorizes any other capped nonnegative vector \(a\) of mass \(v\), Karamata gives

\[
\sum_jD(a_j)\ge\sum_jD(e_j(v))+140\delta(v),
\quad \delta(v)=\|e(v)\|_2^2-\|a\|_2^2\ge0.
\]

Moreover, for the decreasing rearrangement \(a^\downarrow\),

\[
\boxed{\delta(v)\ge\|e(v)-a^\downarrow\|_2^2.}
\]

Indeed \(a^\downarrow\cdot(e-a^\downarrow)\ge0\) by Abel summation and majorization, and expand the difference of squared norms.

Set \(\delta_I=x^2-\sum_Ia_i^2\), and \(\delta_C=U_C^{\max}(y)-\sum_Ca_i^2\), with \(U_C^{\max}(y)=k/16+(y-k/4)^2\), \(k=\lfloor4y\rfloor\), extended continuously at \(y=1\).

## New midpoint-energy second-order stability [PROVED CONDITIONALLY]

In the high-core-mass branch \(y\ge1/2\), necessarily \(y<3/4\), and

\[
D_I\ge D(x)+140\delta_I,\quad
D_C^{\rm mass}\ge42+D(y-1/2)+140\delta_C.
\]

The scalar constraints imply

\[
D(y-1/2)\le D(s(x))-70\delta_I-140\delta_C-\Xi/2.
\]

As \(0<D'(t)\le196\), inversion yields \(y\le1/2+s(x)-(70\delta_I+140\delta_C+\Xi/2)/196\). The retained scalar-envelope inequality \(x+s(x)\le r+s_1\) therefore gives

\[
\boxed{A+\tfrac5{14}\delta_I+\tfrac57\delta_C+\tfrac1{392}\Xi\le A_*.}\tag{1}
\]

In particular, if \(A\ge A_*-\varepsilon\), the isolated masses are within squared Euclidean distance \(14\varepsilon/5\) of a one-supported vector, and the four sorted core masses are within squared distance \(7\varepsilon/5\) of \((1/4,1/4,y-1/2,0)\). This is **midpoint-mass rigidity, not D5 geometric rigidity**. For \(y<1/2\), \(A\le1/2+r=A_*-s_1\), giving a gap \(s_1>0.039\) from the scalar maximum.

## New global Q-frame stability [PROVED CONDITIONALLY]

Let \(V_z=\|\sum_i z_i z_i^\top-(20-A)I_5/5\|_F^2=\|\sum_iQ_i\|_F^2\ge0\). The exact frame identity is

\[
C_z:=\sum_{i<j}(z_i\cdot z_j)^2
=30-3A+A^2/10-\tfrac12\sum_i a_i^2+\tfrac12V_z.
\]

For \(y\ge1/2\), insert \(\sum a_i^2=x^2+1/8+(y-1/2)^2-\delta_I-\delta_C\). The remaining scalar expression is decreasing in \(y\), and along \(y=1/2+s(x)\) it is decreasing in \(x\in[0,r]\), as established by the derivative bounds in the 2026-10-28 note. Its minimum is

\[
L_*=30-3A_*+A_*^2/10-\tfrac12(1/8+r^2+s_1^2).
\]

For \(y\le1/2\), the elementary bounds \(A\le1/2+r\) and \(\sum a_i^2\le r^2+1/8-\delta_I-\delta_C\) give a stronger scalar floor \(>28.383\). Therefore **for all Type E**,

\[
\boxed{C_z\ge L_*+\tfrac12(\delta_I+\delta_C+V_z).}\tag{2}
\]

This retains the positive quadratic corrections from mass dispersion and frame anisotropy without a D5 labeling or any six-to-six kernel identification.

## New six-exception transfer and integer counts [PROVED CONDITIONALLY]

For the six exceptional core pairings let \(d_e=(|z_i\cdot z_j|-1/2)_+\), \(D_{\rm raw}=\sum_e d_e\le D_*=1780062775/4032758016<0.441401\). Their squared correlations sum to at most \(3/2+D_{\rm raw}+D_{\rm raw}^2\). Subtracting from (2),

\[
\boxed{\sum_{\rm 184\ safe}(z_i\cdot z_j)^2
\ge L_*-\tfrac32-D_{\rm raw}-D_{\rm raw}^2
+\tfrac12(\delta_I+\delta_C+V_z).}\tag{3}
\]

Exact rational brackets \(L_*>282677/10000\), \(D_*<441401/10^6\) give the safe squared-correlation sum \(>26.131464157199>26\). If at most 40 of the 184 safe pairs had \(|z_i\cdot z_j|>1/3\), their sum would be at most \(40/4+144/9=26\). Thus **at least 41 safe pairings exceed 1/3 in absolute correlation**.

Independently, for the sixteen isolated projected vectors, the frame/Welch inequality and \(x<11/400\) give

\[
\sum_{i<j\in I}(z_i\cdot z_j)^2>
\frac{7015679}{400000}=17.5391975>\frac{35}{2}.
\]

At most 30 isolated pairs above \(1/3\) would yield at most \(30/4+90/9=35/2\). Thus **at least 31 of the 120 isolated-isolated pairings exceed 1/3**.

These are necessary conditions, not a contradiction or a Type-E elimination. The new stability identities provide an exact target for a finite signed-F3 endpoint/KKT certificate near two core masses approaching \(1/4\).

**Verification:** [companion SymPy regression](tau5_typeE_midpoint_majorization_Qstability_2026-11-01_verify.py). **[OPEN]** Type E, C, D, generic \(e\ge27\), non-isolated branches; sparse \(e=23/24\) classification remains conditional on \(\delta(G)\ge1\). **Global proved range: \(40\le\tau_5\le44\).**
