# Type E: fixed-core-norm spectral completion and isolated/core frame tradeoff (2026-10-29)

**[PROVED EXACTLY — STANDALONE LINEAR ALGEBRA]**. Type-E application **[CONDITIONAL ON RETAINED 16+4 MATCHING DECOMPOSITION]**. No D5 alignment, generic SDP, or Type-E exclusion. Global proved range remains **40 <= tau_5 <= 44**.

## Setup
Let S=sum_{i=1}^{16} z_i z_i^T, C=sum_{j=1}^4 q_j q_j^T, w_j=||q_j||^2 sorted w1>=...>=w4>=0, c=sum w_j, mu=(tr S+c)/5, E=S+C-mu I, V=||E||_F^2. Write eigenvalues s1>=...>=s5 of S. In Type E, w_j=1-a_j, c=4-A+x, A=sum_{20}a_i, x=sum_{16}a_i.

## Theorem A: exact norm-constrained rank-four completion
**[PROVED]** The minimum of V over all four columns q_j with prescribed squared norms w_j is

    Phi_w(S)=(s1-mu)^2
      +min_{lambda in L(w)} sum_{j=1}^4(s_{6-j}+lambda_j-mu)^2,

where L(w) is the four-variable convex polytope
    lambda1>=lambda2>=lambda3>=lambda4>=0,
    sum lambda_j=c,
    sum_{j=1}^k lambda_j>=sum_{j=1}^k w_j (k=1,2,3).

**Proof:** The 4x4 Gram matrix K=(q_j dot q_k) has diagonal w and eigenvalues lambda. Schur-Horn characterizes its possible eigenvalues exactly by lambda majorizing w. C=QQ^T has eigenvalues (lambda1,...,lambda4,0). Von Neumann trace rearrangement minimizes tr(SC) by opposite eigenvalue pairing, pairing s1 with 0 and s_{6-j} with lambda_j. Conversely Schur-Horn constructs K, and orthogonal left rotation realizes this opposite alignment. The displayed strictly convex quadratic objective follows by expansion and is attained. Dropping majorization recovers the previous rank-four water-filling bound, so Phi_w>=Phi.

For k=1,...,4 define W_k=sum_{j<=k}w_j and Delta_k=W_k-k*mu+sum_{j=1}^k s_{6-j}. Schur-Horn and Ky Fan's variational formula give
    V >= 5/[k(5-k)] * max(Delta_k,0)^2.
Indeed, sum_{j<=k}lambda_j(C)>=W_k, while C=mu I-S+E and tr E=0 imply sum_{j<=k}lambda_j(C)<=k mu-sum_{j<=k}s_{6-j}+sqrt(k(5-k)/5)*sqrt(V). Also retain the independent rank-four-kernel bound V>=5/4*(s1-mu)^2. The k=4 term is included in that last bound.

## Theorem B: exact SOS and robust core-norm dispersion
**[PROVED]** Choose any unit top eigenvector p of S, P=pp^T, r=mu-c/4, S0=mu P+r(I-P), H=S-S0, and sigma=||H||_F. Define D_w=sum_j(w_j-c/4)^2. Then

    ||C-(c/4)(I-P)||_F^2
      = D_w + 2*sum_{j<k}(q_j dot q_k)^2
            + (c/2)*sum_j(p dot q_j)^2.             (EXACT SOS)

**Proof:** tr(C^2)=sum_j w_j^2+2 sum_{j<k}(q_j dot q_k)^2 and tr(PC)=sum_j(p dot q_j)^2. Expanding the square and using tr C=c, tr(I-P)=4 gives tr(C^2)-c^2/4+(c/2)tr(PC), exactly the right side. As E=H+[C-(c/4)(I-P)], the triangle inequality yields

    sqrt(V)+sigma >= sqrt(D_w+2*sum_{j<k}(q_j dot q_k)^2
                                  +(c/2)*sum_j(p dot q_j)^2),
    V >= max(sqrt(D_w)-sigma,0)^2.

Here sigma^2=(s1-mu)^2+sum_{i=2}^5(s_i-r)^2. Equality in the dispersion bound is attained in the abstract completion problem when S=S0 and the four q_j are mutually orthogonal and perpendicular to p. The identity retains both core-core projected correlations and core projection onto the leading isolated-frame eigenvector.

## Exact rational boundary example (not a spherical-code realization)
Set x=0, A=383/504, four core midpoint energies (5/504,1/4,1/4,1/4). Then
    w=(499/504,3/4,3/4,3/4), c=1633/504,
    mu=9697/2520, r=30623/10080.
For the abstract PSD S=diag(mu,r,r,r,r), unconstrained rank-four completion has V=0 by choosing four completion eigenvalues c/4. But these cannot be eigenvalues of four columns with the prescribed norms, since w1=499/504>c/4=1633/2016. The *exact* norm-constrained optimum is

    Phi_w(S)=D_w=14641/338688,
    extra Q-frame penalty = Phi_w(S)/2=14641/677376
                          ~=0.02161428807634.

It is attained abstractly by four orthogonal core columns with squared norms w in the four-dimensional subspace perpendicular to the first axis. This is a **weak-deep-edge cap-boundary abstract frame**, not a Type-E realization, and does not show a uniform positive Type-E gap.

## Q bridge and open obligations
For twenty projected vectors, a_i=1-||z_i||^2, A=sum a_i, Q=sum_{i<j}(z_i dot z_j)^2, the exact identity is

    Q=30-3A+A^2/10-(1/2)sum_i a_i^2+V/2.

Thus **[CONDITIONAL TYPE-E NECESSARY INEQUALITY]**
    Q>=30-3A+A^2/10-(1/2)sum_i a_i^2+Phi_w(S)/2,
with the simpler bound using (sqrt(D_w)-sigma)_+^2/2.

**[OPEN]** Bound sigma via the 120 isolated-isolated and 64 isolated-core safe Walsh blocks, or lower-bound the retained core-core SOS terms using exact F3 incidence. An anisotropic S can still admit V=0; Type E is not eliminated. Upstream graph/mass/harmonic/signed-Gram certificates not independently recertified. Retain M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, and the audited zero-midpoint boundary. Types C,D, generic e>=27, and non-isolated branches remain open. Global proved interval 40<=tau_5<=44.

Local full proof and exact Fraction verifier are also available in the 2026-10-29 research package.