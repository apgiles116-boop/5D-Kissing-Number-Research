# Type E: sharp singleton PSD certificate and five-edge stability (2026-10-10)

**Proof ledger:** Local lemmas below are PROVED EXACTLY from stated hypotheses. Application to Type E is CONDITIONAL on the retained all-singleton F3 incidence localization and midpoint energy A <= 383/504. No Type-E elimination; retained 40 <= tau_5 <= 44.

## Sharp local singleton lemma [PROVED EXACTLY]

Let four unit endpoints be m_i +/- z_i and m_j +/- z_j, with m_i.z_i=m_j.z_j=0, a=||m_i||^2, c=||m_j||^2 in [0,1/4]. All cross products are <=1/2, exactly one is <-1/2, and |z_i.z_j|=1/2+d, d>0. Orient z_j so z_i.z_j=1/2+d, put m_i.m_j=-b, w=z_i.m_j, v=m_i.z_j. The endpoint inequalities imply

|w+v| <= b-d,  |w-v| >= b+d.

After simultaneous reversal of z_i,z_j, take w-v>=b+d, so b>=d, w>=d, -v>=d. Flip m_i and inspect the four-vector Gram matrix with diagonal blocks diag(a,1-a), diag(c,1-c), and cross block B=[[b,-v],[w,1/2+d]]. B is nonnegative and entrywise >= B0=[[d,d],[d,1/2+d]]. Spectral norm of a nonnegative matrix is monotone in its entries. Hence Gram PSD implies the matrix with B0 is PSD. Its determinant is

det(G0) = [ac(3-4a-4c+4ac)-4ac*d-3d^2]/4 >= 0.

**Exact sharp inequality:**
3d^2+4ac*d <= ac(3-4a-4c+4ac),

equivalently d <= [sqrt(ac(9-12a-12c+16ac))-2ac]/3 (for ac>0). Equality is realized by the local PSD rank-three Gram matrix with b=w=-v=d. The four cross products are 1/2,1/2,-1/2,-1/2-4d. This is only local realizability, not global Type E.

## Quadratic midpoint imbalance penalty [PROVED EXACTLY]

Put s=a+c<=1/2, p=ac, f=s(1-s)/2, P(t)=3t^2+4pt-p(3-4s+4p). Then P(d)<=0 and

P(f)=(a-c)^2[3(1-s)^2+4p]/4.

As d<=f and P(f)-P(d)=(f-d)[3(f+d)+4p]<=(f-d)(6f+4p), while 3(1-s)^2>=6f, it follows that

**d + (a-c)^2/4 <= (a+c)(1-a-c)/2.**

The coefficient 1/4 is optimal uniformly: at a=1/4,c=1/4-epsilon,d=d_*(a,c), (f-d)/epsilon^2 -> 1/4.

## Four-cross-edge variance [PROVED EXACTLY]

For four core midpoint energies a1,...,a4, set C=sum a_i, p=a1+a2, q=a3+a4, delta=p-q, x=a1-a2, y=a3-a4. If all four cross pairs 13,14,23,24 have positive singleton exceedances, summing the preceding lemma gives

S=d13+d14+d23+d24 <= L(C)-delta^2/4-3(x^2+y^2)/4,
where L(C)=C(1-C/2).

## Five-edge spectral stability [PROVED EXACTLY]

Suppose 12 is also positive singleton and 34 is missing. Put D=d12+S, k=1-1/sqrt(2), V=m1+m2, W=m3+m4, T=m3-m4, E=V+W/sqrt(2). The exact identity

C/sqrt(2)-[sqrt(2)(-m1.m2)-V.W]=[||E||^2+||T||^2/2]/sqrt(2)

and d_ij<=-m_i.m_j on singleton-positive pairs imply

**D <= D0(C) - k*delta^2/4 - 3k*(x^2+y^2)/4 - ||E||^2/2 - ||T||^2/4**,
D0(C)=C/2+k*L(C).

With Cmax=383/504, a rational contradiction argument gives the explicit uniform gap

**D <= D0(Cmax)-1/5000 = 0.517766022324...**

Sketch of exact gap certificate: assume D>D0(Cmax)-eps with eps=1/5000. Since D0'>=1/2, Cmax-C<2eps. Set eta(C)=D0(C)-L(C), whose derivative has absolute value <=1/2. Then eta(C)>eta(Cmax)-eps, d12>=eta(C)-eps, |delta|<=2sqrt(eps/k), ||E||<=sqrt(2eps), ||T||^2<=4eps. Using

2(-m1.m2)=delta-||E||^2+sqrt(2)E.W+||T||^2/2,

and ||W||^2<=2C, one gets eta(Cmax)<(1/sqrt(k)+sqrt(2Cmax))*sqrt(eps)+3eps. But 1/sqrt(k)<187/100, sqrt(2Cmax)<5/4, sqrt(eps)<1/70 give RHS<1581/35000<23/500, while 1/sqrt(2)<442/625 gives eta(Cmax)>11873/254016>23/500. Contradiction.

## Type-E all-singleton corollary [CONDITIONAL]

Assume only the six F3 core pairings can have positive defects, all of singleton type, and total core midpoint energy C<=A<=383/504. Classify the positive support on four vertices: <=3 edges gives D<=3/8; four-cycle D<=L(C); four-edge paw D<=C/2+3/32; five edges use the new gap; six edges D<=C/2. Thus

**sum_core d_ij < 0.517767**.

Since d<=1/8, the raw quartic positive defect R=sum (1/2+d)^2(d+d^2) satisfies

**R <= (225/512)*sum_core d_ij < 0.227534**.

This improves the retained generic R<=0.441401 for the all-singleton pattern without assuming the extra upstream C_core<=169/252. It is weaker than the optional R<0.204786 result with that extra premise. The double-incidence pattern is not improved here.

**OPEN:** No contradictory safe-pair upper bound, no Type-E elimination, no D5-labeling theorem. Type C, D, generic e>=27 remain open. Keep the source-audited 21-line zero-midpoint exclusion, M(F3)<=89, matching S/2-28/3, and A<=383/504; do not regress to obsolete F3<=94 or S/2-343/32.
