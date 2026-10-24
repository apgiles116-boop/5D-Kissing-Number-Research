# Type E: lifted triangle and rational six-defect budget (2026-10-24)

**Status:** [PROVED EXACTLY] universal three-edge inequalities. [PROVED UNDER RETAINED TYPE-E INPUTS] rational quadratic budget and safe-pair floor. [OPEN] Type-E exclusion and the global five-dimensional kissing number.

## Hypotheses and retained data

For twenty selected deep edges, write unit endpoints as (x_i^±=m_i±z_i). Then (|m_i|^2+|z_i|^2=1), (|m_i|^2le 1/4), and the four endpoint constraints imply (m_icdot m_j+|z_icdot z_j|le 1/2). Define (delta_{ij}=(|z_icdot z_j|-1/2)_+). In the retained Type-E reduction, only six pairings among four selected core edges can have positive defects. Retain (D=sum_{mathrm{core}}delta_{ij}le D_0=1780062775/4032758016), (A=sum_{i=1}^{20}|m_i|^2le B=383/504), and the capped-frame floor (L=8790283/317520) for the sum of all 190 squared projected correlations.

## Theorem 1: lifted three-edge geometry [PROVED EXACTLY]

For any three distinct selected edges (i,j,k), put (a=delta_{ij}), (b=delta_{ik}). Then
[
a+ble(sqrt3-1)/2,qquad
a+b+4(a^2+b^2-ab)le 1/2. 	ag{1}
]
If either defect is zero, both follow from (0ledeltale1/4). Otherwise orient (z_j,z_k) so their inner products with (z_i) are positive and form unit vectors in (mathbb R^5oplusmathbb R^5):
[
u=(m_i,z_i),quad v=(-m_j,s_jz_j),quad w=(-m_k,s_kz_k).
]
The endpoint inequalities imply (ucdot vge p=1/2+2a), (ucdot wge q=1/2+2b), (vcdot wle1/2). Thus, for every (lambda,muge0),
[
(lambda p+mu q)^2le|lambda v+mu w|^2lelambda^2+lambdamu+mu^2.
]
Taking (lambda=mu=1) gives the first inequality. Taking (lambda=2p-q), (mu=2q-p), both nonnegative since (p,qin[1/2,1]), and setting (F=p^2+q^2-pq), gives (4F^2le3F), hence (Fle3/4), equivalent to the second inequality.

For disjoint core pairings (ij,kl), (delta_{ij}+delta_{kl}le(|m_i|^2+|m_j|^2+|m_k|^2+|m_l|^2)/2le B/2). Since ((sqrt3-1)/2<3/8<B/2), **every two** of the six core defects obey (delta_e+delta_fle b_0:=B/2=383/1008).

## Theorem 2: rational six-defect quadratic certificate [PROVED UNDER TYPE-E INPUTS]

[
oxed{sum_{mathrm{six core}}delta_e^2< Q_0:=819/10000=0.0819.} 	ag{2}
]

Set (r=D_0-b_0), (T=122237/500000=0.244474), and (t=max_edelta_e). Exact rational checks establish (0<D_0/3<b_0/2<T<1/4), (0<r<1/16), (D_0+1/4<B), (D_0^2/3<Q_0), (b_0^2/2+r^2<Q_0), (F(T):=T^2+(b_0-T)^2+r^2<Q_0), and (4D_0>1+B).

* If (tle D_0/3), then (sumdelta^2le tD_0le D_0^2/3<Q_0).
* If (D_0/3le tle b_0/2), capped-simplex concentration of the remaining five entries gives (sumdelta^2le2t^2+(D_0-2t)^2). Convexity reduces the maximum to (D_0/3,b_0/2), where the preceding rational comparisons apply.
* If (b_0/2le tle T), every remaining entry is at most (h=b_0-t). Since (hle D_0-tle2h), capped concentration gives (sumdelta^2le F(t)=t^2+(b_0-t)^2+r^2). Convexity reduces to (b_0/2,T), both below (Q_0).
* If (Tle tle1/4), the unique disjoint partner has defect (yle h=b_0-t); the four adjacent defects are each bounded by the nonnegative root (c(t)) of (P(t,c)=t+c+4(t^2+c^2-tc)-1/2=0). Exact evaluation gives (P(T,r)>0), so (c(T)<r<1/16). Implicit differentiation yields (c'=-(1+8t-4c)/(1+8c-4t)le-4) on ([T,1/4)), because (8t-12c>8T-12/16>1). Therefore
[
sumdelta^2le t^2+y^2+c(t)(D_0-t-y)
lemax{G_0(t),G_1(t)},
]
where (G_0=t^2+c(t)(D_0-t)<3/40<Q_0) and (G_1=t^2+(b_0-t)^2+c(t)r). Since (G_1'le1+B-4D_0<0), (G_1(t)le G_1(T)<F(T)<Q_0). The endpoint (t=1/4) follows by continuity.

This proves (2) without a D5 labeling or a new SDP. It improves the previous bound (((sqrt2-1)/2)D_0approx0.0914171071).

## Exact scalar-relaxation witness [NOT GEOMETRIC FEASIBILITY]

Set (delta_{12}=244473/1000000), (delta_{34}=b_0-244473/1000000), (delta_{13}=r), and all other core defects zero. Direct rational checks verify the individual caps, all 12 adjacent polynomial constraints (1), all 3 disjoint budgets, and (sumdelta=D_0). This scalar witness gives (sumdelta^2approx0.0818987987078), within (1.202	imes10^{-6}) of (2). No feasible five-dimensional midpoint/projected realization is claimed.

## Safe-pair consequence [CONDITIONAL TYPE E]

On each of the six candidate pairs, ((z_icdot z_j)^2le1/4+delta_{ij}+delta_{ij}^2). Therefore the 184 projectively safe pairings obey
[
oxed{sum_{mathrm{184 safe}}(z_icdot z_j)^2>
L-3/2-D_0-Q_0
=rac{64677589778681}{2520473760000}
approx25.6608859830705.} 	ag{3}
]
The previous floor was approximately 25.6513688759251. This is a necessary condition, **not** a Type-E contradiction.

**Open:** opposing safe-pair upper bound; actual rank-five four-core Gram feasibility; global D5 labeling; Type E, C, D, generic (ege27), and non-isolated branches. **Unchanged:** (40le	au_5le44); (M(F_3)le89), (M(P)ge S/2-28/3), (Ale383/504). The (e=23,24) graph classification remains conditional on (delta(G)ge1).

Companion exact verifier: `research/tau5_typeE_lifted_triangle_defect_budget_2026-10-24_verify.py`.
