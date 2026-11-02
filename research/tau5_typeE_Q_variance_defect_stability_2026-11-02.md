# Type E: five-to-four Q-frame variance splitting and defect-sensitive stability

**Date:** 2026-11-02. **Global proved range unchanged: 40 <= tau_5 <= 44.**

## Status

**[PROVED EXACTLY — universal algebra]** The five-dimensional frame variance splits into an eigenvalue term, a signed mixed-moment term, and a four-dimensional traceless-frame term.

**[RETAINED, NOT NEW]** The cap-improved global correlation floor P >= 8790283/317520 was already established in the earlier 2026-11-02 forest-mass work.

**[PROVED EXACTLY — CONDITIONAL TYPE E]** Six-exception bounds give a spectral/correlation-count dichotomy. A canonical three-singleton-defect path with raw defect D >= 1/3 has a further exact second-order Q-floor penalty of 1/252.

**[OPEN]** No Type-E exclusion, no A > 383/504 contradiction, and no new global kissing-number bound.

## 1. Exact five-to-four sum-of-squares identity

Let z_1,...,z_20 be vectors in R^5, t_i=||z_i||^2=1-a_i, A=sum a_i, T=20-A, Z=sum z_i z_i^T and P=sum_{i<j}(z_i.z_j)^2. Put Q_i=z_i z_i^T-(t_i/5)I_5.

The trace identity is exact:

$$
P=30-3A+\frac{A^2}{10}-\frac12\sum_i a_i^2
+\frac12\left\|Z-\frac T5 I_5\right\|_F^2. \tag{1}
$$

For any unit x, write c_i=x.z_i, y_i=z_i-c_i x, E=sum c_i^2, U=sum c_i y_i, and Y=sum y_i y_i^T acting on x-perp. Then Z has blocks [E,U^T;U,Y] and tr Y=T-E. Orthogonality of its scalar and traceless blocks proves

$$
\left\|Z-\frac T5 I_5\right\|_F^2
=\frac{(T-5E)^2}{20}
+2\|U\|^2
+\left\|Y-\frac{T-E}{4}I_4\right\|_F^2. \tag{2}
$$

Thus the exact **second-order stability identity** is

$$
\boxed{
P=30-3A+\frac{A^2}{10}-\frac12\sum_i a_i^2
+\frac{(T-5E)^2}{40}
+\|U\|^2
+\frac12\left\|Y-\frac{T-E}{4}I_4\right\|_F^2.
} \tag{3}
$$

Equality in the directional variance lower bound holds exactly when x is a frame eigenvector (U=0) and Y is scalar on x-perp. The signed and four-dimensional residuals are explicitly

$$
\sum_{i<j}c_i c_j(z_i.z_j)
=\frac{E^2-E+\sum_i a_i c_i^2+\|U\|^2}{2}, \tag{4}
$$

$$
\left\|Y-\frac{T-E}{4}I_4\right\|_F^2
=\sum_i\|y_i\|^4+2\sum_{i<j}(y_i.y_j)^2-\frac{(T-E)^2}{4}. \tag{5}
$$

For a frame eigenvector U=0 in (4). The U^2 term must NOT be dropped for an arbitrary x.

## 2. Six-exception quantitative tradeoff

Assume the retained Type-E matching hypotheses: 0<=a_i<1/4, A<=A0=383/504, at most six possibly exceptional projected pairings, and raw positive defect D=sum delta_ij with delta_ij=(|z_i.z_j|-1/2)_+.

Capped mass majorization gives sum a_i^2<=3/16+(5/504)^2=47653/254016. The scalar part of (3) is minimized at A=A0, giving the **previously retained** P0=8790283/317520. Consequently, if E=x^T Z x <=E0<=(20-A0)/5,

$$
P\ge P_0+\frac{(20-A_0-5E_0)^2}{40}. \tag{6}
$$

The six exceptional squares sum to at most 3/2+D+H, H=sum delta_ij^2. For 0<=delta_ij<=c and D<=D0, convex concentration yields

$$
H\le k c^2+(D_0-kc)^2,\quad k=\lfloor D_0/c\rfloor. \tag{7}
$$

The other 184 pairings are safe. If K of them have |z_i.z_j|>1/3, their total squared correlation is at most 184/9+5K/36.

Exact rational comparisons from (6)-(7) give the following **conditional** results:

| Matching branch | If lambda_min(Z)<=1/2 | If lambda_min(Z)<=1 |
|---|---:|---:|
| General mass-selected, D0=1780062775/4032758016, c=1/4 | K>=88 | K>=74 |
| Canonical singleton path-only, D0=366383/1016064, c=1/8 | K>=89 | K>=75 |

For E0=1/2 the positive gaps against K=87 and K=88 are respectively

- 1978091112988045103/16263137215612256256 (general);
- 123066464351/1032386052096 (canonical path).

These are dichotomies, not unconditional high-correlation counts. Previous noncollapse bounds >0.3372 and >0.4298 do not rule out the lambda_min<=1/2 branch.

## 3. Exact midpoint-spread penalty in a high-defect canonical path

Assume three positive singleton defects on a four-vertex path, each <=1/8 and each <=sqrt(a_i a_j) at its incident core vertices. If D>=1/3, then each edge defect is at least D-1/4>=1/12. Since each a_j<1/4, **all four core masses** satisfy a_i>1/36.

Let r=5/504 and b=1/36. Because the largest three masses leave at least one of four core masses outside them, their sum is strictly less than A0-b. Along with the individual cap, the entire twenty-mass vector is strictly majorized by

(1/4, 1/4, A0-1/2-b, b, 0,...,0).

Hence

$$
\sum_i a_i^2 < \frac18+(A_0-\frac12-b)^2+b^2.
$$

The loss relative to the unrestricted capped maximum factors exactly:

$$
\left(\frac3{16}+r^2\right)
-\left(\frac18+(A_0-\frac12-b)^2+b^2\right)
=(b-r)(\frac12-2b)=\frac1{126}.
$$

By (3), this produces the strict additional **1/252**:

$$
\boxed{
P>\frac{8791543}{317520}
+\frac{(T-5E)^2}{40}+\|U\|^2
+\frac12\left\|Y-\frac{T-E}{4}I_4\right\|_F^2.
} \tag{8}
$$

More generally, b(D)=4(D-1/4)^2 gives a penalty (b(D)-5/504)(1/4-b(D)) whenever 5/504<=b(D)<=(A0-1/2)/2. On 1/3<=D<366383/1016064 the penalty increases with D and is at least 1/252.

## 4. Next step and limits

Equations (3)-(5) give a concrete interface between the global Q-floor, signed Walsh correlations, and the previous four-dimensional quartic Gegenbauer argument. The next finite polynomial/KKT step is to retain the six individual exceptional correlations and both nonnegative residuals instead of discarding them.

All statements about Type E remain conditional on the retained exact graph and mass lemmas, including M(F3)<=89, M(P)>=S/2-28/3 and A<=383/504. No D5 kernel/exception bijection is asserted. The withdrawn endpoint-Perron argument is not used. Types C, D, generic e>=27, and non-isolated branches remain open. Global 40<=tau_5<=44.

**Verifier:** research/verify_typeE_Q_variance_defect_stability_2026_11_02.py
