# Type E: exact D5 Q-spectrum, isolated-center separation, and F3 matching sharpness (2026-10-14)

**Status: PROVED EXACTLY** for the three lemmas below, under the stated model assumptions. **NOT a Type E elimination.** Preserve the global range `40 <= tau_5 <= 44`, the Type E `M(F3)<=89`, matching `M(P)>=S/2-28/3`, and midpoint energy `A<=383/504`.

## Lemma 1: D5 traceless-projector spectrum [PROVED EXACTLY]

For the 20 D5 projective lines `v_ij^±=(e_i±e_j)/sqrt(2)` in R5, put `Q_i=v_i v_i^T-I/5`. The 20-by-20 Q-Gram has exact eigenvalues

`3/2 (multiplicity 4), 1 (multiplicity 10), 0 (multiplicity 6)`.

Proof: pass to symmetric/antisymmetric ± combinations. The ten antisymmetric columns are an orthonormal basis of off-diagonal symmetric matrices, giving eigenvalue 1. The ten symmetric columns are `(E_ii+E_jj-2I/5)/sqrt(2)`; their Gram is `(1/2)B^T B-(2/5)J` for the unsigned vertex-edge incidence matrix B of K5. Since `BB^T=3I+J`, this sector has eigenvalues `3/2^4,0^6`. The nullspace is the global constant edge weighting plus five independent alternating four-cycle relations, for cycles (0123),(0124),(0134),(0234),(1234). Smallest positive eigenvalue is exactly 1.

For vectors z_i aligned with v_i, with `||z_i||<=1`, set `d^2=sum||z_i-v_i||^2` and `T e_i=z_i z_i^T-(||z_i||^2/5)I`. Then `||T-T0||op<=2d`. If `d<1/2`, `rank T=14`, `nullity T=6`, and its nonzero singular values are >= `1-2d`. For `c in ker T`, `dist(c,ker T0)<=2d||c||`; for `c in ker T0`, `dist(c,ker T)<=2d/(1-2d)||c||`. These are **conditional on a justified D5 alignment**, not evidence of one.

## Lemma 2: quantitative isolated-center D5 exclusion [PROVED EXACTLY]

For any unit u in R5, define `t_i=|u·v_i|` and `s4=sum_{k=1}^5 u_k^4`. Direct expansion gives `sum t_i^2=4`, `sum t_i^4=(3+s4)/2`, `1/5<=s4<=1`. Therefore `max_i t_i >=sqrt(2/5)>1/2` (sharp for uniform-coordinate u).

More strongly, with `delta_i=(t_i-1/2)_+`, put `E=sum t_i^2(t_i^2-1/4)=(1+s4)/2`. Discard negative terms, use `t+1/2<=3/2` on positive terms, then Cauchy-Schwarz:

`E <= (3/2)(sum t_i^4)^(1/2)(sum delta_i^2)^(1/2)`.

Thus `sum delta_i^2 >= 2(1+s4)^2/[9(3+s4)] >=1/10`.

If 20 vectors z_i admit a unit u with `|u·z_i|<=1/2` for every i, then **for every** rotated, signed, relabeled D5 template v_i,

`sum_i ||z_i-v_i||^2 >= 1/10`.

In Type E with an isolated deep-graph center x0, the nondeep endpoint contacts imply `|x0·z_i|<=1/2`, so this forbidden D5 neighborhood applies. **No global D5 proximity theorem has been proved, so this is not a contradiction.** A stronger value `13/2-2sqrt(10)` for the optimal sum of squared exceedances is suggested numerically but is **UNPROVED**.

## Lemma 3: matching loss 28/3 is sharp for abstract F3 mass constraints [PROVED EXACTLY]

Label F3 edges `02,04,05,14,17,23,27,36,56,57`. Its three perfect matchings are `{02,14,36,57}`, `{04,17,23,56}`, and `{05,14,27,36}`.

Assign abstract masses `M(02)=M(05)=M(27)=M(57)=28/3`, `M(04)=M(17)=M(23)=M(56)=14/3`, `M(14)=M(36)=0`. Then `S=56<=89`; every incident star has mass <=70/3; even the optional incident two-edge cap 343/16 is satisfied. Yet all three perfect matchings have mass 56/3, so

`S/2-max_P M(P)=28/3`.

Together with the inherited guarantee `max_P M(P)>=S/2-28/3`, this proves **sharpness for the abstract mass relaxation**. The witness is not claimed geometrically realizable. Improving the matching theorem requires genuinely additional geometric or mass-coupling constraints.

## Research priority [OPEN]

Bridge the D5 spectral/center separation to the six-exception defect and midpoint-energy bounds by proving a quantitative D5 alignment/contact-labeling lemma or deriving a center-sensitive bound that does not assume alignment. Type C, D, E, generic e>=27, and the minimum-degree dependency remain open.
