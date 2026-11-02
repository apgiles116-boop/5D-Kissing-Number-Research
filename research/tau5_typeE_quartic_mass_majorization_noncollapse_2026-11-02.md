# Type E: capped-midpoint majorization and sharper quartic frame noncollapse

Date: 2026-11-02. **Global proved range unchanged: 40 <= tau_5 <= 44.**

## Proof status

**[PROVED EXACTLY — universal]** The fourth-moment majorization lemma and rational polynomial estimates below.

**[CONDITIONAL TYPE-E]** For a *canonical F3 selected matching satisfying* A <= 383/504 and the six singleton exceptional-pair conditions, the frame operator Z = sum_i z_i z_i^T has lambda_min(Z) > 3/10. With the retained global raw defect ceiling it has lambda_min(Z) > 673/2000; with the canonical path-only support and defect ceiling it has lambda_min(Z) > 461/1250 = 0.3688. These are necessary conditions, not an exclusion. The proof does not establish that the mass-selected Type-E matching must be canonical.

## 1. Four-dimensional quartic harmonic input

For arbitrary y_i in R^4, let t_i = ||y_i||^2 and s_ij = y_i.y_j. The exact Gegenbauer-positive polynomial (3/8)u^2(4u^2-1) = (3/32)P0 + (9/16)P2 + (15/32)P4 gives

    sum_(i<j) s_ij^2(4s_ij^2-t_i t_j)
      >= (sum_i t_i^2)^2/8 - (3/2)sum_i t_i^4.         (1)

## 2. New majorization lemma

Let a_i in [0,1/4], e_i >= 0, A=sum a_i<1, E=sum e_i, b_i=a_i+e_i <= 1 and t_i=1-b_i. Put k=floor(4A), r=A-k/4. For k>=1, the vector

    b*=(E+1/4, [1/4 repeated k-1 times], r, 0,...,0)

majorizes b in descending order: the sum of the j largest b_i is at most E+min(A,j/4), exactly the partial sum of b* until total A+E is reached. For k=0 use b*=(A+E,0,...,0). Convexity of (1-b)^4 and Karamata imply, for 20 vectors,

    sum_i t_i^4 <= U(A,E),

    U=19+(1-A-E)^4                              if k=0,
    U=19-k+(k-1)(3/4)^4+(1-r)^4+(3/4-E)^4      if k>=1.   (2)

For a unit x in R^5, put c_i=x.z_i, e_i=c_i^2, E=x^TZx, y_i=z_i-c_i*x. Then y_i lie in R^4 and t_i=1-a_i-e_i. Since sum t_i=20-A-E, (1)-(2) give the lower polynomial

    Rcap(A,E)=(20-A-E)^4/3200-(3/2)U(A,E).             (3)

On 0<=A<=A0=383/504 and 0<=E<=461/1250, Rcap is decreasing in A,E. Indeed each partial derivative of U is in [-4,0], while (20-A-E)^3/800 > 18^3/800 > 6. At A0, k=3 and r=5/504:

    R0(E)=(20-A0-E)^4/3200
      -(3/2)[16+2(3/4)^4+(499/504)^4+(3/4-E)^4].     (4)

## 3. Exact quartic upper polynomials

Set u_ij=|c_i c_j|, B_ij=a_i+a_j+e_i+e_j+4u_ij+4u_ij^2, delta_ij=(|z_i.z_j|-1/2)_+, D=sum delta_ij, q=(5+4E)^2/64. The singleton cap delta<=1/8 implies

    4s_ij^2-t_i t_j <= B_ij+(9/2+4E)delta_ij.         (5)

Safe pairs satisfy s_ij^2 <= 1/4+(1+E/2)u_ij; defective pairs satisfy s_ij^2<=q.

The conservative six-core upper polynomial from the previous rank-four certificate is

    Lsix=(19A+57E+2E^2)/4
       +(1+E/2)[(9/4)AE+(17/4)E^2+E^3]
       +(q-1/4)(3A+9E+2E^2)
       +q(9/2+4E)D.                                   (6)

For canonical path-only support, sharper exact sums give

    sum_all B_ij <=19A+57E+(19/10)E^2,
    sum_all u_ij B_ij <=(109/50)AE+(102/25)E^2+E^3/2,
    sum_defect B_ij <=2A+(21/4)E+E^2.                 (7)

Proof: sum u^2 <=19E^2/40. Also u^3 <= e_i e_j(e_i+e_j)/2, hence sum u^3<=E^3/8. The mixed sum uses sqrt(19)/2<109/50. The defect support is a subgraph of P4: maximum degree two, bipartite, adjacency spectral radius <=(1+sqrt5)/2<13/8, so sum_defect u<=13E/16 and sum_defect u^2<=E^2/4.

Consequently

    Lpath=(19A+57E+(19/10)E^2)/4
      +(1+E/2)[(109/50)AE+(102/25)E^2+E^3/2]
      +(q-1/4)[2A+(21/4)E+E^2]
      +q(9/2+4E)D.                                   (8)

Both Lsix and Lpath are coefficientwise nondecreasing in A,E,D.

## 4. Exact contradiction gaps

For any E<=E0, the harmonic inequality requires R0(E0)<=L(A0,E0,D0). Exact rational subtraction instead yields:

| Assumptions | E0 | Positive gap R0-L |
|---|---|---|
| Six exceptions, D<=3/4; Lsix | 3/10 | 50930070610356481/129048256512000000 |
| Retained D<=1780062775/4032758016; Lsix | 673/2000 | 670796742034030475489/89616844800000000000000 |
| Canonical path-only D<366383/1016064; Lpath | 461/1250 | 113450575137045459617281/31505922000000000000000000 |

Thus lambda_min(Z) exceeds the respective E0, conditional on the listed upstream Type-E hypotheses. The exact checker verifies these gaps and all polynomial monotonicities.

## 5. Further research

For a minimum-frame eigenvector x, the *signed* identity

    sum_(i<j) c_i c_j (z_i.z_j)
       = [E^2-E+sum_i a_i e_i]/2                      (9)

follows by expanding x^T Z^2 x=E^2. This is not used in the current upper polynomial and may provide a sharper cut.

**[OPEN]** No Type-E elimination or proof that A>383/504. The alternative matching double-positive branch, Type C, Type D, generic e>=27 and non-isolated cases remain open. The endpoint-Perron argument remains withdrawn. The stronger center-sensitive Q-total certificate is not used. Preserve M(F3)<=89, matching S/2-28/3, 20-edge mass >=2137/6, and the audited Musin/Boyvalenkov zero-midpoint boundary theorem.

Verifier: research/verify_typeE_quartic_mass_majorization_noncollapse_2026_11_02.py.
