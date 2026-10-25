# Type E: exact six-exception safe-mass and Q-frame transfer

**2026-10-24. [PROVED EXACTLY, conditional on retained Type-E hypotheses].** Improved raw squared-correlation floor, 184-safe mass floor, forced safe-pair correlation count, and normalized Q-frame stability. **[OPEN]** Type-E elimination and any improvement to 40 <= tau_5 <= 44.

## Hypotheses

For 20 selected disjoint deep edges x_i^±=m_i±z_i in R^5, let a_i=||m_i||^2 in [0,1/4], A=sum a_i<=B=383/504, ||z_i||^2=1-a_i, v_i=z_i/sqrt(1-a_i). For i<j put r_ij=|z_i·z_j|, s_ij=(v_i·v_j)^2, delta_ij=(r_ij-1/2)_+. Only six designated core pairings can have delta_ij>0, and their total D=sum delta_ij<=D0=1780062775/4032758016 (retained exact convex theorem). The other 184 are *raw safe* (r_ij<=1/2); normalization need not preserve safety.

Set Delta=sum_i(v_i v_i^T-I/5), W=sum_i a_i(v_i v_i^T-I/5), T=||Delta||_F^2/2>=0.

## 1. Exact second-order identity [PROVED]

S_z=sum_i z_i z_i^T=((20-A)/5)I+Delta-W. Taking trace squares and removing diagonal contributions gives

    S_raw := sum_{i<j}r_ij^2
      = 30-3A+A^2/10-(1/2)sum_i a_i^2
        +(1/2)||Delta-W||_F^2.                         (1)

Convexity with individual a_i<=1/4 gives, for k=floor(4A), t=A-k/4,

    sum_i a_i^2 <= k/16+t^2.

The resulting scalar floor is decreasing for 0<=A<=B; at B=3/4+5/504,

    sum_i a_i^2 <= M_B=47653/254016,
    S_raw >= F0+(1/2)||Delta-W||_F^2,
    F0=8790283/317520=27.684186822877... .           (2)

This improves the old floor 17456771/635040 by exactly 131/672. It is a necessary bound, not a contradiction.

## 2. Six-exception safe mass [PROVED]

For any two selected edges, average the two cross-endpoint kissing inequalities whose endpoint-sign products agree with sign(z_i·z_j). This gives

    m_i·m_j+r_ij<=1/2,
    0<=delta_ij<=(-m_i·m_j)_+<=sqrt(a_i a_j)<=1/4.   (3)

For six designated core pairings r_ij^2<=(1/2+delta_ij)^2. Convexity, 1/4<D0<1/2, and sum delta_ij<=D0 yield

    sum_core delta_ij^2<=1/16+(D0-1/4)^2,
    S_exc<=13/8+D0/2+D0^2
         =33185502670742844241/16263137215612256256
         =2.040535121285... .

Consequently the 184 raw-safe pairings satisfy

    S_safe := sum_raw-safe r_ij^2
      >= L0+(1/2)||Delta-W||_F^2,                    (4)
    L0=2085231131661776940907/81315686078061281280
      =25.643651701591... .

**Forced correlation count [PROVED]:** At least 76 of the 184 raw-safe pairs have r_ij>1/4. Otherwise S_safe<=75/4+109/16=409/16=25.5625<L0. Similarly at least 38 safe pairs have r_ij>1/3. This is not a D5 labeling.

## 3. Normalized Q-frame transfer [PROVED]

Since (1-a_i)(1-a_j)>=9/16 and delta_ij<=1/4,

    s_ij <= (4/9)(1+2delta_ij)^2
         <= 4/9+(20/9)delta_ij.                     (5)

The last step is delta_ij(1-4delta_ij)>=0. Expanding W's Frobenius norm and using a_i a_j<=1/16 gives

    ||W||_F^2
      <= (11/45)A^2+(5/9)sum_i a_i^2+(5/18)D
      <= C0=133562881183/362948221440
      =0.367994312392... .                           (6)

This improves the naive (4/5)B^2=0.461983... . From Delta=(Delta-W)+W and ||Delta||_F=sqrt(2T),

    S_safe >= L0
        +(1/2)(sqrt(2T)-sqrt(C0))_+^2.              (7)

Equation (7) is a labeling-free, exact *second-order* bridge between the normalized frame excess and the 184 raw-safe correlations, using the six-exception budget. Its additional penalty activates only when T>C0/2~0.184, so it does not alone close the earlier T<=1/25 near-tight dichotomy.

## Proof-status ledger

- **[PROVED EXACTLY]** Identities/inequalities (1)--(7), F0, L0, C0, and the 76-safe-pair count, under the retained Type-E assumptions. A local exact SymPy checker accompanies this note.
- **[RETAINED]** H=16K2+F3, M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, only six possible raw exceptional pairings. Zero-midpoint exclusion retains the source-audited Musin--Boyvalenkov result.
- **[OPEN]** A conflicting upper bound on S_safe or an incompatible normalized three-block defect bound; Type E, C, D, generic e>=27. Sparse e=23,24 graph classification remains conditional on delta(G)>=1.
- **[GLOBAL]** 40<=tau_5<=44.

Next: feed (4)--(7) into a finite four-core rank-five Gram polynomial problem, retaining all normalization denominators and the endpoint mixed terms. Do not equate six core exceptions with six D5 Q-kernel relations without proof.
