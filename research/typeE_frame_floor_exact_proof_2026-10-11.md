# Type-E Q-frame floor: exact proof (2026-10-11)

**[PROVED EXACTLY, GIVEN RETAINED A<=383/504]** Fix the one mass-selected set of 20 deep edges. Let a_i=||m_i||²<1/4, A=Σa_i, u=Σa_i², b_i=1-a_i, and R2=Σ_{i<j}(z_i·z_j)².

Set Q_i=z_i z_iᵀ-(b_i/5)I. Expanding ||ΣQ_i||² gives

R2=30-3A+A²/10-u/2+(1/2)||ΣQ_i||².

At fixed A, the maximum of u with 0<=a_i<=1/4 is k/16+(A-k/4)², k=floor(4A). Proof: transferring weight from a smaller interior entry to a larger interior entry increases the sum of squares, until all but one entries are at 0 or 1/4.

For k/4<=A<=(k+1)/4, the resulting lower-bound function f_k(A) has derivative -3-(4/5)A+k/4<0. Thus it is minimized at A*=383/504=3/4+5/504, k=3, yielding

**R2 > 8790283/317520 = 27.684186822877...**

The strictness follows because actual deep edges have a_i<1/4, whereas the scalar equality case requires three a_i=1/4. This improves the prior 27.489246... floor that used only u<=A².

**[OPEN]** This is a necessary bound, not a Type-E elimination. The scalar equality pattern is not asserted to satisfy the stronger mass polynomial or geometric contacts. The global range remains 40<=tau_5<=44.
