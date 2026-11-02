# Type E: sharp singleton mass-defect inequality and canonical F3 spectral improvement (2026-11-02)

**[PROVED EXACTLY — standalone local four-endpoint theorem and four-midpoint graph inequalities].** **[CONDITIONAL ON RETAINED TYPE-E HARMONIC/MASS/Q CERTIFICATES]** The canonical numerical bounds. **[OPEN]** No Type-E exclusion; global proved range remains **40 <= tau_5 <= 44**.

## 1. Sharp local singleton-contact theorem [PROVED EXACTLY]

Let two selected deep edges have unit endpoints (u_i^pm=m_ipm z_i), (u_j^pm=m_jpm z_j), with (m_icdot z_i=m_jcdot z_j=0), (a_i=|m_i|^2<1/4), (a_j=|m_j|^2<1/4). Suppose exactly one of the four cross-endpoint contacts is deep (dot product below (-1/2)); the other three are two-sided safe in ([-1/2,1/2]). Define (t=a_i+a_j<1/2), (delta=(|z_icdot z_j|-1/2)_+). Then

[
oxed{deltale 	frac12t(1-t).} 	ag{1}
]

For (delta>0), this implies (tge(1-sqrt{1-8delta})/2).

**Proof.** Reorient so the unique deep cross contact is (u_i^+cdot u_j^+<-1/2). If (delta>0), necessarily (d=z_icdot z_j=-1/2-delta): if (d>1/2), the average of the two opposite-sign contacts would be below (-1/2), creating a second deep contact. Set (c=m_icdot m_j=-k). Averaging the upper bounds on the two opposite-sign contacts gives (c-dle1/2), hence (kgedelta). The safe (--) contact gives (p+qle-(k+delta)), where (p=m_icdot z_j), (q=z_icdot m_j). With (X=m_i+m_j), (Y=z_i+z_j), we have (|X|^2=t-2k), (|Y|^2=1-t-2delta), and (|Xcdot Y|=|p+q|ge k+delta). Cauchy-Schwarz yields

[
(t-2k)(1-t-2delta)ge(k+delta)^2.
]

Both factors on the left are nonnegative, and (kgedelta); therefore ((t-2delta)(1-t-2delta)ge4delta^2), equivalent to (1).

**Sharp local witness.** For (0<t<1/2), put (b=t/2), (delta=t(1-t)/2) and take the four-vector Gram in order ((m_i,z_i,m_j,z_j)) with diagonal (b,1-b,b,1-b), within-edge (mcdot z=0), and all four cross correlations (c=p=q=-delta), (d=-1/2-delta). Its symmetric/antisymmetric (2	imes2) blocks are

[
rac12egin{pmatrix}t^2&-t(1-t)\\-t(1-t)&(1-t)^2end{pmatrix},qquad
egin{pmatrix}t(2-t)/2&delta\\delta&(3-t^2)/2end{pmatrix}.
]

The first is PSD of rank one; the second has positive diagonal and determinant (t(3-2t)/2>0). The four cross endpoint contacts are (-1/2-4delta,-1/2,1/2,1/2); both selected-edge contacts are (t-1<-1/2). Thus (1) is sharp for local feasibility, **not** asserted sharp for a complete F3 configuration.

## 2. Four-core support-pattern theorem [PROVED EXACTLY]

For four core midpoint vectors (m_0,ldots,m_3), write (C=sum|m_i|^2), (E={ij:delta_{ij}>0}), (D=sum_Edelta_{ij}). Assume every positive-defect pair is a singleton cross-contact, as in the canonical F3 matching. The endpoint upper bound gives (delta_{ij}le-m_icdot m_j) on (E). Exhausting simple graphs on four vertices:

- (|E|le3): (D<3/8) by the strict singleton (1/8) cap.
- (|E|=4), cycle (C_4): (Dle C(1-C/2)), by (1), concavity of (f(t)=t(1-t)/2), and (sum_{ijin E}(a_i+a_j)=2C).
- (|E|=4), triangle plus pendant: (Dle(3703/5000)C). For the graph with edges (01,02,12,23), the adjacency matrix (B) has (B+(3703/2500)Isucc0), certified by rational leading principal minors (3703/2500, 7462209/6250000, 12595059927/15625000000, 700659681/39062500000000). Thus (-sum_E m_icdot m_jle(3703/5000)C).
- (|E|=5): (Dle C/sqrt2). Relabel so (01) is missing and (23) is present. Set (X=m_0+m_1), (Y=m_2+m_3), (c_{23}=m_2cdot m_3<0). The exact identity
[
C/sqrt2+Xcdot Y+c_{23}
=rac{|X+sqrt2Y|^2+|m_0-m_1|^2}{2sqrt2}-(sqrt2-1)c_{23}ge0
]
proves the bound.
- (|E|=6): (Dle C/2) from (-sum_{i<j}m_icdot m_j=(C-|sum m_i|^2)/2).

The two four-edge types exhaust all four-edge graphs on four vertices. No D5 labeling or generic SDP is assumed.

## 3. Canonical F3 consequence [CONDITIONAL]

For the canonical matching (P_0=04|17|23|56), the six quotient pairings each have one deep cross contact. **Retain additionally** the earlier isolated-center harmonic/mass bound (A<0.566926<567/1000); it is **not independently re-established here**. Then (C=A_Cle A<567/1000). Comparing the five cases with exact rational arithmetic yields

[
oxed{D_{m raw}<rac{2099601}{5000000}=0.4199202.} 	ag{2}
]

The largest case is the triangle-plus-pendant bound. This improves the retained global raw-defect ceiling (1780062775/4032758016approx0.44140084) by approximately 4.87%, **only for the canonical-selected F3 branch**. Alternative-selected F3 matchings contain a double-contact pairing and are not covered by (2).

**[FURTHER CONDITIONAL]** Retain the Q-frame projected squared-correlation floor (C_z>28.3626). With six singleton caps, convex concentration gives (sum_{m core}delta_{ij}^2<3/64+(D_*-3/8)^2), where (D_*=2099601/5000000). Hence the 184 safe pairings satisfy

[
oxed{sum_{m safe}(z_icdot z_j)^2>
rac{659844674390799}{25000000000000}
=26.39378697563196.} 	ag{3}
]

This improves the previous canonical floor (26.369914907199) but still forces only at least 43 safe pairings with (|z_icdot z_j|>1/3) under this particular Q input.

## Status

**[PROVED EXACTLY]** (1), its local PSD sharpness witness, the graph-support case bounds, the rational spectral certificate, and the five-edge SOS identity. **[CONDITIONAL]** (2)–(3) depend on retained upstream Type-E harmonic/mass and Q-frame certificates. **[OPEN]** No Type-E elimination. Types C, D, generic (ege27), and non-isolated branches remain open. Sparse (e=23/24) classification requires (delta(G)ge1). Preserve star (le70/3), broom (M(F3)le89), matching (M(P)ge S/2-28/3), selected mass (ge2137/6), baseline (Ale383/504), and the audited Musin/Boyvalenkov zero-midpoint exclusion. **Global proved range (40le	au_5le44).**

Verifier: `research/tau5_typeE_singleton_mass_cycle_spectral_2026-11-02_verify.py`.
