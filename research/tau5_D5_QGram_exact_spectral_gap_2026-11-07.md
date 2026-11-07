# Exact D5 Q-Gram spectrum and kernel projector (2026-11-07)

**[PROVED EXACTLY — D5 template only].** This note computes the complete spectrum of the 20-by-20 Gram matrix of the traceless rank-one tensors of the D5 20-line configuration. It does **not** assume Type E has D5 incidence, and gives no new global bound; `40 <= tau_5 <= 44` remains unchanged.

For each unordered support `0 <= i < j < 5` and sign `s in {+1,-1}`, put
`z_(ij,s)=(e_i+s e_j)/sqrt(2)` and `Q_(ij,s)=z z^T-I_5/5`.
The 20-by-20 Q-Gram is
`K_(a,b)=tr(Q_a Q_b)=(z_a.z_b)^2-1/5`.
Its entries are rational and depend only on the D5 incidence.

**[PROVED EXACTLY]** The complete spectrum is

```
eigenvalue 0    multiplicity 6
eigenvalue 1    multiplicity 10
eigenvalue 3/2  multiplicity 4
```

Hence `rank K=14`, and the **smallest positive eigenvalue is exactly 1**. In particular `K(K-I)(K-3I/2)=0`.

The orthogonal projector onto the six-dimensional Q-kernel is the exact polynomial

```
P_ker = (2/3)(K-I)(K-(3/2)I)
      = I - (5/3)K + (2/3)K^2.
```

It satisfies `P_ker^2=P_ker`, `P_ker^T=P_ker`, `K P_ker=0`, and `tr P_ker=6`.
For every coefficient vector `c in R^20`,

```
c^T K c >= ||(I-P_ker)c||^2.
```

Equality holds precisely when `c` has no component in the eigenvalue-3/2 subspace. This is an exact **spectral rigidity/coercivity inequality modulo the six Q-kernel directions**.

**[PROVED EXACTLY — conditional perturbation statement].** For any real symmetric `K'=K+E` with `||E||_op <= epsilon`, Weyl's theorem puts the six smallest eigenvalues of `K'` in `[-epsilon,epsilon]` and the other fourteen in `[1-epsilon,infinity)`. If `epsilon<1/2`, the two clusters are separated. For a true Q-Gram `K'`, all eigenvalues are nonnegative. This is a **conditional stability tool**, not a proof that Type-E Q-Grams are close to D5.

**[EXACT KERNEL STRUCTURE]** The ten support-pair sums satisfy
`Q_(ij,+)+Q_(ij,-)=E_ii+E_jj-(2/5)I`.
The unsigned vertex-edge incidence matrix of K5 has rank 5, so its kernel is five-dimensional and gives five independent relations among these sums. The sixth independent relation is the global tight-frame relation `sum_(ij,s) Q_(ij,s)=0`. No identification with the six potentially exceptional Type-E pairings is claimed.

**[VERIFIED EXACT ARITHMETIC]** Companion pure-Python verifier constructs the rational Gram matrix and verifies its cubic minimal polynomial, spectral multiplicities via rational traces, projector identities, and the unsigned-incidence rank, without numerical eigensolvers.

**[OPEN]** To use this for Type E, first establish a justified correspondence or a quantitatively controlled perturbation of its twenty projected lines to D5. In particular the current midpoint ceiling `A<=383/504` does not itself imply `||K'-K||_op<1/2`. The canonical F3 three-defect path witnesses and sixteen outside edges still need a joint rank-five obstruction. Types C/D, generic `e>=27`, non-isolated branch remain open; sparse `e=23,24` classification assumes `delta(G)>=1`.
