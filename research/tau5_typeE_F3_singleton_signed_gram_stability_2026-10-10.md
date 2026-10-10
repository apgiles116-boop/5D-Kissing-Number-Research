# Type E / F3: exact signed-midpoint Gram gap for the all-singleton matching

**Audit date:** 2026-10-10  
**Status:** **PROVED EXACTLY** under the stated Type-E deep-contact assumptions for the specific all-singleton matching. This is **not** a Type-E exclusion. The mass-selected perfect matching need not be this matching.

## Graph and orientation

Use the ten-edge graph on vertices 0,...,7,

`E(F3) = {02,04,05,14,17,23,27,36,56,57}`.

Choose the perfect matching `04|17|23|56` and orient the pairs as

`(0,4), (7,1), (2,3), (5,6)`,

assigning sign + to the first endpoint and - to the second in each pair. The six remaining edges are `02,05,14,27,36,57`. Each joins a different pair of matched edges, all six unordered pairs of the four matched edges occur exactly once, and both endpoints in each of these six edges have the **same sign** in the chosen orientation.

Write the two unit endpoints of pair `i` as `x_i^± = m_i ± z_i`. Then `m_i·z_i=0`, `a_i=||m_i||²∈[0,1/4]`, `||z_i||²=1-a_i`, and `C=Σ_{i=1}^4 a_i≤1`. Assume that every one of the six cross edges is deep: its endpoint inner product is strictly less than -1/2.

Define `s_ij=m_i·m_j` and `N=Σ_{i<j}(-s_ij)_+`.

## Lemma 1 — exact signed-Gram defect identity [PROVED EXACTLY]

Set `E_ij=a_i+a_j-2|s_ij|=min(||m_i-m_j||²,||m_i+m_j||²)≥0`. Then

```text
4(C-N) = ||Σ_i m_i||² + Σ_{i<j} E_ij.
```

Indeed, `Σ_{i<j}s_ij=(||Σ_i m_i||²-C)/2`, `N=(Σ|s_ij|-Σs_ij)/2` and `Σ_{i<j}(a_i+a_j)=3C`. In particular, `Σ E_ij≤4(C-N)`.

## Lemma 2 — Cauchy–Schwarz bound for mixed cross terms [PROVED EXACTLY]

For each cross edge joining pairs `i<j`, let `ε_ij∈{±1}` be its common endpoint sign, and put

```text
t_ij = (m_i+ε_ij z_i)·(m_j+ε_ij z_j)
     = s_ij + z_i·z_j + ε_ij(m_i·z_j+z_i·m_j) < -1/2,
T = Σ_{i<j} ε_ij(m_i·z_j+z_i·m_j).
```

Choose `σ_ij∈{±1}` such that `σ_ij s_ij=|s_ij|`. Orthogonality gives `|m_i·z_j|=|(m_i-σ_ij m_j)·z_j|≤√E_ij ||z_j||` and similarly `|z_i·m_j|≤√E_ij ||z_i||`. Hence

```text
|T| ≤ Σ_{i<j} √E_ij (||z_i||+||z_j||)
    ≤ √[(Σ E_ij) Σ_{i<j}(||z_i||+||z_j||)²]
    ≤ √[4(C-N) · 6(4-C)]
    = √[24(4-C)(C-N)].
```

The last step uses `(u+v)²≤2(u²+v²)` and `Σ_{i<j}(||z_i||²+||z_j||²)=3(4-C)`.

## Theorem — quantitative stability gap [PROVED EXACTLY]

Because the six cross edges are deep, `Σ t_ij<-3`. On the other hand,

```text
Σ_{i<j}(m_i·m_j+z_i·z_j)
 = [||Σ_i m_i||²+||Σ_i z_i||²-4]/2
 ≥ -2.
```

Therefore `T<-1`, so `|T|>1`, yielding

```text
C-N > 1 / [24(4-C)] ≥ 1/96.
```

The bound is strict even when `C=0`. This quantitatively excludes the abstract rank-one 2+2 equality case `N=C` for the all-singleton matching.

**Upstream-dependent refinement:** if an independently established all-singleton theorem gives `C>33/500`, then `C-N>125/11802`. This refinement is **CONDITIONAL on that separate theorem**, not independently certified by this note.

## Scope and open dependencies

The existing mass theorem selects **some** perfect matching with adequate Delsarte mass; it does not select this all-singleton matching. Thus the gap must **not** be inserted into the mass-selected 20-edge estimates or the global 21-line defect inequality without a transfer argument. The other two F3 matching patterns and generic Type E remain open. Other Type C/D branches, generic e≥27 and the sparse-graph δ(G)≥1 gap also remain open.

Retain the exact historical constants `M(F3)≤89`, `M(P)≥S/2-28/3`, `A≤383/504`; **do not** revert to older superseded mass bounds. Global proved range remains `40≤τ5≤44`.

**Verification:** companion Python `tau5_typeE_F3_singleton_signed_gram_stability_2026-10-10.py` checks the graph/orientation, Lemma 1 on 6561 exact rational examples, and the conditional arithmetic refinement. The proof of Lemma 2 and the theorem is analytic, not empirical.
