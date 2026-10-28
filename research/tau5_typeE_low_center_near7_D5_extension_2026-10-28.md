# Type E: exact near-seven low-center exclusion using sixteen D5 lines (2026-10-28)

**[NEW EXACT DERIVATION; CONDITIONAL TYPE-E BRANCH EXCLUSION]** Assuming the retained Type-E mass/harmonic certificates and the previously verified six-/seven-basis signed-Gram atlases, no Type-E configuration can have isolated-center second moment

\[
\boxed{\frac{209}{30}\le s=\sum_{w\ne v}(v\cdot w)^2\le7.}
\]

Combined with the preceding **conditional** exclusion of \(s\ge7\), this forces \(s<209/30\) in any surviving Type E. **This does not prove \(\tau_5=40\)**; the global proved range remains \(40\le\tau_5\le44\).

## 1. Exact low-center harmonic polynomial

Let \(m_i\pm z_i\), \(1\le i\le16\), be the sixteen isolated deep edges. Write \(x=\sum_I\|m_i\|^2\), \(D_I=\sum_I D(\|m_i\|^2)\), where \(D(a)=196a-644a^2+896a^3-448a^4\). Let \(N_0\) be Delsarte nondeep slack on the forty center contacts, \(R=N-N_0\) the slack on the other **754** nondeep contacts, and \(E=(35/6)\|T\|_F^2+14K_4\). The retained Type-E mass identity gives

\[
D_I+N_0+R+E\le15. \tag{1}
\]

Set \(s=7-d\), \(0\le d\le1/30\), \(q=s-36/5=-1/5-d\). The capped-simplex center quantization lemma gives \(N_0\ge n(d)=7d(1-4d)\). The degree-two/four harmonic center row gives

\[
E\ge\frac{175}{24}q^2+
\frac{147}{4}\left(\frac57+\frac5{12}q+\frac{N_0}{28}\right)^2.
\]

The right side increases with \(N_0\) on this interval. Substituting \(n(d)\) and simplifying *exactly* yields

\[
\boxed{E+N_0\ge\frac{955}{64}+g_-(d),\qquad
g_-(d)=\frac{7d}{16}(84d^3+28d^2-151d+5).} \tag{2}
\]

The cubic decreases on \([0,1/30]\), and its endpoint value is \(1/1125>0\). Therefore

\[
\boxed{D_I+R+g_-(d)\le5/64,\quad R\le5/64,\quad x<1/2500.} \tag{3}
\]

The last inequality follows from \(D_I\ge D(x)\) and \(D(1/2500)>5/64\), with the preliminary \(D(a)\ge84a\) establishing \(x<1/4\). **Do not infer \(N\le5/64\)**: the center slack \(N_0\) can be larger.

## 2. Exact rounding of the sixteen isolated directions

For each noncenter nondeep contact, \(f(t)=7t^2(1-4t^2)\le R\le5/64\). Therefore \(|t|<1/9\) or \(12/25<|t|\le1/2\). Since \(2\sqrt{x}<1/25\), the four contacts between two isolated deep edges share a low/high category and have alternating signs when high. Round the true \(16\times16\) Gram \(G_{16}=\operatorname{Gram}(z_1,\ldots,z_{16})\) to \(\widehat G_{16}\) with diagonal 1 and off-diagonal \(0,\pm1/2\).

The exact Walsh transform and the contact inequality \(f(t)\ge(539/81)\rho(t)^2\), where \(\rho(t)=\min(|t|,1/2-|t|)\), give

\[
\boxed{\|G_{16}-\widehat G_{16}\|_F^2
\le\frac{81}{1078}R+x^2
<\frac{158207437}{26950000000}<\frac1{169}.} \tag{4}
\]

Let \(M=2\widehat G_{16}\). Then \(M\) is integral, with diagonal 2 and off-diagonal \(0,\pm1\), and is within squared Frobenius distance \(4/169<1/16\) of the PSD rank-at-most-five matrix \(2G_{16}\).

**[EXACT — USING RETAINED ATLAS COMPLETENESS]** The principal-minor/integrality argument with Frobenius error \(<1/13\) makes every principal minor of order 8 or higher vanish, so \(\operatorname{rank}M\le7\). For a nonsingular principal 7-block the determinant is even and the same bound gives absolute determinant \(<3\); hence it is \(\pm2\). The previous exact seven-basis atlas at the *larger* squared-error threshold \(158205281/3368750000\) leaves only two characteristic polynomials:

\[
\begin{aligned}
p_1(t)&=t^7-14t^6+77t^5-210t^4+292t^3-186t^2+37t-2,\\
p_2(t)&=t^7-14t^6+76t^5-202t^4+271t^3-166t^2+33t-2.
\end{aligned}
\]

For both, exact sign variation of \(p_j(t+4/25)\) is 6. Their second-smallest eigenvalue is therefore \(>4/25\), requiring squared distance \(>16/625\) from the PSD rank-five cone, larger than \(4(158207437/26950000000)\). Thus \(\operatorname{rank}M\le6\).

**[NEW EXACT FINITE ENUMERATION]** The retained six-basis atlas has only three switching-normalized bases admitting a ten-clique of Schur-complement columns. An independent exhaustive enumeration of all **4,096** maximal ten-cliques (1,024, 1,024 and 2,048) shows that every resulting sixteen-vertex matrix has the *same* nonzero characteristic polynomial

\[
q_6(t)=t^6-32t^5+411t^4-2676t^3+9091t^2-14484t+7161.
\]

The sign variation of \(q_6(t+1/2)\) is 6, so all six nonzero eigenvalues exceed \(1/2\). Such a rank-six matrix has squared distance \(>1/4\) from PSD rank five, contradicting (4). Hence \(\operatorname{rank}M\le5\).

The retained universal small-rank integer atlas (order at least 13) makes \(M\) **PSD of rank exactly five**. The ADE classification then identifies its sixteen projective root lines as a subset of \(D_5\): \(A_5\) has only 15 root lines. This is a labeling of the **rounded** directions, not the true ones.

## 3. New exact 16-line D5 extension atlas and alignment

**[NEW EXACT FINITE CERTIFICATE]** The \(\binom{20}{4}=4845\) omitted four-line subsets of \(D_5\) form **17** Weyl-group orbits. In each representative, the three-term integer root relations span the eleven-dimensional kernel of the retained \(5\times16\) root matrix \(R_D\). For \(c\in\{-1,0,1\}^{16}\) of the form \(c=R_D^\top t_0\), the permitted squared norms are

\[
\|t_0\|^2\in\{0,1,5/4,2,3,13/4\}.
\]

The norm-two solutions are **exactly the eight signed omitted roots**. The exact verifier enumerates 51 or 53 feasible columns per orbit.

For the rounded unit frame \(X\), the full \(D_5\) frame identity and Gershgorin bound for four omitted lines give

\[
\frac32 I_5\preceq XX^\top\preceq4I_5.
\]

For the true frame \(Y=[z_1,\ldots,z_{16}]\), polar alignment using (4) yields an orthogonal \(U\) such that

\[
\boxed{\|Y-UX\|_F<1/10.} \tag{5}
\]

Explicitly, with \(\epsilon=\|Y^\top Y-X^\top X\|_F<1/13\), the least singular value of the least-squares factor exceeds \(h=\sqrt{1-2\epsilon/3}>24/25\), and

\[
\|Y-UX\|_F\le\epsilon\left(\frac4{3(1+h)}+\frac1{\sqrt3 h}\right)<1/10.
\]

## 4. Nine external unit vectors versus eight missing signed roots

For each of the **eight** \(F_3\) endpoints \(w\), its 32 contacts with the sixteen isolated deep edges are noncenter nondeep contacts. Round its sixteen \(w\cdot z_i\) correlations to \(b_w\in\{0,\pm1/2\}^{16}\). The two-contact Walsh bound gives

\[
e_w^2:=\|Y^\top w-b_w\|^2
\le\frac12\sum_{\text{32 contacts}}\rho(t)^2
\le\frac{81}{1078}R<1/64. \tag{6}
\]

The center \(v\) needs a separate estimate. The exact harmonic lower bound from (2), without the added \(N_0\), gives \(N_0\le N<281/1000\) throughout the interval. For each center contact set \(r_j=\min(t_j^2,1/4-t_j^2)\). As \(f(t_j)=7r_j(1-4r_j)<281/1000<21/64\), each \(r_j<1/16\). Hence

\[
J:=\sum_{40}r_j\le\frac4{21}N_0<\frac{281}{5250}.
\]

Let \(k\) be the number of center contacts nearer \(\pm1/2\) than zero. Since \(|4s-k|\le4J<1/4\) and \(4s\in[418/15,28]\), necessarily **\(k=28\)**. Let \(L\) sum \(r_j\) over low contacts and \(H\) over high contacts. Then \(H-L=d\ge0\), so \(L\le J/2\), \(H\le J\). Low contacts have \(\rho^2=r_j\); high contacts satisfy \(\rho^2\le(4/3)r_j^2\). The center's rounded sixteen-correlation error is therefore

\[
\boxed{e_v^2\le\frac12\left(L+\frac43H^2\right)
\le\frac J4+\frac23J^2
<\frac{2528719}{165375000}<1/64.} \tag{7}
\]

Its 32 contacts with the isolated edges round in opposite pairs because the center low/high categories are separated by more than \(2\sqrt{x}<1/25\).

For each of the **nine** unit vectors \(w\in\{v\}\cup V(F_3)\), set \(t=\sqrt2\,U^\top w\), \(c=2b_w\), and \(R_D=\sqrt2X\). From (5)-(7),

\[
\|c-R_D^\top t\|<2(1/8+1/10)=9/20.
\]

Every three-term integer root relation \(q\) has \(\|q\|=\sqrt3\), so \(|q^\top c|<9\sqrt3/20<1\). By integrality it is zero. Since those relations span \(\ker R_D\), there is a unique \(t_0\) with \(c=R_D^\top t_0\). Since \(R_DR_D^\top\ge3I_5\),

\[
\|t-t_0\|<\frac9{20\sqrt3}<\frac{27}{100}.
\]

The permitted norm list has a gap \(>27/100\) between \(\sqrt2\) and every other norm. Since \(\|t\|=\sqrt2\), necessarily \(\|t_0\|^2=2\). Thus each of the nine original unit vectors lies within \(27/(100\sqrt2)\) of one of the **eight signed omitted roots**, after applying \(U\). Two vectors in the same neighborhood would have inner product \(>1/2\), violating the kissing-code condition. Nine cannot occupy eight neighborhoods.

\[
\boxed{\text{Type E with }209/30\le s\le7\text{ is impossible, conditionally.}}
\]

Together with the previously conditional high-center exclusion \(s\ge7\), any surviving Type E must have \(s<209/30\).

## Proof-status ledger

**[PROVED EXACTLY, CONDITIONAL ON RETAINED INPUTS]** Equations (2)-(7), the sixteen-direction rounding, the polar alignment, and the nine-versus-eight contradiction.

**[NEW FINITE CERTIFICATES]** 4,096 maximal rank-six sixteen-vertex extensions share the single polynomial \(q_6\); 4,845 omitted \(D_5\) four-line subsets form 17 Weyl orbits with triangle-kernel rank 11 and exactly eight signed norm-two missing-root extensions. These finite checks still rely on the prior six-/seven-basis atlas completeness.

**[OPEN]** Type E with \(s<209/30\), Types C and D, generic \(e\ge27\), non-isolated branches, and sparse \(e=23,24\) classification without \(\delta(G)\ge1\). Retain \(M(F_3)\le89\), matching \(M(P)\ge S/2-28/3\), \(A\le383/504\), and the Musin/Boyvalenkov zero-midpoint theorem. **Global proved range remains \(40\le\tau_5\le44\)**.
