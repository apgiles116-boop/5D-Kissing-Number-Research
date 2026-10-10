# Type E: exact six-core exception / frame-variance stability (2026-10-10)

**Proof status:** [PROVED EXACTLY] for the stated vector theorem; [CONDITIONAL — TYPE E] for the retained 64-safe-pair graph reduction. No exclusion of Type E. Global retained range 40 <= tau_5 <= 44.

Let 20 vectors z_i in R^5 have ||z_i||^2=1-a_i, 0<=a_i<=1/4, A=sum a_i<=383/504. Partition them into a four-element core J and sixteen-element I, and assume |z_i.z_j|<=1/2 on all 64 cross pairs. Put C=sum_J a_i, t=4-C, mu=(20-A)/5, S_J=sum_J z_i z_i^T, S_I=sum_I z_i z_i^T, E=S_J+S_I-mu I_5, Delta=||E||_F^2/2, D64=sum_(J x I)[1/4-(z_i.z_j)^2]^2. Define the *raw* six-core positive defect X_J=sum_(i<j in J)[(z_i.z_j)^2-1/4]_+ and midpoint variance V_a=sum_J(a_i-C/4)^2.

## [PROVED EXACTLY] Explicit rank-four stability remainder

Writing w=tr(S_J^2)-t^2/5, direct expansion gives

    w=t^2/20+U,
    U=V_a+2 sum_(i<j in J)(z_i.z_j)^2 >= V_a+2 X_J.

Thus the previous rank-four inequality w>=t^2/20 has a nonnegative remainder that measures precisely the nonuniformity of core midpoint energies and the six core correlations. U=0 exactly when the four core a_i are equal and the four z_i are pairwise orthogonal.

Set K=16-mu*t+t^2/5=[16+12C+(4-C)A+C^2]/5. The trace identity and two Cauchy--Schwarz inequalities give

    8 sqrt(D64)+sqrt(2w Delta) >= K+w.

Hence for 1/6<=lambda<=1,

    D64+lambda Delta >= (K+t^2/20+U)^2 /
                        [64+(t^2/10+2U)/lambda].

The following exact additive stability bounds hold:

    D64+Delta   >= 10/41 + (385/3362) U
                >= 10/41 + (385/3362) V_a + (385/1681) X_J;

    D64+Delta/6 >= 5/23 + U/16
                >= 5/23 + V_a/16 + X_J/8.

**Proof of coefficients.** For f_lambda(w)=(K+w)^2/(64+2w/lambda), the baseline f_1(t^2/20)>=10/41 and f_(1/6)(t^2/20)>=5/23 follows from A>=C>=0. For lambda=1, f'_1(w) increases in both K and w when K<6. Here K>=(16+12C)/5 and w>=(4-C)^2/20. Substitution gives

    g(C)=[(C^2-56C+1232)(C^2+40C+80)]/
         [2(C^2-8C+656)^2],

    g'(C)=2304(C-12)(C^2-24C-560)/
          (C^2-8C+656)^3 > 0

for 0<=C<4/5. Therefore f'_1(w)>=g(0)=385/3362. For lambda=1/6, the identity

    16(K+w)(128+12(w-K))-(64+12w)^2
      =16(w+16-2K)(6K+3w-16)>=0

holds because 16/5<=K<6 and w>=0, so f'_(1/6)(w)>=1/16. Integrate each derivative from t^2/20 to t^2/20+U.

## [PROVED EXACTLY] Homogeneous-to-raw bridge

With r_i=1-a_i and h_ij=(z_i.z_j)^2/(r_i r_j), let X_hom,J=sum_(i<j in J)(h_ij-1/4)_+. Then

    X_J >= [(9/16) X_hom,J - 3C/4 + (C^2-u_C)/8]_+,

where u_C=sum_J a_i^2. This follows pairwise from [r_i r_j h_ij-1/4]_+ >= r_i r_j(h_ij-1/4)_+ -(1-r_i r_j)/4, using r_i r_j>=9/16.

## [CONDITIONAL — TYPE E] Interpretation

In H=16K2 disjoint_union F3, the four matched core edges have six potentially exceptional mutual pairings, and all 64 core-to-isolated pairings are safe. Thus the inequalities quantify an unavoidable *joint* cost in the 64 safe-pair squared deficits and global frame excess whenever core correlations or core midpoint variance are present. They do **not** give an independent upper bound on that joint quantity. The existing upper bound on raw positive defect X_J is not a lower bound and cannot by itself close Type E. No identification with the six-dimensional Q-kernel is asserted.

**Open:** derive an independent compatible upper bound or a certified finite polynomial infeasibility. Retain M(F3)<=89, matching M(P)>=S/2-28/3, mass >=2137/6, A<=383/504, and the Musin/Boyvalenkov zero-midpoint exclusion. Types C, D, E and generic e>=27 remain open; e=23/24 graph classification conditional on delta(G)>=1.
