# Type E: exact disjoint-defect midpoint-dispersion frame correction

Date: 2026-10-24. Proof status: **[PROVED EXACTLY]** algebraic midpoint/frame lemma; **[CONDITIONAL TYPE E]** near-saturated disjoint-defect branch; **[OPEN]** Type E exclusion and global tau_5.

## Exact midpoint theorem

For 20 selected deep edges let a_i=||m_i||^2 in [0,1/4], A=sum a_i, and delta_ij=(|z_i.z_j|-1/2)_+. The necessary endpoint inequality m_i.m_j+|z_i.z_j|<=1/2 implies a_i a_j>=delta_ij^2. Choose two **disjoint** candidate defect pairs with p=delta_ij and q=delta_kl, and define E=A-2(p+q)>=0. Then

**sum_i a_i^2 <= 2(p^2+q^2)+max{4pE+E^2, 4qE+E^2, E/4}.** (1)

Proof: Write a_i+a_j=2p+t_1, a_k+a_l=2q+t_2, and r=E-t_1-t_2>=0. The two pair-square sums are bounded by (2p+t_1)^2-2p^2 and (2q+t_2)^2-2q^2. The other 16 squared energies sum to at most r/4. The resulting convex quadratic in (t_1,t_2) attains its maximum over the triangle t_1,t_2>=0, t_1+t_2<=E at (E,0),(0,E),(0,0). This proves (1). Equality is possible in the midpoint-only relaxation at E=0; no physical kissing configuration is asserted.

## Global frame coupling [CONDITIONAL TYPE E]

Retain B=383/504, S_cap=3/16+(B-3/4)^2=47653/254016 and the frame inequality

sum_{i<j}(z_i.z_j)^2 >= 30-3A+A^2/10-(1/2)sum a_i^2.

For any two disjoint core defects p,q, put E_B=B-2(p+q). Because the frame lower expression decreases with A<=B and the bound (1) increases with E, one obtains

**sum_190(z_i.z_j)^2 >= 30-3B+B^2/10 - (1/2)min{S_cap, 2(p^2+q^2)+max(4pE_B+E_B^2,4qE_B+E_B^2,E_B/4)}.** (2)

This is an exact functional second-order correction linking disjoint exceptional defects to the global frame floor. No D5 labeling is assumed.

## Rational near-saturation branch [CONDITIONAL TYPE E]

Let b=B/2=383/1008, h=1/1000. If some disjoint core defects satisfy p+q>=b-h, then s=p+q is in (1/4,b], E_B<=2h, and p^2+q^2<=1/16+(b-1/4)^2. Therefore

sum a_i^2 <= S_near=2[1/16+(b-1/4)^2]+2h+4h^2
=1276298377/7938000000 < S_cap.

Consequently,

**sum_190(z_i.z_j)^2 >= 146575669291/5292000000 = 27.6975943482615...**

This improves the unconditional capped floor L=8790283/317520 by exactly 212857873/15876000000=0.0134075253842....

Using the retained D0=1780062775/4032758016, Q=sum_six delta^2<40949/500000, and six exceptional squared correlations <=3/2+D0+Q, this branch gives

**sum_184-safe(z_i.z_j)^2 > 32355694067773/1260236880000 = 25.6742955084547...**

compared with the previous unconditional 25.6608879830705....

## Proof ledger

- **[PROVED EXACTLY]** Midpoint dispersion inequality (1), its convex vertex proof, and algebraic frame coupling (2) under the stated inputs.
- **[CONDITIONAL TYPE E]** Explicit near-saturation branch and exact rational safe-mass bound.
- **[NOT PROVED]** That the branch holds for all Type E; a safe-pair upper bound; Type E elimination; D5 labeling; any new global bound on tau_5.
- **[UNCHANGED]** 40<=tau_5<=44, M(F3)<=89, M(P)>=S/2-28/3, A<=383/504; Types C,D and generic e>=27 remain open.

A full expanded note and rational verifier are retained as companion local artifacts.