# Type E: exact four-core PSD defect-concentration penalty

Date: 2026-10-31. **Global proved range 40 <= tau_5 <= 44. Type E OPEN.**

## Statement and proof status

**[PROVED EXACTLY — universal four-midpoint algebra; numerical Type-E corollary conditional on retained caps]**

For four core midpoint vectors m_i, let a_i=||m_i||^2 <= 1/4 and A_C=sum a_i <= 383/504. For each pair write c_ij=m_i.m_j, d_ij=|z_i.z_j|, eps_ij=max(d_ij-1/2,0), delta=sum eps_ij, E2=sum eps_ij^2, and Q6=sum d_ij^2. Assume all upper cross-endpoint contact inequalities and the retained Type-E raw defect cap

    delta <= D = 1780062775/4032758016.

Then the six exceptional core squared correlations obey

    Q6 <= 32436090936603055633/16263137215612256256 - 27/80000
       = 20269126329870491560321/10164460759757660160000
       = 1.994117229525... .

The improvement over the preceding 1.994454729525... bound is **exactly 27/80000 = 0.0003375**. No D5 alignment, Q-rank condition, or numerical optimizer is used.

**[PROVED CONDITIONALLY — retained Type-E global Q-energy floor]**

    Q_safe >= 259144239476339336023679/10164460759757660160000
           = 25.495129117161... .

With the separately retained center-derived frame-variance floor, Q_safe > 25.765028770790... .

## Proof

### Step 1: retain the pointwise endpoint remainders

The four cross-endpoint upper contacts imply c_ij+d_ij <= 1/2 and 0 <= eps_ij <= max(-c_ij,0) <= 1/4. Define N=sum over negative c_ij of (-c_ij) and s_C=||sum_i m_i||^2.

For c>=0, d^2 <= (1/2-c)^2, so the previous affine endpoint majorant has nonnegative remainder at least c(1/4-c). For c<0, d^2 <= (1/2+eps)^2 and the affine remainder is at least (3/4)(-c-eps)+eps(1/4-eps). Summing, and using 2 sum c_ij=s_C-A_C, gives

    Q6 <= 3/2 + delta/4 + E2 + 3(A_C-s_C)/8
          - 3(N-delta)/4
          - sum over positive c_ij of c_ij(1/4-c_ij).             (1)

All final terms subtracted are nonnegative.

### Step 2: either the scalar convexity bound has a gap, or two defects are large

For 1/4<=t<=1/2 define F(t)=1/16+(t-1/4)^2. Capped-simplex convexity gives E2<=F(delta) in this range, and E2<=delta^2 below 1/4. Set

    B = 3/2 + D/4 + F(D) + 3(383/504)/8.

If delta<=D-1/1000, monotonicity yields

    B-Q6 >= (2D-251/1000)/1000 > 27/80000.

If delta>D-1/1000 but E2<=F(delta)-1/2000, the loss is at least 1/2000.

In the remaining case, delta>D-1/1000>11/25 and E2>F(delta)-1/2000. Sort the six defects p>=q>=... . Then

    p > 6/25,       q > 9/50.                                   (2)

Indeed, if p<=6/25, majorization gives E2<=(6/25)^2+(delta-6/25)^2, whereas the difference from F(delta) is 49/5000-delta/50>1/1250>1/2000. If q<=9/50, majorization by (1/4,9/50,1/50,0,0,0) gives E2<=953/10000, but E2>981/10000.

### Step 3: PSD forces a positive-correlation penalty

The two largest defects cannot lie on disjoint pairs: their sum is >21/50, but Cauchy and AM-GM bound any disjoint pair-defect sum by A_C/2<19/50. Relabel their edges as (1,2) and (1,3).

If N-delta>=1/1000, equation (1) already loses at least 3/4000. Otherwise put u=-c_12>=p and v=-c_13>=q. The unused-negative-correlation slack is <1/1000, so

    u-v > p-q-1/1000 >= 2p-delta-1/1000
        > 12/25-D-1/1000 > 3/80.                              (3)

The three-vector Gram Schur complement, together with a_i<=1/4, gives

    c_23 >= [uv-sqrt((a_1 a_2-u^2)(a_1 a_3-v^2))]/a_1
         >= 4[(6/25)(9/50)
                -sqrt((1/16-(6/25)^2)(1/16-(9/50)^2))]
         > 3/25.                                               (4)

The final inequality is exact: the square root is less than 13/1000.

On the other hand, Cauchy and (3) give

    (u-v)^2 = |m_1.(m_2-m_3)|^2
            <= a_1(a_2+a_3-2c_23)
            <= 1/8-c_23/2,

so c_23<1/4-2(3/80)^2=791/3200. The positive pair (2,3) therefore contributes the loss

    c_23(1/4-c_23) > (3/25)(9/3200) = 27/80000.

Every possible case loses at least 27/80000 from B, proving the theorem.

### Step 4: safe-correlation floor

The retained global frame identity gives Q_all>=17456771/635040. Since Q_all=Q_safe+Q6, subtract the new upper bound to obtain the exact safe floor above. The separately retained center-derived bound Q_all>5876056025347/211680000000 yields the stronger conditional floor.

## Verification and limitations

The companion Python verifier checks every rational comparison and runs 3,000 supplementary deterministic rational Gram tests. The proof is analytic; the finite tests are not its justification.

**[PROVED EXACTLY]** The universal four-vector inequality under the explicitly stated endpoint and energy/defect hypotheses.

**[PROVED CONDITIONALLY]** The numerical Type-E bounds, relying on the retained upstream certificates A<=383/504 and delta<=D. Those upstream proofs were not independently re-audited in this pass.

**[OPEN]** Type E remains unresolved. Types C, D, generic e>=27, and non-isolated branches remain open. Sparse e=23/24 classification still requires minimum degree >=1. Retain M(F3)<=89, M(P)>=S/2-28/3, twenty-edge deep mass >=2137/6, and Musin/Boyvalenkov's zero-midpoint exclusion.

Next: sharpen the joint residual (1) using the full signed 4x4 midpoint Gram, core centroid, four rank-free Q residuals, and one common labeling; avoid another generic SDP.
