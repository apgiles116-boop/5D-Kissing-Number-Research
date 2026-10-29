# Exact 21-line quartic-integrality stability (2026-10-29)

**[PROVED EXACTLY — standalone]** For any 21 unit vectors (y_0,ldots,y_{20}) in (mathbb R^5), set (x_{ij}=(y_icdot y_j)^2) and
[
P=sum_{i<j}[x_{ij}(x_{ij}-1/4)]_+.
]
Then **(P>1/120)**. In particular, 21 projective lines cannot all have coherence at most (1/2). This is a self-contained proof of the 21-line zero-midpoint boundary, independent of Musin/Boyvalenkov or a D5 uniqueness assertion. It does not improve the global (40le	au_5le44) range.

## Harmonic proof

Let (T=sum_i y_iy_i^T), (V=|T-(21/5)I|_F^2), (f(t)=t^4-t^2/4). The normalized five-dimensional Gegenbauer polynomials are
[
P_2(t)=(5t^2-1)/4,qquad P_4(t)=(21t^4-14t^2+1)/8.
]
The exact expansion
[
f(t)=1/28+(1/3)P_2(t)+(8/21)P_4(t)
]
has positive coefficients. By the addition theorem (sum_{i,j}P_4(y_icdot y_j)ge0), and (sum_{i,j}P_2(y_icdot y_j)=(5/4)V). The constant term (21^2/28=63/4) exactly cancels the diagonal (21f(1)=63/4). With (N=sum_{i<j}[-f(y_icdot y_j)]_+),
[
oxed{P-Nge (5/24)V.}	ag{1}
]

If all (|y_icdot y_j|le1/2), then (P=0), hence (N=V=0). Consequently (T=(21/5)I) and each (x_{ij}in{0,1/4}). But for each (i),
[
sum_{j
e i}x_{ij}=y_i^TTy_i-1=16/5,
]
not a multiple of (1/4). Contradiction.

## Quantitative rounding argument

Round each (x_{ij}in[0,1]) to its nearest (r_{ij}in{0,1/4}). The exact scalar bound
[
|x-r|le8[-x(x-1/4)]_++4[x(x-1/4)]_+
]
gives
[
left|rac{336}{5}+V-rac m2ight|
le16N+8Ple24P-rac{10}{3}V,	ag{2}
]
where (m) counts pairs rounded to (1/4), using (2sum_{i<j}x_{ij}=operatorname{tr}T^2-21=336/5+V). If (Vge1/20), (1) gives (Pge1/96>1/120). If (V<1/20), the distance from (336/5+V) to the nearest half-integer is (1/5+V); therefore
[
oxed{Pge1/120+(13/72)V.}	ag{3}
]
Strictness follows because (P>0) by the preceding boundary proof and the rounding inequality is strict on any positive-defect pair (x>1/4). Thus (P>1/120).

## Bridge to the six Type-E exceptional pairs

**[CONDITIONAL ON RETAINED TYPE-E 16+4 MATCHING AND RAW-SAFETY CLASSIFICATION]** Let (z_0=v) be the isolated center direction, (|z_0|=1), and (z_1,ldots,z_{20}) the selected projected edge directions, (|z_i|^2=b_i=1-a_i), (0le a_ile1/4). Write (A=sum_{i=1}^{20}a_i) and (A_C) for the four core midpoint energies. Assume all 210 raw pairings satisfy (|z_icdot z_j|le1/2) except possibly the six pairs among those four core directions. Normalize (y_i=z_i/sqrt{b_i}) (with (b_0=1)), and let
[
P_{m raw}=sum_{i<j}[(z_icdot z_j)^2((z_icdot z_j)^2-1/4)]_+.
]
Only the six exceptional pairs contribute to (P_{m raw}). The exact identity
[
x_{ij}(x_{ij}-1/4)=rac{W_{ij}^2(W_{ij}^2-1/4)+(1-b_ib_j)W_{ij}^2/4}{(b_ib_j)^2}
]
with (W_{ij}=z_icdot z_j), (b_ib_jge9/16), and (1-b_ib_jle a_i+a_j) shows that each raw-safe pair contributes at most ((16/81)(a_i+a_j)) to normalized (P), while each exceptional pair contributes at most ((256/81)[W_{ij}^2(W_{ij}^2-1/4)]_++(64/81)(a_i+a_j)). There are 20 incidences per (a_i) among the 210 pairs and three incidences per core (a_i) among the six exceptional pairs. Hence
[
Plerac{256}{81}P_{m raw}+rac{320}{81}A+rac{16}{9}A_C
]
and therefore the **exact strict bridge**
[
oxed{P_{m raw}>rac{27}{10240}-rac54 A-rac9{16}A_C.}	ag{4}
]

The right-hand side of (4) may be negative at the retained Type-E ceiling (Ale383/504), so this does **not** eliminate Type E. It does imply that if (A<27/18560), at least one of the six exceptional raw pairings must exceed (1/2) in absolute value.

**[OPEN]** Improve (4) with weighted harmonic/integrality control and the 184 safe Walsh blocks. Types C, D, E, generic (ege27), and non-isolated branches remain open; sparse (e=23/24) classification still requires (delta(G)ge1). Retain (M(F_3)le89), matching (M(P)ge S/2-28/3), and (Ale383/504). **Global proved range unchanged: (40le	au_5le44).**
