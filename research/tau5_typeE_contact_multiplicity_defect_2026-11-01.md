# Type E: contact-multiplicity defect caps and stronger safe-pair counts (2026-11-01)

**[PROVED EXACTLY — standalone endpoint/Gram and scalar concentration lemmas].** **[PROVED EXACTLY, CONDITIONAL ON RETAINED TYPE-E HARMONIC, Q-FRAME AND RAW-DEFECT CERTIFICATES]** for the 43/44 safe-pair counts. No Type-E exclusion. Global proved range **40 <= tau_5 <= 44**.

## 1. New signed midpoint obstruction

For two selected deep edges with endpoints \(u_\pm=m\pm z\) and \(v_\pm=m'\pm z'\), let \(c=m\cdot m'\), \(d=z\cdot z'\), \(a=\|m\|^2\), \(a'=\|m'\|^2\), and \(\delta=(|d|-1/2)_+\). Every endpoint cross-product is at most \(1/2\). Averaging the \(++\) and \(--\) products gives \(c+d\le1/2\); averaging \(+-\) and \(-+\) gives \(c-d\le1/2\). Thus

\[
\boxed{c+|d|\le1/2,\qquad
\delta\le(-c)_+\le\sqrt{aa'}\le1/4.}
\]

Every raw projective threshold violation therefore forces **negative midpoint correlation**. For the four core midpoints, writing \(C_{ij}=m_i\cdot m_j\),

\[
D_{\rm raw}\le\sum_{i<j}(-C_{ij})_+,\qquad
\sum_{i<j}\delta_{ij}^2\le\sum_{i<j}C_{ij}^2
\le\sum_{i<j}a_i a_j.
\]

This is a new four-by-four PSD midpoint-Gram target, without D5 labeling.

## 2. A sharper cap from the number of deep cross contacts

If all four cross-endpoint products are two-sided safe, \(|d|\le1/2\), so \(\delta=0\). If **exactly one** is deep, the other three lie in \([-1/2,1/2]\), while the deep product lies in \([-1,-1/2)\). Since \(4d\) is their alternating signed sum,

\[
|d|\le5/8,\qquad\boxed{\delta\le1/8}.
\]

If two cross contacts are deep, the preceding midpoint bound still gives \(\delta\le1/4\).

The one-deep cap is sharp under weak local endpoint inequalities: the rational Gram matrix in order \(u_+,u_-,v_+,v_-\),

\[
\begin{pmatrix}
1&-1/2&-1&1/2\\
-1/2&1&1/2&-1/2\\
-1&1/2&1&-1/2\\
1/2&-1/2&-1/2&1
\end{pmatrix}
\]

is PSD with eigenvalues \(0,1/2,(7-\sqrt{17})/4,(7+\sqrt{17})/4\), and has \(d=-5/8\). A double-deep opposite-corner PSD witness reaches \(d=-3/4\). These are local weak-boundary witnesses, not full Type-E configurations.

## 3. Exact F3 multiplicities and squared-defect concentration

The ten F3 deep contacts are \(02,04,05,14,17,23,27,36,56,57\). The canonical matching \(P_0=04|17|23|56\) has six core pairings, **each with exactly one deep contact**; the other 184 of 190 projected pairings are safe. The alternatives \(P_1=02|14|36|57\), \(P_2=05|14|27|36\) have core cross-contact multiplicities \(0,1,1,1,1,2\); thus 185 pairings are safe and the five possible positive defects have caps \(1/4,1/8,1/8,1/8,1/8\).

For nonnegative numbers with sorted caps and bounded sum, the sum of squares is maximized by successively filling the largest caps (majorization/convexity). Retain \(D_{\rm raw}<D_0=441401/10^6\), with \(3/8<D_0<1/2\), and set \(r=D_0-3/8=66401/10^6\). Hence the **new exact upper bounds** are

\[
\begin{aligned}
P_0:\quad&\sum_{\rm exceptional}\delta^2
<3/64+r^2
=\frac{51284092801}{10^{12}},\\
P_1/P_2:\quad&\sum_{\rm exceptional}\delta^2
<5/64+r^2
=\frac{82534092801}{10^{12}}.
\end{aligned}
\]

The older estimate \(\sum\delta^2\le D_{\rm raw}^2\) allowed about \(0.1948\); these improve it to \(0.0512841\) or \(0.0825341\) using contact multiplicity alone.

## 4. Improved safe-correlation floors [CONDITIONAL]

Retain the center/Q-frame theorem \(C_z=\sum_{i<j}(z_i\cdot z_j)^2>283626/10000=28.3626\) from [center Q anisotropy](tau5_typeE_center_Q_anisotropy_2026-11-01.md). This depends on earlier Type-E harmonic/mass certificates; it is **not reproved here**. Each exceptional squared correlation is at most \(1/4+\delta+\delta^2\).

**Canonical matching:**

\[
\sum_{\rm 184\ safe}(z_i\cdot z_j)^2>
28.3626-\frac64-D_0-\left(\frac3{64}+r^2\right)
=\boxed{\frac{26369914907199}{10^{12}}=26.369914907199}.
\]

At most 42 safe pairs with \(|z_i\cdot z_j|>1/3\) would give a squared sum at most \(42/4+142/9=473/18=26.27777\ldots\), contradiction. **At least 43 of 184 safe pairs exceed \(1/3\)**.

**Alternative matching:**

\[
\sum_{\rm 185\ safe}(z_i\cdot z_j)^2>
28.3626-\frac54-D_0-\left(\frac5{64}+r^2\right)
=\boxed{\frac{26588664907199}{10^{12}}=26.588664907199}.
\]

At most 43 safe pairs above \(1/3\) would give at most \(43/4+142/9=955/36=26.52777\ldots\), contradiction. **At least 44 of 185 safe pairs exceed \(1/3\)**.

On each such safe pair the exact two-sided Walsh inequalities force both mixed coefficients \(|m_i\cdot z_j|,|z_i\cdot m_j|<1/6\). These counts improve the previous 42/43 respective results, but are necessary conditions **not** a Type-E contradiction.

## 5. Next finite polynomial/KKT target

Optimize \(\sum_{i<j}(-C_{ij})_+\) or \(\sum\delta_{ij}^2\) over the PSD four-by-four core midpoint Gram, diagonal masses \(a_i\in[0,1/4]\), retained F3 harmonic/scalar mass inequalities, and one-/two-deep contact caps. This may yield an incidence-sensitive upper certificate strong enough to combine with the Q-floor. Do not infer any six-to-six identification with D5 Q-kernel modes.

**[VERIFIED EXACT ARITHMETIC]** Companion Fraction/SymPy script checks the F3 matching incidence, rational local PSD witnesses, cap concentration, and integer threshold margins. **[OPEN]** Type E, Types C/D, generic \(e\ge27\), non-isolated branches. Sparse \(e=23/24\) classification remains conditional on \(\delta(G)\ge1\). Preserve star \(\le70/3\), broom \(M(F3)\le89\), matching \(M(P)\ge S/2-28/3\), selected mass \(\ge2137/6\), \(A\le383/504\), the two defect ceilings, and Musin/Boyvalenkov's zero-midpoint boundary theorem. **Global proved range: \(40\le\tau_5\le44\).**
