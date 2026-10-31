# Type E: exact rank-13 D5 missing-plane stability theorem

Date: 2026-10-31. **Global proved range 40<=tau_5<=44; Type E OPEN.**

## Status and theorem

**[PROVED EXACTLY — finite D5 spectral certificate]** For any rank-13 sixteen-line D5 subframe (both signed roots on one support deleted, plus two single roots on distinct other supports), the smallest positive eigenvalue of its traceless-projector Q-Gram matrix satisfies

lambda_min^+(K_I) > 1/8.

The exact rational/SymPy verifier fixes the missing support {0,1} by symmetry, enumerates all 144 other deletion pairs, and checks exact characteristic polynomials and Sturm root counts. Five polynomials occur, with multiplicities 36,24,48,24,12; none has a positive root <=1/8. This covers all 1,440 rank-13 D5 subframes by coordinate symmetry.

**[PROVED EXACTLY — conditional Type-E exclusion]** In a hypothetical Type-E system of twenty selected deep edges with endpoints m_i±z_i, a_i=||m_i||²<=1/4 and A=sum a_i<=383/504, suppose the sixteen isolated normalized lines u_i=z_i/sqrt(1-a_i) have traceless Q-span of rank 13, whose Frobenius-unit missing matrix S has matrix rank two. Suppose **all four F3 core projectors have two genuinely distinct rank-one completions** from the isolated Q measurements. Let the isolated lines admit a bijective commonly rotated labeling by a rank-13 D5 sixteen-line reference r_i, and define

A_I=sum_{i isolated}a_i,
E_I=sum_{i isolated}||u_i u_i^T-r_i r_i^T||_F².

Then the conditions A_I<=1/10000 and E_I<=1/100000000 are **incompatible**. Thus within this explicit D5 neighborhood at least one core completion must be unique.

This does not prove D5 proximity or small isolated midpoint energy for arbitrary Type E, and does not eliminate Type E.

## 1. Exact stability of the missing Q-plane

Let T0:R^16 -> Sym_0(5) synthesize the sixteen D5 reference projectors Q(r_i)=r_i r_i^T-I/5, and T the actual isolated Q(u_i). Then ||T-T0||_F²=E_I. The D5 spectral lemma gives the smallest nonzero singular value of T0 greater than 1/sqrt(8).

Let S0 be the Frobenius-unit missing-Q matrix of T0, and S the corresponding missing matrix of T. Since T* S=0 and ||S||_F=1,

||T0* S|| <= sqrt(E_I).

Writing S=alpha S0+S_perp yields ||S_perp||_F <= sqrt(8 E_I). Choose the sign of S0 to make alpha>=0. Then

||S-S0||_F²=2(1-alpha)<=2(1-alpha²)<=16 E_I,

so ||S-S0||_F<=4sqrt(E_I).

A tracefree rank-two Frobenius-unit symmetric matrix has eigenvalues +1/sqrt(2), -1/sqrt(2), 0,0,0. Thus P=2S² and P0=2S0² are orthogonal projectors onto their two-dimensional ranges, and

||P-P0||_F <=2(||S||_op+||S0||_op)||S-S0||_F <=8sqrt(2 E_I).

For E_I<=1/100000000 this is <3/2500=:eta. By the exact rank-two phase-retrieval lemma, any genuinely ambiguous core projected vector z_c lies in range(S), so its component perpendicular to the reference D5 missing-support plane L=range(S0) has norm <=eta.

## 2. Core coordinate cap from safe isolated contacts

For distinct deep edges i,c, the four endpoint inequalities imply

m_c.m_i+|z_c.z_i|<=1/2.

Since a_c<=1/4, |z_c.z_i|<=(1+sqrt(a_i))/2. For normalized u_i and projective reference r_i, choose the sign of r_i to ensure

||u_i-r_i|| <= ||u_i u_i^T-r_i r_i^T||_F=:e_i.

Consequently

|z_c.r_i| <= (1+sqrt(a_i))/(2sqrt(1-a_i))+e_i.

Every D5 rank-13 subframe retains at least one signed root on every support except the fully deleted support {p,q}. For each j=p,q, choose a retained root (e_j±e_k)/sqrt(2) with k outside {p,q}. Since the transverse core component is <=eta,

|(z_c)_j| <= (1+sqrt(a_i))/sqrt(2(1-a_i)) +sqrt(2)e_i+eta.

The hypotheses A_I<=1/10000 and E_I<=1/100000000 give a_i<=1/10000 and e_i<=1/10000. Hence

|(z_c)_j| <=101/sqrt(19998)+sqrt(2)/10000+3/2500
<101/141+3/20000+3/2500 <18/25=:B.

The last rational margin is 6593/2820000>0.

## 3. Two-class midpoint-energy contradiction

Decompose each core z_c=x_c+y_c, with x_c in the D5 missing-support plane L and ||y_c||<=eta. Then ||x_c||²>=3/4-eta², and both planar coordinate magnitudes are <=B=18/25. Both are nonzero. Divide the four cores into two classes according to the sign of the product of these two planar coordinates.

For two vectors x_c,x_d in the same class, independent global sign changes put them in the same quadrant. Their normalized coordinate magnitudes are <=B/sqrt(3/4-eta²). The elementary angular-interval inequality gives

x_c.x_d >= 2B sqrt(3/4-eta²-B²).

The exact rational margin

3/4-eta²-B²-(12/25)² =7491/6250000>0

implies x_c.x_d>432/625. Since y_c.y_d>=-eta², we have

|z_c.z_d|>432/625-eta²

for every same-class pair. The endpoint envelope therefore forces

m_c.m_d < -239/1250+eta².

For a class of n cores, midpoint Gram PSD gives 0<=||sum m_c||², hence its total midpoint energy exceeds n(n-1)(239/1250-eta²). For two classes of sizes n and 4-n, the minimum of n(n-1)+(4-n)(3-n) is 4. Thus

A_C > 4(239/1250-eta²)=478/625-4(3/2500)² >383/504.

The final exact margin is 959491/196875000>0. Contradiction.

## Interpretation and retained ledger

This removes the previous *exact core-plane* assumption in a small, explicitly quantified D5 rank-13 neighborhood. The new uniform rank-13 spectral gap >1/8 enables further perturbative phase-retrieval analysis. The previous sign-parity criterion and the cancellation of core signs from V_z-2Q_6 remain valid. Next seek to enlarge the forbidden neighborhood or link A_I/E_I to retained global Q-energy and center constraints.

Preserve star 70/3, broom M(F3)<=89, matching M(P)>=S_total/2-28/3, twenty-edge mass >=2137/6, A<=383/504, raw/homogeneous defect caps, Musin/Boyvalenkov zero-midpoint exclusion, and sparse e=23/24 classification only when delta(G)>=1. **Types C,D,E, generic e>=27, non-isolated branches OPEN; global 40<=tau_5<=44 unchanged.**
