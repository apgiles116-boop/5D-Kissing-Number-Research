# D5 Q-Gram spectral gap, universal nullity, and Type-E template separation

2026-11-01. **[PROVED EXACTLY — standalone D5 algebra]** Spectrum, projector, coercivity and stability inequality. **[CONDITIONAL TYPE E]** Quantitative template separation uses the retained Type-E anisotropy certificate. No Type-E exclusion or claim of novelty relative to the literature.

## Exact D5 spectrum

Let v_{ij}^\pm=(e_i\pm e_j)/sqrt(2), for 1<=i<j<=5, and Q(v)=vv^T-(||v||^2/5)I_5. Let K0 be the 20-by-20 Q-Gram matrix, K0_{ab}=tr(Q(v_a)Q(v_b)). Then

    spec(K0) = {0 (multiplicity 6), 1 (multiplicity 10), 3/2 (multiplicity 4)}.

If N=ker(K0), the exact coercivity inequality is

    dist(c,N)^2 <= c^T K0 c <= (3/2)dist(c,N)^2.  (1)

**Important conceptual correction.** Sym_0(5) has dimension 14. Consequently the Q-Gram of *any* 20 vectors in R5 has nullity at least six. The nullity count alone cannot identify the six Type-E exceptional pairings with D5-specific relations. The explicit kernel subspace and positive spectral gap are special to D5.

## Proof and rational projector

Index the ten supports e={i,j}. Let B be the unsigned 5-by-10 vertex-edge incidence matrix of K5; P=I_5-J_5/5. Let S and D be 10-by-20 matrices taking respectively the sum and difference of the plus/minus coefficients on each support. Orthogonality of the traceless diagonal and off-diagonal parts gives the exact identity

    K0 = (1/2)D^T D + (1/4)S^T B^T P B S.        (2)

Since B B^T=3I_5+J_5, P B B^T P=3P. The antisymmetric support sector has eigenvalue 1 and dimension 10. The symmetric support sector has eigenvalue 3/2 and dimension 4, plus a six-dimensional kernel. This kernel is the global all-support relation together with the five-dimensional zero-degree cycle space ker(B).

The exact orthogonal kernel projector is

    P_N = (1/2) S^T [I_10-(1/3)B^T P B] S.       (3)

It is symmetric and idempotent, tr(P_N)=6, K0 P_N=0. For any 20 projected vectors z, with K(z) their Q-Gram, define the label-dependent six-mode residual

    R_D5(z)=tr(P_N K(z))>=0.                       (4)

It vanishes precisely when the six D5 kernel relations hold for Q(z); this alone is *not* asserted to characterize a D5 packing. Since the normalized all-ones vector belongs to N,

    R_D5(z) >= ||sum_i Q(z_i)||_F^2/20 = V_z/20. (5)

## Second-order template-distance inequality

For any 20 vectors z_i with sum ||z_i||^2=20-A, define S_z=sum z_i z_i^T and V_z=||S_z-(20-A)I_5/5||_F^2. For *any* D5 template assignment v_i, including arbitrary common rotations, signs, and permutations, put D=sum_i ||z_i-v_i||^2. Then

    V_z + A^2/5 = ||S_z-4I_5||_F^2
                 <= (4 sqrt(D)+D)^2.              (6)

Proof: write z_i=v_i+delta_i. Since sum v_i v_i^T=4I_5, the linear frame perturbation L=sum(v_i delta_i^T+delta_i v_i^T) satisfies ||L||_F<=4 sqrt(D). Indeed for every Frobenius-unit symmetric H, |tr(HL)|<=2 sqrt(D) sqrt(tr(H^2 sum v_i v_i^T))=4 sqrt(D). The quadratic remainder sum delta_i delta_i^T is PSD with Frobenius norm at most its trace D. The trace/traceless decomposition gives the left equality.

The retained Type-E certificate is V_z>949/5000. If D<=9/800, equation (6) gives

    V_z <= 9/50+81/640000+27/(2000 sqrt(2))
         < 9/50+81/640000+27/2800
         = 949/5000-137/4480000,

using sqrt(2)>7/5. Contradiction. Therefore:

    [CONDITIONAL TYPE E] D>9/800=0.01125       (7)

for every assignment to every rotated/signed D5 template. Also R_D5(z)>949/100000. Neither is a Type-E exclusion; retain the coupled A-dependent bound (6).

## Conditional kernel transport

Let eta=||K(z)-K0||_op. If eta<1, the universal rank ceiling 14 and Weyl's inequality imply rank K(z)=14 and nullity exactly six. For every c in ker K(z), coercivity (1) gives

    ||(I-P_N)c|| <= eta ||c||.                  (8)

This is a quantitative kernel-rotation estimate, but neither a justified D5 support labeling nor eta<1 has been established for Type E.

## Proof-status ledger

**[PROVED EXACTLY — standalone]** (1)-(6), (8) conditional on its explicit closeness hypothesis, and the universal nullity observation. **[PROVED EXACTLY — conditional on retained Type-E Q-frame anisotropy]** (7) and R_D5(z)>949/100000. Companion SymPy verifier checks the exact Gram entries, spectrum, projector, and rational margin. **[OPEN]** Type E, C global/boundary, D, generic e>=27, and non-isolated branches. Sparse e=23/24 classification still assumes delta(G)>=1. Preserve M(F3)<=89, M(P)>=S/2-28/3, and Musin/Boyvalenkov. **Global proved range remains 40<=tau_5<=44.**
