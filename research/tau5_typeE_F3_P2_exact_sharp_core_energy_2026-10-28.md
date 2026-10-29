# Type E: sharp exact F3 all-singleton (P2) midpoint energy

**2026-10-28. [PROVED EXACTLY — STANDALONE F3 CORE THEOREM].**
For canonical F3 edges 02,04,05,14,17,23,27,36,56,57 and the all-singleton perfect matching P2=04|17|23|56, any eight unit endpoint vectors satisfying all F3 deep contacts strictly below -1/2 obey

$$
C:=\sum_{ab\in P2}\|(u_a+u_b)/2\|^2
>c_*:=2-\sqrt{2+\sqrt3}=0.06814834742186343\ldots.
$$

This sharpens the retained P2 bound C>=17/250. It is sharp as an **infimum for the isolated F3 constraints** (not a global Type-E realization). The bound needs no ambient-rank restriction, D5 alignment, or numerical SDP.

## Exact rank-five PSD stress

Order H=(0,2,7,5) as a 4-cycle and L=(4,3,1,6) as their matched partners. The six cross-matching F3 edges split into O4={02,05,27,57}, a C4 on H, and O2={14,36}, opposite pairs on L.

Define
$$
h=\sqrt6/4,\quad \ell=(1/\sqrt6+1/\sqrt2)/2,\quad
a=(\sqrt6-\sqrt2)/4,\quad b=1/\sqrt2-1/\sqrt6.
$$
Construct an 8x8 symmetric matrix S: diagonal h on H, diagonal ell on L, offdiagonal 1/2 on P2, a/2 on O4, b/2 on O2, and zero elsewhere.

**[PROVED EXACTLY] S is PSD of rank five.** The C4 adjacency and opposite matching commute. Fourier decomposition gives four 2x2 blocks
$$
S_{\lambda,\mu}=
\begin{pmatrix}h+a\lambda/2&1/2\\1/2&\ell+b\mu/2\end{pmatrix},
\quad(\lambda,\mu)=(2,1),(0,-1),(0,-1),(-2,1).
$$
The two (0,-1) blocks have determinant zero since h(ell-b/2)=1/4; the (-2,1) block has determinant zero since (h-a)(ell+b/2)=1/4. The (2,1) block is positive definite. All block diagonals are positive.

For any endpoint Gram G>=0 with G_ii=1, tr(SG)>=0, and
$$
\operatorname{tr}(SG)=4(h+\ell)+\sum_{P2}G_{ij}
+a\sum_{O4}G_{ij}+b\sum_{O2}G_{ij}.
$$
Since each cross F3 edge is strictly below -1/2,
$$
C=2+\tfrac12\sum_{P2}G_{ij}>
2-2(h+\ell)+a+b/2
=2-(\sqrt6+\sqrt2)/2=c_*.
$$

## Exact rank-three witness and equality rigidity

For k=0,1,2,3 let theta=k*pi/2 and s=(-1)^k. The following 3D unit vectors, indexed by H_k and L_k, attain the nonstrict bound:
$$
U_{H_k}=(\cos\theta,\sin\theta,s)/\sqrt2,\qquad
U_{L_k}=(-\sqrt3\cos\theta/2,-\sqrt3\sin\theta/2,-s/2).
$$
All matched products are -sqrt(2+sqrt3)/2, all six cross F3 products equal -1/2, and all nonedges are <1/2 (largest 1/(2sqrt2)). The Gram has rank three and SG=0.

**[PROVED EXACTLY] The equality Gram is unique.** Equality implies SG=0 and hence G=UTU^T for a symmetric 3x3 T. Unit diagonal equations fix T13=T23=0 and T11=T22=T33=1. One O4 contact equality fixes T12=0, giving T=I.

To make all ten deep edges **strict**, replace the H planar/vertical squared amplitudes (1/2,1/2) by (1/2-t,1/2+t), and the L amplitudes (3/4,1/4) by (3/4+t,1/4-t). For all sufficiently small t>0 the O4 products become -1/2-t, O2 products -1/2-2t, matched products remain <-1/2, and all nonedges stay <1/2. Thus strict feasible realizations approach C=c_*.

## Quantitative second-order stability

For cross F3 edges define delta_ij=-1/2-G_ij>=0. Exact expansion gives
$$
\boxed{C-c_*=\tfrac12\operatorname{tr}(SG)
+\tfrac a2\sum_{O4}\delta_{ij}
+\tfrac b2\sum_{O2}\delta_{ij}.}
$$
The smallest positive eigenvalue of S exceeds 1/4: its two singular block types have positive eigenvalues >1, and the (2,1) block satisfies
$$
\det(S_{2,1}-I/4)=
\sqrt3/2-7/16-\sqrt6/8-\sqrt2/16>0.
$$
With Pi the orthogonal projection onto range(S), S>=Pi/4, yielding
$$
\boxed{C-c_*\ge\tfrac18\operatorname{tr}(\Pi G)
+\tfrac a2\sum_{O4}\delta_{ij}
+\tfrac b2\sum_{O2}\delta_{ij}.}
$$
For G=VV^T, tr(Pi G)=||Pi V||_F^2, an exact squared frame-deviation penalty. This does not presume D5 geometry.

Under the separately retained <=3-active-pairing certificate and raw-excess estimate epsilon_raw >= (1-sqrt3/2) C, the P2 branch now has
$$
\epsilon_{\rm raw}>
(1-\sqrt3/2)(2-\sqrt{2+\sqrt3})
=0.009130147328601944\ldots,
$$
improving the old P2 value 0.009110272542658172....

**[RETAINED]** M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, Musin/Boyvalenkov 21-line zero-midpoint exclusion. **[OPEN]** P1/P3 double-pattern sharp constants; global coupling to 184 safe pairings and Q variance; Type E, C, D, generic e>=27 and non-isolated branches. **GLOBAL PROVED RANGE UNCHANGED: 40<=tau_5<=44.**

Exact SymPy verifier: research/tau5_typeE_F3_P2_exact_sharp_core_energy_2026-10-28_verify.py.
