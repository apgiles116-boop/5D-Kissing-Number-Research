# Type E: rounded Gershgorin stability and the exact A>1/68 bootstrap

Date: 2026-10-26. Builds on the consolidated 2026-09-05 ledger and the A>1/80 rounded-degree result.

**[PROVED EXACTLY — UNIVERSAL]** For any 21 unit vectors in R^5, writing s_ij=(u_i.u_j)^2 and P=sum_{i<j}[s_ij(s_ij-1/4)]_+, one has **P>101/6000**.

**[PROVED EXACTLY, CONDITIONAL TYPE E]** Under the previously retained Type-E 204-safe/6-exception normalized defect inequality, **A=sum_i||m_i||^2>1/68**. The upper bound A<=383/504 is unchanged.

## 1. Rounding and frame estimates

Let F=sum_i u_i u_i^T, H=F-(21/5)I, V=tr(H^2), and E=sum_{s_ij<=1/4}s_ij(1/4-s_ij). Degree-four spherical-harmonic positivity yields P-E>=5V/24, hence V<=24P/5.

Round s_ij to b_ij/4, where b_ij=1 iff s_ij>=1/8. Define k_i=sum_{j!=i}b_ij, K=sum_i k_i/2, c_i=k_i/4-16/5, e_i=u_i^T H u_i, d_i=e_i-c_i. For s<=1/4, |s-b/4|<=8s(1/4-s); for s>1/4, |s-1/4|<=4s(s-1/4). Thus the total pairwise rounding error R satisfies R<=8E+4P<=12P-5V/3, giving

sum_i|d_i|<=24P-10V/3, and sum_i d_i=V+336/5-K/2.

Since H is traceless symmetric, |e_i|<=sqrt(4V/5). Each individual |d_i|<=R, so

**|c_i|<=12P+sqrt(4V/5)-5V/3<=12P+3/25**.

For P<7/240 the rounding identities force K=134 or 135. The respective variance bounds are V<=3(24P-1/5)/13 and V<=3(24P-3/10)/7.

## 2. New degree-sensitive Q-Gram bound

Set Q_i=u_i u_i^T-I/5 and B_ij=tr(Q_iQ_j). Then B is PSD, B_ii=4/5, B_ij=s_ij-1/5 for i!=j, e=B*1, V=1^T B 1, and sum_i e_i^2<=lambda_max(B)V.

The rounded row Gershgorin bound is

lambda_max(B)<=max_i[24/5-3k_i/20+sum_{j!=i}|s_ij-b_ij/4|].

If every k_i>=12, this implies

**sum_i e_i^2<=(3+12P-5V/3)V<=(3+12P)V**.

This is sharper than the earlier degree-blind (24/5+4P)V estimate.

## 3. Universal exact contradiction

Assume P<=p=101/6000. Then |c_i|<=12p+3/25=161/500<9/20, forcing all integer k_i in {12,13,14}. Also K=134 or 135, so the rounded Gershgorin bound applies.

For lambda>=0 and eta real define g(c)=min_e(e^2-eta e+lambda|e-c|). It is convex in c, with minimizer e=clip(c,(eta-lambda)/2,(eta+lambda)/2). The rounding inequalities give

sum_i e_i^2>=sum_i g(c_i)-24lambda P+(10lambda/3+eta)V.

For K=134, the degree multiplicities are (n12,n13,n14)=(5+t,16-2t,t); for K=135 they are (3+t,18-2t,t). Convexity minimizes the total g-cost at t=0. With C the minimum, the contradiction margin is

C-24lambda*p-(3+12p-10lambda/3-eta)*Vcap(K,p).

Exact rational choices and margins:

| K | lambda | eta | C | positive margin |
|---|---|---|---|---|
| 134 | 3/10 | 0 | 91/400 | 8569/3250000 |
| 135 | 1 | -93/100 | 8799/20000 | 1233/3500000 |

Both are strictly positive, proving **P>101/6000** for every 21-unit-vector family in R^5. No D5 labeling or generic SDP is used.

## 4. Conditional Type-E energy bootstrap

**Retained, not reproved here:** for the normalized isolated-center-plus-20-edge configuration, the six-core endpoint certificates give

P <= [sum_i k_i*a_i/16 + A_C/4 + 11*A_C^2/16 + 7*A_C^3/16 + A_C^4/16]/(1-A)^4,

where a_0=0, a_i=||m_i||^2 and A_C<=A. If all k_i<=k, then P<=P_k(A)=[(k+4)A+11A^2+7A^3+A^4]/[16(1-A)^4], increasing in A.

Assume A<=a=1/68. First P<=P_20(a)=7597709/322417936. The pointwise degree bound forces all k_i in {12,13,14}, with exact margin 9/20-3/25-12P_20(a)=47579409/1007556050>0. Thus P<=p14=P_14(a)=5711117/322417936.

If any degree 14 occurs, convexity raises the minimum g-cost by g12+g14-2g13. With the same rounded Gershgorin bound, the exact degree-14 exclusion certificates are:

| K | lambda | eta | C with degree 14 | positive margin |
|---|---|---|---|---|
| 134 | 3/10 | 0 | 131/400 | 179521022690742833/2111551923294533200 |
| 135 | 1/5 | -1/10 | 99/400 | 3344950076830347/162427071022656400 |

Hence all k_i<=13. But P<=P_13(a)=5396685/322417936, and

**101/6000-P_13(a)=5753173/60453363000>0**,

contradicting the universal theorem. Therefore **A>1/68**, conditional on the retained six-core estimate.

## Proof ledger

**[RETAINED]** M(F3)<=89; M(P)>=S/2-28/3; twenty-edge mass>=2137/6; A<=383/504; the zero-midpoint 21-line exclusion via the source-audited Musin/Boyvalenkov integrality theorem. The e=23/e=24 sparse graph classification assumes delta(G)>=1.

**[OPEN]** Type E, Type C global/boundary, Type D, generic e>=27 and non-isolated branches. The global proved range is unchanged: **40<=tau_5<=44**. Next priority: strengthen the conditional degree-weighted defect bound and couple individual core energies to frame variance/endpoint mixing.