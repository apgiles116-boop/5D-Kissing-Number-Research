# Exact quadratic Q-perturbation and 16-line D5 rank persistence (2026-10-28)

**[PROVED EXACTLY — standalone frame theorem]** This note strengthens the 16-line Q spectral-atlas perturbation criterion. **[CONDITIONAL Type-E use]** Applying it requires an independently established rounded D5 labeling, alignment, and radial-energy bounds. No new Type-E branch is excluded. Global proved range: **40 <= tau_5 <= 44**.

## Exact quadratic identity

For x,y in R^5 with ||x||=1, ||y||²=1-a, a in [0,1], and d=||y-x||, put Q(u)=uu^T-(||u||²/5)I. Then

\[
\boxed{\|Q(y)-Q(x)\|_F^2=(2-a)d^2-\tfrac12d^4+\tfrac3{10}a^2.}\tag{1}
\]

Proof: traceless projection gives (1-a)²+1-2(x.y)²-a²/5; substitute x.y=1-(a+d²)/2. Thus for aligned frames X,Y with unit x_i, ||y_i||<=1, epsilon=||Y-X||_F, a_i=1-||y_i||², and b=sum a_i,

\[
\boxed{\|T_Y-T_X\|_{\rm op}^2\le \|T_Y-T_X\|_F^2
\le 2\epsilon^2+\tfrac3{10}\sum_i a_i^2
\le 2\epsilon^2+\tfrac3{10}b^2.}\tag{2}
\]

The earlier bound 2epsilon on the *unsquared* operator difference is unnecessarily weak. Independently the sharp Lipschitz constant of Q on the unit ball is 4/sqrt(5), via its derivative or traceless polarization.

## Sixteen-line D5 theorem

**[PROVED EXACTLY]** For any sixteen distinct D5 projective root lines X, the exact 17-orbit Q-Gram atlas has r=rank(T_X) in {12,13,14} and

\[
\sigma_r(T_X)^2\ge \lambda_{16}:=(13-\sqrt{149})/20.
\]

There are 3360 rank-14, 1440 rank-13, and 45 rank-12 templates. The key *exact* comparison is

\[
\lambda_{16}>31/800>4/125=(16/5)(1/10)^2.
\]

The first inequality is equivalent to sqrt(149)<489/40, verified by rational squaring. The **sharp global Lipschitz constant** of Q on the unit ball is 4/sqrt(5): differentiating gives
\[
\|DQ_u(h)\|_F^2=2\|u\|^2\|h\|^2+(6/5)(u\cdot h)^2\le(16/5)\|h\|^2.
\]
It is sharp in radial directions. Consequently
\[
\|T_Y-T_X\|_{\rm op}^2\le(16/5)\epsilon^2\le4/125<\lambda_{16}
\]
whenever epsilon<=1/10. Weyl's singular-value inequality proves the **stronger, no-energy-assumption** theorem
\[
\boxed{\epsilon\le1/10\ \Longrightarrow\ \operatorname{rank}T_Y\ge\operatorname{rank}T_X.}\tag{3}
\]
In 3360 rank-fourteen D5 templates, rank(T_Y)=14 and nullity(T_Y)=2. In the rank-thirteen/twelve templates only the corresponding rank lower bounds are asserted. This eliminates the earlier apparent 0.1 versus 0.099589 alignment gap.

**[SHARPER WHEN RADIAL ENERGY IS SMALL]** The quadratic identity (2) gives the more flexible condition
\[
2\epsilon^2+(3/10)b^2<\lambda_{16}.\tag{4}
\]
For example epsilon<=1/10 and b<=1/4 satisfy (4) since the left side is at most 31/800; this extra energy assumption is **not needed** for epsilon<=1/10. With b<1/2500, condition (4) permits epsilon<=7/50=0.14, a useful tolerance for future geometric rounding arguments. At epsilon=1/10 the exact energy threshold from (4) is b<sqrt((10/3)(lambda_16-1/50)) ~0.256074333.

## Quantitative near-seven consequence

**[PROVED EXACTLY — CONDITIONAL on earlier near-seven certificates]** The retained near-seven Type-E note gives the sixteen isolated projected directions b=x<1/2500 and aligned epsilon<1/10. Hence

\[
\|T_Y-T_X\|_{\rm op}^2<1/50+3/62500000<(71/500)^2.
\]

Exact rational-square comparisons also give sqrt(lambda_16)>199/1000. By singular-value perturbation,

\[
\boxed{\sigma_r(T_Y)>199/1000-71/500=57/1000.}\tag{4}
\]

For rank-14 rounded frames this yields the fourth-moment coercivity inequality for every nonzero traceless symmetric B:

\[
\boxed{\sum_{i=1}^{16}(y_i^T B y_i)^2>
(3249/10^6)\|B\|_F^2.}\tag{5}
\]

The near-seven branch was *already conditionally excluded* by a separate nine-versus-eight root-extension argument. This is improved conditioning, not a new elimination.

## Proof ledger

**[NEW EXACT]** Identities (1)-(2), rational criterion (3), and conditional consequence (4)-(5). Companion verifier checks the symbolic identity, all 4,845 16-line D5 subsets via 17 Weyl orbits, the sharp eigenvalue, and every rational comparison using exact SymPy arithmetic.

**[CONDITIONAL]** No uniform D5 rounding/alignment is established for residual low-center Type E s<209/30. The six exceptional core pairings have not been identified with D5 Q-kernel relations.

**[OPEN]** Residual Type E; Types C,D; generic e>=27; non-isolated branches; sparse e=23/24 classification without delta(G)>=1. Preserve M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, and the rigorous Musin/Boyvalenkov zero-midpoint boundary. Global proved range unchanged: 40<=tau_5<=44.

Verifier: research/tau5_D5_Q_rank_persistence_sharp_2026-10-28_verify.py.
