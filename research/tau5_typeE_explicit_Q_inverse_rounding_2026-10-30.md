# Type E: explicit inverse Q-kernel rounding and positive residual floor
Date: 2026-10-30

**[PROVED EXACTLY — universal inverse theorem; conditional Type-E consequence]**

For 20 **unit** directions `u_{pq}^+,u_{pq}^-` labeled by the ten edges `pq` of `K5`, let
`S_pq=u_+u_+^T+u_-u_-^T`, `F=sum S_pq`,
`O=sum_pq (u_+·u_-)^2`,
`V=||F-4I||_F^2`,
`C=tr(P_c K)>=0`, where `K` is the Gram matrix of the traceless projectors `Q_i=u_i u_i^T-I/5` and `P_c` is the exact rank-five D5 support-cycle kernel projector. Put
`rho^2=2C+V/10`, `delta=sqrt(3)(2 sqrt(O)+5rho+rho^2)`, and `h=rho+22delta`.

**Inverse theorem.** If `h<1/10`, there is an orthonormal basis `b_1,...,b_5` and, on each support `pq`, an orthonormal pair `f_pq^+,f_pq^-` spanning `span(b_p,b_q)`, with
`max_i ||u_i u_i^T-f_i f_i^T||_F <5h`.
This rounds to the **full ten-angle support-plane fibre**, not necessarily the rigid D5 roots.

## Proof

Set
`B_p=(1/3)sum_{q!=p}S_pq-(2/15)F+I/5`.
The exact K5 incidence identities give `sum B_p=I`, `tr B_p=1`, and, with `E_pq=S_pq-B_p-B_q`,
`sum ||E_pq||_F^2=rho^2`.
The previously established exact projector-defect inequality gives
`Delta=(sum ||B_p^2-B_p||_F^2)^(1/2)<=delta`.

If `h<1/10`, then `delta<1/220`. Spectrally round each real symmetric `B_p` to a 0/1 projector `R_p`: for every real lambda and nearest `r in {0,1}`,
`|lambda-r|<=2|lambda(lambda-1)|`.
Thus `||B_p-R_p||_F<=2delta`. Since `tr B_p=1`, the integer `rank R_p` differs from one by less than `2sqrt(5)delta<1`; hence `rank R_p=1`.

Choose unit columns `r_p` for `R_p`, and form the 5-by-5 matrix `T=[r_1 ... r_5]`. Then
`||TT^T-I||_F<=sum ||R_p-B_p||_F<=2sqrt(5)delta<1`,
so `T` is invertible. Its orthogonal polar factor `W` obeys
`||T-W||_F<=||T^TT-I||_F=||TT^T-I||_F<=2sqrt(5)delta`.
Let `P_p=b_p b_p^T` for the columns of `W`. The unit-projector inequality `||rr^T-bb^T||_F<=2||r-b||` yields
`||B_p-P_p||_F< (2+4sqrt(5))delta<11delta`.
Therefore
`||S_pq-(P_p+P_q)||_F<=rho+22delta=h`.

Fix a support, abbreviate `S=uu^T+vv^T` and `P=P_p+P_q`. With `t=u·v`, the eigenvalues of `S` are `1+|t|,1-|t|,0,0,0`; Hoffman-Wielandt gives `sqrt(2)|t|<=h`. If `Pi` is the projector onto `span(u,v)`, then `||Pi-S||_F=sqrt(2)|t|<=h` and `||Pi-P||_F<=2h`.

Gram-Schmidt produces `G=[u,(v-tu)/sqrt(1-t^2)]` with `||v-G_2||<=h`. Put `Z=PG`, `L=G^T(I-P)G`. Then `L>=0` and `tr L=||Pi-P||_F^2/2<=2h^2<1`. The two-column polar factor `H=Z(Z^TZ)^(-1/2)` lies in `range(P)` and is orthonormal. Its singular-value estimate gives
`||G-Z||_F<=sqrt(2)h`, `||Z-H||_F<=tr L<=2h^2`, so `||G-H||_F<2h`. Hence `||u-H_1||<2h`, `||v-H_2||<3h`. Since `||xx^T-yy^T||_F<=sqrt(2)||x-y||` for unit vectors, the projective distance is less than `3sqrt(2)h<5h`. QED.

## Type-E corollary

**[PROVED CONDITIONALLY]** Label the four Type-E core directions on four star supports, the other 16 arbitrarily. The separately verified exact 2026-10-30 interval theorem excludes every admissible Type-E configuration within projective Frobenius distance `1/650` of **any** such support-plane fibre. Thus the inverse theorem forces `h>=1/3250` (also trivial if `h>=1/10`).

If `rho<=1`, the rational inequalities `sqrt(3)<7/4`, `rho^2<=rho` yield
`h<=77sqrt(O)+232rho<=sqrt(59753)sqrt(O+rho^2)<245sqrt(O+rho^2)`.
Since `245*3250=796250`, this proves
`O+2C+V/10>1/(796250^2)`.
For `rho>1`, the same conclusion is immediate.

**[OPEN]** This positive residual floor is far too small to contradict `A<=383/504`. It does not imply a positive lower bound on `C+V` alone: `O` may be nonzero. A sharp Walsh/energy upper bound on this combined residual is still missing. The six exceptional pairings have **not** been identified with the six Q-kernel relations.

**[RETAINED]** Global `40<=tau_5<=44`; `M(F3)<=89`; selected-edge mass `>=2137/6`; `A<=383/504`; Types C, D, generic e>=27 and non-isolated branches open. Sparse e=23/24 graph classification requires `delta(G)>=1`.


## Exact sanity check: the global squared-correlation mass does not imply D5 proximity

**[PROVED EXACTLY — counterexample to a tempting inference, NOT to Type E]**
Let `v=(1,1,1,1,1)/sqrt(5)`, and let `H_0=I` and
`H_k=I-2q_k q_k^T/(q_k·q_k)` for
`q_1=(1,2,3,4,-10)`, `q_2=(2,3,4,5,-14)`,
`q_3=(3,4,5,6,-18)`. Take the 20 unit directions
`u_{kj}=H_k e_j` for `k=0,1,2,3` and `j=1,...,5`.
Each `H_k` is rational orthogonal and fixes `v`, so
`sum_i u_i u_i^T=4I`,
`sum_{i<j}(u_i·u_j)^2=30`, and
`|v·u_i|^2=1/5<=1/3` for every i.
Exact rational comparison verifies that all 20 projective lines are distinct.
Nevertheless only 154 of the 190 line pairs have `|u_i·u_j|<=1/2`;
the other 36 violate that threshold.

Thus **even exact equality with the D5 total squared-correlation mass 30,
together with a center satisfying the normalized contact cap, does not force
D5 alignment**. This is not an admissible Type-E example, precisely because
the 184-safe/six-exception Walsh incidence fails. It explains why the inverse
theorem must retain local cycle and within-support information rather than
rely on the global frame floor alone.
