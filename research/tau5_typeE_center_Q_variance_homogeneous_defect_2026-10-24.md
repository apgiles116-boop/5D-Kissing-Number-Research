# Type E: exact center/Q-frame variance–homogeneous-defect stability

**2026-10-24. [PROVED EXACTLY]** The theorem below follows from the retained isolated-center and midpoint hypotheses. **[OPEN]** Type E elimination and any improvement of the global 40 <= tau_5 <= 44 bound.

## Hypotheses and normalization

For twenty selected disjoint deep edges of the hypothetical 41-code, let the endpoints be \(m_i\pm z_i\), \(a_i=\|m_i\|^2\in[0,1/4]\), \(A=\sum a_i\le B=383/504\), and \(\|z_i\|^2=1-a_i\). An isolated deep-graph center \(u\) satisfies \(|u\cdot m_i|+|u\cdot z_i|\le1/2\). Put \(v_i=z_i/\sqrt{1-a_i}\), \(q_i=(u\cdot v_i)^2\), and \(s_{ij}=(v_i\cdot v_j)^2\).

Define
\[
T=\sum_{i<j}s_{ij}-30\ge0,\quad
E_+=\sum_{i<j}s_{ij}(s_{ij}-1/4)_+,\quad
L_-=\sum_{i<j}s_{ij}(1/4-s_{ij})_+.
\]
These are **normalized weighted** defects. They are not the retained raw or homogeneous defects, and the six raw exceptions do **not** imply only six normalized exceptions.

For \(0\le A\le B\), let \(h(a)=a/[16(1-a)^2]\), \(k=\lfloor4A\rfloor\), \(r=A-k/4\), and
\[
H(A)=k/36+h(r),\qquad
\eta(A,T)=\left(25/28-\frac54H(A)-\frac{3}{8\sqrt5}\sqrt{2T}\right)_+.
\]

## Theorem: exact labeling-free second-order tradeoff

**[PROVED EXACTLY, under the stated hypotheses]**
\[
\boxed{2L_-+\frac{14}{13}\eta(A,T)^2+\frac3{10}T
\le\frac57+2E_+.}
\]

**Proof.** The two-sided center cap gives \(q_i\le1/[4(1-a_i)]\). Therefore \(q_i^2-q_i/4\le h(a_i)\). Since \(h\) is increasing and strictly convex on \([0,1/4]\), its sum with total \(A\) is maximized by \(k\) entries at \(1/4\), one at \(r\), and the others at zero. Thus
\[
\sum_iq_i^2\le\frac14\sum_iq_i+H(A).
\]
Let \(\widehat Q_i=v_iv_i^T-I/5\) in the 14-dimensional trace-free symmetric space, \(\Delta=\sum\widehat Q_i\), \(F=\sum\widehat Q_i\otimes\widehat Q_i\), \(U=uu^T-I/5\). Then \(\operatorname{tr}F=16\), \(\|U\|^2=4/5\), \(\|\Delta\|^2=2T\),
\[
\sum q_i=4+\langle\Delta,U\rangle,\quad
\sum q_i^2=4/5+(2/5)\langle\Delta,U\rangle+\langle U,FU\rangle.
\]
Consequently the Rayleigh quotient \(\rho=\langle U,FU\rangle/\|U\|^2\) obeys
\[
\rho\le1/4+(5/4)H(A)+(3/(8\sqrt5))\sqrt{2T}.
\]
Writing \(\mu=\operatorname{tr}F/14=8/7\) and \(V=\operatorname{tr}(F-\mu I)^2\), trace-zero Cauchy–Schwarz against \(ww^T-I/14\), where \(w=U/\|U\|\), gives
\[
V\ge\frac{14}{13}(\mu-\rho)^2\ge\frac{14}{13}\eta(A,T)^2.
\]
But \(\langle\widehat Q_i,\widehat Q_j\rangle=s_{ij}-1/5\), and direct expansion gives
\[
V=\frac{68}{7}+2\sum_{i<j}s_{ij}^2-\frac45\sum_{i<j}s_{ij}
=\frac57-\frac3{10}T+2E_+-2L_-.
\]
Combining the two proves the claim. No D5 labeling, numerical SDP, or assignment of six normalized exceptions was used.

## Exact conditional corollaries

**[PROVED, CONDITIONAL ON \(T=E_+=0\)]** A normalized tight twenty-line frame with no normalized superthreshold pairs must satisfy
\[
H(A)\ge\frac45\left(\frac{25}{28}-\sqrt{\frac{65}{98}}\right).
\]
The unique threshold obtained from this inequality is \(A_*=0.5944781591654525\ldots\), so **\(A>297/500\)**. The rational certificate at \(A_0=297/500\) is
\[
H(A_0)=17159/273612,\quad
[25/28-(5/4)H(A_0)]^2-65/98
=107327905/1197816424704>0.
\]
This is **not** a uniform Type E energy lower bound.

**[PROVED, SAME CONDITIONS AND \(A\le383/504\)]** We have
\[
L_-\le42477492561665/1857068868125952
=0.0228734072767\ldots<3/128.
\]
Each pair with \(s_{ij}\in[1/16,3/16]\) contributes at least \(3/256\) to \(L_-\); hence **at most one** of the 190 normalized pairings lies in this intermediate interval.

**[PROVED, EXACT D5 TEMPLATE ONLY]** For the normalized D5 lines \(v_{ij}^{\pm}=(e_i\pm e_j)/\sqrt2\), any unit center \(u\) has
\[
\max_{i<j,\pm}(u\cdot v_{ij}^{\pm})^2\ge2/5.
\]
If \(a\ge b\) are the two largest absolute coordinates of \(u\), then \(1\le a^2+4b^2\) and
\((a+b)^2-\frac45(a^2+4b^2)=(a-b)(a+11b)/5\ge0\).
But isolation requires every normalized line to have \(q_i\le1/3\). Thus **an exact normalized D5 template is impossible** for Type E, regardless of its midpoint distribution. This is not a global D5-labeling theorem.

## Proof status and next task

**[RETAINED]** \(M(F_3)\le89\), \(M(P)\ge S/2-28/3\), \(A\le383/504\), and six *raw* exceptional core pairings. **[OPEN]** Obtain sufficiently small \(T\) and \(E_+\), or a compatible full rank-five Gram obstruction, from the raw six-exception and midpoint constraints to force \(A>383/504\). Types C, D, and generic \(e\ge27\) remain open. Global proved range remains \(40\le\tau_5\le44\).

An independent exact SymPy/Fraction checker is in the companion _verify.py file.
