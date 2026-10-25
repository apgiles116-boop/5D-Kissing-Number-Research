# Type E: sharp 20-vector Q-comparison and strengthened six-core tradeoff

**25 October 2026.** **[PROVED EXACTLY — universal theorem]** Sharp comparison spectral floor `5/16` for twenty vectors, improving `13/44`. **[CONDITIONAL ON RETAINED TYPE-E INPUTS]** Improved safe/core slack tradeoff. **[OPEN]** Type E and the global problem.

## 1. Sharp 20-vector comparison lemma [PROVED EXACTLY]

For arbitrary `b_i in [3/4,1]`, `i=1,...,20`, define
[
K_0=operatorname{diag}(b_i^2-1/4)+	frac14mathbf1mathbf1^T-	frac15bb^T.
]
Then
[
oxed{K_0succeq (5/16)I_{20}.}	ag{1}
]
This is sharp: `b_1=b_2=3/4`, other `b_i=1`, and `x=e_1-e_2` attain equality. Total norm deficit in this example is `1/2<383/504`.

**Proof.** Put `a_i=1-b_i`, `A=sum a_i`, and split at `A=7/32`.

*If `A<=7/32`*, use the exact identity
[
K_0=operatorname{diag}(b_i^2-1/4)+	frac1{20}(mathbf1+4a)(mathbf1+4a)^T-aa^T.
]
Since `a_i<=A` and `sum a_i^2<=A^2`,
[
K_0succeq [(1-A)^2-1/4-A^2]I=(3/4-2A)Isucceq(5/16)I.
]

*If `A>=7/32`*, put `t_i=b_i-3/4=1/4-a_i`, `S=sum x_i`, `T=sum t_i x_i`, and `D=sum_i t_i(3/2+t_i)x_i^2`. Direct expansion yields
[
x^T(K_0-	frac5{16}I)x=D+	frac{11}{80}(S-	frac{12}{11}T)^2-	frac4{11}T^2.
	ag{2}
]
Weighted Cauchy gives `T^2 <= P D`, where `P=sum_i t_i/(3/2+t_i)`. Since `f(t)=t/(3/2+t)` satisfies `f(1/4)=1/7` and `f'(t)>=24/49` on `[0,1/4]`,
[
Ple20/7-(24/49)Ale20/7-(24/49)(7/32)=11/4.
]
The negative term in (2) is therefore canceled by `D`, proving (1). The two certificates are exact and require no Type-E midpoint-energy assumption.

## 2. Universal signed quartic Q-rank theorem [PROVED EXACTLY]

Let `z_1,...,z_20 in R^5` with `3/4<=b_i=||z_i||^2<=1`, without assuming any pairwise correlation cap. Put
[
Q_i=z_i z_i^T-(b_i/5)I_5,qquad K_{ij}=langle Q_i,Q_jangle=(z_icdot z_j)^2-b_i b_j/5.
]
Then `K>=0` and `rank K<=14`. For `E=K_0-K`, `E_ii=0`, `E_ij=1/4-(z_i.z_j)^2`, and `tr E=0`. By (1), at least six eigenvalues of `E` are at least `5/16`; the remaining fourteen sum to at most `-6(5/16)`. Hence
[
operatorname{tr}(E^2)ge6(5/16)^2+[6(5/16)]^2/14,
]
and
[
oxed{sum_{i<j}ig(1/4-(z_icdot z_j)^2ig)^2ge375/896
approx0.418526785714286.}	ag{3}
]
This improves the earlier `2535/6776` by exactly `4815/108416`. Sharpness is proved for the **comparison constant**, not asserted for (3).

## 3. Type-E application [CONDITIONAL ON RETAINED INPUTS]

In Type E, 184 of the 190 distinguished-edge pairings are raw-safe; only six core pairings can exceed `|z_i.z_j|=1/2`. Let `H_184=sum_safe (1/2-r_ij)^2`, `H_C^-=sum_{core:r<=1/2}(1/2-r_ij)^2`, and `T_C^+=sum_{core:r>1/2}(d_ij+d_ij^2)^2`, with `d_ij=r_ij-1/2`.

For each safe pair, `(1/4-r^2)^2=(1/2-r)^2(1/2+r)^2<=(1/2-r)^2`. Thus (3) implies
[
oxed{H_{184}+H_C^-+T_C^+ge375/896.}	ag{4}
]

The exact six-defect square budget `sum d_ij^2<819/10000`, individual cap `d_ij<=1/4`, and convex concentration estimate `T_C^+<12286461/100000000` were established in `tau5_typeE_lifted_triangle_defect_budget_2026-10-24.md` and `tau5_typeE_leave_one_core_out_Qrank_2026-10-25.md`. Consequently
[
oxed{H_{184}+H_C^->206963523/700000000approx0.295662175714286.}	ag{5}
]

If all six core pairings have `r>1/2`, then `H_C^-=0` and the lower bound applies directly to `H_184`. Otherwise **no** such direct conclusion is warranted. The complementary 19-vector weighted inequality is `H_184+(1/2)H_C^->755723921/2800000000+(1/4)H_OC`. No contradiction with `A<=383/504` is obtained.

**[OPEN]** Type E, Types C and D, generic `e>=27`, and non-isolated branches. **[UNCHANGED]** `40<=tau_5<=44`; `M(F3)<=89`; `M(P)>=S/2-28/3`; `A<=383/504`; sparse `e=23/24` classification conditional on `delta(G)>=1`.

Local exact verifier: `tau5_typeE_sharp20_Qcomparison_2026-10-25_verify.py`.
