# Type E: sharper vector-valued inverse Q rounding and residual obstruction

Date: 2026-10-30.

**[PROVED EXACTLY — universal algebra]** The inverse Q-kernel rounding estimate improves from a projective distance bound of 5h to a Euclidean **vector** distance bound of 15h/7. **[PROVED CONDITIONALLY — Type E]** Combined with the previously certified 1/360 *vector* exclusion of the core-star D5 support-plane fibre, this improves the necessary Q-residual floor by a factor >7.62. **[OPEN]** Type E itself remains unexcluded.

## Definitions and inherited lemma

For twenty unit directions assigned in pairs to the ten supports pq of K5, set O=sum_pq (u_pq^+ · u_pq^-)², V=||sum_i u_i u_i^T-4I||_F², C=tr(P_c K)>=0 (the five-cycle traceless-projector kernel residual), rho²=2C+V/10, delta=sqrt(3)(2sqrt(O)+5rho+rho²), h=rho+22delta and R=O+rho².

The previously proved inverse-Q reconstruction gives five orthogonal coordinate projectors P_p and, for each support, ||S_pq-(P_p+P_q)||_F<=h whenever h<1/10, where S_pq=uu^T+vv^T. The following improves the final rounding step.

## Exact vector rounding theorem

**[PROVED EXACTLY]** If h<1/10, there are ten orthonormal pairs f_pq^+,f_pq^- in the ten coordinate two-planes of a common orthonormal basis of R^5 such that

[
oxed{max_i|u_i-f_i|le 15h/7.}
]

Proof. Fix a support, put S=uu^T+vv^T and P=P_p+P_q. Hoffman–Wielandt gives sqrt(2)|t|<=h for t=u·v. Gram–Schmidt gives g_1=u and g_2=(v-tu)/sqrt(1-t²); write G=[g_1,g_2], Pi=GG^T. Since ||Pi-S||_F=sqrt(2)|t|, we have ||Pi-P||_F<=2h. Let L=G^T(I-P)G. Then L is PSD, tr L=||Pi-P||_F²/2<=2h² and lambda_max(L)<=2h²<1/50. The polar factor H=PG(I-L)^(-1/2) has orthonormal columns in range(P) and G^TH=(I-L)^(1/2).

For 0<=x<1, 2(1-sqrt(1-x))<=x/(1-x). Consequently,

[
|G-H|_F^2=2sum_j(1-sqrt{1-lambda_j(L)})
lerac{2h^2}{1-2h^2}le(10h/7)^2.
]

Also,

[
|v-g_2|^2=2(1-sqrt{1-t^2})
lerac{t^2}{1-t^2}
lerac{100h^2}{199}le(5h/7)^2.
]

Thus ||u-H_1||<=10h/7 and ||v-H_2||<=15h/7. Repeat for all ten supports. No geometric D5 alignment of the input is assumed.

## Exact Type-E residual improvement

The previously certified exact interval argument excludes all Type-E configurations for which every sign-aligned normalized projected vector lies within Euclidean distance 1/360 of a core-star-labeled support-plane model. (Its original statement used projective distance, but the proof only needs this vector-distance assumption.) The interval enumeration is an **upstream dependency**, not rerun in this note.

**[PROVED CONDITIONALLY]**

[
oxed{O+2C+V/10>rac{49}{1117800^2}
=rac{49}{1249476840000}
approx3.9216413167cdot10^{-11}.}
]

Suppose R<=r*=49/1117800². Then rho<=sqrt(R)<1/100. Therefore

[
hle44sqrt3sqrt O+
left(1+22sqrt3rac{501}{100}ight)ho
le Ksqrt R.
]

The rational enclosure sqrt(3)<97/56 gives

[
K^2<rac{334302852689}{7840000}<207^2.
]

Hence h<207sqrt(R)<=7/5400<1/10, so the inverse vector theorem constructs a support-plane model within 15h/7<1/360, contradicting the upstream exact certificate. The old floor 1/441000² is strengthened by the exact factor 2941225/385641>7.62.

## Projective-distance correction

**[PROVED CONDITIONALLY]** For sign-aligned unit vectors, e²=||u-f||²=2(1-|u·f|) and d²=||uu^T-ff^T||_F²=2e²-e⁴/2. The same upstream vector exclusion therefore yields

[
oxed{max_i d_i>sqrt{rac{518399}{33592320000}}>rac1{255},}
]

improving the previously stated projective radius 1/360 without any new interval search. The direct vector argument gives the stronger residual consequence above.

## Ledger

**[OPEN]** No bound yet forces R below the new positive floor. Type E, Type C, Type D, generic e>=27, and non-isolated branches remain open. The global proved range remains 40<=tau_5<=44. Sparse e=23,24 classification still requires delta(G)>=1. Retain M(F3)<=89, matching mass >=2137/6, A<=383/504, and the source-audited Musin/Boyvalenkov zero-midpoint exclusion. No six-exception/Q-kernel identification is claimed.

Companion exact-rational verifier: tau5_typeE_sharp_vector_inverse_residual_2026-10-30_verify.py.
