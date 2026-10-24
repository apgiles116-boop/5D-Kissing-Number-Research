# Type E: two-eigenspace inverse-frame obstruction

2026-10-24. **Status:** analytic exact theorem plus 59,049-case integer certificate; Type-E application **conditional** on retained isolated-center hypotheses. This is NOT a Type-E elimination.

## Hypotheses

Twenty deep edges have endpoints x_i^±=m_i±z_i, a_i=||m_i||² in [0,1/4], A=sum a_i<=383/504, and ||z_i||²=1-a_i. The isolated unit center u has q_i=(u·z_i)²<=1/4. Let Q_i=z_i z_i^T-(1-a_i)I/5, G_ij=tr(Q_iQ_j), G0 the exact 20-line D5 Q-Gram in any ordering, and d=||G-G0||_op. The spectrum of G0 is 1 (10), 3/2 (4), 0 (6).

## 1. Inverse-frame theorem (PROVED EXACTLY)

Let F:R^20 -> Sym_0(5) have columns Q_i. Write L and H for the orthogonal spectral projectors of G0 for eigenvalues 1 and 3/2, and U=L+H. If d<1, F restricted to ran(U) is an invertible 14x14 operator and

F_U^*F_U = UGU|ran(U) >= (1-d)L+(3/2-d)H.

For v=uu^T-I/5, ||v||²_F=4/5, b=F^*v=q+a/5-1/5*1, and U1=0. Inversion of positive definite operators gives the necessary inequality

**4/5 <= ||L(q+a/5)||²/(1-d)+||H(q+a/5)||²/(3/2-d).** (1)

This retains both distinct positive eigenvalues, unlike the previous full-kernel bound.

## 2. Explicit D5 spectral projectors (PROVED EXACTLY)

Index the ten K5 supports e={v,w}, each with signs ±. For y in R^20, put s_e=y_(e,+)+y_(e,-) and t_e=y_(e,+)-y_(e,-). Then

||Ly||² = (1/2) sum_e t_e²,

||Hy||² = (1/6) sum_(v=1)^5 [sum_(e containing v) s_e -(2/5)sum_e s_e]². (2)

The six-dimensional kernel consists of the global support-sum relation and five further centered-incidence relations. No identification with six exceptional Type-E pairs is claimed.

## 3. Rational finite certificate at d0=139/250

Set W=L/(1-d0)+H/(3/2-d0), B=383/504, r=5/504, C=3/16+r². W is PSD, so the maximum over q in [0,1/4]^20 is attained at q=x/4 with binary x. Sign swaps within each K5 support preserve the optimization; it suffices to check 3^10=59,049 support occupancies s_e=x_(e,+)+x_(e,-) in {0,1,2}.

For each occupancy set T=sum_e s_e, deg_v=sum_(e containing v)s_e, D_v=5deg_v-2T, k=#{e:s_e=1}. In canonical sign orientation define

Q=29500k+185 sum_v D_v²;
n_(e,±)=925(D_v+D_w)±29500*1_{s_e=1}.

These are exact integers satisfying q^TWq=Q/419136 and (Wq)_(e,±)=n_(e,±)/104784. If t1>=t2>=t3>=t4 are the four largest nonnegative n values, the capped-simplex linear bound is

q^TWq+(2/5) max_a (Wq)^Ta <= N/132027840,
N=315Q+126(t1+t2+t3)+5t4.

The companion pure-Python checker exhaustively verifies **max N=104223500**, uniquely at all ten occupancies s_e=1.

The diagonal of W is D=1/[2(1-d0)]+1/[5(3/2-d0)], and its largest off-diagonal entry is c=1/[30(3/2-d0)]. For nonnegative a with sum a<=B and sum a²<=C,

a^TWa <= (D-c)C+cB².

Combining these bounds yields the exact certificate

(q+a/5)^TW(q+a/5) <= 2661669119/3327101568
= 4/5 - 60677/16635507840 < 4/5. (3)

If d<=d0, the inverse weights in (1) are bounded by those at d0. Thus (1) contradicts (3), proving:

**CONDITIONAL THEOREM: ||G_Q-G_D5||_op > 139/250 = 0.556** for every ordering of G0 under the retained isolated-center Type-E assumptions.

The previous exact bound was 4025531/7257600 ≈0.554664214065.

## 4. Scalar-relaxation equality witness

Take q_(e,+)=1/4, q_(e,-)=0 on all ten K5 supports. Place a=1/4 on three plus lines of a four-edge star, a=5/504 on its fourth plus line, and zero elsewhere. All scalar upper bounds in (3) are attained. This is **not** asserted to be a physical kissing-code configuration.

The corresponding scalar function is T(d)= [4499233/12700800]/(1-d)+[64159/31752000]/(3/2-d), crossing 4/5 at the smaller root of 101606400d²-208767034d+84664469=0 (approximately 0.5560020272). This root is a diagnostic, **not** an additional proved universal gap beyond 139/250.

## 5. Status

**PROVED EXACTLY:** inverse-frame lemma, spectral projectors, capped-simplex bound, rational finite certificate and scalar equality witness.

**PROVED CONDITIONALLY:** spectral separation >139/250 for retained isolated-center Type-E assumptions.

**CONDITIONAL ON A D5 LABELING:** if G-G0=R+E, E has only six core-core off-diagonal entries, and eta=max|E_ij|, then ||R||_op+3eta>139/250.

**OPEN:** Type-E elimination, global D5 proximity/labeling, physical q/z coupling, Types C/D, generic e>=27, and non-isolated branches.

**UNCHANGED:** 40<=tau_5<=44; M(F3)<=89; M(P)>=S_F3/2-28/3; A<=383/504; zero-midpoint 21-line exclusion. Sparse e=23/24 classification is conditional on delta(G)>=1.

Verifier: research/tau5_typeE_two_eigenspace_inverse_gap_2026-10-24_verify.py.
