# Type E: sharp local nonlinear center-contact quantization (2026-10-29)

**Status: [PROVED EXACTLY — standalone capped-simplex inequality and sharpness]. [CONDITIONAL TYPE-E APPLICATION]** The application retains the upstream harmonic/mass, signed-Gram and derivative certificates of \`tau5_typeE_tensor_contact_stability_2026-10-29.md\`; those are not independently recertified here. No Type-E exclusion; global range remains **40 <= tau_5 <= 44**.

## Exact sharp local theorem

Let \`13/2 <= s < 7\`, \`rho=s-13/2\`, \`1/4 <= rho < 1/2\`. Sort twenty numbers \`0 <= y_i <= 1/2\` with sum \`s\` in decreasing order, and set
\[
x=(\underbrace{1/2,\ldots,1/2}_{13},\rho,\underbrace{0,\ldots,0}_{6}),\qquad
\delta=\sum_{i=1}^{20}|y_i-x_i|.
\]
Then
\[
\boxed{\sum_i y_i(1-2y_i)-\rho(1-2\rho)\ge(1-2\rho)\delta-\delta^2.}\tag{1}
\]
The bound is **sharp at every** \`0 <= delta <= 1/2-rho\`: transfer \`delta/2\` from one saturated coordinate to the residual coordinate, leaving all other coordinates fixed. The sorting remains valid and equality holds.

### Exact proof

Put \`D=sum_{i<=13}(1/2-y_i)\`, \`E=sum_{i>=15}y_i\`. The sum constraint yields \`y_14=rho+D-E\`, and \`delta=D+E+|D-E|=2M\` where \`M=max(D,E)\`. With \`h=x-y\`,
\[
\sum_i x_ih_i=(1/2-\rho)D+\rho E\ge(1/2-\rho)M
\]
because \`rho>=1/4\`. Also
\[
\|h\|^2\le D^2+(D-E)^2+E^2
=2(D^2+E^2-DE)\le2M^2=\delta^2/2.
\]
Since \`sum y_i=sum x_i\`,
\[
\sum_i y_i(1-2y_i)-\sum_i x_i(1-2x_i)
=4\sum_i x_ih_i-2\|h\|^2
\ge(1-2\rho)\delta-\delta^2.
\]
For the stated transfer, both intermediate inequalities are equalities. Thus the local first-order coefficient \`1-2rho\` is optimal.

## Conditional Type-E improvement

On the retained critical rectangle \`x_2<=x<=1/250\`, \`69/10<=s<=s_0=209/30\`, one has \`2/5<=rho<=7/15\`. The previously proved global linear inequality gives the contact concavity gap at least \`delta/30\`; (1) gives at least \`delta/15-delta^2\`. The exact remainder identity \`R_N\` in the previous tensor-contact note therefore yields
\[
\boxed{R_N/112\ge\frac1{16}\max\{\delta/30,\delta/15-\delta^2\}.}\tag{2}
\]
Consequently, **conditional on all retained upstream certificates**,
\[
\begin{aligned}
Q\ge F_*&+\frac23(x-x_2)+\frac1{10}(s_0-s)
+\frac1{160}B+\frac{29}{40}B^2\\
&+\|PTv\|^2+\frac12\|PTP-\beta P\|_F^2
+\frac1{16}\max\{\delta/30,\delta/15-\delta^2\}.
\end{aligned}\tag{3}
\]
Here \`F_*=F(x_2,s_0)\`; notation is as in the earlier note.

Let \`epsilon=Q-F_*\`. If \`0<=epsilon<1/14400\`, the old inequality gives \`delta<=480epsilon<1/30\`. In this interval the new quadratic dominates, and inversion gives
\[
\boxed{\delta\le\frac1{30}-\sqrt{\frac1{900}-16\epsilon}.}\tag{4}
\]
The leading small-\`epsilon\` estimate is \`delta<=240epsilon+O(epsilon^2)\`, improving the previous \`480epsilon\` factor by two. The numerical \`Q\` floor is **unchanged**; no realizability of the sharp capped-simplex example within Type E is claimed.

**[OPEN]** Type E and all other outstanding graph branches remain unresolved. In particular, no contradictory upper bound for the 184 safe pairings or inequality forcing \`A>383/504\` follows from this lemma.

Verifier: \`research/tau5_typeE_sharp_local_contact_quantization_2026-10-29_verify.py\`.
