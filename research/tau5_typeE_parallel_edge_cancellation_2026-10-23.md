# Type E: parallel-edge cancellation and improved matching-uniform core slack

Date: 2026-10-23. **[PROVED EXACTLY]** The finite F3 enumeration and vector inequality below under strict deep-contact hypotheses. **[CONDITIONAL ON RETAINED TYPE-E REDUCTIONS]** Application to the mass-selected matching and energy ceiling. **[OPEN]** Type-E elimination and global 41-code exclusion.

## Theorem

For any perfect matching of F3 with edges 02,04,05,14,17,23,27,36,56,57, let the four selected deep endpoint pairs be x_i^±=m_i±z_i, with m_i.z_i=0 and a_i=||m_i||²<1/4. Put C=sum a_i, d=sum_{i<j}(-m_i.m_j)_+, epsilon=C-d. Assume all six unmatched F3 edges are strict deep contacts, with endpoint dot products <-1/2.

**Every matching satisfies C>0 and, when C<=383/504, epsilon>C²/1242.**

For the two non-singleton matchings a stronger variable-C inequality is

    epsilon > C²/[1024+132C+16 sqrt(64C+8C²)].              (1)

For the all-singleton matching the earlier independent bound epsilon>1/[24(4-C)]>=1/96 is stronger.

## Exact graph certificate

There are exactly three perfect matchings:
- P1: 02|14|36|57. The quotient pair 0,3 has parallel cross edges 05 and 27, with endpoint signs (+,+) and (-,-). Balanced triangles: matched-pair triples (0,1,3) using 04,05,17 and (0,2,3) using 23,27,56.
- P2: 04|17|23|56. All six quotient pairings occur once, and all four quotient triangles are switching-balanced.
- P3: 05|14|27|36. The quotient pair 0,2 has parallel cross edges 02 and 57, with endpoint signs (+,+) and (-,-). Balanced triangles: (0,1,2) using 04,02,17 and (0,2,3) using 57,56,23.

These orientations use the lower-numbered vertex as the + endpoint of each matching edge. The companion verifier exhaustively enumerates all four-edge subsets.

## Proof for P1 and P3

Define M=sum m_i, s=||M||, b_i=||m_i||, bbar=(sum b_i)/4, E_ij=a_i+a_j-2|m_i.m_j|. The exact four-core Gram decomposition gives

    4epsilon=s²+sum_{i<j}E_ij,    sum_i(b_i-bbar)²<=epsilon. (2)

For a balanced quotient triangle I, expanding its three strict deep contacts gives

    ||sum_{i in I}m_i||²/2 + ||sum_{i in I}eta_i z_i||²/2 + T_I < 0,

where eta_i eta_j is the product of endpoint signs on the chosen cross edge and T_I is the mixed midpoint/z term. Each cross-edge mixed term has magnitude <=2sqrt(E_ij) by m_i.z_i=0 and ||z_i||<=1.

Use the two balanced triangles in the graph certificate. The mixed terms for their shared quotient pair **cancel exactly**: the parallel edges use (+,+) and (-,-) endpoints. The other four cross edges connect distinct quotient pairs. If F is the sum of their four E_ij, and r,h are the distinct omitted matched-pair indices, Cauchy gives

    ||M-m_r||²+||M-m_h||² < 8sqrt(F),    F+s²<=4epsilon. (3)

The equal-length variance in (2) implies, for any two indices r,h,

    a_r+a_h >= C/2-sqrt(Cepsilon).                         (4)

Indeed a_r+a_h-C/2 is half a signed sum of the four b_i² with two plus and two minus signs. Subtract bbar², apply Cauchy, and use sum_i(b_i+bbar)²=C+12bbar²<=4C.

Since ||m_r+m_h||<=sqrt(2C), equations (3)-(4) give

    C/2 < 8sqrt(F)+2sqrt(2C)s+sqrt(Cepsilon).

A **joint** Cauchy inequality bounds the first two terms by

    8sqrt(F)+2sqrt(2C)s
      <=sqrt(64+8C)sqrt(F+s²)
      <=2sqrt(64+8C)sqrt(epsilon).

Thus C/2 < [2sqrt(64+8C)+sqrt(C)]sqrt(epsilon). Squaring gives (1). Strictness comes from the strict deep contacts. C=0 is impossible already from a balanced triangle.

## Rational uniform consequence

The denominator D(C)=1024+132C+16sqrt(64C+8C²) is increasing. For B=383/504, D(B)<1242 follows exactly: 1242-1024-132B>0 and

    (1242-1024-132B)²-256(64B+8B²)=3458281/15876>0.

Hence P1/P3 have epsilon>C²/1242. P2 has epsilon>1/96>C²/1242 for C<=B<1. This proves the theorem for whichever perfect matching is mass-selected.

## Six-exception consequence

The raw four-core negative-Gram defect now satisfies

    4d < 4C - 2C²/621.                                      (5)

This replaces the older 4d<4C-C²/788, increasing the guaranteed quadratic penalty by a factor 1576/621 (approximately 2.54). The independent 4d<=4C-||M||² penalty may be combined by a maximum, **not by adding** penalties. Retain (1) when possible.

**Not proved:** This is not a Type-E exclusion, does not produce a global safe-pair squared-correlation upper bound, and does not establish D5 labeling or any six-exception/Q-kernel correspondence. Type C, D, E, generic e>=27 and non-isolated branches remain open. The sparse e=23/24 classification still assumes delta(G)>=1. Global proved range remains 40<=tau_5<=44. Preserve exact F3 inputs M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass >=2137/6, and A<=383/504.