# Type E / F3: exact exclusion of one canonical three-defect path orbit

**Date:** 2026-11-02.

**[PROVED EXACTLY — standalone eight-endpoint theorem]** For the canonical F3 perfect matching, the three positive-defect quotient edges cannot be 01,12,23 simultaneously. An explicit finite integer Gram/Farkas certificate excludes this pattern even in the weak-contact, unrestricted-rank relaxation. Exact F3 automorphisms transfer it to **four of the twelve** labeled three-edge paths. The remaining two four-path orbits are **not** eliminated here.

**[CONDITIONAL TYPE-E CONSEQUENCE]** Combined with separately retained triangle-free, four-cycle-exclusion, and canonical star-exclusion lemmas, any canonical positive-defect support with three edges must lie in one of **two remaining path orbits**. Zero-, one-, and two-edge supports are not eliminated. Type E remains open; the proved global range is `40 <= tau_5 <= 44`.

## 1. Eight-endpoint setup

Take eight unit vectors `u_0,...,u_7`. Their ten strict-deep endpoint pairs (inner product `< -1/2`) are

    02,04,05,14,17,23,27,36,56,57.

Every other endpoint pair is safe (inner product in `[-1/2,1/2]`). Orient the canonical selected matching as

    (A0,B0)=(u0,u4), (A1,B1)=(u7,u1),
    (A2,B2)=(u2,u3), (A3,B3)=(u5,u6),
    w_i=(A_i-B_i)/2.

Each cross-matching quotient pair has exactly one strict deep *same-sign* contact. As in the independently retained switching lemma, any positive projective defect must have `w_i.w_j < -1/2`, rather than `>+1/2`. Thus the path support 01,12,23 would imply

    w0.w1 <= -1/2, w1.w2 <= -1/2, w2.w3 <= -1/2.  (P)

We exclude even these weak inequalities without using a midpoint-energy cap or a rank-five assumption.

## 2. Exact integer Farkas/Gram certificate

Write `x_ij=u_i.u_j` for `i<j`. After multiplying by four, all constraints take the form `A_k.x <= b_k`:

- Deep pair `ij`: `4*x_ij <= -2`.
- Safe pair `ij`: `4*x_ij <= 2` and `-4*x_ij <= 2`.
- Quotient path pair `ij`: `x_(A_i,A_j)-x_(A_i,B_j)-x_(B_i,A_j)+x_(B_i,B_j) <= -2`.
- Gram PSD, for any integer `v in Z^8`: `-8*sum_(i<j) v_i*v_j*x_ij <= 4*sum_i v_i^2`. Its slack is `4*||sum_i v_i*u_i||^2 >= 0`.

The self-contained verifier lists **29 inequalities** (16 endpoint constraints, three path constraints, and ten integer-vector Gram sum-of-squares constraints) and **29 strictly positive integer multipliers** `lambda_k`. Exact integer arithmetic establishes

    sum_k lambda_k*A_k = 0        (all 28 coefficients vanish)
    sum_k lambda_k*b_k = -12164187608516934784.

Consequently the weighted sum of nonnegative slacks would satisfy

    sum_k lambda_k*(b_k-A_k.x)
      = -12164187608516934784 < 0.                  (CERT)

This is impossible. Therefore the path 01,12,23 is excluded. Floating-point linear optimization was used to discover the certificate, **not** to validate it. The independent verifier checks every integer coefficient, multiplier sign, and the negative constant using no third-party libraries.

The integer multipliers are large (up to 21 decimal digits); the complete reproducible certificate is in the companion Python verifier rather than repeated in the prose.

## 3. Automorphism transfer

The F3 deep graph has eight automorphisms preserving the four *oriented* canonical matched pairs. Their quotient action partitions the twelve unoriented Hamiltonian paths on four quotient vertices into three orbits of four. The excluded orbit is

    (0,1,2,3), (0,1,3,2), (1,0,2,3), (1,0,3,2).

Each path is identified with its reversal. All four are excluded by exact relabeling of (CERT). The **two unresolved path orbits** are represented by

    (0,2,1,3)  and  (0,2,3,1).

They are *not* claimed feasible.

## 4. Proof ledger

**[PROVED EXACTLY]** The 29-term integer Farkas certificate, standalone 01,12,23 exclusion, and exact four-path automorphism transfer. This excludes the pattern even for weak deep inequalities and arbitrary ambient dimension.

**[CONDITIONAL ON RETAINED LEMMAS]** Combining with the previously proved triangle-free, C4-exclusion, and canonical star-exclusion results leaves two canonical three-defect path orbits. The scalar ceiling `D_raw < 366383/1016064` is **unchanged** by this orbit exclusion.

**[OPEN]** The two remaining canonical path orbits, zero-/one-/two-defect supports, both alternative F3 matchings (especially double-positive cases), rank-five coupling to sixteen isolated deep edges, Types C/D, generic `e>=27`, and non-isolated branches.

**[RETAINED, NOT REPROVED HERE]** `M(F3)<=89`, `M(P)>=S/2-28/3`, twenty-edge mass `>=2137/6`, `A<=383/504`, the audited Musin/Boyvalenkov antipodal boundary theorem, and the universal Q-frame inequality. The withdrawn endpoint-Perron argument is not used.

**Next:** seek exact certificates for the two remaining canonical path orbits, or an obstruction involving rank five and the sixteen isolated edges.

**Verifier:** `research/verify_typeE_F3_path_orbit_exact_Farkas_2026_11_02.py`.
