# Type E: six-deep / 474-safe Walsh edge-frame conservation (2026-10-30)

**[PROVED EXACTLY — universal algebra]** Let twenty selected deep edges have endpoints x_i^±=m_i±z_i, with m_i·z_i=0, a_i=||m_i||², ||z_i||²=1−a_i, A=Σa_i, U=Σa_i². Define

W_ij=(m_i·m_j)²+(m_i·z_j)²+(z_i·m_j)²+(z_i·z_j)².

Four-character Walsh orthogonality gives Σ_{σ,τ}(x_i^σ·x_j^τ)²=4W_ij. Set S_i=m_i m_iᵀ+z_i z_iᵀ; then tr S_i=1, tr S_i²=a_i²+(1−a_i)², W_ij=tr(S_i S_j). With V_edge=||Σ_i S_i−4I₅||²≥0, exact frame-potential expansion gives

**Σ_{i<j}W_ij=30+A−U+V_edge/2.** (1)

In particular A−U=Σ_i a_i(1−a_i)≥3A/4.

**[PROVED EXACTLY — conditional on retained Type-E 184-safe/six-core incidence]** Choose *any combinatorial* K5 support labeling with the four F3 matching-core edges on four star supports. Among 190 selected-edge pairings, 10 have the same support, 60 disjoint supports, and 120 meeting supports. Six core-core meeting pairings are potentially exceptional; the other 114 meeting pairings are fully safe. Define W70=Σ_{same/disjoint}W_ij, X6=Σ_{six core}(W_ij−1/4), and S114=Σ_{114 safe meeting}(1/4−W_ij)≥0. Then (1) gives the exact second-order identity

**W70+X6=A−U+V_edge/2+S114.** (2)

No geometric D5 alignment or six-exception/Q-kernel correspondence is assumed.

Among the 24 endpoint contacts in the six core-core pairings are **six actual nonmatching F3 deep contacts** (distributed as zero, one or two per core pairing) and **18 safe contacts**. The 114 safe meeting blocks contribute 456 more safe endpoint contacts, totaling **474 safe meeting-support contacts**. For safe t, set d(t)=1/4−t²≥0; for deep t<−1/2, set e(t)=t²−1/4>0. The four-contact Walsh identity gives S114=(1/4)Σ_{456 safe}d(t) and X6=(1/4)Σ_{6 deep}e(t)−(1/4)Σ_{18 core safe}d(t). Therefore

**W70+(1/4)Σ_{6 deep}(t²−1/4) = A−U+V_edge/2+(1/4)Σ_{474 safe}(1/4−t²).** (3)

This is an exact six-deep/474-safe conservation law. All displayed terms are nonnegative. The zero-midpoint D5 template saturates it algebraically; no actual Type-E code attaining equality is claimed.

**[PROVED EXACTLY — conditional Type-E mass/Q consequence]** For F(t)=28t²(t²−1/4) on deep contacts, F(t)/112≤(t²−1/4)/4≤F(t)/28. Let M_extra=M(F3)−M(P) be the mass of the six nonmatching F3 deep contacts, and S474=(1/4)Σ_{474 safe}(1/4−t²). Then

A−U+V_edge/2+S474 ≤ W70+M_extra/28. (4)

Decompose W70=O_z+D_z+T70, where O_z,D_z are the same/disjoint squared projected correlations, and T70 is the sum of the three midpoint/mixed squared correlations over those 70 pairings. The weighted Petersen Q-SOS identity E=V_z+12C_z≥8O_z+4D_z implies O_z+D_z≤E/4. Hence the **second-order mass–Walsh–Q bridge**

**A−U+V_edge/2+S474 ≤ T70+E/4+M_extra/28.** (5)

For each safe contact, −F(t)=28t²(1/4−t²)≤7(1/4−t²), so S474≥N474/28, where N474 is the nondeep Delsarte slack of these 474 contacts. Therefore

**28(A−U+V_edge/2)+N474 ≤ 28T70+7E+M_extra.** (6)

**[VERIFIED]** The companion exact Fraction checker confirms the 10/60/114/6 partition, four-contact Walsh identity, 20-edge frame identity on a non-D5 rational family with A<567/1000 (not Type-E safe), and exact D5 saturation. The proof is the universal algebra, not finite sampling.

**[OPEN]** These are necessary identities/inequalities, not a Type-E contradiction. The outstanding task is a joint bound on T70 and M_extra using F3 endpoint-charge/signed-triangle restrictions and isolated-center harmonic slack. Preserve M(F3)≤89, M(P)≥S/2−28/3, historical A≤383/504, stronger conditional A<567/1000, Musin/Boyvalenkov zero-midpoint exclusion, and global 40≤τ₅≤44. Types C,D, generic e≥27 and non-isolated branches remain open; e=23/24 classification requires δ(G)≥1.

Verifier: `research/tau5_typeE_Walsh_edge_frame_conservation_2026-10-30_verify.py`.
