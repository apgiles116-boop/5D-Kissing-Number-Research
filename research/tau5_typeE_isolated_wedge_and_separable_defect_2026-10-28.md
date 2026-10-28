# Type E: isolated fourth-energy, midpoint-wedge SOS, and separable core-defect tightening (2026-10-28)

**[PROVED EXACTLY — algebra]** The identity below is an exact refinement of the earlier frame/mixing square completion, retaining the isolated-edge fourth energy and midpoint wedge dispersion. The separable core-defect inequality is also exact.

**[PROVED EXACTLY — CONDITIONAL TYPE E]** Assuming the previously retained F3 graph, endpoint-charge/signed-triangle/diagonal-interference lemmas, and mass certificates, the effective corrected harmonic-positive defect ceilings improve to **183/1024** for P1/P3 and **6173/51200** for P2. These are not standalone raw quartic bounds.

**[OPEN]** No exclusion of Type E; the global proved range remains 40 <= tau_5 <= 44.

## 1. Exact isolated-energy and midpoint-wedge decomposition

Retain the 20 selected deep edges with endpoints m_i +/- z_i, m_i.z_i=0, a_i=||m_i||^2, r_i=||z_i||^2=1-a_i. Let C be the four selected F3 core edges, K their six pairings, and R the other 184 endpoint-safe pairings. Write

    A=sum a_i, U=sum a_i^2, U_C=sum_{i in C}a_i^2,
    U_I=U-U_C, R2=sum r_i^2=20-2A+U,
    F_z=sum z_i z_i^T, F_w=sum r_i z_i z_i^T,
    B=sum a_i m_i m_i^T, B0=B-(U/5)I,
    E=F_w-(R2/5)I, W=||E||_F^2,
    h_ij=1-r_i*r_j, X_ij=m_i.z_j, Y_ij=z_i.m_j,
    T_R=sum_{ij in R}h_ij*(X_ij^2+Y_ij^2).

Use the previously defined nonnegative slacks

    J1=sum_R[(h_ij-a_i)X_ij^2+(h_ij-a_j)Y_ij^2],
    J2=tr(B(F_z-F_w)),
    J3=3*U_C-sum_K[a_i X_ij^2+a_j Y_ij^2].

Define the **midpoint wedge dispersion**

    Omega=U^2-tr(B^2)
         =2*sum_{i<j} a_i*a_j*(a_i*a_j-(m_i.m_j)^2) >= 0.

The equality follows by expanding B and using ||m_i||^2=a_i. Every summand is nonnegative by Cauchy-Schwarz. Then the previous exact frame/mixing identity rearranges to the stronger **EXACT SOS identity**

    (5/24)*W+(1/4)*T_R
      = U*(1/4-A/10-U/100)
        +(3/4)*U_I+(3/40)*Omega
        +(5/24)*||E+(3/5)*B0||_F^2
        +(J1+J2+J3)/4.                                    (1)

Proof: the old identity has base U*R2/20-(3/4)U_C-(3/40)||B0||^2. Substitute U_C=U-U_I, R2=20-2A+U and ||B0||^2=tr(B^2)-U^2/5; simplify. No endpoint-contact, D5 labeling, or SDP assumption is needed for this algebraic identity.

Unlike the previous coarse inequality, (1) retains **3 U_I/4** and **3 Omega/40** as explicit positive costs. It also retains all three J slacks and the matrix-square slack.

## 2. Mass-concavity stability forces isolated energy near scalar saturation

This section is **[PROVED EXACTLY — CONDITIONAL ON RETAINED F3 MASS CERTIFICATES]**. Let

    D(t)=196t-644t^2+896t^3-448t^4,
    r=D^{-1}(15) = (1-sqrt((7+sqrt(721))/56))/2,
    s0=D^{-1}(43/3), s1=D^{-1}(41/6),
    Astar=1/2+r+s1, Ustar=1/8+r^2+s1^2,
    Delta=r+s1-s0 > 0.

All inverse roots refer to the unique roots on [0,1/4]. The retained scalar mass argument gives x=A_I in [0,r], s(x)=D^{-1}(43/3-D(x)/2), A<=1/2+x+s(x), and U_C<=1/8+s(x)^2. The function s(x) is convex and decreasing, so both s(x) and x+s(x) lie below their endpoint chords.

Set epsilon=Astar-A>=0 and eta=Ustar-U>=0. The chord for x+s(x) implies

    x >= r*(1-epsilon/Delta).

The chord for s(x) then gives

    s(x) <= s1+(s0-s1)*epsilon/Delta.

Since U_I=U-U_C, this yields the quantitative stability bound

    U_I >= [
       r^2-eta
       -2*s1*(s0-s1)*epsilon/Delta
       -(s0-s1)^2*(epsilon/Delta)^2
    ]_+.                                                     (2)

This is an exact inequality between the scalar mass-relaxation quantities, not an assertion that the scalar extremizer is a feasible Type-E code. At epsilon=eta=0, (2) forces U_I=r^2 (the isolated energy is concentrated on one isolated edge in the scalar relaxation).

Combining (1) and (2) shows that simultaneous near-saturation of the mass bounds Astar,Ustar requires a nonzero frame/safe-mixing cost. At exact scalar saturation, the isolated-energy contribution alone is

    3*r^2/4 = 0.0092832908046...,

in addition to c(Astar,Ustar)*Ustar=0.0255001478842..., with c(A,U)=1/4-A/10-U/100. Thus (1) forces at least 0.0347834386888... before the other nonnegative slacks, compared with 0.0255001478842... from the earlier scalar coercivity. These decimal values are evaluations of exact radical/algebraic expressions, not new universal constants.

## 3. New separable active-core defect inequality

For an active exceptional core pair put

    d=|z_i.z_j|-1/2 > 0, g(d)=d+d^2,
    w=(1/2+d)^2, a=a_i, b=a_j,
    f(d)=w*g(d).

Endpoint safety gives m_i.m_j<=-d, hence ab>=d^2. The exact core-orthogonality estimate from the earlier J3 note gives

    J3 >= J3core
       := sum_{ij in K} [
          a_i*a_j*(a_i+a_j)
          +w_ij*(a_i^2/r_i+a_j^2/r_j)
       ] >=0.                                               (3)

For one active pair, its contribution to the corrected positive defect budget **after subtracting its J3core/4 term** is at most

    f(d)+h_ij*g(d)/4
       -[ab*(a+b)+w*(a^2/(1-a)+b^2/(1-b))]/4.

Using h_ij=a+b-ab<=a+b, a^2/(1-a)>=a^2, ab(a+b)>=2d^3, and the two completed squares

    g*a-w*a^2 <= g^2/(4w),
    g*b-w*b^2 <= g^2/(4w),

we obtain the new **exact separable bound**

    Fsep(d)=f(d)+g(d)^2/(8w)-d^3/2
           =d*(16d^5+40d^4+50d^3+34d^2+11d+1)
             /[4*(2d+1)^2].                                 (4)

It is increasing and strictly convex for d>=0, because Fsep'(0)>0 and

    Fsep''(d) =
      (384d^6+1056d^5+1240d^4+800d^3+300d^2+62d+7)
      /[2*(2d+1)^4] >0.

For the two-contact diagonal, the earlier uniform h<=7/16 and quadratic J3 penalty, **now retaining the cubic J3 penalty**, yield a better function at large d:

    Fdiag(d)=f(d)+(7/64)*g(d)
              -w*d^2/[2*(1-d)]-d^3/2.                       (5)

Fdiag is increasing and convex on [0,1/4]. Indeed its second derivative is

    (384d^5-768d^4+151d^3+315d^2+69d-79)
      /[32*(d-1)^3] >0;

the numerator is negative on [0,1/4] even after dropping the negative -768d^4 term, and the denominator is negative.

## 4. Exact branchwise effective defect caps

**[PROVED EXACTLY — CONDITIONAL ON RETAINED F3 ENDPOINT LEMMAS]**

P2: at most three one-contact pairings are active, each d<1/8, with total d<=1/4. Convex capped-simplex allocation gives

    sum_active Fsep(d) <= 2*Fsep(1/8)
                        = 6173/51200
                        = 0.12056640625.                    (6)

The same bound applies to P1/P3 when their two-contact diagonal is inactive.

P1/P3 diagonal active: write d0 for its defect. The endpoint-charge/signed-triangle lemmas allow at most two additional one-contact active pairs.

* None active: Fdiag(d0)<=Fdiag(1/4)=183/1024.
* One active, defect s<=1/8: d0<=3/16-s/2-s^2. By convex secants Fdiag(d0)<=[16 Fdiag(3/16)/3]*d0 and Fsep(s)<=[8 Fsep(1/8)]*s. The resulting concave quadratic is increasing on [0,1/8] and at s=1/8 equals 10904461/85196800 <183/1024.
* Two active, total defect s<=1/4: d0<=1/6-s/3-s^2/3. Convex secants give Fdiag(d0)<=[6 Fdiag(1/6)]*d0 and sum Fsep(d_i)<=[8 Fsep(1/8)]*s. The resulting concave quadratic is increasing on [0,1/4] and at s=1/4 equals 13591/86400 <183/1024.

Thus the corrected net positive-defect ceilings after the core J3core/4 penalty are

    C_P1=C_P3=183/1024 = 0.1787109375,
    C_P2=6173/51200    = 0.12056640625.                    (7)

Earlier caps were 191/1024 and 479/3584 respectively. This is a reduction of 4.19% and 9.79%. These bounds do not imply a Type-E contradiction.

## 5. Strengthened necessary harmonic inequality retaining the full geometry

Write T_ij=(m_i.m_j)^2+(m_i.z_j)^2+(z_i.m_j)^2 for ij in R, and define

    Resid_R=sum_{ij in R}[
       w_ij*T_ij+(h_ij/4)*(m_i.m_j)^2
    ] >=0,
    J3slack=J3-J3core >=0.

The audited fixed-versus-weighted harmonic inequality, combined with the exact decomposition (1), yields the following **necessary Type-E condition**:

    H4plus
      +c(A,U)*U+(3/4)*U_I+(3/40)*Omega
      +(5/24)*||E+(3/5)*B0||_F^2
      +(J1+J2+J3slack)/4+Resid_R
    <= C_branch-R2^2/56+(3/8)*S4
       +(19/16)*A-(A^2-U)/32,                              (8)

where S4=sum r_i^4 and c(A,U)=1/4-A/10-U/100. For the retained stronger mass bounds, c(A,U)>=c(Astar,Ustar)>917532974747/5000000000000>0.

Equation (8) retains the isolated fourth-energy penalty, wedge dispersion, frame-square, two additional J slacks, the unused J3 slack, and the 184-safe residual. It is a stricter interface for a future finite polynomial/SOS or KKT certificate. No contradiction has yet been proved.

## 6. Verification and proof ledger

**[VERIFIED]** Companion SymPy script checks the rational expressions, exact branch envelopes, convexity identities, pairwise active-defect inequalities on rational test cases, exact 20-vector frame/mixing identity with rational vectors, J3core slack, and exact brackets for the three scalar mass roots. The general proofs are the analytic derivations above, not the finite test cases.

**[RETAINED]** Global 40<=tau_5<=44. Type E has M(F3)<=89, some matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504 (strengthened conditionally by Astar), U<=Ustar, and rigorous zero-midpoint exclusion via Musin/Boyvalenkov. The 184 safe/six core split and prior F3 endpoint lemmas are retained inputs, not independently re-proved here.

**[OPEN]** Type E, Types C and D, generic e>=27, and non-isolated branches. Sparse e=23/e=24 classification still assumes delta(G)>=1. Priority: exploit (8) with the isolated-center row and rank-five Gram geometry, particularly the P1/P3 diagonal-only branch.

Companion verifier: tau5_typeE_isolated_wedge_defect_2026-10-28_verify.py.
