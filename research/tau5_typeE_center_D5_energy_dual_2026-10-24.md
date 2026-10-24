# Type E: sharp isolated-center / D5 midpoint-energy dual theorem (2026-10-24)

**Proof status:** [PROVED EXACTLY] the universal center-to-normalized-line inequality, a quartic dual minorant, and a sharp D5-template center-only energy bound with second-order stability. [CONDITIONAL] the D5-template application. [OPEN] any global Type-E elimination or D5 labeling.

## Universal center constraint

For a unit center (u) and unit endpoints (x_i^pm=m_ipm z_i), assume (m_icdot z_i=0), (a_i=|m_i|^2le1/4), (|z_i|^2=1-a_i), and (ucdot x_i^pmle1/2). Set (v_i=z_i/sqrt{1-a_i}) and (q_i=(ucdot v_i)^2). The center inequalities and orthogonality imply

[
sqrt{1-a_i}sqrt{q_i}-sqrt{a_i}sqrt{1-q_i}le	frac12.
]

By the elementary angle addition formula, this is equivalent to the necessary bound

[
q_ileleft(rac{sqrt{1-a_i}+sqrt{3a_i}}2ight)^2.
]

In particular (q_ile3/4). Define (g(q)=0) for (qle1/4) and

[
g(q)=rac{1+2q-2sqrt{3q(1-q)}}4quad(qge1/4).
]

Then (a_ige g(q_i)), with sharpness for each admissible single center/endpoint-pair subsystem. Also (((q_i-1/4)_+)^2le a_i), sharply.

**Audit:** The actual isolated-center inequalities yield (ucdot m_i+|ucdot z_i|le1/2). They do NOT alone imply (|ucdot z_i|le1/2). Any earlier application of the latter raw cap must be treated as conditional unless an additional proof supplies it.

## Exact quadratic dual certificate

Let
[
alpha=rac{25(sqrt2-1)}{16},qquad
eta=rac74-rac{11sqrt2}{8},qquad
p(q)=alpha q^2+eta q.
]

**[PROVED EXACTLY]** (g(q)ge p(q)) on (0le qle1), with equality only at (q=0,2/5).

For (qle1/4), (p(q)le0=g(q)) since (alpha/4+eta=(87-63sqrt2)/64<0). For (qge1/4),

[
g''(q)=rac{sqrt3}{8[q(1-q)]^{3/2}}gesqrt3>2alpha=p''(q).
]

The functions have matching values and first derivatives at (q=2/5), so their difference is nonnegative by strict convexity. Consequently the following is universal, with no D5 assumption:

[
oxed{A=sum_i a_igealphasum_i(ucdot v_i)^4+etasum_i(ucdot v_i)^2.}
]

## Sharp D5-template consequence

**[PROVED EXACTLY, CONDITIONAL ON THE NORMALIZED D5 TEMPLATE]** If the 20 normalized lines are (v_{jk}^{pm}=(e_jpm e_k)/sqrt2), their center moments satisfy

[
sum q_i=4,qquad sum q_i^2=rac32+rac12sum_{j=1}^5u_j^4gerac85.
]

Therefore

[
oxed{Agerac92-3sqrt2=0.257359312880714854ldots.}
]

The constant is sharp for the **center-only** constraints: choose (u=(1,1,1,1,1)/sqrt5). Ten lines have (q=2/5), ten have (q=0). Assign (a=g(2/5)=9/20-3sqrt2/10) to the former and (a=0) to the latter, with each midpoint antiparallel to the projection of (u) perpendicular to its line. All center-to-endpoint inequalities hold with total energy exactly (9/2-3sqrt2). This is NOT a full 40-endpoint kissing configuration.

Let (R(q)=g(q)-p(q)ge0). The **exact second-order stability identity** is

[
oxed{
A-left(rac92-3sqrt2ight)
=sum_i[a_i-g(q_i)]+sum_iR(q_i)
+racalpha2sum_{j=1}^5(u_j^2-	frac15)^2.
}
]

It quantifies energy cost of center-coordinate imbalance and deviations from the D5 equality moments.

For arbitrary normalized (v_i), an attempted D5 labeling (w_i), and (E=sum_i|v_iv_i^T-w_iw_i^T|_F^2), the universal dual certificate also gives

[
A+rac{14sqrt2-11}{8}sqrt{20E}gerac92-3sqrt2.
]

This is columnwise/template conditional, not intrinsic Q-Gram control.

## Status

The result is compatible with the retained Type-E ceiling (Ale383/504); it does not eliminate Type E. The global proved range remains (40le	au_5le44). Retain (M(F_3)le89), (M(P)ge S/2-28/3), and the source-audited 21-line zero-midpoint exclusion. Types C, D, and generic (ege27) remain open.

**Next step:** insert the universal quartic center-energy inequality into the rank-five Gram polynomial model, and derive a labeling-free lower bound on its right-hand side from the six-exception structure.
