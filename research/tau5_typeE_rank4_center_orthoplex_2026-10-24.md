# Quantitative rank-four center-cap theorem (Type E)

**2026-10-24. Status:** [PROVED EXACTLY] universal center-cap inequality; [PROVED EXACTLY, BALANCED-D5 CONDITIONAL] energy bound. [OPEN] Type E elimination and global D5 labeling.

## 1. Rank-four Gram lemma

For k>8 unit vectors w_i in R^4, put rho=max_{i<j} w_i·w_j. Then rho>0 and

rho(1+rho) >= (k-8)/(4(k-1)).                                              (1)

Proof. The Gram matrix G is PSD, rank at most 4, and tr(G)=k, hence tr(G^2)>=k^2/4. For -1<=x<=rho and rho>=0,

rho(1+rho)-x(1+x)=(rho-x)(1+rho+x)>=0.

Consequently tr(G^2)<=2k-||sum_i w_i||^2+k(k-1)rho(1+rho). Combining yields (1). If rho<=0, the same calculation with rho=0 gives k<=8, contradiction.

For 9<=k<=20 define

r_k=(sqrt(1+(k-8)/(k-1))-1)/2,
t_k=sqrt((1/2-r_k)/(1-r_k)),
c_k=(1/2+t_k)/2.                                                        (2)

## 2. Center-cap theorem

Let u be an isolated unit center of a five-dimensional kissing code. Take distinct selected deep edges x_i^±=m_i±z_i, with endpoints of distinct edges satisfying x_i^s·x_j^t<=1/2. Orient z_i so u·z_i>=0, and put b_i=|u·z_i|. The center constraint u·m_i+b_i<=1/2 implies for the actual endpoint y_i=m_i-z_i,

u·y_i<=1/2-2b_i.

**[PROVED EXACTLY]** For every k distinct selected edges, 9<=k<=20,

min_i b_i <= c_k.                                                        (3)

Proof. Otherwise each s_i=-u·y_i>t_k>1/2. Decompose y_i=-s_i u+h_i, with h_i in u^perp=R^4. Each h_i is nonzero: if y_i=-u, it has dot product s_j>1/2 with another y_j. Normalize w_i=h_i/||h_i||. Endpoint kissing implies

w_i·w_j <= (1/2-s_i s_j)/sqrt((1-s_i^2)(1-s_j^2)).

For s_i,s_j>1/2 the right side decreases in each variable, because its derivative in s_i has sign s_i/2-s_j<0. Thus w_i·w_j< (1/2-t_k^2)/(1-t_k^2)=r_k, contradicting (1).

Exact constants:

r_9=(3sqrt(2)-4)/8; t_9^2=(13-2sqrt(2))/21; c_9=0.597980104714...
r_10=(sqrt(11)-3)/6; t_10^2=(43-3sqrt(11))/70; c_10=0.593563913938...

Among any ten selected edges, at least two have b_i<=c_9, and at least one of those has b_i<=c_10.

## 3. Balanced D5 consequence

**[PROVED EXACTLY, CONDITIONAL ON NORMALIZED D5 DIRECTIONS AND BALANCED CENTER]** Suppose the twenty normalized z_i directions form D5 lines (e_j±e_l)/sqrt(2), and the isolated center has |u_j|=1/sqrt(5). Ten aligned lines have q_i=(u·v_i)^2=2/5, and b_i^2=(1-a_i)q_i, where a_i=||m_i||^2.

The previously established center-only bound gives a_i>=g_0=(9-6sqrt(2))/20 for each aligned line. By (3), two of them have a_i>=a_9=1-(5/2)c_9^2, and one of those two has a_i>=a_10=1-(5/2)c_10^2. Since a_10>a_9>g_0, summation gives

A=sum_i a_i >= 8g_0+a_9+a_10
             = 0.431141636396037177... .                                (4)

This is a strict improvement over the balanced-center-only 0.2573593... and the earlier uniform-D5-template 0.2580065... bound, but **not** a uniform bound for arbitrary D5 center directions or for Type E without a D5 labeling. It does not contradict A<=383/504.

## 4. Proof-status ledger

- [PROVED EXACTLY] Gram lemma (1), universal center-cap theorem (3).
- [PROVED EXACTLY, BALANCED-D5 CONDITIONAL] Energy bound (4).
- [OPEN] Arbitrary-center D5 extension, labeling-free Type E contradiction, Types C/D and generic e>=27.
- [RETAINED] 40<=tau_5<=44; Type E M(F3)<=89, M(P)>=S/2-28/3, A<=383/504.

The local symbolic checker is tau5_typeE_rank4_center_orthoplex_2026-10-24_verify.py. It checks the exact constants and algebra; the quantified proof is given above.
