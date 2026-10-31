# Type E: rank-free four-local Q tomography and exact safe-only energy identities

Date: 2026-10-31. Global proved range: **40 <= tau_5 <= 44**, unchanged. **Type E is not eliminated.**

## Proof status

- **[PROVED EXACTLY; universal linear algebra]** Four eight-projector residuals R_j, each using only safe pairwise Q-correlations, sum to the global projected Q-frame deviation B_z. Their squared norms obey an exact four-vector variance identity.
- **[PROVED CONDITIONALLY; retained Type-E center theorem]** The total four-local residual energy is > 0.0374795887196 using the historical A<=383/504 center-variance floor; > 0.046296253125 using the additional stronger harmonic A<567/1000 floor. These are lower bounds, not a contradiction.
- **[PROVED EXACTLY; Type-E incidence]** A weighted safe-only squared-correlation sum H satisfies an exact second-order identity. In the strip x<=1/250, H>2.92224171499 under historical caps; H>2.9507651265625 under the additional stronger harmonic cap. D5 has H=3.
- **[PROVED EXACTLY; rank-free]** All six exceptional core projected squared correlations have explicit safe-only predictors with rigorous Cauchy-Schwarz error bars, whether or not the sixteen isolated Q-projectors have full rank.
- **[PROVED EXACTLY; conditional on any fixed D5 comparison labeling]** A rank-deficient isolated Q-synthesis operator in the strip x<=1/250 must be separated from that D5 sixteen-line frame by total squared normalized-projector distance E2>140617/625000=0.2249872.
- **[OPEN]** A Type-E exclusion; the corresponding upper bound on local residuals or safe Walsh slack; Types C, D, generic e>=27, non-isolated branches. Sparse e=23/e=24 classification still requires delta(G)>=1.

## 1. Four local residuals

Label the four F3 core selected edges by c_j=(0,j,+), j=1,2,3,4, and the sixteen isolated selected edges by the remaining D5 support labels. This is only combinatorial bookkeeping, not D5 alignment. Let a_p=||m_p||^2, w_p=1-a_p=||z_p||^2 and Q_p=z_p z_p^T-(w_p/5)I. Let T_j be the triangle on {1,2,3,4} minus j. Define

    L_j = Q_(0,j,-) + (1/2) sum_{kl in T_j}(Q_(k,l,+)+Q_(k,l,-))
    R_j = Q_(0,j,+) + L_j.

Each R_j has eight weights (1,1,1/2,...,1/2) and contains exactly one F3 core edge. Every off-diagonal pair used in ||R_j||^2 is therefore safe. Direct expansion gives the safe-only formula

    ||R_j||^2 = sum_p c_jp^2 w_p^2
                 + 2 sum_{p<q} c_jp c_jq (z_p.z_q)^2
                 - (sum_p c_jp w_p)^2/5.

Each core and negative-star label has total weight 1 across j, and each K4 label occurs twice with weight 1/2. Consequently

    sum_j R_j = sum_{all 20 p} Q_p = B_z.

Writing V_z=||B_z||^2, the exact four-vector Hilbert-space identity is

    sum_j ||R_j||^2
       = V_z/4 + (1/4)sum_{j<k}||R_j-R_k||^2 >= V_z/4.   (1)

Thus some j has ||R_j||^2>=V_z/16, for EVERY such labeling. Under the retained historical center theorem V_z>47602076041/317520000000, this gives

    sum_j ||R_j||^2 > 47602076041/1270080000000,
    max_j ||R_j||^2 > 47602076041/5080320000000.

With the independently retained stronger harmonic A<567/1000 and V_z>14814801/80000000, the two thresholds become 14814801/320000000 and 14814801/1280000000. The stronger harmonic result remains a separate dependency.

## 2. Safe-only squared-correlation identity

Define the weighted safe-only sum

    H = sum_j sum_{p<q in S_j} c_jp c_jq (z_p.z_q)^2.

Define b_j=sum_{p in S_j} c_jp a_p, A=sum_p a_p, A_K=sum_{12 K4 labels} a_p, eta_p=sum_j c_jp^2, and U_eta=sum_p eta_p a_p^2. The weights satisfy eta_p=1 for the eight star labels and eta_p=1/2 for the twelve K4 labels, sum_j b_j=A, sum_p eta_p a_p=A-A_K/2, and sum_p eta_p=14. Expanding the four norms gives the EXACT identity

    H = 3-A_K/2-U_eta/2+(1/10)sum_j b_j^2
          +(1/2)sum_j ||R_j||^2
      = 3-A_K/2-U_eta/2+(1/10)sum_j b_j^2
          +V_z/8+(1/8)sum_{j<k}||R_j-R_k||^2.          (2)

There are 112 pair occurrences (some repeated), all safe. The D5 template has H=3 and R_j=0.

In the critical strip x=sum_{16 isolated}a_p<=1/250, A_K<=x and individual caps a_p<=1/4 imply U_eta<=(A-x)/4+x^2. Hence

    H >= 3-A/8-3x/8-x^2/2+V_z/8.                       (3)

With A<=383/504 and the retained historical V_z floor,

    H > 7422961514761/2540160000000 = 2.922241714994725...

With additional A<567/1000 and its stronger V_z floor,

    H > 1888489681/640000000 = 2.9507651265625.

These necessary lower bounds do not show D5 proximity or eliminate Type E.

## 3. Rank-free reconstruction of six exceptional projected correlations

For distinct core indices j,k, R_j=Q_cj+L_j implies the exact identity

    <Q_cj,Q_ck>-<L_j,L_k>
       = -<R_j,L_k>-<L_j,R_k>+<R_j,R_k>.                (4)

Put r_j=||R_j||, l_j=||L_j||, and t_jk=w_cj w_ck/5+<L_j,L_k>. By Cauchy-Schwarz,

    |(z_cj.z_ck)^2-t_jk|
       <= r_j l_k + l_j r_k + r_j r_k.                  (5)

Every t_jk, r_j^2 and l_j^2 is determined by norms and SAFE projected squared correlations. No pseudoinverse or rank assumption enters (5). If all four residuals vanish, all six exceptional Q-correlations are reconstructed exactly, regardless of isolated rank.

For D_raw=sum_{j<k}(|z_cj.z_ck|-1/2)_+, rho^2=sum_j r_j^2 and ell^2=sum_j l_j^2, the 1-Lipschitz positive-part map and ||J_4-I_4||_op=3 yield

    D_raw <= sum_{j<k}(t_jk-1/4)_+ +3 rho ell +(3/2)rho^2. (6)

This is an exact, rank-free safe-only interface to the six-exception raw defect. It is NOT yet a numerical improvement on the retained raw positive-defect cap 1780062775/4032758016.

## 4. Rank-deficient branch: exact perturbation energy

Fix any single common D5 comparison labeling and global rotation of the sixteen isolated normalized lines. Write P_p=u_pu_p^T, P_p^0=r_pr_p^T, e_p^2=||P_p-P_p^0||_F^2, E2=sum_I e_p^2 and U_I=sum_I a_p^2. The exact rank-one trace calculation gives

    ||Q_p-Q_p^0||_F^2 = (1-a_p)e_p^2+(4/5)a_p^2.        (7)

The D5 isolated Q-synthesis has rank 14 and smallest squared singular value lambda_*=(31-sqrt(481))/40>9/40. If the actual sixteen-isolated Q-synthesis has rank <=13, the Eckart-Young rank-distance bound and (7) give

    sum_I(1-a_p)e_p^2+(4/5)U_I >= lambda_*,
    E2 >= lambda_*-(4/5)U_I.

For x<=1/250, U_I<=x^2<=1/62500, so

    E2 > 9/40-4/(5*250^2)=140617/625000=0.2249872. (8)

This is a separation condition for rank-deficient configurations, not an assertion that Type E must be close to D5.

## Verification and next step

An exact-rational SymPy verifier, bundled with the local research package, checks (1), (2), (4), (7), the weight counts, the D5 equality case, generic rational unit-vector data, a rank-deficient family, and the rational thresholds. The full note and verifier are included in the corresponding 2026-10-31 research package.

**Next target:** derive an upper bound on rho^2 or H from the 184 safe Walsh constraints and six actual F3 endpoint contacts; then combine it with (1), (3), (6). Do not impose all R_j approximately zero: the retained center variance gives a positive lower bound. Preserve M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, the Musin/Boyvalenkov 21-line zero-midpoint exclusion, and 40<=tau_5<=44.