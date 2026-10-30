# Type E: critical-rectangle Q gap and sharp five-well Walsh quantization

2026-10-30. **Global proved range unchanged: 40 <= tau_5 <= 44.**

## Proof status

**[PROVED EXACTLY, standalone]** For any four safe endpoint products t_j in [-1/2,1/2], their degree-four Delsarte nondeep mass has a sharp five-well lower bound (Section 2).

**[PROVED CONDITIONALLY]** Assuming the retained Type-E mass/harmonic and tensor-contact stability theorems, and the exact six/seven-basis signed-Gram, ADE and sixteen-line D5 extension atlases, the *critical rectangle* obeys

Q > F_* + 1/1440 = 28.39720122578...,

where Q=sum_(i<j)(z_i.z_j)^2, F_*=F(x_2,209/30)=28.39650678133767..., x_2 is the small root D(x_2)=2509/6400, and D(x)=196x-644x^2+896x^3-448x^4. The decimal is illustrative; the proof uses the exact algebraic F_*.

**[OPEN]** This does not exclude Type E outside the critical rectangle, or determine tau_5. The older atlas completeness is an explicit proof dependency, not newly recertified here.

## 1. Resource and tensor-contact reduction

Let x be the sum of midpoint energies on the sixteen isolated deep edges; s the sum of squared contacts with the isolated center; N0 the nondeep Delsarte mass of the forty center contacts; and R the nondeep mass of the other 754 safe contacts (736 from 184 fully safe selected-edge pairings, plus 18 safe core contacts). The retained Type-E theorem gives

D(x)+E(s)+N0+R <= 15,
E(s)=10+(35/64)(5s-32)^2.

Set s0=209/30 and x2 the small root D(x2)=2509/6400, with exact enclosure x2<2094/1000000. On the critical rectangle

x2 <= x <= 1/250,  69/10 <= s < s0,

the retained tensor-contact SOS decomposition and exact derivative bounds give, for epsilon=Q-F_*,

epsilon >= (2/3)(x-x2)+(1/10)(s0-s)+R0/112,
R0=15-D(x)-E(s)-N0 >= R >= 0.

Therefore x-x2 <=3epsilon/2, s0-s<=10epsilon, and R<=112epsilon. This last inequality directly couples the 754 noncenter safe contacts to the Q-floor gap.

## 2. New sharp five-well Walsh theorem

For four safe contacts t1,...,t4, define W=(sum t_j^2)/4, b=1/4-W, and Nblock=sum 7t_j^2(1-4t_j^2). Write b=k/16+r with k=floor(16b) and 0<=r<=1/16. Then

Nblock >= 28r(1-16r).

Proof: set d_j=1/4-t_j^2 in [0,1/4]. Now sum d_j=4b and Nblock=28 sum d_j(1/4-d_j). Concavity minimizes this at a capped-simplex vertex: k coordinates 1/4, one coordinate 4r, and the rest zero (at b=1/4, all four coordinates equal 1/4). The bound is sharp for the abstract four-contact cube.

If eta=dist(W,{0,1/16,1/8,3/16,1/4}), then Nblock>=28eta(1-16eta)>=14eta. Summing over 184 safe blocks gives the **new conditional five-well stability inequality**

sum_safe dist(W_ij,{0,1/16,1/8,3/16,1/4}) <= R/14 <= 8epsilon.

At zero nondeep slack, each contact is in {0,+1/2,-1/2}, and the exact four-contact Walsh transform has |z_i.z_j| in {0,1/8,1/4,3/8,1/2}. The companion checker enumerates all 81 zero-slack patterns.

## 3. Exact 1/1440 critical-branch contradiction

Suppose epsilon<=1/1440. The preceding inequalities give

R<=7/90<5/64,
x<=2094/1000000+1/960=9407/3000000<1/256,
s>=209/30-1/144=5011/720.

As D and E increase on this rectangle,

N0<=15-2509/6400-E(5011/720)
   =10773469/33177600<21/64.

**Sixteen isolated directions.** For every noncenter safe contact, 7t^2(1-4t^2)<=R<5/64. Concavity in t^2 and exact endpoint checks force |t|<1/9 or |t|>12/25. For any two isolated deep edges, their four contacts are within x/2+sqrt(2x)<1/8 of the signed projected correlation. Since 12/25-1/9=83/225>1/4, all four have the same low/high category and alternating signs when high. The 16-by-16 Gram matrix G16 of the half-differences therefore rounds to a symmetric half-integral Ghat16 with diagonal 1 and off-diagonal 0,+/-1/2. The retained exact Walsh rounding lemma gives

||G16-Ghat16||_F^2 <= (81/1078)R+x^2
 <=4056813856973/693000000000000
 <158207437/26950000000<1/169.

The penultimate number is the **previously certified** signed-Gram atlas threshold. By that atlas and the retained ADE classification, Ghat16 is PSD rank five and represents sixteen D5 projective root lines. The retained polar alignment theorem gives a common orthogonal alignment with vector Frobenius error <1/10.

**Eight F3 endpoints.** Every F3 endpoint has 32 safe contacts with the sixteen isolated pairs. Because |w.m_i|<=sqrt(x)<1/16, the same rounding gives b_w in {0,+/-1/2}^16 with error squared <=(81/1078)R<1/64.

**Isolated center.** For each of its forty contacts define r_t=min(t^2,1/4-t^2). Since N0<21/64, every r_t<1/16, and J=sum r_t <=(4/21)N0 <=1539067/24883200<1/16. If k center contacts are high (closer to +/-1/2 than to zero), then |4s-k|<=4J<1/4; the s interval forces k=28. Let H be the sum of 1/4-t^2 over these 28, and L the sum of t^2 over the other 12. Then H-L=d=7-s>=1/30, H+L=J. The two center contacts on each isolated pair share their category, and high ones have opposite signs, because 2sqrt(x)<1/8. Thus the center's rounded 16-correlation vector b_v exists, and the refined center estimate is

|| (v.z_i)_i-b_v ||^2
 <=(L+(4/3)H^2)/2
 =(J-d)/4+(J+d)^2/6
 <=32096511258649/3715041853440000 <1/64.

The improvement over the older near-seven rounding argument is retention of the positive difference H-L=7-s instead of discarding it.

**Nine-versus-eight contradiction.** The retained exact 16-line D5 extension atlas classifies all 17 Weyl orbits of omitted four-line subsets and shows that the permitted norm-two extensions are exactly the eight signed omitted roots. Its triangle-kernel/integer-rounding lemma applies with the above 1/10 and 1/8 error bounds: the isolated center and eight F3 endpoints must each lie within 27/(100sqrt(2)) of one of those eight roots. Distinct kissing-code points cannot occupy the same neighborhood, since their inner product would exceed 1/2. Nine cannot occupy eight. Therefore epsilon>1/1440 in the critical rectangle.

## 4. Dependencies and next work

The new Fraction verifier checks all displayed rational inequalities, the 17^4 grid of four-contact blocks, sharp capped-simplex extremizers, and all 81 zero-slack Walsh states. It does **not** rerun the upstream signed-Gram atlas or independently prove the retained tensor-contact SOS.

To extend this into a global Type-E Q gap, analyze the adjoining parameter regions x<x2, x>1/250 and s<69/10. The five-well theorem also gives a finite-state route for coupling the 184 safe pairings to the six F3 exceptions.

Retained without regression: star 70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, midpoint A<=383/504, Musin/Boyvalenkov zero-midpoint exclusion, and 40<=tau_5<=44. No identification between six exceptional pairings and six Q-kernel modes is assumed.
