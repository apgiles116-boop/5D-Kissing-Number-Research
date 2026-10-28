# Type E: low-center near-seven exclusion via sixteen-line D5 rigidity (2026-10-28)

**[NEW EXACT DERIVATION; CONDITIONAL TYPE-E EXCLUSION]** Under the retained Type-E graph/mass/harmonic inputs and the previously certified small-rank signed-Gram atlases, the entire isolated-center interval

[
oxed{rac{209}{30}le s=sum_{w
e v}(vcdot w)^2le 7}
]

is impossible. Together with the previously conditional exclusion of (sge7), any surviving Type-E configuration must satisfy **(s<209/30)**. This does **not** eliminate Type E or change the global proved range **(40le	au_5le44)**. The upstream mass and finite-atlas certificates are retained inputs, not independently re-proved in this note.

## 1. A new low-center harmonic/quantization polynomial

For the sixteen isolated deep edges (m_ipm z_i), set (x=sum_{I}|m_i|^2), (D_I=sum_I D(|m_i|^2)), (D(a)=196a-644a^2+896a^3-448a^4). Let (N_0) be the nondeep Delsarte slack on the forty contacts with the isolated center (v), (R=N-N_0) the other 754 nondeep contacts, and (E=(35/6)|T|_F^2+14K_4). The retained exact Type-E resource identity gives

[
D_I+N_0+R+Ele15. 	ag{1}
]

Write (s=7-d), (0le dle1/30), so (q=s-36/5=-1/5-d). Capped-simplex contact quantization yields

[
N_0ge n(d)=7d(1-4d).
]

The exact degree-2/fourth-harmonic center-row bound is

[
Egerac{175}{24}q^2+rac{147}{4}
 left(rac57+rac5{12}q+rac{N_0}{28}ight)^2.
]

The right side is increasing in (N_0) on the stated interval. Substitution of (n(d)) and exact polynomial simplification give

[
oxed{E+N_0gerac{955}{64}+g_-(d),qquad
g_-(d)=rac{7d}{16}(84d^3+28d^2-151d+5).} 	ag{2}
]

The cubic in parentheses decreases on ([0,1/30]) and equals (1/1125>0) at (d=1/30). Therefore

[
oxed{D_I+R+g_-(d)lerac5{64}.} 	ag{3}
]

In particular (Rle5/64), (D_Ile5/64), and the standard concavity argument gives

[
oxed{x<1/2500.} 	ag{4}
]

Unlike the earlier (sge7) theorem, (3) does **not** assert (Nle5/64); center slack (N_0) may be substantially larger.

## 2. Sixteen isolated directions: exact rounding and PSD D5 template

Every one of the 754 noncenter nondeep contacts has the same low/high alternative as in the high-center proof:

[
|t|<1/9quad	ext{or}quad12/25<|t|le1/2,
]

since (7t^2(1-4t^2)le Rle5/64). For any two isolated deep edges, their four endpoint contacts all have the same low/high category, with alternating signs in the high case, because (2sqrt{x}<1/25).

Round the 16-by-16 true Gram (G_{16}=operatorname{Gram}(z_1,ldots,z_{16})) to a symmetric half-integral matrix (widehat G_{16}) with diagonal 1 and off-diagonal (0,pm1/2). The exact Walsh identity, (7t^2(1-4t^2)ge(539/81)ho(t)^2) on the two intervals, and (3)-(4) give

[
oxed{|G_{16}-widehat G_{16}|_F^2
 lerac{81}{1078}R+x^2
 <rac{158207437}{26950000000}
 <rac1{169}.} 	ag{5}
]

Here (ho(t)=min(|t|,1/2-|t|)). The true Gram is PSD of rank at most five; (M=2widehat G_{16}) is integral, diagonal 2, off-diagonal (0,pm1), and is within squared Frobenius distance (4/169<1/16) of a PSD rank-five matrix.

**[EXACT, USING RETAINED FINITE ATLASES]** The integral principal-minor argument with error (<1/13) makes all principal minors of order at least eight vanish, hence (operatorname{rank}Mle7). For a hypothetical rank-seven block, the same determinant/parity argument gives (det M_B=pm2). The previous exact seven-vertex atlas, run at the *larger* proximity threshold (158205281/3368750000), leaves only the two characteristic polynomials

[
egin{aligned}
p_1(t)&=t^7-14t^6+77t^5-210t^4+292t^3-186t^2+37t-2,\
p_2(t)&=t^7-14t^6+76t^5-202t^4+271t^3-166t^2+33t-2.
end{aligned}
]

For both, exact sign variations of (p_j(t+4/25)) give six roots above (4/25); thus the second-smallest eigenvalue is (>4/25), requiring squared PSD-rank-five distance (>16/625), larger than (4(158207437/26950000000)). Rank seven is impossible.

For rank six, the earlier six-basis atlas has only three normalized bases admitting a ten-clique of outside columns. A new exhaustive enumeration of **all 4,096** such maximal ten-cliques (1,024, 1,024 and 2,048 per basis) shows that **every** resulting sixteen-vertex matrix has the same nonzero characteristic polynomial

[
q_6(t)=t^6-32t^5+411t^4-2676t^3+9091t^2-14484t+7161.
]

Exact sign variation of (q_6(t+1/2)) is six, so all six nonzero eigenvalues exceed (1/2). Its squared distance to PSD rank five is therefore (>1/4), contradicting (5). Hence (operatorname{rank}Mle5).

The retained universal small-rank integral atlas (order at least 13) makes (M) PSD of rank five. The ADE classification then places its sixteen projective root lines inside **(D_5)**, since (A_5) has only 15 lines. This labeling concerns the **rounded** sixteen directions only.

## 3. Exact sixteen-line extension atlas

**[NEW FINITE EXACT CERTIFICATE]** All (inom{20}{4}=4845) omitted four-line subsets of (D_5) form 17 Weyl-group orbits. On each orbit representative, three-term integer root relations span the full eleven-dimensional kernel of the retained (5	imes16) root matrix (R_D). The integer columns (cin{-1,0,1}^{16}) satisfying (c=R_D^	op t_0) have

[
|t_0|^2in{0,1,5/4,2,3,13/4}.
]

The **norm-two** solutions are exactly the **eight signed roots omitted** from the sixteen-line subsystem. Each orbit has 51 or 53 feasible integer columns. The companion verifier checks all 17 orbits using exact rational arithmetic and modular rank certificates.

The rounded sixteen-unit-vector frame (X) obeys

[
rac32 I_5preceq XX^	oppreceq4I_5
]

because it is the full (D_5) tight frame (4I_5) minus four unit roots, whose Gram has largest eigenvalue at most (5/2) by Gershgorin. With (Y=[z_1,ldots,z_{16}]), the same polar-alignment proof as in the seventeen-line theorem, now using (5), gives an orthogonal (U) such that

[
oxed{|Y-UX|_F<1/10.} 	ag{6}
]

Indeed, with (epsilon=|Y^	op Y-X^	op X|_F<1/13), the polar factor (L) has (sigma_{min}(L)>h=sqrt{1-2epsilon/3}>24/25), and

[
|Y-UX|_Fleepsilonleft(rac4{3(1+h)}+rac1{sqrt3 h}ight)<1/10.
]

## 4. All nine external endpoints are forced into eight signed root neighborhoods

For each of the eight (F_3) endpoints (w), its 32 contacts with the sixteen isolated edges are noncenter nondeep contacts. The two contacts for each isolated edge have the same low/high category and opposite rounded signs when high. Rounding the sixteen (wcdot z_i) correlations to (b_win{0,pm1/2}^{16}) gives

[
e_w^2:=|Y^	op w-b_w|^2
 lerac12sum_{	ext{32 contacts}}ho(t)^2
 lerac{81}{1078}R<rac1{64}. 	ag{7}
]

The center (v) needs a different estimate because its forty contacts are **not** covered by (R). The exact minimum of the center harmonic bound on (0le dle1/30) gives (N_0le N<281/1000). Put (r_j=min(t_j^2,1/4-t_j^2)). Since (7r_j(1-4r_j)<281/1000<21/64), every (r_j<1/16). Therefore

[
J:=sum_{40}r_jlerac4{21}N_0<rac{281}{5250}.
]

If (k) contacts are nearer (pm1/2) than zero, (|4s-k|le4J), forcing **(k=28)** because (4sin[418/15,28]) and (4J<1/4). Write (L) for the sum of (r_j) over low contacts and (H) over high contacts. Then (H-L=dge0), so (Lle J/2) and (Hle J). For low contacts (ho^2=r_j); for high contacts (ho^2le(4/3)r_j^2). Thus the center's rounded sixteen-correlation error satisfies

[
oxed{e_v^2lerac12left(L+rac43H^2ight)
lerac J4+rac23J^2
<rac{2528719}{165375000}<rac1{64}.} 	ag{8}
]

The center's 32 contacts with the sixteen isolated edges round in opposite pairs because their low/high intervals are separated by more than (2sqrt{x}<1/25).

For each of the **nine** unit vectors (win{v}cup V(F_3)), set (t=sqrt2,U^	op w) and (c=2b_w). With (R_D=sqrt2X), (6)-(8) give

[
|c-R_D^	op t|<2(1/8+1/10)=9/20.
]

Each three-term integer root relation (q) has (|q|=sqrt3), so (|q^	op c|<9sqrt3/20<1); integrality makes it zero. The triangle relations span (ker R_D), so (c=R_D^	op t_0) for a unique (t_0). Since (R_DR_D^	opge3I_5),

[
|t-t_0|<rac9{20sqrt3}<rac{27}{100}.
]

The exact norm list above has a gap (>27/100) between (sqrt2) and every other permitted norm. As (|t|=sqrt2), necessarily (|t_0|^2=2). Therefore each of the nine original unit vectors is within (27/(100sqrt2)) of one of the **eight signed omitted (D_5) roots** (after applying (U)). Two original code vectors in the same neighborhood would have inner product (>1/2), contrary to the kissing constraint. Nine vectors cannot occupy eight neighborhoods.

[
oxed{	ext{Type E with }209/30le sle7	ext{ is impossible, conditionally.}}
]

Together with the preceding conditional high-center exclusion (sge7), **Type E now requires (s<209/30)**.

## Proof-status ledger

**[PROVED EXACTLY, CONDITIONAL ON RETAINED UPSTREAM INPUTS]** The low-center polynomial (g_-), noncenter slack budget, sixteen-direction Frobenius rounding, center error estimate, polar alignment, and nine-versus-eight contradiction.

**[NEW FINITE CHECK]** 4,096 maximal sixteen-vertex rank-six extensions share the single polynomial (q_6); 4,845 omitted (D_5) four-line subsets form 17 Weyl orbits with triangle-kernel rank 11 and exactly eight norm-two signed missing-root extensions. The finite classification still relies on the previous exhaustive six-/seven-basis atlas completeness.

**[OPEN]** Type E with (s<209/30), Type C, Type D, generic (ege27), non-isolated branches, and sparse (e=23,24) classification without (delta(G)ge1). Retain (M(F_3)le89), matching (M(P)ge S/2-28/3), (Ale383/504), and the Musin/Boyvalenkov zero-midpoint theorem. **Global proved range remains (40le	au_5le44)**.
