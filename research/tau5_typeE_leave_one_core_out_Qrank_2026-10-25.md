# Type E: leave-one-core-out signed Q-rank stability (2026-10-25)

**[PROVED EXACTLY — universal R5 theorem]** Signed 19-vector Q-rank obstruction.
**[PROVED UNDER RETAINED TYPE-E INPUTS]** Stronger 184-safe/six-core slack tradeoff.
**[OPEN]** Type E elimination; global bound remains 40 <= tau_5 <= 44.

## Universal signed 19-vector theorem

For any 19 vectors z_i in R5 with b_i=||z_i||^2 in [3/4,1], define E_ii=0 and E_ij=1/4-(z_i.z_j)^2 for i!=j. There is **no pairwise-safety assumption**. Then

    sum_{i<j} E_ij^2 >= 2375/7168.                      (1)

Proof: Q_i=z_i z_i^T-(b_i/5)I lies in the 14-dimensional traceless symmetric space. Its Gram K has rank <=14. Set K0=diag(b_i^2-1/4)+(1/4)11^T-(1/5)bb^T, so E=K0-K, tr E=0. With t_i=b_i-3/4, S=sum x_i, T=sum t_i x_i, D=sum [(3/2)t_i+t_i^2]x_i^2, exact expansion gives

    x^T(K0-5I/16)x = D+(11/80)(S-12T/11)^2-(4/11)T^2.

Weighted Cauchy gives T^2 <= (19/7)D, hence K0 >=5I/16 with an explicit SOS remainder D/77+(11/80)(S-12T/11)^2. Since dim ker K>=5, the top five eigenvalues of E are >=5/16. Its other 14 eigenvalues sum to at most -25/16, so

    tr E^2 >= [5+25/14](5/16)^2;
    sum_{i<j}E_ij^2=tr E^2/2 >=2375/7168.

Signed E_ij are allowed; this is crucial for exceptional core pairs.

## Four 19-vector Type-E subsets

Take O=16 outside-core selected deep edges and C=4 F3-core selected matching edges. The 184 O-O and O-C pairings are raw-safe: r_ij=|z_i.z_j|<=1/2. Put H_OO=sum_OO(1/2-r)^2, H_OC=sum_OC(1/2-r)^2, H_184=H_OO+H_OC. On the six core pairs, let H_C^- be squared slack summed over r<=1/2, and T_C^+ be sum (d+d^2)^2 over d=r-1/2>0.

Apply (1) to O plus each of the four triples from C. Each O-O pair occurs four times, each O-C pair three times, each C-C pair twice. On safe pairs E_ij^2=(1/2-r)^2(1/2+r)^2 <= (1/2-r)^2. Thus

    H_OO+(3/4)H_OC+(1/2)H_C^-+(1/2)T_C^+
       >=2375/7168.                                   (2)

In particular,

    H_184+(1/2)H_C^- >=2375/7168-(1/2)T_C^+ +(1/4)H_OC.

## Exact rational core-defect bound

Use the source-supported exact Type-E budget sum_C d^2 <819/10000 from research/tau5_typeE_lifted_triangle_defect_budget_2026-10-24.md, with 0<=d<=1/4. The function f(u)=u+2u^(3/2)+u^2 is increasing and convex. Capped concentration of sum u<819/10000, u<=1/16 gives one u=1/16 and one u=97/5000. Since sqrt(97/5000)<7/50,

    T_C^+ <25/256+97/5000+(97/5000)^2
                 +2*(97/5000)*(7/50)
          =12286461/100000000.                         (3)

Combining (2)-(3) gives the exact strict Type-E tradeoff

    H_OO+(3/4)H_OC+(1/2)H_C^-
       >755723921/2800000000 =0.269901400357142857...

and therefore

    H_184+(1/2)H_C^-
       >755723921/2800000000 +(1/4)H_OC.              (4)

This strengthens the earlier joint H_184+H_C^->0.259617... inequality, but does **not** give H_184>0.2699 without controlling safe core slack. In the six-positive-core-defect branch H_C^-=0, (4) does give the stronger uniform H_184 bound. The stronger square-defect budget <19/250 mentioned in another note was not independently re-audited, so this result uses the documented <819/10000 certificate instead.

**Status:** universal theorem and subset counting proved exactly; Type-E corollary conditional on retained midpoint/endpoint and six-defect hypotheses. No D5 labeling, Type-E contradiction, or global improvement. Type C, D, generic e>=27, non-isolated branches open; e=23/24 classification assumes delta(G)>=1. Retain M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, 40<=tau_5<=44.
