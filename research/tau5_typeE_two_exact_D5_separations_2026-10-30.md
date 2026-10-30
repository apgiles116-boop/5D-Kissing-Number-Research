# Type E: exact D5 root and support-fibre separation improvements (2026-10-30)

## Proof status

**[PROVED BY EXACT FINITE CERTIFICATE — conditional on the retained Type-E reduction]** Let x_i^±=m_i±z_i be the twenty selected deep edges, a_i=||m_i||² in [0,1/4], A=sum a_i≤383/504, and u_i=z_i/sqrt(1-a_i). The isolated center v is a unit vector satisfying |v·z_i|≤1/2.

**Root-line separation.** For every rotated, signed and relabeled D5 twenty-root-line template r_i=(e_p±e_q)/sqrt(2),

\[
\boxed{\max_i\|u_iu_i^T-r_ir_i^T\|_F>\sqrt2/8.}
\]

This improves the earlier approximately 0.16270 separation to approximately 0.17678. Only the center and midpoint-energy hypotheses are needed.

**Support-plane-fibre separation.** For every core-star-labeled model f_i consisting of ten orthonormal pairs in the ten coordinate two-planes of a common orthonormal basis,

\[
\boxed{\max_i\|u_iu_i^T-f_if_i^T\|_F>1/360.}
\]

This improves the previous 1/650 radius by a factor 65/36. The full 184 raw-safe-pair incidence is used.

**[CONDITIONAL CONSEQUENCE]** Together with the previously established inverse Q-kernel rounding theorem, the support-fibre result improves the necessary residual floor to

\[
\boxed{O+2C+V/10>1/441000^2.}
\]

**[OPEN]** None of these statements eliminates arbitrary Type E. The global proved range remains 40≤τ₅≤44. Types C, D, generic e≥27 and non-isolated branches remain open. Sparse e=23/24 graph classification still assumes δ(G)≥1. Retain M(F3)≤89, matching mass ≥2137/6, and A≤383/504.

## Proof of the root-line separation

Fix any D5 comparison template, rotate coordinates and sort p_i=v_i² in decreasing order. Then p_i≥0 and sum p_i=1. For each coordinate pair i<j, one D5 root line has squared center contact

\[
s_{ij}=(\sqrt{p_i}+\sqrt{p_j})^2/2.
\]

If the maximum projector Frobenius distance were at most sqrt(2)/8, the difference of the corresponding squared center contacts would be at most 1/8 (the operator norm of a rank-one projector difference is its Frobenius norm divided by sqrt(2)). Since (1-a_i)(v·u_i)²≤1/4 and a_i≤1/4, each s_ij≤11/24. Moreover the associated midpoint energy must be at least g(s_ij), where g(s)=0 for s≤3/8 and g(s)=(8s-3)/(8s-1) for s>3/8. The ten selected root lines are distinct, so

\[
A\ge\sum_{i<j}g(s_{ij}).
\]

The companion exact integer/rational verifier exhaustively proves that no sorted p with sum one can simultaneously satisfy s_12≤11/24 and sum g(s_ij)≤383/504. It visits 111,395 subsimplices, excludes 1,636 by the center-domain bound and 54,062 by a strict energy lower bound, with no unresolved cells. This proves the strict root separation.

## Proof of the support-fibre separation

Suppose the projector distances to a core-star-labeled support-plane model are at most ε=1/360. Independent line-sign choices ensure ||u_i-f_i||≤ε. For each support e of K5 let t_e in [0,1] be the squared-coordinate imbalance of its orthonormal pair.

There are 24 fully safe meeting-support pairs, after discarding the six star-star support pairs containing the potentially exceptional core-core contacts. For each safe meeting-support pair e,f, choose the two model lines of maximum absolute contact. Raw safety and perturbation imply

\[
\sqrt{(1-a_i)(1-a_j)(1+t_e)(1+t_f)}\le1+4\varepsilon.
\]

Set c=(1+4ε)²=8281/8100. For a,b in [0,1/4], 1/(1-a)≤1+4a/3 and ab≤(a+b)/8, so

\[
1/((1-a)(1-b))\le1+14(a+b)/9.
\]

Hence t_e+t_f≤(c-1)+(14c/9)(a_i+a_j). The 24 safe support blocks have degrees three on the four star supports and six on the six nonstar supports. Summing yields the new rational estimate

\[
T_C+2T_N\le8(c-1)+(28c/9)A
\le3406199/1312200.
\]

For every support, one safe neighbor and a_i≤1/4 give

\[
t_e\le16c/9-1=14899/18225<325/397.
\]

Set κ=13/25. The inequality sqrt(1-t²)≥1-κt holds throughout this interval because 2κ/(1+κ²)=325/397. The center constraints on the two orthonormal lines in support ij imply p_i+p_j≤2/3+3ε. With η=3ε=1/120, the difference of their squared center contacts then gives

\[
t_{ij}\ge
\frac{[(\sqrt{p_i}+\sqrt{p_j})^2-2/3-\eta]_+}
{p_i-p_j+(26/25)\sqrt{p_ip_j}}.
\]

The quotient is defined as zero when its denominator vanishes. An exact rational simplex certificate proves that, over all sorted p with sum one and p_1+p_2≤2/3+1/120, the sum of these ten quotients is at least 13/5. The certificate visits 988,525 subsimplices, excludes 73,371 by the center domain and 420,892 by interval lower bounds, and has no unresolved cells. All square-root bounds use integer isqrt floors/ceilings and all certification comparisons use exact fractions.

Therefore T_C+T_N≥13/5, while T_N≥0 and the safe-block inequality forces T_C+2T_N≤3406199/1312200. Their exact contradiction margin is

\[
13/5-3406199/1312200=5521/1312200>0.
\]

Thus the support-plane separation is strict.

## Residual corollary and limitations

The prior inverse-Q rounding theorem gives distance≤5h when h<1/10, where h=ρ+22δ and ρ²=2C+V/10. Hence h>1/1800; the h≥1/10 case is immediate. The existing universal estimate h<245 sqrt(O+ρ²) when ρ≤1 (and the ρ>1 case is trivial) gives O+2C+V/10>1/441000².

The new estimates do not prove arbitrary Type-E configurations are close to D5, nor identify the six exceptional pairings with the six Q-kernel relations. The residual floor remains too small for an exclusion.

Exact verification scripts:
- research/tau5_typeE_D5_root_energy_1over8_verify.py
- research/tau5_typeE_D5_fibre_1over360_verify.py
