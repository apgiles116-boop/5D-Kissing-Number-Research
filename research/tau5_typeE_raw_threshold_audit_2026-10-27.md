# Type E: fixed-threshold versus weighted-harmonic defect — exact audit and mixing-corrected bridge

Date: 2026-10-27.

**[PROVED EXACTLY — algebra]** The fixed-threshold and weighted-harmonic quartic defects differ by a nonnegative midpoint correction. **[PROVED EXACTLY — conditional on Type-E endpoint-safe pairings]** A new upper bound retains the 184 safe-pair mixing penalties and the six core-pair excesses. **[CORRECTION]** The previously asserted implication `D_raw <= P_raw` in `tau5_typeE_center_O4_harmonic_branching_2026-10-27.md` is not valid for nonzero midpoint energies. The fourth-harmonic identity itself remains valid. **[OPEN]** No Type-E exclusion.

## 1. Distinguish the thresholds

For twenty selected deep edges write unit endpoints `m_i +/- z_i`, `a_i=||m_i||^2`, `r_i=||z_i||^2=1-a_i`, `A=sum a_i`, and `U=sum a_i^2`. Set

```
w_ij = (z_i.z_j)^2,  h_ij = 1-r_i*r_j = a_i+a_j-a_i*a_j,
D_weighted = sum_{i<j} w_ij*(w_ij-r_i*r_j/4),
P_fixed = sum_{i<j} [w_ij*(w_ij-1/4)]_+,
E_fixed = sum_{i<j} [w_ij*(1/4-w_ij)]_+.
```

Here `[t]_+=max(t,0)`. The six-exception bound `P_fixed <= 1780062775/4032758016` uses the **fixed raw threshold 1/4**. It is not an upper bound on `D_weighted`. The exact identity is

```
D_weighted = P_fixed-E_fixed + (1/4)*sum_{i<j} h_ij*w_ij.  (1)
```

The last term is nonnegative. It cannot be silently discarded from an upper bound.

**Exact endpoint-safe local counterexample:** In R^5 take

```
z1=(1/2,1/2,1/2,0,0),       m1=(0,0,0,0,1/2),
z2=(1/2,1/2,0,1/2,0),       m2=(1/(2 sqrt(2)),-1/(2 sqrt(2)),0,0,0).
```

Each pair `m_i +/- z_i` consists of unit endpoints, `m_i.z_i=0`, and all four cross-endpoint inner products are exactly `+/- 1/2`. Yet `r1=r2=3/4`, `w12=1/4`, so the fixed positive defect is zero while the weighted defect is `7/256>0`. This is a two-edge counterexample to the *algebraic implication*, not a 20-edge Type-E realization.

## 2. Mixing-corrected six-exception bridge

Let `R` denote the 184 endpoint-safe edge-edge pairs and `K` the six core-core pairs. For each safe pair set

```
B=m_i.m_j, X=m_i.z_j, Y=z_i.m_j, Z=z_i.z_j,
T_ij=B^2+X^2+Y^2.
```

The Walsh/Parseval identity for the four cross-endpoint inner products, all of absolute value at most `1/2`, proves

```
w_ij+T_ij <= 1/4  for every (i,j) in R.              (2)
```

Put `delta_ij=[w_ij-1/4]_+` for core pairs. From (1), (2), and `E_fixed>=sum_R w_ij*T_ij` we obtain the **exact necessary upper bound**

```
D_weighted <= P_fixed
  + 19*A/16 - (A^2-U)/32
  + (1/4)*sum_K h_ij*delta_ij
  - sum_R (w_ij+h_ij/4)*T_ij.                        (3)
```

Proof: on safe pairs, `w<=1/4-T`; on core pairs, `w<=1/4+delta`. Apply these inequalities to `(1/4)sum h*w` in (1), subtract `E_fixed>=sum_R w*T`, and use

```
sum_{i<j} h_ij = 19*A - (A^2-U)/2.                  (4)
```

All quantities in (3) are polynomial in the original projected and midpoint vectors. The final safe-pair mixing term is nonnegative and must be **retained** in a sharp KKT/SOS calculation. It cannot be replaced by an all-pair mixing sum without justification.

## 3. Corrected fourth-harmonic budget

The universal O(4)-decomposed identity from the prior note remains valid:

```
D_weighted = R2^2/56 - 3*S4/8
 + 5*W/24 + 21*h0^2/16 + ||L||^2/3 + ||B4||^2/24
 + 2*||T3||^2 + ||T4||^2/2.
```

Here `R2=sum r_i^2`, `S4=sum r_i^4`, `W` is the weighted frame variance, and `h0,L,B4,T3,T4` are the five harmonic sectors defined in that note. The **correct** necessary comparison is

```
5*W/24 + 21*h0^2/16 + ||L||^2/3 + ||B4||^2/24
 + 2*||T3||^2 + ||T4||^2/2
 <= P_fixed - R2^2/56 + 3*S4/8
    + 19*A/16 - (A^2-U)/32
    + (1/4)*sum_K h_ij*delta_ij
    - sum_R (w_ij+h_ij/4)*T_ij.                      (5)
```

The earlier equation that omitted the midpoint correction is **withdrawn**.

For a coarse label-free numerical envelope, `h_ij<=7/16` (as `0<=a_i<=1/4`), `sum_K delta_ij<=5792292955405/4129544208384`, and `U<=Phi(A)=k/16+(A-k/4)^2` with `k=floor(4A)`. The function `19A/16-(A^2-Phi(A))/32` increases on `0<=A<=383/504`. Therefore

```
(1/4)*sum h_ij*w_ij
 <= 19*A/16 - (A^2-U)/32 + (7/64)*P_hom
 <= 39403364934925/37755832762368
 ~= 1.043636494073.
```

Thus a valid but weak scalar replacement for the withdrawn `D_weighted<=0.44140084` is

```
D_weighted <= 392481748566875/264290829336576
           ~= 1.485037333880.                       (6)
```

This scalar bound is deliberately not called sharp. Equation (5), with the *negative* safe mixing term, is the useful research object.

## 4. Proof ledger

**[RETAINED, not re-proved here]** Global `40<=tau_5<=44`; Type-E `1/49<A<=383/504`; exact broom `M(F3)<=89`; matching `M(P)>=S/2-28/3`; twenty-edge mass `>=2137/6`; zero-midpoint exclusion via Musin/Boyvalenkov; 184 safe pairings plus six core exceptions. The previously established raw squared-correlation floor remains unaffected.

**[OPEN]** The correction does not exclude Type E. Types C, D, generic `e>=27`, and non-isolated branches remain open. Sparse `e=23,24` classification assumes `delta(G)>=1`. The next rigorous task is a small polynomial/KKT or SOS certificate using (5), the individual core `delta_ij`, and safe mixing `T_ij`, rather than a bare scalar positive-defect cap.

Companion exact SymPy verifier: `research/tau5_typeE_raw_threshold_audit_2026-10-27_verify.py`.
