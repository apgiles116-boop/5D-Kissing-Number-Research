# Type E: exact 3D/4D leakage from sixteen isolated safe lines (2026-11-01)

**[PROVED EXACTLY — conditional on the retained Type-E safe-pair and midpoint-cap hypotheses.]** Not a Type-E exclusion. Global established range **40 <= tau_5 <= 44**.

## Theorem

Let the sixteen isolated K2 selected edges have endpoints x_i^±=m_i±z_i, with a_i=||m_i||²<=1/4, ||z_i||²=1-a_i and A_I=sum a_i<=383/504. Every isolated-isolated pairing is safe, so the two-sided Walsh inequality gives |z_i·z_j|+|m_i·m_j|<=1/2. In particular |z_i·z_j|<=1/2.

For **every** three-plane W in R5,

    sum_i ||P_(W^perp) z_i||² > 7/10.                              (T3)

For **every** four-plane W in R5,

    sum_i ||P_(W^perp) z_i||² > 1/25.                             (T4)

No D5 labeling, rank-13 hypothesis, core coplanarity or later October 28 mass refinements are required. This strengthens the older three-plane leakage >3/20 and extends the four-plane positive-ray bound to the full midpoint cap.

## Exact weighted harmonic proof

For either W, d=dim W=3 or 4, put w_i=P_W z_i, ell_i=||P_(W^perp)z_i||², b_i=a_i+ell_i, r_i=||w_i||²=1-b_i, L=sum ell_i, B=sum b_i=A_I+L. Then 0<=b_i<=1 and |w_i·w_j|<=1/2+s_ij with s_ij=sqrt(ell_i ell_j).

The degree-four polynomial f(t)=t⁴-t²/4 has positive harmonic expansions:

    dimension 3: f=(7/60)P0+(17/42)P2+(8/35)P4;
    dimension 4: f=(1/16)U0+(1/8)U2+(1/16)U4,

where Pk are Legendre and Uk are Chebyshev-second-kind kernels. Set alpha_3=7/60, alpha_4=1/16 and F_ij=(w_i·w_j)^4-r_i*r_j*(w_i·w_j)²/4. Apply positive definiteness with weights r_i² to the normalized directions (zero r_i are harmless). The diagonal is 3r_i^4/4, giving

    sum_(i<j) F_ij >= alpha_d/2*(sum r_i²)² -3/8*sum r_i⁴.

We have sum r_i²>=16-2B+B²/16. Convex mass concentration on 0<=b_i<=1 gives sum r_i⁴<=M(B), where M(B)=15+(1-B)^4 for B<=1 and M(B)=14+(2-B)^4 for 1<=B<=2. Thus

    sum_(i<j) F_ij >= H_d(B)
       :=alpha_d/2*(16-2B+B²/16)²-3M(B)/8.                   (1)

For each pair let s=s_ij and h=1/2+s. Since |w_i·w_j|<=h and h²>=r_i*r_j/4, the convex quadratic x(x-r_i*r_j/4), x=(w_i·w_j)², is at most h²(h²-r_i*r_j/4). Using r_i*r_j>=(1-b_i-b_j),

    F_ij <= (1/4+s+s²)*((b_i+b_j)/4+s+s²)
          = (b_i+b_j)/16+(b_i+b_j)s/4+(b_i+b_j)s²/4
            +s/4+5s²/4+2s³+s⁴.

Summing over sixteen indices uses

    sum_(i<j)(b_i+b_j)=15B,
    sum_(i<j)s_ij<=15L/2, sum_(i<j)s_ij²<=15L²/32,
    s_ij<=L/2, b_i+b_j<=1/2+L.

It follows that

    sum_(i<j)F_ij <= U(B,L)
      :=15B/16 +15(1/2+L)L/8+15(1/2+L)L²/128
        +15L/8+75L²/128+15L³/32+15L⁴/128.                  (2)

Every feasible realization must satisfy H_d(B)<=U(B,L). U is increasing in B,L. On the two pieces of M, differentiation gives

    H_d'(B)=alpha_d*(16-2B+B²/16)*(-2+B/8)
             +(3/2)*(k+1-B)^3, k=floor B.

For d=4, assuming L<=1/25 implies B<=10079/12600<4/5 and H_4'(B)<=-21/100. Therefore

    H_4(10079/12600)-U(10079/12600,1/25)
     =4974138029636009089/206477210419200000000 >0.

For d=3, assuming L<=7/10 implies B<=3679/2520<3/2 and H_3'(B)<=-1199/960. Therefore

    H_3(3679/2520)-U(3679/2520,7/10)
     =125849511944131207/1238863262515200000 >0.

Both contradict (1)-(2), proving (T3)-(T4) exactly.

## Conditional rank-13/two-ray corollary

**[PROVED EXACTLY — conditional additionally on the previously specified rank-13, two-ray and four genuinely ambiguous coplanar core-completion hypotheses.]** Let p,q be the two missing-plane axes, X=sum_i(p·z_i)², Y=sum_i(q·z_i)². Applying (T4) to p^perp and q^perp, and (T3) to (span{p,q})^perp, gives X,Y>1/25, X+Y>7/10 and hence

    XY>33/1250.

The retained double-angle core wedge gap W_C>=81/2048 and the two-ray Cauchy-Binet factorization for the safe 16-by-4 squared-correlation matrix D_ic=(z_i·z_c)² give

    sum_(i<j,c<d) (D_ic D_jd-D_id D_jc)²
       >=(81/131072)X²Y²
       >88209/204800000000.

All 64 isolated-core pairings are safe, so D_ic<=1/4, ||D||_F²<=4 (sharper than the earlier coarse 81/4). Since rank(D)=2, Cauchy-Binet gives

    sigma_2(D)>297*sqrt(2)/1280000 =0.000328141740644...

This closes the previously missing absolute XY gap in the **conditional** two-ray branch. It is not an exclusion of Type E.

## Ledger

**[VERIFIED LOCALLY]** The accompanying SymPy/Fraction verifier checks the positive harmonic expansions, pairwise polynomial identity, monotonicity bounds, exact rational contradiction margins, two-ray constants and a 16-line D5 example. These checks supplement the analytic proof.

**[OPEN]** A signed-F3-incidence-sensitive *upper* bound on safe minors or sigma_2(D) is still needed to exploit the new lower certificate. General Type E, Types C/D, generic e>=27 and non-isolated graph branches remain open. Sparse e=23/24 graph classification requires delta(G)>=1. Retain M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, raw/homogeneous defect ceilings, and the Musin/Boyvalenkov 21-line zero-midpoint theorem. Stronger separately conditional October 28 scalar/Q bounds are not superseded. **Global 40<=tau_5<=44 unchanged.**