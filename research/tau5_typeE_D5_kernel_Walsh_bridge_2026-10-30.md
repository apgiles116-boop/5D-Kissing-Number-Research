# Type E: exact D5 Q-kernel / Walsh-class bridge and ten soft modes
Date: 2026-10-30. **[PROVED EXACTLY — universal algebra; Type E still OPEN]**

## 1. D5 kernel, exactly
Index the 20 D5 projective roots by the two signs on each support e={p,q} of K5:
r_e^±=(e_p±e_q)/sqrt(2). Their traceless Q-Gram is
K0_ij=(r_i·r_j)^2-1/5.
Exact rational matrix multiplication yields spectrum
0 (multiplicity 6), 1 (multiplicity 10), 3/2 (multiplicity 4).
Its six-dimensional kernel projector is
P0=I-(5/3)K0+(2/3)K0².
P0 has diagonal 3/10, off-diagonal 3/10 on the 10 same-support pairs, -1/30 on the 120 meeting-support pairs, and 2/15 on the 60 disjoint-support pairs.
Moreover P0 1=1, Pg=11^T/20 and Pc=P0-Pg are orthogonal projectors of ranks 1 and 5.

## 2. Exact weighted identity
For ANY twenty vectors z_i in R5, arbitrarily assigned these D5 labels, let
w_i=||z_i||²=1-a_i, A=sum a_i, U=sum a_i²,
Q_i=z_i z_i^T-(w_i/5)I, K_ij=tr(Q_i Q_j),
S=sum_{i<j}(z_i·z_j)², V=||sum_i Q_i||_F²,
C=tr(Pc K)>=0.
Define O=sum d_ij² over the 10 same-support pairs;
D=sum d_ij² over the 60 disjoint-support pairs;
J=sum(d_ij²-1/4) over the 120 meeting-support pairs,
where d_ij=z_i·z_j.

**[PROVED EXACTLY]**
9O+4D-J
=3A-(9/2)U+3a^T P0 a+15 tr(P0 K)
=3A-(9/2)U+(3/20)A²+(3/4)V+3a^T Pc a+15C
=(3/2)S-45+(15/2)A-(15/4)U+3a^T Pc a+15C.

Proof: K_ii=(4/5)w_i². Expand tr(P0 K) using the four rational entry classes above, obtaining
tr(P0 K)=-A/5+(3/10)U-(1/5)a^T P0 a+(9O+4D-J)/15.
Use P0=Pg+Pc, tr(Pg K)=V/20 and
V=2S-60+6A+U-A²/5.
This proves all three identities.

If 0<=a_i<=1/4, then U<=A/4. PSD of Pc and K therefore gives the exact second-order inequality

**9O+4D-J >= (15/8)A+(3/20)A²+(3/4)V.**

This is a genuine link from the global squared-correlation floor to labeled D5 contact defects. It does NOT prove Type E impossible: O,D,J have not been independently bounded sharply, and no D5 geometric alignment has been justified.

## 3. Five local cycle residuals
Let T_e=Q_e^++Q_e^- for each of the ten supports and let V_p=sum_{e containing p}T_e for p=1,...,5. The unsigned K5 vertex-edge incidence matrix B satisfies BB^T=3I+J, (BB^T)^-1=I/3-J/24. The five-dimensional local kernel projector is the duplicated edge-cycle projector. Hence

C=(1/2)sum_e||T_e||_F²
 -(1/6)sum_p||V_p||_F²
 +(1/12)||sum_e T_e||_F² >=0.

This formula avoids any conjectural identification of the five cycle relations with F3 exceptions.

## 4. Six-exception combinatorial bridge
Assign the four selected F3 core edges to D5 labels (01,+),(02,+),(03,+),(04,+). This is only a relabeling, NOT an alignment. All six core-core pairings then fall in the 120 meeting-support class J. The 10 same-support and 60 disjoint-support pairings are all among the 184 fully safe Type-E blocks. The remaining meeting-support pairs split into 114 safe and six potentially exceptional. Thus the identity has an exact six-exception interpretation.

## 5. Q-kernel alone has ten exact soft modes
For each support e={p,q}, independently rotate its two orthonormal D5 lines within span(e_p,e_q) by any angle phi_e. The sum of the two rank-one projectors on that support is unchanged. Therefore ALL six Q-kernel relations remain exact, and V=C=0, throughout this ten-parameter family. Nontrivial rotations can break projective safety (cos phi=3/5, sin phi=4/5 on one support gives an adjacent squared correlation 49/100>1/4). Thus Q-kernel relations alone do NOT force D5 alignment.

## 6. Walsh rigidity removes those soft modes inside the exact fibre
For two support planes meeting in one coordinate, the 2-by-2 cross-Gram matrix between their orthonormal bases is an outer product p q^T of two unit vectors in R2. Its four squared entries sum to 1. If all four cross-pair contacts obey |dot|<=1/2, each squared entry must equal 1/4. Both bases are then coordinate-balanced, hence D5 up to signs and interchange.

In the four-core-star labeling, every support has an intersecting support with all four line pairings safe: core supports meet noncore supports, and noncore supports meet other noncore supports. Consequently the 184 safe blocks force all ten internal rotations to D5 values **inside the exact coordinate-support-plane fibre**, even though six core pairings are exceptional.

**[QUANTITATIVE, PROVED EXACTLY]** If t=|p_+²-p_-²| in [0,1] measures one support's imbalance, the maximum cross-contact magnitude is at least sqrt(1+t)/2 >=1/2+t/5. Thus a four-contact upper bound 1/2+epsilon forces t<=5 epsilon (and more sharply t<=4epsilon+4epsilon²). At least one squared positive contact excess is >=t²/25. This supplies a quadratic stability penalty for each soft mode.

## 7. Status
**[PROVED EXACTLY]** Spectral projector, three weighted identities, five-cycle incidence formula, six-exception star labeling, ten exact soft modes, and their conditional exact-fibre Walsh rigidity.
**[OPEN]** Establish an approximate coordinate-support-plane decomposition and an incompatible upper bound on the labeled defect combination. No Type-E exclusion or improved global kissing bound is claimed.
**[RETAINED]** Type E: M(F3)<=89, M(P)>=S/2-28/3, selected-edge mass >=2137/6, A<=383/504. Type C, D, generic e>=27, and non-isolated branches open. Sparse e=23,24 classification conditional on delta(G)>=1. Global 40<=tau_5<=44 unchanged.

An exact Fraction regression script is included in the downloadable research package supplied in the conversation.