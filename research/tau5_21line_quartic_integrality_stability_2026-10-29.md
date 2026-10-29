# A self-contained 21-line obstruction and quantitative quartic-defect floor in R^5

Date: 2026-10-29.

**[PROVED EXACTLY — standalone theorem]** For any 21 unit vectors y_0,...,y_20 in R^5, put x_ij=(y_i dot y_j)^2 and

    P = sum_{i<j} [ x_ij*(x_ij-1/4) ]_+.

Then **P > 1/120**. In particular, no 21 projective lines in R^5 have coherence <=1/2. This is an independent, self-contained proof of the zero-midpoint boundary, not a claim of D5 uniqueness.

## Exact harmonic identity

Set T=sum_i y_i y_i^T, V=||T-(21/5)I||_F^2, and f(t)=t^4-t^2/4. The normalized Gegenbauer polynomials for S^4 are

    P_2(t)=(5t^2-1)/4,
    P_4(t)=(21t^4-14t^2+1)/8.

The positive-coefficient identity is

    f(t)=1/28+(1/3)P_2(t)+(8/21)P_4(t).

By the spherical-harmonic addition theorem, sum_{i,j}P_4(y_i dot y_j)>=0. Direct expansion gives sum_{i,j}P_2(y_i dot y_j)=(5/4)V. Since 21^2/28=21*f(1)=63/4, the constant term cancels the diagonal. With N=sum_{i<j}[-f(y_i dot y_j)]_+,

    **P-N >= (5/24)V.**                                        (1)

If all off-diagonal |y_i dot y_j|<=1/2, then P=0. Equation (1) forces N=V=0, so T=(21/5)I and every x_ij is 0 or 1/4. But for each i,

    sum_{j != i} x_ij = y_i^T T y_i - 1 = 16/5,

which is not an integer multiple of 1/4. Contradiction.

## Quantitative integrality

For each x_ij in [0,1], round to its nearest r_ij in {0,1/4}. The following exact scalar bound holds:

    |x-r| <= 8[-x(x-1/4)]_+ + 4[x(x-1/4)]_+.

Indeed, for x<=1/4, min(x,1/4-x)<=8x(1/4-x), and for x>=1/4, x-1/4<=4x(x-1/4). If m pairs round to 1/4, then

    2*sum_{i<j} x_ij = tr(T^2)-21 = 336/5+V,
    2*sum_{i<j} r_ij = m/2.

Consequently,

    dist(336/5+V, (1/2)Z) <= 16N+8P <= 24P-(10/3)V.   (2)

If V>=1/20, (1) gives P>=1/96>1/120. If V<1/20, the nearest half-integer to 336/5+V is 67, at distance 1/5+V. Therefore

    **P >= 1/120+(13/72)V.**                              (3)

Strictness: P>0 by the boundary proof, and for any x>1/4 the scalar rounding bound is strict. Thus P>1/120 for all 21-line configurations.

## Conditional Type-E six-exception bridge

**[PROVED EXACTLY UNDER EXPLICIT TYPE-E ASSUMPTIONS]** Let z_0=v be the unit isolated-center direction, and z_1,...,z_20 the selected projected deep-edge directions, with squared norms b_i=1-a_i, 0<=a_i<=1/4. Put a_0=0, A=sum_{i=1}^{20}a_i, and A_C=sum a_i over the four F3 matching indices. Assume all 210 raw pairings satisfy |z_i dot z_j|<=1/2 except possibly the six pairs among the four core indices. Define normalized y_i=z_i/sqrt(b_i) and

    W_ij=z_i dot z_j,
    P_raw=sum_{i<j}[W_ij^2*(W_ij^2-1/4)]_+.

Only the six exceptional core pairings contribute to P_raw. Since b_i*b_j>=9/16, 1-b_i*b_j<=a_i+a_j, and

    x_ij*(x_ij-1/4)
      = [W_ij^2*(W_ij^2-1/4)+(1-b_i*b_j)*W_ij^2/4]
        /(b_i*b_j)^2,

each raw-safe pair contributes at most (16/81)(a_i+a_j) to normalized P. Each exceptional pair contributes at most (256/81)[W_ij^2*(W_ij^2-1/4)]_+ +(64/81)(a_i+a_j). There are twenty incidences per a_i among 210 pairs and three incidences per core a_i among the six K4 pairs. Summation gives

    P <= (256/81)P_raw + (320/81)A + (16/9)A_C.

Combining with the 21-line theorem yields the exact **strict six-exception bridge**

    **P_raw > 27/10240 - (5/4)A - (9/16)A_C.**          (4)

This translates a projective harmonic/integrality floor into six-exception raw quartic defect. If A<27/18560, at least one exceptional pair must have |W_ij|>1/2 (using A_C<=A). However at the retained Type-E cap A<=383/504, the right side can be negative: this does NOT eliminate Type E or improve its midpoint ceiling. The quartic defect defined here is not automatically the same normalization as the previously tracked raw/homogeneous defect; compare definitions before combining numerical bounds.

## Proof ledger

- **[PROVED EXACTLY]** Self-contained 21-line boundary exclusion, universal P>1/120, exact harmonic and rounding inequalities.
- **[CONDITIONAL TYPE E]** The bridge assumes the retained isolated-center 20-edge matching and six-exception raw-safety classification; upstream graph, mass, harmonic, and signed-Gram certificates are not re-audited.
- **[OPEN]** Need stronger weighted/integrality and 184 safe-Walsh control. Types C, D, E, generic e>=27 and non-isolated branches remain unresolved. Sparse e=23/e=24 classification is conditional on delta(G)>=1.
- **[GLOBAL PROVED RANGE UNCHANGED]** 40 <= tau_5 <= 44. Retain M(F3)<=89, matching M(P)>=S/2-28/3, and A<=383/504.
