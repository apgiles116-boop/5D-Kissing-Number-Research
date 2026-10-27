# Type E: isolated-center obstruction to exact D5 normalized directions

2026-10-27. Companion: `tau5_typeE_isolated_center_D5_covering_obstruction_2026-10-27_verify.py`.

**[PROVED EXACTLY — isolated-center deep-edge hypotheses]** The 20 normalized directions of selected deep edges in an isolated-center 41-code cannot equal the 20 projective D5 root lines, even after an orthogonal transformation, permutation and independent sign changes.

**[PROVED EXACTLY — quantitative]** For every such alignment, at least one normalized direction has projective angular distance at least

`theta = arccos(sqrt(2/15)+sqrt(2/5)) = 0.0692394943... radians = 3.96713... degrees`

from its D5 counterpart. The corresponding projective chord-distance lower bound is `sqrt(2-2(sqrt(2/15)+sqrt(2/5))) = 0.0692256642...`.

## Exact proof

For the D5 projective lines `d_pq^±=(e_p±e_q)/sqrt(2)`, any unit `x in R^5` satisfies

`max_{p<q,±}|x·d_pq^±|=(b_1+b_2)/sqrt(2)>=sqrt(2/5)`,

where `b_1>=...>=b_5>=0` are the absolute coordinates of `x`. Indeed, with `t=b_1+b_2`, `b=b_2 in [0,t/2]`,

`1=sum b_j^2 <= (t-b)^2+4b^2 <= 5t^2/4`.

The last quadratic is convex and its maximum on the interval occurs at an endpoint. Equality is attained by `x=(1,1,1,1,1)/sqrt(5)`, so the D5 covering constant is sharp.

For each selected deep edge, write its unit endpoints `p_i^±=m_i±z_i`, `a_i=||m_i||^2=(1+p_i^+·p_i^-)/2<=1/4` and `||z_i||^2=1-a_i>=3/4`. The isolated center `x_0` is non-deep with both endpoints. Kissing constraints give `-1/2<=x_0·p_i^±<=1/2`; subtraction yields `|x_0·z_i|<=1/2`. Thus for `u_i=z_i/sqrt(1-a_i)`,

`|x_0·u_i|<=1/(2sqrt(1-a_i))<=1/sqrt(3)`.

If the `u_i` were the D5 lines, their covering bound would force some `|x_0·u_i|>=sqrt(2/5)>1/sqrt(3)`. Equivalently, the selected edge would require `a_i>=1-1/[4(2/5)]=3/8>1/4`. Contradiction.

For quantitative separation, fix any rotated/relabelled D5 template `d_i`. The covering property supplies `i` with `|x_0·d_i|>=c=sqrt(2/5)`, whereas `|x_0·u_i|<=b=1/sqrt(3)`. The projective spherical triangle inequality implies

`angle_proj(d_i,u_i)>=arccos(b)-arccos(c)`.

The cosine of this difference equals `sqrt(2/15)+sqrt(2/5)`, proving the claimed angular and chord gaps. These conclusions hold after optimizing the common rotation, labels and line signs.

## Interpretation and status

The prior exact-D5-template mixing/energy theorem is a correct **conditional algebraic statement**, but its exact-D5 premise is impossible for an isolated-center Type E configuration. Do **not** present its `A>=0.165...` consequence as an actual Type-E lower bound. A new proof could instead show that the six-exception/frame constraints force the normalized lines into a D5 neighborhood of angular radius less than `theta`, contradicting the center obstruction; no such stability theorem is currently available. The global squared-correlation floor by itself does not establish proximity to D5.

**[OPEN]** Type E, C, D, generic e>=27 and non-isolated branches remain unresolved. Retain exact Type-E mass bounds `M(F3)<=89`, `M(P)>=S/2-28/3`, twenty-edge mass `>=2137/6`, `A<=383/504` and the separately established label-free `A>1/49`. The sparse e=23,24 classification is conditional on minimum degree at least one. Global proved range remains `40<=tau_5<=44`.
