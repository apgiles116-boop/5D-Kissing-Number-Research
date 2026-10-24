# Type E: lifted triangle and exact rational six-defect budget

**24 October 2026.** **[PROVED EXACTLY]** Universal three-edge inequalities. **[PROVED UNDER RETAINED TYPE-E INPUTS]** Rational six-defect budget and safe-pair floor. **[OPEN]** Type-E elimination.

## Retained hypotheses

For the twenty selected deep edges, the unit endpoints are $x_i^\pm=m_i\pm z_i$. Thus $\|m_i\|^2+\|z_i\|^2=1$, $\|m_i\|^2\le1/4$, and endpoint feasibility gives
$$m_i\cdot m_j+|z_i\cdot z_j|\le1/2.$$
Put $\delta_{ij}=(|z_i\cdot z_j|-1/2)_+$. Only six pairs in the selected four-edge core can have positive defects. Retain the established Type-E bounds
$$D=\sum_{\rm core}\delta_{ij}\le D_0=\frac{1780062775}{4032758016},\quad A=\sum_{i=1}^{20}\|m_i\|^2\le B=\frac{383}{504}.$$
The capped-frame squared-correlation floor is $L=8790283/317520$ for all 190 pairs.

## Theorem 1. Lifted triangle [PROVED EXACTLY]

For any three distinct selected edges $i,j,k$, with $a=\delta_{ij}$ and $b=\delta_{ik}$,
$$\boxed{a+b\le\frac{\sqrt3-1}{2},\qquad a+b+4(a^2+b^2-ab)\le\frac12.}\tag{1}$$

**Proof.** If either defect vanishes, both inequalities follow from the other being at most $1/4$ (notably $x+4x^2\le1/2$ for $0\le x\le1/4$). Otherwise orient $z_j,z_k$ so their products with $z_i$ are positive. In $\mathbb R^5\oplus\mathbb R^5$, form the unit vectors
$$u=(m_i,z_i),\quad v=(-m_j,s_jz_j),\quad w=(-m_k,s_kz_k).$$
Endpoint feasibility gives $u\cdot v\ge p=1/2+2a$, $u\cdot w\ge q=1/2+2b$, and $v\cdot w\le1/2$. Hence for all $\lambda,\mu\ge0$,
$$(\lambda p+\mu q)^2\le\|\lambda v+\mu w\|^2\le\lambda^2+\lambda\mu+\mu^2.$$
Taking $\lambda=\mu=1$ proves the first bound. Taking $\lambda=2p-q$, $\mu=2q-p$ (both nonnegative for $p,q\in[1/2,1]$), and writing $F=p^2+q^2-pq$, gives $4F^2\le3F$, hence $F\le3/4$, equivalent to the second bound. **The positive-defect case distinction is essential:** when $\delta=0$, the lifting need not give $u\cdot v\ge1/2$.

For disjoint core pairs $ij,kl$, AM-GM gives
$$\delta_{ij}+\delta_{kl}\le\frac{\|m_i\|^2+\|m_j\|^2+\|m_k\|^2+\|m_l\|^2}{2}\le B/2.$$
Since $(\sqrt3-1)/2<3/8<B/2$, **every two of the six core defects** satisfy $\delta_e+\delta_f\le b_0:=B/2=383/1008$.

## Theorem 2. Exact rational quadratic certificate [CONDITIONAL TYPE E]

$$\boxed{\sum_{\rm six\ core}\delta_e^2<Q_0:=819/10000=0.0819.}\tag{2}$$

**Proof.** Put $r=D_0-b_0$, $T=122237/500000=0.244474$, and $t=\max_e\delta_e$. Exact rational comparisons (checked in the companion verifier) give
$$0<D_0/3<b_0/2<T<1/4,\quad0<r<1/16,\quad D_0+1/4<B,$$
$$D_0^2/3<Q_0,\quad b_0^2/2+r^2<Q_0,\quad F(T):=T^2+(b_0-T)^2+r^2<Q_0,\quad4D_0>1+B.$$

**Case I:** If $t\le D_0/3$, then $\sum\delta^2\le tD_0\le D_0^2/3<Q_0$.

**Case II:** If $D_0/3\le t\le b_0/2$, the five remaining entries have cap $t$ and total at most $D_0-t\in[t,2t]$. Capped concentration gives
$$\sum\delta^2\le2t^2+(D_0-2t)^2.$$
This is convex in $t$; the endpoint values are $D_0^2/3$ and $b_0^2/2+r^2$, both below $Q_0$.

**Case III:** If $b_0/2\le t\le T$, every remaining entry is at most $h=b_0-t$. Since $h\le D_0-t\le2h$, capped concentration gives
$$\sum\delta^2\le F(t)=t^2+(b_0-t)^2+r^2.$$
Convexity reduces to $t=b_0/2,T$, both below $Q_0$.

**Case IV:** If $T\le t\le1/4$, the unique disjoint partner has defect $y\le h=b_0-t$. The four adjacent defects are each bounded by the nonnegative root $c(t)$ of
$$P(t,c):=t+c+4(t^2+c^2-tc)-1/2=0.$$
The exact rational check $P(T,r)>0$ implies $c(T)<r<1/16$. Implicit differentiation yields
$$c'(t)=-\frac{1+8t-4c}{1+8c-4t}\le-4,$$
since $8t-12c>8T-12/16>1$. Thus
$$\sum\delta^2\le t^2+y^2+c(t)(D_0-t-y)\le\max\{G_0(t),G_1(t)\},$$
where $G_0=t^2+c(t)(D_0-t)<3/40<Q_0$ and $G_1=t^2+(b_0-t)^2+c(t)r$. Finally
$$G_1'(t)=4t-2b_0+rc'(t)\le1+B-4D_0<0,$$
so $G_1(t)\le G_1(T)<F(T)<Q_0$. Continuity covers $t=1/4$. This proves (2).

This improves the previous quadratic ceiling $((\sqrt2-1)/2)D_0\approx0.0914171071$.

## Near-sharp scalar witness [NOT GEOMETRIC FEASIBILITY]

Set $\delta_{12}=244473/1000000$, $\delta_{34}=b_0-244473/1000000$, $\delta_{13}=r$, and the other three defects to zero. The exact checker verifies all individual caps, twelve adjacent polynomial inequalities, three disjoint budgets, and $\sum\delta=D_0$. This gives $\sum\delta^2\approx0.0818987987078$, within $1.202\times10^{-6}$ of the upper bound. This is **only a witness for the scalar relaxation**, not a realizable five-dimensional configuration.

## Safe-pair consequence [CONDITIONAL TYPE E]

For each candidate pair, $(z_i\cdot z_j)^2\le1/4+\delta_{ij}+\delta_{ij}^2$. Subtracting their six contributions from the capped-frame floor gives
$$\boxed{\sum_{\rm 184\ safe}(z_i\cdot z_j)^2>
L-\frac32-D_0-Q_0
=\frac{64677589778681}{2520473760000}
\approx25.6608859830705.}\tag{3}$$
Previous floor: approximately 25.6513688759251. This is a **necessary condition, not a Type-E contradiction**.

**[OPEN]:** A matching upper bound on safe squared correlations; geometric four-core rank-five feasibility; global $D_5$ labeling; Type E, C, D, generic $e\ge27$, and non-isolated branches. **[UNCHANGED]:** $40\le\tau_5\le44$, $M(F_3)\le89$, $M(P)\ge S/2-28/3$, $A\le383/504$. The sparse $e=23,24$ classification remains conditional on $\delta(G)\ge1$.

Exact checker: research/tau5_typeE_lifted_triangle_defect_budget_2026-10-24_verify.py.
