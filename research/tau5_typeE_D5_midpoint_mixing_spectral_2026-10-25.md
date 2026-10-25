# Type E: exact D5 midpoint-mixing spectral gap (2026-10-25)

**Status:** [PROVED EXACTLY, rational linear algebra] the mixing inequality and the D5 spectral theorem below; [PROVED EXACTLY, finite rational enumeration] the four-core deletion diagnostic; [OPEN] Type E, global D5 labeling/stability, and tau_5. The attached detailed local research note and verifier are retained separately.

## Endpoint mixing: a term omitted by scalar projective bounds

For endpoints p_i^±=m_i±z_i, all four cross-endpoint inner products are <=1/2, **including core pairs**. Set t=z_i·z_j and sigma=sign(t), with sigma=+1 at t=0. Taking the two endpoint choices whose sign product is sigma gives

    m_i·m_j + |t| + |m_i·z_j + sigma z_i·m_j| <= 1/2.      (1)

The extra absolute-value term is linear in the midpoints. In particular, the six raw-projective exceptional core pairings do **not** permit us to discard (1): a deep contact is a negative inner product <-1/2, not an exception to the universal upper bound.

## Exact sharp D5 midpoint-mixing theorem

Take the 20 unit D5 line representatives v_pq^±=(e_p±e_q)/sqrt(2). There are exactly 120 contact pairs with |v_i·v_j|=1/2. For arbitrary m_i perpendicular to v_i, define

    c_ij=m_i·v_j+sign(v_i·v_j) v_i·m_j.

Then

    sum_{120 contacts} c_ij^2 >= sum_{i=1}^{20} ||m_i||^2.       (2)

**Sharp:** equality occurs on a 20-dimensional linear subspace.

**Exact certificate.** With integer roots r_i=e_p±e_q, build the 120x100 integer contact coefficient matrix B_c, and let P=diag(I_5-r_i r_i^T/2), the rank-80 rational projector onto the midpoint perpendicularity space. The normalized squared mixing operator is T=P B_c^T B_c P/2. Exact rational characteristic polynomial:

    X^20 (X-1)^20 (X-2)^10 (X-4)^10
      (X^2-13X/2+6)^5 (X^2-9X/2+4)^15.               (3)

The two quadratic factors have roots (13±sqrt(73))/4 and (9±sqrt(17))/4, all greater than 1. Thus the least positive eigenvalue is 1, proving (2). No floating-point eigensolver or assumed Type-E D5 labeling enters the proof.

## Four-core deletion diagnostic (not a valid Type-E relaxation)

For each of the binom(20,4)=4845 choices of four D5 core lines, *artificially* delete the contact mixing rows internal to the core, retaining all 20 perpendicularity equations and all other contact equations. The reduced system is injective for 4815 choices. Exactly 30 choices have a one-dimensional kernel: precisely those consisting of both sign lines on two coordinate supports sharing one coordinate.

This classification is certified by exact small rational determinants. If B is the full 140x100 integer matrix (20 perpendicularity rows +120 contact rows), B has rank 100. Deleting contact rows R loses rank exactly when det(I-R(B^T B)^(-1)R^T)=0. The determinant is at most 6x6; exhaustive exact enumeration gives 30 zeros, each of corank one.

For a representative core v_12^±,v_13^±, an explicit six-line A2 mode is m_12^+=e_3, m_12^-=-e_3, m_13^+=e_2, m_13^-=-e_2, m_23^+=-e_1, m_23^-=e_1, all others zero. It violates only the four deleted core contact equations.

**Warning:** This A2 mode is an artifact of deleting valid endpoint inequalities. It is not a feasible Type-E infinitesimal motion. It is also not an identification of the six Q-kernel relations with six exceptional pairings.

## Next step

Combine the full signed endpoint inequality (1), not just m_i·m_j+|z_i·z_j|<=1/2, with a perturbation-stable version of the spectral gap (2), frame-operator variance and A<=383/504. The D5 spectral theorem is conditional on a D5 template; no unconditional Type-E contradiction follows.

**Unchanged:** 40<=tau_5<=44. Type E retains M(F3)<=89, M(P)>=S/2-28/3 and A<=383/504. Types C,D, generic e>=27 and non-isolated branches remain open. Sparse e=23/24 classification requires delta(G)>=1.
