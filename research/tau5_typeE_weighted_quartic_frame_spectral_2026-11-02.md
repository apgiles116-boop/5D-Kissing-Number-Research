# Type E: weighted quartic frame noncollapse (2026-11-02)

**Global proved range unchanged: 40 <= tau_5 <= 44.**

## Proof status

**[PROVED EXACTLY — universal]** The capped-mass spectral estimate and joint mixed-moment estimate below.

**[CONDITIONAL TYPE E — all selected matching types]** Suppose twenty disjoint strict deep edges satisfy midpoint energy A <= 383/504, only six core projected pairings may exceed 1/2, and the retained raw-defect bound D <= 1780062775/4032758016 holds for this selection. Then their projected frame Z satisfies **lambda_min(Z) > 297/1000**, irrespective of which of the three F3 perfect matchings is selected. In particular, no canonical-selection assumption is used in this conclusion.

**[FURTHER CONDITIONAL — singleton/canonical]** With six singleton exceptions, delta <= 1/8, the lower bound is >63/200 without the global D bound and >343/1000 with it. If the selected matching is canonical with the retained path-only defect support and D < 366383/1016064, then **lambda_min(Z)>3/8**.

**[OPEN]** Type E is not excluded. Type C, Type D, generic e>=27 and non-isolated branches remain open. The withdrawn endpoint-Perron argument is not used.

## 1. Quartic harmonic setup

For selected deep edges, let unit endpoints be m_i +/- z_i, with m_i.z_i=0, a_i=||m_i||^2<1/4, ||z_i||^2=1-a_i, A=sum a_i<=A0=383/504. For any unit x in R^5 define c_i=x.z_i, e_i=c_i^2, E=sum e_i=x^TZx, y_i=z_i-c_i*x in R^4, t_i=||y_i||^2=1-a_i-e_i, and s_ij=y_i.y_j.

The exact S^3 Gegenbauer-positive inequality is

    sum_(i<j) s_ij^2*(4*s_ij^2-t_i*t_j)
      >= (sum_i t_i^2)^2/8 - (3/2)*sum_i t_i^4.            (1)

By the previously proved capped-mass Karamata majorization, for E<=3/8,

    sum_i t_i^4 <= U(A,E),
    U(A0,E)=16+2*(3/4)^4+(499/504)^4+(3/4-E)^4.

Cauchy gives sum t_i^2 >=(20-A-E)^2/20. Hence the left side of (1) is at least

    R(A,E)=(20-A-E)^4/3200-(3/2)*U(A,E).

For 0<=A<=A0, 0<=E<=3/8, R is decreasing in A,E: on each majorization interval the derivatives of U lie in [-4,0], whereas -(20-A-E)^3/800+6<0. Therefore R(A,E)>=R0(E0) whenever E<=E0, where

    R0(E)=(20-A0-E)^4/3200
       -(3/2)*(16+2*(3/4)^4+(499/504)^4+(3/4-E)^4).      (2)

## 2. NEW weighted midpoint-mass bound

Put u_ij=|c_i*c_j|=sqrt(e_i e_j), v_i=sqrt(e_i). Then

    J_a=sum_(i<j)u_ij*(a_i+a_j)=v^T M v,
    M_ij=(a_i+a_j)/2 (i!=j), M_ii=0.

Writing a=(a_i), 1=(1,...,1),

    M=(a 1^T+1 a^T)/2-diag(a) <= (a 1^T+1 a^T)/2

in PSD/Loewner order. The rank-two right-hand matrix has top eigenvalue (A+sqrt(20*sum a_i^2))/2. The cap 0<=a_i<=1/4 and A<=3/4+5/504 gives, by convex concentration,

    sum a_i^2 <= 3/16+(5/504)^2 = 47653/254016.

The exact difference

    (27/10-A0)^2-20*(47653/254016)
      = 75821/6350400 >0

proves

    J_a <= (27/20)*E.                                     (3)

The older bound (109/50)*A*E has coefficient about 1.65663 at A0; (3) reduces it to 1.35.

## 3. NEW joint quartic mixed bound

Set J_e=sum_(i<j)u_ij*(e_i+e_j). For E>0 let p_i=e_i/E and T=sum p_i^2. Cauchy yields

    J_e/E^2
      =sum_i p_i^(3/2)*sum_(j!=i)sqrt(p_j)
      <=sqrt(19)*sum_i p_i*sqrt(p_i*(1-p_i)).

Since f(t)=sqrt(t(1-t)) is concave on [0,1], weighted Jensen gives J_e/E^2<=sqrt(19*T*(1-T)). Also 4*sum u_ij^2=2*E^2*(1-T). Thus

    (J_e+4*sum u_ij^2)/E^2
      <=sqrt(19*T*(1-T))+2*(1-T)
      <=1+sqrt(23)/2 <17/5,                               (4)

where the final inequality follows from 23<576/25. Moreover sqrt(e_i e_j)<=(e_i+e_j)/2 and e_i*(E-e_i)<=E^2/4 give sum u_ij^3<=E^3/8.

With B_ij=a_i+a_j+e_i+e_j+4u_ij+4u_ij^2, (3)-(4) imply the **universal** estimate

    sum_all u_ij*B_ij
       <= J(E):=(27/20)*E+(17/5)*E^2+E^3/2.              (5)

The E=0 case follows by continuity.

## 4. Exact upper polynomials

For projected g_ij=z_i.z_j and defect delta_ij=(|g_ij|-1/2)_+, write D=sum delta_ij. The 184 safe pairings have |g_ij|<=1/2. All pairs satisfy

    4*s_ij^2-t_i*t_j
      <=B_ij+(4+4delta_ij+8u_ij)*delta_ij.

The elementary bounds are

    sum_all B_ij <=19A+57E+(19/10)E^2,
    sum_exception B_ij <=3A+9E+2E^2.                     (6)

The second uses only the six possible exceptional edges on four F3 quotient indices.

For **any matching**, averaging all four endpoint cross-products gives m_i.m_j+|g_ij|<=1/2, hence delta_ij<=sqrt(a_i a_j)<1/4. For exceptional pairs, s_ij^2<=q_alt(E):=(3+2E)^2/16 and the defect multiplier is <=5+4E. For safe pairs, s_ij^2<=1/4+(1+E/2)u_ij. Therefore the left side of (1) is at most

    L_alt(A,E,D)
      =[19A+57E+(19/10)E^2]/4
       +(1+E/2)*J(E)
       +(q_alt(E)-1/4)*(3A+9E+2E^2)
       +q_alt(E)*(5+4E)*D.                               (7)

This is coefficientwise nondecreasing in A,E,D.

For **six singleton exceptions**, delta<=1/8, replace q_alt by q_single(E)=(5+4E)^2/64 and the multiplier (5+4E) by (9/2+4E); call the result L_single.

For **canonical path-only support**, replace the factor (3A+9E+2E^2) in L_single by (2A+21E/4+E^2), using path degree <=2, adjacency spectral radius <13/8 and bipartite sum_edge e_i e_j<=E^2/4; call this L_path.

## 5. Rational certificates

If E<=E0, (1)-(7) require R0(E0)<=L(A0,E0,D0). Exact arithmetic gives the following *positive* contradiction gaps:

| Branch | E0 | R0(E0)-L(A0,E0,D0) |
|---|---|---|
| Any matching, D<=3/2 | 37/200 | 170756865083663731/5040947520000000000 |
| Any matching, retained D<=1780062775/4032758016 | **297/1000** | **232166826351874649779/12602368800000000000000** |
| Singleton exceptions, D<=3/4 | 63/200 | 65464532636720153/2520473760000000000 |
| Singleton exceptions, retained global D | 343/1000 | 102410241566713858021/3150592200000000000000 |
| Canonical singleton path, D<366383/1016064 | **3/8** | **300860069611/12904825651200** |

The exact verifier checks all five gaps, polynomial monotonicity, Gegenbauer coefficients, Jensen concavity, and rational relaxations.

## 6. Limitations

The matching-independent >0.297 noncollapse certificate is a necessary geometric condition, not a Type-E exclusion. The canonical >3/8 certificate still assumes that the canonical matching is the one satisfying the twenty-edge energy cap. The five local D5 Q-kernel relations are not identified with the six exceptional pairings. The separate center-sensitive Q_total>28.3626 certificate is not used.

Retain the correct F3 broom bound M(F3)<=89, matching mass M(P)>=S/2-28/3, selected-edge mass >=2137/6, and A<=383/504. The next target is a polynomial Gram/KKT cut retaining the individual six defects rather than replacing them by a common 1/4 or 1/8 cap.

Verifier: research/verify_typeE_weighted_quartic_frame_spectral_2026_11_02.py.
