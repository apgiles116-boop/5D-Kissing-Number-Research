# Type E: sharp quadratic core budget, Q-floor improvement, and 21-line gap
Date: 2026-10-26. Full derivation and exact checker also supplied as local attachments.

**Proof status:** [PROVED EXACTLY] The universal negative-Gram square inequality, frame-trace floor, and universal 21-line quartic gap. [CONDITIONAL ON RETAINED TYPE-E HYPOTHESES] The exceptional-core consequences, safe squared-correlation floor, and energy floor. [OPEN] Exclusion of Type E and determination of tau_5.

## 1. Sharp negative-Gram square bound

For any Euclidean vectors m_i, with A=sum ||m_i||^2,

    sum_{i<j} [(-m_i.m_j)_+]^2 <= A^2/4.             (1)

Proof: G=(m_i.m_j) is PSD with trace A. Phi(G)=sum_{i<j}(-G_ij)_+^2 is convex. The trace-A PSD cone section is the convex hull of rank-one matrices A vv^T with ||v||=1. For such a matrix Phi=A^2 (sum_{v_i>0}v_i^2)(sum_{v_i<0}v_i^2)<=A^2/4. Equality occurs for v=(1,-1,0,...)/sqrt(2).

For four Type-E core edges, endpoint upper inequalities on the exceptional set E imply delta_ij+|c_ij|<=-m_i.m_j, where delta_ij=(|z_i.z_j|-1/2)_+ and c_ij=m_i.z_j+sign(z_i.z_j)z_i.m_j. Hence

    sum_E (delta_ij+|c_ij|)^2 <= A_C^2/4,           (2)
    P_raw=sum_E(delta_ij+delta_ij^2)<=A_C+A_C^2/4. (3)

The retained sharp four-core linear bound sum_E(delta_ij+|c_ij|)<=A_C is used in (3). The quadratic coefficient 1/4 improves the former 3/8 bound.

## 2. Exact improved Q/frame floor

For 20 z_i in R^5, ||z_i||^2=1-a_i, 0<=a_i<=1/4, A=sum a_i<=383/504,

    S=sum_{i<j}(z_i.z_j)^2
     >=30-3A+A^2/10-(1/2)sum_i a_i^2.             (4)

At fixed A, the maximum of sum a_i^2 occurs with k=floor(4A) entries 1/4 and one remainder r=A-k/4, giving k/16+r^2. The right side of (4) decreases with A on [0,383/504]. At A=383/504, k=3 and r=5/504, so

    S >= 8790283/317520 = 27.684186822877... .    (5)

This improves 17456771/635040 by exactly 131/672.

For Type E, the six core squares total at most 3/2+A_C+A_C^2/4, by (2)-(3). Therefore the 184 safe squared correlations satisfy

    S_safe >= S-3/2-A_C-A_C^2/4
           >=128429963/5080320 =25.279896345112... . (6)

This is a direct, exact six-exception bridge, but it is far from a contradiction.

## 3. Universal 21-line quartic gap

For any 21 unit vectors u_i in R^5, set s_ij=(u_i.u_j)^2 and P=sum_{i<j}[s_ij(s_ij-1/4)]_+. Then

    P > 9/625 = 0.0144.                              (7)

Proof: Write D_-=sum[-s(s-1/4)]_+, F=sum u_i u_i^T, V=||F-(21/5)I||_F^2. The Gegenbauer expansion of t^4-t^2/4 gives D_-<=P-5V/24 and V<=24P/5. Round each s to r=0 if s<=1/8, and r=1/4 otherwise. Under P<=9/625, each negative defect h=s(1/4-s) is <=9/625=(9/100)(16/100); thus d=min(s,1/4-s)<=9/100 and |s-r|<=25h/4. For positive defects |s-r|<=4s(s-1/4). Therefore

    sum |s-r| <= (41/4)P-(125/96)V.

Let E be the integer number of rounded 1/4 pairs. The frame identity gives

    |672/5+2V-E| <= 41P-(125/24)V.

Since V<=216/3125, E is 134 or 135. E=135 would imply (77/24)V<=-6/625, impossible. Thus E=134 and V<=v=2856/108125<1/36.

Let d_i=4sum_{j!=i}r_ij be integer row degrees. For every integer d, |d-64/5|>=8-3d/5, hence R=sum_i|d_i-64/5|/4>=9/5 since sum d_i=268. Writing Delta=F-(21/5)I and using Cauchy-Schwarz,

    R<=sqrt(21(21/5+sqrt(V))V)+(41/2)P-(125/48)V.

Because V<=v<1/36, sqrt((917/10)V)-(125/48)V increases on [0,v]. Consequently R<=sqrt((917/10)v)+369/1250-(125/48)v. But q=9/5-369/1250+(125/48)v=170144/108125 is positive and

    q^2-(917/10)v=631562236/11691015625>0.

Thus R<9/5, contradiction. This proves (7).

## 4. Type-E midpoint floor

Assume A<=t=1/107, normalize the 20 z_i to unit vectors and include the isolated center. The 210 pairs comprise 184 safe edge pairs, 20 center pairs, and six core pairs. For safe/center pairs, positive quartic defect is bounded by (a_i+a_j)/[16(1-t)^2]. For core pairs, with w=(1-a_i)(1-a_j)>=1-t and delta=(|z_i.z_j|-1/2)_+, the normalized square s satisfies

    s<=(1+t)^2/[4(1-t)],
    (s-1/4)_+ <=[delta+delta^2+(a_i+a_j)/4]/(1-t).

Use sum_core delta<=A_C, sum_core delta^2<=A_C^2/4<=t A_C/4, and sum_core(a_i+a_j)=3A_C. Summing all pair classes gives

    P <= K_O(t) A_O+K_C(t) A_C <=K_C(t)A,
    K_O(t)=20/[16(1-t)^2],
    K_C(t)=[17+(1+t)^2(7+t)]/[16(1-t)^2].

At t=1/107,

    K_C(t)=29573731/19236032,
    9/625-K_C(t)/107=40716941/1286409640000>0.

This contradicts (7), proving the **conditional Type-E floor A>1/107**. This improves the previous 1/183, but is much smaller than the retained upper bound 383/504.

**[OPEN]** Type E remains unresolved. Other branches (C, D, generic e>=27, non-isolated) remain open. The proved global working range is 40<=tau_5<=44. Retain M(F3)<=89, matching mass >=S/2-28/3, and 20-edge mass >=2137/6. Sparse e=23,24 graph classification requires delta(G)>=1. No D5 labeling, uniqueness claim, or new generic SDP is used.
