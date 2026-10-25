# Type E: exact zero-contact/midpoint-covariance SOS decomposition (2026-10-25)

**[PROVED EXACTLY under retained Type-E hypotheses]** A uniform strengthening of the earlier mixed-frame theorem. **[OPEN]** Type E elimination and improvement of 40 <= tau_5 <= 44.

## Definitions

For twenty selected deep edges x_i^± = m_i ± z_i, put a_i=||m_i||^2<1/4, A=sum a_i<=B=383/504. The four F3 matching edges form core C; the remaining sixteen form O. Put Ac=sum_C a_i, Ao=A-Ac, sc=sum_C a_i^2, so=sum_O a_i^2. Let M=sum m_i m_i^T, Z=sum z_i z_i^T, V=tr(M^2), M0=M-(A/5)I, Z0=Z-((20-A)/5)I, sigma=||M0||_F=sqrt(V-A^2/5), R=||Z0||_F.

For the 184 zero-cross-contact pairings outside C, put r_ij=|z_i.z_j|<=1/2, h_ij=1/2-r_ij, H=sum_safe h_ij^2. Write c_ij=m_i.m_j, p_ij=m_i.z_j, q_ij=z_i.m_j. The endpoint box constraints imply |p+q|<=h-c, |p-q|<=h+c and |c|<=h after orienting r>=0. Thus e_ij=h^2+c^2-p^2-q^2=1/2[((h-c)^2-(p+q)^2)+((h+c)^2-(p-q)^2)]>=0.

Set E_safe=sum_safe e_ij >=0; E_core=sum_core [a_i(1-a_j)+a_j(1-a_i)-p_ij^2-q_ij^2]>=0 by Gram Cauchy; E_cov=sigma R+<M0,Z0>>=0 by Frobenius Cauchy.

## Exact identity [PROVED EXACTLY]

H + sigma R =
  A(1-A/5)
  + Ao(3-Ac-Ao/2)
  + (Ac^2-sc)/2 + so/2 + (A^2-V)/2
  + E_safe + E_core + sum_core c_ij^2 + E_cov.    (1)

Proof: tr(MZ)=sum_(i<j)(p_ij^2+q_ij^2)=A(20-A)/5+<M0,Z0>. On safe pairs, sum(p^2+q^2)=H+sum_safe c^2-E_safe. Also sum_safe c^2=(V-sc-so)/2-sum_core c^2 and sum_core(p^2+q^2)=3Ac-Ac^2+sc-E_core. Substitute and collect. All correction terms on the right of (1) are nonnegative because A<=B<1, sc<=Ac^2, V<=A^2, and Gram/endpoint inequalities.

Since sigma<=2A/sqrt(5) and 3-Ac-Ao/2>=3-B=1129/504, (1) yields

**H + (2A/sqrt(5)) R >= (2137/2520) A + (1129/504) Ao.**    (2)

This uniformly strengthens the earlier theorem 2H+(2A/sqrt(5))R >=(2137/2520)A. For R=0 the coefficient on H doubles, and the outside-core midpoint-energy penalty remains explicit. Equivalently Ao <= (504/1129)[H+(2A/sqrt(5))R-(2137/2520)A].

**[OPEN]** There is no upper bound on H and R jointly that makes (2) contradictory. No D5 labeling, Type-E elimination, or improvement of tau_5 is claimed. The decomposition supplies endpoint polynomial slacks, 2x2 Gram-minor slacks, and covariance slacks for a future finite rank-five KKT/SOS certificate.

Retained inputs unchanged: M(F3)<=89; M(P)>=S/2-28/3; twenty-edge mass>=2137/6; A<=383/504; six possible raw exceptional core pairings; Musin--Boyvalenkov zero-midpoint exclusion. Types C,D, generic e>=27 and non-isolated branches remain open. Sparse e=23/24 classification remains conditional on delta(G)>=1.

Exact symbolic verifier: research/tau5_typeE_refined_mixed_frame_SOS_2026-10-25_verify.py.
