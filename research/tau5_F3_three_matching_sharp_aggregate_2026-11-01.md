# F3: sharp aggregate midpoint-energy obstruction for all three perfect matchings (2026-11-01)

**[PROVED EXACTLY — standalone sharp eight-vector theorem].** **[CONDITIONAL TYPE E]** Applies to the F3 core of the isolated-center Type-E branch, but does **not** exclude that branch. Global proved range remains **40 <= tau_5 <= 44**.

## Statement

Let eight unit vectors `u_0,...,u_7` in a real Euclidean space have exactly the strict deep F3 edges

`02,04,05,14,17,23,27,36,56,57` (dot product < -1/2),

and all 18 other pairs two-sided safe (dot product in [-1/2,1/2]). Its three perfect matchings are

- `P0=04|17|23|56` (canonical),
- `P1=02|14|36|57`,
- `P2=05|14|27|36`.

For `C(P)=sum_(ij in P) ||(u_i+u_j)/2||^2`, let `y` be the unique positive root of

`g(y)=y^4+8y^3+15y^2-2y-4=0`,

with `509/1000<y<51/100`. Then the **sharp** aggregate bound is

```
C(P0)+C(P1)+C(P2) >= L
L = 5/2-y-1/y+3/[y(y+4)]
  = 1.33350731002294... > 3067199/2300100 > 4/3.
```

Equality is attained by a rank-three Gram configuration satisfying **all ten deep inequalities strictly** and all eighteen nonedge two-sided safety constraints. The inequality itself requires only `u_0.u_7<=1/2` and `u_2.u_5<=1/2`; the full F3 incidence is needed for the sharpness claim *within the specified graph*.

Consequences: at least one matching has `C(P)>=L/3>0.44450`. Because each of the four canonical edges is strict deep, `C(P0)<1`, hence `C(P1)+C(P2)>L-1>1/3`, and `max(C(P1),C(P2))>(L-1)/2>1/6`. This does **not** identify the mass-selected matching.

## Exact dual/SOS proof

Order the vertices as `A=(0,2,5,7)`, `B=(4,3,6,1)`. Let `W` be the weighted adjacency matrix obtained by summing the three matching adjacency matrices. Its blocks are

```
W = [[C4, I4], [I4, 2J]],
```

where `C4` is the 4-cycle adjacency on A and `J` is the adjacency of the disjoint pairs `(0,3),(1,2)` in each four-vertex block. In A, these are precisely the F3 nonedges `07,25`. Let `E=diag(J,0)`, `G=(u_i.u_j)` in A/B order. Since there are 12 matching edges,

`C(P0)+C(P1)+C(P2)=6+tr(WG)/4.`

For any `y>0` with `y(y+4)>2`, set

```
mu=1-2/[y(y+4)] >0,
a=-mu-1/y,       b=-2-y,
D=diag(a I4,b I4),   K=W+mu E-D.
```

The four Hadamard characters simultaneously diagonalize `C4` and `J`. They give the following 2x2 blocks of `K`:

```
mode 0:  [[4+1/(y+4), 1], [1, y+4]],
modes 1,2: [[1/y, 1], [1, y]],
mode 3:  [[1/(y+4), 1], [1, y+4]].
```

All are PSD: modes 1,2,3 have determinant zero; mode 0 has determinant `4(y+4)>0` and positive diagonal. Thus `K>=0`. The **exact SOS identity** is

```
C(P0)+C(P1)+C(P2) - [6+a+b-mu/2]
  = tr(KG)/4 + (mu/2)*(1-u_0.u_7-u_2.u_5) >=0.
```

The first term is nonnegative by PSD of both `K` and `G`; the second by the two safe nonedges. The bracket equals `f(y)=5/2-y-1/y+3/[y(y+4)]`. Its derivative is

`f'(y)=-g(y)/[y^2(y+4)^2]`.

Since `g''(y)=12y^2+48y+30>0`, `g(0)=-4`, and `g(y)->infinity`, `g` has exactly one positive zero; it maximizes `f` on the admissible positive interval. Exact rational signs at `509/1000` and `51/100` bracket the root.

The explicit rational choice `y=51/100` gives

```
mu=3001/23001, a=-48101/23001, b=-251/100,
6+a+b-mu/2 = 3067199/2300100
                  = 4/3+133/766700.
```

Therefore the displayed strict rational improvement over 4/3 is independently certified without algebraic-number arithmetic.

## Exact rank-three equality witness

Let `h_0=(1,1,1,1)/2`, `h_1=(1,1,-1,-1)/2`, `h_2=(1,-1,1,-1)/2`, and `h_3=(1,-1,-1,1)/2`. For `i=0,1,2,3` set three-dimensional vectors

```
A_i=(h_1i/sqrt(2), h_2i/sqrt(2), sqrt(3)*h_3i),
B_i=(-h_1i/(sqrt(2)*y), -h_2i/(sqrt(2)*y),
     -sqrt(3)*h_3i/(y+4)).
```

Each `A_i` has squared norm 1. The quartic equation is equivalent to

`1/y^2+3/(y+4)^2=4`,

so each `B_i` also has squared norm 1. Assign the vectors to the vertex labels in the A/B order above. Their distinct pairwise inner products are:

| Pair class | Inner product | F3 status |
|---|---:|---|
| A-A cycle (02,05,27,57) | -3/4 | strict deep |
| A-A matching (07,25) | +1/2 | safe, saturated |
| B-B matching (14,36) | 3/[4(y+4)^2]-1/(4y^2) | strict deep |
| B-B other pairs | -3/[4(y+4)^2] | safe |
| A_i-B_i | -(y+1)/[y(y+4)] | strict deep |
| A_i-B_j, cycle adjacency | 3/[4(y+4)] | safe |
| A_i-B_j, matching adjacency | (2-y)/[2y(y+4)] | safe |

All asserted signs and ranges follow already from the exact bracket `509/1000<y<51/100`; no floating-point feasibility is needed. The Gram is PSD of rank at most three and satisfies `u_0.u_7=u_2.u_5=1/2`. The two rank-one Hadamard blocks of `K` annihilate this Gram, and the positive mode-0 block has zero witness component. Hence both SOS terms vanish, attaining `L` exactly.

At the witness, approximately `C(P0)=0.6859816215` and `C(P1)=C(P2)=0.3237628443`; these are explanatory decimals, not part of the certificate.

## Proof-status and next use

- **[PROVED EXACTLY, SHARP]** The aggregate F3 three-matching energy bound and rank-three strict-deep, safe-nonedge equality witness.
- **[VERIFIED EXACT ARITHMETIC]** Companion SymPy checker verifies weighted graph, Hadamard PSD blocks, root bracket, exact SOS constants, Gram norm identity, and rational pair-class inequalities.
- **[CONDITIONAL TYPE E]** Applies to the retained F3 eight-endpoint subgraph. It proves a **matching tradeoff**, not a lower bound for the particular matching chosen by the retained mass theorem.
- **[OPEN]** Convert this matching tradeoff into an incidence-sensitive joint upper certificate for the mass-selected F3 matching, safe Walsh defects, or frame energy. Type E, Types C/D, generic e>=27, and non-isolated branches remain open. Sparse e=23/24 classification still requires delta(G)>=1. Preserve M(F3)<=89, M(P)>=S/2-28/3, A<=383/504 and stronger conditional harmonic refinements, and the Musin/Boyvalenkov zero-midpoint boundary theorem. **Global proved range: 40<=tau_5<=44.**
