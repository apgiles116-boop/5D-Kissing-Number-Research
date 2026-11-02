# Type E: F3 switched-endpoint Perron obstruction (2026-11-02)

**[PROVED EXACTLY — F3 endpoint theorem]** Canonical positive-defect support has at most 3 edges and raw defect D<1/4. All three F3 matchings have at most 3 positive-defect quotient pairs. **[CONDITIONAL]** Canonical D <= (sqrt(2)-1)/2 uses the retained stronger core midpoint cap C<567/1000. Safe-correlation counts retain the separate Q_total>28.3626 certificate. **[OPEN]** No Type-E exclusion; global 40<=tau_5<=44.

## 1. Canonical switching and endpoint negativity

The F3 strict deep-contact graph on 0,...,7 is 02,04,05,14,17,23,27,36,56,57. Select canonical matching P0=(04),(17),(23),(56), writing each selected edge as u_i^±=m_i±z_i, with ||u_i^±||=1, m_i·z_i=0 and a_i=||m_i||²<1/4. Put g=(1,-1,1,1), w_i=g_i z_i, v_i=m_i+w_i. Each v_i is one of the original unit endpoints.

Every one of the six quotient pairs has exactly one deep cross-contact; its endpoint sign product is g_i g_j. The opposite same-sign contact is <=1/2 while the deep contact is <-1/2. Their average therefore gives

    c_ij+w_i·w_j<0,   c_ij=m_i·m_j.                 (1)

For delta_ij=(|z_i·z_j|-1/2)_+>0, the previously proved F3 switching theorem gives w_i·w_j=-1/2-delta_ij. The four cross-contact upper inequalities give c_ij+|z_i·z_j|<=1/2, hence c_ij<=-delta_ij. Consequently

    v_i·v_j<=-1/2-2delta_ij   if delta_ij>0;
    v_i·v_j<0                otherwise.           (2)

The strict negativity on **nondefect** pairs is the new ingredient.

## 2. Weighted Perron obstruction

Let E={ij:delta_ij>0}; on E put b_ij=1/2+2delta_ij and let B be the nonnegative weighted adjacency matrix on the four quotient vertices. For every t>=0 componentwise,

    0<=||sum t_i v_i||²<=t^T(I_4-B)t.

Taking a nonnegative Perron eigenvector yields **rho(B)<=1**. The earlier signed F3 theorem excludes triangles in E. Four positive edges would form C4, where every b_ij>1/2; thus rho(B)>rho(A(C4)/2)=1, contradiction. **At most three positive defects occur in the canonical matching.**

All six pairs are singleton-contact, so delta_ij<1/8. For at most two positive defects, D=sum delta<1/4. For three, apply the unit-vector Gram bound to t=(1,1,1,1): since all other pair dots are negative,

    0<=||sum_i v_i||²<4-2sum_(ij in E)(1/2+2delta_ij)
                   =1-4D.

Hence **D_raw<1/4**, with no stronger harmonic assumption. This supersedes the earlier canonical 0.4062555 ceiling.

## 3. Stronger mass-sensitive canonical ceiling

**[CONDITIONAL on retained C=sum_four a_i<567/1000 and singleton mass-defect inequality delta_ij<=f(a_i+a_j), f(t)=t(1-t)/2].**

Every triangle-free support with at most 3 edges is one edge, two adjacent/disjoint edges, a three-edge star, or a three-edge path.

- One edge: D<1/8.
- Two adjacent: rho(B)=sqrt(b1²+b2²)<=1, so D=(b1+b2-1)/2<=(sqrt(2)-1)/2.
- Two disjoint: their mass sums t1+t2=C, hence D<=2f(C/2)=C(1-C/2)/2<812511/4000000<(sqrt(2)-1)/2.
- Three-edge star: rho(B)=sqrt(sum b_i²)<=1, so D<=(sqrt(3)-3/2)/2.
- Three-edge path with weights b1,b2,b3: rho(B)<=1 implies b2²<=(1-b1²)(1-b3²). AM-GM yields b1²+b3²<=2(1-b2), hence b1+b3<=2sqrt(1-b2). Since b2>=1/2 and x+2sqrt(1-x) decreases on [1/2,3/4], sum b_i<=1/2+sqrt(2), yielding D<=(sqrt(2)-1)/2.

Thus **D_raw<=(sqrt(2)-1)/2 = 0.2071067811865...** in the canonical-selected branch under the stronger retained cap.

## 4. Alternative matchings: double-defect-free branch

For P1=(02),(14),(36),(57), switch g=(1,-1,-1,1); for P2=(05),(14),(27),(36), switch g=(1,-1,1,1). Each has four singleton deep quotient pairs forming C4, one diagonal with two opposite same-sign deep contacts, and one diagonal with zero deep contacts. On singleton pairs, (1)-(2) hold; on the double diagonal v_i·v_j<-1/2; on the zero diagonal v_i·v_j<=1/2.

If all four singleton pairs had positive defect, then sum_(i<j) v_i·v_j<-2-2D_single-1/2+1/2<-2, impossible for four unit vectors. Combined with the triangle-free theorem, **every F3 perfect matching has at most three positive-defect quotient pairs**.

If the double-contact diagonal has zero positive defect, there are at most three positive singleton defects. With <=2, their 1/8 caps give D<1/4. With three, the double diagonal <-1/2 cancels at most +1/2 from the zero diagonal, while the remaining nonpositive singleton is negative, so sum v_i·v_j<-3/2-2D; PSD gives D<1/4. Therefore **D_raw<1/4 for alternative-selected matchings with zero double-contact defect**. The alternative double-positive branch is still open.

## 5. Projected-frame consequences [FURTHER CONDITIONAL]

For each of the six canonical core pairs, d_ij²<=1/4+delta_ij+delta_ij². With D<1/4 and singleton caps delta<1/8, convex concentration gives sum delta²<1/32 and sum_core d²<57/32. Retaining Q_total=sum_(i<j)(z_i·z_j)²>283626/10000 yields

    Q_safe (184 fully safe pairs) > 531627/20000=26.58135.

At most 44 of those 184 pairs with |d|>1/3 would give Q_safe<=44/4+140/9=239/9<26.58135. Thus **at least 45 canonical safe pairs have |d|>1/3**.

With the stronger C<567/1000 and D<=(sqrt(2)-1)/2, the cap-concentration formula gives sum delta²<=1/64+(D-1/8)² (for the maximal relevant D), hence

    Q_safe>529127/20000+sqrt(2)/8=26.633126695...,

still forcing 45, not 46.

For alternative matchings with zero double defect, only five core pairs can violate the projective threshold. The same D<1/4 and singleton cap imply sum_core d²<49/32. Of the 185 fully safe pairs,

    Q_safe>536627/20000=26.83135.

At most 45 pairs with |d|>1/3 contribute <=45/4+140/9=965/36<26.83135, so **at least 46 of the 185 fully safe pairs have |d|>1/3** in this branch.

## Proof-status ledger

**[PROVED EXACTLY]** Exact F3 switching incidence, endpoint negativity, Perron spectral obstruction, all-matching exclusion of four positive defects, canonical D<1/4, and alternative double-defect-free D<1/4. **[CONDITIONAL]** Canonical D<=(sqrt(2)-1)/2 uses the stronger retained harmonic/mass cap. Safe-pair counts additionally use the retained Q-frame floor; neither upstream certificate is re-established here. **[VERIFIED EXACT ARITHMETIC]** Companion checker enumerates quotient incidences and verifies determinant, radical, and rational thresholds. **[OPEN]** Type E, C, D, generic e>=27, and non-isolated branches. Sparse e=23/24 classification still requires delta(G)>=1. Preserve star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, baseline A<=383/504, and Musin/Boyvalenkov's 21-line zero-midpoint exclusion. Global proved range **40<=tau_5<=44**.

Next: seek a joint endpoint-Gram and Walsh certificate for the alternative **double-positive** branch, then couple surviving configurations to Q-frame variance. No D5 Q-kernel labeling is assumed.
