# Type E / F3: twelve exact near-cap realizations — local-only cap-envelope limitation

Date: 2026-10-29.

**[PROVED EXACTLY — FINITE RATIONAL CERTIFICATES]** Twelve explicit eight-vector configurations in R^5 satisfy the *exact* strict F3 deep graph, including both bounds on every nonedge. A standard-library Python verifier checks every assertion using rational arithmetic.

**[NEGATIVE RESULT FOR A PROPOSED PROOF ROUTE]** Local F3 incidence constraints alone permit more than 99.9% of the scalar capped-simplex fourth-moment envelope in every matching/exceptional-position pattern. A Type-E contradiction must exploit the other sixteen selected edges, the isolated center, or a global cross-pair/frame argument. These examples are not Type-E codes.

## Exact statement

Use the canonical F3 edges `02,04,05,14,17,23,27,36,56,57` and perfect matchings

- `P1 = 02|14|36|57`
- `P2 = 04|17|23|56`
- `P3 = 05|14|27|36`.

For a matched pair define `a_ij=(1+u_i·u_j)/2`, `A_core=sum a_ij`, and `U_core=sum a_ij^2`.

For **each** of the twelve choices of matching and one distinguished matched edge, there are eight rational unit vectors in R^5 with:

1. Every F3 edge strictly deep: `u_i·u_j < -1/2`.
2. All eighteen nonedges strictly safe: `-1/2 < u_i·u_j < 1/2`.
3. The distinguished matching energy in `(99/10000,1/100)`.
4. Each other matching energy in `(1249/5000,1/4)`.
5. `759/1000 < A_core < 383/504`.
6. `U_core > 4686/25000 = 0.18744`.

The scalar envelope at `A*=383/504` is
`U*=3/16+(5/504)^2=47653/254016≈0.1875984189972`.
An exact rational comparison yields `4686/25000 > (999/1000)U*`. Thus all twelve local configurations exceed 99.9% of this scalar maximum.

## Explicit rational construction

Each JSON certificate contains eight four-integer rows `b=(b1,b2,b3,b4)` and denominator `D=100000`. Put `t=b/D` and map to the unit sphere by inverse stereographic projection:

`u(t)=(2t1/(1+||t||^2),...,2t4/(1+||t||^2),(1-||t||^2)/(1+||t||^2))`.

Every coordinate is rational and `||u(t)||=1` identically. The verifier checks all 28 endpoint pairs, both safe bounds, all matching energies, A, and U with `fractions.Fraction`; no floating-point tolerance enters the proof. The committed data were also fetched back and independently verified using BigInt rational arithmetic: all 12 passed, with every endpoint inequality strict.

## Proof-status implications

**[PROVED EXACTLY]** The twelve finite rational configurations. In particular, an F3-only upper bound `U_core <= U* - c` valid for all `A_core<=A*` cannot have `c >= U* - 4686/25000 ≈ 0.000158419`. A smaller F3-only penalty remains possible.

**[NOT PROVED]** No extension to the 32 endpoints of `16K2` or to an isolated center. The examples need not satisfy the 184 safe Walsh blocks, the global Q-frame inequality, harmonic/mass constraints, or the Type-E matching-selection theorem. They do not establish sharpness of the cap envelope for a full Type-E code.

**[NEXT]** Use these twelve exact witnesses as adversarial inputs for any proposed F3-only concentration argument, and target a genuinely global 184-block/frame incompatibility. The conditional center-critical and 13+1+6 estimates still require independent recertification of upstream certificates.

**[RETAINED]** Star sum<=70/3; broom M(F3)<=89; matching M(P)>=S/2-28/3; twenty-edge mass>=2137/6; A<=383/504; source-audited zero-midpoint exclusion. No regression to older constants.

**[GLOBAL PROVED RANGE — UNCHANGED]** `40 <= tau_5 <= 44`. Types C, D, generic e>=27, and non-isolated branches remain open.

## Files

- [Exact rational witness data](tau5_typeE_F3_all_12_near_cap_witnesses_2026-10-29.json)
- [Standalone exact verifier](tau5_typeE_F3_all_12_near_cap_exact_verifier_2026-10-29.py)
