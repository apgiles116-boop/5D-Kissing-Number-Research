# Type E: joint range/kernel Q-frame bound and a stronger isolated-center gap

Date: 2026-10-23. **Proof status: exact conditional theorem, not a Type-E elimination.**

## Hypotheses

Retain twenty deep-edge endpoint pairs `x_i^±=m_i±z_i` in R^5, `a_i=||m_i||²` with `0<=a_i<=1/4`, `A=sum a_i<=B=383/504`, `||z_i||²=1-a_i`, and an isolated unit center `u` with `q_i=(u.z_i)²<=1/4`. Put `Q_i=z_i z_i^T-(1-a_i)I/5`, `G_ij=tr(Q_iQ_j)`, and let `G0` be any permutation of the exact twenty-line D5 Q-Gram. Its eigenvalues are 3/2 (4), 1 (10), 0 (6), and the all-ones vector is in its kernel. Set `d=||G-G0||_op`.

## Joint range/kernel frame lemma (PROVED)

Let `F:R^20 -> Sym_0(5)` have columns `Q_i`. Let `P` project onto `ker G0`, `U=I-P`. For `d<1`, `(F|ran U)^*(F|ran U)>= (1-d)I_14`. This is a square 14-dimensional full-rank operator, so for every traceless symmetric `v`,

    ||F^*v||² >= (1-d)||v||² + ||PF^*v||².

Take `v=uu^T-I/5` (norm squared 4/5), `b_i=tr(Q_i v)=q_i-(1-a_i)/5`, and `t=sum_i b_i`. Since `1/sqrt(20)` is a unit kernel vector,

    BOXED: sum_i b_i² >= (4/5)(1-d)+t²/20.             (1)

The extra kernel term was discarded in the earlier bound. For `d>=1` the final numerical conclusion is automatic.

## Exact scalar identity and optimization (PROVED)

Let

    S=sum_i [q_i(1/4-q_i)
             +(2/5)a_i(1/4-q_i)
             +(1/25)a_i(1/4-a_i)] >=0.

Direct expansion yields

    sum_i b_i² = 1/5+3A/50-(3/20)t-S.

Together with (1), completing the square gives

    BOXED: 40d >= 195/8-3A+50S+(5/2)(t+3/2)².      (2)

For any 20 numbers `0<=y_i<=1/4` with sum `Y`, let `r_Y=Y-floor(4Y)/4`. Capped-simplex concentration gives

    sum_i y_i(1/4-y_i) >= r_Y(1/4-r_Y).             (3)

Apply (3) separately to `a_i` and `q_i`, discarding the nonnegative mixed part of `S`. Write `h=sum q_i=4-A/5+t`. Then

    40d >= 195/8-3A+2r_A(1/4-r_A)
           +(5/2)(h-5/2+A/5)²+50r_h(1/4-r_h).     (4)

On each quarter-grid interval `h in [k/4,(k+1)/4]`, the last two terms have second derivative `5-100=-95`, so their minimum lies at a grid endpoint. For `0<=A<=383/504`, the nearest grid point to `5/2-A/5` is either `5/2` or `9/4`, with the switch at `A=5/8`. Therefore

    40d >= 195/8-3A+2r_A(1/4-r_A)
           +(5/2)min{(A/5)²,(1/4-A/5)²}.         (5)

The right side decreases strictly on `[0,B]`: the derivative of the first two A-dependent terms is at most `-5/2` on each quarter interval, while the final derivative has magnitude at most `1/8`. Continuity covers interval boundaries.

At `B=383/504=3/4+5/504`, (5) yields the exact rational theorem

    BOXED: ||G-G0||_op >= 56198549/101606400
                          = 0.5531004838277904... .            (6)

This holds for **every** permutation of the D5 Q-Gram, with no prior D5 proximity or labeling assumption. It improves the previous exact gap `3521297/8890560=0.396071451...`.

## Conditional six-exception consequence

For a *chosen* D5 labeling, if `G-G0=R+E` and `E` is supported on six off-diagonal entries in a four-core block, with `eta=max|E_ij|`, then `||E||_op<=3eta`, hence

    ||R||_op+3eta >= 56198549/101606400.

This is a **necessary lower bound**, not a contradiction or an upper bound obtained from the homogeneous positive defect.

## Status

**PROVED algebraically:** frame lemma, exact slack identity, capped-simplex concentration, concavity minimization, rational constant.

**CONDITIONAL theorem:** gap (6) under the stated isolated-center Type-E hypotheses.

**OPEN:** Type E elimination, global D5 proximity/labeling, Types C and D, generic e>=27 and non-isolated branches.

**UNCHANGED:** 40<=tau_5<=44; M(F3)<=89; M(P)>=S_F3/2-28/3; A<=383/504; sparse e=23/24 classification remains conditional on delta(G)>=1.

Verifier: `research/tau5_typeE_joint_range_kernel_center_gap_2026-10-23_verify.py`.
