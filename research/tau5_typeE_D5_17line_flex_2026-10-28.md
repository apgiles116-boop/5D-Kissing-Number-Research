# Exact finite-flex theorem for every 17-line D5 subsystem (2026-10-28)

**[PROVED EXACTLY — D5 TEMPLATE THEOREM]** Every 17-line subset of the 20 projective root lines of D5 admits a noncongruent continuous deformation that retains coherence at most 1/2. In particular **no 17-line D5 subset is locally rigid as a projective spherical code**. The result is proved by seven Weyl-orbit representatives and an integer Bernstein-polynomial certificate for every one of the 136 pairs in each representative.

**[TYPE-E APPLICATION CONDITIONAL]** The previous high-center branch classified the *rounded* center-plus-16-isolated-direction Gram as 17 D5 lines, conditional on its upstream mass/harmonic/rounding certificates. This theorem shows that the rounded 17-line subsystem **alone** cannot be treated as infinitesimally rigid. A Type-E obstruction must use the remaining four F3 matched directions, their deep endpoint contacts, or additional second-order constraints. It does not weaken the rigorous zero-midpoint 21-line exclusion.

## 1. Seven orbits of omitted triples

Order the 20 integer roots `x_ij^±=e_i±e_j` lexicographically by support `0<=i<j<5`, taking the minus sign before the plus sign. Their normalized projective representatives are `x/sqrt(2)`. The Weyl action by coordinate permutations and even sign changes (1920 actions on projective root lines) partitions the `C(20,3)=1140` omitted triples into exactly seven orbits:

| Missing root indices (0-based) | Orbit size | Sparse integral velocity witness on the sorted 17 retained roots |
|---|---:|---|
| (0,1,2) | 120 | `v[5]=(1,0,0,0,0)` |
| (0,1,14) | 60 | `v[0]=v[1]=(0,-1,0,0,0)`; `v[6]=v[7]=(1,0,0,0,0)` |
| (0,2,4) | 160 | `v[6]=(-1,0,0,0,0)` |
| (0,2,8) | 40 | `v[0]=(0,0,-1,0,0)` |
| (0,2,9) | 40 | `v[0]=(0,0,1,0,0)`; `v[1]=(0,-1,0,0,0)`; `v[6]=(1,0,0,0,0)` |
| (0,2,10) | 480 | `v[7]=(-1,0,0,0,0)` |
| (0,2,18) | 240 | `v[7]=(-1,0,0,0,0)` |

All unspecified velocities vanish. Every witness is tangent: `x_i·v_i=0`.

## 2. A finite deformation, not just a tangent-cone calculation

For each orbit representative define

```
y_i(t) = (x_i+t*v_i)/||x_i+t*v_i||,    0 <= t <= 1/10.
```

For each retained pair `i<j`, form the exact integer quartic

```
P_ij(t) = ||x_i+t*v_i||^2 ||x_j+t*v_j||^2
          -4*((x_i+t*v_i)·(x_j+t*v_j))^2.
```

Then `P_ij(t)>=0` is precisely `|y_i(t)·y_j(t)|<=1/2`. Write `P_ij(t)=sum_{k=0}^4 p_k*t^k` and substitute `s=10t`. Its degree-four Bernstein coefficients on `0<=s<=1` are

```
b_j = sum_{k=0}^j p_k * binom(j,k)/(binom(4,k)*10^k),   0<=j<=4.
```

The scaled coefficients `12*10^4*b_j` are **integers**. The companion verifier checks that **all five are nonnegative for all 136 pairs in each of the seven representatives**, using only Python integer arithmetic. As Bernstein basis functions are nonnegative on `[0,1]`, all the required quartics are nonnegative throughout the full interval, not merely at sampled values.

The verifier also checks that at least one pairwise Gram entry has a nonzero first derivative for each representative. Hence the deformation is not a common orthogonal motion or a relabeling for sufficiently small positive `t`. In five orbits one or two active `|inner product|=1/2` contacts strictly relax at first order; in the other two, an originally orthogonal pairing changes at first order while all active contacts have zero first derivative.

**[PROVED EXACTLY]** All 1140 possible omitted triples are covered by the seven Weyl orbits, so every 17-line D5 subset is flexible.

## 3. What this rules out as a proof strategy

The infinitesimal rigidity of the **full 20-line D5 configuration** cannot be inherited automatically by deleting three lines. In fact the exact 17-line subsystem admits genuine finite deformations while retaining the projective threshold. Therefore a proposed inequality claiming the true 17-line Gram must be exactly its rounded D5 Gram, or must have a positive first-order rigidity modulus solely from those 17 contacts, would be false.

This does **not** invalidate the previous rounded Gram rank/PSD/D5 classification, the 17-line Q-kernel rank 13/14 calculation, or the perturbative Gram-kernel bounds. It identifies a genuine missing ingredient: the F3 core, the six exceptional pairings, and/or a higher-order stress certificate coupling the full 21-direction system.

## 4. Status

- **[PROVED EXACTLY]** Seven omitted-triple Weyl orbits; seven explicit integral deformation witnesses; all 952 pairwise quartic Bernstein certificates (7×136) nonnegative on the full interval; noncongruence near zero.
- **[CONDITIONAL]** Relevance to Type E requires the retained high-center proof that its rounded 17-line Gram is D5. The deformed root lines are not asserted to realize the full 41-point code.
- **[OPEN]** Type E (high and low center), Types C/D, generic e>=27, and non-isolated branches. No bound stronger than 40<=tau_5<=44 is claimed. Retain M(F3)<=89, M(P)>=S/2-28/3 and A<=383/504.

Verifier: [tau5_typeE_D5_17line_flex_2026-10-28_verify.py](tau5_typeE_D5_17line_flex_2026-10-28_verify.py).
