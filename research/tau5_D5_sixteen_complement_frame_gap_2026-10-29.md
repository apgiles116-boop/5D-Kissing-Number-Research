# D5 sixteen-line complement: global frame anisotropy gap (2026-10-29)

**[PROVED EXACTLY — STANDALONE LINEAR ALGEBRA]**. **[CONDITIONAL TYPE-E APPLICATION]** requires a certified D5 alignment of the sixteen isolated selected edges. **No Type-E elimination.** Global proved range: 40 <= tau_5 <= 44.

## Statement

The twenty projective D5 roots `r_ij^±=(e_i±e_j)/sqrt(2)` form a tight frame: `sum r_i r_i^T=4 I_5`. Choose any sixteen labels I and let J be the four omitted labels. Set `W=span{r_j:j in J}^perp`, `k=dim W`. Exhaustive exact rank enumeration of all 4845 choices gives **4015 with k=1, 830 with k=2**.

For twenty selected deep edges, `u_i^±=m_i±z_i`, put `a_i=||m_i||²`, `||z_i||²=1-a_i`, `A=sum a_i`, `x=sum_{i in I}a_i`, `T=sum z_i z_i^T`, `mu=(20-A)/5=4-A/5`, `V=||T-mu I||_F²`. Assume *only* the sixteen isolated normalized directions `y_i=z_i/sqrt(1-a_i)` have a signed D5 alignment, with

`eta²=sum_{i in I}(1-a_i)||y_i-r_i||²`.

The four core directions are **arbitrary**. Define `L=(max(0,sqrt(4-x)-eta))²` and `D=max(0,L-mu)`. Then

`V >= [5k/(5-k)] D²`,

`Q=sum_{i<j}(z_i.z_j)² >= 30-3A+A²/10-(1/2)sum a_i²+[5k/(2(5-k))]D².`

**Radial special case (eta=0):**

`V >= [5k/(5-k)](A/5-x)_+²`, with corresponding `Q` correction half as large.

## Proof

For every unit `w in W`, D5 tightness and the omitted-root orthogonality give `sum_{i in I}(w.r_i)²=4`. Thus `sum_{i in I}(1-a_i)(w.r_i)²>=4-x`. The actual weighted coefficient vector `(sqrt(1-a_i)(w.y_i))_{i in I}` differs from the reference vector by at most `eta` in Euclidean norm. The reverse triangle inequality gives `w^T T w>=L`; the four core summands are PSD and can only increase it.

Let P project onto W. For traceless `E=T-mu I`, `tr(PE)>=k(L-mu)`, and `||P-(k/5)I||_F²=k(5-k)/5`. Frobenius Cauchy-Schwarz gives `||E||_F² >= [5k/(5-k)](L-mu)_+²`. The exact frame identity `Q=30-3A+A²/10-(1/2)sum a_i²+V/2` proves the second bound. The coefficient is sharp for the abstract trace/Rayleigh matrix inequality, but no Type-E equality case is claimed.

## Exact rational evaluations (hypothetical parameters only)

At `A=383/504`, `x=1/250`, `eta=0`: for k=1 the Q correction is at least `86918329/6350400000 ≈ 0.01368706`; for k=2 it is at least `86918329/2381400000 ≈ 0.03649884`.

For a robust example, **if** `A>=1/2`, `x<=1/250`, and `eta<=1/100`, then `sqrt(4-x)>=2-x/2` yields `L>=(497/250)²`, `mu<=39/10`, and

`V >= 10621081/3125000000 > 0.00339`.

These conditions are *not* asserted for all Type-E codes.

## Proof status and next step

**[EXACT]** D5 tightness, complement rank counts, frame/Rayleigh inequality, Q correction and rational examples. See companion standalone exact verifier.

**[CONDITIONAL]** The required sixteen-line D5 alignment is not established in the residual low-center Type-E branch; upstream mass/harmonic/atlas certificates were not recertified here. Thus this is not an unconditional improvement of the Type-E Q floor.

**[OPEN]** Prove a sufficiently strong low-center D5 alignment bound, or replace it by a label-free spectral gap. Types C,D, generic e>=27 and non-isolated branches remain unresolved. Retain M(F3)<=89, M(P)>=S/2-28/3 and A<=383/504. Global proved range unchanged: **40<=tau_5<=44**.
