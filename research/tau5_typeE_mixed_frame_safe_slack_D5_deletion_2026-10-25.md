# Type E: global mixed-frame / 184-safe-slack theorem and D5 three-deletion spectrum

**2026-10-25.** **[PROVED EXACTLY]** Labeling-free mixed-frame theorem, exact D5 finite spectral enumeration. **[TEMPLATE CONDITIONAL]** D5 contact-spanning midpoint estimates. **[OPEN]** Type E and global improvement beyond 40 <= tau_5 <= 44.

## Labeling-free Type-E theorem

Let the 20 selected deep edges have endpoints x_i^± = m_i ± z_i, with m_i.z_i=0, a_i=||m_i||²<1/4, ||z_i||²=1-a_i, A=sum a_i<=383/504. Let C denote the four F3-core selected edges. Set A_C=sum_{i in C}a_i and s_C=sum_{i in C}a_i². The 184 pairs not wholly in C have no deep cross-endpoint contacts. For those pairs define h_ij=1/2-|z_i.z_j| and H=sum_safe h_ij². Define M=sum_i m_i m_i^T, Z=sum_i z_i z_i^T, R=||Z-(20-A)I/5||_F.

**[PROVED EXACTLY]**
```
2 H + (2 A/sqrt(5)) R
  >= A(1-A/5) + 3(A-A_C) + A_C²-s_C
  >= (2137/2520) A.
```
This is a necessary tradeoff, not a Type-E contradiction. It requires no D5 labeling.

**Proof.** For each zero-contact pair, write c=m_i.m_j, p=m_i.z_j, q=z_i.m_j, r=|z_i.z_j| and h=1/2-r. The four cross-endpoint bounds in [-1/2,1/2] give |p+q|<=h-c, |p-q|<=h+c, |c|<=h. Hence p²+q²<=h²+c²<=2h². Orthogonality m_i.z_i=0 gives tr(MZ)=sum_{i<j}[(m_i.z_j)²+(m_j.z_i)²]. For each of the six core pairs, Cauchy gives p²+q²<=a_i(1-a_j)+a_j(1-a_i). Summing these six bounds yields
```
tr(MZ) <= 2H + 3A_C - A_C²+s_C.
```
Because M is PSD with trace A, ||M-AI/5||_F<=2A/sqrt(5). Cauchy for the trace-free parts of M,Z gives
```
tr(MZ) >= A(20-A)/5 - (2A/sqrt(5))R.
```
Combine and rearrange. Since A_C²>=s_C, A>=A_C and A<=383/504, the rational lower bound follows. QED.

**[EXACT IDENTITY]** The raw frame anisotropy is determined by the squared-correlation mass:
```
R²=2 sum_{i<j}(z_i.z_j)²-60+6A-A²/5+sum_i a_i².
```
**[TIGHT-FRAME CONDITIONAL]** R=0 implies H >= (2137/5040) A, with stronger positive corrections retained above. R=0 is NOT assumed for arbitrary Type E.

## Exact D5 deletion-spectrum certificate

Take the 20 projective D5 lines v_ab^±=(e_a±e_b)/sqrt(2). For any line v, the 12 lines with |v.w|=1/2 have sum ww^T=diag(3,3,2,2,2), up to permutation.

**[PROVED EXACTLY — 220 finite cases]** Deleting any <=3 of the 12 neighbors leaves a positive-definite frame with
```
lambda_min >= gamma=(3-sqrt(5))/2.
```
The bound is attained by some triple deletions. Fix v=(e_1+e_2)/sqrt(2). The 220 triple deletions have exactly six characteristic polynomials, with multiplicities:
```
96  (x-2)(2x²-8x+7)(2x²-6x+3)/4
48  (x-1)(2x-5)(2x-3)(2x²-8x+7)/8
24  (x-3)(x-2)²(x-1)²
24  (x-2)²(x-1)(2x²-8x+7)/2
16  (x-3)(2x-3)²(2x²-6x+3)/8
12  (x-2)³(x²-3x+1).
```
All roots are >=gamma; the last row attains gamma. Fewer deletions only increase the PSD frame sum. Exact SymPy enumeration and polynomial checks are provided in the companion verifier.

**[D5 TEMPLATE CONDITIONAL]** If the normalized projected lines z_i/sqrt(1-a_i) form the exact D5 set, then for every i outside the four-edge core,
```
a_i <= (2/3) sum_{j: |v_i.v_j|=1/2} h_ij².
```
For i inside the core, after deleting at most three potentially exceptional neighbors,
```
a_i <= [2(3+sqrt(5))/3] sum_{j: |v_i.v_j|=1/2, {i,j} not subset C} h_ij².
```
Indeed the corresponding raw-neighbor frame is >=(3/4)*2 I or >=(3/4)*gamma I, while each |m_i.z_j|<=h_ij. These are quantitative contact-spanning stability inequalities, **not** a D5 labeling theorem for arbitrary Type E.

## Status

**[RETAINED]** M(F3)<=89, matching mass >=S/2-28/3, A<=383/504, six raw core exceptions, previous core squared defect <19/250, and 184-safe squared mass >12938492114773/504094752000. **[OPEN]** An opposing upper bound on H and R strong enough to contradict the mixed-frame inequality, Type E, Types C/D, generic e>=27, non-isolated cases. The e=23/24 graph classification still assumes delta(G)>=1. Global proved range: 40<=tau_5<=44.

Local full research note: tau5_typeE_mixed_frame_safe_slack_D5_deletion_2026-10-25.md.
