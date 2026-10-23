# Type E: rank-14 D5 Q-Gram Schur completion and exact 1/26 frame gap
2026-10-23. **[PROVED EXACTLY, conditional on D5 labels with four distinct core supports]** The sixteen complementary D5 Q-vectors form a frame on the 14-dimensional traceless-symmetric space with lower frame bound 1/26. This upgrades the previous 4-by-4 PSD inequality to an **exact nonlinear rank-14 Schur-complement identity** with quadratic remainder. **[NEGATIVE RESULT, PROVED EXACTLY]** A repeated-support core admits a PSD rank-14 Gram completion with unchanged safe/diagonal entries and a changed missing entry; it duplicates a line and is not Type-E feasible. **[OPEN]** Global D5 labeling, collision-case endpoint completion, Type-E exclusion, and tau_5=40. Global proved range: 40<=tau_5<=44.

## Exact complementary frame gap

Let w_ab^±=(e_a±e_b)/sqrt(2) for the twenty D5 projective lines and Q_i=w_i w_i^T-I/5. Their rational Q-Gram G0_ij=(w_i.w_j)^2-1/5 has rank 14 and six-dimensional kernel. Select four core indices J with distinct K5 coordinate supports and put O=J^c. On Sym_0(R^5), define F_O by <B,F_O B>=sum_{i in O} tr(Q_i B)^2.

**Theorem 1 [PROVED EXACTLY].** For every one of the 210 four-support subsets and all sixteen choices of core signs,
    F_O >= (1/26) I.
Thus G0[O,O] has rank 14, and its fourteen positive eigenvalues are >=1/26.

**Rational certificate.** Use the basis D_j=E_jj-E_44 (j=0,...,3) and F_ab=E_ab+E_ba (a<b). Its metric is diag(H,2I_10), H=I_4+J_4. For support s={a,b}, let d_s[j]=(1_{j in s}-1_{4 in s})/2. Then 2 sum_s d_s d_s^T=(3/2)H. The Schur complement of the off-diagonal block of F_O-tI, with t=1/26, is
    S_J(t)=(3/2-t)H-[2(1-t)/(1-2t)] sum_{s in J} d_s d_s^T.
The ten eliminated pivots are 2-2t or 1-2t, all positive. Removed-root signs cancel from this Schur complement. For all 210 subsets, the exact minima of the four leading principal minors of S_J(1/26) are
    131/156,
    146969/129792,
    72205331/121485312,
    32734055/1579309056.
They are all positive; Sylvester's criterion proves the frame gap without numerical eigenvalues.

## Exact rank-14 nonlinear completion

Let G be any 20-by-20 real PSD matrix of rank at most 14 and write G=G0+R+E, where E has zero diagonal and is supported only on the six off-diagonal pairs in J. Let P=I-(5/3)G0+(2/3)G0^2, H_J=P[J,J], K=P[:,J]H_J^(-1). Then G0 K=0 and K[J,:]=I_4. Put T=K^T R K, B=R[O,:]K, and epsilon=||R||_op.

**Theorem 2 [PROVED EXACTLY, conditional on the stated labeling and epsilon<1/26].**
    E[J,J]+T = B^T (G[O,O])^dagger B.
The right-hand side is PSD and quadratic in R. Exact enumeration gives ||k_r||^2<=14 and ||k_r||||k_s||<=4sqrt(7) for r!=s. Therefore
    0<=T_rr<=14 epsilon^2/(1/26-epsilon),
    |E_rs+T_rs|<=4sqrt(7) epsilon^2/(1/26-epsilon),
    |E_rs|<=4sqrt(7) epsilon/(1-26epsilon).
For epsilon<1/52, the final bound improves the earlier 8sqrt(7)epsilon PSD-only estimate; the quadratic identity is the more useful new constraint.

**Proof.** Theorem 1 and Weyl's inequality give 14 positive eigenvalues of G[O,O] at least 1/26-epsilon. Since rank G<=14 and G is PSD, rank G[O,O]=rank G=14. Hence G=G[:,O](G[O,O])^dagger G[O,:] and ||(G[O,O])^dagger||<=1/(1/26-epsilon). Compress this exact identity with K. Because G0K=0, K[J,:]=I, and E[O,:]=0, the left side is T+E[J,J] and the right side is B^T(G[O,O])^dagger B. The bounds follow by Cauchy-Schwarz and the exact kernel dual-norm enumeration. An independent exact rational perturbed-rank-one-Q-Gram test checks the identity.

For actual Type-E Q_i=z_i z_i^T-(||z_i||^2/5)I, rank G<=14 automatically. **But** the current global correlation floor and frame variance do not imply D5 labeling or epsilon<1/26; neither hypothesis may be assumed.

## Sharp repeated-support limitation

**[PROVED EXACTLY; not Type-E feasible]** Choose both signed lines of one D5 support in J and replace Q_ab^- by a duplicate of Q_ab^+. Its inner products with all Q vectors on different supports are unchanged, as are its norm and every safe/diagonal Gram entry. Thus R=0 and the new G is still PSD of rank 14, but the same-support missing entry changes from -1/5 to 4/5, giving E=1. No universal |E|<=C||R|| estimate can hold for such repeated-support cores under PSD/rank alone.

The example has coherence 1 and violates the endpoint bound. For genuine selected deep edges, m_i.m_j+|z_i.z_j|<=1/2 and a_i=||m_i||^2<1/4 imply |z_i.z_j|<=1/2+sqrt(a_i a_j)<3/4. A collision-case theorem must retain this endpoint geometry.

## Proof-status ledger

- **PROVED EXACTLY:** 1/26 D5 complementary frame gap (210 rational certificates, all 3360 signed cases), rank-14 Schur completion, quadratic remainder, collision counterexample.
- **CONDITIONAL:** Type-E use of the completion requires a D5 labeling with distinct core supports and epsilon<1/26.
- **OPEN:** repeated-support completion using endpoint inequalities; global D5 proximity; Type E, C, D, generic e>=27, non-isolated 41-code branches; tau_5=40.
- **RETAINED:** M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass>=2137/6, A<=383/504, squared-correlation floor 8790283/317520+V/2. Sparse e=23/e=24 graph classification requires delta(G)>=1. Global 40<=tau_5<=44.

Next: eliminate the pseudoinverse by fixing a 14-by-14 invertible minor of G[O,O], retain the four quadratic diagonal identities and six off-diagonal identities in the finite endpoint polynomial system. Do not infer a D5 neighborhood from the scalar frame variance alone.
