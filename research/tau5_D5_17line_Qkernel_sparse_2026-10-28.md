# Analytic Q-kernel decomposition and sparse local relations for 17 D5 lines

**Date:** 2026-10-28. **[PROVED EXACTLY]** Standalone D5 statement; Type-E relevance remains **conditional** on a separately certified rounded D5 labeling.

## Incidence formula for D_n

For support e={i,j}, set x_e^+=(e_i+e_j)/sqrt(2), x_e^-=(e_i-e_j)/sqrt(2), and Q(x)=xx^T-(||x||^2/n)I. Let S be the set of supports represented by at least one chosen line and D the supports represented by both signs. Let B_D be the n-by-|D| unsigned vertex-edge incidence matrix, and P=I-11^T/n. Then

    rank{Q(x): x chosen}=|S|+rank(P B_D).

**Proof:** Every represented support contributes a unique off-diagonal matrix coordinate, giving off-diagonal rank |S|. The kernel of this off-diagonal projection is generated exactly by Q(x_e^+)+Q(x_e^-)=E_ii+E_jj-(2/n)I for e in D. These diagonal vectors are the columns of P B_D. Therefore a Q-kernel vector has zero coefficients on singly represented supports, equal coefficients on the two signs of each double support, and weights lambda satisfying P B_D lambda=0, i.e. equal weighted vertex degrees.

## Exact 17-line D5 classification

Omitting three of the 20 projective D5 lines gives exactly two patterns:

* Three distinct supports: |S|=10, |D|=7, with binom(10,3)*2^3=960 choices.
* Both signs of one support plus one sign of another: |S|=9, |D|=8, with 10*9*2=180 choices.

Any 7- or 8-edge graph on five vertices is connected and nonbipartite, since disconnected or bipartite graphs have at most six edges. Its unsigned incidence matrix has rank five; P B_D has rank four. Thus the Q-ranks are respectively 14 and 13, with nullities 3 and 4. This is an analytic proof of the earlier 1,140-case classification; no root-vector enumeration is needed.

## Guaranteed eight-line local relations

Any 7-edge graph on five vertices contains a four-cycle. Otherwise each vertex pair has at most one common neighbor, so sum_v binom(deg(v),2)<=10, whereas 14 total degrees imply this sum is at least 13. For any four-cycle (a,b,c,d,a) consisting of double supports, define R_ij=Q(x_ij^+)+Q(x_ij^-). Then the exact eight-line relation

    R_ab-R_bc+R_cd-R_da=0

holds by diagonal cancellation.

**[EXACT FINITE CHECK]** The companion verifier checks all 120 seven-edge and 45 eight-edge support graphs. For seven edges, 60 graphs have two four-cycles and 60 have three; their alternating cycle vectors span ker B_D of dimension 2. For eight edges, all 45 graphs have five four-cycles, spanning ker B_D of dimension 3. Since ker(P B_D) has dimension one greater than ker B_D, the Q-kernel splits into a local four-cycle subspace (dimension 2 or 3) and one global equal-nonzero-degree direction. No identification with Type E's six exceptional pairings is claimed.

## Conditional quantitative stability

If an aligned true frame Y (column norms <=1) is within Frobenius distance epsilon of the rounded unit-root frame X, then for c in ker Q(X),

    ||sum_i c_i Q(y_i)||_F <= 2 epsilon ||c||_2.

This follows from contraction of the traceless projection, ||yy^T-xx^T||_F <= (||y||+||x||)||y-x||, and Cauchy-Schwarz. Under the **previously conditional** high-center alignment epsilon<2/17, a four-cycle relation has eight coefficients +/-1 and residual squared <128/289. This is not an exact relation for the true vectors and is not a Type-E contradiction.

**[OPEN]** Residual Type E, Types C/D, generic e>=27, and non-isolated branches remain unresolved. **Global proved range: 40<=tau_5<=44.**