# Type E: variance-aware quartic frame stability (2026-11-02)

**[GLOBAL PROVED RANGE UNCHANGED]** 40 <= tau_5 <= 44.

**[PROVED EXACTLY — universal lemma]** For 20 real numbers 0<=b_i<=q, B=sum b_i<=B0<4, with q<4, define t_i=1-b_i and F=(sum t_i^2)^2/8-(3/2)sum t_i^4. If 6-3q/2>=0, then

F >= R(B0,q) := 20-4B0+B0^2/2 - (4+B0/2)^2/[4(1/8+(6-3q/2)/B0)].

**Proof.** Put U_k=sum b_i^k. Exact expansion:
F=20-4B+B^2/2-(4+B/2)U_2+U_2^2/8+6U_3-(3/2)U_4.
The pointwise cap implies U_4<=q U_3. Cauchy–Schwarz gives U_2^2<=B U_3. Therefore
F>=20-4B+B^2/2-(4+B/2)U_2+[1/8+(6-3q/2)/B]U_2^2.
Replace B by B0 in the decreasing first term and in the coefficients in the indicated monotone directions, then complete the square in U_2. The B=0 case follows directly. QED.

**[CONDITIONAL TYPE-E APPLICATION]** Choose twenty disjoint strict deep edges with endpoints m_i +/- z_i; let a_i=||m_i||^2<1/4, A=sum a_i<=A0=383/504, and Z=sum z_i z_i^T. For arbitrary unit x, e_i=(x.z_i)^2, E=sum e_i=x^T Z x. Project to x-perp (dimension 4), obtaining t_i=1-a_i-e_i. The lemma applies with B0=A0+E and q=1/4+E, giving

Rvar(E)=20-4(A0+E)+(A0+E)^2/2
 -(4+(A0+E)/2)^2/[4(1/8+(45/8-3E/2)/(A0+E))].

The positive S^3 Gegenbauer expansion yields
sum_(i<j) s_ij^2(4s_ij^2-t_i t_j)>=F>=Rvar(E),
where s_ij is the projected inner product. Rvar is strictly decreasing for 0<=E<=2149/5000: B0<4; the positive numerator of its subtracted quotient increases and the denominator decreases.

**[RETAINED UPPER INEQUALITIES — proof dependency]** Put J=(27/20)E+(17/5)E^2+E^3/2, Ball=19A+57E+(19/10)E^2, Bcore=3A+9E+2E^2, Bpath=2A+(21/4)E+E^2, qa=(3+2E)^2/16, qs=(5+4E)^2/64. The earlier weighted quartic lemma gives
La=Ball/4+(1+E/2)J+(qa-1/4)Bcore+qa(5+4E)D
for arbitrary Type-E matchings, with D=sum positive raw projective defects. For singleton exceptions use
Ls=Ball/4+(1+E/2)J+(qs-1/4)Bcore+qs(9/2+4E)D.
For canonical path-only support replace Bcore by Bpath to obtain Lp.
These upper polynomials increase in A,E,D>=0.

**[EXACT CONDITIONAL CERTIFICATES]** In each row Rvar(E0)-L(A0,E0,D0) is the indicated strictly positive rational, contradicting E<=E0:

| Branch | E0 | D0 | Positive gap |
|---|---|---|---|
| General, coarse D | 213/1000 | 3/2 | 2068181855076531043/344643516000000000000 |
| General, global D | 843/2500 | 1780062775/4032758016 | 11637056493033844209773651/3622627761942656250000000000 |
| Singleton, coarse D | 179/500 | 3/4 | 38581113578514221/41497800750000000000 |
| Singleton, global D | 3901/10000 | 1780062775/4032758016 | 347727676502590567436420711/149315820383520000000000000000 |
| Canonical path | 2149/5000 | 366383/1016064 | 84433297068480293813057/256498966710000000000000000 |

Thus **[PROVED EXACTLY, CONDITIONAL ON THE RETAINED TYPE-E INPUTS]** any mass-selected matching satisfying the global defect budget has lambda_min(Z)>0.3372, without requiring canonical selection. A singleton matching with global defect budget has lambda_min(Z)>0.3901. A mass-selected canonical singleton path matching has lambda_min(Z)>0.4298. These improve the previous respective bounds 0.297, 0.343, 0.375.

**[OPEN]** Type E is not eliminated. No proof that the mass-selected matching is canonical, no global extension of the rational F3 paths, and no D5 six-cycle/exception identification is claimed. Types C, D, generic e>=27 and non-isolated cases remain open. The exact Type-E constants remain M(F3)<=89, M(P)>=S/2-28/3, A<=383/504.

A full proof package and exact verifier are available in the companion artifact; see also research/verify_typeE_variance_aware_quartic_noncollapse_2026_11_02.py.
