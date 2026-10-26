# Type E: exact outside-sixteen frame gap 3/16

Date: 2026-10-25. **[PROVED EXACTLY]** Standalone sixteen-vector theorem. **[CONDITIONAL ON RETAINED TYPE-E CERTIFICATES]** Type-E corollary. **[OPEN]** Type-E exclusion and the five-dimensional kissing number.

## Theorem

Suppose sixteen vectors \(z_i\in\mathbb R^5\) satisfy
\[
\|z_i\|^2=1-a_i,\quad 0\le a_i\le1/4,\quad
\sum_i a_i\le383/504,\quad |z_i\cdot z_j|\le1/2\ (i\ne j).
\]
Then
\[
\boxed{F_O=\sum_{i=1}^{16}z_i z_i^T\succ (3/16)I_5.}
\]
This improves the retained \(I_5/6\) bound by 12.5%, without a D5 labeling or a generic SDP.

## Weighted four-dimensional inequality

Assume a unit \(x\) has \(B=\sum_i(x\cdot z_i)^2\le3/16\). Define \(q_i=(x\cdot z_i)^2\), \(c_i=1-a_i\), \(w_i=z_i-(x\cdot z_i)x\), \(b_i=\|w_i\|^2=c_i-q_i\), and \(p_{ij}=\sqrt{q_iq_j}\). We have \(b_i\ge9/16>0\). On \(S^3\),
\[
f(t)=t^4-t^2/4=\tfrac1{16}C_0^{(1)}(t)+\tfrac18C_2^{(1)}(t)+\tfrac1{16}C_4^{(1)}(t).
\]
The positive-definite Gegenbauer kernel, with weights \(b_i^2\), gives
\[
\sum_{i<j}\left[(w_i\cdot w_j)^4-\tfrac{b_ib_j}{4}(w_i\cdot w_j)^2\right]
\ge R(b):=\frac{(\sum_i b_i^2)^2}{32}-\frac38\sum_i b_i^4.
\]
The derivative \(\partial R/\partial b_i\le8/9\) on the unit cube, hence \(R(b)\ge R(c)-(8/9)B\).

## Exact deficit/projection spectral lemma

For all admissible nonnegative \(a_i,q_i\),
\[
\boxed{\sum_{i<j}(a_i+a_j)\sqrt{q_iq_j}\le(27/25)\sum_iq_i.}
\]
Indeed, put \(r_i=\sqrt{q_i}\) and \(M(a)_{ii}=0\), \(M(a)_{ij}=(a_i+a_j)/2\). The left side is \(r^TM(a)r\). Its top eigenvalue is coordinatewise nondecreasing for nonnegative \(a\), convex in \(a\), and invariant under permutations. Filling the deficit budget and applying majorization reduces the maximum to
\[
a^*=(1/4,1/4,1/4,5/504,0,\ldots,0).
\]
For groups of sizes \((3,1,12)\), the quotient of \(M(a^*)\) is
\[
K=\begin{pmatrix}
1/2&131/1008&3/2\\
131/336&0&5/84\\
3/8&5/1008&0
\end{pmatrix}.
\]
All other eigenvalues are \(-1/4\) (twice) or \(0\) (eleven times). With \(D=\mathrm{diag}(3,1,12)\), the symmetric matrix \(D((27/25)I-K)\) has leading principal minors
\[
87/50,\qquad121870727/70560000,\qquad22005127/73500000,
\]
all positive. Thus \(\lambda_{\max}(M(a))<27/25\), proving the lemma.

## Improved quartic summation

Let \(h_{ij}(t)=t^4-(b_ib_j/4)t^2\). From \(|w_i\cdot w_j|\le1/2+p_{ij}\), convexity as a function of \(t^2\), and \(h_{ij}(1/2+p_{ij})\ge0\), one has \(h_{ij}(w_i\cdot w_j)\le h_{ij}(1/2+p_{ij})\). Writing \(\Delta_{ij}=c_iq_j+c_jq_i-q_iq_j\in[0,q_i+q_j]\) and expanding,
\[
\begin{aligned}
h_{ij}(w_i\cdot w_j)\le&
(1-c_ic_j)/16+(q_i+q_j)/16\\
&+p_{ij}/4+(a_i+a_j)p_{ij}/4
+(q_i+q_j)p_{ij}/4\\
&+(3/2)p_{ij}^2+(q_i+q_j)p_{ij}^2/4
+2p_{ij}^3+p_{ij}^4.
\end{aligned}
\]
For \(B=\sum q_i\), the following are elementary:
\[
\begin{array}{c|c}
\text{sum over }i<j&\text{upper bound}\\
q_i+q_j&15B\\
p_{ij}&15B/2\\
(a_i+a_j)p_{ij}&27B/25\\
(q_i+q_j)p_{ij}&3B^2\\
p_{ij}^2&B^2/2\\
(q_i+q_j)p_{ij}^2&B^3\\
p_{ij}^3&B^3/4\\
p_{ij}^4&B^4/8
\end{array}
\]
For the fourth bound, put \(S_2=\sum q_i^2\). Cauchy gives
\[
\sum_{i<j}(q_i+q_j)p_{ij}
=(\sum q_i^{3/2})(\sum\sqrt{q_i})-S_2
\le4B\sqrt{S_2}-S_2\le3B^2.
\]
The other bounds follow by Cauchy, \(p_{ij}\le B/2\), and direct summation. With \(U(c)=\sum_{i<j}(1-c_ic_j)/16\), the weighted LP inequality therefore requires
\[
D(a):=R(c)-U(c)\le
\frac{14297}{3600}B+\frac32B^2+\frac34B^3+\frac18B^4. \tag{*}
\]

## Exact contradiction

Writing \(A=\sum a_i\), \(S_k=\sum a_i^k\), the symmetric polynomial is
\[
32D(a)=64-46A+5A^2-4AS_2-41S_2+S_2^2+48S_3-12S_4.
\]
The earlier weighted-four-dimensional proof established that \(D\) decreases coordinatewise and is Schur-concave at fixed \(A\). For reference,
\[
\frac{\partial_iD-\partial_jD}{a_i-a_j}
=\frac{-8A+4S_2-82+144(a_i+a_j)-48(a_i^2+a_ia_j+a_j^2)}{32}<0
\]
on the permitted domain. Hence \(D(a)\ge D(a^*)=1665618603949/2064772104192\). The right side of (*) increases with \(B\ge0\) and at \(B=3/16\) equals \(31554331/39321600\). The exact difference is
\[
\boxed{
\frac{1665618603949}{2064772104192}
-\frac{31554331}{39321600}
=\frac{870478520203}{206477210419200}>0.
}
\]
Contradiction. Thus every unit \(x\) has \(x^TF_Ox>3/16\), proving the theorem.

## Type-E corollary and limits

**[CONDITIONAL ON RETAINED TYPE-E CERTIFICATES]** The sixteen outside-core selected deep edges satisfy the hypotheses. The retained two-sided safe-endpoint inequality gives
\[
2H_{184}\ge\operatorname{tr}(T_OF)+\operatorname{tr}(T_CF_O)
\ge\operatorname{tr}((T_O+T_C)F_O)>\tfrac3{16}A
\quad(A>0),
\]
so \(\boxed{H_{184}\ge(3/32)A}\), strictly for \(A>0\). The existing energy-sensitive Q-rank bound is still stronger as an *absolute* lower bound on \(H_{184}\); this result improves frame coercivity, not Type-E exclusion.

**[OPEN]** No contradictory safe-slack upper bound or global D5 stability theorem is known. Type E, C, D, generic \(e\ge27\), and non-isolated branches remain open. **[UNCHANGED]** \(40\le\tau_5\le44\), \(M(F_3)\le89\), \(M(P)\ge S/2-28/3\), \(A\le383/504\); the \(e=23/24\) sparse classification remains conditional on \(\delta(G)\ge1\), and the 21-line zero-midpoint boundary exclusion remains based on Musin/Boyvalenkov.

Companion verifier: research/tau5_typeE_weighted_fourD_frame_gap_3over16_2026-10-25_verify.py.
