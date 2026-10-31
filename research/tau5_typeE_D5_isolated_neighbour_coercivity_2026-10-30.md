# Type E: D5 isolated-neighbour coercivity and robust midpoint/projector stability

2026-10-30. **Global proved range unchanged: 40 <= tau_5 <= 44.**

## Proof status

- **[PROVED EXACTLY — finite D5 algebra]** The 16 roots remaining after deleting the four positive star roots from the 20 projective D5 roots have 78 meeting-support pairs, degrees 9^4 and 10^12. The meeting-neighbour frame restricted to each root's orthogonal complement has least eigenvalue at least (7-sqrt(17))/4 > 7/10 and full operator norm <=3.
- **[PROVED EXACTLY — conditional on exact D5 alignment and safe contacts]** If x is the total midpoint energy on those sixteen edges, then either x=0 or x >= 3(7-sqrt(17))/[320(7-4sqrt(3))] = 0.3756559642... >175/486.
- **[PROVED EXACTLY — conditional on one common approximate D5 labeling and safe contacts]** If E2 is the sum of squared Frobenius distances between the sixteen normalized projectors and the corresponding D5 projectors, then x<=1/250 implies E2>=x/180. More generally, x<1/35 implies E2>x/260 when x>0.
- **[PROVED CONDITIONALLY — retained Type-E resource theorem]** The existing inequality D(x)+E(s)+N0+R<=15, with E(s)>=10 and A<=383/504, forces x<1/35. Thus exact D5 alignment forces x=0; it does NOT eliminate arbitrary Type E.
- **[OPEN]** The arbitrary Type-E projected directions are not known to admit this D5 alignment. No Type-E exclusion is claimed.

## Exact local D5 spectra

Take r_pq^sigma=(e_p+sigma e_q)/sqrt(2), 0<=p<q<=4. Remove r_0j^+ for j=1,2,3,4. Let N(i) consist of remaining roots whose supports meet the support of r_i in exactly one coordinate. Set Z_i^0=sum_{j in N(i)} r_j r_j^T. Its characteristic polynomial on r_i-perpendicular is:

1. Four opposite-star roots: (t-3/2)^2(t^2-15t/4+3).
2. Six positive nonstar roots: (t-1)(t-2)^2(t-5/2).
3. Six negative nonstar roots: (t-2)^2(t^2-7t/2+2).

Hence the least restricted eigenvalue is lambda_*=(7-sqrt(17))/4>7/10. Direct full characteristic polynomials give ||Z_i^0||_op<=3.

## Universal four-contact mixed-square lemma

For any two fully safe deep-edge blocks, write c=m_i.m_j, b=m_i.z_j, e=z_i.m_j, d=|z_i.z_j|<=1/2 and delta=1/2-d. Choosing a sign for z_j, endpoint safety gives

|c+d|+|b+e|<=1/2, and |c-d|+|b-e|<=1/2.

Therefore |c|<=delta, |b+e|<=delta-c and |b-e|<=delta+c, so

**(m_i.z_j)^2+(z_i.m_j)^2 <= delta^2+c^2 <= 2delta^2.** (1)

No D5 assumption is used in (1).

## Exact D5 energy gap

Let a_i=||m_i||^2<=1/4, w_i=1-a_i and x=sum_I a_i. For exact D5 normalized directions, meeting pairs have d_ij=sqrt(w_i w_j)/2. Since sqrt(w_i)>=sqrt(3)/2,

delta_ij=(1-sqrt(w_i w_j))/2 <= (2-sqrt(3))(a_i+a_j). (2)

As m_i is orthogonal to r_i and w_j>=3/4, the restricted local frames give

(3/4)lambda_* x <= sum_{ij meeting I}[(m_i.z_j)^2+(m_j.z_i)^2].

The meeting graph has maximum degree 10, and convexity on the simplex gives sum_meeting(a_i+a_j)^2<=10x^2. Apply (1),(2):

(3/4)lambda_* x <= 20(2-sqrt(3))^2 x^2.

Thus x=0 or x>=3lambda_*/[80(2-sqrt(3))^2] = 3(7-sqrt(17))/[320(7-4sqrt(3))] >175/486.

## Robust version, one fixed labeling

Let u_i=z_i/sqrt(w_i), P_i=u_i u_i^T, P_i^0=r_i r_i^T, e_i=||P_i-P_i^0||_F, E2=sum e_i^2 and epsilon=max e_i. Signed unit-vector alignment implies

delta_ij <= (2-sqrt(3))(a_i+a_j)+e_i+e_j. (3)

The perturbation of the orthogonal-complement compression of Z_i^0 has operator norm at most 6epsilon (since ||Z_i^0||<=3). Perturbing its at most ten neighbour projectors contributes at most 10epsilon. Weyl's inequality, m_i perpendicular to u_i, and w_j>=3/4 therefore give, whenever epsilon is sufficiently small,

sum_{j in N(i)}(m_i.z_j)^2 >= (3/4)(lambda_*-16epsilon)a_i. (4)

Using (1),(3), the graph inequalities sum(a_i+a_j)^2<=10x^2 and sum(e_i+e_j)^2<=20E2, and (2-sqrt(3))<27/100 gives

(3/4)(lambda_*-16epsilon)x <= 40(2-sqrt(3))^2 x^2+80E2 < 3x^2+80E2. (5)

If x<=1/250, split at epsilon=1/200. In the small-epsilon branch (5) yields E2>453x/80000>x/180. In the other branch E2>1/40000>=x/160>x/180. Hence E2>=x/180.

For x<1/35, split instead at epsilon=1/95. The small-epsilon branch gives E2>333x/85120>x/260; the other branch gives E2>1/95^2>(7/1805)x>x/260.

## Retained resource consequence

The retained polynomial is D(x)=196x-644x^2+896x^3-448x^4=28y(7-16y), y=x(1-x). The retained Type-E resource inequality and E(s)=10+(35/64)(5s-32)^2 imply D(x)<=5. If 1/35<=x<=383/504<34/35, then 34/1225<=y<=1/4. Concavity gives D(x)>=min(1092216/214375,21)>5, a contradiction. Thus x<1/35, conditional on that upstream resource certificate.

**Limitations:** This proves a quantitative second-order necessary deviation from D5, not an incompatible upper bound. The six exceptional core pairings have not been identified with six Q-kernel modes. Preserve star <=70/3, M(F3)<=89, matching >=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504 and the Musin/Boyvalenkov antipodal boundary theorem. Types C,D, generic e>=27, non-isolated branches remain open; sparse e=23/24 classification requires delta(G)>=1.

A companion exact SymPy verifier is in the same research directory.