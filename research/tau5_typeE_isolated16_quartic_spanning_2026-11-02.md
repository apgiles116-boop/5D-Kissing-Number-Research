# Type E: exact quartic noncollapse of the sixteen isolated edges

**2026-11-02. Global proved range unchanged: 40 <= tau_5 <= 44.**

## Proof status

**[PROVED EXACTLY — universal lemma]** Let z_1,...,z_16 in R^5 satisfy ||z_i||^2=1-a_i, 0<=a_i<1/4, sum a_i<=383/504, and |z_i.z_j|<=1/2 for i!=j. Then

    lambda_min(sum_i z_i z_i^T) > 9/50.

**[PROVED EXACTLY — CONDITIONAL TYPE E]** In the Type-E graph H=16K2+F3, the sixteen isolated edges are fixed in every selected twenty-edge matching. Their pairings are all safe. Thus, conditional on the retained mass-selected matching theorem A<=383/504, the sixteen isolated projected vectors **alone** span R^5 quantitatively. This does not assume that the F3 matching is canonical.

**[OPEN]** No Type-E exclusion or new global kissing-number bound is obtained.

## 1. Four-dimensional harmonic inequality

For arbitrary unit x in R^5, put c_i=x.z_i, e_i=c_i^2, E=sum e_i, y_i=z_i-c_i*x in R^4, b_i=a_i+e_i, t_i=||y_i||^2=1-b_i, B=sum b_i, and s_ij=y_i.y_j.

The degree-four Gegenbauer inequality on S^3, homogenized to nonunit y_i, gives

    L := sum_(i<j) s_ij^2*(4*s_ij^2-t_i*t_j)
       >= F := (sum_i t_i^2)^2/8-(3/2)*sum_i t_i^4.    (1)

Indeed, the two positive-definite spherical-harmonic kernels are

    K2(i,j)=4*t_i*t_j*s_ij^2-t_i^2*t_j^2,
    K4(i,j)=16*s_ij^4-12*t_i*t_j*s_ij^2+t_i^2*t_j^2.

The polynomial identity 4*s^4-t*u*s^2-t^2*u^2/4 = K4/4+K2/2 yields the exact SOS remainder

    L-F = (1/8)*sum_(i,j)K4(i,j)+(1/4)*sum_(i,j)K2(i,j) >=0.

The second term is the weighted traceless-frame variance

    (1/4)*sum_(i,j)K2(i,j)
      = ||sum_i t_i*(y_i*y_i^T-(t_i/4)*I_4)||_F^2.     (2)

## 2. Upper bound using sixteen safe pairings

All distinct isolated K2 components have four safe endpoint cross-correlations, so Walsh averaging gives |z_i.z_j|<=1/2. Put d_ij=|c_i*c_j|=sqrt(e_i*e_j). Then

    |s_ij|<=1/2+d_ij,
    4*s_ij^2-t_i*t_j<=b_i+b_j+4*d_ij+4*d_ij^2.

Expanding the pair upper expression instead of replacing every s_ij^2 by a worst-case value gives

    s_ij^2*(4*s_ij^2-t_i*t_j)
      <= (1/4+d_ij+d_ij^2)*(b_i+b_j+4*d_ij+4*d_ij^2).

After summing over 120 safe pairs, the right side is

    15*B/4 + sum d_ij*(b_i+b_j) + sum d_ij^2*(b_i+b_j)
      + sum d_ij + 5*sum d_ij^2 + 8*sum d_ij^3 + 4*sum d_ij^4.

Cauchy and the mass caps give

    sum d_ij <= 15*E/2,      sum d_ij^2 <= E^2/2,
    sum d_ij^3 <= E^3/4,     sum d_ij^4 <= E^4/8,
    sum d_ij^2*(b_i+b_j) <= (1/2+E)*E^2/2,
    sum d_ij*(a_i+a_j) <= 4*sqrt(M2)*E < 7*E/4,
    sum d_ij*(e_i+e_j) <= sqrt(15)*E^2/2 < 2*E^2.

For the penultimate inequality, write the sum as
sum_i a_i*sqrt(e_i)*sum_(j!=i)sqrt(e_j), apply Cauchy twice,
and use sum a_i^2<=M2<49/256. For the last inequality,
sum_(j!=i)sqrt(e_j)<=sqrt(15*(E-e_i)) and another Cauchy gives

    sum_i e_i^(3/2)*sqrt(E-e_i)
      <= sqrt[(sum e_i^2)*(E^2-sum e_i^2)] <= E^2/2.

Thus the stronger exact safe-pair upper polynomial is

    L <= (15/4)*A_I + 13*E + (19/4)*E^2
         +(5/2)*E^3 + (1/2)*E^4.                         (3)


## 3. Exact variance-aware lower bound

Writing U_k=sum b_i^k, expansion of F for sixteen vectors gives

    F=8-2*B+B^2/2-(5+B/2)*U2+U2^2/8+6*U3-(3/2)*U4. (4)

With q=1/4+E, we have U4<=q*U3 and U2^2<=B*U3. Therefore

    F>=8-2*B+B^2/2-(5+B/2)*U2
      +[1/8+(6-3*q/2)/B]*U2^2.                      (5)

The capped-mass concentration inequality and elementary moment bounds give

    sum a_i^2 <= M2=3/16+(5/504)^2=47653/254016,
    U2 <= M2+E/2+E^2.                               (6)

Assume E<=E0=9/50. Set the exact rationals

    B0=A0+E0=11843/12600,
    q0=1/4+E0=43/100,
    V0=M2+E0/2+E0^2=49215349/158760000,
    C0=1/8+(6-3*q0/2)/B0=551627/94744,
    K0=5+B0/2=137843/25200.

Because B<=B0<2 and q<=q0, equation (5) is at least

    8-2*B0+B0^2/2-K0*U2+C0*U2^2.

The quadratic is decreasing on 0<=U2<=V0, since

    K0-2*C0*V0=13989845831977/7520778720000>0.

Thus (1),(5),(6) imply

    L >= R=8-2*B0+B0^2/2-K0*V0+C0*V0^2.

But (3) implies

    L <= U=(15/4)*A0+13*E0+(19/4)*E0^2+(5/2)*E0^3+E0^4/2.

The exact contradiction gap is

    R-U=32005920115782093751/477599531834880000000>0.

Consequently E>9/50 for every unit x, proving the theorem.

## 4. Consequences and limitations

For the four core projected vectors z_j and their midpoint energy C_core, the sixteen-vector bound gives the cross-block estimate

    sum_(i isolated, j core) (z_i.z_j)^2
       = tr(Z_I*Z_core) > (9/50)*(4-C_core).

The important structural consequence is that the sixteen isolated projected vectors cannot be confined to a four-dimensional subspace, even when the F3 core has a strict rational R^3 realization.

Next target: retain the positive weighted traceless-frame term (2) together with the previous unweighted five-to-four Q-frame remainder and the individual six F3 exceptional correlations. No one-to-one D5 kernel/exception correspondence is assumed.

**Retained inputs:** exact Type-E star sum<=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, and source-audited Musin/Boyvalenkov zero-midpoint boundary exclusion. Types C/D, generic e>=27, and non-isolated configurations remain open.

Verifier: research/verify_tau5_typeE_isolated16_quartic_2026_11_02.py.
