# Type E: defect quantization yields a strict sub-two six-core Q budget

Date: 2026-10-31. **Global proved range remains 40 <= tau_5 <= 44. Type E remains OPEN.**

## Proof-status ledger

**[PROVED EXACTLY — universal endpoint algebra]** For two selected deep edges with midpoint inner product c=m_i.m_j, projected correlation d=|z_i.z_j|, and epsilon=(d-1/2)_+, upper endpoint contacts imply c+d<=1/2 and |c|<=1/4. The previous affine majorant

    d^2 <= 1/4 + epsilon/2 - 3c/4

has an explicit nonnegative remainder. If c>=0, the remainder is at least c(1/4-c). If c<0, it is at least (3/4)(-c-epsilon)+epsilon(1/4-epsilon). These are exact inequalities without lower endpoint-contact assumptions.

**[PROVED EXACTLY — four-core second-order theorem]** Let A_C=sum_j ||m_j||^2, s_C=||sum_j m_j||^2, delta=sum_(j<k)epsilon_jk, E2=sum_(j<k)epsilon_jk^2, and Q6=sum_(j<k)(z_j.z_k)^2 for the four core edges. Then

    Q6 <= 3/2 + delta/4 + E2 + 3(A_C-s_C)/8.              (1)

Proof: Sum the preceding affine majorants, subtract the nonnegative remainder sum_(j<k)epsilon_jk(1/4-epsilon_jk)=delta/4-E2, and use 2sum_(j<k)m_j.m_k=s_C-A_C. Every epsilon_jk is in [0,1/4]. No D5 labeling or Q-rank hypothesis is required.

**[PROVED EXACTLY — capped-simplex defect quantization]** For six numbers 0<=epsilon_jk<=1/4 with sum delta, convexity gives

    E2 <= k/16 + (delta-k/4)^2,   k=floor(4delta).        (2)

Proof: Moving mass from a smaller interior coordinate to a larger one increases their squared sum; at an extremizer all but at most one coordinate are 0 or 1/4. In particular, for 1/4<=delta<=1/2, E2<=1/16+(delta-1/4)^2. The function delta/4+E2_max(delta) is increasing on [0,1/2].

**[PROVED CONDITIONALLY — retained Type-E exact caps]** Retain the established raw defect cap D=1780062775/4032758016 and midpoint cap A_C<=A<=383/504. Since 1/4<D<1/2 and s_C>=0, (1)-(2) yield

    Q6 <= 3/2 + D/4 + 1/16 + (D-1/4)^2 + 3(383/504)/8
       = 32436090936603055633/16263137215612256256
       = 1.994454729525... < 2.                             (3)

The preceding affine-centroid cap was 16176768847/8065516032=2.005670657998... . The exact improvement is 182406183756108143/16263137215612256256=0.011215928472... .

A short rational certificate for the strict sub-two threshold is

    D<9/20,  383/504<19/25,
    3/2+(9/20)/4+1/16+(9/20-1/4)^2+3(19/25)/8 = 2.

Thus **Q6<2** is a new exact conditional Type-E conclusion, not a Type-E exclusion.

**[PROVED CONDITIONALLY — safe-correlation consequence]** The global frame identity is

    Q=30-3A+A^2/10-(1/2)sum_i a_i^2+V_z/2,

where V_z=||sum_i Q_i||_F^2>=0. Partitioning Q=Q_safe+Q6, (1) gives the exact bridge

    Q_safe >= 57/2-3A+A^2/10-(1/2)sum_i a_i^2
              +V_z/2-delta/4-E2-3A_C/8+3s_C/8.       (4)

With the retained universal Type-E floor Q>=17456771/635040 and (3),

    Q_safe >= 2073126471766663342507/81315686078061281280
            =25.494791617161... .

If the separately retained center-variance theorem is also assumed, the stronger historical Q>5876056025347/211680000000 gives Q_safe>25.764691270790... . The improved scalar floor does not yet yield a Type-E contradiction.

**[PROVED EXACTLY — finite-polynomial KKT interface]** For disjoint core pairings (i,j),(k,l), epsilon_ij+epsilon_kl<=A_C/2, by epsilon_ij<=sqrt(a_i*a_j)<=(a_i+a_j)/2. For each triple of midpoint vectors, the 3x3 PSD Gram minor gives

    (a_i*c_jk-c_ij*c_ik)^2
      <= (a_i*a_j-c_ij^2)*(a_i*a_k-c_ik^2).            (5)

The six signs of c_ij should be enumerated in the next finite polynomial/KKT analysis. Two large defects sharing one vertex can force a compensating positive correlation between their opposite vertices; this has not yet been converted into a certified numerical improvement.

**[VERIFIED LOCALLY]** The companion Fraction checker verifies all rational constants, the strict sub-two identity, 1,089 scalar endpoint-grid cases, 1,548 six-defect allocations, and rational four-vector Gram cases. The analytic proof, not the finite test grid, establishes (1)-(5).

**[OPEN]** Type E, Type C, Type D, generic e>=27, and non-isolated branches remain unresolved. Sparse e=23/24 graph classification remains conditional on delta(G)>=1. Preserve M(F3)<=89, M(P)>=S/2-28/3, the twenty-edge mass >=2137/6, A<=383/504, and the Musin/Boyvalenkov zero-midpoint exclusion. **40<=tau_5<=44** remains the global proved range.
