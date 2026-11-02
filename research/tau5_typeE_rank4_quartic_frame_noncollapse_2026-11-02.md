# Type E: exact rank-four quartic harmonic cut and rank-five noncollapse

Date: 2026-11-02. **Global proved range unchanged:** `40 <= tau_5 <= 44`.

## Proof status

**[PROVED EXACTLY, UNIVERSAL]** The four-dimensional weighted quartic inequality below.

**[CONDITIONAL TYPE-E THEOREM]** For the canonical Type-E twenty-edge matching, with `A=sum ||m_i||^2<=383/504`, 184 safe projected pairs, six possible F3 exceptions each of defect `delta<=1/8`, and `Z=sum z_i z_i^T`, we have `lambda_min(Z)>1/4`. Using the separately retained exact defect budget `D<=1780062775/4032758016` strengthens this to `lambda_min(Z)>7/25`. Using the separately retained canonical path-only budget `D<366383/1016064` strengthens it to `lambda_min(Z)>29/100`. The latter uses prior F3 star/path exclusions; this note does not re-prove them.

**[OPEN]** No Type-E contradiction yet. The sixteen isolated edges must be coupled to the surviving local F3 paths. This result uses neither the withdrawn endpoint-Perron argument nor unproved D5 uniqueness.

## 1. Universal quartic rank-four inequality

For arbitrary `y_i in R^4`, put `t_i=||y_i||^2`, `s_ij=y_i.y_j`. Then

```
sum_(i<j) s_ij^2*(4*s_ij^2-t_i*t_j)
 >= (sum_i t_i^2)^2/8 - (3/2)*sum_i t_i^4.                 (1)
```

Proof: for `t_i>0`, normalize `v_i=y_i/sqrt(t_i)` and weight them by `w_i=t_i^2`. The polynomial

```
f(u)=(3/8)*u^2*(4*u^2-1)
    =(3/32)*P0(u)+(9/16)*P2(u)+(15/32)*P4(u)
```

has nonnegative coefficients in normalized Gegenbauer polynomials `P_k=C_k^1/(k+1)` for the three-sphere. The spherical-harmonic addition theorem gives `sum_ij w_i*w_j*f(v_i.v_j)>=(3/32)*(sum_i w_i)^2`. Since `w_i*w_j*f(v_i.v_j)=(3/8)*(4*s_ij^4-t_i*t_j*s_ij^2)`, separating the diagonal yields (1). Extend to zero vectors by continuity. In particular, (1) excludes sixteen unit projective lines in R4 of coherence <=1/2: its left side would be <=0 but its right side would equal 8.

## 2. Project the Type-E lines to a hyperplane

For an arbitrary unit `x in R^5`, set

```
a_i=||m_i||^2, A=sum_i a_i<=383/504, 0<=a_i<1/4,
c_i=x.z_i, e_i=c_i^2, E=sum_i e_i=x^T Z x,
y_i=z_i-c_i*x, t_i=1-a_i-e_i, T=sum_i t_i=20-A-E,
d_ij=z_i.z_j, s_ij=d_ij-c_i*c_j, u_ij=|c_i*c_j|.
```

Assume `E<=29/100` when testing a contradiction. Then all `t_i>0`. By (1), Cauchy `sum t_i^2>=T^2/20`, and `t_i^4<=t_i`,

```
sum_(i<j) s_ij^2*(4*s_ij^2-t_i*t_j)
 >= R(A,E):=T^4/3200-(3/2)*T.                           (2)
```

The 190 pairs have `|d_ij|<=1/2+delta_ij`, with `delta=0` except on the six core pairs, where `delta<=1/8`; let `D=sum delta`. Define `B_ij=a_i+a_j+e_i+e_j+4*u_ij+4*u_ij^2>=0`. As `u_ij<=E/2`,

```
4*s_ij^2-t_i*t_j <= B_ij+(9/2+4*E)*delta_ij.          (3)
```

For safe pairs, `s_ij^2<=1/4+(1+E/2)*u_ij`; for the six core pairs, `s_ij^2<=q(E):=(5+4E)^2/64`. The following bounds are exact:

```
sum_all B_ij <=19*A+57*E+2*E^2,
sum_core B_ij <=3*A+9*E+2*E^2,
sum_all u_ij*B_ij <=(9/4)*A*E+(17/4)*E^2+E^3.         (4)
```

For the last bound, use `|c_i| sum_(j!=i)|c_j|<=sqrt(19*e_i*(E-e_i))<=sqrt(19)*E/2<9*E/4`, `sum u^2<=E^2/2`, and `sum u^3<=E^3/4`. The core bounds use only that six possible exceptions form a K4. Equations (2)-(4) give the *necessary polynomial cut* `R(A,E)<=L(A,E,D)`, with

```
q=(5+4*E)^2/64,
L=(19*A+57*E+2*E^2)/4
 +(1+E/2)*((9/4)*A*E+(17/4)*E^2+E^3)
 +(q-1/4)*(3*A+9*E+2*E^2)
 +q*(9/2+4*E)*D.                                      (5)
```

## 3. Three exact rational noncollapse certificates

`L` increases with `A,E,D>=0`. `R` decreases with `A,E` on the tested domain because `d/dT[T^4/3200-3*T/2]=T^3/800-3/2>0` for `T>18`. At `A0=383/504`, the following are **strictly positive** exact gaps `R(A0,E0)-L(A0,E0,D0)`:

| Defect budget D0 | Tested E0 | Positive rational gap |
|---|---|---|
| 3/4 | 1/4 | 78380992451281/206477210419200 |
| 1780062775/4032758016 | 7/25 | 19455206461371049681/80655160320000000000 |
| 366383/1016064 | 29/100 | 11317880882876435281/80655160320000000000 |

Thus no unit `x` can have `x^T Z x<=E0` in the respective cases. By Rayleigh-Ritz, `lambda_min(Z)>E0`. This is a **quantitative rank-five spanning condition**, not a Type-E exclusion.

For either exact rational R3 witness of a surviving F3 path, if its core is fixed inside a hypothetical global extension, every unit direction `x` perpendicular to the three-dimensional core span must satisfy `sum_(sixteen isolated j)(x.z_j)^2>29/100` under the strongest retained budget. This is a concrete extension constraint.

**[OPEN]** A rank-five 40-endpoint polynomial/KKT model should retain the individual `a_i,e_i,delta_ij` and the quartic inequality (1), rather than only aggregate (5). Types C, D, generic `e>=27`, and non-isolated cases remain unresolved.

Verification: `research/verify_typeE_rank4_quartic_frame_noncollapse_2026_11_02.py`.
