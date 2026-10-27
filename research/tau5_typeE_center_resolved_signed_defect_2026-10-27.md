# Type E: center-resolved fourth harmonic and signed-defect floor

Date: 2026-10-27. **[PROVED EXACTLY — universal algebra]** harmonic and rank-13 identities. **[PROVED EXACTLY — conditional on retained isolated-center Type-E endpoint hypotheses]** energy-resolved inequalities. **[OPEN]** No Type-E exclusion.

## Setup
For twenty disjoint deep edges write endpoints as (m_i\pm z_i), (a_i=\|m_i\|^2\in[0,1/4]), (A=\sum a_i\le383/504), (u_i=z_i/\sqrt{1-a_i}), and isolated center (x_0). Set (s_i=(x_0\cdot u_i)^2), (t=\sum s_i), (T=\sum s_i^2), (V=\|\sum u_i u_i^T-4I\|_F^2), and (R=\sum a_i/[16(1-a_i)^2]). For (c_{ij}=(u_i\cdot u_j)^2), define homogeneous twenty-line defects (P=\sum_{i<j}[c_{ij}(c_{ij}-1/4)]_+) and (E=\sum_{i<j}[c_{ij}(1/4-c_{ij})]_+).

The center-to-endpoint safety conditions imply (|x_0\cdot z_i|+|x_0\cdot m_i|\le1/2), hence (s_i\le1/[4(1-a_i)]). Therefore (T\le t/4+R).

## [PROVED EXACTLY — conditional Type E] Center-resolved inequality
The positive-definite degree-four spherical harmonic (h_4(q)=q^4-(2/3)q^2+1/21) satisfies
[
\sum_{i,j=1}^{20}h_4(u_i\cdot u_j)=5/7+2(P-E)-(5/12)V.
]
Its Gram matrix and a test vector (x_0) yield
[
P-E\ge-5/14+(5/24)V+(21/16)(T-2t/3+20/21)^2.
]
Since (V\ge(5/4)(t-4)^2) and (T\le t/4+R),
[
\boxed{P-E\ge-5/14+25(t-4)^2/96+(21/16)[5t/12-20/21-R]_+^2.}\tag{1}
]
Unlike the earlier global fourth-moment cap, this retains the coupling between center-frame coordinate (t) and quartic moment (T).

When (q=5t/12-20/21-R\ge0), the right side of (1) is **exactly**
[
\frac{125}{256}\left(t-\frac{4(7R+20)}{25}\right)^2+\frac{R(7R-10)}{10}.
]
If (q\le0), the retained energy budget gives (R<1/10), so (t<5/2); the frame term in (1) is then strictly positive. In either case,
[
\boxed{P-E\ge\frac{R(7R-10)}{10}\ge-\frac A9+\frac{7A^2}{810}.}\tag{2}
]
The last inequality uses (R\le A/9) and monotonicity of the displayed quadratic for (R\in[0,1/10]).

The function (a/[16(1-a)^2]) is increasing and strictly convex. Thus (R) is maximized at midpoint energies ((1/4,1/4,1/4,5/504,0,\ldots,0)), giving
[
R\le R_{\max}=\frac{250891}{2988012}.
]
Consequently the **uniform exact signed-defect floor** is
[
\boxed{P-E\ge-\frac{7056029129753}{89282157121440}\approx-0.0790306748543.}\tag{3}
]
This is stronger than the previous (-5/14) baseline and the center-quartic-only uniform relaxation, but is not a contradiction.

## [PROVED EXACTLY — conditional Type E] Positive-defect/frame-variance dichotomy
For (t\ge37/10), the right side of (1) increases with (t) and decreases with (R\le R_{\max}), giving
[
\boxed{t\ge37/10\Longrightarrow P-E\ge\frac{274102462207}{190468601859072}\approx0.00143909526049.}\tag{4}
]
In particular,
[
\boxed{t\ge4\Longrightarrow P-E\ge\frac{7824330390487}{47617150464768}\approx0.164317484648.}\tag{5}
]
These are also lower bounds on (P), because (E\ge0). Alternatively (t<37/10) forces (V>9/80). The split does **not** exclude either branch.

## [PROVED EXACTLY — universal algebra] Rank-13 Q-Schur inequality
Let (Q_i=u_i u_i^T-I/5), (Q_0=x_0x_0^T-I/5), (B_{ij}=\langle Q_i,Q_j\rangle), (b_i=\langle Q_0,Q_i\rangle=s_i-1/5), and (L=\|b\|^2=T-2t/5+4/5). The matrix (C=B-(5/4)bb^T) is the Gram matrix of the projections of the twenty (Q_i) onto (Q_0^\perp), hence PSD with rank at most 13. Using (\mathrm{tr}(B^2)=19+2(P-E)-3V/20) gives
[
\mathrm{tr}(B^2)\ge\frac{(16-5L/4)^2}{13}+\frac{25L^2}{16}
=\frac{128}{7}+\frac{(35L-32)^2}{728},
]
and therefore
[
\boxed{P-E\ge-5/14+3V/40+(35L-32)^2/1456.}\tag{6}
]
This independent rank-sensitive constraint can enter the finite six-core-pair optimization.

## Status and verification
**[EXACT SYMBOLIC CHECKS PASSED]** Companion SymPy verifier checks (2)-(6), rational constants, and the exact D5 Q-Gram rank 14. The inherited Type-E graph and endpoint certificates are **assumed**, not independently re-proved here.

**[OPEN]** Combine the individual six exceptional correlations, endpoint mixing, (t,T,V,R,L), and the negative defect (E) in a finite polynomial/KKT certificate. Type E is not eliminated.

**[RETAINED]** (40\le\tau_5\le44); (1/49<A\le383/504); (M(F_3)\le89); matching (M(P_{\mathrm{matching}})\ge S/2-28/3); twenty-edge mass (\ge2137/6). Types C, D, generic (e\ge27), and non-isolated branches remain open. Sparse (e=23,24) classification assumes (\delta(G)\ge1).
