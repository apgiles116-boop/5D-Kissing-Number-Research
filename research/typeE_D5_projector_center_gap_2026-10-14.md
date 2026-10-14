# Type E: new exact isolated-center obstruction in the D5 projector metric

Date: 2026-10-14. STATUS: standalone results are **PROVED EXACTLY**; applications to Type E rely on the retained center and midpoint-energy hypotheses. **NOT** a Type-E elimination or a proof of tau_5=40.

## Retained baseline

`40 <= tau_5 <= 44`. For Type E, twenty selected deep edges have endpoints `x_i^±=m_i±z_i`, with `a_i=||m_i||²`, `||z_i||²=1-a_i`, `0<=a_i<1/4`, `A=sum a_i<=383/504`. The isolated center `u=x0` obeys `|u·x_i^±|<=1/2`, and hence `|u·z_i|<=1/2`. The F3 mass estimates are still `M(F3)<=89` and `M(P)>=S/2-28/3`; the mass-derived energy ceiling is inherited, not re-proved here.

Let `V={v_ij^±=(e_i±e_j)/sqrt(2): 1<=i<j<=5}` be the twenty D5 *projective* lines. Match each `z_i` with an independently signed, globally rotated, and permuted `v_i`. Sign disappears in the rank-one projectors.

## Theorem 1: improved Euclidean L2 template separation [PROVED EXACTLY]

For every `u in S^4`,

`sum_{v in V} (|u·v|-1/2)_+² >= 1568/9255 = 0.169421934...`.

This improves the preceding `16/97` theorem. To prove it, let `t_v=|u·v|`, `p_j=u_j²`, `s2=sum p_j²`, `s3=sum p_j³`. Then

`M2=sum t_v²=4`, `M4=(3+s2)/2`, `M6=(15s2-11s3)/4`, `s3>=s2²`, `1/5<=s2<=1`.

The signed polynomial moment is

`E=sum t_v²(t_v²-1/4)=(1+s2)/2`.

On `t_v>1/2`, the positive summand equals `t_v²(t_v+1/2)(t_v-1/2)`. Dropping nonpositive terms and applying Cauchy-Schwarz yields

`E² <= [sum t_v⁴(t_v+1/2)²] [sum (t_v-1/2)_+²]`.

The global upper bound `(t+1/2)² <= (5/3)t²+5/8` follows from `(t-3/4)²>=0`. Therefore

`sum t_v⁴(t_v+1/2)² <= (5/3)M6+(5/8)M4 <= (45+315s2-220s2²)/48`.

Consequently,

`sum (t_v-1/2)_+² >= 12(1+s2)²/(45+315s2-220s2²)`.

The rational function decreases until `s2=45/151` and increases thereafter. Substitution yields `1568/9255`. If Type E has `|u·z_i|<=1/2`, then `||z_i-v_i|| >= (|u·v_i|-1/2)_+`; sum over the twenty assigned lines to obtain Euclidean squared alignment gap `>=1568/9255`.

## Theorem 2: sharp scalar **projector** moment gap [NEW; PROVED EXACTLY]

For every `u in S^4`, set `q_v=(u·v)²` and

`H(u)=sum_{v in V}(q_v-1/4)_+²`.

Then

`H(u) >= 9/40 = 0.225`.

The constant **is optimal for H** and is attained at `u=(1,1,1,1,1)/sqrt(5)` (and its signed permutations): ten projective lines have `q_v=2/5` and ten have `q_v=0`.

Proof: `sum_v q_v=4` and `sum_v q_v²=(3+s2)/2` as above. Since the summands with `q_v<=1/4` are nonpositive,

`E=sum q_v(q_v-1/4)=(1+s2)/2 <= sum_v q_v(q_v-1/4)_+`.

Cauchy-Schwarz gives

`E² <= (sum q_v²) H(u)=((3+s2)/2)H(u)`.

Hence

`H(u) >= (1+s2)²/[2(3+s2)] >= (6/5)²/[2(16/5)] = 9/40`,

since the rational function is increasing in `s2>=1/5`.

## Theorem 3: quantitative **Q-column** obstruction for Type E [NEW; PROVED EXACTLY GIVEN RETAINED ENERGY CERTIFICATE]

Write `P(z)=zz^T` and `Q(z)=zz^T-(||z||²/5)I_5`. Assume `|u·z_i|<=1/2` and match `z_i` to any rotated/signed/permuted D5 reference `v_i`.

For each i,

`||P(v_i)-P(z_i)||_F >= |u^T(P(v_i)-P(z_i))u| >= ((u·v_i)²-1/4)_+`.

Squaring and summing, Theorem 2 yields

`sum_i ||P(z_i)-P(v_i)||_F² >= 9/40`.

This is an **unconditional** (given center-band) separation in the natural rank-one projector metric, independent of midpoint-energy magnitude.

For the traceless Q columns, the orthogonal decomposition

`P(v_i)-P(z_i)=[Q(v_i)-Q(z_i)]+(a_i/5)I_5`

implies the **exact identity**

`sum_i ||Q(v_i)-Q(z_i)||_F² = sum_i ||P(v_i)-P(z_i)||_F² - (1/5)sum_i a_i²`.

Using the inherited energy cap and the individually capped concentration inequality

`sum_i a_i² <= 3/16 + (5/504)² = 47653/254016`,

we obtain

`boxed: sum_i ||Q(v_i)-Q(z_i)||_F² >= 47623/254016 = 0.187480316200...`.

This holds for every common rotation, permutation, and independent sign choice of the D5 template. Equivalently, if the columns of a linear map `T:R^20 -> Sym_0(R^5)` are these twenty Q matrices, then `||T-T_D5||_F² >=47623/254016` under all such alignments.

The 9/40 constant is sharp only for the *scalar moment H*, and is **not claimed sharp** for the 20-column projector distance. The Q bound is a necessary separation, not an upper or a contradiction.

## Important limitations [OPEN]

1. The D5 labeling/alignment is only a comparison template; there is no theorem implying that Type E is close to it. In particular, high total squared-correlation mass does not by itself force D5 proximity.
2. The Q-column distance is NOT the same as a Gram-matrix/operator-norm distance. A separate quantitative inverse-Gram theorem would be needed to infer one from the other.
3. No one-to-one correspondence of six exceptional Type E pairs with six D5 kernel relations has been proved.
4. Type E, C, D and generic e>=27 remain unresolved. The sparse e=23/24 classification still assumes minimum degree at least one. Global range stays 40<=tau_5<=44.

## New next target

Derive, under a justified D5-type labeling and the six-exception contact constraints, an **upper** bound on the Q-column alignment norm below `47623/254016`; or formulate a labeling-free center-sensitive polynomial certificate. A matching upper bound would eliminate Type E in the corresponding justified branch. Avoid treating high 20-vector frame mass as a D5 alignment theorem.

## External research context

Musin, *Bounds for Codes by Semidefinite Programming* (2008), Section 5, reports the Boyvalenkov antipodal five-dimensional 40 bound. Cohn–Jiao–Kumar–Torquato, *Rigidity of spherical codes* (2011), analyzes D5 jamming. A 2026 Discrete & Computational Geometry article, *Variations on Five-Dimensional Sphere Packings*, describes four non-isometric 40-point kissing configurations, reinforcing the need to avoid assuming uniqueness of five-dimensional near-optimal arrangements.