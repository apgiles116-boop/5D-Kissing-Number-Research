# Type E: isolated-center harmonic gap forces macroscopic Q-frame anisotropy (2026-10-30)

**[PROVED EXACTLY — conditional on Type E graph and retained M(F3)≤89]** The isolated-center harmonic second-moment row satisfies **q<−983/5000**.

**[PROVED EXACTLY — using retained A≤383/504]** The global projected Q-frame variance satisfies
[
V_z>rac{47602076041}{317520000000}>0.1499.
]
The full twenty-edge frame variance satisfies
[
V_{edge}>rac{24830289}{80000000}>0.3103.
]

**[PROVED CONDITIONALLY — using the stronger 2026-10-28 harmonic A<567/1000 cap]**
[
oxed{V_z>rac{14814801}{80000000}=0.1851850125.}
]
Thus the weighted Petersen residual (E_Q=V_z+12C_z) exceeds the same value, independently of D5 labeling. This is a *lower* bound, not a Type-E exclusion.

## Exact proof of the rational q cap

Let (v) be the isolated center and (x_i^pm=m_ipm z_i) the twenty selected deep-edge endpoint pairs. Set
[
T=sum_{xin X}xx^	op-rac{41}{5}I,quad
s=sum_{x
e v}(vcdot x)^2,quad q=v^	op Tv=s-rac{36}{5},
]
and (N_0=sum_{x
e v}7(vcdot x)^2(1-4(vcdot x)^2)ge0).
The degree-four Delsarte identity and Type-E mass ceiling give
[
M_{deep}=410+N+E_h=336-D_I+M(F_3)le425-D_I,
]
where (E_h=(35/6)|T|_F^2+14K_4), (D_Ige0), (Nge N_0). Hence
[
E_h+N_0le15.
]
The exact isolated-center harmonic row estimate (2026-10-28) gives, whenever (qge-12/7),
[
E_hge f(q)=10+rac{35}{64}(5q+4)^2.
]
If (qge-39/200), then (f(q)ge307287/20480>15).
If (-983/5000le qle-39/200), then (s=7+r) with (17/5000le rle1/200). The exact capped-simplex concentration inequality gives
[
N_0ge7r(1-4r)gerac{5831}{250000}.
]
Because (f) is increasing there,
[
E_h+N_0ge f(-983/5000)+rac{5831}{250000}
=15+rac{72851}{64000000}>15,
]
again impossible. The remaining case (q<-12/7) already satisfies the claimed bound. Therefore (q<-983/5000).

## Exact transfer to frame variance

Let (S=sum_i(m_im_i^	op+z_iz_i^	op)), (M=sum_i m_im_i^	opsucceq0), (Z=S-M), and (A=operatorname{tr}M). Opposite-sign endpoint pairing gives
[
v^	op S v=s/2=18/5+q/2.
]
Define (B_{edge}=S-4I), (B_z=Z-(20-A)I/5=sum_iQ_i). Both are trace-free, with
[
v^	op B_{edge}v=q/2-2/5,quad
v^	op B_zv=q/2-2/5+A/5-v^	op Mv.
]
For every trace-free symmetric (5	imes5) matrix (B),
[
|B|_F^2gerac54(v^	op Bv)^2
]
by Cauchy against (vv^	op-I/5). Inserting (q<-983/5000) gives
[
V_{edge}=|B_{edge}|_F^2>rac54(4983/10000)^2
=rac{24830289}{80000000}.
]
With (Ale383/504),
[
V_z=|B_z|_F^2>rac54(218179/630000)^2
=rac{47602076041}{317520000000}.
]
With the stronger retained (A<567/1000),
[
V_z>rac54(3849/10000)^2
=rac{14814801}{80000000}.
]

## Walsh and squared-correlation consequences

The previously verified six-deep/474-safe Walsh identity has the term (V_{edge}/2) on its nonnegative right-hand side. We now have the **strict new offset** (V_{edge}/2>24830289/160000000=0.15518930625).

The exact projected correlation identity
[
sum_{i<j}(z_icdot z_j)^2
=30-3A+A^2/10-U/2+V_z/2
]
and the retained 2026-10-28 joint scalar minimum (28.2677055569326959ldots) yield
[
sum_{i<j}(z_icdot z_j)^2>28.36029806318ldots.
]
A simpler rational bound, using (A<567/1000) and (U<129/1000), is
[
sum_{i<j}(z_icdot z_j)^2>rac{36299829}{1280000}=28.35924140625.
]
These are necessary conditions, not a D5 proximity theorem.

**[OPEN]** Type E remains open. This changes the Q-kernel strategy: an upper bound on (V_z) below (0.1851850125) from the 184 safe Walsh blocks and six exceptional core pairings would now exclude Type E; merely proving a tiny positive lower bound on (E_Q) is no longer the best target. No identification between six exceptional pairings and six Q-kernel modes is assumed.

**[RETAINED]** M(F3)≤89, matching (M(P)ge S/2-28/3), historical (Ale383/504), the stronger conditional harmonic cap, Musin/Boyvalenkov zero-midpoint exclusion, and sparse graph classification conditional on (delta(G)ge1). Types C,D, generic e≥27 and non-isolated branches remain open. **Global proved range: 40≤τ5≤44.**
