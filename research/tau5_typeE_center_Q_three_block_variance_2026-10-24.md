# Type E: three-block center/Q-frame variance certificate

**2026-10-24. [PROVED EXACTLY]** The block variance theorem, its isolated-center Type-E specialization, and the near-tight normalized-defect dichotomy. **[OPEN]** Type E elimination and improvement of 40 <= tau_5 <= 44. No D5 labeling or generic SDP.

## Setting

Twenty selected disjoint deep edges have endpoints m_i +/- z_i, a_i=||m_i||^2 <= 1/4, A=sum a_i <= B=383/504. The isolated unit center u has two-sided inner products in (-1/2,1/2], so v_i=z_i/sqrt(1-a_i) are unit vectors with q_i=(u.v_i)^2 <= 1/[4(1-a_i)].

On Sym_0(R^5), dimension 14, set Qhat_i=v_i v_i^T-I/5, Delta=sum Qhat_i, F=sum Qhat_i tensor Qhat_i, U=uu^T-I/5, mu=tr F/14=8/7, rho=<U,FU>/||U||^2, d=<Delta,U>=sum q_i-4. Put s_ij=(v_i.v_j)^2 and

    T=sum_{i<j} s_ij-30=||Delta||^2/2 >= 0,
    Eplus=sum_{i<j} s_ij(s_ij-1/4)_+,
    Lminus=sum_{i<j} s_ij(1/4-s_ij)_+.

Eplus is a *normalized* weighted defect; the six raw exceptions do not imply only six normalized exceptions.

Retain the exact capped-simplex center moment estimate

    sum q_i^2 <= (1/4)sum q_i + H(A),
    H(A)=floor(4A)/36 + r/[16(1-r)^2], r=A-floor(4A)/4.

H is increasing, H(B)=250891/2988012. It follows that

    rho <= 1/4+(5/4)H(A)-(3/16)d.                      (1)

## Exact three-block variance theorem

Fix u. Sym_0(R^5) decomposes orthogonally into span{U} (dimension 1), the mixed u-perp matrices u w^T+w u^T (dimension 4), and Sym_0(u-perp) (dimension 9). The three traces of F are

    rho,
    b=2 sum q_i(1-q_i)=32/5+(6/5)d-(8/5)rho,
    c=16-rho-b.

The mixed projection of Qhat_i has squared norm 2q_i(1-q_i). Trace Cauchy-Schwarz on each diagonal block and nonnegativity of the off-diagonal Frobenius contributions imply, for V=tr(F-mu I)^2,

    V >= (rho-mu)^2+(b-4mu)^2/4+(c-9mu)^2/9
      = (42/25)*(8/7-rho+d/3)^2+d^2/3.                (2)

This exact 1+4+9 variance bound holds for any twenty unit vectors in R^5.

## Labeling-free Type-E inequality

Set c(A)=25/28-(5/4)H(A), theta=c(A)+(25/48)d. By (1), 8/7-rho+d/3 >= theta. Also

    V=5/7-(3/10)T+2Eplus-2Lminus.

Consequently

    2Lminus+(42/25)*(theta_+)^2+d^2/3+(3/10)T
        <= 5/7+2Eplus.                                (3)

The bound |d|<=sqrt(8T/5) follows from ||U||^2=4/5 and ||Delta||^2=2T.

## Exact consequences

Let c_B=c(B)=65919115/83664336.

**[PROVED EXACTLY, T=0]** Then d=0, so

    Eplus-Lminus >= (42*c_B^2/25-5/7)/2
      = 7824330390487/47617150464768
      = 0.164317484648... .                            (4)

Thus a normalized tight frame with no normalized superthreshold correlations cannot satisfy the retained Type-E midpoint ceiling.

**[PROVED EXACTLY, T<=1/25]** Minimizing the quadratic in (3) over |d|<=sqrt(8T/5), using c(A)>=c_B, gives its minimum at d=-sqrt(8T/5) in this range: the unconstrained minimizer is -112*c_B/101, whose magnitude exceeds sqrt(8/125). With x=sqrt(T),

    2(Eplus-Lminus) >= (42/25)*(c_B-(5sqrt(10)/24)*x)^2
                         +(5/6)*x^2-5/7.

The RHS decreases on 0<=x<=1/5 (quadratic vertex 28sqrt(10)c_B/125 > 1/5). At x=1/5 this yields

    Eplus-Lminus >= 9312366342511/47617150464768
                    -13183823*sqrt(10)/239040960
                  = 0.021158425428... > 1/50.         (5)

The last strict comparison is certified by positive R,S in (value-1/50)=R-Ssqrt(10), with

    R^2-10S^2 =
      63836833008778530901655209/
      157457848498913566556200960000 > 0.

Therefore Type E must satisfy the **necessary dichotomy**

    T>1/25   OR   Eplus>Lminus+1/50.                 (6)

This is not a contradiction: no six-raw-exception theorem yet forces both alternatives to fail.

## Proof ledger

- **[PROVED EXACTLY]** (1)-(6), including the 1+4+9 block traces and exact surd certificate.
- **[RETAINED]** M(F3)<=89, M(P)>=S/2-28/3, A<=383/504; zero-midpoint exclusion via the source-audited Musin--Boyvalenkov result; six *raw* exceptional pairings.
- **[OPEN]** Bound normalized T and Eplus-Lminus from raw safe/core pairings and rank-five endpoint Gram compatibility; Type E, C, D and generic e>=27.
- **[GLOBAL]** 40<=tau_5<=44; sparse e=23,24 graph classification conditional on minimum degree >=1.

Next: insert (3) as an exact cut in the six-core rank-five Gram polynomial model, preserving normalization denominators and without identifying the six D5 kernel relations with the six core exceptions.
