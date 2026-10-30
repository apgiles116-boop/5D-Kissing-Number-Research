# Type E: weighted Q-kernel leverage proves H204 > 9/8

Date: 2026-10-30. **[EXACT, CONDITIONAL TYPE-E THEOREM]** Assumes retained H=16K2+F3 matching, isolated center, 184 fully two-sided safe selected-pair blocks, 20 fully two-sided safe center blocks, six potentially exceptional core-core blocks, and A<=383/504. This is a lower bound on safe slack, NOT Type-E elimination.

Write x_i^±=m_i±z_i, a_i=||m_i||²<=1/4, w_i=||z_i||²=1-a_i, A=sum a_i, U=sum a_i². Include y_0=v (isolated unit center), y_i=z_i for 1<=i<=20. Define

\[
H_{204}=\sum_{184\ {\rm safe}}(1/2-|z_i\cdot z_j|)^2+\sum_{i=1}^{20}(1/2-|v\cdot z_i|)^2.
\]

**[NEW PROVED EXACTLY]**
\[
\boxed{H_{204}>\frac{2061191525172601}{1826639216640000}>\frac98.}
\]
This improves the previous exact bound H204>1.050467... and requires neither D5 labeling nor a new SDP.

## Weighted kernel-leverage argument

Set Q_i=y_i y_i^T-(w_i/5)I_5, K_ij=tr(Q_i Q_j)=(y_i·y_j)²-w_iw_j/5. Then K is PSD, rank<=14. Let P project onto ker K, k=tr P>=7, k<=20. Compare M=(3/4)diag(w_i²)+(1/20)ww^T with K, writing E=K-M. E has zero diagonal and E_ij=(y_i·y_j)²-w_iw_j/4. Trace correction gives the universal exact inequality

\[
\sum_{i<j}E_{ij}^2\ge\frac{21}{2k(21-k)}\left[\frac34\sum_iw_i^2P_{ii}+\frac1{20}\|Pw\|^2\right]^2. \tag{1}
\]
Indeed tr E=0 and -tr(PE)=tr(PM), so use |tr(PE)|<=sqrt(k(21-k)/21)||E||_F.

Define Xi=sum_{i=1}^{20}(2a_i-a_i²)(1-P_ii)>=0. Then sum_i w_i²P_ii=k-2A+U+Xi.

For every fully safe block, all four endpoint products (or both center products) belong to [-1/2,1/2], so |y_i·y_j|<=1/2 and |K_ij|<=1/5. For six exceptional core-core blocks, |K_ij|<=4/5 by Cauchy-Schwarz. Diagonal K_ii<=4/5. Apply weighted row domination with weights 1 on 16 isolated indices and center, and 13/8 on the four core indices:

- isolated row: 4/5+15/5+4(13/8)/5+1/5=53/10;
- core row: [16/5+1/5+(4/5+3·4/5)(13/8)]/(13/8)=344/65<53/10;
- center row: 4/5+16/5+4(13/8)/5=53/10.

Thus lambda_max(K)<=53/10, and since K is PSD, K<=(53/10)(I-P). Diagonal comparison gives 1-P_ii>=(8/53)(1-a_i)². Since (2-a)(1-a)²>=63/64 for 0<=a<=1/4,

\[
\boxed{\Xi\ge(63/424)A.} \tag{2}
\]
Drop only the nonnegative ||Pw||² term in (1). The function (k-c)²/[k(21-k)] increases for k>=7 and c=(785/424)A-U in [0,3/2). Hence

\[
\boxed{\sum_{i<j}E_{ij}^2\ge\frac{27}{448}(7-\frac{785}{424}A+U)^2.} \tag{3}
\]

## Exact six-exception bridge

Retain the previously proved negative-Gram-square inequality sum_{i<j}[-m_i·m_j]_+²<=A²/4, applied to the four core midpoints. Write A_C=sum_core a_i, U_C=sum_core a_i², C2=2U_C+A_C². The 184 safe blocks and 20 center blocks bound negative E-defects by H204 and positive E-defects by (19U+A²-C2)/16. All four universal upper endpoint inequalities on each exceptional block give m_i·m_j+|z_i·z_j|<=1/2. Collectively, the six exceptional positive E-defects cost at most [A_C/2+(11/32)sqrt(C2)]²; their negative defects cost at most 3/8-21A_C/64+49C2/1024. Therefore

\[
H_{204}\ge\frac{27}{448}(7-\frac{785}{424}A+U)^2-\frac{19U+A^2-C2}{16}
-[A_C/2+\frac{11}{32}\sqrt{C2}]^2-\frac38+\frac{21A_C}{64}-\frac{49C2}{1024}. \tag{4}
\]
Here **two-sided** safety is essential for |z_i·z_j|<=1/2 in the 184 safe blocks; no such condition is imposed on the six exceptions.

## Exact rational scalar certificate

Set B=383/504. RHS (4) decreases in U, since derivative <=27/32-19/16<0; replace U by A/4. It decreases in C2; replace C2 by D(A_C)=A_C/2+A_C². It becomes base(A)+g(A_C), with

\[
base(A)=\frac{27}{448}(7-\frac{679}{424}A)^2-\frac{19A/4+A^2}{16}-\frac38,
\quad
g(c)=\frac{21c}{64}-\frac{c^2}{4}-\frac{106}{1024}D(c)-\frac{11c}{32}\sqrt{D(c)}.
\]
base decreases on [0,B]. g is concave because c sqrt(c/2+c²) is convex; g(0)=0 and g(B)<0, so g(c)>=g(B) for c in [0,B]. The rational bounds (9/10)²<D(B)=243205/254016<(49/50)² give the strict certificate

\[
H_{204}>base(B)+D(B)/16-[B/2+(11/32)(49/50)]^2+21B/64-49D(B)/1024
=\frac{2061191525172601}{1826639216640000}
=\frac98+\frac{6222406452601}{1826639216640000}.
\]

**[OPEN]** No contradictory upper bound on H204 yet. Next: retain eta=||Pw||² and individual mixed Walsh channels. **[GLOBAL RANGE RETAINED]** 40<=tau_5<=44. Type C, D, generic e>=27 and non-isolated branches remain open; sparse e=23/24 classification assumes delta(G)>=1. Preserve M(F3)<=89, matching S/2-28/3, mass>=2137/6 and A<=383/504.
