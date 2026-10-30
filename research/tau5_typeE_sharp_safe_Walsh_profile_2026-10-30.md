# Type E: sharp safe-block Walsh profile and second-order rigidity

Date: 2026-10-30. **Global proved range unchanged: 40 <= tau_5 <= 44.**

## Proof status

**[PROVED EXACTLY — universal four-contact algebra]** Sharp piecewise bounds on midpoint/mixed Walsh energy and safe squared-contact slack in terms of the projected correlation, with a ternary quantization corollary.

**[PROVED EXACTLY — conditional on the retained Type-E 184-safe/six-core incidence and prior exact frame identities]** A strengthened six-exception/Petersen-Q necessary inequality with a new nonnegative penalty from all 114 safe meeting-support blocks.

**[OPEN]** This is not a Type-E exclusion; no incompatible upper bound is established. C,D, generic e>=27 and non-isolated branches remain open. The e=23/24 sparse classification still requires delta(G)>=1.

## 1. Sharp four-contact theorem

For two selected deep edges x_i^sigma=m_i+sigma*z_i, x_j^tau=m_j+tau*z_j, set

    p=m_i.m_j, b=z_i.m_j, c=m_i.z_j, h=z_i.z_j,
    t_(sigma,tau)=p+sigma*b+tau*c+sigma*tau*h.

Assume **all four** endpoint contacts are safe: |t_(sigma,tau)|<=1/2. Put

    d=|h|, T=p^2+b^2+c^2,
    W=T+d^2=(1/4)sum_(sigma,tau)t_(sigma,tau)^2,
    s=1/4-W>=0.

Then 0<=d<=1/2 and

    T <= F(d) = { 1/4-d+3d^2,       0<=d<=1/4;
                  3(1/2-d)^2,       1/4<=d<=1/2. }

Equivalently,

    s >= Phi(d) = { d(1-4d),               0<=d<=1/4;
                    (2d-1/2)(1-2d),       1/4<=d<=1/2. }

These bounds are **sharp for the abstract four-contact cube**, not asserted to be globally sharp for five-dimensional Type-E Gram realizations.

**Proof:** Set y_(sigma,tau)=sigma*tau*t_(sigma,tau). Walsh orthogonality gives sum y=4h, sum y^2=4W, and -1/2<=y<=1/2. Negate y if necessary to make h=d>=0. Let x=y+1/2 in [0,1], so sum x=2+4d. Convexity of the square implies sum x^2 is maximized by an extreme point with at most one nonendpoint coordinate. For d in [0,1/4], the extremal multiset is (1,1,4d,0), yielding sum y^2=1-4d+16d^2. For d in [1/4,1/2], it is (1,1,1,4d-1), yielding sum y^2=3-12d+16d^2. Divide by four, subtract d^2, and then subtract W from 1/4. Each extremizer is attainable within the four-contact cube.

## 2. Quantization and absorption

For d>=1/4, epsilon=1/2-d, the exact estimates are

    T<=3epsilon^2,   s>=epsilon(1-4epsilon).

Moreover each of |p|,|b|,|c| is <=epsilon. Indeed the four safe inequalities are equivalent to

    |p+h|+|b+c|<=1/2,
    |p-h|+|b-c|<=1/2.

They imply |p|+d<=1/2 and max(|p|,d)+max(|b|,|c|)<=1/2. When d>=1/4, |p|<=epsilon<=d.

For all 0<=d<=1/2,

    **dist(d,{0,1/4,1/2}) <= 2s**.

This follows from Phi(d)=4r(1/4-r), where r is distance to the nearer endpoint of the relevant quarter interval; the other factor is at least 1/8. Factor two is sharp at d=1/8 and 3/8.

If d>=3/8, **T<=(3/4)s**. If d>=7/16, **T<=s/4**. Both thresholds are sharp for the abstract contact cube. More generally, d>=1/2-eta with 0<eta<1/4 implies T<=[3eta/(1-4eta)]s. These are exact second-order near-contact mixing bounds.

## 3. Type-E six-exception/Petersen interface

Choose any combinatorial K5 support labeling with the four F3 core selected edges on four star supports. Let N70 denote the ten same-support plus sixty disjoint-support pairings (all safe), R114 the 114 safe meeting-support pairings, and K6 the six possibly exceptional core-core pairings. **No D5 geometric alignment is assumed.**

The previously proved exact Walsh conservation law is

    W70+X6=A-U+V_edge/2+S114,

where U=sum a_i^2, V_edge=||sum_i(m_i m_i^T+z_i z_i^T)-4I||_F^2, X6=sum_K6(W_ij-1/4) is SIGNED, and S114=sum_R114(1/4-W_ij).

The new theorem yields the stronger necessary inequality

    **W70+X6 >= A-U+V_edge/2+sum_R114 Phi(|z_i.z_j|).**      (A)

Let M_extra be the total Delsarte mass of the six nonmatching F3 deep endpoint contacts. The polynomial comparison gives X6<=M_extra/28. Decompose W70=T70+O+D into midpoint/mixed and projected squared correlations. The exact Petersen Q-SOS identity gives O+D<=E_Q/4, where E_Q=V_z+12C_z. Hence

    **T70+E_Q/4+M_extra/28
        >= A-U+V_edge/2+sum_R114 Phi(|z_i.z_j|).**          (B)

This adds a genuine nonnegative 114-block penalty to the earlier interface. It does not identify the six exceptional core pairings with the six Q-kernel modes.

Under the retained Type-E center-harmonic variance floor V_edge>24830289/80000000 and individual caps a_i<=1/4, a conditional consequence is

    T70+E_Q/4+M_extra/28
      > 3A/4+24830289/160000000+sum_R114 Phi(|z_i.z_j|).

This is a **necessary condition**, not a contradiction.

## 4. Verification and next target

Companion Python script verifies exact cube-slice vertex maxima at 101 rational d values, all 625 four-contact tuples from a five-value grid, ternary quantization, threshold absorption, and a rational safe-block geometric witness. The universal theorem is proved by the convexity argument, not by grid testing.

Next: split R114 into near-threshold (d>=3/8, mixing absorbed by safe-contact slack) and far-from-threshold (positive Phi penalty) branches in a small exact polynomial/KKT analysis. Need an incidence-sensitive incompatible upper bound before claiming Type-E exclusion.

Retain M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, Musin/Boyvalenkov's 21-line zero-midpoint exclusion, and **40<=tau_5<=44**.