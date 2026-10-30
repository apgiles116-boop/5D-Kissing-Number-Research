# Type E: rank-14 safe-subframe defect and core-energy/slack tradeoff (2026-10-29)

**[PROVED EXACTLY — rank and scalar lemmas; CONDITIONAL Type-E application]**. No D5 alignment or new SDP is assumed. **Type E remains open; global proved range 40 <= tau_5 <= 44.**

## Rank-14 quadratic-defect lemma

For n>=15 unit vectors u_i in R^5 put Delta_ij=(u_i.u_j)^2-1/4. The traceless projectors Q_i=u_i u_i^T-I/5 have Gram matrix K_ij=(u_i.u_j)^2-1/5 with rank at most dim Sym_0(5)=14. Compare with K0=(3/4)I_n+(1/20)J_n, whose diagonal equals 4/5 and whose off-diagonal equals 1/20. Its smallest eigenvalue is 3/4, with multiplicity n-1. Eckart–Young and rank(K)<=14 give

    2 sum_{i<j} Delta_ij^2 = ||K-K0||_F^2 >= (n-14)*9/16,

so

    sum_{i<j} Delta_ij^2 >= 9(n-14)/32.               (1)

For n=16 the bound is 9/16; for n=17 it is 27/32.

## Conversion to raw safe-contact slack

Let z_i=sqrt(1-a_i)u_i, 0<=a_i<=1/4, and suppose all pairwise raw correlations obey |d_ij|=|z_i.z_j|<=1/2. Write w_ij=(1-a_i)(1-a_j), h_ij=1/2-|d_ij|, A_*=sum a_i<1, U_*=sum a_i^2. Then

    (Delta_ij)_+ <= (1-w_ij)/(4w_ij) <= (7/18)(a_i+a_j),  (2)
    (-Delta_ij)_+ <= h_ij/w_ij <= h_ij/(1-A_*).        (3)

The 7/18 constant follows from
(1-w)/w = a_i/(1-a_i)+a_j/(1-a_j)+a_i*a_j/w
<= (4/3)(a_i+a_j)+(16/9)(a_i+a_j)/8
= (14/9)(a_i+a_j).
It is sharp for a_i=a_j=1/4. Also
sum_{i<j}(a_i+a_j)^2=(n-2)U_*+A_*^2.
Thus (1)–(3) prove

    H_n=sum_{i<j}h_ij^2
       >= (1-A_*)^2 * [9(n-14)/32
                          -(49/324)((n-2)U_*+A_*^2)].  (4)

A negative bracket gives a vacuous bound, not a contradiction.

## The 16 isolated Type-E pairs

Under the retained Type-E reduction H=16K2+F3, the 16 isolated selected deep edges have all 120 cross-pair blocks safe. Put A_I=sum_{i in I}a_i and U_I=sum_{i in I}a_i^2. From (4):

    H_120=sum_{i<j in I}(1/2-|z_i.z_j|)^2
       >= (1-A_I)^2[9/16-(49/324)(14U_I+A_I^2)].      (5)

Using U_I<=A_I/4 and A_I<=A<=B=383/504 yields the exact uniform floor

    H_120 >= 1793273603/426649337856 > 0.00420315.  (6)

## The isolated center gives a stronger 17-line certificate

Adjoin the isolated center v=x_0 as u_0=z_0=v, a_0=0. Its two endpoint contacts with every isolated edge are safe, hence |v.z_i|<=1/2. There are 136 safe pairs among these 17 lines. For center–isolated pairs, (Delta_0i)_+<=a_i/[4(1-a_i)]<=a_i/3, improving (2). Thus

    H_136=H_120+sum_{i in I}(1/2-|v.z_i|)^2
       >= (1-A_I)^2[27/32-(361/162)U_I-(49/324)A_I^2]. (7)

Using U_I<=A_I/4 and A_I<=383/504 gives

    H_136 >= 57333292181/2986545364992 > 0.01919719. (8)

## Explicit core-energy tradeoff

Write A_C=sum_{four core edges}a_i, so A_I<=B-A_C. On 0<=t<=B define the decreasing positive functions

    f16(t)=(1-t)^2[9/16-(49/324)(7t/2+t^2)],
    f17(t)=(1-t)^2[27/32-(361/648)t-(49/324)t^2].

Then H_120>=f16(B-A_C) and H_136>=f17(B-A_C). Conditional on A_C>=1/4, these give H_120>0.0608 and H_136>0.1249. This is a quantitative core-energy/safe-slack compensation, **not** a core-energy lower bound or a Type-E exclusion.

## Status and dependencies

**[PROVED EXACTLY]** Rank-defect lemma, sharp scalar 7/18 normalization, 16/17 safe-subframe inequalities, and exact rational floors. The companion Fraction/SymPy verifier checks the constants and exact D5 test cases; finite tests are not substituted for the linear-algebra proof.

**[RETAINED, NOT REPROVED]** Isolated-center Type-E matching reduction, deep-edge a_i<=1/4, A<=383/504, star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, 20-edge mass >=2137/6, Musin/Boyvalenkov 21-line zero-midpoint exclusion.

**[OPEN]** Need an incompatible upper bound on H_120 or H_136, using the 184 safe Walsh blocks and six core exceptions. Type C, D, generic e>=27, and non-isolated branches remain open; sparse e=23/24 classification requires delta(G)>=1. Global 40<=tau_5<=44.

Companion verifier: research/tau5_typeE_safe_subframe_rank_defect_2026-10-29_verify.py.
