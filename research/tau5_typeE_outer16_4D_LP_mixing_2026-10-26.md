# Type E: rational 4D projection obstruction and safe mixed-frame coercivity

Date: 2026-10-26.

**[PROVED EXACTLY]** The four-dimensional 16-line coherence certificate, projected-frame polynomial and mixed-frame trace inequality. **[CONDITIONAL ON RETAINED TYPE-E HYPOTHESES]** The existence of 16 mutually safe outside-core selected edges. **[OPEN]** Exclusion of Type E.

## 1. Exact rational LP certificate in R^4

Let P_k(t)=U_k(t)/(k+1), with U_k the Chebyshev polynomial of the second kind, the normalized positive-definite zonal polynomials on S^3. Put

    mu=73/132,
    f(t)=(t+1)(t+2/3)^2 t^2(t-mu).

The exact expansion is

    f=(1475/19008)P0+(5455/19008)P1
      +(1621/3168)P2+(1475/2376)P3
      +(215/396)P4+(235/704)P5+(7/64)P6.

All coefficients are strictly positive; f(t)<=0 on [-1,mu], and f(1)=1475/594=32*(1475/19008). For N antipodal points in S^3 with all distinct-pair inner products <=mu, the positive-definite kernel bound gives

    (1475/19008)N^2 <= sum_{p,q} f(p.q) <= N f(1),

so N<=32. Equality for N=32 forces every distinct-pair inner product to be a root of f. For two different projective lines, antipodality forces both s and -s to occur, but the only common root of f(s) and f(-s) with |s|<1 is zero: the roots are -1,-2/3,0,mu, and mu != 2/3. Sixteen orthogonal lines cannot lie in R^4. Thus **every sixteen projective lines in R^4 have coherence strictly greater than 73/132**.

## 2. Exact spectral obstruction for 16 safe projected lines

Let z_1,...,z_16 in R^5 satisfy ||z_i||^2=1-a_i, 0<=a_i<=1/4, and |z_i.z_j|<=1/2 for i!=j. Set

    A_O=sum_i a_i,
    F_O=sum_i z_i z_i^T,
    lambda=lambda_min(F_O).

**[PROVED EXACTLY]**

    5329 A_O+14041 lambda+4356 lambda^2 > 973.    (T)

Choose a unit eigenvector w of F_O for lambda and project v_i=z_i-(w.z_i)w into w^perp=R^4. If any v_i=0, then lambda>=||z_i||^2>=3/4 and (T) is immediate. Otherwise the 4D result supplies i!=j with

    (73/132)||v_i||||v_j|| < |v_i.v_j|
      <= |z_i.z_j|+|(w.z_i)(w.z_j)| <= (1+lambda)/2.

Writing p_i=a_i+(w.z_i)^2, we have p_i+p_j<=A_O+lambda and (1-p_i)(1-p_j)>=1-A_O-lambda. If A_O+lambda>=1, (T) is immediate; otherwise square the displayed inequality and clear denominators to obtain (T).

For A_O<973/5329 this implies the positive lower bound

    lambda > [sqrt(14041^2+17424*(973-5329*A_O))-14041]/8712.

In particular A_O<=1/10 forces lambda>3/100, because

    5329/10+14041*(3/100)+4356*(3/100)^2
       =1197563/1250 < 973.

## 3. Exact unweighted safe endpoint mixing

In Type E, let O be the 16 selected edges outside the F3 core. All pairs involving an outer edge are safe. Write F_m=sum_{i=1}^{20}m_i m_i^T, A=tr(F_m), and m_i.z_i=0. Then

    M_safe := sum_{safe {i,j}}[(m_i.z_j)^2+(z_i.m_j)^2]
       >= sum_{i=1}^{20}sum_{j in O}(m_i.z_j)^2
       = tr(F_m F_O) >= lambda A.

Hence **[CONDITIONAL ON RETAINED TYPE-E HYPOTHESES]**, if A_O<=1/10, then M_safe>(3/100)A. This is an unweighted mixing estimate. It must not be substituted for the harmonic quantity J, which weights each mixed term by (z_i.z_j)^2. A rigorous relation between M_safe and J is still missing.

**[OPEN]** No Type-E exclusion and no improvement to the retained 1/99<A<=383/504 energy interval. Preserve M(F3)<=89, M(P)>=S/2-28/3, and global 40<=tau_5<=44. Types C,D, generic e>=27 and non-isolated branches remain open.