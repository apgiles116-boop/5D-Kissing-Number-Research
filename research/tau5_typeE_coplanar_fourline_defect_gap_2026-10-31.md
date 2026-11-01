# Type E: coplanar four-core raw-defect gap

Date: 2026-10-31. **[PROVED EXACTLY — under stated hypotheses]** Type E remains **OPEN**. Global proved range remains **40 <= tau_5 <= 44**.

## Theorems

Let four projected half-differences z_i lie in a common real two-plane, with a_i=1-||z_i||^2 in [0,1/4]. Put A_C=sum a_i, B=1-A_C, theta=arccos(2/3), and

D_C=sum_{1<=i<j<=4} (|z_i.z_j|-1/2)_+.

**[PROVED EXACTLY — no total-mass cap]**

D_C >= 1/9.                                                   (1)

This is sharp in the four-line relaxation: take ||z_i||^2=3/4 and projective angles 0, theta, 2theta, 3theta. Its A_C=1 is *outside* the retained Type-E cap.

**[PROVED EXACTLY — mass-sensitive, no D5 labeling]**

D_C >= 1 - pi/(4theta) + (pi/(3theta)-1)(1-A_C).          (2)

**[PROVED EXACTLY — Type E with A_C<=A<=383/504]**

D_C >= 383/504 - 257*pi/(1512*theta)
    = 0.1250287897245... > 1/8.                            (3)

Thus four coplanar core lines in Type E must consume more than 1/8 of the retained six-core raw-defect budget. This does not contradict the upper bound D_C<=1780062775/4032758016<0.441401.

## Proof of the mass-sensitive theorem

Write b_i=1/4-a_i in [0,1/4]. Set Delta=pi/3-theta, k=1/(4theta), h=Delta/(2theta). We prove the scalar inequality, valid for b,c in [0,1/4], p=sqrt((3/4+b)(3/4+c)), and 0<=g<=pi:

(p*|cos(g)|-1/2)_+ >= k*(theta-g)+h*(b+c).                 (4)

First, p(b,c) is jointly concave, and comparison at the four corners of the square yields

p >= 3/4+(2sqrt(3)-3)(b+c).                               (5)

The function Phi(p)=arccos(1/(2p)) is increasing and concave on [3/4,1], because Phi'(p)=1/(p sqrt(4p^2-1)) is positive and decreasing. Thus Phi(p(b,c)) is concave. Corner comparison gives

Phi(p)-theta >= 2Delta*(b+c).                             (6)

The only nontrivial corner is (b,c)=(1/4,0), where (6) becomes 2 arccos(1/sqrt(3)) >= theta+pi/3. Taking cosines (both angles in [0,pi]) reduces it to sqrt(15)<=4.

For 0<=g<=theta, concavity of cosine gives cos(g)>=1-g/(3theta). Using (5) and cos(g)>=2/3 yields

p*cos(g)-1/2 >= k*(theta-g)+(2/3)(2sqrt(3)-3)(b+c)
             >= k*(theta-g)+h*(b+c).

The last comparison follows from theta>pi/4 (so h<1/6) and (2/3)(2sqrt(3)-3)>1/4.

For theta<=g<=Phi(p), the function p*cos(g)-1/2 is concave in g. At g=theta it dominates the affine right-hand side, as above. At g=Phi(p) it equals zero, while the affine right-hand side is nonpositive by (6). Concavity proves (4) between. For g>=Phi(p), the affine right-hand side stays nonpositive, while the positive-part left-hand side is nonnegative, including for g>pi/2. Hence (4) holds for all g in [0,pi].

Represent the four projective directions by ordered angles 0<=phi_1<=...<=phi_4<pi. Their four cyclic gaps g_i sum to pi. The four cyclic adjacent pairs are distinct among the six core pairs. Sum (4) over these four pairs. Each b_i occurs twice:

D_C >= k*(4theta-pi)+2h*B
    = 1-pi/(4theta)+(pi/(3theta)-1)(1-A_C),

proving (2). Since theta<pi/3, its coefficient of B is positive. A_C<=383/504 gives (3).

For a rigorous rational certificate of the strict >1/8 comparison, (3)>1/8 is equivalent to theta>257pi/960. Use pi<355/113 and x=257*355/(960*113)<1. The alternating cosine Taylor bound

cos(257pi/960)>cos(x)>=1-x^2/2+x^4/24-x^6/720>2/3

shows theta>257pi/960. The final comparison is exact rational arithmetic; the companion verifier checks it. The bound pi<355/113 follows, for example, from Machin's identity pi/4=4atan(1/5)-atan(1/239) and alternating rational arctangent bounds.

The pairwise affine coefficients k and h are coefficientwise optimal within the certificate form (4): b=c=g=0 forces k<=1/(4theta), and b=c=1/4, g=pi/3 forces h<=2kDelta. No claim of global sharpness of (2) is made.

## Independent sharp 1/9 proof

Let f(g)=(3|cos g|/4-1/2)_+. If a cyclic gap exceeds pi/2, the other three sum to less than pi/2. On [0,pi/2], the chord bound gives f(g)>=k(theta-g), hence the sum of their defects exceeds k(3theta-pi/2)>1/9.

Otherwise all four gaps are <=pi/2. Any gap >theta has zero defect; transferring its excess to gaps <theta cannot increase the total defect. We may therefore minimize with all gaps in [0,theta]. There f(g)=3cos(g)/4-1/2 is concave. Its sum on the polytope 0<=g_i<=theta, sum g_i=pi, is minimized at a vertex. Because 3theta<pi<4theta, each vertex has three gaps theta and one pi-3theta. Thus the sum is at least 3cos(pi-3theta)/4-1/2 = (3/4)(22/27)-1/2=1/9. The four-line witness above attains it.

## Implication for the research route

**[PROVED EXACTLY — strategic consequence]** For the 21 normalized selected lines, normalizing z_i increases |z_i.z_j|. Hence D_norm>=D_C>1/8 in the coplanar branch, so the universal 21-line raw-defect lower bound (~0.0534355) is automatically satisfied by the core alone. Improving that universal *lower* bound modestly will not by itself eliminate this branch. The next useful target is an *upper* bound on the six core defects coupled to signed F3 endpoint/Walsh constraints and isolated safe-pair measurements.

**[OPEN]** Type E remains open, including other Q-rank and noncoplanar cases. Types C, D, generic e>=27, and non-isolated branches remain open. Preserve the stronger star sum<=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass>=2137/6, A<=383/504, exact raw/homogeneous defect ceilings, Musin/Boyvalenkov zero-midpoint exclusion, and all earlier conditional rank/Q statements. Sparse e=23/24 classification still requires delta(G)>=1. **Global proved range: 40<=tau_5<=44.**
