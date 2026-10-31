# Type E: four-core PSD compensation gives Q6 < 1989/1000

Date: 2026-10-31. **Global proved range 40 <= tau_5 <= 44; Type E OPEN.**

## Proof-status ledger

**[PROVED EXACTLY — universal endpoint/Gram algebra]** For four selected deep-edge midpoints m_i and half-differences z_i, put a_i=||m_i||²<=1/4, c_ij=m_i·m_j, d_ij=|z_i·z_j|, eps_ij=(d_ij-1/2)_+, delta=sum eps_ij, E2=sum eps_ij², Q6=sum d_ij². Assuming all four cross-endpoint upper contact inequalities for each core pair, we have

    Q6 <= 3/2 + delta + E2 - sum_(c_ij>0) c_ij(1-c_ij).       (1)

We also have the independent scalar bound, writing A_C=sum a_i and s_C=||sum m_i||²,

    Q6 <= 3/2 + delta/4 + E2 + 3(A_C-s_C)/8.                 (2)

**[PROVED CONDITIONALLY — retained exact Type-E caps]** Under

    A_C <= T=383/504,
    delta <= D=1780062775/4032758016,

the four-case exact rational argument below proves

    Q6 < 1989/1000 = 1.989.                                 (3)

This improves the previous 1.994117229525... cap by more than 0.005117. It does not assume D5 alignment or full Q-rank; applicability to Type E relies on the upstream T and D certificates.

**[PROVED CONDITIONALLY — global frame bounds]** For the 184 safe projected pairings,

    Q_safe > 404841911/15876000 = 25.500246346686... .

With the separately retained center-derived frame-variance bound,

    Q_safe > 5455024505347/211680000000 = 25.770146000316... .

**[OPEN]** Type E remains unresolved. No bound A>383/504 or global improvement of 40<=tau_5<=44 has been proved.

## Universal endpoint inequalities

Averaging the four cross-endpoint inequalities yields c+d<=1/2, hence eps<=(-c)_+. If c<=0, d²<=1/4+eps+eps². If c>0, eps=0 and d²<=(1/2-c)²=1/4-c+c². Summation proves (1).

The pointwise majorant d²<=1/4+eps/4+eps²-3c/4 follows because its gap is c(1/4-c)>=0 when c>=0 and (3/4)(-c-eps)>=0 when c<0. Summing, with 2 sum c_ij=s_C-A_C, proves (2).

For two negative correlations c_12=-u, c_13=-v, the 3x3 midpoint Gram Schur complement gives

    c_23 >= [uv-sqrt((a1*a2-u²)(a1*a3-v²))]/a1
         >= 4[uv-sqrt((1/16-u²)(1/16-v²))],                (4)

provided the last bracket is nonnegative. It increases in u,v on [0,1/4]. Two disjoint defects obey eps_ij+eps_kl<19/50, since their sum is <=A_C/2<=T/2<19/50.

## Exact four-case certificate

Let F(t)=1/16+(t-1/4)² on [1/4,1/2], h=1/100,

    B=3/2+D/4+F(D)+3T/8 = 1.994454729525...,
    C=3/2+D+F(D)       = 2.040535121285... .

Capped-simplex convexity gives E2<=F(delta) for delta>=1/4, and E2<=delta² otherwise. The associated scalar envelope is increasing.

**Case I: delta<=D-h.** Equation (2) gives Q6<=1.988226712729...<1.989.

For all remaining cases delta>D-h>0.4314>0.42. Sort six defects p>=q>=... .

**Case II: q<=41/250=0.164.** Majorization yields E2<=(1/4)²+(41/250)²+(delta-1/4-41/250)². The gap from F(delta) increases with delta. At delta=D-h, (2) gives Q6<=1.988747254069...<1.989.

**Case III: 41/250<q<=1/5, p<=11/50.** Majorization yields E2<=(11/50)²+(1/5)²+(delta-11/50-1/5)². At delta=D-h the increasing gap from F(delta) gives Q6<=1.987578443991...<1.989.

**Case IVa: q>1/5.** Then p+q>2/5>T/2, so the two largest defects share a vertex. Relabel them 12 and 13. Equation (4) gives c_23>7/100. The positive-correlation penalty in (1) gives Q6<=C-(7/100)(93/100)=1.975435121285...<1.989.

**Case IVb: 41/250<q<=1/5, p>11/50.** Now p+q>48/125>T/2, so the two defects again share a vertex. Equation (4) gives c_23>273/5000: the relevant radicand is 1255041/2500000000 < (2243/100000)², and (11/50)(41/250)-2243/100000=273/20000. Consequently (1) gives Q6<=C-(273/5000)(4727/5000)=1.988916281285...<1.989.

These cases are exhaustive. All numerical comparisons above are exact rational inequalities, not floating-point proof steps. The companion Fraction script independently verifies every strict comparison and performs supplementary rational Gram checks.

## Research implications

The improvement comes from *PSD compensation*: two large negative midpoint correlations sharing a core vertex force a positive correlation between the opposite vertices. That positive correlation carries an endpoint-contact penalty. The finite case split rules out near-saturation of the old scalar defect envelope.

The remaining task is a **joint upper bound** on the 184 safe Walsh/Q correlations under one common K5 labeling, using the four rank-free Q residuals and the full signed four-core midpoint Gram matrix. Preserve M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, A<=383/504, and the Musin/Boyvalenkov zero-midpoint exclusion. Types C, D, generic e>=27, and non-isolated branches remain open; sparse e=23/24 classification requires delta(G)>=1.
