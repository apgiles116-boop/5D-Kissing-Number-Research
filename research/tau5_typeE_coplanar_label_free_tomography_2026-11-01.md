# Type E: label-free rank-two tomography for a coplanar F3 core (2026-11-01)

**[PROVED EXACTLY — standalone quadratic-lift lemma; conditional Type-E application].** Global proved range remains **40 <= tau_5 <= 44**. Type E is **OPEN**.

## Inputs and conclusion

Let z_1,...,z_16 be the sixteen isolated projected edge vectors and z_c (c=1,...,4) the four selected F3 core vectors, assumed **coplanar** in a plane W. Define S_I=sum_i z_i z_i^T and the fully safe 16-by-4 matrix D_ic=(z_i.z_c)^2.

Two previously retained inputs (not reproved here) are:

1. The isolated-center harmonic gap, F3 broom M(F3)<=89, and sixteen-line weighted harmonic leakage give lambda_min(S_I)>c=73/200; see `tau5_typeE_small_isolated_mass_harmonic_spectral_gap_2026-11-01.md`.
2. The coplanar core Q-minor theorem, using a_c<=1/4 and the six-core raw defect ceiling 1780062775/4032758016, gives rank(K_C)=3 and lambda_3(K_C)>epsilon=7/100000; see `tau5_typeE_coplanar_Qminor_gap_2026-11-01.md`.

**Theorem [EXACT, CONDITIONAL].** Without isolated-Q rank 13, a two-ray factorization, D5 labeling, or ambiguous-core-completion assumptions,

```
rank(D) >= 2,
sigma_2(D)^2 > epsilon*c^2/64 = 37303/256000000000,
sigma_2(D) > (73/1600)*sqrt(7/100000) > 3/8000,
sum_{i<j,c<d} (D_ic D_jd-D_id D_jc)^2
  > 9*epsilon*c^4/4096
  = 1789089183/655360000000000000
  = 2.7299334457...e-9.
```

These bounds are weaker numerically than the earlier **more conditional** two-ray estimates sigma_2>0.003162 and minor sum >3.99969e-5. They remove those extra hypotheses within the coplanar branch; they do not prove coplanarity or eliminate Type E.

## Universal quadratic-lift lemma [PROVED EXACTLY]

For arbitrary w_i in R^2 (i=1,...,n), if S=sum_i w_i w_i^T >= c I_2 with c>0, let B be the n-by-3 matrix of symmetric-tensor coordinates of w_i w_i^T in an orthonormal basis of Sym^2(R^2). Then

```
sigma_2(B)^2 >= c^2/(4n).
```

Proof. Put q_i=||w_i||^2 and let u_i=(cos 2theta_i,sin 2theta_i); choose arbitrary u_i for zero w_i. In trace/traceless coordinates the i-th B row is q_i p_i with p_i=(1,u_i)/sqrt(2). Let R=B^T B, eigenvalues lambda_1>=lambda_2>=lambda_3. The top Rayleigh quotient is attained by a positive-semidefinite symmetric matrix H: replacing H by its matrix absolute value |H| preserves Frobenius norm and weakly increases every |w_i^T H w_i|. Write the corresponding unit coordinate vector as (a,b v), where a^2+b^2=1, a>=b>=0, ||v||=1, and put t_i=u_i.v.

For all t in [-1,1],

```
1-(a+b*t)^2/2 >= (1-t)/4.
```

For t<=0, 0<=a+bt<=1 and both sides are bounded by 1/2 in the required direction. For t>=0, (a+bt)^2<=1+t^2 by Cauchy, leaving the nonnegative difference (1-t)(1+2t)/4. Thus

```
lambda_2+lambda_3 = tr(R)-lambda_1
 >= (1/4)sum_i q_i^2(1-t_i).
```

The eigenvalues of S are (sum q_i +/- ||sum q_i u_i||)/2, so S>=cI implies sum_i q_i(1-t_i)>=2c for every v. Cauchy and sum_i(1-t_i)<=2n give sum_i q_i^2(1-t_i)>=2c^2/n. Therefore lambda_2+lambda_3>=c^2/(2n), hence lambda_2>=c^2/(4n).

A full-rank 3D lift is **not** implied: vectors w_i confined to two perpendicular rays can have S positive definite but rank(B)=2.

## Core Q transfer and minor floor [PROVED EXACTLY under inputs]

Compress to W: w_i=P_W z_i and S_W>c I_2. Let B be the lift matrix above and C the 3-by-4 matrix whose columns are symmetric-tensor coordinates of z_c z_c^T. Then D=BC. The five-dimensional traceless-Q map restricted to Sym^2(W) has metric M=diag(3/5,1,1), hence K_C=C^T M C <= C^T C. The rank-three Q eigenvalue bound implies C C^T>epsilon I_3. Therefore DD^T >=epsilon BB^T and sigma_2(D)^2>epsilon*c^2/(4*16), proving the first bound.

All D entries are nonnegative. Since ||z_c||^2>=3/4 and S_I>cI, their sum is sum_c z_c^T S_I z_c>3c. Testing D against the normalized all-ones vectors in R^16 and R^4 gives sigma_1(D)>3c/8. By Cauchy-Binet, the sum of squared 2-by-2 minors equals sum_{r<s}sigma_r(D)^2 sigma_s(D)^2, which is at least sigma_1^2 sigma_2^2 > 9 epsilon c^4/4096. No rank-two factorization identity is assumed.

**[VERIFIED LOCALLY]** The companion Fraction/SymPy script checks the exact constants, the pointwise algebra, the Q metric and a rank-two lift witness. The universal proof is analytic, not based on sampling.

**[OPEN]** An F3-incidence-sensitive upper bound on safe minors/sigma_2 is still missing. Type E (including noncoplanar cores), Types C,D, generic e>=27 and non-isolated branches remain open. Sparse e=23/24 classification still requires delta(G)>=1. Preserve star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, selected mass >=2137/6, A<=383/504, raw/homogeneous defect ceilings, and the Musin/Boyvalenkov 21-line boundary theorem.