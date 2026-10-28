# D5 sparse-eight Q circuits and safe-pair incidence bridge (2026-10-28)

**[PROVED EXACTLY — standalone D5 algebra and finite combinatorics].** Applications to Type E are **[CONDITIONAL]** on the upstream rounded-D5 labeling/alignment certificates. **[OPEN]** No new Type-E exclusion. Global proved range remains **40 <= tau_5 <= 44**.

For the 20 projective D5 roots x_ij^±=(e_i±e_j)/sqrt(2), let Q(x)=xx^T-(||x||²/5)I. Define R_ij=Q(x_ij^+)+Q(x_ij^-)=E_ii+E_jj-(2/5)I. If s_ij=c_ij^++c_ij^-, t_ij=c_ij^+-c_ij^-, d_i=sum_{j!=i}s_ij, then the **exact SOS identity** is

||sum c_ij^± Q(x_ij^±)||_F² = (1/4)sum_i(d_i-mean(d))² + (1/2)sum_ij t_ij².

Thus a kernel relation must have c_ij^+=c_ij^- and equal weighted degrees at the five coordinates. The full 20-line Q-Gram has nonzero eigenvalues 3/2 (multiplicity 4) and 1 (multiplicity 10), and six zeros. An explicit minimum-norm right inverse for traceless symmetric H is c_ij^±=(H_ii+H_jj)/3 ± H_ij, with ||c||²=||H||_F²-(1/3)sum H_ii².

**Shortest kernel circuits:** Every nonzero relation uses at least eight root lines. Exactly eight lines occur only for (i) four coordinate supports forming a four-cycle, with alternating weights +1,-1,+1,-1 on both root signs, or (ii) a triangle plus its complementary disjoint edge, with weights 1,1,1,2 on both root signs. There are 15 cycle patterns and 10 triangle-plus-edge patterns. The latter is a **positive tight-frame relation**: its eight weighted root lines sum to 2I_5 in outer products.

Exhaustive exact combinatorics over all 4,845 sixteen-line and 1,140 seventeen-line D5 subsets gives the number-of-retained-eight-line-circuits histograms:

- 16 lines: {1:960, 2:2160, 3:360, 4:960, 5:360, 8:30, 9:15}. In 240 cases no four-cycle survives, but a positive triangle-plus-edge circuit does.
- 17 lines: {3:80, 4:640, 5:240, 8:120, 9:60}. Every case has at least two four-cycle circuits.

**[NEW EXACT LOCAL CORRELATION IDENTITY]** For eight arbitrary vectors y_p indexed by a triangle-plus-edge pattern, with weights c_p=(2,2,1,1,1,1,1,1), set a_p=1-||y_p||², B=sum c_p a_p, A_T=sum of a_p over the six triangle lines, and R=sum c_p Q(y_p). Then

sum_{p<q} c_p c_q (y_p·y_q)² = 3-A_T+B²/10-(1/2)sum c_p² a_p²+(1/2)||R||_F².

The exact D5 template has 12 half-contact pairs (between the three triangle support groups) and 16 zero-correlation pairs. If C is the unweighted squared-correlation sum on those 12 contacts and N the weighted sum on the other 16, then

sum_contacts[1/4-(y_p·y_q)²] = N+A_T-B²/10+(1/2)sum c_p²a_p²-(1/2)||R||_F².

**[CONDITIONAL TYPE-E CONSEQUENCE]** If the sixteen isolated deep-edge projected directions admit a justified sixteen-line D5 labeling, all 28 pairings in such an eight-line circuit lie among the 120 isolated-isolated safe Walsh blocks (a subset of the 184 safe pairings), entirely avoiding the six exceptional F3 core pairings. For original endpoints m_p±y_p, the four cross-endpoint kissing constraints imply |y_p·y_q|<=1/2-m_p·m_q. This yields a concrete local eight-line polynomial/KKT test coupling safe contacts, noncontact leakage, midpoint Gram entries and the Q residual; no contradiction has been established.

For an aligned eight-line template with epsilon_R²=sum||y_p-x_p||² and b_R=sum(1-||y_p||²)>=0, the exact Q perturbation identity gives ||R||_F² <= 14(2 epsilon_R²+(3/10)b_R²) for the positive circuit (8 instead of 14 for the signed cycle).

**Proof status:** The D5 algebra, minimum-support classification, exact histograms and local identity are proved independently. Type-E use depends on upstream geometric certificates, not recertified here. Types C/D, generic e>=27 and non-isolated branches remain open; e=23/24 sparse classification retains delta(G)>=1. Do not replace retained F3<=89 or matching S/2-28/3 by obsolete weaker versions.

Verifier: research/tau5_D5_sparse8_Q_incidence_2026-10-28_verify.py
