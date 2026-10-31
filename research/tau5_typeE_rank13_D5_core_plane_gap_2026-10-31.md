# Type E: rank-13 D5 core-plane exclusion and sign-parity theorem

Date: 2026-10-31. **Global proved range 40 <= tau_5 <= 44. Type E OPEN.**

## Proof-status ledger

**[PROVED EXACTLY — conditional geometric theorem]** Fix a sixteen-line D5 subframe obtained from the twenty projective roots (e_i ± e_j)/sqrt(2) by deleting both signs on one coordinate support {p,q} and two further roots on distinct supports. Label the sixteen isolated Type-E normalized projected lines u_i by this subframe, up to a common orthogonal rotation, and let L=span(e_p,e_q). Write each selected edge as m_i ± z_i, a_i=||m_i||²<=1/4, u_i=z_i/sqrt(1-a_i). If all four F3 core projected vectors z_c lie in L, then the following three inequalities are incompatible:

A=sum_all a_i <= 383/504;
A_I=sum_isolated a_i <= 1/10000;
E_I=sum_isolated ||u_i u_i^T-r_i r_i^T||_F² <= 1/250000.

**[PROVED EXACTLY — stronger boundary]** If the isolated lines are exactly that rank-13 D5 subframe and all sixteen isolated midpoints vanish, then four core projected vectors in L would force A_C >= 2(sqrt(2)-1) > 383/504. Thus at least one core projector must lie outside L; in particular not all four core projectors can be ambiguous relative to the rank-13 isolated Q measurements.

**[PROVED EXACTLY — rank-13 sign graph]** If the isolated traceless-Q span has rank 13 with unit missing matrix S of rank two, and all four core projectors have two genuine rank-one completions Q_c=L_c+sigma_c t_c S, t_c>0, sigma_c=±1, define B_cd=<L_c,L_d>+w_cw_d/5 and h_cd=(1/2-m_c.m_d)²-B_cd. The six *projected* core contact envelopes are feasible for a sign choice iff h_cd>=-t_ct_d for every pair and the graph of pairs h_cd<t_ct_d is bipartite. This is not sufficient for the full four-endpoint constraints, which also have mixed midpoint terms.

**[PROVED EXACTLY — energy cancellation]** For those sign completions, V_z=||sum Q_i||_F² and Q_6=sum_core_pairs (z_c.z_d)² satisfy V_z-2Q_6 independent of the core signs. Thus the global squared-correlation identity alone cannot choose among these completions.

**[OPEN]** No Type-E exclusion without the D5 reference/plane hypotheses; no claim that an arbitrary Type-E isolated frame has a D5 labeling. Types C, D, E, generic e>=27 and non-isolated branches remain open.

## Proof of the geometric theorem

For any two distinct selected deep edges, averaging opposite endpoint-sign inequalities gives

m_c.m_i + |z_c.z_i| <= 1/2.

Consequently |z_c.z_i| <= 1/2+sqrt(a_ca_i) <= (1+sqrt(a_i))/2. For normalized u_i and a projective unit reference root r_i, choose its sign so u_i.r_i>=0. The identity

||u_i-r_i||²=2(1-u_i.r_i) <= 2(1-(u_i.r_i)²)=||u_i u_i^T-r_i r_i^T||_F²

shows |z_c.r_i| <= (1+sqrt(a_i))/(2sqrt(1-a_i)) + ||u_i u_i^T-r_i r_i^T||_F.

A rank-13 D5 subframe retains at least one sign on *every* support other than {p,q}; in particular each j in {p,q} has a retained root (e_j ± e_k)/sqrt(2), k outside {p,q}. For z_c in L this root gives |z_c.r_i|=|(z_c)_j|/sqrt(2), so

|(z_c)_j| <= (1+sqrt(a_i))/sqrt(2(1-a_i)) + sqrt(2)||u_i u_i^T-r_i r_i^T||_F.

Under A_I<=1/10000 and E_I<=1/250000, each a_i<=1/10000 and each projector displacement <=1/500. Thus

|(z_c)_j| <= 101/sqrt(19998)+sqrt(2)/500 < 101/141+3/1000 < 18/25 =: B.

The last strict margin is 97/141000.

Every core has ||z_c||²=1-a_c>=3/4, and both its L coordinates are <=B in absolute value. They are nonzero. Classify the four core projective vectors by the sign of the product of their two L coordinates, giving two classes. For two vectors in the same class, after global sign changes they lie in the same quadrant. Their lengths are >=sqrt(3)/2, and their normalized coordinate magnitudes are <= B/(sqrt(3)/2). An elementary angular-interval argument therefore gives

|z_c.z_d| >= 2B sqrt(3/4-B²) = 18sqrt(579)/625 > 432/625,

using sqrt(579)>24. The endpoint envelope forces m_c.m_d < 1/2-432/625 = -239/1250 for every same-class pair.

For a class of n core vectors, PSD gives 0<=||sum m_c||²=sum a_c+2sum_{c<d}m_c.m_d, hence its midpoint energy is > (239/1250)n(n-1) when n>=2. The two class sizes sum to four, and the minimum of n(n-1)+(4-n)(3-n) is four. Therefore

A_C > 4(239/1250)=478/625 >383/504,

with exact margin 1537/315000. Contradiction.

If A_I=E_I=0, replace B by 1/sqrt(2). The same angular calculation gives |z_c.z_d|>=1/sqrt(2) within a class, hence A_C>=4(1/sqrt(2)-1/2)=2(sqrt(2)-1)>383/504.

## Rank-13 sign-parity and frame-energy identities

For genuinely ambiguous rank-one core completions, write Q_c=L_c+sigma_c t_c S with S Frobenius-unit and orthogonal to the isolated Q span. Then

(z_c.z_d)²=B_cd+sigma_c sigma_d t_ct_d.

Because m_c.m_d<=1/4, the necessary envelope |z_c.z_d|<=1/2-m_c.m_d is equivalent to sigma_c sigma_d t_ct_d<=h_cd. If h_cd<-t_ct_d no sign works; if -t_ct_d<=h_cd<t_ct_d opposite signs are forced; if h_cd>=t_ct_d either works. A graph whose edges require opposite signs has a feasible 2-coloring iff bipartite. This is an iff statement **only for the six projected envelopes**.

Put T=sum_isolated Q_i+sum_core L_c and t_sigma=sum_c sigma_c t_c. Orthogonality to S gives

V_z=||T||_F²+t_sigma²,
Q_6=sum_{c<d}B_cd + (t_sigma²-sum_c t_c²)/2.

Thus V_z-2Q_6=||T||_F²-2sum B_cd+sum t_c², sign-independent. The exact identity

Q_all=30-3A+A²/10-(1/2)sum_i a_i²+V_z/2

implies Q_safe=Q_all-Q_6 is sign-independent too. A scalar Q-energy floor cannot resolve the rank-13 signs; the full signed endpoint constraints are needed.

## Next step and preserved ledger

Seek an exact perturbation estimate transferring closeness of the sixteen isolated Q measurements to closeness of the rank-two missing matrix S and its ambiguity plane, using the appropriate D5 subframe spectral gap (not a universal four-star constant). Then apply the forbidden-neighborhood inequality without assuming the core plane is exactly the reference plane.

Preserve: star 70/3, broom M(F3)<=89, matching M(P)>=S_total/2-28/3, twenty-edge mass >=2137/6, A<=383/504, exact raw and homogeneous defect caps, Musin/Boyvalenkov zero-midpoint exclusion, and sparse e=23/24 classification only under delta(G)>=1. **Global proved range unchanged: 40<=tau_5<=44.**
