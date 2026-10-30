# Type E: weighted Q-rank, negative-core Gram PSD, and H204 > 1
Date: 2026-10-30. **[EXACT THEOREM — TYPE-E APPLICATION CONDITIONAL ON RETAINED 16K2+F3 MATCHING, ISOLATED CENTER, AND A<=383/504]**. Global proved range unchanged: 40<=tau_5<=44.

## Statement
For the twenty selected deep pairs x_i^±=m_i±z_i, put a_i=||m_i||²<=1/4, w_i=||z_i||²=1-a_i, A=sum a_i<=B=383/504, U=sum a_i². There are 16 isolated pairs and four selected F3-core pairs, with core energy A_C and U_C. Let v be the isolated unit center. Exactly 184 selected-pair blocks and 20 center blocks are two-sided safe. Define
\[
H_{204}=\sum_{\text{184 safe }ij}(1/2-|z_i\cdot z_j|)^2+
\sum_{i=1}^{20}(1/2-|v\cdot z_i|)^2.
\]
Then **H204 > 1**. This is a *lower* safe-slack bound, not a Type-E exclusion.

## 1. Weighted trace-corrected rank theorem [PROVED EXACTLY, UNIVERSAL]
For n>14 nonzero vectors y_i in R^5, let w_i=||y_i||², Q_i=y_i y_i^T-(w_i/5)I and K_ij=tr(Q_iQ_j). The PSD matrix K has rank at most 14. Define
\[
M=\frac34\operatorname{diag}(w_i^2)+\frac1{20}ww^T,\quad E=K-M.
\]
Then E_ii=0 and E_ij=(y_i·y_j)²-w_iw_j/4. If P projects onto ker K and k=rank P>=n-14, the identities tr E=0 and -tr(PE)=tr(PM) give
\[
\sum_{i<j}E_{ij}^2\ge
\frac{n}{2k(n-k)}
\left[\frac34\sum_iw_i^2P_{ii}+\frac1{20}\|Pw\|^2\right]^2. \tag{WQ}
\]
Indeed |tr(PE)|=|tr((P-kI/n)E)|<=sqrt(k(n-k)/n)||E||_F.
For y_1,...,y_20=z_i and y_0=v, we have sum w_i²P_ii>=k-2A+U because 0<=P_ii<=1. The function (k-c)²/[k(21-k)] increases for k>=7 and 0<=c=2A-U<=2B: its derivative has positive numerator k(21-2c)+21c. Thus
\[
\sum_{i<j}E_{ij}^2\ge\frac{27}{448}(7-2A+U)^2. \tag{R21w}
\]
Unlike normalization-first arguments, this retains raw weights and avoids a global (1-A)² loss.

## 2. Negative Gram-square theorem [PROVED EXACTLY, UNIVERSAL]
For arbitrary vectors m_1,...,m_r with T=sum||m_i||²,
\[
\sum_{i<j}[-m_i\cdot m_j]_+^2\le T^2/4. \tag{NG}
\]
Proof: write their PSD Gram matrix as sum λ_l q_lq_l^T with λ_l>=0, ||q_l||=1. Entrywise negative part is subadditive; Minkowski bounds its off-diagonal Euclidean norm by the sum of rank-one norms. For rank-one q, negative products occur only between positive and negative coordinates, with squared sum S_+S_-<=1/4. Hence the norm is <=sum λ_l/2=T/2. Equality occurs for a sign-balanced rank-one Gram matrix. Applied to the four core midpoints, sum_core(-m_i·m_j)_+²<=A_C²/4.

## 3. The 204-safe/six-core weighted bridge [PROVED EXACTLY, CONDITIONAL TYPE E]
For selected pair ij write s=a_i+a_j, p=a_i a_j, c=m_i·m_j, d=z_i·z_j and w_ij=(1-a_i)(1-a_j)=1-s+p. In every two-sided safe block |d|<=1/2, so
\[
(E_{ij})_+\le s/4,\qquad (E_{ij})_-\le1/2-|d|.
\]
For each center block the analogous positive bound is a_i/4. In a core-core block, the four *universal upper* kissing inequalities imply c+|d|<=1/2 even when a lower contact inequality fails. Since c²<=p<=s/8,
\[
(E_{ij})_+\le(-c)_++s/4+3p/4\le(-c)_++11s/32.
\]
Minkowski and (NG) yield, with C2=sum_core s²=2U_C+A_C²,
\[
\sum_{\rm core}(E_{ij})_+^2\le(A_C/2+11\sqrt{C2}/32)^2.
\]
Also (E_ij)_-<=w_ij/4, and w_ij<=1-7s/8. Since sum_core s=3A_C,
\[
\sum_{\rm core}(E_{ij})_-^2\le3/8-21A_C/64+49C2/1024.
\]
The exact identities sum_190 s²=18U+A² and sum_20 a_i²=U now imply
\[
\boxed{H_{204}\ge\frac{27}{448}(7-2A+U)^2
-\frac{19U+A^2-C2}{16}
-\left(\frac{A_C}{2}+\frac{11}{32}\sqrt{C2}\right)^2
-\frac38+\frac{21A_C}{64}-\frac{49C2}{1024}.} \tag{TE-WQ}
\]
No D5 labeling or six-to-six Q-kernel identification is assumed.

## 4. Exact rational certificate [PROVED EXACTLY, CONDITIONAL TYPE E]
We have U<=A/4, A_C<=A<=B and C2<=D(A_C)=A_C/2+A_C². The derivative of the right side of (TE-WQ) with respect to U is at most 27/32-19/16<0, so replace U by A/4. The C2-dependent part is
\[
-\frac{A_C^2}{4}-\frac{11A_C}{32}\sqrt{C2}-\frac{106}{1024}C2,
\]
hence replace C2 by D(A_C). Write the resulting bound as H204>=base(A)+g(A_C), where
\[
base(A)=\frac{27}{448}(7-7A/4)^2-\frac{19A/4+A^2}{16}-\frac38,
\]
\[
g(c)=\frac{D(c)}{16}-(c/2+11\sqrt{D(c)}/32)^2
+\frac{21c}{64}-\frac{49D(c)}{1024}.
\]
base is decreasing on [0,B]. g is concave because
\[
g(c)=21c/64-c^2/4-106D(c)/1024-(11/32)c\sqrt{D(c)}
\]
and
\[
\frac{d^2}{dc^2}\left(c\sqrt{c/2+c^2}\right)
=\frac{\sqrt2(32c^2+24c+3)}{8\sqrt c(2c+1)^{3/2}}>0.
\]
Thus g(c)>=min(g(0),g(B)). Since g(0)=0 and g(B)<0 (certified using sqrt(D(B))>9/10), H204>=base(B)+g(B). Finally
\[
(9/10)^2<D(B)=243205/254016<(49/50)^2
\]
gives the strict rational bound
\[
H_{204}>\frac{21346842527}{20321280000}
=1+\frac{1025562527}{20321280000}>1.
\]
All numerical comparisons are exact rationals. Companion checker: research/tau5_typeE_weighted_Q_rank_core_PSD_slack_2026-10-30_verify.py.

## Ledger
**[PROVED EXACTLY]** Weighted Q-rank (WQ), negative Gram-square lemma (NG), and algebraic Type-E bridge (TE-WQ) under its stated hypotheses.
**[OPEN]** No incompatible *upper* bound on H204. Retain the weighted kernel-orientation term ||Pw||² for the next pass. Type E, Type C, Type D, generic e>=27, and non-isolated branches remain open. Sparse e=23/e=24 classification remains conditional on delta(G)>=1. Preserve the source-audited Musin/Boyvalenkov zero-midpoint exclusion, star 70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, total mass >=2137/6, and A<=383/504.
