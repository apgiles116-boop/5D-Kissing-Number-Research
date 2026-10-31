# Type E: mass-sensitive four-core planar obstruction and rank-two polynomial

Date: 2026-10-31. **GLOBAL PROVED: 40 <= tau_5 <= 44. TYPE E OPEN.**

## Proof-status ledger

**[PROVED EXACTLY — universal planar inequality]** Let four selected deep-edge pairs have midpoint energies a_c=||m_c||^2 in [0,1/4], projected half-differences z_c with ||z_c||^2=1-a_c, and endpoint constraints m_c.m_d+|z_c.z_d|<=1/2. Suppose each z_c is within eta of a common coordinate 2-plane and its two planar coordinate magnitudes are <=B, where 1/sqrt(2)<=B<sqrt(3/4-eta^2). Put A_C=sum a_c, u0=sqrt(1-eta^2-B^2), u1=sqrt(3/4-eta^2-B^2), D=u0-u1. According to the sign-parity split of the four planar vectors, one of the following necessary lower bounds holds:

- 2+2: A_C >= (8 B u0-2-4 eta^2)/(1+8 B D).
- 3+1: A_C >= (12 B u0-3-6 eta^2)/(1+16 B D).
- 4+0: A_C >= (24 B u0-6-12 eta^2)/(1+24 B D).

For a uniform bound take the **minimum** of these three expressions.

**[PROVED EXACTLY — conditional Type-E exclusion]** Let the sixteen isolated normalized Q-projectors have rank 13 and rank-two missing matrix; assume all four F3 core lines have genuinely ambiguous rank-one completions relative to the fixed isolated realization. Suppose the sixteen isolated lines have a bijective, commonly rotated rank-13 D5 sixteen-line reference with squared projector deviation E_I<=1/2,000,000, and isolated midpoint energy A_I<=1/100. Then A=A_I+A_C>383/504, contradicting the retained Type-E cap. Thus all four core completions cannot be ambiguous in this neighborhood. This improves the previous neighborhood's A_I cap by a factor 100 and E_I cap by a factor 50. **No universal D5 proximity is assumed or proved.**

**[PROVED EXACTLY — sign-free planar core polynomial]** For any three projected core vectors lying in one plane, put t_i=1-a_i, d_ij^2=(z_i.z_j)^2, C_ij=2d_ij^2-t_i t_j. Then

t_i^2 t_j^2 t_k^2 + 2 C_ij C_ik C_jk - t_k^2 C_ij^2 - t_j^2 C_ik^2 - t_i^2 C_jk^2 = 0.

For four coplanar vectors, H_ii=1, H_ij=C_ij/(t_i t_j) is PSD of rank at most 2, so all its 3x3 minors vanish. These are polynomial constraints on exceptional squared correlations and core masses, independent of orientation choices.

## Proof of planar midpoint bound

Write x_c for the planar component of z_c and y_c for the transverse component, with ||y_c||<=eta. The two planar coordinate magnitudes are <=B and ||x_c||^2>=1-a_c-eta^2. Because B^2>=1/2 and ||x_c||^2<=1<=2B^2, the first-quadrant angle of each x_c lies between arccos(B/||x_c||) and arcsin(B/||x_c||). For two vectors of the same sign parity, the maximal angular separation yields

|x_c.x_d| >= B(v_c+v_d), v_c=sqrt(1-a_c-eta^2-B^2).

Therefore |z_c.z_d|>=B(v_c+v_d)-eta^2 and m_c.m_d<=1/2-B(v_c+v_d)+eta^2. For a parity class of size n, PSD of ||sum_class m_c||^2 gives

sum_class a_c >= 2B(n-1)sum_class v_c - n(n-1)(1/2+eta^2).

The concavity chord on 0<=a_c<=1/4 gives v_c>=u0-4a_c(u0-u1). Summing over parity classes of sizes (2,2), (3,1), or (4,0), and bounding the energy of each class by A_C, gives the three stated formulas. All arguments are analytic.

## Three-support D5 budget and perturbation

For every rank-13 D5 sixteen-line subframe, the missing support is a pair {p,q} with both signed roots removed; the two further deletions remove only single roots. Consequently, for each j=p,q, all three supports {j,k} with k outside {p,q} retain at least one root.

The previously certified exact rank-13 D5 Q spectral gap lambda_min^+>1/8 implies that the actual missing-plane projector P and reference P0 satisfy ||P-P0||_F<=8 sqrt(2E_I)=eta, assuming rank 13 and rank-two missing matrices. Genuinely ambiguous core lines lie in range(P), hence have transverse norm <=eta.

For an isolated root r_i and normalized actual line u_i=z_i/sqrt(1-a_i), orient u_i so ||u_i-r_i||<=e_i:=||u_i u_i^T-r_i r_i^T||_F. The endpoint envelope and a_c<=1/4 give

|z_c.r_i| <= (1+sqrt(a_i))/(2sqrt(1-a_i))+e_i.

Each of the three roots for coordinate j therefore yields

|(z_c)_j| <= (1+sqrt(a_i))/sqrt(2(1-a_i))+sqrt(2)e_i+eta.

Average over these **same three roots**, then use Cauchy and sum a_i<=A_I, sum e_i^2<=E_I:

B(A_I,E_I)=(1+sqrt(A_I/3))/sqrt(2(1-A_I))+sqrt(2E_I/3)+8sqrt(2E_I).

This avoids incorrectly assuming that the minimum-a_i root also minimizes e_i.

## Exact rational contradiction

For E_I<=1/2,000,000, eta<=1/125 and sqrt(2E_I/3)<29/50000.

Case 0<=A_I<=1/200: sqrt(1/600)<41/1000 and 1/sqrt(199/100)<709/1000, so B<746649/1000000<747/1000. For B=747/1000, eta=1/125, exact rational square tests give

664775/10^6<u0<664777/10^6; u1>438094/10^6.

Use lower u0 in numerators and upper D<(664777-438094)/10^6 in denominators. The (2+2),(3+1),(4+0) bounds respectively exceed

246554925/294332201, 739664775/927328804, 739664775/632996603.

Each exceeds 79/100>383/504. Contradiction.

Case 1/200<=A_I<=1/100: sqrt(1/300)<58/1000 and 1/sqrt(198/100)<711/1000, so B<760818/1000000<761/1000. For B=761/1000, eta=1/125, exact rational square tests give

648702/10^6<u0<648704/10^6; u1>413297/10^6.

The three parity bounds respectively exceed

243630222/304144727, 365445333/483289454, 730890666/662434181.

Each exceeds 189/250. Hence A=A_C+A_I>189/250+1/200=761/1000>383/504. Contradiction.

All inequalities can be checked by clearing positive denominators and squaring nonnegative rational bounds; no numerical optimization is used.

## Proof of sign-free polynomial

Write z_i/sqrt(t_i)=(cos theta_i,sin theta_i) in their common plane. Then H_ij=2cos^2(theta_i-theta_j)-1=cos(2theta_i-2theta_j). Hence H is the Gram matrix of (cos 2theta_i,sin 2theta_i), so PSD rank<=2. The 3x3 determinant identity, multiplied by t_i^2 t_j^2 t_k^2, is precisely the displayed polynomial.

## Status and next step

**[OPEN]** The result does not eliminate rank-13 cases outside this neighborhood, cases with unique core completions, or other Q ranks. A next step is to use the sign-free rank-two core equations for three or four ambiguous lines in a finite KKT/endpoint system and to seek proximity bounds from safe data.

Retain star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, raw defect <=1780062775/4032758016, homogeneous defect <=5792292955405/4129544208384, and Musin/Boyvalenkov antipodal zero-midpoint exclusion. Sparse e=23/24 classification requires delta(G)>=1. Types C, D, generic e>=27, non-isolated branches OPEN. **GLOBAL PROVED RANGE UNCHANGED: 40<=tau_5<=44.**
