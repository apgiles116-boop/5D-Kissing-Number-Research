# 21-line row-integrality variance improvement (2026-10-23)

**[PROVED EXACTLY, universal]** For 21 unit vectors y_0,...,y_20 in R^5, set v_ij=(y_i.y_j)^2 and P=sum_{i<j}[7v_ij(4v_ij-1)]_+. Then **P>459/1000**. This strengthens the previous P>9/20.

**[CONDITIONAL ON RETAINED TYPE-E REDUCTIONS]** For the mass-selected Type-E matching, **A=sum ||m_i||^2 > 5313/500000=0.010626**. **[OPEN]** Type-E exclusion; the global proved range remains 40<=tau_5<=44.

## Exact universal proof

Write N=sum[-7v_ij(4v_ij-1)]_+, S=sum y_i y_i^T, B=S-(21/5)I and V=tr(B^2). Gegenbauer positivity gives

    P-N >= (35/6)V,  sum_{i<j}v_ij=168/5+V/2.      (1)

Round v<=1/4 to its nearest endpoint in {0,1/4}, and v>1/4 to 1/4. Write b_ij for the rounded value, e_ij=v_ij-b_ij, E=4sum b_ij integer, D_-=sum_{v<=1/4}min(v,1/4-v), D_+=sum_{v>1/4}(v-1/4). Then

    N>=(7/2)D_-,  N>=g(D_-)=7D_--28D_-^2,
    D_+<=P/7,  sum|e_ij|<=2N/7+P/7<=3P/7-(5/3)V. (2)

Assume P<=p=459/1000. Equation (1) and (2) force E in {134,135}. For E=135, sum e=-3/20+V/2 and D_->=3/20-V/2, so P>=21/40+(49/12)V>p. Hence E=134.

Let k_i be degrees of the rounded graph, so sum k_i=268. Let L={i:k_i<=12}, l=|L| in {1,...,20}, H its complement and b=sum_L(16/5-k_i/4). Degree counting yields b>=max(l/5,(25-l)/20)>=1. Define

    r_i=y_i^T B y_i=k_i/4-16/5+sum_{j!=i}e_ij,
    sum_i r_i=V.

Set E_+=sum[e_ij]_+, q=2E_+<=6p/7-(10/3)V<1, t=b-q>=1-q. Then sum_L r_i<=-t, sum_H r_i>=t+V. Cauchy-Schwarz gives

    sum_i r_i^2 >= t^2/l+(t+V)^2/(21-l)
       >= (21/80)(1-q)^2+(1-q)V/10+V^2/20.         (3)

For l<=5 use b>=1 and 1/l+1/(21-l)>=21/80; for l>=5 use b>=l/5, t>=(l/5)(1-q) and 21l/[25(21-l)]>=21/80. In either case 1/(21-l)>=1/20 supplies the retained high-row terms.

By Jensen and the traceless spectral bound lambda_max(B)<=sqrt(4V/5),

    sum_i r_i^2<=tr(B^2 S)<=(21/5+sqrt(4V/5))V. (4)

Set v0=1541/50000. If V>=31/1000 then V>v0. Otherwise lambda_max(S)<1743/400, since (63/400)^2-(4/5)(31/1000)=1/160000. Equations (3)-(4) imply h(V)<0, where

    h(v)=(21/80)(1-6p/7+10v/3)^2
         +(1-6p/7+10v/3)v/10+v^2/20-(1743/400)v.

But h is decreasing on [0,v0] and h(v0)=463361/175000000000>0. Therefore V>v0.

As E=134, sum e=1/10+V/2, whence D_->=1/10+V/2-p/7. Also D_-<=(2/7)(p-(35/6)V)<1/8, so g is increasing on the relevant interval. The function g(1/10+v/2-p/7)+(35/6)v is increasing for v in [v0,6p/35]. Thus

    P>=N+(35/6)V
      >g(1/10+v0/2-p/7)+(35/6)v0
      =p+5491693/52500000000>p,

contradiction. No D5 labeling or numerical SDP is used.

## Type-E corollary

Import the previously proved degree-counted six-exception estimate, for the **one mass-selected matching**:

    P<=fstar(A)=7A[17+(1+A)^2(7+A)]/[4(1-A)^2].

This is increasing on 0<=A<1 and the exact rational comparison is

    459/1000-fstar(5313/500000)
      =5575655015507445273/244715227969000000000000>0.

Therefore A>5313/500000. This remains much smaller than A<=383/504 (and subsequent retained ceilings); Type E is **not excluded**. Preserve M(F3)<=89, matching M(P)>=S/2-28/3, and total selected mass >=2137/6. Types C,D, generic e>=27, non-isolated branches remain open; sparse e=23/24 classification is conditional on delta(G)>=1.

Next priority: retain the individual row discrepancies r_i together with the six core midpoint Gram variables in a small exact polynomial/KKT model, rather than collapsing to a scalar P bound.
