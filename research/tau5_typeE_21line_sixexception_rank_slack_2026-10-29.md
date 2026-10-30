# Type E: 21-line rank-14 / six-exception Walsh safe-slack theorem (2026-10-29)

**[PROVED EXACTLY — rank and scalar inequalities; TYPE-E APPLICATION CONDITIONAL ON RETAINED GRAPH/MATCHING REDUCTION].** This does not eliminate Type E. Global proved range remains `40<=tau_5<=44`.

## Statement

Assume the retained isolated-center Type E branch: twenty selected deep edges `x_i^±=m_i±z_i`, `a_i=||m_i||²<=1/4`, `||z_i||²=1-a_i`, `A=sum a_i<=B=383/504`, sixteen isolated edges and four F3 core edges, plus isolated unit center `v`. All 184 non-core/core blocks are fully safe; each of the six core/core blocks has at least one safe Walsh parity channel, for all three F3 perfect matchings.

Define the **204-safe squared slack**
```
H204 = sum_(184 safe selected pairs) (1/2-|z_i.z_j|)^2
     + sum_(20 center-selected pairs) (1/2-|v.z_i|)^2.
```
Then
```
H204 > 4833/100000 = 0.04833.                           (T)
```
This is a lower bound on a new 204-pair functional, not an upper bound or a Type-E exclusion.

## Proof 1: rank-14 defect

Normalize `u_i=z_i/sqrt(1-a_i)` and adjoin `u_0=v`. Set `Delta_ij=(u_i.u_j)^2-1/4`. The 21 traceless projectors `u_i u_i^T-I/5` have Gram rank at most 14. Compare with `K0=(3/4)I_21+(1/20)J_21`, whose 20 smaller eigenvalues equal `3/4`. Eckart--Young gives
```
2 sum_(i<j) Delta_ij² >= 7*(3/4)²,
sum_(i<j) Delta_ij² >= 63/32.                      (1)
```

## Proof 2: six-exception normalization bounds

For safe selected pairs let `w=(1-a_i)(1-a_j)`, `s=a_i+a_j`, `h=1/2-|z_i.z_j|>=0`. Then
```
(Delta_ij)_+ <= (1-w)/(4w) <= (7/18)s,
(-Delta_ij)_+ <= h/w <= h/(1-A).                    (2)
```
The coefficient `7/18` follows from `(1-w)/w <= (14/9)s` using `a_i,a_j<=1/4`. For center-selected safe pairs `(Delta_0i)_+ <= a_i/3`.

For each of the six exceptional core pairs, the surviving safe Walsh parity channel implies
```
|z_i.z_j| <= 1/2+|m_i.m_j| <= 1/2+sqrt(a_i*a_j).
```
Writing `p=a_i*a_j`, `s=a_i+a_j`, and `w=(1-a_i)(1-a_j)`, we obtain
```
(Delta_ij)_+ <= [sqrt(p)+s/4+3p/4]/w <= (3/2)s,  (3)
(-Delta_ij)_+ <= 1/4.
```
The last inequality in (3) uses `sqrt(p)<=s/2`, `p<=s/8`, and `w>=9/16`; the coefficient `3/2` is attained in the scalar closure at `a_i=a_j=1/4`.

## Proof 3: exact 21-line Walsh/rank bridge

Write `A_C=sum_(four core) a_i`, `U=sum a_i²`, `U_C=sum_(core) a_i²`. Exact combinatorics gives
```
sum_(190 selected pairs)(a_i+a_j)²=18U+A²,
sum_(6 core pairs)(a_i+a_j)²=2U_C+A_C²,
sum_(20 center pairs)a_i²=U.
```
Splitting positive and negative squared defects and applying (1)--(3) yields
```
63/32 <= H204/(1-A)²
       + (49/324)*(18U+A²-2U_C-A_C²)
       + U/9 + (9/4)*(2U_C+A_C²) + 6/16.
```
Thus the exact **new necessary inequality** is
```
H204 >= (1-A)² * [51/32-(17/6)U-(49/324)A²
                  -(170/81)*(2U_C+A_C²)].            (4)
```
A negative right side is vacuous. Using `U<=A/4`, `U_C<=A_C/4` gives the scalar envelope
```
H204 >= (1-A)² * [51/32-(17/24)A-(49/324)A²
                  -(170/81)*(A_C/2+A_C²)].           (5)
```

## Proof 4: exact rational split

The sixteen isolated directions plus center form a 17-line safe subframe. Its rank-14 estimate gives `H204>=H136>=f17(A_I)`, where `A_I=A-A_C` and
```
f17(t)=(1-t)²*[27/32-(361/648)t-(49/324)t²].
```
This is positive and decreasing on `0<=t<=B`. Set `c0=64/625`.

If `A_C>=c0`, then
```
H204 >= f17(B-c0)
     = 22025252761259802036053/455710657500000000000000
     > 4833/100000.
```
If `A_C<=c0`, the bracket in (5) is positive at `(B,c0)` and decreases in both arguments. Therefore
```
H204 >= (1-B)²*[51/32-(17/24)B-(49/324)B²
                 -(170/81)*(c0/2+c0²)]
     = 11278777913463577/233323856640000000
     > 4833/100000.
```
Exact rational margins are, respectively,
```
756684284802036053/455710657500000000000000,
2235922052377/233323856640000000.
```

## Proof-status ledger

- **[PROVED EXACTLY]** 21-line rank defect, exceptional normalized coefficient `3/2`, 204-safe/six-exception inequality (4), and conditional Type-E rational slack floor (T).
- **[VERIFIED]** Companion standard-library Fraction checker checks all rational constants and enumerates all three F3 perfect matchings, confirming that deep cross-contacts of any core/core pair occupy at most one Walsh parity channel.
- **[OPEN]** Need a sufficiently strong *upper* bound on `H204` or a sign-sensitive global certificate. This lower bound alone is not contradictory.
- **[RETAINED]** Star `70/3`, broom `M(F3)<=89`, matching `M(P)>=S/2-28/3`, 20-edge mass `>=2137/6`, midpoint cap `A<=383/504`, and source-audited Musin/Boyvalenkov 21-line zero-midpoint exclusion.
- **[GLOBAL PROVED RANGE — UNCHANGED]** `40<=tau_5<=44`. Types C/D, generic `e>=27`, non-isolated branches remain open. Sparse `e=23,24` graph classification is conditional on `delta(G)>=1`.

Verifier: `research/tau5_typeE_21line_sixexception_rank_slack_2026-10-29_verify.py`.
