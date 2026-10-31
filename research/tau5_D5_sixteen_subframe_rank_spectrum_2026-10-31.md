# D5 sixteen-line Q-subframes: exact rank and sharp spectral audit

Date: 2026-10-31. **Global proved range: 40 <= tau_5 <= 44. Type E OPEN.**

## Proof status

**[PROVED EXACTLY — analytic]** Among the 20 projective D5 roots r_ij^s=(e_i+s e_j)/sqrt(2), delete any four and retain sixteen. Let k be the number of coordinate supports {i,j} for which BOTH signs were deleted. For Q(r)=rr^T-I/5, the retained traceless-Q span has rank **14-k**. Thus exactly 3360 deletions have rank 14, 1440 rank 13, and 45 rank 12. Every rank-13 D5 subframe has a missing Q direction proportional to E_ij+E_ji, a rank-two symmetric matrix.

**[PROVED EXACTLY — exhaustive rational finite certificate]** Across the 3360 rank-14 D5 sixteen-line subframes, the least positive eigenvalue of the Q-Gram matrix K_I obeys the sharp interval

(13-sqrt(149))/20 <= lambda_min(K_I) <= (31-sqrt(481))/40,

or 0.0396722192133... <= lambda_min <= 0.2267071950135....

The lower endpoint is attained by 160 deletions whose supports form a triangle and a disjoint edge (one signed root deleted from each support). The upper endpoint is attained by 80 deletions whose four supports form a star (one signed root deleted from each). An exact SymPy verifier partitions all C(20,4)=4845 deletions into 17 signed-coordinate-permutation orbits, computes rational characteristic polynomials, and uses exact Sturm root counts. No floating-point decision is part of the proof.

**[SCOPE CORRECTION]** The previous rank-deficiency D5 separation constant (31-sqrt(481))/40 is valid for the fixed four-star D5 comparison subframe and its symmetries, NOT for arbitrary sixteen-line D5 subframes. Some other full-rank templates have spectral gap only (13-sqrt(149))/20; rank-13 D5 reference subframes give zero distance to themselves. Hence a uniform positive separation from **all** D5 sixteen-line subframes is false.

**[PROVED EXACTLY — isolated-only no-go]** Rank-13 D5 sixteen-line subframes have |r_i.r_j|<=1/2 for all isolated pairs and zero midpoint energy. Isolated safe coherence and isolated Q-rank alone therefore cannot exclude the rank-13/rank-two-null Type-E branch. The four core endpoints and/or twenty-first line must be used.

## Analytic rank proof

Let S be symmetric traceless and orthogonal to all retained Q(r). Write d_i=S_ii. The equation for a retained signed root is

0=<S,Q_ij^s>=(d_i+d_j)/2+s S_ij.

If both signs on a support {i,j} are retained, d_i+d_j=0 and S_ij=0. Four root deletions leave at least SIX supports with both signs retained. These form a graph F on five coordinate vertices with at least six edges.

**Graph lemma:** if sum_i d_i=0 and d_i+d_j=0 on every edge of a five-vertex graph with at least six edges, then all d_i=0. If F is connected and nonbipartite, an odd cycle forces zero. If connected and bipartite, d is constant with opposite signs on the two parts; since five is odd, the trace-zero condition forces zero. If disconnected, at least six edges is possible only for K4 plus an isolated vertex; the triangle forces four zeros and trace zero the fifth.

Thus all diagonal entries of S vanish. A support with at least one retained sign forces S_ij=0. Each fully omitted support leaves precisely one free off-diagonal entry. Consequently

(span{Q(r):r retained})^perp = span{E_ij+E_ji : support {i,j} fully deleted},

so rank(Q_I)=14-k. Counts: k=2 gives C(10,2)=45; k=1 gives 10*C(9,2)*4=1440; k=0 gives 4845-45-1440=3360.

For k=1, S=E_ij+E_ji has rank two, eigenvectors (e_i+e_j)/sqrt(2) and (e_i-e_j)/sqrt(2), and r^T S r=2r_i r_j=0 for every retained root. Hence those sixteen roots lie in the union of the coordinate hyperplanes x_i=0 and x_j=0, exactly the rank-two-null phase-retrieval incidence locus.

## Finite exact spectral proof

Signed coordinate permutations preserve Q-Gram spectra. Four adjacent coordinate swaps plus one coordinate sign flip generate their action on the twenty D5 projective roots. The verifier exhaustively closes each four-deletion orbit under these generators, finding 17 orbits: nine rank-14 orbits (3360 deletions), six rank-13 (1440), and two rank-12 (45).

For each rank-14 orbit representative, the verifier removes the x^2 zero factor from det(xI-K_I) and uses exact rational Sturm counts on [0,1/20] and [0,1/5]. Exactly two 80-member orbits have one positive eigenvalue below 1/20, both with characteristic polynomial

x^2 (x-1)^6 (2x-3)(2x-1)(4x^2-7x+2)^2 (20x^2-26x+1)/1280.

Their smallest eigenvalue is alpha=(13-sqrt(149))/20. All seven other full-rank orbits have least eigenvalue >1/20>alpha.

Exactly one 80-member orbit has no positive eigenvalue below 1/5; its characteristic polynomial is

x^2 (x-1)^6 (4x^2-7x+2)^3 (20x^2-31x+6)/1280.

Its least positive eigenvalue is beta=(31-sqrt(481))/40>1/5; each other rank-14 orbit has an eigenvalue below 1/5<beta. This proves both sharp endpoints, without numerical root approximations.

## Type-E implications

The four-star D5 template used in the preceding rank-stratified Q note has the **largest**, not the smallest, least-positive-eigenvalue among rank-14 D5 sixteen-line templates. It is a useful *fixed* reference but its 0.226707... gap must not be applied to arbitrary core-to-D5 labelings. In the rank-13 D5 case the missing matrix has rank two; the rank-two-null branch is D5-realizable on isolated safe data and cannot be discarded as a generic anomaly.

**[OPEN]** None of these D5 reference facts proves that a Type-E candidate is D5-labeled, or yields a Type-E contradiction. Next: impose the four F3 core endpoint constraints and signed midpoint Gram PSD on the rank-two-null hyperplane-cover branch. The six exceptional pairings have NOT been identified with the six D5 Q-kernel relations.

Retain star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, raw defect <=1780062775/4032758016, the Musin/Boyvalenkov zero-midpoint boundary exclusion, and the delta(G)>=1 qualification on sparse graph classification. Types C,D, generic e>=27 and non-isolated branches remain open. **40<=tau_5<=44 unchanged.**
