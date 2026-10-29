# Exact sharp F3 double-matching midpoint energy and rigidity (2026-10-28)

**[PROVED EXACTLY — STANDALONE F3 CORE]** For the graph with deep edges
02,04,05,14,17,23,27,36,56,57, choose either perfect matching
P1 = 02|14|36|57 or P3 = 05|14|27|36. For unit endpoint vectors with
every deep inner product strictly below -1/2 and every nonedge inner product
at most 1/2, let C be the sum of the four squared midpoint norms. Then

\[
\boxed{C>c_*:=1-\sqrt{\sqrt3-\frac34}
=0.00901523343248242768377\ldots.}
\]

This constant is **sharp even for strictly feasible 3D realizations**.
It improves the previously retained uniform C>9/1000. Together with the
previously certified sharp all-singleton matching P2 bound
C>2-sqrt(2+sqrt(3)), it is the sharp **matching-uniform** F3 floor.

## Explicit PSD stress

For P1 let H={0,2,5,7}, L={1,3,4,6}, E_H={05,27},
E_X={04,17,23,56}, and E_L={13,46}, the last two being *safe nonedges*.
Set
\[
t=(2-\sqrt3)/4,\quad
s=(1-\sqrt{1-4t^2})/2,\quad
k=\sqrt{s/(1-s)},\quad
\gamma=2k/(1-k^2).
\]
Then 0<k<1/14 and t=k/(1+k^2). Define
\[
\alpha=\gamma(\sqrt3-k)/2,\quad
\beta=\gamma(1/\sqrt3-k)/2,\quad
h=1/2+\gamma(\sqrt3+k)/4,\quad
\ell=1/2+\gamma(1/\sqrt3+k)/4.
\]
Define S, symmetric 8x8, with diagonal h on H and ell on L,
offdiagonal 1/2 on P1, alpha/2 on E_H, beta/2 on E_L,
gamma/2 on E_X, zero otherwise.

Use the Klein-four indexing H=(0,2,5,7), L=(1,6,3,4).
The simultaneous Fourier transform reduces S to
\[
S_0=\begin{pmatrix}1+\gamma\sqrt3/2&\gamma/2\\
\gamma/2&1+\gamma/(2\sqrt3)\end{pmatrix},
\]
\[
S_1=\frac\gamma2\begin{pmatrix}\sqrt3&-1\\-1&1/\sqrt3\end{pmatrix},
\quad
S_2=\frac\gamma2\begin{pmatrix}1/k&-1\\-1&k\end{pmatrix},
\quad
S_3=\frac\gamma2\begin{pmatrix}k&1\\1&1/k\end{pmatrix}.
\]
Thus S is PSD, rank five, nullity three, with exact eigenvalues
0 (x3), 2gamma/sqrt(3), 1, (1+k^2)/(1-k^2) (x2),
and 1+2gamma/sqrt(3). Its positive spectral gap is 2gamma/sqrt(3).

For the endpoint Gram G, tr(SG)>=0, and the six unmatched deep edges
and two safe E_L pairs imply
\[
C=2+\tfrac12\sum_{P1}G_{ij}>
2-2(h+\ell)+\alpha/2-\beta/2+\gamma
=\gamma(1-\sqrt3/2-k)
=\frac{2k^2}{1+k^2}=c_*.
\]
The final equality follows from (2-sqrt(3))(1+k^2)=4k.

## Exact 3D sharpness witness

Let the three nontrivial Klein characters, in group order 0,1,2,3, be
chi1=(+,-,+,-), chi2=(+,+,-,-), chi3=(+,-,-,+). Put
\[
u=\frac{k^2(1-3k^2)}{4(1-k^4)},\quad
v=\frac{k^2(3-k^2)}{4(1-k^4)}.
\]
Then u=k^2(1/4-v), v=k^2(3/4-u), and u+v=s.
For each group element g set
\[
H_g=(\chi_1(g)/2,\chi_2(g)\sqrt u,\chi_3(g)\sqrt{3/4-u}),
\]
\[
L_g=(\chi_1(g)\sqrt3/2,\chi_2(g)\sqrt{1/4-v},
-\chi_3(g)\sqrt v).
\]
Assign H to (0,2,5,7) and L to (1,6,3,4). All vectors are unit.
Matched deep products are 2u-1 and 2v-1. The hub-hub unmatched deep
products are -1/2; hub-leaf deep products are
\[
-\sqrt3/4-\sqrt{u(1/4-v)}-\sqrt{(3/4-u)v}
=-\sqrt3/4-k/(1+k^2)=-1/2.
\]
Distinguished leaf safe products are +1/2; every other safe product is
strictly below +1/2. Hence C=2(u+v)=c_* at the nonstrict boundary.

For sufficiently small delta>0, replace hub squared amplitudes
(1/4,u,3/4-u) by (1/4-delta,u+delta,3/4-u), and leaf squared amplitudes
(3/4,1/4-v,v) by (3/4-delta,1/4-v,v+delta). All deep products become
strictly below -1/2 and all safe products strictly below +1/2: the
hub-leaf deep-contact absolute sum has derivative 1/k-2/sqrt(3)>0.
The matching energy becomes c_*+4delta. This proves sharpness in R3.

## Uniqueness and second-order rigidity

At equality, tr(SG)=0 and all six unmatched deep and two E_L safe
contacts saturate. Since ker(S) is exactly the three-dimensional
span of the witness matrix U, G=U T U^T. The four hub unit diagonals
force the offdiagonal entries of symmetric T to vanish. Hub norm and
hub cross-deep contact force T11=1. The remaining hub and leaf unit
equations have determinant
uv-(3/4-u)(1/4-v)<0, so T22=T33=1. The boundary Gram is unique.

Let delta_e=-1/2-G_e>0 for unmatched deep edges and
rho_e=1/2-G_e>=0 for the two E_L safe pairs. There is an **exact identity**
\[
C-c_*=\frac12\operatorname{tr}(SG)
+\frac\alpha2\sum_{E_H}\delta_e
+\frac\gamma2\sum_{E_X}\delta_e
+\frac\beta2\sum_{E_L}\rho_e.
\]
For Pi the orthogonal projector onto range(S),
\[
C-c_*\ge\frac\gamma{\sqrt3}\operatorname{tr}(\Pi G)
+\frac\alpha2\sum_{E_H}\delta_e
+\frac\gamma2\sum_{E_X}\delta_e
+\frac\beta2\sum_{E_L}\rho_e.
\]
This is a quantitative second-order core stability bound without D5
alignment. P3 follows from the F3 automorphism
(0,1,2,3,4,5,6,7) -> (0,1,5,6,4,2,3,7).

## Conditional Type-E consequence and proof ledger

**[CONDITIONAL ON RETAINED F3 CLASSIFICATION]** The previously proved
three-active core estimate d<=sqrt(3) C/2 now yields
C-d>(1-sqrt(3)/2)c_*=0.00120781225890586244...
for every F3 matching. This replaces the older 0.001205771... raw
slack floor; it is distinct from negative-Gram slack.

**[OPEN]** No Type-E elimination. A global incidence-sensitive upper
bound compatible with the 184 safe pairings and Q-frame variance is
still missing. Types C,D, generic e>=27, and non-isolated branches
remain open. **Global proved range unchanged: 40<=tau_5<=44.**

Exact SymPy verifier: research/tau5_typeE_F3_double_matching_exact_sharp_2026-10-28_verify.py.
