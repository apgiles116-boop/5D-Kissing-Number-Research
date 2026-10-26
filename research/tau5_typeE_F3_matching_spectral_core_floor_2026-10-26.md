# Type E: exact F3 matching-dependent core-energy floors (2026-10-26)

**[PROVED EXACTLY]** The Gram/PSD certificates below. **[CONDITIONAL TYPE E]** Application to a selected F3 perfect matching. **[OPEN]** Type E elimination.

Let F3 have edges 02,04,05,14,17,23,27,36,56,57, and perfect matchings P1={02,14,36,57}, P2={04,17,23,56}, P3={05,14,27,36}. For any matching P of four deep endpoint edges, write m_i=(p_u+p_v)/2, z_i=(p_u-p_v)/2, and C_P=sum ||m_i||^2=2+(1/2)sum_{uv in P}p_u.p_v. Every endpoint has norm one; deep contacts satisfy p_u.p_v<=-1/2.

## All-singleton matching P2: C_P2 >= 17/250

**[PROVED EXACTLY]** Let G=(p_u.p_v)_{u,v=0}^7, so G is PSD with diagonal 1. Define symmetric integer B with diagonal 12291 on vertices {0,2,5,7} and 11095 on {1,3,4,6}; off-diagonal entries 10000 on P2, 2958 on unmatched deep edges {14,36}, 2587 on unmatched deep edges {02,05,27,57}, and zero otherwise. The characteristic polynomial is exactly

```
(lambda^2-31518 lambda+145435645)
(lambda^2-21170 lambda+15201)
(lambda^2-20428 lambda+11867)^2.
```

B is symmetric and each quadratic has positive root sum and product, hence B is positive definite. Put Q=B/10000, dA=12291/10000, dB=11095/10000, b1=2958/10000, b2=2587/10000. The six unmatched F3 contacts give

```
0 <= tr(QG)
  <= 4(dA+dB)+2 sum_{uv in P2}G_uv-2b1-4b2.
```

Thus sum_{P2}G_uv >= b1+2b2-2(dA+dB)=-483/125, so

**C_P2 >= 2-483/250 = 17/250 = 0.068.**

This needs neither the rank-five restriction nor any nonedge bounds. A numerical eigenvalue-cut relaxation suggests about 0.068148, but optimality is **not proved**.

## Doubled-contact matchings P1 and P3

**[PROVED EXACTLY]** For P1 order edges (02),(14),(36),(57), and orient them in that order. Let eta=(1,-1,-1,1), w_i=eta_i z_i and h=(7,4,4,7). Five distinct quotient pairs 01,02,03,13,23 carry deep contacts; pair 03 has two deep contacts (++ and --), whose average cancels mixing. The missing quotient pair 12 is safe and satisfies m_1.m_2+w_1.w_2<=1/2 by averaging two endpoint upper bounds.

Use the four singleton contacts 04,23,17,56, retaining their mixed terms. The five deep and one safe inequalities give the exact weighted bound

```
||sum h_i m_i||^2 + ||sum h_i w_i||^2 <= -15 - 2T,
T = sum_{ij} L_ij (m_i.z_j),
L = [[0,-28,28,0],[28,0,0,-28],[-28,0,0,28],[0,28,-28,0]].
```

Since the left side is nonnegative, |T|>=15/2. The operator norm of L is exactly 56; Cauchy-Schwarz gives |T|<=56 sqrt(C_P(4-C_P)). Therefore

**C_P(4-C_P)>=225/12544, hence C_P>=2-sqrt(49951)/112>0.00448.**

The F3 automorphism (2 5)(3 6) maps P1 to P3, proving the same bound for P3. These bounds apply to the respective matching's own midpoint energy; energies of different matchings must never be conflated.

## Proof-audit correction

**[CORRECTION]** A sentence in the earlier balanced-triangle note claimed that C=0 alone contradicts the three deep contacts of *one* balanced quotient triangle. This is false: three unit vectors at mutual inner product -1/2 provide a zero-midpoint example. The theorem C-N>C^2/3600 was stated for 0<C<=1, and its positive-C proof is unaffected. Strict C>0 for the actual F3 matchings is now established by the additional constraints in the two certificates above, not by a single triangle.

**[CONDITIONAL TYPE E]** If P2 is the mass-selected matching, A>=C_P2>=17/250, strengthening the retained global Type-E floor 1/99<A in that branch. If P1/P3 is selected, the doubled-pattern core floor applies. None conflicts with A<=383/504.

**[OPEN / UNCHANGED]** Type E, Types C/D, generic e>=27 and non-isolated branches remain unresolved. Global 40<=tau_5<=44. Retain M(F3)<=89, M(P)>=S/2-28/3, total twenty-edge mass >=2137/6. Sparse e=23/24 classification assumes delta(G)>=1.
