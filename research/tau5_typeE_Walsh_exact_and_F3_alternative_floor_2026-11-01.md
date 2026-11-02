# Exact four-sign Walsh reduction and alternative-F3 midpoint floor (2026-11-01)

**[PROVED EXACTLY — standalone identities and eight-vector lemma].** **[CONDITIONAL TYPE E]** Applies only under the stated F3 incidence. **[OPEN]** No Type-E exclusion. Global proved range 40<=tau_5<=44.

## 1. Exact two-sided-safe Walsh characterization

For two selected deep edges write unit endpoints u_i^s=m_i+s*z_i (s=+/-1), m_i.z_i=0. Put

    c=m_i.m_j, d=z_i.z_j, p=m_i.z_j, q=z_i.m_j.

The four cross-products are T_st=c+s*q+t*p+s*t*d. All four cross-pairs are two-sided safe (|T_st|<=1/2) **if and only if**

    |c+d|+|p+q| <= 1/2,
    |c-d|+|p-q| <= 1/2.                              (W)

Indeed T_++=c+d+p+q, T_--=c+d-p-q, T_+-=c-d+q-p, T_-+=c-d-q+p; apply max(|x+y|,|x-y|)=|x|+|y| twice. Consequences are

    |m_i.m_j|+|z_i.z_j|<=1/2,
    |m_i.z_j|+|z_i.m_j|<=1/2,                        (W1)

and the exact Walsh Parseval identity gives

    (m_i.m_j)^2+(z_i.z_j)^2+(m_i.z_j)^2+(z_i.m_j)^2
       =(1/4)*sum_(s,t) T_st^2 <=1/4.              (W2)

**[AUDIT CLARIFICATION]** A temporary audit was withdrawn because it checked only T_st<=1/2, overlooking the necessary lower bound T_st>=-1/2. The earlier inference |z_i.z_j|<=1/2 for *fully two-sided-safe* isolated pairs is correct. The stronger (W) retains mixed terms and can be used directly in a finite polynomial/KKT formulation.

## 2. Positive floor for both alternative F3 perfect matchings

Use F3 deep edges 02,04,05,14,17,23,27,36,56,57; all other 18 pairs are two-sided safe. Its perfect matchings are

    P0=04|17|23|56,
    P1=02|14|36|57,
    P2=05|14|27|36.

Define C_k=sum_(ij in Pk) ||(u_i+u_j)/2||^2.

**[PROVED EXACTLY — standalone eight-unit-vector theorem]**

    C_1 > (7-4*sqrt(3))/16 = 0.00448729810778...,
    C_2 > (7-4*sqrt(3))/16.                         (F)

Proof for P1: put m_A=(u0+u2)/2, m_B=(u1+u4)/2, m_C=(u3+u6)/2, m_D=(u5+u7)/2, and a=u0, d=u5, b=u1, c=u3, w=a+d, v=b+c. Deep edges 04,17,23,56 give

    a.b>=1/2-2||m_B||, d.b>=1/2-2||m_D||,
    a.c>=1/2-2||m_A||, d.c>=1/2-2||m_C||.

Hence w.v>=2-2*(||m_A||+||m_B||+||m_C||+||m_D||). Deep 05 implies ||w||^2=2+2a.d<1. Safe 13 implies ||v||^2=2+2b.c<=3. Cauchy gives

    2-2*sum ||m_*|| <= w.v < sqrt(3),
    sum ||m_*|| > (2-sqrt(3))/2.

A second Cauchy gives sum ||m_*||<=2*sqrt(C_1). Therefore C_1>(2-sqrt(3))^2/16=(7-4*sqrt(3))/16. The F3 automorphism (2 5)(3 6) preserves all deep/safe incidences and interchanges P1,P2, proving the C2 inequality.

This floor is not claimed sharp. It rules out an exactly antipodal alternative F3 matching, but does not approach the Type-E midpoint cap.

## 3. Proof ledger

**[PROVED EXACTLY]** (W), (W1), (W2), (F). The companion SymPy verifier checks the Walsh identities, F3 automorphism, edge incidences and algebraic constant. The Cauchy argument, not numerical optimization, establishes (F).

**[CONDITIONAL TYPE E]** If the mass-selected F3 matching is P1 or P2, its midpoint energy is strictly greater than (7-4sqrt(3))/16. This is compatible with the retained A<=383/504 and the separately stronger harmonic cap.

**[OPEN]** Combine the full mixed-term Walsh constraints with the 20-line Q-frame variance, six exceptional core pairings and F3 incidence to seek second-order control. Type E, Types C,D, generic e>=27 and non-isolated branches remain open. Sparse e=23/e=24 classification is conditional on delta(G)>=1. Preserve star <=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6 and Musin/Boyvalenkov zero-midpoint boundary. Global range 40<=tau_5<=44.

Verifier: research/verify_Walsh_F3_alternative_floor_2026-11-01.py.
