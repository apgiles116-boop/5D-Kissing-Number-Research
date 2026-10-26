# Type E: matching-uniform F3 balanced-triangle stability improved to 1/3600

Date: 2026-10-26. Status: **[PROVED EXACTLY]** graph enumeration, vector theorem, and rational SOS. **[CONDITIONAL TYPE E]** application to the selected F3 matching and six-core defects. **[OPEN]** Type E exclusion.

## Graph and theorem

Use F3 edges 02,04,05,14,17,23,27,36,56,57. Its three perfect matchings are 02|14|36|57, 04|17|23|56, and 05|14|27|36. For each matching, three *actual unmatched deep edges* form a balanced triangle on three matched-pair indices: the product of the three endpoint-sign products is +1. One choice of triangle edges for each matching is respectively (04,05,17), (02,14,27), (02,04,17). These are quotient triangles, not triangles of F3.

Write endpoints of the four selected deep edges as p_i^±=m_i±z_i with m_i·z_i=0, ||m_i||²+||z_i||²=1 and ||m_i||²≤1/4. Put C=Σ||m_i||², N=Σ_{i<j}(-m_i·m_j)_+, epsilon=C-N, M=Σm_i, E_ij=||m_i||²+||m_j||²-2|m_i·m_j|≥0, s=ΣE_ij, q=||M||². Exact identity:

    s+q=4 epsilon.

**Theorem [PROVED EXACTLY].** If the three actual endpoint inner products on a balanced quotient triangle are ≤−1/2, and 0<C≤1, then

    epsilon > C²/3600.

This strengthens the earlier matching-uniform C²/4608 by 32/25. It applies separately to *every* F3 perfect matching, not just the all-singleton matching. Do not transfer energy budgets between matchings.

## Proof

Let I be the triangle indices and h the omitted index. Balance supplies signs eta_i with endpoint-sign product eta_i eta_j. Summing the three actual deep endpoint products gives

    Σ_triangle (p_i^sigma·p_j^tau+1/2)
      = ||M-m_h||²/2 + ||Σ_{i in I} eta_i z_i||²/2 + T ≤ 0,

where T is the sum of the three mixed midpoint/projection terms. Orthogonality m_i·z_i=0 gives |m_i·z_j|,|z_i·m_j|≤sqrt(E_ij), hence |T|≤2sqrt(3s). By Minkowski,

    sqrt(C)≤2||m_h||+sqrt(s),

and consequently

    ||M-m_h||≥sqrt(C)/2-sqrt(s)/2-sqrt(q).

If epsilon=0, s=q=0 contradicts the displayed deep-triangle identity. Suppose 0<epsilon≤C²/3600. Set r=sqrt(s/(4epsilon)), t=sqrt(q/(4epsilon)), so r²+t²=1 and r,t≥0. Since C≤1,

    ||M-m_h||≥sqrt(C)[1/2-(r+2t)/60],
    |T|≤(sqrt(3)/15)Cr.

The bracket is positive. The deep-triangle identity would force

    (30-r-2t)² ≤ 480sqrt(3)r.

But sqrt(3)<26/15, so 480sqrt(3)<832. Using r²+t²=1, r≤1−t²/2 and rt≥0,

    (30-r-2t)²−832r
     = 901+3t²+4rt−892r−120t
     ≥ 9+449t²−120t
     = 449(t−60/449)²+441/449 > 0.

Contradiction. If C=0, the deep-triangle identity with all m_i=0 also contradicts its nonnegative right-hand side. QED.

## Six-core consequence [CONDITIONAL TYPE E]

For each exceptional core pair define delta_ij=(|z_i·z_j|−1/2)_+. Two endpoint upper inequalities imply, whenever delta_ij>0,

    delta_ij + |m_i·z_j+sign(z_i·z_j)z_i·m_j|
      ≤ −m_i·m_j.

Thus, for the *mass-selected matching*,

    Σ_exceptional(delta_ij+|mixed_ij|)
      ≤ N < C−C²/3600.

The sharp PSD negative-Gram inequality Σdelta_ij²≤C²/4 also yields

    P_raw=Σ_core[(z_i·z_j)²−1/4]_+
       < C+(899/3600)C².

These are new quadratic cuts, not replacements for the stronger retained convex raw-defect cap 1780062775/4032758016 when that applies.

## Ledger

**[PROVED EXACTLY]** Matching enumeration, balanced triangles, s+q=4epsilon, SOS proof. **[CONDITIONAL]** Six-core application uses Type-E graph, deep contacts, and all endpoint upper constraints. **[OPEN]** No improvement of the retained energy interval 1/99<A≤383/504 or exclusion of Type E. Next: insert the strict quadratic cut into the 21-vector harmonic/frame-variance polynomial problem while retaining endpoint mixing.

Global proved range remains 40≤tau_5≤44. Preserve M(F3)≤89, selected matching mass ≥S/2−28/3, twenty-edge mass ≥2137/6, and the delta(G)≥1 caveat for sparse e=23/24 classification. Types C, D, generic e≥27, and non-isolated branches remain open.
