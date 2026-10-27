# Type E: exact fourth-harmonic localization at the isolated center

Date: 2026-10-27. **[PROVED EXACTLY — universal algebra]** for the harmonic identities; **[PROVED EXACTLY — conditional on retained Type-E endpoint hypotheses]** for the energy-sensitive inequalities. **[OPEN]** No Type-E exclusion.

## 1. Universal 21-line identity and local correction

On the unit sphere in R^5 the degree-four positive-definite zonal harmonic kernel is
$
h_4(t)=t^4-\frac23t^2+\frac1{21},\qquad h_4(1)=\frac8{21}.
$
For 21 unit vectors v_0,...,v_20 put s_ij=(v_i·v_j)^2,
$
P=\sum_{i<j}[s_{ij}(s_{ij}-1/4)]_+,\quad
E=\sum_{i<j}[s_{ij}(1/4-s_{ij})]_+,\quad
V=\|\sum_i v_iv_i^T-(21/5)I\|_F^2.
$
From S=Σ_(i<j)s_ij=168/5+V/2 and W=Σ_(i<j)s_ij²=P-E+S/4 follows the **exact cancellation**
$
K_4:=\sum_{i,j}h_4(v_i\cdot v_j)=2(P-E)-\frac5{12}V.
$
By the harmonic addition theorem and Cauchy-Schwarz,
$
K_4\ge\frac{21}{8}\left(\sum_jh_4(v_0\cdot v_j)\right)^2.
$
Write t=Σ_(i=1)^20(v_0·v_i)^2, T=Σ_(i=1)^20(v_0·v_i)^4, and e_0=t-16/5. The row sum is h=T-(2/3)t+4/3=T-(2/3)e_0-4/5. Thus
$
\boxed{P-E\ge\frac5{24}V+\frac{21}{16}(T-\frac23t+\frac43)^2.}\tag{1}
$
The traceless quadratic tensor additionally gives V≥(5/4)e_0². The squared residual in (1) strengthens the ordinary global degree-four positivity inequality without a D5 labeling.

## 2. Type-E center-energy correction

For isolated-center Type E take v_0=x_0, v_i=u_i=z_i/√(1-a_i), a_i=||m_i||²∈[0,1/4], A=Σa_i≤383/504. Endpoint safety implies s_i=(x_0·u_i)²≤1/[4(1-a_i)]. Consequently
$
T\le t/4+R(a),\qquad
R(a)=\sum_i\frac{a_i}{16(1-a_i)^2}\le A/9.
$
Hence h≤-(5/12)e_0+R(a), and (1) gives the **exact, individual-energy-resolved second-order penalty**
$
\boxed{P\ge\frac5{24}V+
\frac{21}{16}\left[\frac5{12}e_0-R(a)\right]_+^2
\ge\frac{25}{96}e_0^2+
\frac{21}{16}\left[\frac5{12}e_0-R(a)\right]_+^2.}\tag{2}
$
A weaker scalar version replaces R(a) by A/9.

## 3. Direct 20-line defect translation

For the twenty normalized projected directions alone, put V20=||Σu_iu_i^T-4I||², with defects P20,E20, t=Σ(x_0·u_i)², T=Σ(x_0·u_i)^4. The same exact calculation yields
$
K_{4,20}=\frac57+2(P_{20}-E_{20})-\frac5{12}V_{20},
\quad K_{4,20}\ge\frac{21}{8}
\left(T-\frac{12}{7}-\frac23(t-4)\right)^2.
$
The retained isolated-center quartic cap is T≤1043632/747003. Put
$
\delta=\frac{12}{7}-\frac{1043632}{747003}
=\frac{1658612}{5229021}.
$
Then
$
\boxed{P_{20}-E_{20}\ge-\frac5{14}+\frac5{24}V_{20}
+\frac{21}{16}\left[\delta+\frac23(t-4)\right]_+^2.}\tag{3}
$
This is an exact **label-free translation of the center fourth-moment deficit into the homogeneous positive/negative projective-defect language**. The negative constant -5/14 prevents (3) alone from excluding Type E.

## 4. Status

**[PROVED EXACTLY]** Identities (1)-(3), conditional only where Type-E hypotheses enter. They preserve the actual center row, fourth moment, frame variance and individual midpoint energies instead of replacing all information by A.

**[OPEN]** Combine (1)-(3) with the six exceptional core pairings and the existing endpoint-mixing inequalities in a small polynomial/KKT problem. No new global kissing bound or Type-E exclusion is claimed.

**[RETAINED]** 40≤τ₅≤44; 1/49<A≤383/504; M(F3)≤89; M(P)≥S/2-28/3; twenty-edge mass≥2137/6. Types C,D, generic e≥27, and non-isolated branches remain open. Sparse e=23/e=24 classification assumes δ(G)≥1.
