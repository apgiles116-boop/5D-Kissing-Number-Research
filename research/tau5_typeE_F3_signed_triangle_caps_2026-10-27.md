# Type E: endpoint-Walsh contact counting and signed-triangle obstruction

**[SUPERSEDED BY STRONGER RESULT — 2026-10-27]** See [the exact F3 endpoint-charge SOS](tau5_typeE_F3_endpoint_charge_2026-10-27.md): all three matchings have at most **three** active exceptions, not merely four; the P2 quartic ceiling improves from 0.187511443... to **225/2048 = 0.10986328125**. The signed-triangle lemma and its earlier upper bounds remain valid, but they are not the strongest ledger entries.

Date: 2026-10-27. **[PROVED EXACTLY — conditional on the retained Type-E graph and endpoint inequalities]** This note strengthens the F3 cross-contact defect caps and proves that at most four of the six core pairings can be exceptional. **[OPEN]** No elimination of Type E or improvement to the global bound `40 <= tau_5 <= 44`.

## 1. Sharp contact-counting bound (no D5 labels)

Take two selected deep edges with unit endpoints `p_i^+ = m_i+z_i`, `p_i^- = m_i-z_i`, and similarly for `j`. Every cross-endpoint scalar product is at most `1/2`. The deep graph contains a cross pair precisely when its endpoint scalar product is at most `-1/2`; a nonedge has scalar product strictly greater than `-1/2`.

Set `s = sign(z_i.z_j)` (the case of zero correlation is trivial) and relabel the two endpoints of edge `j` so that its projected vector is `s z_j`. Write `C_{sigma,tau}=p_i^sigma . p_j^{s tau}`. Then the exact Walsh identity gives

    4 |z_i.z_j| = C_{++}+C_{--}-C_{+-}-C_{-+}.

The two plus-sign terms are at most `1/2`. Each minus-sign term is at least `-1`, and if that cross pair is not a deep edge it is strictly greater than `-1/2`. Let `k` be the number of deep cross contacts among the two *opposite-sign* terms. Thus

    |z_i.z_j| <= 1/2 + k/8,   k in {0,1,2},

with a strict inequality when `k<2`. In particular, a positive raw excess `d_ij=(|z_i.z_j|-1/2)_+` requires `k>=1`; if there are no deep cross contacts at all, then `|z_i.z_j|<1/2` and `d_ij=0`. If there is exactly one cross contact, `d_ij<1/8`; if two disjoint contacts, `d_ij<=1/4`.

This elementary exact bound supersedes the weaker `d<1/12` for zero contacts and `d<sqrt(2)-5/4` for one contact in the earlier F3 note. Those older bounds remain valid but are not sharp. It also proves an *orientation condition*: if all existing cross contacts between the two matching edges have the same product of endpoint labels `sigma_i sigma_j`, then an active excess requires `sign(z_i.z_j)=-sigma_i sigma_j`. The F3 two-contact cases have this property.

## 2. The F3 quotient is signed-antibalanced on every triangle

Use the retained F3 edges `02,04,05,14,17,23,27,36,56,57` and perfect matchings

    P1=(02,14,36,57), P2=(04,17,23,56), P3=(05,14,27,36).

Orient each selected edge `(u,v)` by `z=(p_u-p_v)/2`, so `u` has endpoint sign `+` and `v` has `-`. For every pair of selected edges having at least one F3 cross contact, the sign of any positive projected excess is forced as in Section 1. In all three matchings, each triangle of potentially exceptional pairs has product of its three forced signs equal to `-1` (checked by finite exact enumeration; the verifier records all three cases).

**Signed-triangle lemma.** Suppose three projected vectors have squared norms at most `1` and their three pairwise correlations all have magnitude greater than `1/2`, with sign product `-1`. Switching signs of the vectors makes all three correlations negative. But then

    0 <= ||v_1+v_2+v_3||^2
       = sum_i ||v_i||^2 - 2 sum_{i<j}|v_i.v_j|
       < 3 - 2*3*(1/2) = 0,

an impossibility. Hence no such triangle can be fully active. This is a rank/PSD obstruction, not a numerical test or a D5 contact assumption.

For `P2`, all six potential pairings have one cross contact, but each of the four quotient triangles has forced sign product `-1`. Thus the active exceptional graph is triangle-free and has at most **four** edges. For `P1/P3`, one pairing `(14,36)` has zero cross contacts and can never be active; the other five comprise a four-cycle plus its diagonal two-contact pair. Both triangles containing that diagonal have forced sign product `-1`. Thus the active graph again has at most **four** edges, and if the two-contact diagonal is active, it has at most **three** active edges.

**[CORRECTION TO BRANCH LEDGER]** The six-active branch is empty for actual Type-E F3 geometry in every matching. Previous six-active spectral and quartic inequalities remain mathematically correct as conditional statements or relaxed Gram calculations, but cannot be used as though six active exceptions occur in an actual F3 matching.

## 3. New exact branchwise quartic positive-defect envelopes

Retain the independent exact linear excess budget

    D0=1780062775/4032758016 = 0.44140083980679884...,
    sum_core d_ij <= D0,

and define the *fixed-threshold quartic* positive defect by

    f(d)=(1/2+d)^2*(d+d^2),
    P_fixed=sum_core f(d_ij).

The distinction from the midpoint-weighted harmonic defect is essential; the latter has an additional nonnegative moving-threshold correction. Since `f` is increasing and convex, the exact maximum of `sum f(d)` for any fixed allowed active support and its individual caps is obtained by filling the largest caps first. Exhaustive enumeration of the 64 labeled support subsets in each matching, excluding zero-contact pairs and signed triangles, yields:

    P2:       P_fixed <= 3*f(1/8)+f(D0-3/8)
                        = 0.18751144325156904...;

    P1 or P3: P_fixed <= f(1/4)+f(1/8)+f(D0-3/8)
                        = 0.25342941200156904... .

The exact rational values are, respectively,

    49594832638991020555971782600827159585
    /264489632093832371229515191803011137536,

    67029451942051259870417364091748303905
    /264489632093832371229515191803011137536.

These improve the preceding F3 bounds `0.215933080809...` for P2 and `0.267887316759...` for P1/P3. The values are **sharp only for the combinatorial capped-simplex relaxation**, not asserted achievable by a rank-five Type-E code. The strict one-contact caps imply that the numerical extrema generally are suprema, not attained.

## 4. Verification and next step

The companion Python verifier uses exact `fractions.Fraction` arithmetic for all defect evaluations, enumerates the F3 cross-contact signs, checks every potentially exceptional triangle has sign product `-1`, enumerates all 64 possible active supports for each matching, and verifies both rational envelopes. The endpoint Walsh and signed-triangle lemmas are proved analytically above, independently of finite tests.

**[RETAINED]** `40<=tau_5<=44`; `1/49<A<=383/504`; `M(F3)<=89`; `M(P)>=S/2-28/3`; twenty-edge mass `>=2137/6`; Musin/Boyvalenkov zero-midpoint exclusion; 184 endpoint-safe pairings; sparse e=23/24 classification conditional on `delta(G)>=1`.

**[OPEN]** Type E, C, D, generic `e>=27` and non-isolated branches. The next finite polynomial/KKT certificate should branch only over the now-restricted triangle-free active supports, preserve the fixed-versus-weighted harmonic threshold correction, and couple the midpoint Gram and projected Gram to the isolated-center row and 184 safe-pair mixing penalties.
