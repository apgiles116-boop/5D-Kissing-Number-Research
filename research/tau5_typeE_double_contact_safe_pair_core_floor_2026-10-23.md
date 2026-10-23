# Type E / F3: doubled-contact missing-safe-pair coercivity

2026-10-23. **[PROVED EXACTLY — local eight-endpoint theorem]** under the ten F3 deep contacts, unit endpoints, and the kissing upper bound on every cross endpoint dot product. **[CONDITIONAL ON RETAINED TYPE-E GRAPH]** when applied to Type E. **[OPEN]** Type E elimination, C/D, generic e>=27 and non-isolated 41-code branches. Global proved range stays 40<=tau_5<=44.

## Theorem

For F3 edges 02,04,05,14,17,23,27,36,56,57, consider either doubled-contact perfect matching

- P1 = 02|14|36|57
- P3 = 05|14|27|36.

Write the four matched pairs as x_i^±=m_i±z_i, m_i.z_i=0, a_i=||m_i||², C=sum a_i. Every F3 edge has endpoint dot product strictly below -1/2; every distinct pair of code endpoints has dot product at most 1/2. Then

    C > (48-18sqrt(3)-4sqrt(175-91sqrt(3)))/17
      = 0.00857263702649... > 1/117.                      (T)

For P2=04|17|23|56, the separately audited signed-K4 diagonal-shift bound gives C>2-sqrt(15)/2=0.063508... . Hence C>1/117 holds **for each of the three F3 perfect matchings**, but the C values refer to different four-edge selections. The mass-selected 20-edge energy budget is NOT transferred between matchings.

This improves the earlier doubled-contact floor C>2-sqrt(9+4sqrt(3))/2≈0.0044923434.

## Exact quotient graph and sign factorization

For P1 the doubled quotient pair is (p,q)=(0,3) and the missing pair is (r,h)=(1,2); for P3 use (p,q)=(0,2), (r,h)=(1,3). All six remaining deep edges consist of two parallel edges p-q and four edges of {p,q}x{r,h}. Switching z_i to v_i=eta_i z_i makes the z_i.z_j coefficient positive on all six deep edges. The two p-q contacts use opposite incidence signs (++ and --), so their mixed terms cancel. The other four form a checkerboard signed K2,2, giving the **exact** identity

    Tmix=(m_p-m_q).(v_h-v_r)+(m_h-m_r).(v_p-v_q).         (1)

The companion exact verifier enumerates both quotient matrices (spectrum {2,-2,0,0}) and checks this identity with rational vectors.

## Proof

The two p-q deep contacts give m_p.m_q+v_p.v_q<-1/2. Their two unused opposite-sign endpoint contacts are at most 1/2, giving m_p.m_q-v_p.v_q<=1/2. Put U=v_p+v_q, g=||m_p-m_q||². Then

    1-g <= ||U||² < 1-||m_p+m_q||² <=1,                (2)
    ||v_p-v_q||² <=3.                                   (3)

The missing quotient pair r-h has all four cross endpoint products <=1/2. Taking same- and opposite-sign averages gives

    ||v_r+v_h||² <=3,  ||v_r-v_h||² <=3.                 (4)

Sum the three strict deep-contact inequalities on triangle pqr and the three on triangle pqh, using one p-q parallel edge in each. Expanding the dot products and using ||m_i||²+||v_i||²=1 gives

    Z+M+2Tmix<0,                                        (5)

where Z=||U+v_r||²+||U+v_h||² and
M=||m_p+m_q+m_r||²+||m_p+m_q+m_h||²>=0.
By (1), Cauchy-Schwarz, and the parallelogram identity,

    |Tmix| <= sqrt(g+h)*sqrt(||v_r-v_h||²+||v_p-v_q||²),

where h=||m_r-m_h||² and g+h<=2C. The same residual Z satisfies
Z>=||v_r-v_h||²/2, so by (3)

    |Tmix| <= sqrt(2C)*sqrt(2Z+3).

Equation (5) and M>=0 therefore give the **self-consistent** bound

    Z < 2sqrt(2C(2Z+3)),  hence Z²<8C(2Z+3).            (6)

If C>=1/8, (T) is automatic. Otherwise 0<=g<=2C<1/4. Set t=||U||; (2) gives sqrt(1-g)<=t<=1. By (4),

    Z>=2t²+2-(a_r+a_h)-2sqrt(3)t.

The function 2t²-2sqrt(3)t is increasing for t>=sqrt(3)/2. Also g<=2(a_p+a_q), so a_r+a_h<=C-g/2. Consequently

    Z>=4-C-(3/2)g-2sqrt(3)sqrt(1-g)
     >=K-C,  K=4-2sqrt(3),                              (7)

since the derivative of -(3/2)g-2sqrt(3)sqrt(1-g) is
-3/2+sqrt(3)/sqrt(1-g)>0 on 0<=g<=1/4.

The function Z²/(2Z+3) increases strictly for Z>0. Combining
(6)-(7) therefore gives

    (K-C)² < 8C(2(K-C)+3),

or equivalently

    17C²-(18K+24)C+K² < 0.

The smaller root of this exact quadratic is

    C_*=(48-18sqrt(3)-4sqrt(175-91sqrt(3)))/17,

and the other root exceeds 1. Hence C>C_* as claimed.

**Exact rational subcertificate for C>1/117.** The squared rational
comparisons

    1732050/1000000 < sqrt(3) < 1732051/1000000

imply

    Klo=267949/500000 < K < Khi=5359/10000.

If C<=c=1/117, monotonicity of both sides in the relevant interval
would force (Klo-c)² < 8c(2(Khi-c)+3). But exact rational arithmetic gives

    (Klo-c)² - 8c(2(Khi-c)+3)
      =2923336101089/3422250000000000 > 0.

Contradiction. QED.

## Proof ledger and next step

**[PROVED EXACTLY]** Local two-triangle identity, safe-pair coercivity, algebraic and rational bounds. **[RETAINED]** P2 diagonal-shift theorem. **[CONDITIONAL ON TYPE-E REDUCTION]** Matching-uniform core C>1/117. **[NOT PROVED]** No improvement to the stronger total selected A>0.010626; no Type E exclusion; no D5 labeling or Q-kernel identification.

The useful next target is to combine the missing-pair coercivity with the doubled-contact second-order slack C-d>C²/1242, retaining their shared difference norms rather than bounding them separately. Keep F3 mass<=89, matching mass>=S/2-28/3, selected mass>=2137/6, and A<=383/504; never regress to obsolete mass constants.