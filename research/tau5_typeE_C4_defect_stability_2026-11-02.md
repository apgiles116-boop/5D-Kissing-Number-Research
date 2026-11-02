# Type E: canonical F3 defect-support rigidity and exact C4 variance (2026-11-02)

**[PROVED EXACTLY — standalone midpoint-graph and sum-of-squares lemmas].** **[CONDITIONAL — canonical Type-E matching, previously retained harmonic/mass, singleton and Q-frame certificates]** for the numerical conclusions. **[OPEN]** No Type-E exclusion. Global proved range **40 <= tau_5 <= 44**.

## Setup

For the four selected canonical F3 deep edges, let `m_0,...,m_3` be midpoints, `a_i=||m_i||^2`, `C=sum a_i`, `d_ij=z_i.z_j`, and `delta_ij=(|d_ij|-1/2)_+`. All six quotient pairings have exactly one deep cross-contact. The previously proved endpoint lemmas imply, for each positive defect,

    delta_ij <= -m_i.m_j,
    delta_ij <= f(a_i+a_j),   f(t)=t(1-t)/2,
    delta_ij <= 1/8.

Let `E={ij:delta_ij>0}` and `D=sum_E delta_ij`. The numerical corollary additionally retains the stronger isolated-center harmonic certificate `C<=A<567/1000`. This certificate is **not** reproved here.

## 1. New weighted-paw sum of squares [PROVED EXACTLY]

Suppose `E` is a paw: triangle edges 01,02,12 and pendant edge 23. Put `c_ij=m_i.m_j`. Let `W` be the weighted adjacency matrix with weight `sqrt(2)` on triangle edge 01 and weight 1 on the other three edges:

    W = [[0,sqrt(2),1,0],
         [sqrt(2),0,1,0],
         [1,1,0,1],
         [0,0,1,0]].

Its characteristic polynomial is

    (lambda+sqrt(2))^2
    (lambda-sqrt(2)-1)(lambda-sqrt(2)+1).

More directly, `W+sqrt(2) I` has the explicit vector sum of squares

    <m,(W+sqrt(2)I)m>
       = sqrt(2)||m_0+m_1+m_2/sqrt(2)||^2
         + (1/sqrt(2))||m_2+sqrt(2)m_3||^2 >=0.

Thus

    D <= -sum_{ij in E}c_ij
      <= C/sqrt(2) + (sqrt(2)-1)c_01
         - (1/2)<m,(W+sqrt(2)I)m>.

Since `c_01<=-delta_01<0`, we obtain the **incidence-sensitive stability inequality**

    D + (sqrt(2)-1)delta_01
      + (1/2)<m,(W+sqrt(2)I)m> <= C/sqrt(2).    (1)

In particular, every paw support satisfies `D<C/sqrt(2)`. This replaces the earlier paw spectral coefficient `3703/5000` by the smaller exact coefficient `1/sqrt(2)`, using the required sign of a triangle edge. The old unconstrained spectral certificate remains valid but is no longer optimal for this application.

## 2. Exact four-cycle variance [PROVED EXACTLY]

If `E` is the cycle 01,12,23,30, summing the mass-sensitive singleton inequality yields the identity

    D <= sum_{ij in E} f(a_i+a_j)
       = C(1-C/2)
         - [(a_0-a_2)^2+(a_1-a_3)^2]/2.          (2)

The last two squares give a **second-order mass-imbalance penalty**. Near the maximum, the two opposite midpoint masses on each side of the cycle must be nearly equal.

## 3. All support patterns [PROVED EXACTLY]

- `|E|<=3`: `D<=3/8` from the singleton cap.
- `|E|=4`: the support is either C4, covered by (2), or a paw, covered by (1).
- `|E|=5`: relabel the missing edge as 01. Set `X=m_0+m_1`, `Y=m_2+m_3`; since 23 is positive-defect, `c_23<0`. The exact identity

      C/sqrt(2)+X.Y+c_23
       = (||X+sqrt(2)Y||^2+||m_0-m_1||^2)/(2sqrt(2))
         -(sqrt(2)-1)c_23 >=0

  proves `D<=C/sqrt(2)` (with an additional positive penalty for `delta_23`).
- `|E|=6`: `D<=(C-||sum_i m_i||^2)/2<=C/2`.

These cases do not require D5 labeling or uniqueness.

## 4. Stronger canonical Type-E consequences [CONDITIONAL]

With `C<567/1000`, the preceding bounds imply

    D_raw < max{3/8, (567/1000)/sqrt(2),
                (567/1000)(1-567/2000)}
          = 812511/2000000 = 0.4062555.        (3)

The equality of the maximum with the C4 term follows from exact rational comparisons (and `2*401^2>567^2`). This improves the previous canonical bound `2099601/5000000=0.4199202` and the retained general bound `1780062775/4032758016`.

**High-defect rigidity.** If `D_raw>=401/1000`, then `D_raw>C/sqrt(2)` and `D_raw>3/8`, so **the positive-defect support must be a C4**. Moreover (2) forces

    C >= 1-sqrt(99/500) > 0.555,

and gives the explicit variance budget

    (a_0-a_2)^2+(a_1-a_3)^2
      <= 2[C(1-C/2)-D_raw].                     (4)

This is a necessary structural condition, not a contradiction.

**Safe projected squared-correlation transfer.** Retain the upstream conditional `C_z=sum_{i<j}(z_i.z_j)^2>28.3626`. For six singleton exception caps `1/8`, convex concentration and (3) give

    sum_exception delta_ij^2
       < 3/64+(812511/2000000-3/8)^2
       = 191407625121/4000000000000.

Since `d_ij^2 <= 1/4+delta_ij+delta_ij^2`, the 184 fully safe pairings satisfy

    sum_safe (z_i.z_j)^2
       > 105633970374879/4000000000000
       = 26.40849259371975.                    (5)

The integer threshold remains **at least 43 of 184 safe pairings with |d_ij|>1/3**; (5) does not yet force 44.

## Proof-status and next step

**[PROVED EXACTLY]** Weighted paw PSD/SOS, the signed improvement, the C4 variance identity, support classification, and five-edge identity.

**[VERIFIED EXACT ARITHMETIC]** Companion SymPy/Fraction script checks all identities, eigenvalues, graph cases and rational margins.

**[CONDITIONAL]** (3)-(5) retain the earlier canonical F3 incidence, singleton endpoint theorem, `A<567/1000` harmonic certificate, and `C_z>28.3626` Q-frame certificate. They are not new unconditional global kissing-number bounds.

**[OPEN]** Type E remains open; alternative-selected matchings have a double-contact pairing and are not covered by (3). Types C, D, generic `e>=27`, and non-isolated branches remain open. The sparse `e=23/24` classification still assumes `delta(G)>=1`. Preserve `M(F3)<=89`, `M(P)>=S/2-28/3`, `A<=383/504`, and the Musin/Boyvalenkov zero-midpoint boundary theorem.

**Next target:** use (4) and the signed Walsh constraints to exclude near-equal C4 midpoint masses or force a quantitative `Q`-frame energy loss; separately analyze alternative F3 double-contact supports. No identification of the six exceptional pairings with the six D5 Q-kernel modes is asserted.

Verifier: `research/tau5_typeE_C4_defect_stability_2026-11-02_verify.py`.
