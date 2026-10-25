# Isolated-center Type E: exact D5 covering exclusion and quantitative orbit gap

**Date:** 2026-10-25. **Proof status:** [PROVED EXACTLY] isolated-center coherence, D5 covering radius, and quantitative D5-orbit separation under the retained Type-E hypotheses. [CONDITIONAL] Exact D5 directions themselves are excluded; their identification with Type E has NOT been proved. [OPEN] Type E exclusion and all remaining branches.

## 1. Two-sided isolated-center constraint [PROVED EXACTLY]

Let x be the isolated deep-graph vertex in a hypothetical 41-code, and let the twenty selected deep edges have endpoints p_i^± = m_i ± z_i, both unit. Isolation means every x·p_i^± ≥ -1/2; the spherical code condition gives x·p_i^± ≤ 1/2. Hence

$$
|x\cdot m_i|+|x\cdot z_i|\le\tfrac12.
$$

Put a_i=||m_i||² and u_i=z_i/sqrt(1-a_i). Unit endpoints imply m_i·z_i=0, ||z_i||²=1-a_i; the deep-edge condition gives 0≤a_i<1/4. Therefore

$$
\boxed{|x\cdot u_i|\le \frac1{2\sqrt{1-a_i}}<\frac1{\sqrt3}.}\tag{1}
$$

This is stronger than the one-sided center leakage bound and uses no D5 labeling.

## 2. Exact D5 projective covering radius [PROVED EXACTLY]

For the twenty D5 unit line representatives v_{ij}^±=(e_i±e_j)/sqrt(2), and any unit x, let s_1≥s_2≥...≥s_5≥0 be the ordered absolute coordinates of x. Then

$$
\max_{i<j,\pm}|x\cdot v_{ij}^\pm|=(s_1+s_2)/\sqrt2.
$$

Indeed, 1=Σs_j²≤s_1²+4s_2²≤(5/4)(s_1+s_2)², where the final inequality follows from (s_1-s_2)(s_1+11s_2)≥0. Equality occurs at uniform absolute coordinates. Thus

$$
\boxed{\min_{||x||=1}\max_{i<j,\pm}|x\cdot v_{ij}^\pm|=\sqrt{2/5}.}\tag{2}
$$

**[CONDITIONAL D5-TEMPLATE EXCLUSION]** If the normalized u_i were exactly the D5 lines, some i would have |x·u_i|≥sqrt(2/5)>1/sqrt(3), contradicting (1). Equivalently, this i would require a_i≥3/8, contradicting a_i<1/4. This does NOT eliminate Type E without a D5 identification theorem.

## 3. Unconditional separation from the D5 orbit [PROVED UNDER RETAINED TYPE-E MODEL]

For any common R∈O(5), matching of the twenty lines, and independent signs, let

$$
\epsilon=\max_i||u_i-\sigma_i Rv_{\pi(i)}||.
$$

By (2), max_i|x·u_i|≥sqrt(2/5)-ε. By (1), max_i|x·u_i|<1/sqrt(3). Therefore every such alignment satisfies

$$
\boxed{\epsilon>\sqrt{2/5}-1/\sqrt3\approx0.05510526284405.}\tag{3}
$$

This is a necessary condition for the isolated-center branch, not an assumption of proximity.

## 4. Energy-budget sharpening: epsilon > 3/40 [PROVED EXACTLY UNDER RETAINED TYPE-E ENERGY CAP]

Assume the retained Type-E bound A=Σa_i≤383/504. Let C=4/sqrt(3)-2. Convexity of f(a)=1/(2sqrt(1-a)) on [0,1/4] places f below its endpoint chord: f(a)≤1/2+Ca. With t_i=|x·Rv_{\pi(i)}|, (1) and the alignment bound give (t_i-1/2)_+≤ε+Ca_i. Since a_i²≤a_i/4,

$$
D_v:=\sum_i(t_i-\tfrac12)_+^2
\le20\epsilon^2+2CA\epsilon+\frac{C^2A}{4}.\tag{4}
$$

**Exact D5 moment certificate.** Put q_j=x_j², U=Σq_j², W=Σq_j³, and S_k=Σ_i t_i^k. Direct expansion yields S_2=4, S_4=3/2+U/2, S_6=(15U-11W)/4. For d=(t-1/2)_+,

$$
t^4-\tfrac14t^2\le t^2(t+\tfrac12)d,\qquad
(t+\tfrac12)^2\le\tfrac53t^2+\tfrac58
$$

(the second difference equals (2/3)(t-3/4)²). Cauchy--Schwarz and W≥U² imply

$$
D_v\ge\frac{(S_4-S_2/4)^2}{(5/3)S_6+(5/8)S_4}
\ge\frac{(1+U)^2}{(15+105U)/4-(55/3)U^2}
>\frac{27}{160}.\tag{5}
$$

The final strict inequality follows from

$$
160(1+U)^2-27\left((15+105U)/4-55U^2/3\right)
=\tfrac54(524U^2-311U+47)>0,
$$

since the quadratic discriminant is -1791.

If ε≤3/40, the right side of (4) is bounded above by its value at ε=3/40, A=383/504, namely

$$
3133/1890-6511\sqrt3/7560<27/160.
$$

The last comparison is exact: it reduces to sqrt(3)>45025/26044, and 3-(45025/26044)²=7619183/678289936>0. This contradicts (5). Hence

$$
\boxed{\epsilon>3/40=0.075.}\tag{6}
$$

This stronger forbidden neighborhood uses the total midpoint budget but NO D5 identification assumption.

## 5. Proof-status ledger

- **[PROVED EXACTLY]** Equations (1)–(3), isolated-center/D5 covering and basic orbit separation.
- **[PROVED UNDER RETAINED TYPE-E BUDGET]** Equations (4)–(6), the strengthened orbit separation ε>3/40.
- **[CONDITIONAL]** Exact D5 projected directions cannot occur; we have not shown actual Type-E directions are D5 or sufficiently close.
- **[OPEN]** Exclude Type E; exploit the five local Q-cycle relations if a D5-type labeling can be justified; establish a second-order quantitative rigidity inequality; resolve Types C, D, generic e≥27, and non-isolated branches.
- **[UNCHANGED]** 40≤τ_5≤44; M(F3)≤89, M(P)≥S/2-28/3, A≤383/504. Sparse e=23/24 classification remains conditional on δ(G)≥1. Musin/Boyvalenkov 21-line zero-midpoint exclusion retained.

**Next:** Incorporate the absolute center cap into the finite endpoint Gram/KKT formulation. Seek a stability certificate forcing normalized projected directions within 3/40 of a D5 orbit, or a direct contradiction avoiding D5 labeling.