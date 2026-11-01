# Type E: refined 16-line harmonic leakage and two-ray stability

**Date:** 2026-11-01. **[PROVED EXACTLY, CONDITIONAL ON RETAINED TYPE-E SAFE-WALSH AND MIDPOINT INPUTS]**. This improves the earlier 2026-11-01 weighted-harmonic leakage theorem; it does **not** eliminate Type E. Global proved range remains **40 <= tau_5 <= 44**.

## Setting and theorem

For the 16 isolated deep edges let \(z_i\in\mathbb R^5\), \(a_i=1-\|z_i\|^2\), \(0\le a_i\le1/4\), \(A_I=\sum a_i\le383/504\). The two-sided safe-Walsh constraints give \(|z_i\cdot z_j|\le1/2\) for distinct isolated indices.

**Theorem [PROVED EXACTLY].** For every 3-plane \(W\), \(\sum_i\|P_{W^\perp}z_i\|^2>4/5\). For every 4-plane \(W\), \(\sum_i\|P_{W^\perp}z_i\|^2>11/250\). Thus if \(Z_I=\sum_i z_i z_i^\top\) has descending eigenvalues \(\lambda_1,\ldots,\lambda_5\), then \(\lambda_4+\lambda_5>4/5\) and \(\lambda_5>11/250\). No D5 labeling, core coplanarity, or rank-13 hypothesis is needed.

## Weighted harmonic lower bound

For a \(d\)-plane \(W\), \(d=3,4\), set \(\ell_i=\|P_{W^\perp}z_i\|^2\), \(L=\sum\ell_i\), \(b_i=a_i+\ell_i\), \(B=A_I+L\), \(r_i=1-b_i\), \(w_i=P_W z_i\), \(s_{ij}=\sqrt{\ell_i\ell_j}\). Then \(|w_i\cdot w_j|\le1/2+s_{ij}\).

Use \(f(t)=t^4-t^2/4\), with nonnegative harmonic expansions
\[
f=\tfrac7{60}P_0+\tfrac{17}{42}P_2+\tfrac8{35}P_4\quad(d=3),\qquad
f=\tfrac1{16}U_0+\tfrac18U_2+\tfrac1{16}U_4\quad(d=4).
\]
Positive definiteness applied with weights \(r_i^2\) gives, for \(F_{ij}=(w_i\cdot w_j)^4-\tfrac14r_ir_j(w_i\cdot w_j)^2\),
\[
\sum_{i<j}F_{ij}\ge H_d(B)
=\frac{\alpha_d}{2}(16-2B+B^2/16)^2-\frac38 M(B),
\]
where \(\alpha_3=7/60,\alpha_4=1/16\) and \(M(B)=15+(1-B)^4\) for \(0\le B\le1\), \(M(B)=14+(2-B)^4\) for \(1\le B\le2\). The fourth-moment upper envelope follows by concentrating \(b_i\in[0,1]\) at fixed total \(B\).

## Improved upper envelope

Convexity of \(x(x-r_ir_j/4)\) on \(0\le x\le(1/2+s_{ij})^2\) gives
\[
F_{ij}\le (b_i+b_j)/16+(b_i+b_j)s_{ij}/4+(b_i+b_j)s_{ij}^2/4+s_{ij}/4+(5/4)s_{ij}^2+2s_{ij}^3+s_{ij}^4.
\]
The key improvement is to split \(b_i+b_j=(a_i+a_j)+(\ell_i+\ell_j)\), using \(a_i+a_j\le1/2\), rather than replacing the entire sum by \(1/2+L\).

For 16 nonnegative leakage masses, the following exact bounds hold:
\[
\begin{aligned}
&\sum_{i<j}s_{ij}\le(15/2)L,\qquad
\sum_{i<j}s_{ij}^2\le(15/32)L^2,\\
&\sum_{i<j}(\ell_i+\ell_j)s_{ij}\le2L^2,\quad
\sum_{i<j}(\ell_i+\ell_j)s_{ij}^2\le L^3/4,\\
&\sum_{i<j}s_{ij}^3\le L^3/8,\qquad
\sum_{i<j}s_{ij}^4\le L^4/16.
\end{aligned}
\]
The first two follow from AM-GM and Cauchy. For the third,
\(\sum_i\ell_i^{3/2}\sum_{j\ne i}\sqrt{\ell_j}
\le\sqrt{15}\sum_i\ell_i^{3/2}\sqrt{L-\ell_i}
\le(\sqrt{15}/2)L^2<2L^2\).
The fourth follows from \(\sum_i\ell_i^2(L-\ell_i)\le(L^2/4)\sum_i\ell_i\). The fifth follows from \(s_{ij}\le(\ell_i+\ell_j)/2\) and the fourth; the sixth from \(\ell_i\ell_j\le L(\ell_i+\ell_j)/4\) and the fourth.

Summing the pairwise envelope yields the **new polynomial upper bound**
\[
\sum_{i<j}F_{ij}\le U_{\rm new}(B,L)
=\frac{15}{16}B+\frac{45}{16}L+\frac{293}{256}L^2+\frac5{16}L^3+\frac1{16}L^4.
\]
Every feasible configuration therefore satisfies \(H_d(A_I+L)\le U_{\rm new}(A_I+L,L)\).

## Exact rational contradictions

For \(0\le B\le2\), differentiating the two pieces of \(M\) yields
\[
H_d'(B)=\alpha_d(16-2B+B^2/16)(-2+B/8)+\tfrac32(k+1-B)^3,
\]
where \(k=0\) on \([0,1]\) and \(k=1\) on \([1,2]\). The last term is at most \(3/2\). The polynomial \(U_{\rm new}\) is increasing in both nonnegative arguments.

If \(d=3,L\le4/5\), then \(B\le3931/2520<8/5\) and
\(H_3'(B)\le-(7/60)(64/5)(9/5)+3/2=-297/250<0\). Hence
\[
H_3(3931/2520)-U_{\rm new}(3931/2520,4/5)
=\frac{15739941658327447}{1238863262515200000}>0,
\]
contradicting the necessary inequality.

If \(d=4,L\le11/250\), then \(B\le50647/63000<81/100\) and
\(H_4'(B)\le-(1/16)(719/50)(1519/800)+3/2=-132161/640000<0\). Hence
\[
H_4(50647/63000)-U_{\rm new}(50647/63000,11/250)
=\frac{530015660962164281377}{129048256512000000000000}>0.
\]
This proves both leakage bounds.

## Conditional tomography corollary

**[PROVED EXACTLY, ADDITIONALLY CONDITIONAL ON RETAINED RANK-13 / TWO-RAY / FOUR-AMBIGUOUS-COPLANAR-CORE HYPOTHESES].** For the orthonormal missing-ray axes \(p,q\), put \(X=p^\top Z_Ip\), \(Y=q^\top Z_Iq\). Then \(X,Y>11/250\), \(X+Y>4/5\), so \((X-c)(Y-c)\ge0\), \(c=11/250\), implies
\[
XY>\frac{2079}{62500}.
\]
Using the retained core wedge/minor inequality \(\sum(\text{safe }2\times2\text{ minors})^2\ge(81/131072)X^2Y^2\) gives
\[
\sum(\text{safe }2\times2\text{ minors})^2
>\frac{350101521}{512000000000000}.
\]
For the rank-two safe \(16\times4\) squared-correlation matrix \(D\), \(\|D\|_F^2\le4\) then yields
\[
\sigma_2(D)>\frac{18711\sqrt2}{64000000}.
\]
These are stronger necessary conditions, **not** a Type-E exclusion.

**[VERIFIED LOCALLY]** Exact rational/SymPy verification of the harmonic identities, coefficient arithmetic, derivative margins, and conditional constants passed. **[OPEN]** An incidence-sensitive upper bound on safe minors or \(\sigma_2(D)\) remains missing. Types C,D, generic \(e\ge27\), and non-isolated branches remain open. Retain \(M(F_3)\le89\), \(M(P)\ge S/2-28/3\), \(A\le383/504\), the six-core defect bounds and Musin/Boyvalenkov zero-midpoint exclusion; sparse \(e=23/24\) classification still assumes \(\delta(G)\ge1\). Global proved range **40 <= tau_5 <= 44**.
