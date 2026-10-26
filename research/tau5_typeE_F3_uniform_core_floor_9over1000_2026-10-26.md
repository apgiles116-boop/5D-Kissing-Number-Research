# Type E: uniform exact F3 matching-core floor 9/1000 (2026-10-26)

**[PROVED EXACTLY]** The doubled-contact matching inequalities below, using a rational 8x8 positive-definite Gram witness. **[CONDITIONAL TYPE E]** Application to the mass-selected four-edge core. **[OPEN]** Type E elimination and tau_5.

F3 has edges 02,04,05,14,17,23,27,36,56,57. Its perfect matchings are P1={02,14,36,57}, P2={04,17,23,56}, P3={05,14,27,36}. For eight unit endpoints p_0,...,p_7 with all distinct inner products <=1/2 and the ten F3 deep inner products <=-1/2, define

C_P = sum_{uv in P} ||(p_u+p_v)/2||^2 = 2+(1/2)sum_{uv in P} p_u.p_v.

**Theorem [PROVED EXACTLY].** C_P1>9/1000 and C_P3>9/1000. Together with the independently certified C_P2>=17/250, every matching has C_P>9/1000. This improves the earlier doubled-branch bound 2-sqrt(49951)/112 ~=0.00448925.

**Proof.** Let B be symmetric 8x8, indexed 0,...,7, with entries:
- diagonal B_uu=1120425 for u in {0,2,5,7}; B_uu=1043125 for u in {1,3,4,6};
- B_uv=1000000 on P1={02,14,36,57};
- B_uv=133900 on the other deep edges {04,17,23,56};
- B_uv=111500 on the other deep edges {05,27};
- B_uv=34200 on the **nonedges** {13,46};
- all other off-diagonal entries zero.

Its exact characteristic polynomial is

(lambda^2-4309250lambda+4618504390625)
(lambda^2-2017850lambda+445625)^2
(lambda^2-309250lambda+4390625).

Because B is real symmetric, all roots are real. Every quadratic factor has positive root sum and product, hence both roots are strictly positive. Thus Q=B/1000000 is positive definite.

Let G be the endpoint Gram matrix (PSD, diagonal ones). The six unmatched deep constraints bound their contributions to tr(QG) above by minus their positive weights, and the two safe nonedges 13 and 46 use G_13,G_46<=1/2. Therefore

0<tr(QG)<= (8654200-758600+68400)/1000000 + 2sum_{uv in P1}G_uv
             =1991/250 + 2sum_{uv in P1}G_uv.

It follows that sum_{uv in P1}G_uv > -1991/500 and C_P1 > 9/1000. The F3 automorphism (2 5)(3 6) maps P1 to P3, giving C_P3>9/1000. QED.

The extra nonedge constraints 13 and 46 are essential to this particular witness. The lower bound is an exact rational certificate, not a claim of optimality. A numerical dual search suggesting ~0.009014 is **[HEURISTIC ONLY]**.

**[CONDITIONAL TYPE E]** For the mass-selected F3 matching, C_P>9/1000, and if P2 is selected the stronger C_P>=17/250 applies. Do not transfer C_P or total energy A between different matchings. The retained total energy interval remains 1/99<A<=383/504, and the retained mass statements remain M(F3)<=89, M(P)>=S/2-28/3, and total 20-edge mass>=2137/6.

**[OPEN]** This does not exclude Type E, C, D, generic e>=27, or the non-isolated branches. Global proved range remains 40<=tau_5<=44. Sparse e=23/e=24 classification still assumes minimum deep-graph degree >=1.
