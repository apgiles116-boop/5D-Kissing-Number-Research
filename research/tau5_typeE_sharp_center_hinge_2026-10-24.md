# Type E: sharp one-edge center hinge and stronger labeling-free Q inequality

**Date:** 2026-10-24. **[PROVED EXACTLY]** Optimal single-edge quartic coefficient, exact equality witness, and Q-frame corollary. **[OPEN]** Type E elimination and all remaining 41-code branches. Global proved range remains 40 <= tau_5 <= 44.

## 1. Sharp center/edge geometry

Let u be a unit isolated center, x^±=m±z unit endpoints of a selected **deep** edge, a=||m||²<=1/4, b=|u·z|, m·z=0, ||z||²=1-a, and u·x^±<=1/2. Since endpoint center projections lie in [-1,1/2], b<=3/4.

**Theorem 1 [PROVED EXACTLY].** For 0<=a<=1/4,

    b <= (1-a+sqrt(3a(1-a)))/2.                        (1)

For 1/2<b<=3/4, the sharp lower envelope is

    a >= f(b) = (5/4-b-sqrt(9/16+3b/2-3b²))/2.        (2)

**Proof.** Orient z with u·z=b. When b>1/2, u·m<=1/2-b. Cauchy-Schwarz in z-perp yields

    (b-1/2)² <= a(1-b²/(1-a)).

Rearranging gives F(a,b)=a²-(5/4-b)a+(b-1/2)²<=0. The larger root in b is (1), and the smaller root in a is (2). If b<=1/2, (1) is automatic for a<=1/4. The bound is attained by a two-dimensional construction described below.

## 2. Optimal quartic hinge coefficient

**Theorem 2 [PROVED EXACTLY; SHARP].** Set

    C_sharp=(297-108sqrt(6))/25=1.2982043111766706...

Then every selected deep edge satisfies

    a >= C_sharp ((b²-1/4)_+)².                        (3)

This improves the earlier valid but nonoptimal C_old=512/(207+33sqrt(33))=1.291069086240374... . The improvement is about 0.55% in the coefficient.

**Exact optimization.** Minimize R(b)=f(b)/(b²-1/4)² on 1/2<b<=3/4. The limit at 1/2 is 4/3 and the value at 3/4 is 64/25. Writing a=f(b), implicit differentiation of F(a,b)=0 shows that a stationary point must satisfy

    a(-3b²+5b-1/4)+(b-1/2)²(1-6b)=0.                 (4)

Substitution into F=0 factors as

    3b(2b-1)^3(36b²-12b-5)
    -------------------------- = 0.                   (5)
    2(12b²-20b+1)²

The only interior stationary point is b_*=(1+sqrt(6))/6, where a_*=5/12-sqrt(6)/6. The endpoint values and uniqueness imply the global minimum R(b_*)=(297-108sqrt(6))/25.

**Sharpness witness.** In R² let u=e1, c=sqrt(1-a_*-b_*²), t=b_*-1/2, z=b_*e1+ce2, and m=-te1+(tb_*/c)e2. Then ||m||²=a_*, ||z||²=1-a_*, m·z=0, u·(m+z)=1/2, and u·(m-z)=1/2-2b_*<=1/2. The endpoints are unit and their mutual inner product 2a_*-1<-1/2, so the edge is deep and (3) is attained. No stronger universal coefficient follows from the one-edge center hypotheses.

## 3. Labeling-free Type-E Q consequence

**[PROVED EXACTLY, CONDITIONAL ON THE RETAINED TYPE-E SETUP].** For twenty disjoint deep edges let A=sum_i a_i, t_i=(u·z_i)², Q_i=z_i z_i^T-(1-a_i)I/5, and U=uu^T-I/5. The elementary polynomial minorant

    (t-1/4)_+² >= (39/64)t²-(3/16)t                 (6)

holds for t>=0: below 1/4 the right side is nonpositive; above 1/4 the difference is (5t-2)²/64. Also sum_i t_i=4-A/5+<sum_i Q_i,U>. Thus (3) implies

    (1-3C_sharp/80)A
       >= C_sharp[(39/64)sum_i t_i²
                    -3/4-(3/16)<sum_i Q_i,U>].        (7)

Here t_i=(1-a_i)/5+<Q_i,U>. Equation (7) is an exact labeling-free fourth-moment condition and strictly strengthens the prior center/Q hinge coefficient. Single-edge sharpness does not mean all twenty edges can attain equality simultaneously.

## Status

- **[PROVED EXACTLY]** (1)-(7) and the two-dimensional equality witness.
- **[RETAINED CONDITIONAL TYPE E]** M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, and the six exceptional pairings.
- **[OPEN]** A sufficient labeling-free fourth-moment lower bound to force A>383/504; D5 labeling; Type E elimination; Types C, D and generic e>=27.
- **[GLOBAL PROVED RANGE]** 40<=tau_5<=44.
