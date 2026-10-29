# Type E: capped-energy L1 rigidity and stronger outside-16 spectral gap (2026-10-29)

**[PROVED EXACTLY — standalone algebra/4D polynomial]**; Type-E use **[CONDITIONAL ON RETAINED GRAPH, ENERGY, AND SAFE-PAIR INPUTS]**. Global proved range remains 40<=tau_5<=44.

## Capped-frame second-order stability

For 20 deep-edge pairs, put a_i=||m_i||^2 in [0,1/4], A=sum a_i<=B=383/504, U=sum a_i^2, z_i=(u_i^+-u_i^-)/2, V=||sum z_i z_i^T-(20-A)I/5||_F^2, and Q=sum_{i<j}(z_i.z_j)^2. The exact identity is

    Q=30-3A+A^2/10-U/2+V/2.

Sort a decreasingly, and let b(A) be the capped filling vector with k=floor(4A) entries 1/4, one residual r=A-k/4, and remaining entries zero. Define g(A)=k/16+r^2 and delta=sum_i |a_(i)-b_i(A)|.

**[NEW, PROVED]** Capped majorization implies

    g(A)-U >= sum_i (a_(i)-b_i(A))^2 >= delta^2/20.      (1)

Indeed d_i=b_i-a_(i) has nonnegative prefix sums and total zero. Abel summation gives sum_i a_(i)d_i=sum_{j<20}(a_(j)-a_(j+1))sum_{i<=j}d_i>=0. Hence g-U=sum d_i^2+2sum a_(i)d_i>=sum d_i^2, followed by Cauchy.

The previously established exact cap-floor derivative gives f(A)=30-3A+A^2/10-g(A)/2 >= L+(57/20)(B-A), with L=8790283/317520. Thus

    **Q >= L+(57/20)(B-A)+delta^2/40+V/2.**            (2)

If Q-L<=eps, then B-A<=20eps/57, delta<=sqrt(40eps), V<=2eps. The fixed cap pattern b(B)=(1/4,1/4,1/4,5/504,0^16) satisfies ||a_sorted-b(B)||_1<=sqrt(40eps)+20eps/57. Strict deep edges forbid exact cap saturation but not necessarily an approximating sequence.

For the Type-E 16+4 split, let x be total isolated midpoint energy. Separate capped convexity yields

    U<=g(x)+g(A-x),
    Q>=30-3A+A^2/10-[g(x)+g(A-x)]/2+V/2.             (3)

For 3/4<=A<=B and 0<=x<=A-3/4, write r_A=A-3/4. Then (3) simplifies to the exact extra mass-split penalty

    **Q>=f(A)+x(r_A-x)+V/2.**                           (4)

At A=B this adds x(5/504-x), which vanishes at the strip endpoints; no Type-E exclusion follows. This is weaker than some separately retained *conditional center-sensitive* Q floors.

## Outside-16 spectral improvement

Suppose 16 vectors z_i in R^5 obey ||z_i||^2=1-a_i, 0<=a_i<=1/4, sum a_i<=B=383/504, and |z_i.z_j|<=1/2 for i!=j. Put S=sum z_i z_i^T.

**[NEW, PROVED UNDER STATED HYPOTHESES]**

    **lambda_min(S)>9/160=0.05625.**                    (5)

This strengthens the prior >1/18 certificate. Suppose instead a unit eigenvector w gives lambda=sum_i(w.z_i)^2<=L0=9/160. Let s_i=(w.z_i)^2, project to w-perp=R^4, and normalize the projected vectors to unit u_i. Setting

    c_i=1-(1-a_i-s_i)/(1+s_i)^2

gives |u_i.u_j|<=1/[2sqrt((1-c_i)(1-c_j))]. The exact identity

    [a+(3-2a)s-(7/2)s^2-c(a,s)](1+s)^2
       =s^2[(3/2-3a)-(4+2a)s-(7/2)s^2]

has a nonnegative right side for 0<=a<=1/4 and 0<=s<=L0: its bracket is >=24873/51200>0. Hence c_i<=a_i+(3-2a_i)s_i-(7/2)s_i^2.

For any subset of k<=3 indices, its c sum is at most p_k=k/4+(5/2)L0-(7/2)L0^2/k. For k>=4 the bound is p_4=B+3L0-(7/32)L0^2. These follow from sum s_i<=L0 and Cauchy, with the bounding quadratics increasing on [0,L0]. Thus c is weakly majorized by the decreasing vector

    v=(19433/51200,26167/102400,25789/102400,
       2118311/51609600,0^12).

For 16 unit vectors in R^4, f(t)=t^4-t^2/4=(1+6P2(t)+5P4(t))/16, with normalized positive-definite Gegenbauer kernels P2=(4t^2-1)/3 and P4=(16t^4-12t^2+1)/5, yields sum_{i!=j} f(u_i.u_j)>=4. Since f(t)<=f(C) whenever |t|<=C and C>=1/2, the projection bound yields

    sum_{i!=j} f(u_i.u_j)<=F(c),
    F(c)=(1/8)sum_{i<j}[(1-c_i)^(-2)(1-c_j)^(-2)
                         -(1-c_i)^(-1)(1-c_j)^(-1)].

F is symmetric, coordinatewise increasing, and Schur-convex on [0,1)^16. For g(a,b)=x(a)^2x(b)^2-x(a)x(b), x(t)=(1-t)^(-1), g_aa>0 and g_a(a,b)-g_b(a,b)=xy(x-y)(2xy-1)>=0 when a>=b; the remaining terms inherit derivative ordering. Weak majorization therefore gives F(c)<=F(v), but exact rational evaluation yields

    4-F(v)=3740587247549191288613004487326972299372
           /3122586346512138747653771770355267994729243 >0,

a contradiction. This proves (5).

**[CONDITIONAL TYPE-E WALSH CONSEQUENCE]** Retain the endpoint inequality |m_i.z_j|<=h_ij=1/2-|z_i.z_j| on the 120 isolated-isolated and 64 isolated-core safe blocks. With A_O=x and A_C=A-x, the spectral gap implies

    **H_184=sum_safe h_ij^2 > (9/160)A_C+(9/320)A_O
          =(9/320)(A+A_C)>=(9/320)A**                 (6)

for A>0, improving the old (A+A_C)/36 coefficient. The 184-block classification and upstream mass/harmonic certificates are not re-proved here.

**[OPEN]** No uniform Type-E contradiction or higher global bound. Type C, Type D, generic e>=27, and non-isolated branches remain open. Sparse e=23/24 classification is conditional on delta(G)>=1. Global proved range remains 40<=tau_5<=44.
