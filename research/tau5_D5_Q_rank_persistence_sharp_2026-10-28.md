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
\lambda_{16}>31/800=2(1/10)^2+(3/10)(1/4)^2,
\]

equivalent to sqrt(149)<489/40, proved by rational squaring. Therefore

\[
\boxed{\epsilon\le1/10,\quad b\le1/4\quad\Longrightarrow\quad
\operatorname{rank}T_Y\ge\operatorname{rank}T_X.}\tag{3}
\]

In rank-14 rounded cases, rank(T_Y)=14 and nullity(T_Y)=2. In rank-13/12 cases only the respective lower-rank bounds are asserted. At epsilon=1/10, the exact energy threshold is b<sqrt((10/3)(lambda_16-1/50)) ~0.256074333, so b<=1/4 is a convenient rational criterion.

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
