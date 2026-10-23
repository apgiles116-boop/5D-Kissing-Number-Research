# Exact D5 physical Q-Gram reconstruction and qualitative isolated-center gap

**23 October 2026. Proof status: EXACT THEOREM for the D5 Q-Gram; CONDITIONAL TYPE-E COROLLARY.** No numerical gap or Type-E elimination is claimed.

## Exact theorem: unlabeled projective-set reconstruction

Let $w_{ab}^{\pm}=(e_a\pm e_b)/\sqrt2$, $1\le a<b\le5$, be the 20 D5 projective representatives. For $v\in\mathbb R^5$ set $Q(v)=vv^T-(\|v\|^2/5)I$.

Suppose 20 vectors $z_{ab}^{\pm}\in\mathbb R^5$ satisfy
$$
\operatorname{tr}(Q(z_i)Q(z_j))=\operatorname{tr}(Q(w_i)Q(w_j))\quad\text{for every }i,j.
$$
Then there exist a **single** $U\in O(5)$, signs $s_i\in\{\pm1\}$, and a permutation \(\pi\) that preserves each two-element support block \(\{(ab,+),(ab,-)\}\), such that
$$
z_i=s_i U w_{\pi(i)}.
$$
In particular, the *unlabeled projective set* is physically congruent to D5. A permutation within each support is indispensable: independently interchanging the two signs on a support does not alter the Q-Gram.

### Proof

**1. Squared correlations.** The diagonal identity \(\operatorname{tr}Q(v)^2=\tfrac45\|v\|^4\) forces \(\|z_i\|=1\). Hence the Q-Gram determines \((z_i\cdot z_j)^2\) exactly. The value is 0 within a support or across disjoint supports, and \(1/4\) between any two lines on supports sharing one vertex.

**2. Ten support planes.** Put \(P_i=z_i z_i^T\), \(S_{ab}=P_{ab}^++P_{ab}^-\). Orthogonality within a support makes \(S_{ab}\) a rank-two orthogonal projector. For disjoint supports \(S_{ab}S_{cd}=0\). For supports sharing a vertex, \(\operatorname{tr}(S_{ab}S_{ac})=1\).

**3. Commutativity.** Given distinct \(a,b,c\), let \(de\) be their complementary support. Both rank-two planes \(S_{ab}\) and \(S_{ac}\) lie in the 3-space perpendicular to \(S_{de}\). For rank-two projections \(P,Q\) in a 3-space, \(\operatorname{tr}(PQ)=1+(n_P\cdot n_Q)^2\). Here the trace is 1, so their normals are orthogonal and \(PQ=QP\). Disjoint-support projections commute as well. Thus all ten support projections commute.

**4. Recover five axes.** The frame operator \(F=\sum_{ab}S_{ab}\) has trace 20 and, from the squared correlations, \(\operatorname{tr}F^2=80\). Equality in \(\operatorname{tr}F^2\ge(\operatorname{tr}F)^2/5\) yields \(F=4I\). Simultaneously diagonalize the ten commuting projections. Every common eigenvector lies in exactly four support planes, and those four supports are pairwise intersecting edges of \(K_5\). Any four pairwise intersecting edges of \(K_5\) form the star of one vertex. Distinct eigenvectors cannot yield the same star because two supports sharing one vertex have intersection dimension one. Therefore the five axes correspond to the five vertices and \(S_{ab}\) is the plane spanned by axes \(e_a,e_b\).

**5. Recover the lines.** For supports \(ab\) and \(ac\), every one of their four squared cross correlations equals \(1/4\). Writing the components on the common axis as \(\alpha_j\) and \(\gamma_k\), one has \(\alpha_j^2\gamma_k^2=1/4\). Summing over \(k=1,2\), using \(\gamma_1^2+\gamma_2^2=1\), gives \(\alpha_j^2=1/2\). Likewise on the other axis. Thus the two lines on each support are exactly the two 45-degree D5 lines, perhaps interchanged. QED.

## New corollary: positive Q-Gram gap from an isolated center

For any unit \(u\) and 20 vectors \(z_i\) with \(\|z_i\|\le1\) and \(|u\cdot z_i|\le1/2\), let \(G_Q(z)\) be their 20-by-20 Q-Gram and \(G_{D5}\) the fixed D5 Q-Gram. There is a **universal but presently non-explicit** \(\delta_{D5}>0\) with
$$
\boxed{\|G_Q(z)-G_{D5}\|_F\ge\delta_{D5}>0.}
$$
Proof: the center-banded vector domain is compact. If its Q-Gram distance infimum were zero, a limit would have the exact D5 Q-Gram, hence by the theorem its 20 projective lines would be a physical D5 image. But D5's exact covering constant gives \(\max_i|u\cdot z_i|\ge\sqrt{2/5}>1/2\), contradiction. Finite label permutations can also be minimized over without affecting strict positivity.

**Scope:** This is the missing *qualitative* rank-one-preserving Q-Gram reconstruction, not a numerical stability constant. It does not prove proximity of arbitrary Type-E candidates, force \(A>383/504\), or eliminate Type E. Global range remains \(40\le\tau_5\le44\). Retain \(M(F_3)\le89\), matching \(S/2-28/3\), and \(A\le383/504\); Types C, D, generic \(e\ge27\), and non-isolated branches remain open.

The accompanying exact verifier checks the D5 Q-Gram rank 14, ten projector identities, K5 star combinatorics, rational O(5) invariance, and the within-support label ambiguity. The commutativity and compactness implications are analytic proofs, not computer-certified assertions.
