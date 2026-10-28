# Type E: joint mass-deficit fourth energy and 184-safe-pair Q bridge (2026-10-27)

**[PROVED EXACTLY — universal algebra]** Delsarte polynomial decomposition, capped-simplex moment bounds and Q/frame identity.
**[PROVED EXACTLY — CONDITIONAL TYPE E]** New joint fourth-energy cap, strengthened projected correlation floor and F3 branchwise 184-safe-pair floors. The F3 broom S<=89, matching M(P)>=S/2-28/3, graph structure and previously proved endpoint-charge/diagonal-interference lemmas are retained inputs, not re-proved here.
**[OPEN]** No Type-E exclusion; global proved range stays 40<=tau_5<=44.

## 1. Re-derive total deep mass 410

For a 41-code in R^5 with pairwise scalar products <=1/2, use F(t)=7t^2(4t^2-1). Its exact positive-definite harmonic expansion is

    F(t)=1+(35/3)(t^2-1/5)+28(t^4-(2/3)t^2+1/21).

Thus sum_{u,v}F(u.v)>=41^2=1681. The diagonal is 41F(1)=861. All nondeep pairs have -1/2<=u.v<=1/2 and contribute F<=0. Consequently the unordered deep-edge mass is at least (1681-861)/2=410. This uses the standard harmonic addition theorem.

For a selected deep edge m_i +/- z_i, set a_i=||m_i||^2=(1+t_i)/2 in [0,1/4), r_i=||z_i||^2=1-a_i, and

    D(a)=21-F(2a-1)=196a-644a^2+896a^3-448a^4.

D is increasing and strictly concave on [0,1/4]: D'(1/4)=14, D''(a)=-56(96a^2-96a+23)<0. Also D(a)>=84a.

## 2. Re-audit stronger scalar mass bound and NEW fourth-energy cap

Let x=A_I be total midpoint energy of 16 isolated K2 edges and y=A_C that of the four edges of the F3 matching P guaranteed by the mass theorem. Write S=M(F3)<=89. The total mass >=410 gives

    sum_I D(a_i)<=S-74<=15.

By concavity and x<1/4, D(x)<=sum_I D(a_i), so x<=r=D^{-1}(15), where

    r=(1-sqrt((7+sqrt(721))/56))/2
     =0.11125520694693414098....

The matching theorem M(P)>=S/2-28/3, with M(P)=84-sum_C D(a_i), implies

    sum_C D(a_i)+(1/2)sum_I D(a_i)<=169/3.       (1)

First y<3/4, because y>=3/4 would force sum_C D>=63>169/3. For y>1/2, capped-simplex concavity implies sum_C D>=42+D(y-1/2). Hence

    y<=1/2+s(x), s(x)=D^{-1}(43/3-D(x)/2).        (2)

The inverse D^{-1} is increasing convex, and the inner argument is convex, so s is positive convex on [0,r]. Put

    s0=s(0)=D^{-1}(43/3)=0.10354492689797308...,
    s1=s(r)=D^{-1}(41/6)=0.03978180614350047....

Since r>s0, the convex function x+s(x) has its maximum at x=r. The y<=1/2 case is weaker. Thus the stronger 2026-10-14 mass-concavity ceiling is independently re-audited:

    A=x+y<=Astar=1/2+r+s1
     =0.65103701309043461105...<0.651038.         (3)

This strengthens, but does not invalidate, the older A<=383/504 under the additional retained mass inputs.

**NEW:** Put U=sum a_i^2. For the isolated edges, U_I<=x^2 because x<1/4. For the four core edges, U_C<=1/8+s(x)^2, including the case y<=1/2. Since s>=0 is convex, x^2+s(x)^2 is convex and its maximum is at x=r (because r>s0). Hence

    U<=Ustar=1/8+r^2+s1^2
     =0.13896031317284419449....                  (4)

Both (3) and (4) are sharp for the scalar mass-deficit relaxation at isolated energies (r,0,...,0) and core energies (1/4,1/4,s1,0); this is NOT a full Type-E code construction.

## 3. NEW raw squared-correlation floor with exact stability

Let w_ij=(z_i.z_j)^2 and Vz=||sum_i z_i z_i^T-((20-A)/5)I||_F^2>=0. The exact frame identity is

    sum_{i<j}w_ij=30-3A+A^2/10-U/2+Vz/2.       (5)

The scalar expression decreases with A in the relevant interval. From (3),(4),

    sum_{i<j}w_ij>=Lstar
      :=30-3Astar+Astar^2/10-Ustar/2
       =28.019793723383645542....                   (6)

A fully rational consequence is

    sum_{i<j}w_ij >
    17512369247009/625000000000 =28.0197907952144, (7)

using r<111256/10^6 and s1<39782/10^6. This supersedes the weaker conditional floor 8790283/317520=27.684186822877... when the mass hypotheses are retained.

The exact nonnegative stability decomposition is

    sum_{i<j}w_ij-Lstar
     =(Astar-A)(3-(Astar+A)/10)
       +(Ustar-U)/2+Vz/2.                           (8)

Near equality therefore requires A and U near their mass-relaxation maxima and small frame variance. It does not itself force A>Astar.

## 4. NEW F3 squared-defect and 184-safe-pair bridge

Let K be the six core pairings and R the 184 endpoint-safe pairings. For a core pair d_ij=[|z_i.z_j|-1/2]_+, put delta_ij=[w_ij-1/4]_+=d_ij+d_ij^2 if active. Always sum_K w_ij<=3/2+sum_K delta_ij.

**P2:** Endpoint-charge and signed-triangle lemmas give at most three one-contact active pairs, d<1/8 and sum d<=1/4. Convexity of g(d)=d+d^2 yields sum_K delta<=2g(1/8)=9/32.

**P1/P3:** If the two-contact diagonal is inactive, the same 9/32 cap applies. If active, write its excess d0 and the total one-contact excess s:
- No one-contact active: delta total<=g(1/4)=5/16=80/256.
- One active, s<=1/8: diagonal interference gives d0<=3/16-s/2-s^2. The secant bounds g(d0)<=(19/16)d0 and g(s)<=(9/8)s imply total<=57/256+(17/32)s<=74/256.
- Two active, s<=1/4: diagonal interference gives d0<=h(s)=1/6-s/3-s^2/3. Also g(d1)+g(d2)<=(9/8)s. The function g(h(s))+(9/8)s is increasing on [0,1/4] because its derivative is at least 9/8-2/3>0. Its maximum is g(1/16)+9/32=89/256.

Thus

    P1/P3: sum_K delta<=89/256, sum_K w<=473/256;
    P2:    sum_K delta<=9/32,   sum_K w<=57/32.   (9)

Subtracting (9) from (6) gives the new conditional **184-safe-pair squared-correlation floors**:

    P1/P3: sum_R w_ij>=Lstar-473/256
                     =26.1721374733836455...;
    P2:    sum_R w_ij>=Lstar-57/32
                     =26.2385437233836455....      (10)

With C_K=473/256 or 57/32, there is an exact nonnegative stability identity

    sum_R w_ij-(Lstar-C_K)
      =(Astar-A)(3-(Astar+A)/10)
       +(Ustar-U)/2+Vz/2+(C_K-sum_K w_ij).          (11)

This explicitly transfers the global Q floor into the six-exception language and preserves second-order frame variance and core-cap slack. The trivial upper bound on 184 safe pairings is 46, so (10) is not a contradiction.

## Proof ledger

**[VERIFIED]** Exact SymPy/Fraction verifier checks harmonic expansion, deficit polynomial, radical roots, rational floors, F3 contact/sign enumeration, squared-defect envelopes and the 20-vector frame identity. Convexity and harmonic PSD are proved analytically above.

**[RETAINED, NOT REPROVED]** F3 broom S<=89, matching M(P)>=S/2-28/3, F3 endpoint-charge/diagonal-interference theorems, Musin/Boyvalenkov zero-midpoint exclusion, 184-safe/six-core partition. Sparse e=23/24 classification requires delta(G)>=1.

**[OPEN]** Type E, Types C and D, generic e>=27 and non-isolated branches. Next: derive a nontrivial *upper* bound on the 184-safe squared mass using Walsh mixing, center constraints and rank-five Gram geometry, and compare to (10). Global 40<=tau_5<=44 unchanged.

Companion verifier: tau5_typeE_mass_concavity_joint_Q_safe_bridge_2026-10-27_verify.py.
