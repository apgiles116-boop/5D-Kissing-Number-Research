# Type E: exact rounded-degree bootstrap to A>1/80 (2026-10-26)

Continuation of consolidated 2026-09-05 tau_5 ledger and shifted-Huber A>1/89 note. Full local derivation and independent Fraction verifier accompany this result.

**[PROVED EXACTLY, UNIVERSAL]** For any 21 unit vectors in R^5, let s_ij=(u_i.u_j)^2 and P=sum_{i<j}[s_ij(s_ij-1/4)]_+. Then **P>2/141**. Furthermore, if P<=1/64, every rounded contact degree k_i (threshold s_ij>=1/8) is at most 13.

**[PROVED EXACTLY, CONDITIONAL TYPE E]** Under the retained 204-safe/6-core endpoint partition and six-core defect certificates, **A=sum_i||m_i||^2>1/80**. The retained upper bound A<=383/504 is unchanged.

## Exact universal proof

Set H=sum_i u_i u_i^T-(21/5)I, V=tr(H^2), e_i=u_i^T H u_i, c_i=k_i/4-16/5, d_i=e_i-c_i, L=sum_i|d_i|, K=sum k_i/2. Degree-four harmonic positivity, rounding and traceless-Q Gram analysis yield

- V<=24P/5;
- L<=24P-(10/3)V;
- sum_i d_i=V+336/5-K/2;
- sum_i e_i^2<=(24/5+4P)V.

Define g(c)=min_e (e^2-eta e+lambda|e-c|), convex in c. If sum_i g(c_i)>=C, then
C-24lambda P <= (24/5+4P-10lambda/3-eta)V. (H)

Assuming P<=p=2/141 forces K=134 or 135. For K=134, V<=(24p-1/5)*3/13; lambda=3/10, eta=0, integer-degree convexity gives C=91/400, yielding exact contradiction margin **899/2297360>0** in (H). For K=135, V<=(24p-3/10)*3/7; lambda=1/5, eta=-1/10, C=3/16, giving **278881/6185200>0**. Thus P>2/141.

For P<=p=1/64, again K=134 or 135. If any k_i>=14, convexity raises the minimum C to 131/400 (K=134, degree multiset 14, six 12s, fourteen 13s) or 99/400 (K=135, degree multiset 14, four 12s, sixteen 13s). Formula (H) gives contradiction margins **491/8320** and **771/22400** respectively. Hence P<=1/64 implies all k_i<=13.

## Exact Type-E bootstrap

The retained six-core endpoint estimate, with a_0=0 and a_i=||m_i||^2, gives

P <= [sum_i k_i a_i/16 + A_C/4 + 11 A_C^2/16 + 7 A_C^3/16 + A_C^4/16]/(1-A)^4,

where A_C<=A. If k_i<=k, define
P_k(A)=((k+4)A+11A^2+7A^3+A^4)/(16(1-A)^4).

Assume A<=1/80. Initially k_i<=20, so P<=P_20(1/80)=12358961/623201296. Since |e_i|<=sqrt(4V/5) and |d_i|<=L, optimizing in V gives |c_i|<=24P+3/50. If k_i>=15, c_i>=11/20, contradicting the exact margin
11/20-24P_20(1/80)-3/50=54709819/3895008100>0.
Therefore k_i<=14. Next,
1/64-P_14(1/80)=1802237/2492805184>0,
so the universal degree lemma forces k_i<=13. Finally,
2/141-P_13(1/80)=9133091/87871382736>0,
contradicting P>2/141. Thus A>1/80.

**[OPEN]** Type E, C7 global/boundary, Type D, generic e>=27 and non-isolated branches. Retain M(F3)<=89, M(P)>=S/2-28/3, total twenty-edge mass>=2137/6, and sparse e=23/24 classification only conditional on delta(G)>=1. No D5 labeling or uniqueness used. **Global proved interval remains 40<=tau_5<=44.**
