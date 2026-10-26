# Type E: improved universal 21-line quartic gap and midpoint-energy floor

Date: 2026-10-26. Continuation of the 2026-09-05 consolidated tau_5 ledger.

**[PROVED EXACTLY — UNIVERSAL]** For any 21 unit vectors u_0,...,u_20 in R^5, with s_ij=(u_i.u_j)^2,

    P=sum_{i<j} [s_ij(s_ij-1/4)]_+ > 1/72.                (U)

This improves the prior P>1/80 theorem.

**[PROVED EXACTLY, CONDITIONAL ON RETAINED TYPE-E ENDPOINT AND SIX-CORE CERTIFICATES]** For Type E, the total midpoint energy satisfies

    A=sum_{i=1}^{20} ||m_i||^2 > 1/90.                     (E)

This strengthens A>1/99. Type E is not eliminated. Global proved range remains 40<=tau_5<=44.

## I. Exact universal Huber proof

Let F=sum_i u_i u_i^T, H=F-(21/5)I_5, V=tr(H^2), and E=sum_{s_ij<=1/4} s_ij(1/4-s_ij). Frame trace and the positive dimension-five degree-four harmonic kernel P4(t)=(21t^4-14t^2+1)/8 imply

    sum_{i<j}s_ij=168/5+V/2,
    P-E>=(5/24)V,  V<=(24/5)P.                            (1)

Round s_ij to b_ij/4 with b_ij=1 for s_ij>=1/8, else 0. Set K=sum b_ij, k_i=sum_{j!=i}b_ij, e_i=u_i^T H u_i, c_i=k_i/4-16/5, d_i=e_i-c_i, and L=sum_i |d_i|. Pairwise rounding yields

    L<=16E+8P<=24P-(10/3)V,                              (2)
    sum_i d_i=V+336/5-K/2.                                (3)

For Q_i=u_i u_i^T-I/5, the PSD Gram matrix (tr(Q_i Q_j)) has largest eigenvalue <=24/5+4P by Gershgorin: its diagonal is 4/5, and the twenty off-diagonals in any row are bounded by 1/5 plus (s_ij-1/4)_+, whose total is <=4P. The frame-analysis operator then gives

    sum_i e_i^2<=(24/5+4P)V.                               (4)

Suppose P<=1/72. Then V<=1/15, L<=1/3-(10/3)V. Equation (3) excludes K<=133 (residual >=7/10) and K>=136 (residual >=4/5-1/15=11/15). For K=134, (3) implies V<=2/65. For K=135 it implies V<=1/70.

For lambda=3/10, the exact Huber envelope is

    g(c)=min_t [t^2+lambda|t-c|]
        =c^2 if |c|<=3/20, else (3/10)|c|-9/400.

Therefore e_i^2+(3/10)|d_i|>=g(c_i). The function k -> g(k/4-16/5) is convex; for fixed sum k_i=2K its sum is minimized by balancing the integer degrees. Since g(c(12))=3/80 and g(c(13))=1/400:

    K=134: sum_i g(c_i)>=5(3/80)+16(1/400)=91/400.
    K=135: sum_i g(c_i)>=3(3/80)+18(1/400)=63/400.

Using (2) and (4) gives, respectively,

    K=134: 51/400+V<=sum_i e_i^2<=(437/90)V,
           V>=459/13880>2/65, contradiction.

    K=135: 23/400+V<=sum_i e_i^2<=(437/90)V,
           V>=207/13880>1/70, contradiction.

All comparisons are rational: 459*65=29835>27760 and 207*70=14490>13880. Hence P>1/72, with no D5 labeling, uniqueness assumption or generic SDP.

## II. Contact-degree-sensitive Type-E bound

Include the isolated center y_0=x_0 and twenty projected vectors y_i=z_i. Put a_0=0, a_i=||m_i||^2, r_i=1-a_i, r_0=1, A=sum a_i, and u_i=y_i/sqrt(r_i). Define t_ij=(y_i.y_j)^2, q_ij=r_i r_j, s_ij=t_ij/q_ij. The retained Type-E endpoint structure says t_ij<=1/4 for 204 safe pairs (184 edge-edge and 20 center-edge), and only six pairs among four core indices may exceed 1/4.

Let A_C be the sum of the four core energies and delta_ij=(sqrt(t_ij)-1/2)_+ on the six core pairs. Retained exact core certificates give sum delta<=A_C, sum delta^2<=A_C^2/4, and max delta<=A_C/2. Consequently

    E4=sum_core [t_ij(t_ij-1/4)]_+
      <=p(A_C)=A_C/4+5A_C^2/16+A_C^3/4+A_C^4/16.         (5)

For any pair, since q_ij>=(1-A)^2 and 1-q_ij<=a_i+a_j,

    [s_ij(s_ij-1/4)]_+
      <=(1-A)^(-4) { [t_ij(t_ij-1/4)]_+
            +(a_i+a_j)/16
            +(delta_ij+delta_ij^2)(a_i+a_j)/4 }.          (6)

For safe pairs delta=0. Only normalized pairs with s_ij>1/4 contribute P; these are among the rounded contacts b_ij=1 (s_ij>=1/8). The raw excess and the last correction occur only in the six core pairs. Since each core index belongs to three such pairs, the last correction sums to at most 3A_C^2/8+3A_C^3/16.

Writing k_i for the rounded contact degrees of the normalized 21-line configuration, we obtain the exact Type-E necessary bound

    P <= [ (sum_{i=1}^{20} k_i a_i)/16
          + A_C/4+(11/16)A_C^2+(7/16)A_C^3+A_C^4/16
         ]/(1-A)^4.                                      (7)

The key gain is that the linear energy cost is paid only for actual integer contact degrees, not all possible pairs.

## III. Exact exclusion of A<=1/90

Assume A<=1/90. Initially use k_i<=20 and A_C<=A in (7):

    P<=P0(A):=(24A+11A^2+7A^3+A^4)/[16(1-A)^4]
     <=P0(1/90)=17585731/1003875856.                   (8)

For the traceless 5-by-5 H, |e_i|<=sqrt(4V/5), while |d_i|<=L. Thus

    |c_i|<=sqrt(96 P0(1/90)/25)+24P0(1/90)<4/5.         (9)

The final strict comparison is exact: 4/5-24P0>0 and

    (4/5-24P0)^2-96P0/25
      =6047104267847453/78731776114041620>0.

If k_i>=16, then c_i=k_i/4-16/5>=4/5, contradicting (9). Hence every k_i<=15. Returning to (7),

    P<=P15(A):=(19A+11A^2+7A^3+A^4)/[16(1-A)^4]
     <=P15(1/90)=13940731/1003875856.                  (10)

But

    1/72-P15(1/90)=17903/9034882704>0,                (11)

contradicting the universal theorem P>1/72. The scalar functions in (8),(10) are increasing on [0,1/90]. Therefore A>1/90.

## IV. Status

**[NEW, CONDITIONAL TYPE E]** 1/90<A<=383/504. Retain the separate matching-dependent core floors: all-singleton C>=17/250 and doubled-contact C>9/1000. No identification of six core exceptions with the six D5 Q-kernel relations is assumed.

**[OPEN]** Type E; Type C C7 global/boundary; Type D; generic e>=27; non-isolated branches. Preserve exact star sum<=70/3, M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass>=2137/6. Sparse e=23,24 classification requires delta(G)>=1. Global proved range 40<=tau_5<=44.
