# Type E: exact D5 support-plane fibre excluded by the midpoint-energy cap
Date: 2026-10-30

**[PROVED — computer-assisted exact rational certificate; CONDITIONAL on exact D5 support-plane structure]**

For the retained isolated-center Type-E reduction, assume the 20 normalized projected directions are arranged as orthonormal pairs spanning the ten coordinate 2-planes of one orthonormal basis, with the four F3 core selected edges assigned to one line on each of four star supports. Under this **additional geometric hypothesis**, the 184 safe Walsh pairings and isolated-center constraints imply

[
A=sum_{i=1}^{20}|m_i|^2gerac{11}{14}=rac{396}{504},
]

contradicting the retained Type-E cap (Ale383/504) by (13/504).

**[OPEN]** This does not exclude arbitrary Type E: exact or approximate D5 support-plane geometry is not established from the known Type-E hypotheses. The global proved range remains (40le	au_5le44).

## Geometry and safe-support incidence

Write (x_i^pm=m_ipm z_i), (a_i=|m_i|^2le1/4), (w_i=|z_i|^2=1-a_i), (u_i=z_i/sqrt{w_i}). The isolated unit center (v) satisfies (|vcdot z_i|le1/2), hence (|vcdot u_i|^2le1/3).

Label the ten coordinate supports by the edges of (K_5). Assign the four core selected edges to one line each on supports ((1,2),(1,3),(1,4),(1,5)). The other 16 selected edges fill the other 16 positions. Among the 30 pairs of meeting supports, discard six star-star pairs that each may contain one exceptional core-core line pairing. The remaining 24 meeting-support pairs are *fully safe* (all four line pairings safe): 12 star/nonstar and 12 nonstar/nonstar. Their degrees are 3 on each of the four star supports and 6 on each of the six nonstar supports. Fully safe means (|z_icdot z_j|le1/2), by the four endpoint Walsh coefficients.

For each support (e), let (t_ein[0,1]) be its orthonormal basis's absolute squared-coordinate imbalance, equivalently (t_e=|sin2delta_e|) relative to its D5 basis. For meeting supports (e,f), their normalized 2-by-2 cross-Gram matrix is an outer product, so its largest squared entry is ((1+t_e)(1+t_f)/4). At a fully safe meeting pair, the maximizing line pair (i,j) obeys
[
(1+t_e)(1+t_f)le 1/(w_iw_j)le16/9.
]
Every support has a fully safe meeting neighbor; therefore (t_ele7/9).

For (0le ale1/4), (-log(1-a)le7a/6). For (0le tle7/9), (log(1+t)ge11t/15). Both follow from concavity and exact endpoint checks:
[
log(4/3)le47/162<7/24,quad
log(16/9)ge2(7/25+(7/25)^3/3)>77/135.
]
Taking logs of the maximizing-pair inequality gives
[
t_e+t_fle(35/22)(a_i+a_j)le(35/22)(A_e+A_f),
]
where (A_e) is the sum of the two midpoint energies on support (e). Summing over the 24 fully safe meeting-support pairs gives
[
oxed{T_C+2T_Nle(35/22)(A_C+2A_N)le(35/11)A.}	ag{1}
]

## Isolated center forces a minimum total imbalance

Set (p_k=v_k^2), sort (p_1gecdotsge p_5ge0), (sum p_k=1). Each support's two center-projection squares sum to (p_i+p_j) and are individually at most (1/3); hence (p_1+p_2le2/3).

For support ((i,j)), put (D=2sqrt{p_ip_j}), (X=p_i-p_j), (B=2/3-p_i-p_j). The difference of its two squared center projections has magnitude at most (B). Writing this in the rotated D5 basis yields
[
Dsqrt{1-t_{ij}^2}-Xt_{ij}le B.
]
Since (t_{ij}le7/9<4/5), (sqrt{1-t_{ij}^2}ge1-t_{ij}/2). Therefore
[
t_{ij}gerac{((sqrt{p_i}+sqrt{p_j})^2-2/3)_+}{p_i-p_j+sqrt{p_ip_j}},
]
with zero-denominator terms defined as zero. Define (F(p)) as the sum of these ten lower bounds.

**[EXACT INTERVAL LEMMA]** For every sorted (p) with (sum p=1) and (p_1+p_2le2/3),
[
oxed{F(p)ge5/2.}	ag{2}
]

The accompanying pure-Python exact verifier certifies (2) by subdividing the sorted simplex, whose five rational vertices are (p^{(k)}=(1/k,ldots,1/k,0,ldots,0)). Each simplex has vertices represented by integers over a common denominator (D_0). Let (l_i,h_i) be coordinate-wise integer minima/maxima over its vertices. If (3(l_1+l_2)>2D_0), the simplex is infeasible. Otherwise each summand of (F) is bounded below by
[
rac{(3[l_i+l_j+2lfloorsqrt{l_il_j}floor]-2D_0)_+}
{3[h_i-l_j+lceilsqrt{h_ih_j}ceil]}.
]
The bounds follow from coordinate monotonicity and denominator domination. Each simplex is bisected along its longest edge; both children cover their parent. Only exact integer square roots and rational comparisons are used for certification. The executed verifier closed after **28,707 subdivisions**, with 23,846 bound-pruned children and 4,862 domain-pruned children.

Since (T_C+T_Nge F(p)ge5/2), inequality (1) yields (Age11/14), contradicting (Ale383/504).

## Status and next step

**[PROVED — exact computer-assisted, conditional]** The exact D5 support-plane fibre is excluded with energy margin (13/504).

**[OPEN]** Quantitative inverse stability: derive an explicit support-plane approximation from the weighted (Q)-Gram global variance and five cycle residuals, then propagate the energy margin through the approximation. Do not identify the six exceptional pairings with six Q-kernel relations without proof. Type C, Type D, generic (ege27), and non-isolated branches remain open. Sparse (e=23,24) classification remains conditional on (delta(G)ge1). Retain (M(F_3)le89), matching mass (ge2137/6), and (Ale383/504).
