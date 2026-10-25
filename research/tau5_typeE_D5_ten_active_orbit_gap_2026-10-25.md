# Type E: D5 ten-active-line theorem and exact 1/10 orbit gap

**Date:** 2026-10-25. **[PROVED EXACTLY]** D5 counting lemma and positive-excess moment lower bound. **[PROVED UNDER RETAINED TYPE-E HYPOTHESES]** A hypothetical isolated-center Type-E configuration is at sup-vector distance strictly greater than 1/10 from every rotated, signed, relabeled D5 20-line template. **[OPEN]** Type-E exclusion; no D5 identification or global stability theorem has been proved.

This improves the previous necessary orbit-separation radius 3/40 to 1/10. It does **not** assert proximity to D5.

## 1. D5 ten-active-line lemma [PROVED EXACTLY]

Let v_{ij}^±=(e_i±e_j)/sqrt(2), 1<=i<j<=5, be the twenty D5 projective line representatives. For every unit x in R^5,

$$
\boxed{\#\{(i,j,\pm):|x\cdot v_{ij}^\pm|>1/2\}\le10.}\tag{1}
$$

**Proof.** Order the absolute coordinates of x as s_1>=...>=s_5>=0 and put q=1/sqrt(2). The two absolute correlations for pair (i,j) are (s_i+s_j)/sqrt(2) and |s_i-s_j|/sqrt(2). If s_1<=q, no difference correlation exceeds 1/2, so at most the ten sum correlations are active.

Otherwise s_1>q. Put delta=s_1-q, and let B={j in {2,3,4,5}:s_j<delta}, k=|B|. The four sum correlations involving index 1 are active; exactly k difference correlations involving index 1 are active. Differences among indices 2,...,5 are inactive because s_j<=sqrt(1-s_1^2)<q. Sum correlations within B are inactive because 2delta<=2(1-q)<q.

For a mixed pair j in B and l not in B, an active sum correlation requires s_l>q-s_j>2q-s_1. There cannot be two such l, since

$$
1\ge s_1^2+2(2q-s_1)^2
=3(s_1-4q/3)^2+4/3>1.
$$

Thus there are at most k active mixed sums when k<=3, and no mixed pairs when k=4. The total active counts for k=0,1,2,3,4 are bounded by 10,9,9,10,8 respectively. QED.

## 2. D5 moment lower bound [PROVED EXACTLY]

For any unit x put t_i=|x.v_i|, D_v=sum_i(t_i-1/2)_+^2, q_j=x_j^2, U=sum q_j^2, W=sum q_j^3. Direct expansion yields

$$
S_2=\sum t_i^2=4,\quad S_4=3/2+U/2,\quad S_6=(15U-11W)/4.
$$

For 0<=t<=1,

$$
t^2(t^2-1/4)\le t^2(t+1/2)(t-1/2)_+,
$$

and

$$
t^4(t+1/2)^2\le(5/3)t^6+(5/8)t^4,
$$

because the second difference is (2/3)t^4(t-3/4)^2. Cauchy--Schwarz and W>=U^2 give

$$
D_v\ge\frac{(S_4-S_2/4)^2}{(5/3)S_6+(5/8)S_4}
\ge\frac{(1+U)^2}{(15+105U)/4-(55/3)U^2}>\frac{27}{160}.\tag{2}
$$

The last strict comparison follows from

$$
160(1+U)^2-27((15+105U)/4-(55/3)U^2)
=(5/4)(524U^2-311U+47)>0,
$$

whose quadratic has positive leading coefficient and discriminant -1791.

## 3. Type-E orbit separation [PROVED UNDER RETAINED TYPE-E HYPOTHESES]

For the twenty distinguished deep edges write p_i^±=m_i±z_i, a_i=||m_i||^2 in [0,1/4), A=sum a_i<=383/504, and u_i=z_i/sqrt(1-a_i). If x_0 is the isolated deep-graph vertex, both spherical-code and non-deep conditions imply -1/2<=x_0.p_i^±<=1/2, whence

$$
|x_0.m_i|+|x_0.z_i|\le1/2,\qquad
|x_0.u_i|\le1/(2\sqrt{1-a_i}).
$$

Fix any common rotation R, matching to the twenty D5 lines, and signs sigma_i. Let epsilon=max_i||u_i-sigma_i Rv_i|| and t_i=|x_0.Rv_i|. Convexity gives the chord bound

$$
t_i\le1/(2\sqrt{1-a_i})+\epsilon
\le1/2+C a_i+\epsilon,\qquad C=4/\sqrt3-2.
$$

By (1), the set J={i:t_i>1/2} has at most ten members. Using a_i^2<=a_i/4, we obtain

$$
D_v=\sum_{i\in J}(t_i-1/2)^2
\le10\epsilon^2+2CA\epsilon+C^2A/4.\tag{3}
$$

Suppose epsilon<=1/10. Since A<=383/504<19/25 and C<31/100 (equivalent to 3*231^2-400^2=83>0),

$$
D_v<10(1/10)^2+2(31/100)(19/25)(1/10)
 +(31/100)^2(19/25)/4
 =165379/1000000
 <27/160.
$$

This contradicts (2). Therefore, for every rotation, relabeling and choice of line signs,

$$
\boxed{\epsilon>1/10.}\tag{4}
$$

Compactness of O(5) and finiteness of matchings/signs ensure the minimizing epsilon is also strictly greater than 1/10.

## 4. Status

**[PROVED]** D5 ten-active-line lemma and orbit-separation inequality (4), conditional only on the retained isolated-center Type-E midpoint model and A<=383/504. **[OPEN]** A converse D5-proximity theorem or direct endpoint-Gram contradiction. No six-core/Q-kernel identification is claimed. Type C, Type D, generic e>=27, and non-isolated branches remain open. Global proved range unchanged: 40<=tau_5<=44. Retain M(F3)<=89 and matching M(P)>=S/2-28/3; e=23/e=24 sparse classification is conditional on delta(G)>=1.
