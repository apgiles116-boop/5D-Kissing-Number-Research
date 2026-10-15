# Type E: exact wedge-mass stability (2026-10-15)

**Status:** NEW—PROVED EXACTLY, conditional only on the spherical-code geometry and the Delsarte polynomial. This does not eliminate Type E or improve the uniform midpoint-energy ceiling.

Let v,u,w be unit vectors with v·u=-p, v·w=-q, u·w<=1/2, and 1/2<=p,q<=1. Put r=p²+q², s=pq, M(t)=7t²(4t²-1), and d_p=21-M(p), d_q=21-M(q).

The nonnegative weights 2p-q and 2q-p, together with Cauchy–Schwarz, imply r-s<=3/4. Also r+s>=3/4. Exact polynomial expansion gives

    d_p+d_q-329/16
      = 28(r-11/8)^2 + 56(3/4-r+s)(r+s-3/4).

Both terms on the right are nonnegative. Thus the usual wedge mass bound has the exact second-order strengthening

    d_p+d_q-329/16 >= 28(p²+q²-11/8)^2.

**Equality classification:** If d_p+d_q=329/16, then r=11/8, s=5/8 and

    {p²,q²}={(11+sqrt(21))/16,(11-sqrt(21))/16},
    {d_p,d_q}={(329+63sqrt(21))/32,(329-63sqrt(21))/32}.

**Exact rational LP-disjunction:** Since d(t)=21+7t-28t² decreases on 1/4<=t<=1, and d(11/20)=819/50, d(9/10)=231/50, the following holds for *each ordered pair of incident deep edges*:

    d_p<=819/50 AND d_q<=231/50  ==>  d_p+d_q>=518/25.

Equivalently, at least one of d_p>819/50, d_q>231/50, or d_p+d_q>=518/25 must hold. The reverse ordering supplies a second disjunction.

The old closed scalar mass-polytope witness has deficits d_04=49/3, d_05=203/48, whose sum is 329/16; both are below the antecedent thresholds, yet the sum is below 518/25. It violates the cut at eight incident edge pairs. This excludes that particular mass-only witness, not all Type E geometry.

**Retained conditional ledger:** A<=62435281299/10^11 and sum_{i<j}(z_i·z_j)^2>=28.0956913934596. No stronger *uniform* bound is proved here. Global range remains 40<=tau_5<=44. Types C,D,E, generic e>=27, and the minimum-degree dependency remain open.

**Next task:** incorporate these rational disjunctions into the previously exceptional interval-restricted mass-polytope LP branches, and verify exact dual certificates for every surviving branch. No D5-labeling or six-exception correspondence is assumed.
