# Type E: exact 64-cross Walsh/frame-variance bridge and two-scale cap stability (2026-10-29)

**Proof status: [PROVED EXACTLY — standalone under stated hypotheses].** Type-E use is **[CONDITIONAL]** on the retained 20-edge decomposition into 16 isolated and four F3 core matching edges, with all 64 isolated-core endpoint blocks *two-sided safe* (each of their four endpoint inner products in [-1/2,1/2]). The cap corollary additionally assumes A<=383/504. This is not a Type-E exclusion.

## Exact 64-block theorem

Write x_i^±=m_i±z_i, m_i·z_i=0, a_i=||m_i||², ||z_i||²=1-a_i. Let I be the 16 isolated edges and C the four core edges. Set A=sum a_i, y=sum_{j in C}a_j, U_C=sum_{j in C}a_j², S=sum_{i in I}z_i z_i^T, Cmat=sum_{j in C}z_j z_j^T, Z=S+Cmat, mu=4-A/5, V=||Z-mu I||_F², and Q=sum_{i<j}(z_i·z_j)².

For each isolated-core pair put h_ij=1/2-|z_i·z_j|, and H64=sum_{i in I,j in C}h_ij². The previous ledger's H184 sums h² over all 184 safe pairings; H184>=H64. Neither is the mixed Walsh-square mass.

**[PROVED EXACTLY]**

$$
\boxed{H_{64}\ge y\left(1-\frac A5+y-\sqrt{\frac{4V}{5}}\right)-U_C.}\tag{1}
$$

**Proof.** For a safe block, write c=m_i·m_j, b=m_i·z_j, d=z_i·m_j, e=z_i·z_j. The four endpoint correlations are c+t b+s d+st e. Taking differences at fixed t between the two signs s, and using two-sided safety, gives |d+t e|<=1/2 for t=±1. Thus |d|+|e|<=1/2 and d²<=h_ij². Consequently H64>=tr(S M_C), where M_C=sum_{j in C}m_jm_j^T has trace y.

The traceless symmetric 5x5 matrix Z-mu I has least eigenvalue >=-sqrt(4V/5). Hence tr(Z M_C)>=(mu-sqrt(4V/5))y. Orthogonality m_j·z_j=0 and Cauchy give

$$
\operatorname{tr}(Cmat\,M_C)=\sum_{j\ne k\in C}(m_j\cdot z_k)^2
\le\sum_{j\ne k}a_j(1-a_k)=3y-y^2+U_C.
$$

Subtract to obtain (1). No D5 labeling or SDP enters.

For y>0 define D=y(1-A/5+y)-U_C-H64. Rearranging (1) gives the exact **second-order stability bridge**

$$
\boxed{V\ge \frac{5}{4y^2}[D]_+^2,\qquad
Q\ge30-3A+\frac{A^2}{10}-\frac12\sum_i a_i^2
+\frac{5}{8y^2}[D]_+^2.}\tag{2}
$$

Replacing H64 by H184 is valid but weaker. An independent sharp upper bound on H64/H184 is still missing.

## Improved cap-pattern rigidity

For 20 capped midpoint energies 0<=a_i<=1/4 and A<=B=383/504, let b(A) be the sorted cap-filled vector, g(A)=sum b_i(A)^2, and delta=||a_sorted-b(A)||_1.

**[PROVED EXACTLY]**

$$
g(A)-\sum a_i^2\ge\frac5{64}\delta^2.\tag{3}
$$

Proof: d=b-a_sorted has sum zero and positive entries only in the at most four nonzero positions of b. If p<=4 entries are positive, Cauchy on positive and negative parts gives ||d||² >=(delta²/4)(1/p+1/(20-p)) >=5delta²/64. The exact cap majorization identity gives g-sum a²>=||d||².

For 3/4<=A<=B write r=A-3/4<=5/504. There is also a **local linear–quadratic bound**

$$
g(A)-\sum a_i^2\ge r\delta-\frac12\delta^2.\tag{4}
$$

Indeed u=sum_{i<=3}(1/4-a_(i))>=0, t=sum_{i>=5}a_(i)>=0, and d4=r-a_(4) obey t=u+d4, delta=2max(u,t). If d4>=0, b·d>=r t; otherwise b·d=(1/4-r)u+rt>=r u. Thus b·d>=r delta/2. Use g-sum a²=2b·d-||d||² and ||d||²<=delta²/2.

With L=8790283/317520 and the exact frame identity, the improved global cap stability is

$$
\boxed{Q\ge L+\frac{57}{20}(B-A)+\frac5{128}\delta^2+\frac V2.}\tag{5}
$$

The old coefficient on delta² was 1/40. If delta<=r, the stronger local term (r/4)delta replaces (5/128)delta².

If Q<=L+epsilon with 0<=epsilon<=1/300000, exact rational comparisons give A>=3/4 and delta<=r, and therefore

$$
B-A\le\frac{20}{57}\epsilon,\qquad
\delta\le\frac{4\epsilon}{5/504-20\epsilon/57}.\tag{6}
$$

The bootstrap uses delta²<=128epsilon/5 and the exact inequality (5/504-20epsilon/57)²>128epsilon/5 at epsilon=1/300000.

At the formal cap boundary A=y=B, U_C=3/16+(5/504)², (1) reads H64>=1313651/1270080-(383/504)sqrt(4V/5). If V<=1/100, then H64>13485001/13970880>0.9652. This is an abstract near-tight-frame implication, **not a Type-E realization** (three cap energies are on the weak-deep boundary).

## Ledger

**[PROVED EXACTLY]** (1)–(6) under their explicit hypotheses; rational verifier accompanies this note.

**[CONDITIONAL]** Type-E graph/matching classification, two-sided safe incidence, and midpoint cap are retained rather than independently recertified. Prior spectral, harmonic and signed-Gram dependencies retain their qualifications.

**[OPEN]** Derive an incompatible upper bound on H64 or H184, exploiting the six core pairings. No contradiction A>383/504 or Type-E exclusion is obtained. Types C, D, generic e>=27, non-isolated branches remain open; e=23/24 classification still conditional on minimum degree >=1. **Global proved range remains 40<=tau_5<=44.**
