# Type E: shifted-Huber 21-line gap and stronger energy floor A>1/89

Date: 2026-10-26. This note supersedes the same-day P>1/72 and A>1/90 result. Continues the consolidated 2026-09-05 tau_5 proof ledger.

**[PROVED EXACTLY — UNIVERSAL]** For any 21 unit vectors u_0,...,u_20 in R^5, with s_ij=(u_i.u_j)^2,

    P=sum_{i<j}[s_ij(s_ij-1/4)]_+ > 1/71.             (U)

**[PROVED EXACTLY, CONDITIONAL ON RETAINED TYPE-E ENDPOINT/SIX-CORE CERTIFICATES]**

    A=sum_{i=1}^{20}||m_i||^2 > 1/89.                  (E)

This strengthens the retained A>1/99 and the same-day A>1/90. No Type-E exclusion or change to 40<=tau_5<=44 is claimed.

## I. Universal frame and rounded-degree identities

Let F=sum_i u_i u_i^T, H=F-(21/5)I, V=tr(H^2), E=sum_{s_ij<=1/4}s_ij(1/4-s_ij). The positive dimension-five degree-four spherical harmonic P4(t)=(21t^4-14t^2+1)/8 and frame trace give

    P-E>=(5/24)V,   V<=(24/5)P.                         (1)

Round s_ij to b_ij/4 with b_ij=1 for s_ij>=1/8, else 0. Define K=sum_{i<j}b_ij, k_i=sum_{j!=i}b_ij, e_i=u_i^T H u_i, c_i=k_i/4-16/5, d_i=e_i-c_i, L=sum_i|d_i|. Pairwise rounding gives

    L<=16E+8P<=24P-(10/3)V,                            (2)
    sum_i d_i=V+336/5-K/2.                             (3)

For Q_i=u_i u_i^T-I/5, the PSD Gram matrix tr(Q_i Q_j) has maximum eigenvalue <=24/5+4P by Gershgorin: diagonal 4/5, twenty off-diagonals each bounded by 1/5+(s_ij-1/4)_+, with sum of positive raw differences <=4P. Therefore the frame-analysis inequality is

    sum_i e_i^2<=(24/5+4P)V.                            (4)

Assume P<=1/71. Then V<=24/355 and L<=24/71-(10/3)V. Equation (3) excludes K<=133 (residual >=7/10) and K>=136 (residual >=4/5-24/355). For K=134, (3) gives V<=147/4615; for K=135 it gives V<=81/4970.

## II. Two exact shifted-Huber certificates

For lambda>0 and eta real, define

    g_{lambda,eta}(c)=min_t {t^2-eta*t+lambda*|t-c|}.

This is convex in c (infimal convolution of convex functions). For each i,

    e_i^2+lambda*|d_i|-eta*e_i >=g(c_i).

Since sum_i e_i=V, it follows that

    sum_i e_i^2>=sum_i g(c_i)-lambda*L+eta*V.           (5)

For integer degrees k_i with sum k_i=2K, convexity shows that sum_i g(k_i/4-16/5) is minimized by balancing k_i at floor(2K/21) and ceil(2K/21).

**K=134:** Choose lambda=3/10, eta=0. Then g(c(12))=3/80 and g(c(13))=1/400, so sum g>=5(3/80)+16(1/400)=91/400. Equations (2),(4),(5) imply

    91/400-(36/5)(1/71)+V<=(24/5+4/71)V,
    V>=3581/109520>147/4615,

contradiction, with exact margin 17075/20217392>0.

**K=135:** Choose lambda=1/5, eta=-1/10. Then g(c(12))=7/400, g(c(13))=3/400, and sum g>=3(7/400)+18(3/400)=3/16. Equations (2),(4),(5) imply

    3/16-(24/5)(1/71)+(17/30)V<=(24/5+4/71)V,
    V>=2043/73096>81/4970,

contradiction, with exact margin 2116467/181643560>0. This proves P>1/71 without a D5 labeling or generic SDP.

## III. Type-E contact-degree-sensitive quartic upper bound

Include the isolated center y_0=x_0 and twenty projected vectors y_i=z_i. Put a_0=0, a_i=||m_i||^2, r_i=1-a_i, r_0=1, A=sum a_i, u_i=y_i/sqrt(r_i), t_ij=(y_i.y_j)^2, q_ij=r_i*r_j, s_ij=t_ij/q_ij. The retained Type-E endpoint split gives t_ij<=1/4 for all 204 safe pairs (184 edge-edge and 20 center-edge); only six pairs among four core indices may exceed 1/4.

Let A_C=sum_core a_i, delta_ij=(sqrt(t_ij)-1/2)_+ on the six core pairs. Retained exact certificates give sum delta<=A_C, sum delta^2<=A_C^2/4, max delta<=A_C/2, implying

    E4=sum_core[t_ij(t_ij-1/4)]_+
      <=A_C/4+5A_C^2/16+A_C^3/4+A_C^4/16.             (6)

Since q_ij>=(1-A)^2, 1-q_ij<=a_i+a_j and t_ij<=1/4+delta_ij+delta_ij^2,

    [s_ij(s_ij-1/4)]_+
      <=(1-A)^(-4) {[t_ij(t_ij-1/4)]_+
          +(a_i+a_j)/16
          +(delta_ij+delta_ij^2)(a_i+a_j)/4}.          (7)

The left side can be positive only on rounded contacts b_ij=1 (s_ij>=1/8). The last correction occurs only among the six core pairs, each core index occurring three times; it sums to <=3A_C^2/8+3A_C^3/16. Thus, with k_i the normalized rounded degrees,

    P <= [ (sum_{i=1}^{20} k_i*a_i)/16
          +A_C/4+(11/16)A_C^2+(7/16)A_C^3+A_C^4/16
         ]/(1-A)^4.                                    (8)

This pays the linear energy cost only for actual rounded contacts.

## IV. Exact contradiction if A<=1/89

Suppose A<=1/89. First use k_i<=20 and A_C<=A in (8):

    P<=P0(A)=(24A+11A^2+7A^3+A^4)/(16(1-A)^4)
     <=P0(1/89)=17007011/959512576.                 (9)

The traceless-symmetric 5-by-5 operator inequality gives |e_i|<=sqrt(4V/5), while |d_i|<=L. From (1),(2),(9),

    |c_i|<=sqrt(96 P0(1/89)/25)+24P0(1/89)<4/5.    (10)

The strict comparison follows by exact arithmetic from 4/5-24P0>0 and

    (4/5-24P0)^2-96P0/25
      =1039618626526225/14385380992221184>0.

But k_i>=16 implies c_i=k_i/4-16/5>=4/5, impossible. Hence every k_i<=15. Returning to (8),

    P<=P15(A)=(19A+11A^2+7A^3+A^4)/(16(1-A)^4)
     <=P15(1/89)=6741083/479756288.                 (11)

Finally,

    1/71-P15(1/89)=1139395/34062696448>0,         (12)

contradicting the universal P>1/71. The scalar bounds P0(A), P15(A) are increasing on [0,1/89]. Therefore A>1/89.

## V. Status

**[PROVED EXACTLY — UNIVERSAL]** P>1/71 for any 21 unit vectors in R^5.

**[PROVED EXACTLY, CONDITIONAL TYPE E]** A>1/89, assuming the retained 204-safe/6-core endpoint partition and four-core delta certificates. Retain the matching-dependent core floors separately: all-singleton C>=17/250, doubled-contact C>9/1000. No one-to-one identification of the six exceptional pairings with D5 Q-kernel relations is made.

**[OPEN]** Type E remains compatible with 1/89<A<=383/504. Type C C7 global/boundary, Type D, generic e>=27 and non-isolated branches remain open. Preserve star sum<=70/3, M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass>=2137/6, and sparse e=23,24 classification conditional on delta(G)>=1. Global proved range remains 40<=tau_5<=44.
