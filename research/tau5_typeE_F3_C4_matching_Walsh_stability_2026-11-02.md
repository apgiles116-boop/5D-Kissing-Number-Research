# Type E: exact F3 C4 matching dichotomy and mixed-Walsh stability (2026-11-02)

**[PROVED EXACTLY — standalone eight-endpoint F3 lemmas]** under the ten strict deep contacts 02,04,05,14,17,23,27,36,56,57 and eighteen two-sided-safe nonedges. **[CONDITIONAL]** Type-E numerical corollaries retain separately proved/recorded matching, harmonic, and Q-frame certificates. **[OPEN]** Type E and the global problem remain unresolved: 40 <= tau_5 <= 44.

## 1. Actual deep endpoint versus opposite-contact average

For selected deep edges u_i^±=m_i±z_i and u_j^±=m_j±z_j with exactly one deep cross-contact, orient that contact as (++). Set h=m_i·m_j, d=z_i·z_j, p=m_i·z_j, q=z_i·m_j and delta=(|d|-1/2)_+.

The previously audited singleton Walsh theorem, when delta>0, gives

    d=-1/2-delta,
    h<=-delta-|p-q|,
    p+q<=h-delta<=-2delta-|p-q|.

Hence the **actual** deep endpoint correlation satisfies

    u_i^+·u_j^+ <= -1/2-4delta-2|p-q|.       (1)

Its slack eta=-1/2-4delta-u_i^+·u_j^+ is nonnegative and eta>=2|p-q|. For delta=0, the actual deep contact is <-1/2 and eta=-1/2-u_i^+·u_j^+>0. This does NOT replace an endpoint correlation by an opposite-contact average. The withdrawn Perron argument remains withdrawn.

## 2. Exact C4 incidence

Take the canonical matching P0=(04),(17),(23),(56), switch its projected vectors by g=(1,-1,1,1), and order its four quotient vertices 0,1,2,3. The six quotient cross deep contacts are

    01: 4-1 (--); 02: 0-2 (++); 03: 0-5 (++);
    12: 7-2 (++); 13: 7-5 (++); 23: 3-6 (--).

By the retained exact switched-projection triangle theorem, the positive-defect support is triangle-free. Four positive defects therefore form one of three C4s:

    Eplus = {02,03,12,13}: K2,2 on original endpoints {0,7} x {2,5}.
    E1    = {01,02,13,23}: the four actual deep contacts are P1=(02),(14),(36),(57).
    E2    = {01,03,12,23}: the four actual deep contacts are P2=(05),(14),(27),(36).

In E1/E2 one cannot choose four original endpoints realizing all four contacts simultaneously: some are (++) and some (--). The matching identity below handles this exactly.

## 3. All-plus K2,2 second-order identity [PROVED EXACTLY]

Let v0=u0, v1=u7, v2=u2, v3=u5. The four cross contacts are deep; within-part pairs 0-7 and 2-5 are safe. Let Dplus be the sum of their positive projected defects, eta_plus the sum of the four slacks from (1), and

    s=(1/2-v0·v1)+(1/2-v2·v3)>=0,
    T=||v0+v1+v2+v3||^2>=0.

Direct expansion gives the exact sum-of-nonnegative-terms identity

    Dplus+T/8+eta_plus/4+s/4=1/4.              (2)

In particular Dplus<=1/4 and

    Dplus+T/8+(1/2)sum_cross|p-q|+s/4<=1/4.

This is valid even when some of the four cross quotient pairs have zero defect.

## 4. Mixed C4 matching-transfer identity [PROVED EXACTLY]

If all four positive defects form E1 or E2, the four actual deep contacts constitute alternative perfect matching Pk (k=1 or 2). Its midpoint energy Ck=sum_(xy in Pk)|| (u_x+u_y)/2 ||^2 obeys

    Ck=2+(1/2)sum_(xy in Pk) u_x·u_y
      =1-2D_raw-eta/2,

where eta is the sum of the four nonnegative deep slacks. Consequently

    Ck+2D_raw+eta/2=1,
    Ck+2D_raw+sum_(e in Pk)|p_e-q_e|<=1.      (3)

The mixed terms are oriented to the actual deep contact. The separately verified F3 rational SOS theorem gives

    C1,C2 > (1291-1585*C0)/2000.

Combining with (3) yields the exact mixed-Walsh stability inequality

    D_raw+(1/2)sum_e|p_e-q_e| < (709+1585*C0)/4000.  (4)

## 5. Conditional canonical Type-E improvement

**[CONDITIONAL]** Suppose P0 is the mass-selected Type-E matching, C0<=A, and the separately retained stronger harmonic bound A<567/1000 applies. Then (4) gives D_raw<321539/800000=0.40192375 in either mixed C4. With <=3 defects the singleton cap delta<1/8 gives D_raw<3/8; for Eplus use (2). Thus, over every canonical-selected support,

    D_raw < 321539/800000.                     (5)

This improves the previous canonical 812511/2000000=0.4062555 ceiling by exactly 17327/4000000.

**[FURTHER CONDITIONAL]** Retain the preceding exact C4 quadratic mass certificate

    sum_C4 delta_e^2 <= Dstar^2/4,
    Dstar=812511/2000000,

and the independently retained center-sensitive projected-frame floor Q_total>28.3626. With <=3 defects, D+sum delta^2<27/64; for Eplus, (2) and delta<1/8 give <=1/4+1/32. For either mixed C4, (5) and the quadratic certificate give

    D+sum delta^2 < 7090954125121/16000000000000
                  = 0.4431846328200625.

The six potentially exceptional canonical core pairs therefore have squared-correlation sum <3/2+0.4431846328200625. For the other 184 completely two-sided-safe pairs,

    Q_safe > 422710645874879/16000000000000
           = 26.4194153671799375.                (6)

If at most 43 of these 184 safe pairs had |z_i·z_j|>1/3, their squared sum would be <=43/4+141/9=317/12=26.416666..., contradicting (6). Thus **at least 44 of 184 safe pairs exceed 1/3 in absolute projected correlation**, conditional on the stated harmonic and Q-frame certificates. The exact threshold margin is 131937624637/48000000000000.

## Proof-status ledger

**[PROVED EXACTLY]** (1)-(3), the three-C4 contact classification, and (4) using the previously verified standalone F3 SOS matching theorem and triangle-free theorem. The local verifier independently enumerates the contact incidence and checks the exact identities.

**[CONDITIONAL]** (5) additionally needs canonical mass selection and A<567/1000. The 44-safe-pair conclusion additionally needs the previously established C4 quadratic certificate and Q_total>28.3626; these upstream inputs were not re-proved in this pass.

**[WITHDRAWN]** The old endpoint-Perron inference, four-defect exclusion, and any dependent 45/46-safe-pair claims remain withdrawn.

**[OPEN]** Type E, C, D, generic e>=27, non-isolated branches; e=23/24 sparse graph classification still assumes minimum degree >=1. Retain star <=70/3, M(F3)<=89, matching M(P)>=S/2-28/3, twenty-edge mass >=2137/6, baseline A<=383/504, and the audited Musin/Boyvalenkov 21-line zero-midpoint exclusion. Global proved range 40<=tau_5<=44.

Next: exploit the positive eta and T penalties jointly with the rank-five full projected Gram matrix; the integer count alone is not an exclusion.

Verifier: research/verify_typeE_F3_C4_matching_Walsh_stability_2026-11-02.py.
