# Type E: endpoint-slack strengthening of cross-matching stability

**2026-10-24. Status:** [PROVED EXACTLY] four-edge endpoint theorem and an endpoint-feasible equality witness. [CONDITIONAL TYPE E] the numerical energy-cap consequence. [OPEN] a new uniform six-defect bound and Type-E elimination.

For selected edges (x_i^±=m_i±z_i) with unit endpoints, write
(delta_{ij}=(|z_i\cdot z_j|-1/2)_+). The four endpoint inequalities are
[
m_i\cdot m_j+st,z_i\cdot z_j+s,z_i\cdot m_j+t,m_i\cdot z_j\le 1/2
\quad(s,t=\pm1).
]
If (delta_{ij}>0), put (sigma_{ij}=\mathrm{sign}(z_i\cdot z_j)) and
(ell_{ij}=-m_i\cdot m_j-delta_{ij}\ge0). The two endpoint inequalities with (st=sigma_{ij}) imply
[
|m_i\cdot z_j+sigma_{ij}z_i\cdot m_j|\le\ell_{ij}. \tag{1}
]
This is additional information lost by the weaker projected inequality.

**[PROVED EXACTLY] Stronger four-core theorem.** Assume (p=delta_{12}>0), (q=delta_{34}>0), and set
[
C=\sum_{i=1}^4\|m_i\|^2,\quad
\ell=\ell_{12}+\ell_{34},\quad
w=\min(\delta_{13}+\delta_{24},\delta_{14}+\delta_{23}).
]
Then
[
\boxed{(p+q+\ell)^2+w^2\le C^2/4.} \tag{2}
]
In particular,
[
\boxed{p+q+|b_{12}|+|b_{34}|+w^2/C\le C/2,} \tag{3}
]
where (b_{ij}=m_i\cdot z_j+sigma_{ij}z_i\cdot m_j) and (C>0).

**Proof.** Let (x=m_1+m_2), (a=m_1-m_2), (y=m_3+m_4), (b=m_3-m_4), and (r=\|x\|^2+\|y\|^2). The four cross midpoint products are
[
4m_1\cdot m_3=X+U+V+W,\quad
4m_2\cdot m_4=X-U-V+W,
]
[
4m_1\cdot m_4=X-U+V-W,\quad
4m_2\cdot m_3=X+U-V-W,
]
where (X=x\cdot y), (U=x\cdot b), (V=a\cdot y), (W=a\cdot b). If (W\ge0), the first cross matching has total positive defect at most ((|X+U+V|+|X-U-V|)/4); if (W\le0), the second is similarly controlled. Since (m_3\cdot m_4<0), (\|b\|\ge\|y\|). Cauchy–Schwarz yields
(2w\le\|x\|\|b\|+\|a\|\|y\|), hence (4w^2\le r(2C-r)).
The **exact** identity (r=C-2(p+q+\ell)) proves (2). Since (w^2\le C(C/2-p-q-\ell)), (1) proves (3).

**[CONDITIONAL TYPE E]** Under the retained (C\le A\le B=383/504), if (p+q\ge B/2-h), then
[
\boxed{|b_{12}|+|b_{34}|+w^2/B\le h.} \tag{4}
]
For (h=1/1000), this reads (|b_{12}|+|b_{34}|+(504/383)w^2\le1/1000). If (w\ge1/50), the two mixed products have total magnitude at most (907/1915000).

**Exact sharpness witness.** In orthonormal (e_1,\ldots,e_5), take
(m_1=-m_2=e_1/\sqrt{10}), (m_3=-m_4=e_2/\sqrt{10}).
Set (u=3/\sqrt{10}), (v=11\sqrt{10}/60), (t=\sqrt{203/360}), and
[
z_1=ue_3,\quad z_2=ve_3+te_4,\quad z_3=ue_5,\quad
z_4=ve_5+t(3e_3/5-4e_4/5).
]
All endpoint norms are 1; all inter-edge endpoint products are at most 1/2. Here (p=q=1/20), (ell_{12}=ell_{34}=1/20), (C=2/5), (w=0), so (2) is equality. This is a four-edge witness, **not** a full Type-E configuration.

**[EXACT FORMULATION; UNSOLVED]** For a future finite certificate, the four-edge problem has an exact (8\times8) PSD Gram formulation with rank at most 5 (or (H=Y^TY) for (Y\in\mathbb R^{5\times8})), four endpoint inequalities for each of six pairs, and the retained energy and defect caps. Switching each (z_i) lets us impose (z_1\cdot z_j\ge0) for (j=2,3,4); only the three signs on pairs (23),(24),(34) remain, giving **eight** sign classes. Auxiliary (delta\ge0), (delta\ge y-1/2), (delta(delta-y+1/2)=0) impose (delta=(y-1/2)_+) exactly. No optimization certificate has yet been obtained.

**Ledger:** [PROVED] (1)–(3), equality witness. [CONDITIONAL] (4). [OPEN] stronger uniform six-defect ceiling, safe-pair upper bound, Type E, C, D, generic (e\ge27). Retain (40\le\tau_5\le44), (M(F_3)\le89), (M(P)\ge S/2-28/3), (A\le383/504).
