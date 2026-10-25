# Type E: exact Schur-convex fourth-moment bound and outside-16 spectral gap

**2026-10-25. [PROVED EXACTLY UNDER RETAINED TYPE-E INPUTS]** Let the sixteen outside-core selected deep edges have projected vectors z_i in R^5, a_i=||m_i||^2 in [0,1/4], b_i=||z_i||^2=1-a_i, A_O=sum a_i <=383/504, and |z_i.z_j|<=1/2 for i≠j. Define Z_O=sum_i z_i z_i^T.

**Theorem.** lambda_min(Z_O)>1/31. This strengthens the previous 1/500 gap without a D5 labeling or SDP.

## Four-dimensional LP and capped-simplex sharpening

For f(t)=t^4-t^2/4 on S^3, f=(1+6P2+5P4)/16, with P2=(4t^2-1)/3, P4=(16t^4-12t^2+1)/5. Positive definiteness of the Gegenbauer kernels gives sum_{i≠j}f(u_i.u_j)>=4 for any sixteen unit vectors u_i in R^4.

Normalize v_i=z_i/sqrt(b_i). Since |z_i.z_j|<=1/2, direct evaluation of f yields

sum_{i≠j} f(v_i.v_j) <= F(a):=(1/8)sum_{i<j}[(1-a_i)^(-2)(1-a_j)^(-2)-(1-a_i)^(-1)(1-a_j)^(-1)].

**Capped-simplex lemma [PROVED EXACTLY].** F is increasing and Schur-convex on [0,1/4]^16. Put x_i=(1-a_i)^(-1)>=1 and g(a,b)=x^2y^2-xy. Then g_a=2x^3y^2-x^2y>0 and g_aa=2x^3y(3xy-1)>0. For a_i>=a_j, the derivative difference from their mutual pair is x_i*x_j*(x_i-x_j)*(2*x_i*x_j-1)>=0, and contributions from all other indices are nonnegative by g_aa>0. Thus (a_i-a_j)(F_i-F_j)>=0. Majorization at total energy B=383/504 gives the maximum at a*=(1/4,1/4,1/4,5/504,0,...,0). Exact evaluation:

F(a)<=18211220/6723027,  4-F(a*)=8680888/6723027>0.

As a separate stronger rank-four obstruction, if sum a_i<=1 then F(a)<=F(1/4,1/4,1/4,1/4,0,...,0)=100/27<4. Hence any rank-four sixteen-line configuration with the stated raw correlation restriction requires A_O>1 (incompatible with Type E).

## Spectral gap [PROVED EXACTLY]

Assume lambda=lambda_min(Z_O)<=1/31. Choose a unit eigenvector w; put t_i=w.z_i, s_i=t_i^2, sum s_i=lambda, y_i=z_i-t_i*w, beta_i=||y_i||^2=b_i-s_i, and u_i=y_i/sqrt(beta_i) in w-perp=R^4. Then beta_i>=c=89/124. Elementary bounds on (xy)^(-1/2) and |t_i*t_j|<=(s_i+s_j)/2 give

|u_i.u_j-v_i.v_j| <= K(s_i+s_j), K=1/(2c)+1/(4c^2)=9362/7921.

Moreover |v_i.v_j|<=2/3 and |u_i.u_j|<=(1/2+lambda/2)/c<=q=64/89. For f'(t)=4t^3-t/2, its maximum absolute value on [-q,q] is D=4q^3-q/2=795104/704969. The mean-value theorem and sum_{i≠j}(s_i+s_j)=30lambda yield

4 <= sum_{i≠j} f(u_i.u_j) <= 18211220/6723027 + 30*K*D/31.

But exact rational subtraction gives

4 - 18211220/6723027 - (30/31)*(9362/7921)*(795104/704969)
= 44313384250232/37541782445232123 > 0,

a contradiction. Thus Z_O is strictly greater than I_5/31.

## Safe-slack consequence

Let M=sum over all twenty selected edges of m_i*m_i^T and A=tr(M)>0 (zero midpoint boundary already excluded). For the 184 outside-core zero-contact pairings, h_ij=1/2-|z_i.z_j|. The retained zero-contact endpoint theorem implies |m_i.z_j|<=h_ij. With H_OO and H_OC the sums of h_ij^2 over outside/outside and outside/core pairs,

A/31 < tr(M Z_O) <= 2H_OO+H_OC,

so H_184=H_OO+H_OC>A/62. This improves the previous A/1000 corollary. The matrix inequality Z_O ≻ I_5/31 is the principal new constraint for a four-core rank-five polynomial certificate.

**[RETAINED, NOT REPROVED]** M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, six core exceptional pairings, zero-midpoint Musin–Boyvalenkov exclusion.

**[OPEN]** Type E, Types C/D, generic e>=27, non-isolated branches, and any improved global bound. The e=23/e=24 classification is conditional on delta(G)>=1. Global proved range: 40<=tau_5<=44.

Verifier: research/tau5_typeE_outside16_schur_spectral_gap_2026-10-25_verify.py
