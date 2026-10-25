# Type E: energy-sensitive Q-rank inequality and unconditional 184-safe slack

**25 October 2026.** **[PROVED EXACTLY]** Universal signed quartic rank/energy inequality and elementary six-core quartic cap under stated scalar hypotheses. **[CONDITIONAL ON RETAINED TYPE-E INPUTS]** Stronger outside-core squared-slack bound. **[OPEN]** Type E exclusion and the global five-dimensional kissing number.

## 1. Energy-sensitive rank theorem [PROVED EXACTLY]

Let (15\le n\le20), (z_i\in\mathbb R^5), (b_i=\|z_i\|^2=1-a_i), (0\le a_i\le1/4), (A=\sum_i a_i), and (k=n-14). Define
$$
Q_i=z_i z_i^T-\frac{b_i}{5}I_5,\qquad
E_{ii}=0,\quad E_{ij}=\frac14-(z_i\cdot z_j)^2\quad(i\ne j).
$$
When (t=3k/4-2A>0),
$$
\boxed{\sum_{i<j} E_{ij}^2\ge\frac{n}{28k}\left(\frac{3k}{4}-2A\right)^2.}\tag{1}
$$

**Proof.** The Q-Gram (K_{ij}=(z_i\cdot z_j)^2-b_ib_j/5) is PSD of rank at most 14. Set (K_0=K+E). The following identity is exact for every (n):
$$
K_0=\operatorname{diag}(3/4-2a_i+a_i^2)
+\frac1{20}(\mathbf1+4a)(\mathbf1+4a)^T-aa^T.
$$
Choose an orthogonal rank-(k) projector (P) into (ker K). Then (0\le P_{ii}\le1), (a^TPa\le\sum a_i^2), and (a_i^2\le2a_i), so
$$
\begin{aligned}
s=\operatorname{tr}(PE)&=\operatorname{tr}(PK_0)\\
&\ge\frac{3k}{4}-2\sum P_{ii}a_i
+\sum P_{ii}a_i^2-a^TPa\\
&\ge\frac{3k}{4}-2\sum P_{ii}a_i
-\sum(1-P_{ii})a_i^2\\
&\ge\frac{3k}{4}-2A=t.
\end{aligned}
$$
Since (operatorname{tr}E=0), the trace Cauchy inequality on the (P) and (I-P) blocks gives
$$
\operatorname{tr}(E^2)\ge s^2(1/k+1/14).
$$
Using (operatorname{tr}(E^2)=2\sum_{i<j}E_{ij}^2) proves (1). No pairwise correlation cap or D5 labeling is used. QED.

For (n=20),
$$
\boxed{\sum_{i<j}^{20}E_{ij}^2\ge\frac5{42}(9/2-2A)^2.}\tag{2}
$$
Under retained Type-E (A\le383/504), the right side is at least
$$
\boxed{2820005/2667168\approx1.057303102016821,}
$$
versus the earlier uniform (375/896\approx0.418527).

## 2. Six-core quartic cap [PROVED FROM STATED RETAINED SCALAR INPUTS]

The four core indices have six pairings. Write (r=|z_i\cdot z_j|), (d=(r-1/2)_+). Retain the previously established scalar constraints
$$
d\le1/4,\qquad\sum_{\rm core}d^2<819/10000.
$$
A raw-safe pair (r\le1/2) has (E_{ij}^2=(1/4-r^2)^2\le1/16). A positive-defect pair has (E_{ij}^2=(d+d^2)^2\le25/256).

At most one core pair can contribute more than (1/16). Otherwise two positive defects satisfy (d>(\sqrt2-1)/2), giving
$$
\sum d^2>(3-2\sqrt2)/2>819/10000.
$$
The final comparison is exact because ((14181/10000)^2-2=1100761/100000000>0). Hence
$$
\boxed{T_C=\sum_{i<j\in C}E_{ij}^2\le5/16+25/256=105/256.}\tag{3}
$$
Unlike a bound only on positive core defects, this includes **all six** core quartic contributions, including raw-safe core pairs. It uses the weaker retained square budget, not the stronger (19/250) estimate or the quartic tangent certificate.

## 3. Unconditional 184-safe Type-E bound [CONDITIONAL ON RETAINED MODEL]

The 16 outside-core selected deep edges and 4 selected core edges give exactly 184 raw-safe outside/outside and outside/core pairings. Let
$$
H_{184}=\sum_{\text{184 safe}}(1/2-|z_i\cdot z_j|)^2.
$$
For every raw-safe pair, (E_{ij}^2=h_{ij}^2(1-h_{ij})^2\le h_{ij}^2). Subtracting (3) from (2) gives the **energy-sensitive second-order constraint**
$$
\boxed{H_{184}\ge\frac5{42}(9/2-2A)^2-105/256.}\tag{4}
$$
At (A\le383/504), this yields
$$
\boxed{H_{184}\ge13808395/21337344\approx0.647146852016821.}\tag{5}
$$
This is stronger than the previous (H_{184}>1275/7168\approx0.177874), and crucially has **no uncontrolled safe-core term**. It does not eliminate Type E. Because each safe quartic contributes at most (1/16), at least 11 of the 184 safe pairings have strict correlation (<1/2).

**All-six-positive core subbranch [CONDITIONAL].** If all six core correlations exceed 1/2, the previously retained endpoint-Gram argument gives the sharper cap `T_C^+ <= 47653/802816`. There are no raw-safe core pairs, so (5) improves to

$
\boxed{H_{184}\ge\frac{2820005}{2667168}-\frac{47653}{802816}
=\frac{1362784807}{1365590016}\approx0.997945789755979.}
$

This remains a necessary condition, not a contradiction.
## 4. Weighted 19-subset refinement [PROVED UNDER RETAINED TYPE-E MODEL]

Let (O) be the 16 outside indices, (C) the four core indices, and (A_C=\sum_{j\in C}a_j). Applying (1) to the four 19-element sets (O\cup(C\setminus\{j\})) and averaging gives
$$
H_{OO}+\frac34H_{OC}+\frac12H_C^-+\frac12T_C^+
\ge\frac{19}{560}\sum_{j\in C}(15/4-2A+2a_j)^2.\tag{6}
$$
The right side equals
$$
\frac{19}{140}\left[(15/4-2A+A_C/2)^2
+\sum_{j\in C}(a_j-A_C/4)^2\right],
$$
retaining a nonnegative **core midpoint-energy variance**. Applying the core cap (3) to the *raw quartic version* of the averaged inequality, before substituting squared slacks, gives
$$
\boxed{H_{OO}+\frac34H_{OC}\ge33422213/71124480\approx0.469911526945434.}\tag{7}
$$
The second bound is weighted, so it complements rather than supersedes (5).

## 5. Sharper global squared-correlation floor [PROVED UNDER RETAINED ENERGY CAP]

The retained frame-operator identity is

$
\sum_{i<j}(z_i\cdot z_j)^2=30-3A+\frac{A^2}{10}-\frac12\sum_i a_i^2+\frac V2,
\qquad V=\left\|\sum_i Q_i\right\|_F^2\ge0.
$

Convex concentration with `0<=a_i<=1/4` and `A<=383/504` gives

$
\sum_i a_i^2\le3(1/4)^2+(383/504-3/4)^2=47653/254016.
$

Since `30-3A+A^2/10` decreases on this interval,

$
\boxed{\sum_{i<j}(z_i\cdot z_j)^2\ge8790283/317520\approx27.6841868228773.}
$

This improves the older `17456771/635040≈27.4892` floor. With `L=sum_safe h(1-h)` and `P=sum_positive(d+d^2)`, the exact signed-defect translation is

$
\boxed{L-P\le6291917/317520\approx19.8158131771227.}
$

This is an **upper** bound on the linear safe-defect mass minus the positive exceptional mass; it is not an upper bound on squared safe slack and does not exclude Type E.
## 6. Status

- **[PROVED EXACTLY]** The projector theorem (1)–(2); the implication from the explicit scalar budget to (3); exact rational constants and four-subset combinatorics.
- **[CONDITIONAL ON RETAINED TYPE-E INPUTS]** (4)–(7), relying on the Type-E selected-edge model, 184 raw-safe pairings, (A\le383/504), and (\sum d^2<819/10000).
- **[OPEN]** Opposing upper bound on safe slack or endpoint/Gram contradiction; Type E, Types C and D, generic (e\ge27), and non-isolated branches.
- **[UNCHANGED]** (40\le\tau_5\le44). Retain (M(F_3)\le89), matching (M(P)\ge S/2-28/3), and the source-audited 21-line zero-midpoint exclusion. Sparse (e=23,24) classification remains conditional on (\delta(G)\ge1). No D5 kernel-to-core identification is assumed.

Exact standard-library verifier: `research/tau5_typeE_energy_sensitive_Qrank_2026-10-25_verify.py`.
