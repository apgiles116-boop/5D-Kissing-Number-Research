# Type E / F3: exact rational R3 realizations of both surviving canonical path orbits

**Date:** 2026-11-02

## Theorem and proof status

**[PROVED EXACTLY — standalone eight-endpoint theorem]** The two canonical F3 three-defect path orbits not excluded by the previous integer Farkas certificate, represented by (0,2,1,3) and (0,2,3,1), both have strict rational realizations by eight unit vectors in R^3. In each realization all ten prescribed deep endpoint contacts are strictly less than -1/2, the other eighteen endpoint correlations are strictly between -1/2 and 1/2, exactly the prescribed three projected pairings have correlation less than -1/2, and the canonical four-pair midpoint energy C0 is below 383/504.

The first witness has C0 < 7/20; the second has C0 < 7/16. These are exact inequalities, not numerical tolerances.

**[PROVED EXACTLY, PREVIOUS]** The distinct canonical path orbit represented by (0,1,2,3) remains excluded by its independent integer Farkas certificate. The new witnesses concern only the two previously unresolved orbits.

**[LIMITATION]** These are LOCAL eight-endpoint F3 witnesses, not full Type-E configurations or 41-point kissing codes. They have not been extended by the sixteen isolated deep edges or checked against all cross-contact constraints. Because they already live in R^3 and satisfy the core energy cap, the standalone eight-endpoint Gram PSD condition, ambient rank at most five, and scalar C0 cap alone cannot exclude either of these two path orbits.

## Exact conventions

The ten deep endpoint pairs on u0,...,u7 are:

~~~text
02 04 05 14 17 23 27 36 56 57
~~~

The canonical oriented matching is

~~~text
(A0,B0)=(u0,u4), (A1,B1)=(u7,u1),
(A2,B2)=(u2,u3), (A3,B3)=(u5,u6).
~~~

Set m_i=(A_i+B_i)/2, w_i=(A_i-B_i)/2, and C0=sum_i ||m_i||^2. A positive defect on a quotient pair ij means w_i dot w_j < -1/2. The three other quotient pairings in each witness satisfy |w_i dot w_j| < 1/2.

## Rational unit-vector formula

A row (p,s,(b,c)) at scale N gives a vector in Q^3. Let j,k be the other two coordinate indices in ascending order, t=b/N, v=c/N, r=t^2+v^2. Define

~~~text
u[p] = s*(1-r)/(1+r)
u[j] = 2*t/(1+r)
u[k] = 2*v/(1+r)
~~~

Then ||u||^2=1 identically.

### Witness I: path (0,2,1,3), N=100

Rows u0,...,u7:

~~~text
(2,-1,( 31,-30))
(2, 1,( 28,-33))
(2, 1,(  2, 18))
(2,-1,(-30,-32))
(1, 1,(-23, 11))
(2, 1,(-33,-27))
(1, 1,( 27,-12))
(2,-1,( -1, 17))
~~~

**[EXACT RATIONAL CERTIFICATE]** Every endpoint pair has contact margin > 1/60. All three prescribed defects 02,12,13 have margin > 1/40. All other quotient pairs have |w_i dot w_j| < 1/2, and C0 < 7/20 < 383/504. Diagnostic C0 is approximately 0.3475139317.

### Witness II: path (0,2,3,1), N=1000

Rows u0,...,u7:

~~~text
(1, 1,( 251,-168))
(0, 1,(-324,-202))
(1,-1,( 144, 372))
(2,-1,(  60,  87))
(0,-1,(-233, 181))
(2,-1,(-226,-384))
(2, 1,( -44,  77))
(1, 1,(-158, 181))
~~~

**[EXACT RATIONAL CERTIFICATE]** Every endpoint pair has contact margin > 1/2000. The prescribed defects 02,23,13 have margin > 1/3000. The other quotient pairs are safe, and C0 < 7/16 < 383/504. Diagnostic C0 is approximately 0.4302902609.

For deep endpoint pairs the contact margin is -1/2 - u_i dot u_j. For safe pairs it is 1/2 - |u_i dot u_j|. For each defective quotient pair the margin is -1/2 - w_i dot w_j.

## Reproducible proof

Run the pure-Python checker:

~~~text
python research/verify_typeE_F3_two_remaining_paths_rational_R3_2026_11_02.py
~~~

It uses fractions.Fraction, not floating-point arithmetic, for all proofs: exact unit norms, all endpoint contacts, exactly three quotient defects, midpoint orthogonality, and the rational energy and margin bounds. Floating-point values are printed only as diagnostics.

## Research implications

- **[PROVED EXACTLY]** Both remaining canonical three-defect path orbits are locally feasible, even in dimension three and with core midpoint energy below the global Type-E cap.
- **[CONDITIONAL ON RETAINED F3 STRUCTURAL LEMMAS]** The earlier triangle-free, four-cycle, and star exclusions plus the integer path Farkas certificate leave these two path orbits among three-defect canonical supports. Neither can be eliminated using the eight endpoints, their Gram PSD constraint, rank five, and the scalar core-energy cap alone.
- **[OPEN]** Coupling to the sixteen isolated deep edges, alternative-matching double-positive cases, lower-defect supports, Types C and D, generic e>=27, and non-isolated branches.
- **[GLOBAL PROVED RANGE UNCHANGED]** 40 <= tau_5 <= 44.

**Next priority:** build a finite cross-contact/rank-five obstruction involving at least some of the sixteen isolated edges, rather than seeking another dimension-free eight-endpoint Farkas contradiction for these two paths.
