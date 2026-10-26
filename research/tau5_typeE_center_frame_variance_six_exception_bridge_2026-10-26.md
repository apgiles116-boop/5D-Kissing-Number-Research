# Type E: exact center-frame variance / six-exception bridge (2026-10-26)

**Status.** [PROVED EXACTLY] The general frame and endpoint inequalities below. [CONDITIONAL ON RETAINED TYPE-E CERTIFICATES] The numerical low-energy consequence. [OPEN] Type E exclusion and tau_5.

## Frame-variance identity and uncertainty bound

For 20 vectors z_i in R^5 with ||z_i||^2=1-a_i, 0<=a_i<1, A=sum a_i<1, and a unit center x, let

F_z=sum z_i z_i^T, V_z=||F_z-(20-A)I/5||_F^2,
u_i=z_i/sqrt(1-a_i), F_21=xx^T+sum u_i u_i^T,
V_21=||F_21-21I/5||_F^2.

The exact trace identity is

S_z=sum_{i<j}(z_i.z_j)^2
=30-3A+A^2/10-(1/2)sum a_i^2+V_z/2. (1)

Let W=sum a_i u_i u_i^T, which is PSD and tr W=A. Then ||W-AI/5||_F<=2A/sqrt(5), while ||xx^T-I/5||_F=2/sqrt(5). The exact identity

F_21-21I/5 = (F_z-(20-A)I/5)+(W-AI/5)+(xx^T-I/5)

therefore implies sqrt(V_z)+sqrt(V_21)+2A/sqrt(5)>=2/sqrt(5).

For the 21 unit vectors (x,u_1,...,u_20), set
P=sum_{i<j}[s_ij(s_ij-1/4)]_+, s_ij=(u_i.u_j)^2.
The dimension-five normalized Gegenbauer expansion

t^4-t^2/4=(1/28)P_0(t)+(1/3)P_2(t)+(8/21)P_4(t),
P_2(t)=(5t^2-1)/4

and positivity of the degree-four kernel give V_21<=(24/5)P.
Consequently,

sqrt(V_z)+sqrt(24P/5)>=2(1-A)/sqrt(5). (2)

This is a direct second-order link between 20-line projected Q/frame variance and the 21-line positive quartic defect, without any D5 labeling.

## Endpoint-mixing correction to safe defect

For a safe pair of deep edges p_i^±=m_i±z_i, put
M=m_i.m_j, Z=z_i.z_j, X=m_i.z_j, Y=z_i.m_j.
The four cross-endpoint dots in [-1/2,1/2] give
|M+Z|+|X+Y|<=1/2 and |M-Z|+|X-Y|<=1/2.
Thus |Z|+rho<=1/2, where rho=|M|+||X|-|Y||.
Writing w=(1-a_i)(1-a_j), s=Z^2/w, one gets

[s(s-1/4)]_+ <= [a_i+a_j-a_i a_j-4rho+4rho^2]_+/(16w^2). (3)

For the non-deep center, rho_0i=|x.m_i| and similarly

[s_0i(s_0i-1/4)]_+ <= [a_i-4rho_0i+4rho_0i^2]_+/(16(1-a_i)^2). (4)

These inequalities keep midpoint Gram and endpoint mixing terms instead of dropping them.

## Type-E six-exception consequence

For Type E (16 outside + four core deep edges), retain the 184 safe pairs, 20 center pairs, and six possibly exceptional core pairs. The retained collective core bounds sum delta_ij<=A_C and sum delta_ij^2<=A_C^2/4, with delta_ij=(|z_i.z_j|-1/2)_+, imply for A<=t<1

P<=K_O(t)A_O+K_C(t)A_C<=K_C(t)A,
K_O(t)=20/[16(1-t)^2],
K_C(t)=[17+(1+t)^2(7+t)]/[16(1-t)^2].

Together with (2),

sqrt(V_z)+sqrt((24/5)K_C(t)A)>=2(1-A)/sqrt(5). (5)

At t=1/40, exact fractions are
K_C=1560361/973440,
24 K_C t=1560361/1622400,
(99/100)^2-24 K_C t=743831/40560000>0.

Thus for any such Type-E configuration with A<=1/40,

V_z>576/3125=0.18432,
S_z>3001691/100000=30.01691. (6)

For the last inequality use (1), sum a_i^2<=A^2, and monotonicity of 30-3A-(2/5)A^2. The exact D5 20-line frame has V_z=0 and S_z=30 at A=0, so the low-energy branch is quantitatively non-tight, **not** identified with D5.

**Limitations.** Both (5) and (6) are necessary conditions, not Type-E exclusions. An upper bound on S_z or a finite four-core KKT certificate is still missing. Retain 40<=tau_5<=44, M(F3)<=89, M(P)>=S/2-28/3, A<=383/504, and all unresolved Type C/D, generic e>=27 and non-isolated branches.
