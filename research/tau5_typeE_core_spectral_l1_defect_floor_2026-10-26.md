# Type E: four-core spectral L1 defect budget and improved energy floor

Date: 2026-10-26. Full exact working note and verifier are available as conversation attachments.

**[PROVED EXACTLY]** Four-vector negative-Gram inequality. For arbitrary four real vectors m_1,...,m_4 in any Euclidean space,

    sum_{i<j} max(-m_i.m_j,0) <= sum_i ||m_i||^2 = A_C.                 (1)

Proof: Let E contain pairs with negative dot products. For a real x in R^4, drop positive x_i x_j and include all negative cross-sign pairs. If p and q entries have opposite signs, p+q<=4 and pq<=4. Cauchy-Schwarz gives
    -sum_{ij in E} x_i x_j <= (sum_{x_i>0}x_i)(sum_{x_j<0}|x_j|)
                          <= sqrt(pq)||x_+||||x_-|| <= ||x||^2.
Thus 2I+Adj(E) is PSD. Apply coordinatewise to the midpoint vectors. The constant 1 is sharp for (v,v,-v,-v).

**[PROVED EXACTLY GIVEN TYPE-E ENDPOINT CONSTRAINTS]** For the four matching edges in F3, let delta_ij=(|z_i.z_j|-1/2)_+. On exceptional pairs E={ij:delta_ij>0}, set sigma_ij=sign(z_i.z_j) and c_ij=m_i.z_j+sigma_ij*z_i.m_j. The two appropriate upper endpoint constraints imply
    delta_ij+|c_ij| <= -m_i.m_j.
Therefore the new *joint six-exception L1 budget* is

    sum_{ij in E}(delta_ij+|c_ij|) <= A_C.                            (2)

The retained L2 budget is sum_E(delta_ij+|c_ij|)^2 <= 3 A_C^2/8.
For the raw positive squared-correlation defect,

    P_raw=sum_{i<j in C} max((z_i.z_j)^2-1/4,0)
         <= A_C + 3 A_C^2/8.                                        (3)

This is a small-energy bound; it does not supersede the retained unconditional raw-defect cap 1780062775/4032758016.

**[CONDITIONAL ON RETAINED TYPE-E HYPOTHESES]** Improved midpoint floor. Retain the previously established universal 21-line positive quartic-defect theorem P_f>1/120, where P_f=sum_{i<j} max(s_ij(s_ij-1/4),0), s_ij=(u_i.u_j)^2. Use 20 normalized projected edge directions and the isolated center. Suppose A=sum a_i <= t=1/183, a_i=||m_i||^2. There are 184 safe edge-edge pairs, 20 center-edge pairs, and six possibly exceptional core-core pairs.

For a safe pair, w=(1-a_i)(1-a_j)>=1-(a_i+a_j)>=1-t, |z_i.z_j|<=1/2. The positive quartic defect is <=(a_i+a_j)/[16(1-t)^2]. A center-edge pair contributes <=a_i/[16(1-t)^2].

For a core pair, let u=a_i+a_j, delta=(|z_i.z_j|-1/2)_+, w=(1-a_i)(1-a_j), and s=(z_i.z_j)^2/w. Endpoint bounds give delta<=sqrt(a_i a_j)<=u/2<=t/2. Hence
    s <= (1+t)^2/[4(1-t)],
    max(s-1/4,0) <= [(1+t/2)delta+u/4]/(1-t).
Using sum_C delta<=A_C and sum_{i<j in C}(a_i+a_j)=3A_C gives
    sum_{i<j in C} max(s_ij(s_ij-1/4),0)
      <= [(1+t)^2(7+2t)]/[16(1-t)^2] A_C.

Each outside index occurs in 19 safe pairs and one center pair; each core index occurs in 16 safe pairs and one center pair. Thus
    P_f <= K_O(t) A_O + K_C(t) A_C <= K_C(t) A,
    K_O(t)=20/[16(1-t)^2],
    K_C(t)=[17+(1+t)^2(7+2t)]/[16(1-t)^2].
At t=1/183, K_C=147621527/96987072 > K_O, and exactly
    1/120 - K_C/183 = 1418789/88743170880 > 0.
This contradicts P_f>1/120. Therefore

    A > 1/183.                                                      (4)

This improves the previous A>1/200 by factor 200/183. The improvement is modest but exact. The new joint L1 constraint (2) is the more structural contribution.

**[OPEN]** Type E remains unresolved; A<=383/504. Type C, Type D, generic e>=27, and non-isolated branches remain open. Global range 40<=tau_5<=44. Retain M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass>=2137/6, and the conditional delta(G)>=1 qualification for e=23/24 classification. No D5 identification or new SDP is assumed.

**Next:** Combine (2) with homogeneous six-exception defect and global traceless-Q frame variance in a small four-core polynomial/KKT certificate.
