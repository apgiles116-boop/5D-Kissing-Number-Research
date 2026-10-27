# Type E: corrected exact 17-line covering radius and weighted-covering obstruction

Date: 2026-10-27. Proof-status labels are strict. Companion exact verifier: `research/tau5_typeE_17line_exact_covering_correction_2026-10-27_verify.py`.

## [PROVED EXACTLY — FINITE 17-LINE TEMPLATE]

Let D16 consist of the twelve projective roots (e_j +/- e_k)/sqrt(2), 2<=j<k<=5, and four roots (e_1+e_j)/sqrt(2), 2<=j<=5. Set x=(8,-3,-3,-3,-3)/10. These seventeen unit projective lines have coherence <=1/2.

The SHARP projective covering constant is

rho = min_{||y||=1} max( |x.y|, max_{d in D16}|d.y| )
    = sqrt(8/(31-6*sqrt(2))) = 0.596089856463373... > 1/sqrt(3).

**Correction:** The previous value 10/sqrt(297+60*sqrt(2)) = 0.511743... is a valid lower bound, but is NOT sharp. The previous conditional four-core energy conclusion was therefore unnecessarily weak.

Proof certificate: For the polar polytope K defined by |x.y|<=1 and |d.y|<=1, write y=sqrt(2)*(T,V1,...,V4). The D16 facets become |V_i +/- V_j|<=1 and |T+V_i|<=1 (32 integral inequalities). The center adds |8*T-3*sum(V_i)|<=5*sqrt(2).

The exact verifier examines all C(32,5)=201376 five-facet intersections by fraction-free integer elimination and finds exactly 48 feasible vertices. It independently identifies these 48 as the two T-lifts of the 24 base points +/-e_i and (+/-1/2)^4. There are exactly 218 edges, identified by common active-facet rank four. Clipping their segments by the center slab gives 114 vertices, with nine exact squared-norm classes:

| Multiplicity | Squared norm |
|---:|---|
| 8 | 31/8 - 3*sqrt(2)/4 |
| 24 | 631/98 - 135*sqrt(2)/49 |
| 8 | 123/32 - 15*sqrt(2)/16 |
| 8 | 127/22 - 280*sqrt(2)/121 |
| 30 | 5/2 |
| 24 | 631/32 - 195*sqrt(2)/16 |
| 2 | 75/16 - 15*sqrt(2)/8 |
| 8 | 2 |
| 2 | 13/4 - sqrt(2) |

The largest squared norm is (31-6*sqrt(2))/8. An explicit equality witness is y=(-a,a,-b,-b,-b), where a=(10+9*sqrt(2))/20 and b=(11*sqrt(2)-10)/20. Thus rho is exact. Its strict inequality rho>1/sqrt(3) reduces to 6*sqrt(2)>7.

## [PROVED EXACTLY — LABEL-FREE TYPE-E NECESSARY CONDITION]

In the isolated-center Type-E branch H=16K2+F3, write endpoints of each selected deep edge as m_i +/- z_i, with a_i=||m_i||^2<=1/4 and ||z_i||^2=1-a_i. Let O be the sixteen outside-core edges and x0 the isolated center. Define the *weighted* covering constant

rho_w = min_{||y||=1} max( |x0.y|, max_{j in O}|z_j.y| ).

For any of the four core edges i, endpoint safety gives |x0.z_i|<=1/2 and |z_j.z_i|<=1/2 for all j in O. Evaluate the maximum at u_i=z_i/sqrt(1-a_i). It follows that

rho_w <= 1/(2*sqrt(1-a_i)),
a_i >= 1-1/(4*rho_w^2) when rho_w>0,
and necessarily rho_w <= 1/sqrt(3).

This is LABEL-FREE. A proof that the actual weighted center-plus-outside configuration has rho_w>1/sqrt(3) would exclude Type E.

## [PROVED EXACTLY — CONDITIONAL TEMPLATE ENERGY THRESHOLD]

If x0 and the sixteen outside-core normalized directions z_j/sqrt(1-a_j) equal the above 17-line template up to common rotation, relabeling and projective signs, let b=max_{j in O}a_j. Then rho_w>=sqrt(1-b)*rho, so

b >= 1-1/(3*rho^2) = (6*sqrt(2)-7)/24 = 0.0618867239266....

In particular, all sixteen outside-core midpoint energies cannot be zero under this exact template: that would require each core a_i >= 1-1/(4*rho^2) = (1+6*sqrt(2))/32 = 0.296415... > 1/4.

Robust version: if all seventeen normalized template lines are aligned within projective Euclidean chord distance epsilon, then rho_w >= sqrt(1-b)*(rho-epsilon). With b=0, any epsilon < rho-1/sqrt(3) = 0.0187395872737... is excluded. This is conditional on a geometric alignment, which has NOT been established for arbitrary Type E.

## [OPEN — UNCHANGED GLOBAL LEDGER]

No new label-free lower bound on total A is claimed. Retain 1/49<A<=383/504, M(F3)<=89, M(P)>=S/2-28/3, and twenty-edge mass >=2137/6. The zero-midpoint 21-line exclusion remains source-audited via Musin/Boyvalenkov. The six exceptional pairings have not been identified with D5 Q-kernel relations. Types C and D, generic e>=27, and non-isolated branches remain open. Sparse e=23/24 classification requires delta(G)>=1. Global proved range remains 40<=tau_5<=44.
