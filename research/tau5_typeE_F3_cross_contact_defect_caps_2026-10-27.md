> **2026-10-27 strengthening / proof-ledger correction:** The later [F3 signed-triangle theorem](tau5_typeE_F3_signed_triangle_caps_2026-10-27.md) proves the sharper one-cross cap d<1/8, the zero-cross equality d=0, and forbids every fully active quotient triangle. Hence at most four core pairings can be exceptional. The bounds below remain valid but are superseded by P2 quartic <=0.18751144325156904 and P1/P3 <=0.25342941200156904. In particular the six-active F3 branches are impossible, so their numerical bounds below are conditional/vacuous for actual F3 configurations.

# Type E: exact F3 cross-contact defect caps from near-antipodal stability

Date: 2026-10-27.

**[PROVED EXACTLY — graph-sensitive, conditional on the retained Type-E F3 structure]** Every selected F3 matching has strict, nonuniform per-pair raw correlation-excess caps. These improve the earlier uniform quartic positive-defect envelope without a new SDP or a D5 labeling.

**[OPEN]** No Type-E elimination. The actual projected/midpoint rank-five geometry, sixteen outside edges and 184 safe-pair mixing remain to be combined.

## 1. Universal near-antipodal endpoint lemma

For two selected deep edges, write endpoints p_i^sigma=m_i+sigma z_i and p_j^tau=m_j+tau z_j, with a_i=||m_i||^2<=1/4, ||z_i||^2=1-a_i and m_i.z_i=0. All four cross-endpoint inner products are <=1/2. Put

d=(|z_i.z_j|-1/2)_+>0, s=sign(z_i.z_j), epsilon=1/4-d.

The endpoint sign lemma gives m_i.m_j<=-d. Using -m_i.m_j<=sqrt(a_i a_j)<=1/4 and a_i+a_j>=2d gives

||m_i+m_j||^2<=2epsilon,
||z_i-s z_j||^2<=4epsilon.

For the two disjoint cross-endpoint pairs (p_i^sigma,p_j^(-sigma*s)), sigma=+1,-1, their vector sums are M+/-D, where M=m_i+m_j and D=z_i-s z_j. Hence

||M+/-D|| <= (sqrt(2)+2)sqrt(epsilon),       (1)

and

(||M+D||^2+||M-D||^2)/2=||M||^2+||D||^2<=6epsilon. (2)

A cross pair which is NOT a deep edge has inner product >-1/2, hence squared sum norm >1. Therefore:

- **At most one deep cross-contact between the two selected edges:** at least one of the two antipodal-candidate cross pairs is a nonedge. From (1), epsilon>1/(6+4sqrt(2))=3/2-sqrt(2), so

  **d < c := sqrt(2)-5/4 = 0.164213562373... .**

- **No deep cross-contacts:** both candidate pairs are nonedges. From (2), epsilon>1/6, so

  **d < 1/12 = 0.083333333333... .**

- **Two disjoint deep cross-contacts:** the universal individual cap d<=1/4 remains possible; the preceding argument gives no stronger bound.

These strict inequalities also apply at d=0 trivially (as non-strict upper bounds). They require only the actual deep/nondeep adjacency and the kissing inequalities, not a Gram numerical optimization.

## 2. Exact F3 matching adjacency classification

Use the retained labeled F3 edge set

02, 04, 05, 14, 17, 23, 27, 36, 56, 57.

Its three perfect matchings are

P1={02,14,36,57}, P2={04,17,23,56}, P3={05,14,27,36}.

Count deep edges crossing between each unordered pair of selected matching edges:

- P2: all six pairs have exactly **one** deep cross-contact. Therefore all six defects satisfy d<c.
- P1: pair (14,36) has **zero** cross-contacts, pair (02,57) has **two disjoint** cross-contacts, and the other four pairs have **one** each.
- P3: pair (14,36) has **zero** cross-contacts, pair (05,27) has **two disjoint** cross-contacts, and the other four pairs have **one** each.

The unique four-cycle of F3 is 0-2-7-5-0. The only core pairs capable of attaining the extreme d=1/4 are therefore (02,57) in P1 or (05,27) in P3. No pair in P2 can attain it.

Thus the six per-pair caps, sorted decreasingly, are:

P1/P3: (1/4, c, c, c, c, 1/12);
P2:    (c, c, c, c, c, c).

## 3. Exact improved quartic positive-defect envelopes

**[PROVED EXACTLY — conditional Type E]**

Retain the independent exact linear excess certificate

D0=1780062775/4032758016,  sum_{six core pairs} d_ij <= D0.

This D0 bounds the *linear* raw excess sum, not the quartic weighted defect. Let

f(d)=(1/2+d)^2(d+d^2),    P_fixed=sum_{six core pairs} f(d_ij).

The function f is strictly increasing and convex on [0,1/4], with f(0)=0. Under a total excess cap and heterogeneous individual caps, the vector obtained by filling the largest individual caps first majorizes every admissible defect vector; hence it maximizes sum f.

Since 2c<D0<3c and 1/4+c<D0<1/4+2c, we obtain

**For P2:**

P_fixed <= 2 f(c)+f(D0-2c)
        = 0.21593308080901114... .                 (3)

**For P1 or P3:**

P_fixed <= f(1/4)+f(c)+f(D0-1/4-c)
        = 0.26788731675926734... .                 (4)

These improve the earlier uniform quartic envelope 0.284790046861... . The inequalities are deliberately written <= even though the graph-sensitive caps are strict.

**[PROVED EXACTLY — all six raw core exceptions active]**

The independent all-six-active spectral theorem gives sum d<=D6=383/1008. The same capped-simplex argument yields

P2: P_fixed <= 2 f(c)+f(D6-2c)
              = 0.18517279879681838... ,          (5)

P1/P3: P_fixed <= f(1/4)+f(D6-1/4)
                 = 241638909745/1032386052096
                 = 0.23405867335616654... .       (6)

The P1/P3 six-active bound is unchanged, because the scalar extremal allocation concentrates on the one C4-supported pair and a second pair whose permitted cap c exceeds D6-1/4. No feasibility claim for this allocation in a full Type-E code is made.

All displayed decimals are evaluations of exact expressions in Q(sqrt(2)); the accompanying SymPy checker verifies the graph enumeration, inequalities between constants and the envelopes.

## 4. Next proof task and ledger

These are actual F3 graph-sensitive defect restrictions. They should replace the uniform six-core quartic envelope when constructing the corrected weighted-versus-fixed harmonic inequality, with separate P1/P2/P3 branches and retained safe-pair mixing penalties.

The bound on the weighted harmonic defect cannot be obtained by setting D_weighted<=P_fixed; the nonnegative midpoint threshold correction from the exact audit must remain present.

**[RETAINED]** Global 40<=tau_5<=44; Type-E 1/49<A<=383/504; M(F3)<=89; matching M(P)>=S/2-28/3; twenty-edge mass >=2137/6; Musin/Boyvalenkov zero-midpoint exclusion; 184 safe pairings. Types C, D, E, generic e>=27, and non-isolated branches remain open. Sparse e=23/24 classification assumes delta(G)>=1.
