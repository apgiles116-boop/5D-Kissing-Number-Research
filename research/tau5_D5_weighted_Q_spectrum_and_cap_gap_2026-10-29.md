# Weighted D5 Q-frame spectrum and sharp cap-gap (2026-10-29)

**[PROVED EXACTLY — D5-template algebra; CONDITIONAL Type-E application]**. This is an extension of the previously recorded unweighted D5 Q-spectrum, not a new proof of D5 alignment or a Type-E exclusion.

## Exact spectral decomposition

For 20 D5 projective lines indexed by supports `ij` and signs `+/-`, set `v_ij^±=(e_i±e_j)/sqrt(2)` and `R_i=v_i v_i^T-I/5`. The synthesis map `T0 c=sum c_i R_i` has Gram spectrum

`spec(T0* T0)={3/2 (4 times), 1 (10 times), 0 (6 times)}`.

Indeed for every traceless symmetric matrix X,

`sum_i <R_i,X>^2=(3/2)||diag X||_F^2+||offdiag X||_F^2`.

Let `S_ij=R_ij^++R_ij^-`. Five independent local Q-cycle relations are

```
S01+S23-S02-S13=0
S01+S23-S03-S12=0
S01+S24-S02-S14=0
S01+S24-S04-S12=0
S01+S34-S03-S14=0
```

Together with `sum_i R_i=0`, they span the six-dimensional kernel. The six exceptional Type-E pairings are **not** identified with these six relations.

For arbitrary `0<=a_i<=1/4`, put `w_i=1-a_i` and `W=diag(w_i)`. Under **exact D5 alignment** `z_i=sqrt(w_i)v_i`, the Q-Gram is `W G0 W`, has rank 14 and six-dimensional kernel `W^(-1)ker(G0)`, and all 14 positive eigenvalues lie in `[9/16,3/2]`. This follows from `sigma_min^+(T0)=1` and `min w_i>=3/4`. Thus unequal midpoint norms merely reweight, rather than destroy, the six kernel relations.

## Sharp quadratic cap obstruction under D5 alignment

Let `A=sum a_i`, `U=sum a_i^2`, and `J` be the 120 unordered D5 line pairs with `(v_i.v_j)^2=1/4`. Define `J_a=sum_{(i,j) in J}a_i a_j`. Every D5 line has 12 neighbors in J. Direct expansion gives the **exact identities**

```
Q=sum_{i<j}(z_i.z_j)^2 = 30-3A+J_a/4,
V=||sum_i z_i z_i^T-(20-A)I/5||_F^2 = U-A^2/5+J_a/2.
```

Consequently `Q>=30-3A` and `V>=U-A^2/5`. At `A=B=383/504`, with capped energies `(1/4,1/4,1/4,5/504,0^16)`, this gives

```
V>=11447/158760 = 0.0721025447...,
Q>=4657/168 = 27.7202380952...
```

Both are **sharp for the D5-aligned template**: place the four nonzero energies on mutually orthogonal lines `01+`, `01-`, `23+`, `23-`. The Q bound exceeds the previously retained universal capped-frame floor `8790283/317520` by `11447/317520`. It is weaker than separately retained *conditional center-sensitive* Type-E Q floors; it does not improve the global proof ledger without an alignment certificate.

## Robust angular and capped-energy stability

For arbitrary labeled unit directions `u_i`, set `z_i=sqrt(w_i)u_i`, `sin(theta_i)=sqrt(1-(u_i.v_i)^2)`, and `rho=sqrt(2) sum_i w_i sin(theta_i)`. The projector identity `||u_i u_i^T-v_i v_i^T||_F=sqrt(2)sin(theta_i)` gives, with `d0=U-A^2/5+J_a/2`,

```
V >= (sqrt(d0)-rho)_+^2,
Q >= 30-3A+A^2/10-U/2+(sqrt(d0)-rho)_+^2/2.
```

If `b(A)` is the sorted capped-filling vector, `g(A)=sum b_i(A)^2`, `delta=||a_sorted-b(A)||_1`, and `f(A)=30-3A+A^2/10-g(A)/2`, then capped majorization and `|a_i^2-b_i^2|<=|a_i-b_i|/2` yield the explicit **conditional second-order bridge**

```
Q >= f(A)+delta^2/40
    +(sqrt([g(A)-delta/2-A^2/5]_+)-rho)_+^2/2.
```

Define `eta=sqrt(2 sum_i w_i^2 sin(theta_i)^2)`. If `eta<3/4`, the actual 20-column Q-synthesis map has rank 14, and for every coefficient vector c in its kernel,

`dist(c,W^(-1)ker(T0)) <= (4 eta/3)||c||`.

This follows by the singular-value gap `sigma_14(T0 W)>=3/4`, the perturbation bound `||T-T0W||_op<=eta`, and projection off the reference kernel.

## Proof status

**[PROVED EXACTLY]** All displayed algebraic and perturbation statements under their explicit hypotheses. An exact SymPy verifier checks the Gram spectrum, five independent cycles, weighted identities, and sharp rational cap witness.

**[OPEN]** No certified D5 labeling/angular error `rho` or `eta` for the residual Type-E branch. No uniform Type-E contradiction, no `A>383/504`, and no six-pairing/Q-kernel identification. Retain `M(F3)<=89`, matching `M(P)>=S/2-28/3`, `A<=383/504`. Types C, D, generic e>=27 and non-isolated branches remain open. **Global proved range: 40<=tau_5<=44.**
