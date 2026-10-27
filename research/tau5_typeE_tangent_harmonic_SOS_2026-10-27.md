# Type E: exact center-tangent fourth-harmonic sum-of-squares decomposition

Date: 2026-10-27. **[PROVED EXACTLY — universal algebra and harmonic positivity]** for the identities below. **[PROVED EXACTLY — conditional on retained Type-E endpoint hypotheses]** for the isolated-center corollary. **[OPEN]** No Type-E exclusion; global proved range remains 40 <= tau_5 <= 44.

## 1. Setup

For arbitrary vectors z_1,...,z_20 in R^5 and a unit vector x, put r_i=||z_i||^2, R2=sum r_i^2, S4=sum r_i^4, c_i=x.z_i, t0=sum c_i^2, and

    D_raw = sum_{i<j} (z_i.z_j)^2*((z_i.z_j)^2-r_i*r_j/4).

Define F=sum_i r_i*z_i*z_i^T, E=F-(R2/5)I, P=I-xx^T, and

    d=x^T E x=sum_i r_i*c_i^2-R2/5,
    b=P E x=sum_i r_i*c_i*(z_i-c_i*x),
    C=P E P,
    p=sum_i c_i^3*(z_i-c_i*x),
    h=sum_i [c_i^4-(2/3)r_i*c_i^2+r_i^2/21].

All expressions are polynomial in the original projected vectors and x.

## 2. Harmonic Bessel inequality with tangent derivatives

The homogeneous degree-four harmonic kernel is

    H4(v,w)=(v.w)^4-(2/3)||v||^2||w||^2*(v.w)^2
              +(1/21)||v||^4||w||^4.

It is positive definite by the spherical harmonic addition theorem. Put K=sum_{i,j}H4(z_i,z_j). At unit x the evaluation feature has squared norm H4(x,x)=8/21. The four tangential derivative features are orthogonal to evaluation and each other, and have squared norm H4'(1)=8/3. The tangent derivative of sum_i H4(x,z_i) is

    g=4p-(4/3)b.

Consequently

    K >= (21/8)h^2+(3/8)||g||^2.

Define K_res=K-(21/8)h^2-(3/8)||g||^2 >=0.

## 3. Exact center-tangent SOS

The weighted harmonic identity is

    D_raw=R2^2/56-(3/8)S4+(5/24)||E||_F^2+K/2.

Since tr(C)=-d on x-perp,

    ||E||_F^2=(5/4)d^2+2||b||^2+||C+(d/4)P||_F^2.

Completing the remaining vector square gives

    (5/12)||b||^2+3||p-b/3||^2
       =(5/3)||p||^2+(3/4)||b-(4/3)p||^2.

Thus the following is an **exact identity**:

    D_raw = R2^2/56-(3/8)S4
            +(25/96)d^2+(21/16)h^2+(5/3)||p||^2
            +(3/4)||b-(4/3)p||^2
            +(5/24)||C+(d/4)P||_F^2
            +(1/2)K_res.

All terms after the first two are nonnegative. In particular,

    D_raw >= R2^2/56-(3/8)S4
             +(25/96)d^2+(21/16)h^2+(5/3)||p||^2.

The new transverse fourth-moment term (5/3)||p||^2 is label-free and denominator-free; no generic SDP is needed.

## 4. Isolated-center Type-E consequence

For x=x0, endpoint safety implies |c_i|<=1/2, so sum c_i^4<=t0/4. Hence

    h <= t0/4-(2/3)sum_i r_i*c_i^2+R2/21.

Therefore

    D_raw >= R2^2/56-(3/8)S4
             +(25/96)(sum_i r_i*c_i^2-R2/5)^2
             +(21/16)[(2/3)sum_i r_i*c_i^2-t0/4-R2/21]_+^2
             +(5/3)||sum_i c_i^3(z_i-c_i*x0)||^2.

The transverse moment can vanish by symmetry. Thus this is a new polynomial constraint for the six-exception KKT/SOS problem, **not** a Type-E exclusion or a new uniform numerical defect bound.

## 5. Verification and proof status

The companion verifier checks the exact decomposition on twenty rational vectors. Universal nonnegativity of K_res is proved analytically by harmonic reproducing-kernel orthogonality, not by numerical sampling.

**[RETAINED]** 1/49<A<=383/504; M(F3)<=89; matching mass >=S/2-28/3; twenty-edge mass >=2137/6; squared-correlation floor >=8790283/317520. Types C, D, E, generic e>=27 and non-isolated branches remain open. Sparse e=23/e=24 classification is conditional on delta(G)>=1.
