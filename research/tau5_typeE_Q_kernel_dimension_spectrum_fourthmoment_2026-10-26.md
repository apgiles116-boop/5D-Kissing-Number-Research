# Type E: Q-kernel dimension audit, exact D5 spectrum, and universal fourth moment (2026-10-26)

**Proof status:** [PROVED EXACTLY] All general linear-algebra and D5 statements below. [CONDITIONAL] Applying the kernel-stability bound to Type E requires an independently justified D5 labeling and quantitative closeness. [OPEN] Type E exclusion and the exact value of tau_5.

## 1. Six Q-relations are generic, not a D5 certificate

For 20 vectors z_i in R^5, set r_i=||z_i||^2, P_i=z_i z_i^T, Q_i=P_i-(r_i/5)I. The maps L(c)=sum c_i P_i into Sym(5), and T(c)=sum c_i Q_i into Sym_0(5), have ranks at most 15 and 14. Thus dim ker L >=5 and dim ker T >=6. If rank L=15, then rank T=14 and their nullities are exactly 5 and 6. In this full-span case ker T/ker L is one-dimensional: T(c)=0 iff L(c)=(sum c_i r_i/5)I. Full span is generic (the D5 example below supplies a nonzero 15x15 minor). Hence **six Q-null directions, split as five trace-zero and one scalar-identity relation, are generic**. Only the *sparse coefficient pattern* of the D5 relations is special. Six exceptional core pairs must not be identified with six kernel directions by dimension counting.

## 2. Exact D5 spectrum and sparse relations

For each of the ten edges ij of K5, use z_ij^+ = (e_i+e_j)/sqrt(2) and z_ij^-=(e_i-e_j)/sqrt(2). The projectors satisfy P_ij^+ + P_ij^- = E_ii+E_jj and sum P_i=4I. Their 20x20 Q-Gram K0 has diagonal 4/5, entry 1/20 for distinct supports sharing one vertex, and -1/5 for other distinct pairs.

If B is the adjacency matrix of the line graph L(K5), then
K0 = I_20 - J_20/5 + (B tensor J_2)/4.
Since spec(B)={6^1,1^4,(-2)^5}, exactly
**spec(K0)={(3/2)^4,1^10,0^6}**.
Thus the smallest positive eigenvalue is exactly 1, tr K0=16, tr K0^2=19, and the rank-14 spectral variance is 19-16^2/14=5/7.

Let U be the unsigned vertex-edge incidence matrix of K5. Its rank is 5. A relation sum c_i P_i=0 forces equal coefficients on the + and - lines of each support (the off-diagonal matrix entries force this), leaving U t=0 on the ten supports. Alternating coefficients +1,-1,+1,-1 around any 4-cycle give an exact eight-line projector relation; the 15 four-cycles span this five-dimensional kernel. Every nonzero support graph in ker U has minimum nonzero degree at least two, so it has at least four support edges; equality forces a 4-cycle. Hence **eight is the minimum nonzero support size** of a D5 projector relation. The sixth Q-kernel relation is sum Q_i=0, independent of the five trace-zero ones.

## 3. Universal rank-14 fourth-moment inequality

For arbitrary 20 vectors in R^5, put
r_i=||z_i||^2, B=sum r_i^2, C=sum r_i^4,
H=sum_{i<j}r_i r_j(z_i.z_j)^2, and
S4=sum_{i<j}(z_i.z_j)^4.

The Q-Gram K is PSD, rank <=14, diagonal 4r_i^2/5, and off-diagonal (z_i.z_j)^2-r_i r_j/5. By Cauchy on its nonzero eigenvalues,
tr K^2 >= (tr K)^2/14 = 8B^2/175.
Expanding gives the exact universal polynomial constraint
**S4 >= (2/5)H + B^2/350 - (3/10)C**,
equivalently
sum_{i<j}[(z_i.z_j)^2-r_i r_j/5]^2 >= 4B^2/175-8C/25.

For D5, sum_{i<j}(z_i.z_j)^2=30, S4=15/2, the last left side is 31/10, its lower bound is 96/35, and the exact slack is 5/14. This is a valid additional fourth-moment polynomial constraint for the six-exception problem, but is not a Type-E contradiction.

## 4. Conditional quantitative kernel stability

Let K be the Q-Gram of twenty vectors indexed by a proposed D5 labeling and set epsilon=||K-K0||_op. If epsilon<1, Weyl's inequality and rank K<=14 force rank K=14. Let Pi and Pi0 project orthogonally onto ker K and ker K0. For v in ker K, K0v=(K0-K)v, while K0 has spectral gap 1 off its kernel. Therefore ||(I-Pi0)v||<=epsilon||v||. Both kernels are six-dimensional, hence **||Pi-Pi0||_op<=epsilon** by the principal-angle identity.

An explicit polynomial sufficient condition is
epsilon <= [sum_{i,j}((z_i.z_j)^2-(z_i^0.z_j^0)^2-(r_i r_j-1)/5)^2]^(1/2) <1.
Neither this closeness condition nor a D5 labeling follows from the retained Type-E hypotheses at present.

## 5. Status

[PROVED EXACTLY] The rank-nullity audit, D5 spectrum and 4-cycle classification, fourth-moment bound, and conditional spectral lemma have analytic proofs above and exact SymPy checks. [OPEN] No stronger Type-E midpoint bound is claimed: retain 1/99 < A <=383/504, M(F3)<=89, M(P)>=S/2-28/3, and twenty-edge mass >=2137/6. Types C, D, generic e>=27, and non-isolated branches remain open. Sparse e=23/e=24 classification remains conditional on minimum degree >=1. Global proved range stays **40<=tau_5<=44**.
