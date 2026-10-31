# Type E: signed core-midpoint Gram PSD budget (2026-10-31)

**Status:** [PROVED EXACTLY — standalone endpoint and PSD algebra]; Type-E numerical consequences are [CONDITIONAL] on retained Type-E bounds. **No Type-E elimination.** Global proved range remains **40 <= tau_5 <= 44**.

## 1. Sign-sensitive endpoint inequality

For two distinct selected deep edges with endpoints `m_i +/- z_i`, `m_j +/- z_j`, every cross-endpoint inner product is <= 1/2. Put `p=m_i.m_j`, `h=z_i.z_j`. If `h>=0`, average the (++),(--) contacts; if `h<0`, average (+-),(-+). In either case

`p+|h| <= 1/2`.

Consequently `epsilon_ij=(|h|-1/2)_+ <= (-m_i.m_j)_+`. Crucially this holds for all **six exceptional F3 core pairings**, even if some individual endpoint contacts are below -1/2. It does not invoke the fully safe four-contact cube.

## 2. Sharp four-vector PSD inequalities

For the four core midpoints, set `M=(m_j.m_k)` (PSD), `A_C=tr(M)`, `f1(M)=sum_{j<k}(-M_jk)_+`, and `f2(M)=sum_{j<k}(-M_jk)_+^2`.

**Theorem:**

`f1(M)<=A_C`,  `f2(M)<=A_C^2/4`.

Proof: Both objectives are convex in M. The PSD trace-`A_C` slice is the convex hull of rank-one matrices `vv^T` with `||v||^2=A_C`. For rank one, let `B_+,B_-` be the squared masses of positive and negative entries, `B_++B_-=A_C`. Then `f2=B_+ B_-<=A_C^2/4`. If there are p positive and q negative entries (p+q<=4), `f1=(sum v_+)(sum |v_-|)<=sqrt(pq B_+B_-)<=A_C`, because pq<=4. Both inequalities are simultaneously sharp for `v=(c,c,-c,-c)`.

For six exceptional defects `epsilon_jk`, write `delta=sum epsilon_jk`. Therefore

`delta<=A_C`, `sum epsilon_jk^2<=min(delta^2,A_C^2/4)`.

## 3. Quadratic six-exception correlation budget

For each exceptional correlation d, `d^2<=1/4+epsilon+epsilon^2`. Thus the six squared correlations obey

`Q6 <= 3/2 + delta + min(delta^2,A_C^2/4)`.    (1)

Using the retained exact Type-E raw defect cap
`D=1780062775/4032758016` and `A_C<=A<=383/504` gives

`Q6 <= 3/2+D+(383/504)^2/4 = 1051426055/504094752 = 2.085770682651...`.

The independent-defect estimate `3/2+D+D^2` is about 2.136235541; the signed PSD improvement is about 0.0504648585. These inputs are conditional on the retained upstream Type-E certificates.

## 4. Distribution forced among 184 safe pairs

The retained universal Type-E projected squared-correlation floor is
`Q>=17456771/635040`. Since precisely six of 190 pairings may be exceptional,

`Qsafe>=2000899807/78764805=25.403475664...`.

Every safe pair has `|z_i.z_j|<=1/2`. If `K_r` counts the 184 safe pairs with `|z_i.z_j|>r`, then
`Qsafe<=K_r/4+(184-K_r)r^2`. Exact rational ceilings give:

- **At least 102** safe pairs with `|h|>0`.
- **At least 97** safe pairs with `|h|>1/8`.
- **At least 75** safe pairs with `|h|>1/4`.

**[FURTHER CONDITIONAL]** On the previously certified critical rectangle, combining the retained `Q>28.397201...` with the stronger harmonic `A<567/1000` gives **at least 80** safe pairs with `|h|>1/4`. The weaker exact rational `Q>28397/1000` suffices. This does not independently reverify the finite D5 atlas.

## 5. Open interface

The result is a sign-sensitive Gram constraint on the four F3 core midpoints; it does not force D5 alignment or yield `A>383/504`. Next: retain the 4x4 PSD core Gram as a single variable in a finite KKT problem with the six exceptional endpoint contacts and the four rank-free local Q residual predictors. The 75/80-pair counts do not distinguish the 70 nominally orthogonal and 114 meeting-support pairings.

Preserve `M(F3)<=89`, `M(P)>=S/2-28/3`, twenty-edge mass `>=2137/6`, the Musin/Boyvalenkov zero-midpoint exclusion, and `40<=tau_5<=44`. Types C, D, generic e>=27 and non-isolated branches remain open. Sparse e=23/24 classification remains conditional on `delta(G)>=1`.

Companion exact Fraction verifier available in this repository and in the downloadable research package.
