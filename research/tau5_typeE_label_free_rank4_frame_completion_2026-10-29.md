# Type E: label-free rank-four frame completion (2026-10-29)

**[PROVED EXACTLY — standalone matrix theorem]**. **[TYPE-E CONSEQUENCE CONDITIONAL ONLY ON RETAINED 16+4 PAIR DECOMPOSITION]**. No D5 labeling, angular rounding, or new SDP. No Type-E exclusion; global range **40 <= tau_5 <= 44**.

## Definitions

For twenty disjoint deep edges let u_i^+/- = m_i +/- z_i, a_i=||m_i||^2, A=sum a_i. Separate the sixteen isolated selected edges I from four F3 matching edges J. Define

- S=sum_{i in I} z_i z_i^T, x=sum_{i in I} a_i, tr S=16-x;
- C=sum_{j in J} z_j z_j^T, c=tr C=4-A+x, C>=0 and rank(C)<=4;
- T=S+C, mu=(20-A)/5, V=||T-mu I||_F^2;
- Q=sum_{i<j}(z_i.z_j)^2.

Let s1>=s2>=s3>=s4>=s5>=0 be the eigenvalues of S.

## Exact sharp completion theorem

**[PROVED]** For every PSD 5x5 matrix S and every c>=0, the minimum of ||S+C-mu I||_F^2 over C>=0, rank(C)<=4, tr C=c (where mu=(tr S+c)/5) is exactly

    Phi(S,c)=(s1-mu)^2+sum_{i=2}^5(max(s_i,theta)-mu)^2,

where theta is the water level determined by sum_{i=2}^5(theta-s_i)_+=c. For c=0 take theta=s5. A minimizer is diagonal in an eigenbasis of S, with C eigenvalues (0,(theta-s2)_+,...,(theta-s5)_+).

**Proof:** Expand the Frobenius square. For fixed eigenvalues of C, von Neumann's trace rearrangement inequality minimizes tr(SC) by opposite eigenvalue pairing. Since rank(C)<=4, its zero eigenvalue pairs with s1. The remaining four nonnegative eigenvalues are allocated by a strictly convex scalar quadratic minimization; its KKT conditions are exactly the water-filling formula. This proves the formula and its abstract attainability.

In particular,

    V >= Phi(S,c) >= (5/4)(s1-mu)^2.

For the last bound, if s1>=mu, a top eigenvector of S gives a Rayleigh quotient of E=T-mu I at least s1-mu, because C>=0. If s1<=mu, any unit w in ker C has w^T E w<=s1-mu. Since E is traceless, projection onto ww^T-I/5 proves ||E||_F^2 >= (5/4)(w^T E w)^2. The constant 5/4 is sharp: for s1<mu the optimal completion gives eigenvalues of T equal to s1 and four copies of mu+(mu-s1)/4. If s1>mu and s2<=mu-(s1-mu)/4, equality also holds.

## Exact Q consequence — no D5 hypothesis

The universal twenty-vector identity is

    Q=30-3A+A^2/10-(1/2)sum_i a_i^2+V/2.

Therefore every Type-E 16+4 configuration necessarily satisfies

    Q >= 30-3A+A^2/10-(1/2)sum_i a_i^2
         + Phi(S,4-A+x)/2
      >= 30-3A+A^2/10-(1/2)sum_i a_i^2
         + (5/8)(lambda_max(S)-(4-A/5))^2.

This is an exact *label-free quadratic stability penalty*. If Q minus the displayed base expression is at most epsilon, then |lambda_max(S)-(4-A/5)|<=sqrt(8epsilon/5). To turn it into a uniform Type-E improvement, one must prove the isolated 16-line top eigenvalue cannot satisfy this spectral pinning while meeting the 120 isolated-isolated and 64 isolated-core safe Walsh blocks plus center constraints.

## Rational examples (abstract matrices, not spherical codes)

- mu=4, s=(7/2,13/4,3,3,11/4), c=9/2: Cdiag=(0,7/8,9/8,9/8,11/8), V=5/16, equality in the 5/4 bound.
- mu=4, s=(9/2,3,3,5/2,5/2), c=9/2: Cdiag=(0,7/8,7/8,11/8,11/8), V=5/16, equality.
- mu=4, s=(9/2,9/2,3,3,5/2), c=5/2: Cdiag=(0,0,2/3,2/3,7/6), V=5/6, strictly above the single-eigenvalue 5/16 bound.

For an exact D5 sixteen-root subset with zero isolated midpoint energy, s1=4 with multiplicity k=1 or 2; the k-dimensional traceless projection gives V >= 5k/(5-k)*(A/5)^2, recovering the earlier complement theorem's x=0 specialization. No D5 alignment is asserted for Type E.

**[VERIFIED]** Exact Fraction checks of these examples and 500 exact rational PSD rank-four diagnostic completions; diagnostics supplement, not replace, the proof. Companion script in this directory.

**[OPEN]** No proven nonzero lower bound on |lambda_max(S)-mu|, no Type-E contradiction. Retain F3<=89, matching M(P)>=S/2-28/3, A<=383/504, and the audited 21-line boundary theorem. Types C,D, e>=27 and non-isolated branches remain open. Global range **40<=tau_5<=44**.
