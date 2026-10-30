# Type E: Walsh parity-channel audit, sharp positive-part slack, and full four-channel frame identity (2026-10-29)

**[PROVED EXACTLY — algebraic and finite-incidence statements under the hypotheses below].** Application to Type E is **[CONDITIONAL ON RETAINED 16K2+F3 MATCHING REDUCTION]**. This does **not** eliminate Type E or change the proved global range `40 <= tau_5 <= 44`.

## 1. Exactly 374 or 375 safe Walsh parity channels

Write the twenty selected deep pairs as `x_i^s=m_i+s z_i`, `s=+/-1`, with unit endpoints, `m_i.z_i=0`, `a_i=||m_i||^2<1/4`, `||z_i||^2=1-a_i`. For two different selected pairs define

    a=m_i.m_j, b=m_i.z_j, c=z_i.m_j, d=z_i.z_j.

The two Walsh parity channels are the endpoint products with sign product `st=+1` or `st=-1`. Their respective two-contact boxes are equivalent to

    |a+d|+|b+c| <= 1/2,       (plus channel)
    |a-d|+|b-c| <= 1/2.       (minus channel)

A channel is *safe* when both its endpoint products lie in `[-1/2,1/2]`. For the 184 outside/outside or outside/core pairings, both channels are safe, giving 368 safe channels.

For the ten-edge F3 graph

    02,04,05,14,17,23,27,36,56,57,

the three perfect matchings are

    P1 = 02|14|36|57,
    P2 = 04|17|23|56,
    P3 = 05|14|27|36.

Enumerating the six unmatched F3 deep contacts among the six core/core pairings gives deep-contact multiplicities

    P1: (0,1,1,1,1,2)  (up to ordering),
    P2: (1,1,1,1,1,1),
    P3: (0,1,1,1,1,2).

For every core/core pairing, all its cross-deep contacts, if any, occupy **one parity channel** (independent of endpoint orientation). Therefore the other channel is safe. P1/P3 have seven safe core parity channels and five potentially bad ones; P2 has six safe core channels and six potentially bad ones. Of the 380 total parity channels across the 190 selected-edge pairings, **375 are safe for P1/P3, and 374 for P2**. In particular, each core pairing has a sign `sigma_ij=+/-1` for which

    |a+sigma_ij*d|+|b+sigma_ij*c| <= 1/2.             (1)

This retains one full Walsh channel even for each potentially exceptional core pair. No D5 labeling is assumed.

## 2. Sharp positive-part improvement for each fully safe pairing

For a pairing with **both** Walsh channels safe, put

    h=1/2-|d|,  Uplus=1/2-|a+d|,  Uminus=1/2-|a-d|,
    e=h^2+a^2-b^2-c^2.

Both `Uplus,Uminus` are nonnegative and `|b+c|<=Uplus`, `|b-c|<=Uminus`. The identity `(|a+d|+|a-d|)/2=max(|a|,|d|)` gives the **exact nonnegative decomposition**

    e = (|a|-|d|)_+
        + (Uplus^2-(b+c)^2)/2
        + (Uminus^2-(b-c)^2)/2.                       (2)

Consequently

    (m_i.z_j)^2+(z_i.m_j)^2
      <= (1/2-|z_i.z_j|)^2+(m_i.m_j)^2
         - (|m_i.m_j|-|z_i.z_j|)_+.                  (3)

The positive-part term is **sharp for the abstract four-contact Walsh box**: for any `|a|+|d|<=1/2`, take `b+c=Uplus`, `b-c=Uminus`. This saturates both parity constraints and gives equality in (3). It is not claimed that every such four-number example extends to a realizable five-dimensional sphere code.

There is also the sharp two-sided mixed-asymmetry bound

    |b^2-c^2| <= (1/2-|a+d|)(1/2-|a-d|).              (4)

The earlier one-sided asymmetry bound did not retain the two-sided absolute values of `a+d` and `a-d`.

For projected-orthogonal safe pairs `d=0`, (2) yields `e>=|a|`, a **linear penalty** in the absolute midpoint-midpoint correlation. This is a conditional geometric opportunity, not an assertion that the actual Type-E directions have a D5 orthogonality graph.

## 3. Global frame/Parseval identity and direct Q interface

Let

    M=sum_i m_i m_i^T, Z=sum_i z_i z_i^T,
    A=sum_i a_i, U=sum_i a_i^2,
    W=||M+Z-4I_5||_F^2,
    V=||Z-((20-A)/5)I_5||_F^2.

The **full four-channel squared-correlation energy** is

    S4=sum_(i<j)[(m_i.m_j)^2+(m_i.z_j)^2
                  +(z_i.m_j)^2+(z_i.z_j)^2].

Since `tr(M+Z)=20` and `tr(M+Z)^2=80+W`, direct expansion proves

    S4 = 30+A-U+W/2.                                 (5)

This is exact for any twenty unit endpoint pairs, regardless of safety or D5 alignment. With `0<=a_i<=1/4`, `U<=A/4`, so

    S4 >= 30+(3/4)A+W/2.                             (6)

Thus the total four-channel energy increases above 30 whenever `A>0`, even though the projected-only Q-floor decreases as A grows.

The retained exact projected Q identity reads

    Q=sum_(i<j)(z_i.z_j)^2
     =30-3A+A^2/10-U/2+V/2.

Subtracting it from (5) gives the **exact four-channel compensation law**

    S4-Q = 4A-A^2/10-U/2+(W-V)/2.                    (7)

This is a direct translation of the Q/frame information into midpoint and mixed Walsh energy, without assigning any of the six core exceptions to the six D5 Q-kernel relations.

## 4. Explicit improvement of the retained safe-mixing SOS inequality

For the 184 fully safe pairings set

    H184=sum_safe (1/2-|z_i.z_j|)^2,
    G184=sum_safe (|m_i.m_j|-|z_i.z_j|)_+,
    Ao=sum_(i outside core) a_i,
    R=||Z-((20-A)/5)I_5||_F.

The earlier exact decomposition in `tau5_typeE_refined_mixed_frame_SOS_2026-10-25.md` has a nonnegative safe remainder `E_safe=sum_safe e_ij`. Equation (2) strengthens it to `E_safe>=G184`. Under `A<=383/504`, that decomposition therefore gives

    H184+(2A/sqrt(5))*R
      >= (2137/2520)*A+(1129/504)*Ao+G184.          (8)

This is **[PROVED EXACTLY, CONDITIONAL ON THE RETAINED TYPE-E SAFE INCIDENCE AND MIDPOINT CAP]**. It improves the existing bound by an explicit nonnegative sign-sensitive term; no positive uniform lower bound for `G184` has yet been established.

## Proof-status ledger

- **[PROVED EXACTLY]** 374/375 safe Walsh parity-channel incidence, local sharp positive-part identity (2), asymmetry (4), global frame identity (5), and algebraic Q compensation (7).
- **[PROVED CONDITIONALLY]** The strengthened Type-E 184-safe inequality (8), using the previously established SOS decomposition and retained `A<=383/504`.
- **[OPEN]** A rank-five/contact argument forcing a useful positive `G184`, or a sufficiently strong upper bound on `H184` and frame variance. No Type-E exclusion. Type C, Type D, generic `e>=27`, and non-isolated branches remain open. Sparse `e=23,24` classification requires `delta(G)>=1`.
- **[RETAINED]** Star `70/3`, broom `M(F3)<=89`, matching mass `M(P)>=S/2-28/3`, twenty-edge mass `>=2137/6`, and `A<=383/504`. The Musin/Boyvalenkov zero-midpoint boundary exclusion is unchanged.
- **[GLOBAL PROVED RANGE — UNCHANGED]** `40<=tau_5<=44`.

Companion exact Fraction verifier: `research/tau5_typeE_Walsh_parity_positive_gap_frame_2026-10-29_verify.py`.
