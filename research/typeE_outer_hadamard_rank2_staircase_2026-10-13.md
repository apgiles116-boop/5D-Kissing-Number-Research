# Type E: four-contact Hadamard outer-frame stability (2026-10-13)

**Status:** Exact deductions conditional on retained Type-E endpoint geometry and the previously certified midpoint-energy and harmonic projection inequalities. **NOT** a Type-E exclusion. Global retained range: **40 <= tau_5 <= 44**.

## Inputs and matching scope

For the 16 isolated K2 deep edges write x_i^±=m_i±z_i, m_i·z_i=0, a_i=||m_i||²<1/4, ||z_i||²=1-a_i. Let A_O=Σ a_i, S_Z=Σ z_i z_i^T, S_M=Σ m_i m_i^T. Every four cross-endpoint contacts between distinct outer edges lie in [-1/2,1/2]. The mass-selected four-core matching has A_O+A_C<=383/504, M(F3)<=89, M(P)>=M(F3)/2-28/3. For core rank <=2, the previously established angular theorem gives A_C>5/12 and A_O<173/504. This energy bound is for the **selected** matching only.

## New exact four-contact identity

For any two distinct outer edges put q=m_i·m_j, c=z_i·z_j, v=z_i·m_j, w=m_i·z_j. The four endpoint products u_st=q+s v+t w+st c satisfy the Walsh-Hadamard identity

    Σ_{s,t=±1} u_st² = 4(q²+c²+v²+w²) <= 1.

Summing over 120 outer pairs, and using m_i·z_i=0,

    Σ_{i<j}(z_i·z_j)² + Σ_{i<j}(m_i·m_j)²
        + tr(S_Z S_M) <= 30.

Consequently

    tr(S_Z²) <= 76 - 2 A_O + Σ a_i²
                     - 2 tr(S_Z S_M)
                     - 2 Σ_{i<j}(m_i·m_j)².                 (H)

Using Σ a_i²<=A_O/4 and S_Z ≻ η I gives

    tr(S_Z²) <= 76-(7/4+2η)A_O
                  -2 Σ_{i<j}(m_i·m_j)².

The previously proved general η=2/15 yields **tr(S_Z²)<=76-(121/60)A_O**, improving the previous coefficient 7/4.

## New rank-two-specific harmonic projection gaps

Under core rank <=2, A_O<173/504. The retained four-dimensional projection inequalities L4(A,λ)<=U(A,λ) have

    D=7A/4+3λ/2-λ²
    L4=2-7A/8-5λ/4-3λ²/2+D²/32
    U=15λ/8+λ²/8+λ²(1+λ/2)²/2+15(A+λ)/16
      +(1+λ/2)(7λ/4+7λ²+(A+λ)λ/2)/4.

On 0<=A<=173/504, 0<=λ<=6/25, L4 decreases in both arguments and U increases. The exact endpoint gap is

    L4(173/504,6/25)-U(173/504,6/25)
       =352131428671/7257600000000 > 0.

Thus **α1>6/25** for the smallest eigenvalue of S_Z.

The retained three-dimensional harmonic projection has

    L3=134/15-313A/120-179λ/60-3λ²/2+7D²/120.

On 0<=A<=173/504, 0<=λ<=3/4 it decreases while U increases, but

    L3(173/504,3/4)-U(173/504,3/4)
       =792149/13934592 > 0.

Ky Fan implies **α1+α2>3/4**. Therefore (H) strengthens on the rank-two branch to

    tr(S_Z²) <= 76-(223/100)A_O
                     -2 Σ_{i<j}(m_i·m_j)².

## Stronger spectral and core-correlation consequences

By Cauchy-Schwarz on eigenvalue blocks and exact rational endpoint checks:

| Scope | α1+α2+α3 | α5 |
|---|---|---|
| All Type E | >167/50 | <779/100 |
| Core rank <=2 | >189/50 | <193/25 |

The exact lower-three contradiction gaps are respectively 3618737/63504000 and 3607313/63504000. The largest-eigenvalue contradiction gaps are 11751701/127008000 and 14204669/127008000.

Let C=Z_C^T Z_C with descending eigenvalues γ1,...,γ4 and X=Z_O^T Z_C. In the rank-two core branch,

    ||X||_F² > (6/25)(4-A_C) + (51/100)γ2
                    + (303/100)γ3 + (9/2-A_O)γ4.

Here γ3=γ4=0 and the retained one-contact F3 wedge implies γ2>1/8, giving

    ||X||_F² > (6/25)(4-A_C)+51/800.

For a one-contact core pair j,k, the retained core wedge determinant exceeds 11/64. Since α1α2>153/1250, the corresponding two outer-correlation columns obey the exact quartic bound

    ||x_j||²||x_k||²-(x_j·x_k)² > 1683/80000.

This improves the previous universal bound 341/28800, **only in the core-rank-two branch**.

## Limitations and next target

The four-contact identity and rational checks are exact, but the global graph reduction, mass certificate, core angular theorem, and harmonic projection positivity are retained inputs, not reproved here. The mixed lower bounds do not yet contradict safe-pair upper bounds. Rank-two, rank-three, rank-four Type E, Types C/D, generic e>=27 and the δ(G)>=1 sparse-graph prerequisite remain open.

Next: impose all six actual F3 deep-contact sign patterns in the rank-two core Gram/KKT system and seek a finite infeasibility certificate. Do not infer any D5 labeling from Q-nullity six.
