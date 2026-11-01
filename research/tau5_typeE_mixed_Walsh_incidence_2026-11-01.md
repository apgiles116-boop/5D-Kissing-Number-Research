# Type E: mixed-Walsh budget and exact F3 matching-incidence refinement

2026-11-01. **[PROVED EXACTLY — conditional on retained Type-E harmonic/scalar certificates]** for the energy bound. **[PROVED EXACTLY — standalone graph/Walsh algebra]** for incidence. No Type-E exclusion. Global proved range **40 <= tau_5 <= 44**.

## The mixed-Walsh identity

For the twenty selected deep edges write endpoints as `m_i +/- z_i`, with `m_i.z_i=0`, `a_i=||m_i||^2`, `A=sum a_i`, `U=sum a_i^2`. Let

`S_m=sum m_i m_i^T`, `S_z=sum z_i z_i^T`, `T=uu^T+2(S_m+S_z)-(41/5)I_5`, `q=u^T T u`, and `V_z=||S_z-(20-A)I_5/5||_F^2`, where `u` is the isolated center.

The *mixed Walsh energy* is

`R=sum_{i<j} [(m_i.m_j)^2+(m_i.z_j)^2+(z_i.m_j)^2]`.

**[EXACT IDENTITY]**

`R = 1/10+4A-A^2/10-U/2-q/4+||T||_F^2/8-V_z/2.`  (1)

Indeed, with `C_z=sum_{i<j}(z_i.z_j)^2`, polarization and `m_i.z_i=0` give
`R+C_z=(||S_m+S_z||_F^2-20+2A-2U)/2`.
The center identity gives
`||S_m+S_z||_F^2=401/5-q/2+||T||_F^2/4`.
Subtract the exact Q-frame identity
`C_z=30-3A+A^2/10-U/2+V_z/2`.
No D5 labeling or SDP is used.

## Strict Type-E mixed-energy bound

**[PROVED EXACTLY — conditional on retained scalar/harmonic inputs]**

`0<=R<111/40=2.775.`  (2)

Write `B=2595/256`, `c=1245/256`,
`D(t)=196t-644t^2+896t^3-448t^4`,
`r=D^{-1}(c)`, `s=D^{-1}(41/6)`,
`Xi=N+(35/6)||T||_F^2+14K_4-B in [0,c]`,
`k=r/c`, `h=sqrt(1/100+64Xi/875)`.
The retained inequalities are
`A<=1/2+r+s-kXi`, `sum_isolated a_i<=r`,
`q>=-4/5-h`, `||T||_F^2<=(6/35)(B+Xi)`,
and `V_z>=(5/4)(4/5-A/5-h/2)^2` with positive parenthesis.

Cauchy on four core masses yields `U>=max(A-r,0)^2/4`. Substitution in (1) gives

`R<=F(A,Xi)=3/10+4A-A^2/10-max(A-r,0)^2/8+h/4+3(B+Xi)/140-(5/8)(4/5-A/5-h/2)^2.`

Its A-derivative is `4-A/5-max(A-r,0)/4+g/4>0` where `g=4/5-A/5-h/2>0`. Set `A=1/2+r+s-kXi` and call the result `f(Xi)`. Then

`f'=3/140-k[4-A/5-(A-r)/4+g/4]+h'[1/4+5g/8]`.

Using exact bounds `k<7/1200`, `0<g<1`, `h'=32/(875h)>3/50` gives
`f'>3/140-(17/4)(7/1200)+3/200=391/33600>0`.
Thus the maximum is at `Xi=c`, `A=1/2+s`, `h=8/sqrt(175)`.
Exact brackets `39781/10^6<s<39782/10^6`,
`r<27150/10^6`, `8/sqrt(175)<604745/10^6` yield

`f(c)<3107838072643181/1120000000000000=2.774855422...<111/40`.

## Three perfect matchings and exact signed Walsh constraints

The ten deep F3 edges are `02,04,05,14,17,23,27,36,56,57`.
The only perfect matchings are

- canonical `P0=04|17|23|56`: six inter-edge pairings have deep-contact multiplicities `1,1,1,1,1,1`;
- alternative `P1=02|14|36|57` and `P2=05|14|27|36`: multiplicities `0,1,1,1,1,2`.

**[EXACT GRAPH CONSEQUENCE]** For either alternative matching one core pairing is completely safe, leaving **185 safe pairings and at most five exceptional core pairings**, rather than the uniform 184/6. The unique double-deep core pairing has its two deep contacts in opposite corners of the 2x2 endpoint block.

Orient these contacts as ++ and --, and write `a=m_i.m_j`, `b=m_i.z_j`, `c=z_i.m_j`, `d=z_i.z_j`. Its diagonal contacts are `a+b+c+d<-1/2` and `a-b-c+d<-1/2`; its other two contacts are safe. Hence
`a+d<-1/2`, `-1/2<=a-d<=1/2`.
Therefore `a<0`, `d<0` and
`|z_i.z_j|>1/2+m_i.m_j>=1/2-sqrt(a_i a_j)`.
In particular, the midpoint anti-correlation is orientation-independent.

For **any safe pairing**, all four Walsh endpoint products are in [-1/2,1/2], giving
`|a+d|+|b+c|<=1/2` and `|a-d|+|b-c|<=1/2`, hence
`max(|a|,|d|)+max(|b|,|c|)<=1/2`.
Thus `|z_i.z_j|>1/3` forces both mixed coefficients to have magnitude `<1/6`.

## Conditional 43-safe-pairing consequence

**[PROVED EXACTLY — alternative mass-selected matching only, plus retained Q/defect certificates]** Retain `C_z>28.3626` and `D_raw<441401/10^6`. Five exceptional core squared correlations sum to at most `5/4+D_raw+D_raw^2`. Thus the 185 safe squared correlations satisfy

`sum_safe(z_i.z_j)^2>26476364157199/10^12=26.476364157199`.

If at most 42 safe pairs had `|z_i.z_j|>1/3`, the squared sum would be at most `42/4+143/9=475/18=26.3888...`, contradiction. **At least 43 of 185 safe pairings** therefore have `|z_i.z_j|>1/3` and both cross-midpoint Walsh coefficients `<1/6` in absolute value. For the canonical matching, retain the earlier unconditional-over-matchings **42 of 184** result; do not promote 43 without the alternative hypothesis.

**[OPEN]** Type E exclusion, Type C global/boundary, Type D, generic e>=27, and non-isolated branches. Sparse e=23/24 classification still requires delta(G)>=1. Retain M(F3)<=89, M(P)>=S/2-28/3, and Musin/Boyvalenkov. The finite signed-F3/KKT target is to combine the double-deep sign, safe octahedral inequalities, mixed-energy budget and Q-floor, not to introduce a generic SDP.
