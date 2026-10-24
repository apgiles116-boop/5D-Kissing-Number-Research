# Type E: labeling-free center/Q hinge and exact D5 Q-spectrum (2026-10-24)

**[PROVED EXACTLY]** Universal center hinge and Q-operator inequality; exact D5 Q-frame spectrum and coefficient stability. **[OPEN]** Type E elimination, global D5 labeling, and all unresolved 41-code branches. Retain 40 <= tau_5 <= 44.

## 1. Labeling-free center hinge

For a unit isolated center u and selected unit endpoints x_i^±=m_i±z_i, write a_i=||m_i||², m_i·z_i=0, ||z_i||²=1-a_i, b_i=|u·z_i|, A=sum_i a_i. Assume u·x_i^±<=1/2. Let

    C*=512/(207+33sqrt(33))=46/3-22sqrt(33)/9 ≈1.291069086240374.

**[PROVED EXACTLY]** Each edge satisfies

    a_i >= C* ((b_i²-1/4)_+)².                              (1)

For 20 edges, the exact polynomial minorant gives

    A >= C* sum_i ((b_i²-1/4)_+)²
      >= C*[(39/64)sum_i b_i^4 -(3/16)sum_i b_i²].           (2)

Proof: orient z_i so u·z_i=b_i. Center feasibility gives u·m_i+b_i<=1/2. If b_i>1/2, orthogonality and Cauchy-Schwarz yield

    (b_i-1/2)² <= a_i(1-b_i²/(1-a_i)) <= a_i(1-b_i²).

Also b_i=(u·x_i^+-u·x_i^-)/2<=3/4, since center-endpoint inner products lie in [-1,1/2]. Therefore

    a_i >= (b_i²-1/4)² / D(b_i), D(b)=(b+1/2)²(1-b²).

On [1/2,3/4], D'(b)=-(2b+1)(4b²+b-2)/2; its maximum is D((sqrt(33)-1)/8)=(207+33sqrt(33))/512. This proves (1). The hinge h(x)=(x-1/4)_+² obeys h(x)>=p(x)=39x²/64-3x/16: for x<=1/4, p(x)=x(39x-12)/64<=0; for x>=1/4, h(x)-p(x)=(5x-2)²/64>=0. Summing proves (2). C* is optimal only for this intermediate D(b) estimate; no sharpness claim for full endpoint geometry.

### Q-form [PROVED EXACTLY]

Set Q_i=z_i z_i^T-(1-a_i)I/5, U=uu^T-I/5, and t_i=b_i²=(1-a_i)/5+<Q_i,U>, using the Frobenius pairing. Then (2) becomes

    (1-3C*/80)A >= C*[(39/64)sum_i t_i² -3/4
                         -(3/16)<sum_i Q_i,U>].             (3)

The exact fourth-moment expansion is

    sum_i t_i² = sum_i <Q_i,U>²
       +(2/5)sum_i(1-a_i)<Q_i,U> +(1/25)sum_i(1-a_i)².      (4)

This is a labeling-free second-order center/Q coupling, not yet a Type-E contradiction.

## 2. Exact D5 Q-frame spectrum

For v_ij^±=(e_i±e_j)/sqrt(2), 1<=i<j<=5, let Q_ij^±=v_ij^±(v_ij^±)^T-I/5 and let K0 be their 20x20 Frobenius Gram matrix.

**[PROVED EXACTLY]** Its spectrum is

    eigenvalue 3/2, multiplicity 4;
    eigenvalue 1,   multiplicity 10;
    eigenvalue 0,   multiplicity 6.                          (5)

Proof: define D_ij=E_ii+E_jj-2I/5 and O_ij=E_ij+E_ji, so Q_ij^±=(D_ij±O_ij)/2. For any tracefree symmetric V,

    sum_{i<j,±}<Q_ij^±,V>²
      =(1/2)sum_{i<j}(<D_ij,V>²+<O_ij,V>²)
      =(3/2)||V_diag||_F²+||V_off||_F².                     (6)

The diagonal tracefree space has dimension 4 and offdiagonal space dimension 10, giving the positive spectrum. Rank=14 and nullity=6. With Pi0 the orthogonal projector onto ker K0, every c in R^20 satisfies

    ||(I-Pi0)c||² <= c^T K0 c <= (3/2)||(I-Pi0)c||².      (7)

For U=uu^T-I/5, (6) yields

    sum_{i<j,±}(u^T Q_ij^±u)²
      =4/5+(1/2)sum_j(u_j²-1/5)².                           (8)

**Structural audit [PROVED EXACTLY]:** six null directions alone are not special to D5. Any 20 tracefree symmetric 5x5 matrices live in a 14-dimensional space, so their Q-Gram has nullity at least six. The explicit global tight-frame relation, five support-cycle relations, and positive spectral gap in (5) are the distinctive D5 features. No correspondence to the six exceptional Type-E pairings is established.

## 3. Status

**[RETAINED]** Type E: M(F3)<=89; matching M(P)>=S/2-28/3; A<=383/504; six-exception restrictions; 21-line zero-midpoint boundary exclusion. Uniform two-sided three-point SDP at mu=1/2 remains closed as primary route.

**[OPEN]** A labeling-free lower fourth-center-moment bound making (3) incompatible with A<=383/504; a justified D5 labeling to use the five cycle kernels; Type E, C, D, generic e>=27 and other branches. Global proved range remains 40<=tau_5<=44.

Exact SymPy verification is in the companion _verify.py file.
