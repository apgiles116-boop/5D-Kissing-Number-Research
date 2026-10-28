# Type E: high-center binary contacts, 71-edge threshold, and integral rank-8 reduction (2026-10-28)

**[NEW, EXACT ALGEBRA — CONDITIONAL TYPE E, HIGH-CENTER BRANCH]** Suppose a hypothetical 41-code has an isolated deep-graph center v, H=16K2+F3, and its center second moment s=sum_{w != v}(v.w)^2 satisfies s>=7. Retain the previously audited isolated-center harmonic identity, F3 broom bound S=M(F3)<=89, and the exact high-center resource inequality in `tau5_typeE_center_quantized_KKT_2026-10-28.md`. Then the 40 center contacts have **exactly 28 high and 12 low absolute inner products**; among the sixteen isolated deep-edge pairs, their 120 mutual pairings have a binary near-contact structure with **at least 71 high pairings**. A rounded 17-by-17 signed Gram matrix has integer double, **rank at most 8**, and nullity at least 9.

**[OPEN]** This is not a Type-E exclusion and is not a D5 labeling theorem. It provides a finite signed-graph/rank target. Global proved range remains 40<=tau_5<=44.

## 1. Retained resource budget and exact rational thresholds

Let D(a)=196a-644a^2+896a^3-448a^4. For the 16 isolated selected deep edges write a_i=||m_i||^2, x=sum_I a_i, and let N=sum_nondeep f(t), where f(t)=7t^2(1-4t^2). Let d=s-7, R=N-N0, and S=M(F3). The previous high-center proof gives

    D(x)+g(d)+R <= 5/64,
    g(d)=7/4*d*(1+d)*(21*d^2-49*d+20),
    N<=5/64,

and s<7.005. Since D(1/2500)>5/64 and g(1/400)>5/64, with D and g increasing on the relevant intervals,

    0<=x<1/2500,       0<=d<1/400.                     (1)

More precisely, retaining the previously discarded broom slack gives the exact necessary budget

    (89-S)+D_I+g(d)+R+J <= 5/64,                       (2)

where D_I=sum_I D(a_i), and J=E+N0-[955/64+g(d)]>=0 is the center-harmonic/quantization residual. This follows from S=74+D_I+N+E and E+N0>=955/64+g(d). Thus in this branch S>=89-5/64, with every term in (2) nonnegative.

Since every individual nondeep f(t)<=N<=5/64 and f(t) is concave as a function of t^2, while

    f(1/9)=539/6561 > 5/64,
    f(12/25)=49392/390625 > 5/64,

every nondeep contact obeys the **disjoint rational alternative**

    |t|<1/9       OR       12/25<|t|<=1/2.              (3)

Call these low and high contacts.

## 2. Exactly 28 high contacts at the isolated center

For the 40 center contacts set y_j=4t_j^2 in [0,1], and p_j=0 or 1 according as the contact is low or high. Then p_j is the nearest endpoint of [0,1], and

    |y_j-p_j|=min(y_j,1-y_j)<=2y_j(1-y_j).

Since N0=(7/4)sum_j y_j(1-y_j),

    |4s-k|<=sum_j|y_j-p_j|<=8N0/7<=5/56,
    k=sum_j p_j integer.

But 28<=4s<28+1/100 by (1). Necessarily **k=28**. Thus 28 center contacts have |t|>12/25 and the other 12 have |t|<1/9. This is an exact count, not merely a bound on the number of outliers.

For each isolated deep edge x_i^+/-=m_i+/-z_i, the center products t_i^+/- satisfy

    |t_i^++t_i^-|=2|v.m_i|<=2sqrt(a_i)<1/25.

A high and a low value cannot coexist because 12/25-1/9>1/25. Hence each isolated edge contributes either zero or two high center contacts; in the high case the signs are opposite. Writing k_I for the number of high isolated edges gives

    k_I in {10,11,12,13,14},
    number of high F3-core endpoints =28-2k_I in {8,6,4,2,0}.    (4)

## 3. Binary structure of all 120 isolated-isolated pairings

For two isolated edges i,j, all four endpoint scalar products

    t_{sigma,tau}=(m_i+sigma z_i).(m_j+tau z_j),  sigma,tau in {+1,-1}

are nondeep. Flipping one sign gives

    |t_{sigma,tau}+t_{-sigma,tau}|<=2sqrt(a_i)<1/25,
    |t_{sigma,tau}+t_{sigma,-tau}|<=2sqrt(a_j)<1/25.

By (3), high/low categories cannot differ under either flip. Thus all four contacts are low, or all four are high. In the high case every sign flip reverses the sign of t. The exact Walsh formula

    z_i.z_j=(t_{++}-t_{+-}-t_{-+}+t_{--})/4

then proves the binary projected-correlation alternative

    |z_i.z_j|<1/9      OR      12/25<|z_i.z_j|<=1/2.    (5)

The first case has four low contacts, and the second has four high contacts with the alternating sign pattern. Let e be the number of high isolated-isolated pairings among the 120.

## 4. At least 71 high pairings [EXACT]

For the sixteen z_i in R5 put U_I=sum_I a_i^2<=x^2. Their Gram frame satisfies the Welch inequality

    Q_I=sum_{i<j in I}(z_i.z_j)^2
       >=[(16-x)^2/5-(16-2x+U_I)]/2
       >=88/5-11x/5-2x^2/5
       > L:=88/5-11/(5*2500)-2/(5*2500^2)
        =274986249/15625000 =17.599119936.          (6)

For a low pairing, Walsh Cauchy gives (z_i.z_j)^2 <= (1/4)sum_{four contacts}t^2. Since |t|<1/9,

    f(t)> (539/81)t^2.

Summing over all low isolated-isolated pairings, their entire projected squared-correlation mass is at most

    Q_low <=(81/(4*539))*N <=405/137984.              (7)

For a high pairing, |z_i.z_j|<=1/2. Therefore

    Q_I <= e/4+405/137984.

The exact rational comparison

    274986249/15625000 > 70/4+405/137984

forces **e>=71**. In particular at least 284 of the 480 endpoint contacts across the 120 isolated-isolated pairings are high. This is a count for this selected 16-edge subsystem only.

## 5. Walsh quantization and a 17-by-17 integral rank reduction

For each of the 184 fully safe selected-edge pairings, the four endpoint contacts are all nondeep. Round each t to t* in {0,+1/2,-1/2}. The Walsh coefficients

    w=(m_i.m_j, m_i.z_j, z_i.m_j, z_i.z_j)
    w*=H^T t*/4

have all entries in (1/8)Z and obey, by H^T H=4I,

    ||w-w*||^2=(1/4)sum_{four contacts}rho(t)^2,
    rho(t)=min(|t|,1/2-|t|).

The previously proved pointwise f(t)>=(21/4)rho(t)^2 and N<=5/64 yield

    sum_{184 safe pairings}||w-w*||^2<=5/1344.       (8)

For isolated-isolated pairings, (3) and the sign pattern show w*=(0,0,0,c_ij) with c_ij in {0,+1/2,-1/2}. Similarly, the two center contacts on each isolated edge round to opposite half-contacts or both zero, so c_i*=round(v.z_i) lies in {0,+1/2,-1/2}.

Let G be the true 17-by-17 Gram matrix of v,z_1,...,z_16 (PSD rank<=5). Construct the symmetric rounded matrix Ghat with diagonal 1, off-diagonal center entries c_i*, and isolated-isolated entries c_ij*. Then 2Ghat is an **integer symmetric matrix with diagonal 2 and off-diagonal 0,+1,-1**. Walsh orthogonality gives

    ||G-Ghat||_F^2
      <= sum_{center-isolated contacts}rho(t)^2
         +(1/2)sum_{isolated-isolated contacts}rho(t)^2
         +sum_I a_i^2
      <=5/336+x^2
      <5/336+1/6250000 <1/64.                       (9)

Thus ||G-Ghat||_F<1/8. The rounded signed graph on 17 vertices has at least 71+k_I>=81 nonzero off-diagonal pairings.

**Integral rank lemma.** For any principal k-by-k submatrix B of Ghat, k=9,...,17, let A be the corresponding principal submatrix of G. It is PSD, rank<=5 and trace<=k. Singular-value perturbation gives

    sum_{j=6}^k sigma_j(B)^2 <1/64,
    sum_{j=1}^5 sigma_j(B) <k+sqrt(5)/8 <k+9/32.

AM-GM therefore gives

    |det B| <
       ((k+9/32)/5)^5 * (1/[64(k-5)])^((k-5)/2)
       <2^(-k),                                     (10)

for every integer k=9,...,17. The nine final comparisons are exact rational checks after squaring. Because 2B has integer entries, det B is an integer multiple of 2^(-k), so det B=0. A real symmetric matrix of rank r has a nonzero principal minor of order r (use the coefficient of lambda^(17-r) in its characteristic polynomial). Consequently,

    **rank(Ghat)<=8,  nullity(Ghat)>=9.**            (11)

Equivalently, the integer signed adjacency matrix S=2Ghat-2I has eigenvalue -2 with multiplicity at least 9. **Ghat has not been proved PSD or rank<=5.** Do not classify it as a D5 root Gram matrix without a further argument.

## Proof status and next exact task

**[EXACTLY VERIFIED, CONDITIONAL]** (1)-(11) follow from the retained high-center resource inequality and elementary Gram/Walsh algebra. Companion Fraction verifier checks the rational thresholds, Welch comparison, Walsh isometry, and all nine determinant gaps.

**[OPEN]** Classify 17-vertex signed graphs with diagonal-2 integer Gram candidate, at least 81 signed edges, eigenvalue -2 multiplicity >=9, and a rank-5 PSD Gram within Frobenius distance 1/8. An exact finite signed-graph spectral/Gram classification could eliminate the high-center branch; the low-center branch s<7 remains separate.

**[GLOBAL RANGE UNCHANGED]** 40<=tau_5<=44. Types C, D, generic e>=27, non-isolated branches, and sparse classification without delta(G)>=1 remain open.
