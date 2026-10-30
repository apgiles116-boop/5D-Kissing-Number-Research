# Type E: strengthened exact D5 support-plane energy obstruction (2026-10-30)

**[PROVED BY EXACT FINITE CERTIFICATE — CONDITIONAL ON EXACT SUPPORT-PLANE GEOMETRY]** If the twenty normalized Type-E projected directions form orthonormal pairs in the ten coordinate two-planes of a common orthonormal basis, with the four F3 core directions assigned to four star supports, then
[
oxed{A=sum_{i=1}^{20}|m_i|^2ge 243/280=0.867857142857ldots.}
]
The retained Type-E cap (Ale383/504) contradicts this by **exactly (34/315)**. This strengthens the prior conditional exact-fibre bound (143/175). It does **not** exclude arbitrary Type E.

## Exact safe-block improvement

Write (a_i=|m_i|^2in[0,1/4]), (z_i=sqrt{1-a_i}u_i), and (t_ein[0,1]) for the within-support squared-coordinate imbalance. Among the 30 meeting-support pairs of (K_5), discard six star-star pairs potentially contaminated by exceptional core pairings. The remaining 24 are fully safe; their degrees are 3 at four star supports and 6 at six nonstar supports.

For each fully safe meeting-support pair (e,f), choose the two lines maximizing their normalized squared contact, which is ((1+t_e)(1+t_f)/4). Their raw safety implies
[
(1+t_e)(1+t_f)le[(1-a_i)(1-a_j)]^{-1}.
]
Since (0le a,ble1/4),
[
(1-a)^{-1}le1+4a/3,quad able(a+b)/8,quad
[(1-a)(1-b)]^{-1}le1+(14/9)(a+b).
]
Thus (t_e+t_fle(14/9)(a_i+a_j)). Summing over the 24 fully safe support pairs, counting each selected line at most six times, yields
[
oxed{T_C+2T_Nle(28/9)A.}	ag{1}
]
Every support has a safe meeting neighbour, so (t_ele7/9).

## New exact center certificate

Let (p_i=(vcdot e_i)^2), ordered (p_1gecdotsge p_5ge0), with (sum p_i=1). The isolated center gives (|vcdot z_i|le1/2), hence (|vcdot u_i|^2le1/3). Orthonormality in each support implies (p_1+p_2le2/3).

The two squared center contacts in support ({i,j}), together with (sqrt{1-t^2}ge1-t/2) for (tle7/9<4/5), yield
[
t_{ij}gerac{[(sqrt{p_i}+sqrt{p_j})^2-2/3]_+}
{p_i-p_j+sqrt{p_ip_j}}.
]
Zero denominators contribute zero. Define (F(p)) as the sum over all ten supports. A new exhaustive exact-integer/rational interval certificate proves
[
oxed{F(p)ge27/10}
]
on the entire ordered simplex with (p_1+p_2le2/3).

The certificate partitions the ordered simplex, the convex hull of ((1/k,ldots,1/k,0,ldots,0)) for (k=1,ldots,5), by longest-edge bisection. For coordinate bounds (l_ile Dp_ile h_i), each summand is bounded below by
[
rac{[3(l_i+l_j+2lfloorsqrt{l_il_j}floor)-2D]_+}
{3(h_i-l_j+lceilsqrt{h_ih_j}ceil)}.
]
All certification decisions use exact integer square roots and rational comparisons. **Verified execution:** 407,557 simplices visited; 32,997 domain prunings; 170,782 function-bound prunings; maximum depth 36; zero unresolved cells.

Therefore (T_C+2T_Nge T_C+T_Nge F(p)ge27/10). Equation (1) gives
[
Age(9/28)(27/10)=243/280,qquad
243/280-383/504=34/315>0.
]

## Petersen variance coefficient is sharp

**[PROVED EXACTLY — ALGEBRAIC SHARPNESS]** The earlier weighted-Q identity
[
E:=V+12C=8O+4D+(8/5)|P_ca|^2+4|P_perp a|^2
]
implies (sum_i(a_i-A/20)^2le(5/8)E). This coefficient is sharp even if one imposes only (0le a_ile1/4) and (Ale383/504).

Use D5 root lines (r_{pq}^{pm}=(e_ppm e_q)/sqrt2). Let the (K_5) four-cycle weights be (c_{12}=c_{34}=1), (c_{23}=c_{14}=-1), other (c_{pq}=0), and set
[
a_{pq}^{pm}=3/100+c_{pq}/100,quad
z_{pq}^{pm}=sqrt{1-a_{pq}^{pm}},r_{pq}^{pm}.
]
Then (A=3/5), all (a_iin{1/50,3/100,1/25}), and exact rational arithmetic gives
[
sum_i(a_i-A/20)^2=1/1250,quad V=0,quad C=1/9375,quad E=4/3125,
]
hence equality in the (5/8) inequality. **This is not claimed to satisfy isolated-center or Type-E Walsh constraints.** Improving the variance constant requires those additional constraints, not just scalar midpoint caps.

## Proof status and next step

**[OPEN]** No inverse-stability estimate forces arbitrary Type E into the exact fibre. The existing (1/360) forbidden-neighbourhood certificate and weighted-Q residual lower bound are unchanged. The six exceptional core pairings are not identified with the six Q-kernel modes. Continue seeking a second-order bound from the 114 safe meeting-support pairings and the six exceptions.

Retain (M(F_3)le89), (M(P)ge S/2-28/3), twenty-edge mass (ge2137/6), (Ale383/504), the Musin/Boyvalenkov zero-midpoint boundary exclusion, and **global proved (40le	au_5le44)**. Types C, D, generic (ege27), and non-isolated branches remain open; sparse (e=23,24) classification requires (delta(G)ge1).

Verifier: `research/tau5_typeE_exact_fibre_243over280_verify.py`.