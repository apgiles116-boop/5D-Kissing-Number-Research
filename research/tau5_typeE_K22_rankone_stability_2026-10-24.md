# Type E: K2,2 midpoint rank-one stability and four-defect variance

2026-10-24. **[PROVED EXACTLY]** dimension-free four-vector inequalities. **[CONDITIONAL TYPE E]** for the four F3 matching-edge midpoints in the K2,2 negative-product branch. **[OPEN]** Type E elimination and the global tau_5 upper bound.

## Exact decomposition

Assume m1,m2,m3,m4 have negative inner products exactly on the four cross pairs {1,2}|{3,4}. Put C=sum ||mi||^2>0, D=-sum_cross mi.mj>0, eps=C-D, and sigma=(1,1,-1,-1).

Define v=(m1+m2-m3-m4)/4, w=(m1+m2+m3+m4)/4, h=(m1-m2)/2, k=(m3-m4)/2. Then m1=v+w+h, m2=v+w-h, m3=-v+w+k, m4=-v+w-k, and the exact sum-of-squares identities are

C=4||v||^2+4||w||^2+2||h||^2+2||k||^2;
D=4(||v||^2-||w||^2);
eps=8||w||^2+2||h||^2+2||k||^2.

Consequently T=sum_i ||mi-sigma_i v||^2=eps-4||w||^2 <= eps, and
m1.m2+m3.m4 = D-C/2+8||w||^2 >= C/2-eps.

The preceding exact spectral theorem shows eps/C<1-sqrt(3)/2 is sufficient for this K2,2 sign pattern. All formulas here also apply to any other K2,2 instance.

## Theorem 1: sharp rank-one midpoint Gram stability [PROVED EXACTLY]

Let M have columns mi, X=M^T M, X0=||v||^2 sigma sigma^T. Then

**||X-X0||_F^2 <= 2 C eps-eps^2.**

Proof: P=sigma sigma^T/4, M0=MP, E=M(I-P). Since E sigma=0, t=||E||_F^2=T<=eps<C, and the Gram blocks are orthogonal,

||X-X0||_F^2=2||M0^T E||_F^2+||E^T E||_F^2
<=2(C-t)t+t^2=2Ct-t^2<=2Ceps-eps^2.

Sharpness: collinear m1=(v+h)e, m2=(v-h)e, m3=m4=-ve, 0<h<v, give equality.

## Theorem 2: aligned midpoint normal [PROVED EXACTLY]

For spherical endpoints x_i^+-x_i^-=2zi, x_i^++x_i^-=2mi, we have mi.zi=0 and ||zi||<=1. The **specific** direction n=v/||v|| is defined because 4||v||^2>=D>0. Then

**sum_i (n.zi)^2 <= 4eps/D = 4eps/(C-eps).**

Indeed (v.zi)^2=((v-sigma_i mi).zi)^2 <= ||v-sigma_i mi||^2 ||zi||^2; sum and divide by ||v||^2>=D/4. For eps/C<=1/100 the upper bound is 4/99. The coefficient 4 is asymptotically sharp with normalized endpoints.

**Audit:** Merely asserting existence of some normal to four zi in R^5 is vacuous: such a normal always exists. The new statement is useful because n is *fixed by the midpoints*.

## Theorem 3: sharp four-cross-pair variance [PROVED EXACTLY]

Let b_ij=-mi.mj>0 on the four cross pairs. Since sum b_ij=D,

**sum_cross (b_ij-D/4)^2 <= (C^2-D^2)/4 = eps(2C-eps)/4.**

Proof: with L=[m1,m2], R=[m3,m4], C_L=||L||_F^2 and C_R=||R||_F^2,
sum b_ij^2=||L^T R||_F^2 <= C_L C_R <= C^2/4. Subtract D^2/4.
Equality holds for collinear m1=(v+h)e, m2=(v-h)e, m3=(-v+h)e, m4=(-v-h)e, 0<h<v.

For raw projected defects delta_ij=(|zi.zj|-1/2)_+, endpoint feasibility yields 0<=delta_ij<=b_ij. Hence **[CONDITIONAL TYPE E]**

**sum_cross (delta_ij-D/4)_+^2 <= eps(2C-eps)/4**, and each
delta_ij <= D/4 + sqrt(eps(2C-eps))/2.

The two within-part raw defects vanish in the spectral near-saturation branch; their projected correlations obey |z1.z2|+|z3.z4| <= 1-C/2+eps.

These constraints couple the four possible exceptional raw defects quadratically; they do not force any defect to be positive or bound the full 20x20 Q-Gram.

## Proof ledger

- **[PROVED EXACTLY]:** SOS decomposition; sharp rank-one Gram and cross-defect variance bounds; midpoint-aligned normal and aggregate safe-pair margin.
- **[CONDITIONAL TYPE E]:** The four F3 selected matching midpoints satisfy these conclusions if their negative-product graph is K2,2.
- **[OPEN]:** Combine the four-defect variance budget with safe-pair constraints and global Q-frame lower bounds; treat the complementary eps/C>=1-sqrt(3)/2 branch.
- **[UNCHANGED]:** 40<=tau_5<=44, M(F3)<=89, M(P)>=S_F3/2-28/3, A<=383/504. Types C, D, E and generic e>=27 remain open.

Verifier: tau5_typeE_K22_rankone_stability_2026-10-24_verify.py.
