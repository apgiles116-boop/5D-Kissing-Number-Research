# Type E: exact cross-matching quadratic stability

**2026-10-24.** **[PROVED EXACTLY]** Four-vector theorem below. **[CONDITIONAL TYPE E]** Its application using the retained midpoint-energy cap. **[OPEN]** Global Type-E exclusion.

For four selected deep edges, write endpoint vectors as m_i +/- z_i, a_i=||m_i||^2, C=sum_{i=1}^4 a_i, and delta_ij=(|z_i.z_j|-1/2)_+. The endpoint inequalities imply delta_ij <= (-m_i.m_j)_+.

Assume **p=delta_12>0 and q=delta_34>0**. Set
t_12=a_1+a_2-2p, t_34=a_3+a_4-2q, t=C-2(p+q).
Then ||m_1+m_2||^2<=t_12, ||m_3+m_4||^2<=t_34.

**Theorem 1 [PROVED EXACTLY].** With
s_1=delta_13+delta_24, s_2=delta_14+delta_23, w=min(s_1,s_2),

    (p+q)^2 + w^2 <= C^2/4.                      (1)

Equivalently w^2 <= t(p+q)+t^2/4. At t=0 all positive cross defects lie in at most one of the two cross matchings.

**Proof.** Put x=m_1+m_2, a=m_1-m_2, y=m_3+m_4, b=m_3-m_4; X=x.y, U=x.b, V=a.y, W=a.b. Then

    4m_1.m_3=X+U+V+W; 4m_2.m_4=X-U-V+W;
    4m_1.m_4=X-U+V-W; 4m_2.m_3=X+U-V-W.

If W>=0, s_1<=(|X+U+V|+|X-U-V|)/4
= max(|X|,|U+V|)/2.
If W<=0, s_2<=max(|X|,|V-U|)/2.
Because m_3.m_4<=-q, ||b||>=||y||. In either case,
w<=(||x||||b||+||a||||y||)/2.
Cauchy and parallelogram give
4w^2<=r(2C-r), r=||x||^2+||y||^2<=t<=C.
The right side increases for r<=C, so
4w^2<=t(2C-t)=C^2-4(p+q)^2. QED.

**Theorem 2 [PROVED EXACTLY, using a_i<=1/4].**
When delta_13,delta_14>0, endpoint geometry gives
delta_13+delta_14<=-m_1.(m_3+m_4)<=sqrt(a_1 t_34),
so t_34>=4(delta_13+delta_14)^2.
Analogous inequalities hold for each cross-defect pair sharing a vertex. Even when a cross defect is zero, the following polynomial consequences remain valid (then the product vanishes):

    t_34>=16 delta_13 delta_14, t_34>=16 delta_23 delta_24;
    t_12>=16 delta_13 delta_23, t_12>=16 delta_14 delta_24.

Thus

    C >= 2(p+q) + 16 [
      max(delta_13 delta_14,delta_23 delta_24)
      +max(delta_13 delta_23,delta_14 delta_24)].

For a positive L-shape 13,14,23, a stronger form is
C>=2(p+q)+4[(delta_13+delta_14)^2+(delta_13+delta_23)^2].

**[CONDITIONAL TYPE E].** With C<=A<=B=383/504, (1) yields

    (delta_12+delta_34)^2
    +min(delta_13+delta_24,delta_14+delta_23)^2
    <= (383/1008)^2.

If p+q>=383/1008-1/1000, then
w^2<=11953/15750000<49/62500 and w<7/250.
This prunes the near-saturated branch where *both* cross matchings carry substantial positive defect.

**Proof status:** No new uniform bound on sum(delta_ij^2) is claimed. The retained six-defect ceiling <0.081898, Type-E midpoint cap A<=383/504, F3 bound <=89, and global 40<=tau_5<=44 are unchanged. D5 labeling, Type-E exclusion, Types C/D, and generic e>=27 remain open. No generic SDP or D5 labeling was used.

**Verification:** see the paired exact symbolic checker; it checks algebraic identities and rational consequences, while the quantified Cauchy proof is above.