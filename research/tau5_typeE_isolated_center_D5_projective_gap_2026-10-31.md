# Type E: sharp D5 covering energy and isolated-center projector separation (2026-10-31)

**Proof ledger.** [PROVED EXACTLY] The D5 covering-energy theorem below is unconditional. [PROVED EXACTLY, isolated-center hypothesis] The two projective/Q separation inequalities below hold for any 20 disjoint deep edges in a 41-code whose remaining vertex is isolated in the deep graph. [CONDITIONAL TYPE E] The numerical E2 bound uses the retained Type-E cap A<=383/504. [OPEN] Type E is not eliminated; global proved range remains 40<=tau_5<=44.

## Sharp D5 covering-energy theorem

Let R be the 20 projective roots r_ij^±=(e_i±e_j)/sqrt(2), 1<=i<j<=5. For every unit v in R^5 and 0<=b<=2/5,

    sum_{r in R} ((v.r)^2-b)_+^2 >= 10*(2/5-b)^2.                (1)

Equality holds at v=(±1,±1,±1,±1,±1)/sqrt(5). Thus the D5 projective covering radius is sqrt(2/5), and at b=1/4 the sharp squared positive-part energy is 9/40.

Proof: Put t_ij^±=(v_i±v_j)^2/2. Direct expansion yields sum t=4 and sum t²=3/2+(1/2)sum v_i^4>=8/5. Define

    q_b(t)=(1-25b²/4)t²-2b(1-5b/2)t.

For 0<=t<=b<=2/5, q_b(t)<=0. For t>=b, (t-b)²-q_b(t)=(25b²/4)(t-2/5)²>=0. Hence q_b(t)<=(t-b)_+² everywhere. Summation yields sum(t-b)_+²>=10(2/5-b)². For equal-magnitude coordinates, ten t-values are 2/5 and ten are zero, establishing equality. Also max_r (v.r)^2>=2/5 by sum t²<=max(t)sum t.

## Isolated-center quantitative separation

Let the 20 disjoint deep edges be m_i±z_i, with a_i=||m_i||²<=1/4, w_i=||z_i||²=1-a_i, u_i=z_i/sqrt(w_i). The isolated center v has inner product strictly greater than -1/2 and at most 1/2 with *both* endpoints. Consequently |v.z_i|<=1/2-|v.m_i|<=1/2. In particular t_i'=(v.u_i)^2<=1/[4(1-a_i)]<=1/4+a_i/3. **Both lower and upper center-endpoint contacts are needed.**

Choose ANY bijection of these 20 normalized projected lines to the 20 D5 lines and ANY common orthogonal rotation. Let P_i=u_i u_i^T, P_i^0=r_i r_i^T, e_i²=||P_i-P_i^0||_F², E2=sum e_i², U=sum a_i². Rank-one projector geometry gives |v^T(P_i-P_i^0)v|<=e_i/sqrt(2). Therefore

    ((v.r_i)^2-1/4)_+ <= e_i/sqrt(2)+a_i/3.

Apply (1) with b=1/4, then the triangle inequality in R^20:

    sqrt(E2/2)+sqrt(U)/3 >= sqrt(9/40),                     (2)
    E2 >= 2*(sqrt(9/40)-sqrt(U)/3)^2.                        (3)

The bracket is positive because U<=20/16=5/4. Under the retained Type-E A=sum a_i<=383/504, capped-simplex convexity gives U<=3/16+(383/504-3/4)^2=47653/254016. Thus

    E2 >= 2810177/5715360 - sqrt(476530)/2520
       = 0.21775539315855... > 217/1000.                  (4)

This holds for *every* labeling and rotation; it does not assume D5 proximity.

## Rank-free weighted-Q gap

Define Q_i=z_i z_i^T-(1-a_i)I/5 and Q_i^0=r_i r_i^T-I/5. The exact identity

    ||Q_i-Q_i^0||_F²=(1-a_i)e_i²+(4/5)a_i²

and 1-a_i>=3/4 yield, by (3),

    sum ||Q_i-Q_i^0||_F²
      >= (3/2)*(sqrt(9/40)-sqrt(U)/3)^2+(4/5)U
       = 81/290+(29/30)*(sqrt(U)-(15/29)*sqrt(9/40))²
      >= 81/290.                                           (5)

Equation (5) does **not** use the Type-E total midpoint cap. The rational constant is not claimed sharp.

**Next target:** Combine this compulsory D5 Q-distance with an upper bound from the *same-labeling* 184 safe Walsh blocks and the four rank-free local Q residuals. Do not infer a bijection between six exceptional F3 pairings and six D5 kernel modes. Type E, C, D, generic e>=27 and non-isolated branches remain open. Preserve M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, the Musin/Boyvalenkov zero-midpoint exclusion, and the delta(G)>=1 condition for sparse e=23/24 classification.
