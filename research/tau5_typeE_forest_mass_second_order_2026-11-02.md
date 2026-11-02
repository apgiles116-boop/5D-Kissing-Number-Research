# Type E: exact forest midpoint-mass and quadratic-defect ceilings (2026-11-02)

**[PROVED EXACTLY — scalar optimization, conditional on stated geometric inputs]** Assume four midpoint masses 0 <= a_i < 1/4, total C <= A0=383/504, and positive singleton defects delta_ij <= f(a_i+a_j), where f(t)=t(1-t)/2. Assume their support is a forest on four vertices (as supplied by the independently retained F3 triangle-free and C4-exclusion lemmas). Put D=sum delta_ij, S=sum delta_ij^2, and g(t)=f(t)+f(t)^2.

Since g'(t)>=0 and g''(t)=2(1/2-t)^2-1-2f(t)<=-1/2 on 0<=t<=1/2, both f and g are increasing and concave. There are only three support cases:

* At most two edges: D<1/4 and D+S<9/32.
* Three-edge star with center mass x: Jensen gives sum h(x+a_leaf) <= 3h((C+2x)/3) < 3h((A0+1/2)/3) for h=f or g, using x<1/4.
* Three-edge P4: average the mass assignment with its path reversal by concavity. The symmetric masses (x,y,y,x) give arguments C/2,2y,C/2, hence sum h <= 2h(A0/2)+h(1/2).

The star dominates the other cases by exact rational comparison at A0. With t0=(A0+1/2)/3=635/1512, the **new exact canonical ceilings** are

    D < 3f(t0) = 556895/1524096 = 0.365393649743848...
    D+S < 3g(t0) = 2856416366785/6968605851648
        = 0.409897822834892...

These improve D<3/8 and D+S<27/64 without invoking the stronger A<0.567 harmonic certificate. The scalar extremizer is not claimed to be realizable by a complete F3 Gram matrix.

**[PROVED EXACTLY — quantitative mass concentration, conditional canonical F3]** The same inequalities hold with actual C in place of A0. At C=2/3 the star upper bound for D+S is 55825/139968<2/5, and the P4 bound is 2009/5184<2/5. Therefore D+S>=2/5 forces C>2/3, leaving less than 47/504 of total midpoint mass for the sixteen isolated edges. This is a second-order necessary condition, not an exclusion.

**[CONDITIONAL — six-exception Q transfer]** Canonical P0 has six possibly exceptional pairs, so Q_core<=3/2+D+S<1.909897822834892. With the retained baseline Q_total>8790283/317520, the 184 safe pairs have Q_safe>25.7742890000424, forcing at least 39 with |z_i.z_j|>1/3. **[FURTHER CONDITIONAL]** With the separately retained center-sensitive Q_total>141813/5000, Q_safe>26.4527021771651, forcing at least 44 of 184. The upstream center-sensitive certificate is not re-proved here.

**[PROVED EXACTLY — alternative double-defect-zero branch, conditional F3]** In either alternative F3 matching, the four singleton pairs form a C4. If the double-contact pair has no positive defect, any three-edge support is a P4. Therefore

    D < 366383/1016064 = 0.360590474615772...
    D+S < 834099607777/2064772104192 = 0.403966910480615...

Only five core pairs can be exceptional, giving Q_core<1.653966910480615. Baseline Q_total gives Q_safe>26.0302199123967 for 185 safe pairs (at least 40 high-correlation pairs). The further conditional center-sensitive Q_total gives Q_safe>26.7086330895194 (at least 45 of 185 high-correlation pairs). The alternative **double-positive** branch remains OPEN.

**[FURTHER CONDITIONAL — stronger harmonic A<567/1000]** The same star formulas give D<2062511/6000000=0.3437518333 and D+S<41379149625121/108000000000000=0.3831402743. This stronger harmonic input is not substituted silently for baseline A<=383/504.

**[VERIFIED EXACT ARITHMETIC]** Companion Fraction checker verifies all 38 triangle-free/C4-free labeled supports, exact star/path comparisons, rational Q transfers, and integer thresholds. No generic SDP, D5 uniqueness or Q-kernel-to-exception identification is used. The earlier invalid endpoint-Perron argument remains WITHDRAWN.

**[OPEN]** No Type-E elimination or proof of tau_5=40. Global proved range stays 40<=tau_5<=44. Types C, D, generic e>=27, and non-isolated branches remain open; e=23/24 classification requires delta(G)>=1. Preserve the exact Type-E star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, 20-edge mass >=2137/6, and the audited Musin/Boyvalenkov 21-line zero-midpoint exclusion. Next: combine the high-defect mass concentration with the sixteen isolated edges' rank-five Gram and mixed-Walsh constraints.