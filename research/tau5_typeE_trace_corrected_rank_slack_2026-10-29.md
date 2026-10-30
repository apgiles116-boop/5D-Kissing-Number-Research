# Trace-corrected rank-14 Walsh slack: exact Type-E theorem (2026-10-29)

**[PROVED EXACTLY — rank theorem; TYPE-E APPLICATION CONDITIONAL on retained graph/matching and midpoint cap].** The global proved range remains `40<=tau_5<=44`.

## 1. Rank theorem

For unit `u_1,...,u_n in R^5` with `n>14`, put `Delta_ij=(u_i.u_j)^2-1/4`. Then

```
sum_(i<j) Delta_ij^2 >= 9*n*(n-14)/448.                  (R)
```

Thus the floors at `n=16,17,20,21` are `9/14, 459/448, 135/56, 189/64`, respectively. This improves the earlier rank-only bound `9(n-14)/32` by a factor `n/14`.

**Proof.** The Gram matrix `K_ij=tr[(u_i u_i^T-I/5)(u_j u_j^T-I/5)]` is PSD, rank at most 14, diagonal `4/5`. Let `M=(3/4)I+(1/20)J`, `E=K-M`. Then `E_ii=0`, `E_ij=Delta_ij`, `tr E=0`, and `||E||_F^2=2 sum Delta_ij^2`. Let `P` project orthogonally onto `ker K`, with rank `k>=n-14`. Since `KP=0`,

```
-tr(PE)=tr(PM)=3k/4+||P1||^2/20 >=3k/4.
```

The trace-zero condition yields
```
|tr(PE)|=|tr((P-kI/n)E)|
       <=sqrt(k(n-k)/n) ||E||_F.
```
Consequently `||E||_F^2 >= (9/16)nk/(n-k) >= (9/16)n(n-14)/14`. This proves (R). The kernel-sensitive exact refinement is
```
sum Delta_ij^2 >= n/[2k(n-k)]*(3k/4+||P1||^2/20)^2.    (RK)
```
A positive uniform bound on `||P1||` is *not* asserted.

## 2. 21-line Type-E consequence

Retain `x_i^±=m_i±z_i`, `a_i=||m_i||^2<=1/4`, `||z_i||^2=1-a_i`, `A=sum a_i<=B=383/504`; 16 isolated selected deep edges, four selected F3 core edges, and isolated center `v`. Let `A_C=sum_core a_i`, `U=sum a_i^2`, `U_C=sum_core a_i^2`. All 184 non-core/core selected pair blocks and all 20 center blocks are fully safe.

Define
```
H204 = sum_(184 safe selected pairs) (1/2-|z_i.z_j|)^2
     + sum_(20 center-selected pairs) (1/2-|v.z_i|)^2.
```

For a safe selected pair, `w=(1-a_i)(1-a_j)`, `s=a_i+a_j`, `h=1/2-|z_i.z_j|>=0`, normalized squared-correlation defect `Delta` obeys
```
(Delta)_+ <= (7/18)s,   (-Delta)_+ <= h/(1-A).
```
The first inequality follows from `(1-w)/w <= (14/9)s`: use `a/(1-a)<=4a/3`, `ab/((1-a)(1-b))<=16ab/9<=2s/9`. Center blocks give `(Delta_0i)_+<=a_i/3`, `(-Delta_0i)_+<=h/(1-A)`.

For each of six potentially exceptional core pairs, **all four universal upper kissing inequalities** imply `m_i.m_j+|z_i.z_j|<=1/2`; hence `|z_i.z_j|<=1/2+sqrt(a_i a_j)`. With `p=a_i a_j`, `s=a_i+a_j`, `w=(1-a_i)(1-a_j)`, this gives
```
(Delta)_+ <= (sqrt(p)+s/4+3p/4)/w <= (3/2)s,
(-Delta)_+ <=1/4.
```
The last step uses `sqrt(p)<=s/2`, `p<=s/8`, `w>=9/16`. Importantly, this estimate does not incorrectly infer absolute control from only one safe Walsh parity channel.

Exact combinatorics:
```
sum_(190 pairs)(a_i+a_j)^2=18U+A^2,
sum_(6 core pairs)(a_i+a_j)^2=2U_C+A_C^2,
sum_(20 center pairs)a_i^2=U.
```
Using (R) at `n=21` and splitting positive/negative defects gives
```
189/64 <= H204/(1-A)^2
        +(49/324)*(18U+A^2-2U_C-A_C^2)
        +U/9+(9/4)*(2U_C+A_C^2)+6/16.
```
Thus
```
H204 >= (1-A)^2*[165/64-(17/6)U-(49/324)A^2
                  -(170/81)*(2U_C+A_C^2)].           (T21)
```
Using `U<=A/4` and `U_C<=A_C/4`,
```
H204 >= (1-A)^2*[165/64-(17/24)A-(49/324)A^2
                  -(170/81)*(A_C/2+A_C^2)].          (S21)
```

## 3. 17-line fallback and exact uniform split

The 16 isolated directions and center form a fully safe 17-line subframe. With `A_I=A-A_C`, its 136 safe slacks satisfy
```
H204 >= H136 >= f17(A_I),
f17(t)=(1-t)^2*[459/448-(361/648)t-(49/324)t^2].    (S17)
```
`f17` is positive and decreasing on `[0,B]`.

Set `c0=11/70`. If `A_C>=c0`, then
```
H204 >= f17(B-c0)
     = 3809520955097/38093690880000
     = 1/10 + 151867097/38093690880000 > 1/10.
```
If `A_C<=c0`, the positive bracket in (S21) decreases with `A,A_C`, so
```
H204 >= (1-B)^2*[165/64-(17/24)B-(49/324)B^2
                  -(170/81)*(c0/2+c0^2)]
     = 10457848720099/104529087774720
     = 1/10 + 4939942627/104529087774720 > 1/10.
```

**[PROVED EXACTLY — CONDITIONAL TYPE E]** `H204>1/10`. This more than doubles the previous uniform floor `H204>4833/100000`, but is a **lower** bound and does not eliminate Type E.

**[OPEN]** Obtain an incompatible upper bound on H204 or control the kernel-orientation term in (RK). No D5 labeling or five Q-cycle relations are assumed. Types C/D, generic e>=27, and non-isolated branches remain open; sparse e=23/24 classification requires delta(G)>=1.

**[RETAINED]** Star 70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, mass >=2137/6, A<=383/504, and source-audited Musin/Boyvalenkov 21-line boundary exclusion.

Verifier: `research/tau5_typeE_trace_corrected_rank_slack_2026-10-29_verify.py`.
