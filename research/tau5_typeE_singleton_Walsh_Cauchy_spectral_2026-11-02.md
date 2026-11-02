# Type E: exact second-order singleton Walsh–Cauchy stability (2026-11-02)

**[PROVED EXACTLY — standalone local theorem]** Let (u_i^pm=m_ipm z_i) and (u_j^pm=m_jpm z_j) be two selected deep edges, (a=|m_i|^2,b=|m_j|^2<1/4), (h=m_icdot m_j), (d=z_icdot z_j), (p=m_icdot z_j), (q=z_icdot m_j). Orient the unique deep cross-contact as (++), the other three cross-contacts being two-sided safe. If (delta=|d|-1/2>0), the audited singleton Walsh lemma gives
[
d=-1/2-delta,quad hle-delta-|p-q|,quad p,qle-delta.
]
The Gram minors of ((m_i,m_j,z_j)) and ((m_i,z_i,m_j)) give, respectively,
[
(1-b)(ab-h^2)ge bp^2,qquad (1-a)(ab-h^2)ge aq^2.
]
Consequently, with (R=max(a/(1-a),b/(1-b))),
[
oxed{abge(delta+|p-q|)^2+Rdelta^2.}	ag{1}
]
As (R>sqrt{ab}) and (ab-h^2ge Rdelta^2), factor (ab-h^2=(sqrt{ab}-|h|)(sqrt{ab}+|h|)) to obtain
[
oxed{delta+|p-q|+delta^2/2<sqrt{ab}.}	ag{2}
]
This is a **strict second-order midpoint-energy penalty**, including mixed Walsh asymmetry. It does not apply unchanged to double-contact pairings; those retain the weaker (deltalesqrt{ab}).

**[CONDITIONAL ON RETAINED EXACT F3 SUPPORT THEOREMS]** The previously proved F3 positive-defect graph is triangle-free and C4-free, hence a forest with at most three edges on four quotient vertices. Its adjacency spectral radius is at most (sqrt3), with (ho(P_4)=(1+sqrt5)/2) and (ho(K_{1,3})=sqrt3). Write (C=sum_{i=0}^3 a_i), (D=sum_Edelta_e), (S_{m sing}=sum_{m singleton}delta_e^2), and (W=sum_{m singleton}|p_e-q_e|). Summing (2), using (delta_elesqrt{a_i a_j}) for any double contact, and Rayleigh's inequality gives
[
oxed{D+W+	frac12S_{m sing}le	frac12ho(E)Cle	frac{sqrt3}{2}C.}	ag{3}
]
For canonical (P_0=(04),(17),(23),(56)), all six quotient pairs are singleton; thus (D+W+S/2<sqrt3,C_0/2). Since at most three defects are positive, (Sge D^2/3), giving
[
oxed{C_0>rac2{sqrt3}(D+D^2/6+W).}	ag{4}
]
The alternative double-positive branch is not excluded; only singleton defects receive the extra terms.

**[Q-FRAME BRIDGE — CONDITIONAL CANONICAL MATCHING]** The six exceptional core pairings contribute (Q_{m core}le3/2+D+S). With the audited singleton cap (delta<1/8), (Sle D/8), and ((D+S)/(D+S/2)le18/17), (3) implies
[
oxed{Q_{m core}<	frac32+rac{9sqrt3}{17}C_0.}	ag{5}
]
The independent canonical bound (D<3/8) also yields (Q_{m core}<123/64). Therefore
[
oxed{Q_{m safe}>Q_{m total}-	frac32-min(27/64,;9sqrt3,C_0/17).}	ag{6}
]
This is an explicit mass-sensitive bridge between the F3 defects and the global traceless-Q frame floor.

**[FURTHER CONDITIONAL ON RETAINED (Q_{m total}>28.3626)]** If canonical (C_0<234889sqrt3/1215000approx0.3348474750), then (Q_{m safe}>239/9), forcing **at least 45 of 184** safe pairs with (|z_icdot z_j|>1/3). If (C_0<128639sqrt3/1215000approx0.1833821266), then (Q_{m safe}>961/36), forcing **at least 46 of 184**. These are conditional branch splits, NOT unconditional 45/46 claims. The stronger center-sensitive Q certificate is retained, not re-proved here.

**[D5 AUDIT — EXACT]** The D5 traceless-Q Gram has spectrum (3/2) (multiplicity 4), (1) (multiplicity 10), (0) (multiplicity 6). Every 20-vector Q Gram in (operatorname{Sym}_0(5)), a 14-dimensional space, has nullity at least six. Thus the coincidence of six Q null directions and six exceptional pairings is not itself evidence of a bijection.

**[OPEN]** Type E, Type C, Type D, generic (ege27), and non-isolated branches. Do not reuse the withdrawn endpoint-Perron proof. Sparse (e=23,24) classification remains conditional on (delta(G)ge1). **Global proved range unchanged: (40le	au_5le44).** The companion standalone SymPy verifier and expanded proof are available in the generated local package.
