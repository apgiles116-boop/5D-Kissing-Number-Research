# Type E: sharp singleton mass-defect inequality and canonical F3 spectral improvement (2026-11-02)

**[PROVED EXACTLY — standalone local endpoint and four-midpoint graph lemmas].** **[CONDITIONAL ON RETAINED TYPE-E HARMONIC/MASS/Q CERTIFICATES]** Numerical consequences. **[OPEN]** No Type-E exclusion. Global proved range **40 <= tau_5 <= 44**.

## 1. Sharp singleton-contact mass-defect theorem [PROVED EXACTLY]

Two selected deep edges have unit endpoints u_i^+ = m_i + z_i, u_i^- = m_i - z_i and likewise for j, with m_i.z_i = m_j.z_j = 0 and a_i = ||m_i||^2 < 1/4, a_j = ||m_j||^2 < 1/4. Suppose exactly one of their four cross-endpoint contacts is deep (inner product < -1/2), while the other three are two-sided safe in [-1/2,1/2]. Set t = a_i + a_j < 1/2 and delta = (|z_i.z_j| - 1/2)_+.

**Exact sharp inequality:**

    delta <= t(1-t)/2.                                       (1)

For delta > 0, t >= (1-sqrt(1-8*delta))/2.

**Proof.** Reorient so the unique deep cross contact is u_i^+.u_j^+ < -1/2. If delta > 0, then d = z_i.z_j = -1/2-delta: if d > 1/2, the average of the two opposite-sign contacts would be below -1/2, creating another deep contact. Put c = m_i.m_j = -k. Averaging the upper bounds on the two opposite-sign contacts gives c-d <= 1/2, hence k >= delta. The safe -- contact gives p+q <= -(k+delta), where p=m_i.z_j and q=z_i.m_j.

With X=m_i+m_j and Y=z_i+z_j, orthogonality within each selected edge gives

    ||X||^2 = t-2k,
    ||Y||^2 = 1-t-2delta,
    |X.Y| = |p+q| >= k+delta.

Cauchy-Schwarz therefore yields

    (t-2k)(1-t-2delta) >= (k+delta)^2.

Both factors on the left are nonnegative. Since k>=delta, we obtain

    (t-2delta)(1-t-2delta) >= 4delta^2,

equivalently t(1-t)>=2delta, proving (1).

**Sharp local witness.** For any 0<t<1/2, set b=t/2 and delta=t(1-t)/2. In Gram order (m_i,z_i,m_j,z_j), take diagonal (b,1-b,b,1-b), within-edge m.z=0, and cross correlations c=p=q=-delta, d=-1/2-delta. Its symmetric/antisymmetric 2-by-2 blocks are

    Bplus  = (1/2)*[[t^2, -t(1-t)], [-t(1-t), (1-t)^2]],
    Bminus = [[t(2-t)/2, delta], [delta, (3-t^2)/2]].

Bplus is PSD rank one, while Bminus has positive diagonal and determinant t(3-2t)/2 > 0. The four cross-endpoint contacts are -1/2-4delta, -1/2, 1/2, 1/2; both selected-edge contacts are t-1 < -1/2. Hence (1) is sharp for the local four-endpoint problem, **not** asserted sharp for a full F3 or Type-E configuration.

## 2. Four-core support-pattern lemma [PROVED EXACTLY]

For four midpoint vectors m_0,...,m_3, write C=sum_i ||m_i||^2, E={ij:delta_ij>0}, D=sum_E delta_ij. Assume every positive-defect pairing has a singleton cross deep contact (canonical F3 pattern). The universal endpoint upper bound gives delta_ij<=-m_i.m_j on E.

- |E|<=3: D<3/8 by the strict singleton cap.
- |E|=4, graph C4: D<=C(1-C/2). Use (1), concavity of f(t)=t(1-t)/2, and sum_(ij in E)(a_i+a_j)=2C.
- |E|=4, triangle plus pendant: D<=(3703/5000)*C. For edges 01,02,12,23, the adjacency matrix B has B+(3703/2500)*I positive definite. Its four rational leading principal minors are 3703/2500, 7462209/6250000, 12595059927/15625000000, 700659681/39062500000000. The PSD quadratic form gives -sum_E m_i.m_j <= (3703/5000)*C.
- |E|=5: D<=C/sqrt(2). Relabel so 01 is the missing edge and 23 is present. With X=m_0+m_1, Y=m_2+m_3, c23=m_2.m_3<0, the following is an exact nonnegative sum-of-squares identity:

      C/sqrt(2)+X.Y+c23
       = (||X+sqrt(2)*Y||^2+||m_0-m_1||^2)/(2sqrt(2))
          -(sqrt(2)-1)*c23 >= 0.

  Because D<=-X.Y-c23, this proves the claim.
- |E|=6: D<=C/2, since -sum_(i<j)m_i.m_j=(C-||sum_i m_i||^2)/2.

Every four-edge simple graph on four vertices is C4 or triangle plus pendant. These are exact vector identities, with no D5 labeling or generic SDP.

## 3. Canonical F3 consequence [CONDITIONAL]

For the canonical matching P0=04|17|23|56, all six quotient pairings have one deep cross contact. **Retain additionally** the previously certified isolated-center harmonic/mass theorem A<0.566926<567/1000; that upstream theorem is not independently reproved here. Then C=A_C<=A<567/1000.

The five cases above, checked with rational comparisons, imply

    D_raw < 2099601/5000000 = 0.4199202.                    (2)

The triangle-plus-pendant case is the largest. This improves the retained global raw-defect ceiling 1780062775/4032758016 = 0.4414008398... by approximately 4.87%, **only in the canonical-selected F3 branch**. Alternative F3 matchings have a double-contact pairing and are not covered by (2).

**[FURTHER CONDITIONAL]** With the retained projected Q-frame floor C_z=sum_(i<j)(z_i.z_j)^2 > 28.3626, the six singleton caps and convex concentration give sum_core(delta_ij^2) < 3/64 + (Dstar-3/8)^2, where Dstar=2099601/5000000. Therefore the 184 fully safe projected pairings satisfy

    sum_safe (z_i.z_j)^2
      > 659844674390799/25000000000000
      = 26.39378697563196.                                 (3)

This improves the previous canonical floor 26.369914907199. It still forces only at least 43 of 184 safe pairings to have |z_i.z_j|>1/3 under this particular Q input.

## Proof status and next step

**[PROVED EXACTLY]** (1), its PSD sharpness witness, the support-pattern case analysis, rational spectral certificate, and five-edge SOS identity. **[CONDITIONAL]** (2)-(3) use retained upstream Type-E harmonic/mass, F3 incidence, and Q-frame certificates. **[OPEN]** Type E remains unresolved, as do Types C, D, generic e>=27, and non-isolated branches. Sparse e=23/24 classification requires delta(G)>=1.

Preserve star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, baseline A<=383/504, and the audited Musin/Boyvalenkov zero-midpoint exclusion. Global proved range **40<=tau_5<=44**.

Next: insert the local mass-sensitive bound (1) into the alternative-selected double-contact finite polynomial/KKT problem and the global Walsh/Q-frame budget. No six-exception/D5 Q-kernel identification is proved.

Exact checker: research/tau5_typeE_singleton_mass_cycle_spectral_2026-11-02_verify.py.
