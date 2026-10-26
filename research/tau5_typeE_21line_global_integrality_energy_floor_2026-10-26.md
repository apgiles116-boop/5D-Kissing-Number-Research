# Type E: integer-pair quartic gap and a new midpoint-energy floor
2026-10-26. Full expanded working note and exact checker are available in the accompanying research artifacts.

**[PROVED EXACTLY]** For any 21 unit vectors in R^5, let s_ij=(u_i·u_j)^2 and f(s)=s(s-1/4). Put P=sum_{i<j} max(f(s_ij),0), N=sum_{i<j} max(-f(s_ij),0), F=sum_i u_i u_i^T, V=||F-(21/5)I||_F^2. The degree-0/2/4 Gegenbauer expansion of t^4-t^2/4 yields
P-N=(5/24)V+(4/315)sum_{i,j}C_4^(3/2)(u_i·u_j).
Positive definiteness implies N<=P and 0<=V<=(24/5)P.

Round each s_ij to r_ij=0 if s_ij<=1/8, and r_ij=1/4 otherwise. Direct scalar inequalities give |s-r|<=8(-f(s)) for s<=1/4 and |s-r|<=4f(s) for s>1/4 (strict for positive f). Hence sum_{i<j}|s_ij-r_ij|<=8N+4P<=12P.

Let E be the integer number of r_ij=1/4. The frame trace identity gives sum_{i<j}s_ij=168/5+V/2. Therefore
|672/5+2V-E|<=48P.
If P<=1/120 then V<=1/25, so 672/5+2V belongs to [134.4,134.48], whose distance from any integer is >=2/5. Thus P>=1/120. Equality would require V=0, E=134, and equality in the rounding bound, impossible because P>0 entails a strictly bounded positive term. Consequently
**P>1/120**, improving the prior P>1/440. No D5 labeling or generic SDP is used.

**[CONDITIONAL ON RETAINED TYPE-E HYPOTHESES]** Normalize the twenty selected projected vectors u_i=z_i/sqrt(1-a_i), a_i=||m_i||^2, and add the isolated center u_0=x_0. The 210 pairs comprise 184 safe pairs, 20 center pairs, and six potentially exceptional core pairs. Suppose A=sum a_i<=t=1/200, and write u=a_i+a_j<=t, v=sqrt(a_i a_j)<=u/2, w=(1-a_i)(1-a_j)>=(1-t)^2.

For safe pairs, |z_i·z_j|<=1/2 implies f(s_ij)_+<=(1-w)/(16w^2)<=k_s u with k_s=1/[16(1-t)^4].
For center pairs, |x_0·z_i|<=1/2 gives f(s_0i)_+<=k_0 a_i with k_0=1/[16(1-t)^2].
For core pairs, upper endpoint constraints imply |z_i·z_j|<=1/2+v. Hence s_ij<=(1+t)^2/[4(1-t)^2] and (s_ij-1/4)_+ <= [v+u/4+(3/4)v^2]/w <= (3u/4)(1+t/4)/(1-t)^2. Thus f(s_ij)_+<=k_c u, k_c=3(1+t)^2(1+t/4)/[16(1-t)^4].

Counting safe pair incidences (19 for each outside index, 16 for each core index), three exceptional pairs per core index, and one center pair per index gives
P <= (19k_s+k_0)A_O+(16k_s+k_0+3k_c)A_C <= K A,
where K=16k_s+k_0+3k_c=20873290225/12545913608.
But
1/120-K/200=21939473/1505509632960>0,
contradicting P>1/120. Therefore **A>1/200**.

**[OPEN]** This does not eliminate Type E: A<=383/504 remains possible. Type C, Type D, generic e>=27 and non-isolated branches remain open. Retain M(F3)<=89, matching mass >=S/2-28/3, and global 40<=tau_5<=44. The next task is a coupled six-core defect/mixing and Q-frame polynomial certificate.
