# Type E: orthogonality-aware core penalty and improved harmonic envelopes

Date: 2026-10-27.

**[PROVED EXACTLY — projection/Gram algebra; Type-E application conditional on retained endpoint and F3 lemmas]** Retaining the previously discarded core slack J3 yields an explicit second-order penalty for exceptional correlations. The effective corrected fourth-harmonic positive cap improves from 215/1024 to **191/1024** in P1/P3, and from 9/64 to **479/3584** in P2. **[OPEN]** No Type-E exclusion; global proved range remains 40 <= tau_5 <= 44.

## 1. Core orthogonality lemma

For 20 selected deep edges, write unit endpoints m_i +/- z_i, with m_i.z_i=0, a_i=||m_i||^2 <=1/4, r_i=||z_i||^2=1-a_i >=3/4, A=sum a_i <=383/504, U=sum a_i^2. Let C be the four core edges, K their six pairings, R the other 184 pairings, and w_ij=(z_i.z_j)^2. The exact frame/mixing identity in tau5_typeE_frame_mixing_coercivity_2026-10-27.md contains the nonnegative slack

    J3 = 3*U_C - sum_{i<j in C} [a_i*(m_i.z_j)^2+a_j*(z_i.m_j)^2],
    U_C = sum_{i in C} a_i^2.

Since m_i is orthogonal to z_i, projection followed by Cauchy--Schwarz gives

    (m_i.z_j)^2 <= a_i*(r_j-w_ij/r_i).

Summing over four core indices proves the new exact lower bound

    J3 >= sum_{i in C} a_i^2*sum_{j in C,j!=i}(a_j+w_ij/r_i).         (1)

In particular J3 >= sum_{i<j in K} w_ij*(a_i^2/r_i+a_j^2/r_j).

For an active exceptional pair d_ij=|z_i.z_j|-1/2>0, endpoint safety implies m_i.m_j<=-d_ij and hence a_i*a_j>=d_ij^2. AM--GM and sqrt((1-a_i)(1-a_j))<=1-sqrt(a_i*a_j) give

    a_i^2/r_i+a_j^2/r_j
      >= 2*a_i*a_j/sqrt(r_i*r_j)
      >= 2*a_i*a_j/(1-sqrt(a_i*a_j))
      >= 2*d_ij^2/(1-d_ij).

Consequently

    J3/4 >= sum_{active K} (1/2+d_ij)^2*d_ij^2/[2*(1-d_ij)].         (2)

The full expression (1), including cubic midpoint terms and inactive core correlations, is stronger and should be retained in finite KKT/SOS work.

## 2. Corrected harmonic interface

Let H4plus>=0 be the five non-frame harmonic squares, R2=sum r_i^2, S4=sum r_i^4 and c=34697/201600. The retained exact frame/mixing square completion, with J3 kept, gives

    (5/24)*W+(1/4)*T_R >= c*U+J3/4.                                  (3)

Inserting (3) into the **audited** fixed-versus-weighted fourth-harmonic comparison (not the withdrawn comparison) yields

    H4plus+c*U+sum_active (1/2+d)^2*d^2/[2*(1-d)]
      <= P_fixed+(1/4)*sum_K (1-r_i*r_j)*delta_ij
         -R2^2/56+3*S4/8+19*A/16-(A^2-U)/32,                        (4)

where delta_ij=[w_ij-1/4]_+=d+d^2 for active pairs and P_fixed=sum_active (1/2+d)^2*(d+d^2). Since 1-r_i*r_j<=7/16, the net defect-dependent contribution is bounded by sum_active F(d_ij), where

    F(d)=(1/2+d)^2*(d+d^2)+(7/64)*(d+d^2)
         -(1/2+d)^2*d^2/[2*(1-d)].                                  (5)

F(0)=0 and F'(0)=23/64>0. It is increasing and convex on [0,1/4], since

    F''(d)=(384*d^5-672*d^4-137*d^3+603*d^2-27*d-79)/(32*(d-1)^3)>0.

The numerator is <=384/1024+603/16-79<0 and denominator is negative.

## 3. Exact F3 branchwise caps

Use the retained signed-triangle, endpoint-charge and diagonal-interference lemmas.

**P2:** At most three one-contact pairs are active, each d<1/8, and sum d<=1/4. Convex capped-simplex allocation gives

    sum_active F(d) <= 2*F(1/8) = 479/3584.                            (6)

**P1/P3, diagonal inactive:** The same bound applies.

**P1/P3, diagonal active:** Let d0 be the two-contact diagonal excess.

- No active one-contact pair: F(d0)<=F(1/4)=191/1024.
- One active one-contact pair of excess s<=1/8: d0<=3/16-s/2-s^2. Thus F(d0)+F(s)<=F(3/16)+F(1/8)=1110407/5963776 <191/1024.
- Two active one-contact pairs with total excess s<=1/4: d0<=1/6-s/3-s^2/3. By convexity F(d0)<=alpha*d0 and F(d1)+F(d2)<=beta*s, with alpha=6*F(1/6)=10397/17280 and beta=8*F(1/8)=479/896. The upper polynomial alpha*(1/6-s/3-s^2/3)+beta*s increases for 0<=s<=1/4, because beta-alpha/2=56551/241920>0. At s=1/4 it is 331439/1935360 <191/1024.

Hence the sharpened necessary Type-E inequality is

    H4plus+(34697/201600)*U
      <= C_branch-R2^2/56+3*S4/8+19*A/16-(A^2-U)/32,                 (7)

with exact branchwise caps

    C_P1=C_P3=191/1024,   C_P2=479/3584.                             (8)

These are bounds for the necessary relaxation, not realizable constructions or a Type-E contradiction.

## 4. Ledger

**[PROVED EXACTLY]** Core orthogonality bound (1), defect penalty (2), audited harmonic interface (4), and branch caps (8). Companion SymPy verifier checks rational algebra, convexity, frame identity and J3 floor on an exact rational 20-edge example.

**[RETAINED, not reproved]** Global 40<=tau_5<=44; Type E 1/49<A<=383/504; M(F3)<=89; matching mass >=S/2-28/3; twenty-edge mass >=2137/6; 184 safe pairings; Musin/Boyvalenkov zero-midpoint exclusion. Sparse e=23/24 classification assumes delta(G)>=1.

**[OPEN]** Type E, C, D, generic e>=27, and non-isolated branches. Next: retain the full J3 floor (1), J1/J2, isolated-center row and rank-five projected/midpoint Gram constraints in the P1/P3 diagonal-only branch. No global improvement is claimed.
