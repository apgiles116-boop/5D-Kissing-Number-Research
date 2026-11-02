# Type E: F3 switching forbids triangular exceptional supports (2026-11-02)

**[PROVED EXACTLY — standalone eight-endpoint F3 theorem]** under the specified ten strict deep contacts and eighteen two-sided-safe nonedges. **[CONDITIONAL]** Numerical Type-E consequences retain upstream harmonic, raw-defect and Q-frame certificates. **[OPEN]** Type E is not excluded. Global proved range remains 40 <= tau_5 <= 44.

## 1. Exact all-matching triangle obstruction

F3 deep-contact graph: 02,04,05,14,17,23,27,36,56,57. Its perfect matchings are
P0=(04),(17),(23),(56);
P1=(02),(14),(36),(57);
P2=(05),(14),(27),(36).

For each matched edge write unit endpoints u_i^±=m_i±z_i, a_i=||m_i||²<1/4, ||z_i||²=1-a_i. For a quotient pair with a strict deep cross-contact (sigma,tau), put s_ij=sigma*tau, c_ij=m_i·m_j, d_ij=z_i·z_j. The partner (-sigma,-tau) contact is <=1/2 and the deep contact is <-1/2, so c_ij+s_ij d_ij<0. Since c_ij>=-sqrt(a_i a_j)>-1/4, whenever |d_ij|>1/2 one necessarily has s_ij d_ij<-1/2.

Exact incidence, using first endpoint as + in the displayed matching order:

| Matching | Cross-deep multiplicities on 01,02,03,12,13,23 | Switching g |
|---|---|---|
| P0 | 1,1,1,1,1,1 | (1,-1,1,1) |
| P1 | 1,1,2,0,1,1 | (1,-1,-1,1) |
| P2 | 1,2,1,1,0,1 | (1,-1,1,1) |

Every quotient pair with deep contacts has a common s_ij=g_i g_j; in particular, both deep contacts of a double pair have the same product. Zero-deep pairs are fully safe and have |d_ij|<=1/2. Switching w_i=g_i z_i therefore gives w_i·w_j=-1/2-delta_ij whenever delta_ij=(|d_ij|-1/2)_+>0.

If three positive defects formed a triangle, then

0<=||w_i+w_j+w_k||²
 = (3-a_i-a_j-a_k)-3-2(delta_ij+delta_jk+delta_ik)<0,

a contradiction. **The positive-defect support is triangle-free for all three F3 perfect matchings.** It has at most four edges, and four edges force a C4. In P1/P2 the four singleton-contact quotient pairs form this C4, and the double-contact pair is a diagonal. Hence a positive double-contact defect can coexist with at most TWO positive singleton defects. Paw, five-edge and six-edge positive-defect supports are impossible in the canonical branch (previous bounds on them were conservative, not false).

No D5 labeling, Q-kernel correspondence, or D5 uniqueness is assumed.

## 2. New joint linear/quadratic canonical budget

**[PROVED EXACTLY under the retained singleton-contact mass-defect theorem and explicit harmonic cap]** Suppose C=sum_(four core)||m_i||²<=A<567/1000=:cstar. Retain delta_ij<=f(a_i+a_j), f(t)=t(1-t)/2, and the strict singleton cap delta<1/8.

For the only possible four-edge support, C4=(01,12,23,30), the edge sums t_e=a_i+a_j lie in [0,1/2] and satisfy t_01+t_23=t_12+t_30=C. The exact variance identity gives D=sum delta_e<=C(1-C/2)-[(a0-a2)²+(a1-a3)²]/2. A new joint quadratic estimate is

sum delta_e² <= cstar²(1-cstar/2)²/4.

Proof: f(t)² is increasing for 0<=t<=1/2. Enlarge the four masses (each at most 1/4) until their sum is cstar; this cannot decrease the bound and is always possible since total capacity is 1. Put q(t)=t²(1-t)²/4. For x+y=cstar, x,y<=1/2, h=x-cstar/2,

2q(cstar/2)-q(x)-q(y)
 = h²[-3cstar²+6cstar-2-2h²]/4 >=0,

because |h|<=(1-cstar)/2 and the bracket is >=687577/2000000>0. Apply to the two opposite-edge pairs. With Dstar=cstar(1-cstar/2)=812511/2000000,

D+sum delta² <= Dstar+Dstar²/4
 = 7160262125121/16000000000000
 = 0.4475163828200625...

If there are at most three positive singleton defects, the strict cap instead gives D+sum delta²<27/64=0.421875, so the displayed joint budget holds for EVERY canonical support. This strengthens the previous independent-defect concentration budget.

## 3. Conditional Q-frame transfer and exact gap

For six possibly exceptional core pairings, d_ij²<=1/4+delta_ij+delta_ij². Hence Q6<=3/2+0.4475163828200625...

**[FURTHER CONDITIONAL]** Retaining the independently established center-sensitive Q_total=sum_(i<j)(z_i·z_j)²>28.3626 gives for the 184 fully safe pairs

Qsafe > 422641337874879/16000000000000
      = 26.41508361717994...

This still forces at least 43, not 44, safe pairs with |z_i·z_j|>1/3. Since k such pairs can contribute at most 184/9+5k/36, the precise Q_total threshold to force 44 by this route is

Q_total > 1361480786375363/48000000000000
        = 28.36418304948673...

The retained 28.3626 certificate is short by exactly
75986375363/48000000000000 = 0.001583049486729... .
A joint signed-Walsh/Q-frame variance or opposite-safe-pair penalty is the next target, not a claimed contradiction.

## 4. Alternative-selected double-contact budget

**[PROVED EXACTLY conditional on the retained raw-defect ceiling]** If the double-contact pair has positive defect, triangle-freeness permits at most two positive singleton defects. Their caps are (1/4,1/8,1/8). With D<=D0=1780062775/4032758016 and 3/8<D0<1/2, convex concentration yields

D+sum delta² <= D0+5/64+(D0-3/8)²
 = 8520825355071995281/16263137215612256256
 = 0.523934911333847...

If the double defect vanishes, the four singleton edges are a C4 and the smaller canonical-style budget applies IF the stronger C<567/1000 certificate is valid for that selected matching. This is not asserted to supersede all prior alternative-matching bounds.

## Proof ledger

**[PROVED EXACTLY]** F3 sign switching, all-matching triangle-free exceptional support, alternative double-positive cardinality, exact C4 polynomial quadratic budget under its explicit mass cap.

**[VERIFIED EXACT ARITHMETIC]** Companion Python/SymPy/Fraction checker enumerates the three F3 quotient incidences and verifies the polynomial identity, rational comparisons and thresholds. The geometric contradiction is analytic.

**[CONDITIONAL]** Numerical Type-E corollaries use retained singleton endpoint, harmonic A<567/1000, raw-defect, and Q_total>28.3626 certificates where specified; these upstream proofs are not re-established here.

**[OPEN]** Type E, C, D, generic e>=27 and non-isolated branches. The e=23/24 sparse classification assumes delta(G)>=1. Preserve star <=70/3, M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, baseline A<=383/504, and Musin/Boyvalenkov's 21-line zero-midpoint exclusion. Global 40<=tau_5<=44 unchanged.

Verifier: research/tau5_typeE_F3_triangle_free_defect_support_2026-11-02_verify.py.
