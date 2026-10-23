# Type E: joint missing-safe-pair and core-Gram stability

2026-10-23. **[PROVED EXACTLY — local endpoint theorem]** for either doubled-contact matching P1=02|14|36|57 or P3=05|14|27|36 of F3, under the unit endpoint, strict deep-contact, and ordinary kissing inequalities. **[CONDITIONAL ON RETAINED TYPE-E REDUCTIONS]** for the mass-selected matching and C<=A<=383/504. **[OPEN]** Type E exclusion and the global 41-code contradiction. The proved global range remains 40<=tau_5<=44.

Let C=sum_{i=1}^4 ||m_i||^2, d=sum_{i<j}(-m_i.m_j)_+, epsilon=C-d, K=4-2sqrt(3). For P1/P3, the new *joint* inequality is

    epsilon > (K-C/2)^2/[2sqrt(64+8C)+sqrt(C)]^2,    C<2K.       (J)

Combined with the previously proved epsilon>C^2/1242 for C<=383/504 and the independent P2 all-singleton estimate epsilon>1/[24(4-C)]>=1/96, this gives **for every one of the three matchings**

    BOXED: epsilon=C-d>1/4250.                                  (U)

This is an absolute four-core defect gap, not an exclusion of Type E.

## Proof

For P1/P3, use the balanced quotient triangles and signs of the 2026-10-23 parallel-edge and missing-safe-pair notes. Denote the doubled quotient pair p,q and missing safe pair r,h. After switching z_i to v_i, define

    U=v_p+v_q;  Z=||U+v_r||^2+||U+v_h||^2;
    S=m_p+m_q+m_r+m_h;  s=||S||;
    M=||S-m_r||^2+||S-m_h||^2.

Set E_ij=a_i+a_j-2|m_i.m_j|>=0 and F=sum E_ij over the four nonparallel cross contacts of the two triangles. The two parallel mixed terms cancel; each of the remaining four has magnitude <=2sqrt(E_ij), using m_i.z_i=0 and ||z_i||<=1. Summing the six strict deep-contact inequalities, then Cauchy, gives

    Z+M<8sqrt(F)<=8sqrt(4epsilon-s^2),                          (1)

because the exact four-vector identity is 4epsilon=s^2+sum_{i<j}E_ij.

**Missing safe pair, all C:** Put g=||m_p-m_q||^2, t=||U||. The parallel deep contacts and their unused cross contacts imply 1-g<=t^2<1. The four safe cross contacts of r,h give ||v_r+v_h||^2<=3. Also a_r+a_h<=C-g/2. Hence

    Z>=2t^2+2-(a_r+a_h)-2sqrt(3)t.                              (2)

If g<=1/4, then t>=sqrt(1-g)>=sqrt(3)/2, where 2t^2-2sqrt(3)t is increasing. Thus

    Z>=4-C-(3/2)g-2sqrt(3)sqrt(1-g)>=K-C,

as the g-dependent remainder is increasing for 0<=g<=1/4. If g>1/4, the global minimum 2t^2-2sqrt(3)t>=-3/2 gives

    Z>=1/2-C+g/2>5/8-C>K-C.

Therefore Z>=K-C without the earlier small-C restriction.

**Keep core variance in the same inequality:** The four-core identity yields

    a_r+a_h>=C/2-sqrt(C epsilon),   ||m_r+m_h||<=sqrt(2C).

Expanding M gives

    M>=2s^2+C/2-sqrt(C epsilon)-2sqrt(2C)s.                     (3)

Substitute (2)-(3) into (1), discard the nonpositive -2s^2, and apply *one* Cauchy inequality:

    K-C/2 < 8sqrt(4epsilon-s^2)+2sqrt(2C)s+sqrt(Cepsilon)
          <=[2sqrt(64+8C)+sqrt(C)]sqrt(epsilon).

Since C<2K, squaring proves (J). No independent penalties have been added or double counted.

## Rational uniform certificate

Take c0=541/1000. The Type-E ceiling B=383/504 satisfies B<2K. For C>=c0, the previous quadratic gap gives

    epsilon>C^2/1242>=292681/1242000000>1/4250.

For C<=c0, the right side of (J) is decreasing in C. Exact rational upper bounds

    sqrt(3)<17321/10000,
    sqrt(64+8c0)<827/100,
    sqrt(c0)<3/4

give K-c0/2>2653/10000 and 2sqrt(64+8c0)+sqrt(c0)<1729/100, hence

    epsilon>(2653/10000)^2/(1729/100)^2
           =143641/610090000>1/4250.

For P2 the independent signed-K4 gap epsilon>1/96 is stronger. All rational comparisons are checked in the companion script.

## Proof-status and next step

**[PROVED EXACTLY]** The joint local inequality (J), the all-C missing-pair coercivity Z>=K-C, and rational subcertificate. **[CONDITIONAL ON RETAINED TYPE-E REDUCTIONS]** For the *one mass-selected matching*, C-d>1/4250, so 4d<4C-2/2125. Retain the sharper variable-C inequality and epsilon>C^2/1242 rather than replacing them by the uniform scalar constant in an optimization. **[NOT PROVED]** No contradiction with A<=383/504, no D5 labeling, and no identification of the six exceptional pairings with the Q-kernel relations.

Preserve M(F3)<=89, M(P)>=S/2-28/3, selected mass >=2137/6, and A<=383/504. Type C/D, generic e>=27 and non-isolated branches remain open; sparse e=23/24 classification assumes delta(G)>=1. The Musin/Boyvalenkov zero-midpoint exclusion remains independent. The generic two-sided three-point SDP route at mu=1/2 is closed as primary route.

**Next:** Retain the unsquared inequality (1)-(3) with the global Q-frame variance in the finite six-core polynomial/KKT system.
