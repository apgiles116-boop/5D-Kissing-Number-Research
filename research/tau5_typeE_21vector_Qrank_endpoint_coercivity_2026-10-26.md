# Type E: 21-vector Q-rank and endpoint-mixing coercivity (2026-10-26)

**Status:** [PROVED EXACTLY] Universal rank-fourth-moment identity and deficit polynomial. [CONDITIONAL ON RETAINED TYPE-E CERTIFICATES] The 184 safe edge-edge, 20 center-edge and six exceptional core-core partition, endpoint constraints, and four-core negative-Gram budget. [OPEN] Type E exclusion.

Let y_0=x_0 be the unit isolated center and y_i=z_i (i=1,...,20) the projected deep-edge directions. The endpoints are p_i^±=m_i±z_i, with ||p_i^±||=1, m_i·z_i=0, a_i=||m_i||²∈[0,1/4], r_i=||z_i||²=1-a_i. Put a_0=0, r_0=1, A=Σa_i≤383/504. For i<j write t_ij=y_i·y_j, and define

S=Σt_ij², T4=Σt_ij⁴, B=Σr_i², C=Σr_i⁴,
D=Σ(1-r_i r_j)t_ij²,
F=Σy_i y_i^T, V=||F-(21-A)I/5||_F².

For the six core-core pairs define E4=Σ[t_ij⁴-t_ij²/4]_+.

**[PROVED EXACTLY] Q-rank identity.** The traceless Q_i=y_i y_i^T-(r_i/5)I belong to the 14-dimensional traceless symmetric matrix space. Their PSD Gram matrix K has rank≤14 and tr(K)=4B/5. The rank-trace inequality and direct expansion yield

T4 ≥ (2/5)Σr_i r_j t_ij² + B²/350 - (3/10)C.   (1)

The frame trace identity gives

S=((21-A)²/5-B+V)/2.   (2)

**[CONDITIONAL] Safe endpoint quartic correction.** For each of the 184 safe edge-edge pairs, let M=m_i·m_j, Z=z_i·z_j, X=m_i·z_j, Y=z_i·m_j. The four endpoint dots lie in [-1/2,1/2], hence

1/4-Z² ≥ M²+X²+Y²,
Z⁴ ≤ Z²/4-Z²(M²+X²+Y²).

For each center-edge pair put b_i=|x_0·m_i|. The two-sided endpoint constraints imply |x_0·z_i|+b_i≤1/2, so

(x_0·z_i)⁴ ≤ (x_0·z_i)²/4-(x_0·z_i)²(b_i-b_i²).

Let J≥0 be the sum of these 184+20 nonnegative correction terms. The six remaining core pairs contribute at most E4, giving

T4 ≤ S/4-J+E4.   (3)

Combining (1)-(3), with Σr_i r_j t_ij²=S-D, gives

(3/40)V+J ≤ E4+(2/5)D+Φ(a),   (4)

where A_k=Σa_i^k and the **exact** deficit polynomial is

Φ(a)= -12A/25 +351A_2/200 -6A_3/5 +3A_4/10
      -37A²/1400 +2AA_2/175 -A_2²/350.   (5)

**[PROVED EXACTLY] Strictly negative deficit polynomial.** For 0≤a≤1/4, the polynomial
h(a)/a=-12/25+(351/200)a-(6/5)a²+(3/10)a³ is increasing, and its value at 1/4 is -357/3200. Therefore Σh(a_i)≤-357A/3200. Using A_2≤A/4, the remaining three terms in (5) are ≤-33A²/1400. Thus

Φ(a)≤-357A/3200-33A²/1400.

The new **21-vector second-order coercivity budget** is consequently

**(3/40)V+J+(357/3200)A+(33/1400)A² ≤ E4+(2/5)D.**   (6)

This keeps all 204 safe endpoint-mixing terms and the six exceptional fourth moments in one exact inequality. No D5 labeling is assumed.

**[CONDITIONAL] Scalar six-core corollary.** For δ_ij=(|z_i·z_j|-1/2)_+ on the six core pairs, retain Σδ≤A_C, Σδ²≤A_C²/4, and δ≤A_C/2. Since (1/2+δ)⁴-(1/2+δ)²/4=δ/4+5δ²/4+2δ³+δ⁴, we have

E4 ≤ p(A_C)=A_C/4+5A_C²/16+A_C³/4+A_C⁴/16.

Therefore

**(3/40)V+J+(357/3200)A+(33/1400)A² ≤ (2/5)D+p(A_C).**   (7)

**[OPEN]** This is a new coupled necessary condition, not a Type-E exclusion. The main missing step is a lower bound on J relative to D from the 184 safe-pair geometry and the frame operator, without discarding their correlation. The retained interval remains 1/99<A≤383/504. Type C, Type D, generic e≥27 and non-isolated branches remain open. Global range remains 40≤tau_5≤44. Keep M(F3)≤89 and matching M(P)≥S/2-28/3. The sparse e=23/e=24 classification is conditional on δ(G)≥1.

Companion local exact checker: tau5_typeE_21vector_Qrank_endpoint_coercivity_2026-10-26_verify.py.
