# D5 traceless-projector synthesis: exact spectrum and generic-kernel caution (2026-10-30)

**Global proved range unchanged: 40 <= tau_5 <= 44.**

## Proof status

**[PROVED EXACTLY — universal algebra]** The 20-line D5 traceless-projector Gram matrix has spectrum **0 (multiplicity 6), 1 (multiplicity 10), 3/2 (multiplicity 4)**. Its smallest positive eigenvalue is exactly 1.

**[PROVED EXACTLY — dimensional observation]** For *any* twenty vectors in R^5, the Gram matrix of their traceless rank-one projectors has rank at most 14, hence nullity at least six. The numerical agreement between six Q-kernel modes and six exceptional Type-E pairings is therefore **not evidence of a canonical one-to-one correspondence**. D5's distinctive feature is its explicit support-incidence kernel structure, not the number six.

**[PROVED EXACTLY — perturbation theorem]** If twenty unit projectors have total squared Frobenius deviation delta^2 from a fixed D5 template and delta<1, their traceless-projector synthesis has rank 14, and the sine of the maximal principal angle between its kernel and the D5 kernel is at most delta.

**[PROVED CONDITIONALLY — retained Type-E center variance bound]** Without using the stronger October 28 harmonic midpoint cap, the projected squared-correlation sum satisfies **Q > 5876056025347/211680000000 = 27.7591460003165...**. This improves the historical 27.684187 floor, but is weaker than the retained stronger conditional Q>28.360298 result.

**[OPEN]** None of these statements eliminates Type E or identifies the six exceptional pairings with the six Q-kernel modes.

## Exact spectral proof

Index the ten K5 supports ij and their two D5 roots r_ij^pm=(e_i ± e_j)/sqrt(2). Put Q_ij^pm=r_ij^pm(r_ij^pm)^T-I/5. For coefficient pairs c_ij^+,c_ij^-, set s_ij=(c_ij^++c_ij^-)/2 and d_ij=(c_ij^+-c_ij^-)/2. Let B be the unsigned 5-by-10 K5 vertex-edge incidence matrix and P0=I-J/5.

Diagonal and off-diagonal traceless symmetric matrices are orthogonal, giving the exact sum of squares

```
||sum_ij,pm c_ij^pm Q_ij^pm||_F^2
   = 2 sum_ij d_ij^2 + ||P0 B s||_2^2.              (1)
```

The coefficient norm is ||c||^2=2||s||^2+2||d||^2. Since BB^T=3I+J, we have P0 BB^T P0=3P0. Hence ten odd coefficient modes have eigenvalue 1; the ten even modes have four eigenvalues 3/2 and six zero eigenvalues. The kernel consists exactly of d=0 and Bs constant on the five vertices. It splits into one global support relation plus five independent local support-sum relations.

## Why six kernel dimensions are generic

The real vector space Sym_0(5) of traceless symmetric 5-by-5 matrices has dimension 5*6/2-1=14. Thus any linear synthesis map from twenty traceless rank-one projectors into Sym_0(5) has kernel dimension at least 20-14=6, regardless of graph incidence, geometry, or D5 alignment. A claimed exceptional-pairing correspondence requires extra structural proof, not just matching dimensions.

## Sharp spectral-gap perturbation estimate

Let P_i^0=r_i r_i^T, P_i=u_i u_i^T, T0 c=sum_i c_i(P_i^0-I/5), and T c=sum_i c_i(P_i-I/5). Define delta^2=sum_i ||P_i-P_i^0||_F^2. Columnwise Cauchy gives ||T-T0||_op<=delta.

The D5 spectrum yields ||T0 c|| >= ||Proj_(ker T0)^perp c||. For c in ker T,

```
||Proj_(ker T0)^perp c|| <= ||T0 c||
                             = ||(T0-T)c|| <= delta ||c||.    (2)
```

If delta<1, then for c in (ker T0)^perp, ||Tc|| >= (1-delta)||c||, so T has rank 14 and its six-dimensional kernel obeys the principal-angle bound (2). Conversely, for c in ker T0, ||Tc||<=delta||c||. This is *forward* perturbation stability, not an inverse theorem asserting D5 proximity from a small kernel residual.

For weighted Type-E projected vectors z_i=sqrt(1-a_i)u_i, the weighted synthesis equals T diag(1-a_i). Since 0<=a_i<=1/4, its rank is unchanged. Also

```
||Q(z_i)-Q(r_i)||_F
 <= (1-a_i)||P_i-P_i^0||_F + (2/sqrt(5))a_i.
```

## A conservative improved correlation floor

Write A=sum a_i<=383/504, U=sum a_i^2, and retain the previously established center-derived variance lower bound

```
V_z=||sum_i Q(z_i)||_F^2 > 47602076041/317520000000.
```

The universal frame identity is Q=30-3A+A^2/10-U/2+V_z/2. Convexity on the capped simplex 0<=a_i<=1/4 gives

```
U <= 3/16 + (383/504-3/4)^2 = 47653/254016.
```

The function 30-3A+A^2/10 decreases on the allowed A interval. Therefore

```
Q > 5876056025347/211680000000 = 27.7591460003165...
```

This does not replace the stronger harmonic/joint-minimization floor Q>28.360298... previously retained.

## Next proof target

The exact D5 spectral gap 1 can support incidence-sensitive stability estimates *after* a D5 labeling is justified. The number of Q-kernel dimensions cannot, by itself, be used to match the six exceptional Type-E core pairings. Seek an explicit incidence map or a second-order signed-Walsh inequality. Type E, C, D, generic e>=27 and non-isolated branches remain open. Sparse e=23/24 classification still requires delta(G)>=1. Retain M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, and the source-audited Musin/Boyvalenkov 21-line boundary theorem.

Companion exact checker: `research/tau5_D5_Q_spectrum_2026-10-30_verify.py`.
