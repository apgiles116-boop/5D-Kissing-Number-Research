# Type E: sharp singleton midpoint-sum inequality and zero-contact slack rigidity

**2026-10-25.** **[PROVED EXACTLY]** Pairwise results below, including an exact equality witness. **[PROVED UNDER RETAINED TYPE-E INPUTS]** Disjoint singleton-defect budget and 184 safe-pair restrictions. **[OPEN]** Type-E elimination and any improvement on `40 <= tau_5 <= 44`.

## Pairwise notation

For selected deep edges `x_i^±=m_i±z_i`, `x_j^±=m_j±z_j`, put `a_i=||m_i||²<1/4`, `a_j<1/4`, `t=a_i+a_j<1/2`. Orient so `r=z_i.z_j=|z_i.z_j|`. Let `d=(r-1/2)_+`, `c=m_i.m_j`, `p=m_i.z_j`, `q=z_i.m_j`. Four cross-endpoint dots are `c+r±(p+q)` and `c-r±(p-q)`. All distinct endpoint dots are `<=1/2`; a deep contact has dot `<-1/2`.

## Theorem 1: singleton midpoint-sum cost [PROVED EXACTLY]

If **at most one** of the four cross-endpoint pairs is deep, then

```
2d <= t(1-t),
d <= (a_i+a_j)(1-a_i-a_j)/2,
t >= (1-sqrt(1-8d))/2,  and d<1/8 for d>0.
```

Proof: If `d>0`, averaging same-sign cross products gives `c+r<=1/2`, hence `c<=-d`. At least one of the two opposite-sign cross products is not deep, so `|p-q|>=d-c>=2d`. Since `m_i.z_i=m_j.z_j=0`,

```
(d-c)^2 <= (p-q)^2
         = |(m_i+m_j).(z_i-z_j)|^2
         <= (t+2c)(1-t-2d)
         <= (t-2d)(1-t-2d).
```

Both factors in the penultimate product are nonnegative. Subtracting `4d²` from the final product gives exactly `t(1-t)-2d`, proving the theorem. The **unrelaxed** inequality involving `c` should be kept in future finite polynomial/Gram tests.

This strengthens and subsumes the prior individual midpoint polynomial: since `a_j<1/4` and `t<1/2`, `d < (a_i+1/4)(3/4-a_i)/2 = 3/32+a_i/4-a_i²/2` (and symmetrically for `a_j`). Also `t>=2d+4d²`, an exact second-order midpoint cost.

## Sharp rational witness [PROVED EXACTLY]

In ordered vectors `(m_i,z_i,m_j,z_j)`, use the Gram matrix

```
G = [[ 4,  0, -3, -3],
     [ 0, 28,  3, 19],
     [-3,  3,  4,  0],
     [-3, 19,  0, 28]] / 32.
```

Its eigenvalues are `0, 5/16, (27-sqrt(409))/32, (27+sqrt(409))/32`: PSD, rank 3. Both within-edge dots are `-3/4`. The four cross-endpoint dots are `1/2, 1/2, -1/2, -7/8`, so exactly one cross contact is deep and every kissing upper bound holds. Here `a_i=a_j=1/8`, `t=1/4`, `d=3/32`, and `2d=t(1-t)=3/16`. Thus the factor `1/2` in the energy bound cannot be decreased universally. This witness is not a full Type-E configuration.

## Corollary: disjoint singleton pairings [PROVED UNDER TYPE-E INPUTS]

For two disjoint singleton-contact pairings `(i,j)`, `(k,l)`, write `S=a_i+a_j+a_k+a_l<=A<=B=383/504`. Then

```
d_ij+d_kl <= [t1(1-t1)+t2(1-t2)]/2
           <= S/2-S²/4
           <= B/2-B²/4
           = 239375/1016064 ≈ 0.235590474615772.
```

This improves the previous generic disjoint-defect bound `B/2≈0.37996031746` **only when both pairings are singleton-contact**. The retained F3 perfect-matching patterns have either six singleton pairings, or four singleton, one double and one zero pairing.

## Theorem 2: zero-contact safe-slack rigidity [PROVED EXACTLY]

If **none** of the four cross-endpoint pairs is deep, let `h=1/2-r>=0`. All four cross dots are in `[-1/2,1/2]`, so

```
|p+q|<=h-c,   |p-q|<=h+c,   |c|<=h,
|m_i.m_j|<=h, |m_i.z_j|<=h, |z_i.m_j|<=h,
p²+q² <= h²+c²,
r²+c²+p²+q² <= 1/4.
```

The last inequality follows by summing squares of the four cross dots: their sum of squares is `4(r²+c²+p²+q²)<=1`. In particular, `r=1/2` forces `c=p=q=0`; more generally `c²+p²+q²<=3h²`.

For Type E `H=16K2+F3`, **all 184 pairings outside the four-edge F3 core** have zero deep cross contacts. Thus all of these inequalities apply to all 184, and also to any zero-contact core pairing.

## Ledger

**[RETAINED INPUTS, NOT REPROVED HERE]** `M(F3)<=89`, `M(P)>=S/2-28/3`, `A<=383/504`, six candidate core raw exceptions, previous certified `sum_core d²<19/250`, and the 184-safe squared-correlation floor `>12938492114773/504094752000`.

**[OPEN]** Whether the new 184-fold small-slack orthogonality constraints, the unrelaxed singleton Gram inequality, and the rank-five endpoint PSD constraints contradict the midpoint budget. Types C, D, generic `e>=27`, non-isolated cases remain open. Sparse `e=23,24` graph classification is conditional on `delta(G)>=1`.

**Next:** include the unrelaxed singleton constraint and all zero-contact mixed-product slack inequalities in the four-core/rank-five polynomial optimization. Seek a labeling-free frame stability contradiction rather than another generic SDP.
