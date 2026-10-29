# Type E: tensor-frame and center-contact quantization stability (2026-10-29)

**Proof status: [EXACT STANDALONE ALGEBRA; CONDITIONAL TYPE-E APPLICATION].** The 5D tensor identity and sorted capped-simplex identity are exact. The Type-E application assumes the retained mass/harmonic envelopes, conditional signed-Gram exclusion \(s<209/30\), and the earlier rational derivative bounds. None of those upstream certificates is reverified here. **No Type-E elimination. Global proved range remains \(40\le\tau_5\le44\).**

For twenty selected deep pairs \(u_i^\pm=m_i\pm z_i\), put \(a_i=\|m_i\|^2\), \(A=\sum a_i\), \(U=\sum a_i^2\), \(Q=\sum_{i<j}(z_i\cdot z_j)^2\), \(T=\sum z_i z_i^T\). Let \(v\) be the isolated-center unit vector, \(P=I-vv^T\), \(p_i=v\cdot m_i\), \(q_i=v\cdot z_i\), \(B=\sum p_i^2\), \(s_i=2(p_i^2+q_i^2)\), \(s=\sum s_i\). Each center contact is nondeep, hence \(0\le s_i\le1/2\). Set \(t=v^TTv=s/2-B\), \(r=PTv\), \(R=PTP\), and \(\beta=(20-A-t)/4\).

## Exact tensor identity [PROVED]

Orthogonal block decomposition of \(T\) gives
\[
\left\|T-\frac{\operatorname{tr}T}{5}I\right\|_F^2
=\frac54\left(t-\frac{\operatorname{tr}T}{5}\right)^2
+2\|r\|^2+\|R-\beta P\|_F^2.
\]
Consequently the global \(Q\)-frame identity refines *exactly* to
\[
\boxed{Q=30-3A+\frac{A^2}{10}-\frac U2+
\frac58\left(4-\frac A5-\frac s2+B\right)^2+
\|PTv\|^2+\frac12\|PTP-\beta P\|_F^2.}
\tag{1}
\]
The last two nonnegative tensor terms were previously discarded. They vanish precisely when \(v\) is an eigenvector of \(T\) and the restriction to \(v^\perp\) is scalar.

## Sorted capped-simplex stability [PROVED]

Sort \(s_i\) as \(y_1\ge\cdots\ge y_{20}\), and in \(13/2\le s<7\) put \(\rho=s-13/2\), \(t_*=y_{14}\), \(D_c=\sum_{i\le13}(1/2-y_i)\), \(E_c=\sum_{i\ge15}y_i\). Then \(t_*=\rho+D_c-E_c\), and the following is an **exact nonnegative-remainder identity**:
\[
\begin{aligned}
&\sum_i y_i(1-2y_i)-\rho(1-2\rho)\\
&=2\bigg[(\tfrac12-\rho)D_c+\rho E_c+
\sum_{i\le13}(\tfrac12-y_i)(y_i-t_*)+
\sum_{i\ge15}y_i(t_*-y_i)\bigg].
\end{aligned}
\tag{2}
\]
Let \(\sigma=(y_i)\) and \(\sigma_*=(1/2,\ldots,1/2,\rho,0,\ldots,0)\) with thirteen \(1/2\)'s and six zeros. On \(69/10\le s\le209/30\), \(\rho\in[2/5,7/15]\) and \(\|\sigma-\sigma_*\|_1=2\max(D_c,E_c)\). Thus
\[
\boxed{\sum_i s_i(1-2s_i)-\rho(1-2\rho)
\ge\frac1{30}\|\sigma-\sigma_*\|_1.}\tag{3}
\]
This is a quantitative *linear* center-contact quantization penalty, not an assertion of attainment.

## Exact harmonic/frame slack combination [CONDITIONAL TYPE E]

Retain \(D(x)=196x-644x^2+896x^3-448x^4\), \(E(s)=10+(35/64)(5s-32)^2\), \(c(x)=D^{-1}(43/3-(2595/256+D(x))/2)\), \(a(x)=1/2+x+c(x)\), \(u(x)=1/8+x^2+c(x)^2\), \(h=4-a(x)/5-s/2\), and
\[
F(x,s)=30-3a(x)+a(x)^2/10-u(x)/2+5h^2/8.
\]
The retained scalar certificates give \(A\le a(x)\), \(U\le u(x)\), and \(D(x)+E(s)+N_0\le15\), where
\(N_0=7\sum_i[(p_i+q_i)^2(1-4(p_i+q_i)^2)+(p_i-q_i)^2(1-4(p_i-q_i)^2)]\).
Let \(n_2(s)=7\rho(1-2\rho)\). The paired-center expansion gives the **exact nonnegative** remainder
\[
\begin{aligned}
R_N&:=N_0-n_2(s)+56B-\frac{56}{5}B^2\\
&=7\left[\sum_i s_i(1-2s_i)-\rho(1-2\rho)\right]
+112\sum_i(\tfrac12-s_i)p_i^2+
224\left(\sum_i p_i^4-\frac{B^2}{20}\right)\ge0.
\end{aligned}
\tag{4}
\]
Let \(R_0=15-D(x)-E(s)-N_0\ge0\), \(J=F+(D+E+n_2-15)/112\). Equation (1) and the envelope bounds give the exact decomposition
\[
\begin{aligned}
Q={}&J+\left(\frac54h-\frac12\right)B+\frac{29}{40}B^2+
\|PTv\|^2+\frac12\|PTP-\beta P\|_F^2\\
&+R_{AU}+\frac{R_N+R_0}{112},
\end{aligned}\tag{5}
\]
where \(R_{AU}=(a-A)(3-(a+A)/10)+(u-U)/2+
(5/8)[(h+(a-A)/5+B)^2-(h+B)^2]\ge0\).

On \(0\le x\le1/250\), monotonicity of \(a(x)\) and the certified enclosure \(c(1/250)<5427/100000\) give \(a(x)<55827/100000<67/120\). For \(s\le209/30\), therefore \(h>81/200\), so **the previously discarded linear coefficient is strictly positive**:
\[
\boxed{\frac54h-\frac12>\frac1{160}.}\tag{6}
\]

Let \(s_0=209/30\) and \(x_2\) be the small root \(D(x_2)=2509/6400\). The retained rational derivative checks give \(J_x>2/3\), \(J_s<-1/10\), and \(J(x_2,s_0)=F(x_2,s_0)\). Combining (3)-(6), on the critical rectangle \(x_2\le x\le1/250\), \(69/10\le s\le s_0\):
\[
\boxed{\begin{aligned}
Q\ge F(x_2,s_0)&+\frac23(x-x_2)+\frac1{10}(s_0-s)
+\frac1{160}B+\frac{29}{40}B^2\\
&+\|PTv\|^2+\frac12\|PTP-\beta P\|_F^2
+\frac1{480}\|\sigma-\sigma_*\|_1.
\end{aligned}}\tag{7}
\]

The existing conditional numerical floor \(Q>28.3965067\) is **unchanged**. The new content is quantitative tensor and contact-distribution rigidity: for \(\varepsilon=Q-F(x_2,s_0)\), one must have \(B<160\varepsilon\), \(\|PTv\|\le\sqrt\varepsilon\), \(\|PTP-\beta P\|_F\le\sqrt{2\varepsilon}\), and \(\|\sigma-\sigma_*\|_1\le480\varepsilon\).

**[OPEN]** The 13+1+6 center-contact pattern must be combined with the four \(F_3\) core pairs, sixteen isolated pairs, and 184 safe cross-pair inequalities to force a positive residual or a contradiction. Types C, D, generic \(e\ge27\), and non-isolated branches remain open. Do not regress to \(M(F_3)\le94\) or \(M(P)\ge S/2-343/32\).