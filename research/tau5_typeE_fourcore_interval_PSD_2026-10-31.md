# Type E: exact four-core interval/PSD certificate Q6 < 1979/1000

Date: 2026-10-31. **Global proved range 40 <= tau_5 <= 44. Type E OPEN.**

## Status and results

**[PROVED EXACTLY — finite-dimensional lemma under explicit hypotheses]**
For four deep-edge pairs (m_i,z_i), assume a_i=||m_i||^2<=1/4, every cross-endpoint inner product <=1/2, A_C=sum a_i<=T=383/504, and delta=sum_(i<j)(|z_i.z_j|-1/2)_+<=D=1780062775/4032758016. Then

    Q6=sum_(i<j)(z_i.z_j)^2 < 1979/1000 = 1.979.

An exhaustive rational 1000-grid interval certificate covers 30,534 boxes. The largest certified box bound is exactly

    502855011649330350191833 / 254111518993941504000000
       = 1.978875312855... < 1979/1000.

A separate coarser 500-grid verifies <99/50 on 7,665 boxes. The proof is algebra plus exact interval enumeration, not a numerical optimization.

**[PROVED CONDITIONALLY — Type E]** With the retained exact midpoint and defect caps, this improves the previous Q6<1989/1000 by 1/100. The upstream Type-E caps are not re-audited in this note. No D5 alignment or full Q-rank is assumed.

**[REUSED PROVED EXACTLY — global frame/capped-simplex, already established 2026-10-28]** For 20 projected vectors in R^5 with ||z_i||^2=1-a_i, 0<=a_i<=1/4 and A=sum a_i<=T,

    Q_all=sum_(i<j)(z_i.z_j)^2 >= 8790283/317520
       = 27.684186822877...

This is the previously established 2026-10-28 capped-simplex floor, reused here to combine consistently with the new Q6 bound. It improves the original loose 17456771/635040 by 131/672, but is **not** a new theorem of this run. Stronger conditional center-sensitive Q floors are retained separately and are not superseded by this baseline.

**[PROVED CONDITIONALLY — Type E]**

    Q_safe=Q_all-Q6 > 204047773/7938000
       = 25.705186822877...

With the separately retained, not re-audited center-derived Q_all>5876056025347/211680000000, the conditional floor becomes Q_safe>5457141305347/211680000000 =25.780146000316...

**[OPEN]** No contradiction is established. Type E, C, D, generic e>=27 and non-isolated branches remain open; sparse e=23,24 classification retains delta(G)>=1.

## Exact proof reduction

Write c_ij=m_i.m_j, d_ij=|z_i.z_j|, eps_ij=(d_ij-1/2)_+, Eeps=sum eps_ij^2. Four endpoint upper inequalities imply c_ij+d_ij<=1/2 and |c_ij|<=1/4. Checking c>=0 and c<0 separately gives

    d^2 <= 1/4 + eps/4 + eps^2 - 3c/4,
    d^2 <= 1/4 + eps + eps^2 - 1_(c>0)c(1-c).

Summing over the six pairs, using 2 sum c_ij=||sum m_i||^2-A_C, gives the simultaneous bounds

    Q6 <= 3/2 + delta/4 + Eeps + 3T/8,                    (A)
    Q6 <= 3/2 + delta + Eeps - sum_(c_ij>0)c_ij(1-c_ij). (B)

Order the six defects p>=q>=r_1>=...>=r_4. Since r_k<=q and sum r_k=delta-p-q,

    Eeps <= p^2+q^2+min((D-p-q)^2,q(D-p-q)).             (C)

If the top two defect edges are disjoint, Cauchy and AM-GM give p+q<=A_C/2<=T/2. Thus when p+q>T/2 they share a core vertex. Relabel them (1,2),(1,3), with c_12=-u<=-p and c_13=-v<=-q. Three-by-three midpoint Gram PSD yields

    c_23 >= 4[pq-sqrt((1/16-p^2)(1/16-q^2))] = g(p,q)>0.

The expression g is increasing in p,q. For X=1/16-p^2, Y=1/16-q^2, use

    sqrt(XY) <= (X+Y)/2 - (X-Y)^2/[4(X+Y)]

to obtain the rational lower bound

    g(p,q)>=g0(p,q)
     =2(p+q)^2-1/4+(p^2-q^2)^2/(1/8-p^2-q^2).          (D)

The positivity follows from p+q>T/2 and T^2>1/2. Since 0<c_23<=1/4, c_23(1-c_23)>=g0(1-g0) whenever 0<=g0<=1/4.

## Rational finite certificate

Partition p,q into intervals of length h=1/1000, indexed by 0<=iq<=ip<=249. Skip boxes whose lower endpoints pl+ql>D. For each remaining box set pu=pl+h, qu=ql+h, R=D-pl-ql and

    Eupper=pu^2+qu^2+min(R^2,qu*R),
    B1=3/2+D/4+3T/8+Eupper.

If pl+ql>T/2, set g_lower=max(0,g0(pl,ql)); if g_lower<=1/4 also set

    B2=3/2+D+Eupper-g_lower(1-g_lower).

The box upper bound is B1 or min(B1,B2), respectively. This covers all feasible p>=q including p=1/4, and every inequality uses outward interval bounds. The companion Python Fraction checker asserts every one of 30,534 box bounds <1979/1000 and reports the maximum at (ip,iq)=(249,130). The 500-grid independently asserts <99/50.

## Global floor and safe counts

The exact frame identity is

    Q_all=30-3A+A^2/10-U/2+V_z/2,  V_z>=0.

For k/4<=A<=(k+1)/4, capped-simplex convexity gives U<=k/16+(A-k/4)^2. The lower expression has derivative -3-4A/5+k/4<0 for 0<=A<=T, so its minimum is at T. Here Umax(T)=3/16+(T-3/4)^2=47653/254016, giving Q_all>=8790283/317520.

Assuming the retained classification that the other 184 pairings satisfy |z_i.z_j|<=1/2, the new baseline floor requires at least 103 nonzero safe correlations, 88 >1/5, 76 >1/4 and 38 >1/3. With the separate center variance certificate the last two counts become 77 and 39.

Next: obtain an upper bound on the same 184 safe correlations from Walsh blocks and four rank-free Q residuals with one common labeling. Preserve M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504 and the Musin/Boyvalenkov zero-midpoint exclusion. **No improvement to 40<=tau_5<=44 is claimed.**
