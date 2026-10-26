# Type E: squared safe-endpoint budget and core-sensitive coercivity (2026-10-26)

**Proof ledger:** [PROVED EXACTLY] endpoint identities, aggregate trace inequalities, and core exceptional tradeoff. [CONDITIONAL ON RETAINED FRAME CERTIFICATE] numerical constant 4/21. [OPEN] Type-E exclusion; global range remains 40 <= tau_5 <= 44.

## Definitions

Twenty selected deep edges have endpoints p_i^±=m_i±z_i, with m_i·z_i=0, a_i=||m_i||², ||z_i||²=1-a_i. Let O be the 16 outside-core edges and C the 4 matching edges in F3. There are 184 safe pairs (120 OO and 64 OC); six CC pairs need not be safe. Set A_O=sum_O a_i, A_C=sum_C a_i, A=A_O+A_C<=383/504.

For a safe pair let M=m_i·m_j, Z=z_i·z_j, X=m_i·z_j, Y=z_i·m_j, h=1/2-|Z|. All four endpoint dots lie in [-1/2,1/2], so
|M+Z|+|X+Y|<=1/2 and |M-Z|+|X-Y|<=1/2.

## 1. Exact squared endpoint identity [PROVED]

Define
R_ij=(1/2){[1/4-(|M+Z|+|X+Y|)^2]+[1/4-(|M-Z|+|X-Y|)^2]} >=0.
Expanding squares gives

1/4-Z² = M²+X²+Y² + |M+Z||X+Y|+|M-Z||X-Y|+R_ij.

Thus 1/4-Z² >= M²+X²+Y². In addition, squaring the separate bounds on X+Y and X-Y gives

X²+Y² <= (1/2-max(|M|,|Z|))²+min(|M|,|Z|)² <= h²+M².

The second inequality is equality when |M|<=|Z|; otherwise the difference between its two sides is |Z|-|M|<=0.

## 2. Aggregate safe deficit [PROVED]

Let L_184=sum_safe(1/4-(z_i·z_j)²), H_184=sum_safe h_ij², F_O=sum_O z_i z_i^T, F_C=sum_C z_i z_i^T, F=F_O+F_C, T_O=sum_O m_i m_i^T, T_C=sum_C m_i m_i^T, T=T_O+T_C.

The exact directed mixing-square sum is

sum_safe[(m_i·z_j)²+(z_i·m_j)²] = tr(T_O F)+tr(T_C F_O)
=tr(T F_O)+tr(T_O F_C).

Consequently

L_184 >= tr(T_O F)+tr(T_C F_O)+sum_safe(m_i·m_j)².

The difference equals the sum of the explicitly nonnegative absolute-product and R_ij terms above. This is a D5-independent second-order endpoint/defect bridge.

## 3. Core-sensitive raw-safe slack [PROVED; coefficient conditional]

The squared bound gives
H_OO >= tr(T_O F_O)-sum_{i<j in O}(m_i·m_j)².
The previous two-sided maximum bound gives
H_OO >= tr(T_O F_O)/2, H_OC >= tr(T_C F_O).
By Cauchy--Schwarz,
sum_{i<j in O}(m_i·m_j)² <= (A_O²-sum_O a_i²)/2 <=15 A_O²/32.

For any valid F_O >= c I, therefore,

H_184 >= c A_C + max{c A_O/2, c A_O-15 A_O²/32},
L_184 >= c A +sum_safe(m_i·m_j)².

Using the retained strict outside-16 frame certificate F_O > (4/21)I gives, for A>0,

H_184 > (4/21) A_C + max{(2/21) A_O,(4/21) A_O-15 A_O²/32},
L_184 > (4/21)A+sum_safe(m_i·m_j)².

The quadratic OO branch improves the linear OO branch when 0<A_O<64/315. This is stronger than the earlier blanket H_184 > (2/21)A whenever A_C>0.

## 4. Six-exception defect/mixing budget [PROVED]

For a CC pair let r=|z_i·z_j| and delta=(r-1/2)_+. On an exceptional pair delta>0, choose sigma=sign(z_i·z_j) and c_ij=m_i·z_j+sigma z_i·m_j. The universal *upper* endpoint constraint (also valid for deep pairs) gives

m_i·m_j+r+|c_ij|<=1/2,
so delta+|c_ij|<=-m_i·m_j<=sqrt(a_i a_j).

For the exceptional subset E of the six CC pairs,

sum_E(delta_ij+|c_ij|)^2 <= sum_E a_i a_j <= 3 A_C²/8.

The raw positive squared-correlation defect P=sum_E(r_ij²-1/4)=sum_E(delta_ij+delta_ij²) consequently obeys

P <= 3 A_C/2 + 3 A_C²/8.

The joint bound is more informative than separate bounds on raw defects and mixing: both consume the same core-midpoint budget.

## 5. Limits and reproducibility

These inequalities do **not** force A>383/504 and do **not** exclude Type E. The prior 4/21 analytic certificate is an explicit dependency; its rational verifier was rerun, but the present note does not independently reprove its full weighted-Gegenbauer analysis. Types C,D, generic e>=27, and non-isolated branches remain open. The sparse e=23/e=24 classification remains conditional on delta(G)>=1. Retain M(F3)<=89 and matching M(P)>=S/2-28/3, not older constants.

Companion verifier: tau5_typeE_safe_squared_endpoint_core_budget_2026-10-26_verify.py.
