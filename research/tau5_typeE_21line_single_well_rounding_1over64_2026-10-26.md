# Type E: exact 21-line quartic gap 1/64 and midpoint floor 1/99

Date: 2026-10-26. This note continues the consolidated 2026-09-05 state and uses the retained four-core Gram budget. **[PROVED EXACTLY]** Universal theorem. **[CONDITIONAL ON RETAINED TYPE-E HYPOTHESES]** Energy consequence. **[OPEN]** Type E elimination.

## Universal theorem [PROVED EXACTLY]

For any 21 unit vectors u_i in R^5, put s_ij=(u_i·u_j)^2 and P=sum_{i<j}[s_ij(s_ij-1/4)]_+. Then **P>1/64**, improving the earlier 9/625.

Proof. Set F=sum u_i u_i^T, Delta=F-(21/5)I, V=tr(Delta^2), and D_-=sum[-s_ij(s_ij-1/4)]_+. The dimension-five positive-definite polynomial f(t)=t^4-t^2/4 has normalized Gegenbauer expansion (1/28)P0+(1/3)P2+(8/21)P4, yielding D_- <= P-5V/24.

Suppose P<=1/64, hence V<=3/40. Round each s in [0,1/4] to its nearest well 0 or 1/4, and s>1/4 to 1/4. For negative quartic magnitude h=s(1/4-s), the rounding error d=min(s,1/4-s) equals g(h)=1/8-(1/2)sqrt(1/16-4h). The function g is increasing, convex and g(0)=0; therefore sum g(h_i)<=g(sum h_i) when the sum is <=1/64. Positive quartic rounding error is <=4 times its quartic defect. Thus total rounding error L satisfies L<=4P+g(D_-)<=3/16-y/2, where y=sqrt(5V/6), 0<=y<=1/4 and V=6y^2/5.

Let E be the integer number of rounded correlations equal to 1/4. Since sum_{i<j}s_ij=168/5+V/2, we have |672/5+2V-E|<=4L<=3/4-2y. Hence E=134 or E=135.

Let d_i be the rounded degree in row i and R=sum_i|d_i-64/5|/4. For every integer d>=0, |d-64/5|>=8-(3/5)d. Since sum d_i=2E, R>=42-(3/10)E. On the other hand the frame row identities give R<=sqrt(21(21/5+sqrt(V))V)+3/8-y.

If E=134, the integer inequality forces 2y+(12/5)y^2<=7/20, so y<3/20 and V<27/1000<1/36. Since sqrt(2751)<105/2, the row upper bound is strictly less than 3/8+(19/2)(3/20)=9/5, whereas its integer lower bound is 9/5. Contradiction.

If E=135, the integer inequality forces y-(6/5)y^2<=3/40. This expression increases on [0,1/4] and equals 3/40 at y=1/12, so y<=1/12 and V<=1/120<1/36. The row upper bound is strictly less than 3/8+19/24=7/6, whereas its integer lower bound is 3/2. Contradiction. Therefore P>1/64. QED.

## Type-E consequence [CONDITIONAL ON RETAINED TYPE-E HYPOTHESES]

Use 20 selected deep edges p_i^±=m_i±z_i, a_i=||m_i||^2, A=sum a_i=A_O+A_C, 16 outside and four core edges. The isolated center is non-deep to every endpoint; together with the spherical-code upper bound this gives |x_0·z_i|<=1/2. The 210 normalized-line pairings split into 184 safe edge-edge, 20 center-edge, and six core-core pairs.

Assume A<=t. Safe and center positive quartic defects sum to at most (20A_O+17A_C)/[16(1-t)^2]. For the core let delta_ij=(|z_i·z_j|-1/2)_+. Retained four-vector negative-Gram inequalities imply sum delta<=A_C and sum delta^2<=A_C^2/4. Also delta<=t/2, so each core normalized squared correlation is <=(1+t)^2/[4(1-t)], and its positive quartic defect is bounded by (1+t)^2[delta+delta^2+(a_i+a_j)/4]/[4(1-t)^2]. Summing six pairs gives

P <= K_O(t) A_O + K_C(t) A_C <= K_C(t) A,

K_O(t)=20/[16(1-t)^2], K_C(t)=[17+(1+t)^2(7+t)]/[16(1-t)^2].

At t=1/99, K_C=478267/310464 > K_O and 1/64-K_C/99=991/15367968>0. Thus A<=1/99 would imply P<1/64, contradicting the universal theorem. Therefore **A>1/99**.

## Proof status

[PROVED EXACTLY] Universal 21-line gap P>1/64 (no D5 labeling or SDP).
[CONDITIONAL] A>1/99 uses the retained graph-safe/isolated-center and four-core endpoint certificates.
[OPEN] This does not force A>383/504. Type E, C, D, generic e>=27 and non-isolated branches remain open. Global proved range remains 40<=tau_5<=44. Retain M(F3)<=89, M(P)>=S/2-28/3, and twenty-edge mass >=2137/6. The e=23,24 classification requires delta(G)>=1.
