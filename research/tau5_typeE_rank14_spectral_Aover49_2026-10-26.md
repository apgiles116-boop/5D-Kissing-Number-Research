# Rank-14 traceless-Q spectrum and Type-E midpoint floor A > 1/49

2026-10-26. Builds on the consolidated 2026-09-05 ledger and the exact pair-normalization note.

**[PROVED EXACTLY — UNIVERSAL]** For 21 unit vectors in R^5, put s_ij=(u_i·u_j)^2 and P=sum_{i<j}[s_ij(s_ij-1/4)]_+. Then **P>23/1000**.

**[PROVED EXACTLY — CONDITIONAL TYPE E]** For the retained 204-safe/six-core-exception Type-E endpoint configuration, the total midpoint energy satisfies **1/49<A<=383/504**. The upper bound is retained, not reproved.

**[OPEN]** Type E remains unresolved; global proved range remains 40<=tau_5<=44.

## 1. Rank-14 spectral identity

Let F=sum_i u_i u_i^T, H=F-(21/5)I, V=tr(H^2), and E=sum_{s_ij<=1/4}s_ij(1/4-s_ij). Degree-four harmonic positivity gives P-E>=5V/24. Also sum_{i<j}s_ij=168/5+V/2.

Set Q_i=u_i u_i^T-I/5 and B_ij=tr(Q_i Q_j). Then B is PSD, rank(B)<=dim Sym_0(5)=14, B_ii=4/5, B_ij=s_ij-1/5 for i!=j, and tr(B)=84/5. Direct expansion yields the exact identity

tr(B^2)=504/25+2(P-E)-3V/20.

Pad its eigenvalues with zeros to length 14. Their mean is 6/5, so their squared variance is 2(P-E)-3V/20. Since a zero-sum vector of length 14 has maximum coordinate at most sqrt(13/14) times its Euclidean norm,

lambda_max(B)<=6/5+sqrt((13/14)(2P-3V/20)).

Writing e=B1, V=1^TB1, we obtain sum e_i^2<=lambda_max(B)V. For any rational r>0 and P<=p, the tangent sqrt(t)<=r/2+t/(2r) gives

sum e_i^2 <= (L-cV)V,
L=6/5+r/2+13p/(14r), c=39/(560r).          (1)

This rank-sensitive inequality requires no D5 labeling.

## 2. Universal defect gap

Round s_ij to b_ij/4, b_ij=1 for s_ij>=1/8, otherwise zero. Write K=sum b_ij, k_i=sum_{j!=i}b_ij, c_i=k_i/4-16/5, e_i=u_i^THu_i. The established harmonic/rounding inequalities are

sum_i|e_i-c_i|<=24P-(10/3)V,
sum_i(e_i-c_i)=V+336/5-K/2,
|c_i|<=12P+3/25.

If P<=p=23/1000, these force K=134 or 135 and k_i in {12,13,14}.

For lambda>=0, eta rational, let g(c)=min_t(t^2-eta*t+lambda|t-c|). Convexity and the rounded-error bound give

sum_i e_i^2>=C_K-24lambda*p+(10lambda/3+eta)V,

where C_K is the minimum of sum_i g(c_i) over the allowed integer degree sequences. Its minimizers have degree multiplicities (5,16,0) for K=134 and (3,18,0) for K=135. Combining with (1) requires

0>=C_K-24lambda*p-(L-10lambda/3-eta)V+cV^2.  (2)

The rounded row-sum bound also gives 0<=V<=v_K, where v_134=(3/13)(24p-1/5) and v_135=(3/7)(24p-3/10). The following exact rational choices make the right side of (2) decreasing on [0,v_K], yet strictly positive at v_K:

| K | lambda | eta | r | C_K | v_K | positive margin |
|---|---|---|---|---|---|---|
| 134 | 3/10 | 0 | 1/5 | 91/400 | 132/1625 | 101251/3250000 |
| 135 | 19/50 | -3/10 | 1/6 | 633/2500 | 27/250 | 4803/17500000 |

Hence P>23/1000 exactly.

## 3. Conditional Type-E bootstrap

For the 20 selected deep edges, let a_i=||m_i||^2, A=sum a_i, C=sum of the four selected F3 core a_i, and normalize u_i=z_i/sqrt(1-a_i); include u_0=x_0, a_0=0. The exact six-exception pair-normalization certificate from the preceding note is

P <= [sum_i k_i a_i+4C+9C^2+5C^3+C^4]/[16(1-A)^2].

If all k_i<=k, this implies P<=U_k(A), where

U_k(A)=[(k+4)A+9A^2+5A^3+A^4]/[16(1-A)^2].

Assume A<=1/49. First P<=U_20(1/49)=316159/9834496. The pointwise degree inequality forces k_i<=14. Thus P<=p14=U_14(1/49)=713179/29503488<7/240, forcing K=134 or 135; it also forces k_i in {12,13,14}.

To exclude degree 14, use the rank-14 bound lambda_max(B)<=3/2, since 13p14/7<9/100. The shifted-Huber minimum with at least one degree 14 occurs at (n12,n13,n14)=(6,14,1) for K=134 and (4,16,1) for K=135. The following choices give exact contradictions:

| K | lambda | eta | minimum Huber cost | positive margin |
|---|---|---|---|---|
| 134 | 2/5 | 1/10 | 147/400 | 51776099/399526400 |
| 135 | 1/2 | -3/10 | 17/50 | 2918819/86051840 |

Thus every k_i<=13, giving P<=U_13(1/49)=3949/172872. But

23/1000-3949/172872=1691/10804500>0,

contradicting the universal theorem. Therefore **A>1/49**.

## Status and next step

Retain the Type-E exact star bound <=70/3, M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, and A<=383/504. The 21-line zero-midpoint exclusion remains source-audited via Musin/Boyvalenkov. The sparse e=23/e=24 graph classification assumes delta(G)>=1. Type C, D, generic e>=27, and non-isolated branches remain open.

Next: couple the rank-14 Q-spectrum to individual six-core exceptional defects, endpoint mixing, and weighted degree-energy sum_i k_i a_i; the scalar A>1/49 bound is not a Type-E exclusion.
