# Type E high-center exclusion from eight F3 endpoints (2026-10-28)

**[NEW EXACT DERIVATION — CONDITIONAL TYPE-E BRANCH ELIMINATION]** The high-center branch s>=7 is impossible **provided** the previously retained harmonic/mass resource, contact quantization, 17-vector Frobenius rounding, and finite PSD/D5 classification are valid. Those upstream inputs are NOT re-certified here. This is not an unconditional proof of tau_5=40; the low-center Type E branch and other graph types remain open.

## 1. Upstream inputs, precisely

For H=16K2+F3, let v be the isolated center, x_i^+/-=m_i+/-z_i the sixteen isolated deep edges, and w_1,...,w_8 the eight F3 endpoints. Retain the high-center inputs:

- x=sum_i ||m_i||^2<1/2500; N=sum_nondeep 7t^2(1-4t^2)<=5/64.
- Each nondeep contact is low |t|<1/9 or high 12/25<|t|<=1/2. With rho(t)=min(|t|,1/2-|t|), sum_nondeep rho(t)^2<=5/336.
- Y=[v,z_1,...,z_16] has Gram G within ||G-Hhat||_F<1/9 of a rounded 17-line D5 Gram Hhat=X^T X. The rounded PSD/rank-five/D5 result is conditional on the earlier exact finite classification.

For the 17 unit D5 columns X, 2I<=F=XX^T<=4I. Put R=sqrt(2)X, whose columns are integer roots e_i+/-e_j. Thus RR^T>=4I.

## 2. Exact alignment lemma

**[PROVED EXACTLY]** If ||Y^T Y-X^T X||_F=epsilon<1/9, there is an orthogonal U with ||Y-UX||_F<2/17<1/8.

Proof: P=X^T F^{-1}X, L=YX^T F^{-1}, Z=Y(I-P), so Y=LX+Z and ZX^T=0. With B=L^T L-I, the P-P compression of the Gram difference gives ||B||_F<=epsilon/2, hence sigma_min(L)>h=sqrt(17/18). Polar-decompose L=U(L^TL)^{1/2}. Then ||(L-U)X||_F<=epsilon/(1+h), using ||X||_op<=2. The two symmetric cross blocks of the Gram difference give 2||X^T L^T Z||_F^2<=epsilon^2; sigma_min(X^T)>=sqrt(2) and sigma_min(L)>h imply ||Z||_F<=epsilon/(2h). Hence ||Y-UX||_F<=epsilon/(1+h)+epsilon/(2h)<1/17+1/17=2/17. The strict comparisons use h>8/9 and h>17/18.

## 3. Exact D5 extension atlas

**[PROVED EXACTLY]** For any 17 of the 20 projective D5 roots R, an integral column c in {-1,0,1}^17 that lies in col(R^T), c=R^T t0, satisfies ||t0||^2 in {0,1,5/4,2,3}. If ||t0||^2=2, then t0 is one of the six *signed* integer roots corresponding to the three omitted projective lines.

Proof: A support ij is double if both e_i+e_j and e_i-e_j remain. The double-support graph is K5 with at most three edges removed, so connected with no isolated vertices. Each double support enforces t_i+t_j,t_i-t_j in {-1,0,1}, hence |t_i|+|t_j|<=1 and the five coordinates all have the same integral/half-odd-integral parity. In the half-odd case all are +/-1/2 (norm squared 5/4). In the integral case every coordinate is 0,+/-1, and its nonzero support is independent in the double-support graph, of size at most three. Squared norm two means exactly two nonzero coordinates; their support is not double, and any retained root on that support forces the other (missing) root sign. Thus exactly the six signed omitted roots.

**[PROVED BY FINITE INTEGER CERTIFICATE]** Three-term integer root relations q with exactly three +/-1 entries and Rq=0 span ker(R), dimension 12, for every 17-root subset. The checker enumerates all 1920 even-signed coordinate-permutation Weyl actions, all 1140 omitted triples, and seven orbits of sizes 120,60,160,40,40,480,240. On each orbit representative, exact rank modulo 101 of the triangle relations is 12, proving rational rank 12. It also enumerates the 3^5 independent correlation assignments: six orbits have 49 feasible columns and one 40-member orbit has 51. In every case the norm-squared-two patterns are exactly the six signed missing roots.

## 4. Each of eight F3 endpoints must be near a missing signed root

For any F3 endpoint w, all contacts with v and with the 32 endpoints of the sixteen isolated edges are nondeep. For each isolated edge,
|w.x_i^+ + w.x_i^-|=2|w.m_i|<=2sqrt(x)<1/25.
The low/high intervals are separated by more than 1/25, so its two contacts have the same category, and if high have opposite signs. Rounding these contacts to 0,+/-1/2 produces a vector b_w in {0,+/-1/2}^17 approximating Y^T w. The exact two-contact Walsh inequality and the global nondeep rho budget give
e_w^2:=||Y^T w-b_w||^2<=5/336<1/64; thus e_w<1/8.

Let c_w=2b_w in {-1,0,1}^17 and t=sqrt(2)U^T w (so ||t||=sqrt(2)). The alignment bound gives
||c_w-R^T t|| <=2(e_w+||Y-UX||_F)<1/2.
For each triangle relation q, q^T c_w is an integer and
|q^T c_w|=|q^T(c_w-R^T t)|<sqrt(3)/2<1.
Thus every triangle relation annihilates c_w, and by triangle spanning c_w=R^T t0 for a unique t0. Since RR^T>=4I,
||t-t0||<1/4.
The atlas norm list and the strict gaps sqrt(2)-sqrt(5)/2>1/4 and sqrt(3)-sqrt(2)>1/4 force ||t0||^2=2. Therefore t0 is one of six signed missing roots, and
||w-U(t0/sqrt(2))||<1/(4sqrt(2)).

## 5. Contradiction and proof ledger

Eight distinct core endpoints occupy only six signed root neighborhoods. Two w,w' share one signed unit root; then
||w-w'||<1/(2sqrt(2)) and w.w'=1-||w-w'||^2/2>15/16>1/2,
contradicting the kissing-code contact bound. Counting **signed** roots (six), not merely projective lines (three), is essential because antipodal code endpoints are allowed.

**[CONDITIONAL TYPE-E CONSEQUENCE]** The s>=7 branch is eliminated assuming all upstream high-center certificates. The argument uses the eight F3 endpoints and does not depend on the choice of F3 perfect matching.

**[INDEPENDENTLY VERIFIED HERE]** The exact alignment inequalities, analytic D5 extension theorem, seven-orbit/triangle-spanning certificate, and eight-versus-six pigeonhole step. **[UPSTREAM CONDITIONAL]** N<=5/64, x<1/2500, ||G-Hhat||_F<1/9, and rounded PSD/D5 classification. **[OPEN]** Type E with s<7; Types C,D; generic e>=27; non-isolated cases; sparse e=23/24 without delta(G)>=1. Retain M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, and the Musin/Boyvalenkov zero-midpoint theorem. **Global proved range: 40<=tau_5<=44.**

Verifier: [tau5_typeE_high_center_core_extension_2026-10-28_verify.py](tau5_typeE_high_center_core_extension_2026-10-28_verify.py).
