# Type E: singleton-contact 1/8 theorem and improved six-core certificate

**2026-10-25.** [PROVED EXACTLY] Universal singleton-contact cap and midpoint-sensitive stability. [CONDITIONAL ON RETAINED TYPE-E INPUTS] Six-core defect-square ceiling and 184-safe correlation floor. [OPEN] Type E elimination and any global upper-bound improvement.

## Setup

For the twenty selected disjoint deep edges, write unit endpoints \(x_i^\pm=m_i\pm z_i\), \(m_i\cdot z_i=0\), \(a_i=\|m_i\|^2<1/4\), \(\|z_i\|^2=1-a_i\), and \(A=\sum a_i\le383/504\). Every distinct endpoint pair has inner product at most \(1/2\); a deep pair has inner product strictly below \(-1/2\).

For a pair of selected edges, set \(r=|z_i\cdot z_j|\), \(d=(r-1/2)_+\), and \(c=m_i\cdot m_j\). The endpoint upper inequalities give \(c+r\le1/2\), so \(c\le-d\) if \(d>0\).

Retained Type-E inputs: at most six positive defects on the four-core quotient \(K_4\); \(D=\sum_{\rm core}d\le D_0=1780062775/4032758016\); \(A\le383/504\); raw squared-correlation floor \(L=8790283/317520\) with its nonnegative frame-variance remainder.

## 1. Singleton-contact cap [PROVED EXACTLY]

**Theorem.** If at most one of the four cross-endpoint pairs between two selected deep edges is deep, then
\[
\boxed{(|z_i\cdot z_j|-1/2)_+\le1/8.}
\]
For actual strict-deep selected edges and positive defect the inequality is strict.

**Proof.** For \(d>0\), reorient \(z_j\) to make \(z_i\cdot z_j=1/2+d\). The two cross-endpoint inner products with opposite endpoint-sign product have average \(c-r\). At most one is deep, hence one is at least \(-1/2\), and the other is at least \(-1\) because both endpoints are unit vectors. Therefore \(c-r\ge-3/4\). But \(c\le-d\), \(r=1/2+d\), so \(c-r\le-1/2-2d\). Thus \(d\le1/8\).

Equality requires one cross-endpoint pair to be antipodal, \(x_i^\sigma=-x_j^\tau\). Since the selected edge \(i\) is strictly deep, \(x_i^{-\sigma}\cdot x_i^\sigma<-1/2\), hence \(x_i^{-\sigma}\cdot x_j^\tau>1/2\), contradicting kissing feasibility. QED.

This improves the previous singleton cap \((\sqrt2-1)/2\approx0.20710678\) to \(1/8=0.125\), without a \(D_5\) labeling or SDP.

## 2. Midpoint-sensitive stability [PROVED EXACTLY]

The unique deep cross-contact dot \(t\) obeys \(t\le-1/2-4d\); consequently
\[
\|x_i^\sigma+x_j^\tau\|^2=2+2t\le1-8d.
\]
For the other endpoint of selected edge \(i\), kissing feasibility gives
\[
x_i^{-\sigma}\cdot(x_i^\sigma+x_j^\tau)\le(2a_i-1)+1/2=2a_i-1/2.
\]
Cauchy gives the lower bound \(-\sqrt{1-8d}\). Thus, symmetrically in \(i,j\),
\[
\boxed{a_i,a_j\ge1/4-\tfrac12\sqrt{1-8d}.}
\]
Since \(0\le a_i,a_j<1/4\), the equivalent polynomial inequalities are
\[
\boxed{d\le3/32+a_i/4-a_i^2/2,\qquad
d\le3/32+a_j/4-a_j^2/2.}
\]
These are exact second-order, local, midpoint-sensitive constraints for a future four-core Gram/KKT certificate.

## 3. F3 quotient and exact six-defect certificate [CONDITIONAL]

The retained \(F_3\) edge set is \(\{02,04,05,14,17,23,27,36,56,57\}\). Its three perfect matchings yield quotient contact multiplicities \([1,1,1,1,1,1]\) once and \([0,1,1,1,1,2]\) twice. In the latter pattern, the zero- and double-contact quotient pairings are disjoint.

Retain the exact lifted-triangle inequality for adjacent defects:
\[
P(x,y)=x+y+4(x^2+y^2-xy)-1/2\le0.
\]

**Theorem.**
\[
\boxed{\sum_{\text{six core}}d_{ij}^2<19/250=0.076.}
\]

If all six defects are at most \(1/8\), capped-simplex concentration gives
\[
Q\le3/64+(D_0-3/8)^2
=0.05128407152704816\ldots<19/250.
\]

Otherwise a unique double-contact pairing has defect \(x>1/8\), its opposite defect is zero, and the other four singleton defects \(y_k\) satisfy \(y_k\le1/8\), \(\sum y_k\le D_0-x\), and \(P(x,y_k)\le0\). For \(x\in[1/8,1/4]\), the nonnegative root is
\[
c(x)=\frac{4x-1+\sqrt{9-24x-48x^2}}8,
\]
and \(C(x)=\min(1/8,c(x))\) is nonincreasing. On any rational interval \([l,h]\), the exact capped-simplex bound is
\[
Q\le h^2+\Phi_4(C(l),D_0-l),
\]
where \(\Phi_4(C,R)=kC^2+(R-kC)^2\) for \(k=\lfloor R/C\rfloor<4\), and \(4C^2\) if \(R\ge4C\).

The companion Python verifier uses only integer arithmetic and fractions, with outward integer-square-root bounds for \(C(l)\). An adaptive subdivision produces **20 contiguous rational intervals covering \([1/8,1/4]\)**; every bound is strictly below \(19/250\). Worst certified interval bound: \(0.07598232749642492\ldots\). This is an exact finite certificate, not floating-point optimization.

## 4. Safe correlation transfer [CONDITIONAL]

For six candidate core pairings, \(r_{ij}^2\le1/4+d_{ij}+d_{ij}^2\). Therefore
\[
\boxed{\sum_{\text{184 safe}}(z_i\cdot z_j)^2>
\frac{12938492114773}{504094752000}
=25.6667859830705\ldots.}
\]
The nonnegative raw-frame variance \(\tfrac12\|\sum_i[z_i z_i^T-(1-a_i)I/5]\|_F^2\) may be retained on the right. This improves the preceding safe-mass floor by exactly \(1/1000\).

## Status

[PROVED EXACTLY] Singleton cap \(d<1/8\) for positive defects; midpoint-sensitive radical and polynomial stability.

[CONDITIONAL ON RETAINED TYPE-E INPUTS] \(Q<19/250\), improved 184-safe mass floor, finite rational verification.

[OPEN] Contradiction with the Type-E endpoint Gram constraints; Types C, D and generic \(e\ge27\); non-isolated branches; a global \(D_5\) labeling; global upper bound.

[RETAINED] \(M(F_3)\le89\), \(M(P)\ge S/2-28/3\), selected twenty-edge mass \(\ge2137/6\), \(A\le383/504\), audited zero-midpoint boundary exclusion, and \(40\le\tau_5\le44\). The sparse \(e=23,24\) classification remains conditional on \(\delta(G)\ge1\).

Verifier: research/tau5_typeE_singleton_eighth_2026-10-25_verify.py.
