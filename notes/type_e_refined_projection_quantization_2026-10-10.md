# Type E: refined isolated-centre projection quantization (2026-10-10)

**Status:** The vector inequality below is PROVED EXACTLY under its stated hypotheses. Its application to the Type-E graph is CONDITIONAL on the retained midpoint-energy, graph-incidence, and local removal-charge lemmas. No Type-E exclusion is claimed. Retained global range: 40 <= tau_5 <= 44.

## Setup and exact harmonic identity

Let z_1,...,z_20 in R^5, ||z_i||^2=1-a_i, 0<=a_i<=1/4, A=sum a_i<=383/504, u=sum a_i^2. Let ||x||=1 and s_i=(x.z_i)^2<=1/4. Set b=sum s_i, sigma=sum s_i(1/4-s_i), t=sum a_i s_i, rho=sigma+(2/3)(A/4-t)>=sigma, L=5/7-13A/84-u/21, and b0=48/17+14A/255+4u/51.

Write E=sum z_i z_i^T-(20-A)I/5, H=sum H_4(z_i) for the degree-four harmonic kernel (v.w)^4-(2/3)||v||^2||w||^2(v.w)^2+(1/21)||v||^4||w||^4, and V=||E||_F^2/12+||H||_F^2/2. The exact directional contraction and square completion give

V >= (7/17)(L+rho)^2+(85/256)(b-b0+(28/17)rho)^2. (1)

Since L>=Lmin=1777/3024, writing q=b-b0+(28/17)rho gives

V-(7/17)L^2 >= (14/17)Lmin*rho+(85/256)q^2. (2)

## PROVED EXACTLY: two-scale projection-quantization lemma

For any s_i in [0,1/4], with delta=dist(b,(1/4)Z), concavity at fixed b gives sigma>=delta(1/4-delta), 0<=delta<=1/8. Hence if delta>=1/20 then sigma>=1/100; if delta<=1/20 then delta<=5sigma<=5rho. This sharpens the previous linear inequality sigma>=delta/8.

For 3/4<=A<=383/504, the inequalities A^2/20<=u<=A/4 imply

3899/1360 <= b0 <= 370157/128520,

and therefore dist(b0,(1/4)Z)>=d=159/1360.

If delta>=1/20, (2) gives V-(7/17)L^2 >=1777/367200.

If delta<=1/20, the triangle inequality gives

d <= |q|+(28/17+5)rho=|q|+(113/17)rho.

Minimizing the RHS of (2) over |q|>=0, rho>=0 subject to this linear constraint gives |q|*=28432/259335<d and the exact lower bound

epsilon_new = 457849381/101277578880 = 0.004520737818411798...

The previous epsilon was 51456589/13332885120 = 0.003859373911713416...; the gain is exactly 938296871/1418730084144.

For A<3/4, the earlier exact derivative bound partial_i J<=-2377/2520<-1/2 for J=B+(7/17)L^2 gives J(a)-J(a*)>5/1008>epsilon_new, where a*=(1/4,1/4,1/4,5/504,0,...,0).

Combining both cases with the exact degree-four decomposition, and setting W_ij=a_i+a_j-a_i a_j, X_ij=((z_i.z_j)^2-1/4)_+, Y_ij=(1/4-(z_i.z_j)^2)_+, proves

D2 := sum_{i<j}((z_i.z_j)^2-1/4)^2
 >= J(a*)+epsilon_new+(2/3)sum_{i<j}W_ij(Y_ij-X_ij),

where J(a*)=146851901724371/49360958115840.

## CONDITIONAL Type-E safe-pair bounds

Retaining the six-exception incidence classification and removal charges (not re-audited here):

* all-singleton: D2_safe184 >= J(a*)+epsilon_new-6/16 = 1641642531475478291/630290074181160960 = 2.604582554482096...
* one-double: D2_safe184 >= J(a*)+epsilon_new-145/768-5/16 = 1562035582002076451/630290074181160960 = 2.478280471148763...

These are necessary lower bounds, not contradictions. No independent upper bound on D2_safe184 has been established.

**OPEN:** Type E, C, D, generic e>=27. The e=23/24 graph classification remains conditional on delta(G)>=1. Retain M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, and the source-audited Musin/Boyvalenkov antipodal zero-midpoint exclusion. Do not infer a D5 labeling from the six exceptional pairings.

**Next:** incorporate the actual coupling of b0, L, A, u, and the weighted remainder rho-sigma into a small exact polynomial optimization, before considering a new generic SDP.
