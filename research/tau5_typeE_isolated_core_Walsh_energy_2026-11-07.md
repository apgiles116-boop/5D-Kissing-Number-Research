# Type E: exact four-contact Walsh energy bound for isolated/core mixing

**2026-11-07. [PROVED EXACTLY — universal four-contact identity and conditional Type-E application].** Global proved range remains `40 <= tau_5 <= 44`. Type E remains **OPEN**.

## The overlooked safe-pair information

For any two selected deep edges with endpoints `p_i^s=m_i+s z_i` and `p_j^t=m_j+t z_j`, `s,t in {+1,-1}`, define four scalar products

`c=m_i.m_j, d=z_i.z_j, e=z_i.m_j, f=m_i.z_j`.

The four cross-endpoint contacts are `g_st=c+s*e+t*f+s*t*d`. Walsh orthogonality gives the exact identity

```
(1/4) sum_{s,t} g_st^2 = c^2+d^2+e^2+f^2.       (1)
```

If **all four cross-endpoint contacts are safe** (absolute value <=1/2), then

```
(z_i.z_j)^2 + (m_i.m_j)^2
 +(z_i.m_j)^2 +(m_i.z_j)^2 <=1/4.                (2)
```

The four nonnegative squares must be retained jointly. In particular, merely bounding the projected correlation by 1/2 discards three distinct penalties.

## The isolated/core 16-by-4 block

For Type E, let I denote the sixteen isolated selected deep edges and C the four selected F3 edges. Every I-C endpoint pairing is safe, regardless of which of the three F3 perfect matchings was selected. Define PSD operators

`Z_I=sum_{i in I} z_i z_i^T`, `M_I=sum_{i in I} m_i m_i^T`,
and similarly `Z_C,M_C`.

Summing (1)-(2) over the 64 I-C edge pairs gives

```
Q_IC + tr(M_I M_C) + tr(Z_I M_C) + tr(M_I Z_C) <=16,       (3)
Q_IC := tr(Z_I Z_C)=sum_{i in I,j in C}(z_i.z_j)^2.
```

Equivalently, for the endpoint-average frame operators
`F_I=M_I+Z_I`, `F_C=M_C+Z_C`,

```
tr(F_I F_C) <=16,   tr(F_I)=16, tr(F_C)=4.                (4)
```

The exact nonnegative slack in (3) is

```
16 - tr(F_I F_C)
 = (1/4) sum_{i in I,j in C,s,t} [1/4-(p_i^s.p_j^t)^2]. (5)
```

There are 64 selected-edge pairs and 256 safe endpoint pairs in (5). The factor 1/4 is essential.

For each core j, a finer row-wise inequality is

```
z_j^T Z_I z_j + z_j^T M_I z_j
 +m_j^T Z_I m_j+m_j^T M_I m_j <=4.            (6)
```

## Coupling to the previously proved block-variance identity

Put `T_I=tr(Z_I)=16-B`, `T_C=tr(Z_C)=4-C`,
`V_I=||Z_I-(T_I/5)I_5||_F^2`, and
`V_C=||Z_C-(T_C/5)I_5||_F^2`.
Then exactly

```
Q_IC = T_I*T_C/5
       + <Z_I-(T_I/5)I_5, Z_C-(T_C/5)I_5>.     (7)
```

Equations (3) and (7) imply the explicit necessary inequality

```
<Z_I^0,Z_C^0>
 +tr(M_I M_C)+tr(Z_I M_C)+tr(M_I Z_C)
 <=16-(16-B)*(4-C)/5.                         (8)
```

This is the missing *signed mixed-frame* interface: it simultaneously controls the traceless-frame interaction and three distinct midpoint interactions. It is strictly stronger as an identity of retained nonnegative terms than the coarse `Q_IC<=16`, but no numerical improvement is claimed without independent lower bounds on the midpoint traces or the mixed traceless product.

**[VERIFIED EXACT FINITE ARITHMETIC]** Companion checker verifies all 16 Walsh coefficients exactly using integers and the 64/256 incidence counts. The PSD/trace statements follow analytically.

**[OPEN]** Need a lower bound for the three midpoint traces or an upper/lower signed constraint for `<Z_I^0,Z_C^0>` strong enough to contradict the total midpoint cap `A<=383/504`. This note does not prove such a bound. No D5 labeling or Q-kernel/exception bijection is assumed.

**[RETAINED, NOT REPROVED]** Type-E star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, midpoint ceiling A<=383/504, Musin/Boyvalenkov zero-midpoint exclusion. Types C,D, generic e>=27 and non-isolated branches open; e=23/24 sparse classification conditional on delta(G)>=1.
