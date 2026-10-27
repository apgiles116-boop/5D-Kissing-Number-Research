# A quantitative quartic integrality gap for 21 projective lines in R^5

Date: 2026-10-27. **[PROVED EXACTLY — universal 21-line theorem]**. This is a self-contained quantitative consequence of the standard degree-four harmonic positivity argument; no claim of priority in the literature is made. **[OPEN]** It does not eliminate Type E or improve the global bound 40 <= tau_5 <= 44.

## 1. Exact harmonic identity

Let v_1,...,v_21 be unit vectors in R^5, representing 21 projective lines. Put

    x_ij=(v_i.v_j)^2,
    f_ij=x_ij*(x_ij-1/4),
    P=sum_{i<j} max(f_ij,0), E=sum_{i<j} max(-f_ij,0),
    F=sum_i v_i*v_i^T,
    V=||F-(21/5)I||_F^2,
    K=sum_{i,j} [(v_i.v_j)^4-(2/3)*(v_i.v_j)^2+1/21].

The degree-four polynomial in K is the positive-definite degree-four spherical harmonic kernel in dimension five (the inner product of symmetric trace-free fourth tensors). Therefore K>=0. Expansion of the quadratic frame moment and the harmonic moment gives the EXACT identity

    P-E = (5/24)*V + (1/2)*K >= (5/24)*V >=0.        (1)

Also

    sum_{i<j} x_ij = 168/5 + V/2.                     (2)

If all pair coherences were <=1/2, then P=0, so (1) forces E=V=K=0 and every x_ij is either 0 or 1/4. But (2) would require 168/5=33.6 to be an integer multiple of 1/4, an impossibility. Thus 21 lines cannot have coherence <=1/2. This is a direct quartic-integrality proof of the zero-midpoint exclusion, independent of any asserted uniqueness of D5.

## 2. Quantitative theorem

**[PROVED EXACTLY]** Every 21 unit projective representatives in R^5 satisfy

    P >= (sqrt(15)-3)/80 = 0.0109122918275927... .   (3)

Proof. Suppose 0<=P<p_*:=(sqrt(15)-3)/80. Since (1) gives E<=P and V<24*p_*/5<3/50<1/10, (2) places X:=sum x_ij in [33.6,33.65). Consequently X is at least 1/10 away from every multiple of 1/4.

For each pair round x=x_ij to the nearer of 0 and 1/4, obtaining k_ij/4 with k_ij in {0,1}. If x>=1/4, then

    |x-1/4| <= 4*x*(x-1/4).

If 0<=x<=1/4, put d=min(x,1/4-x) and q=sqrt(1/64-P). Since d*(1/4-d)=x*(1/4-x)<=E<=P and 0<=d<=1/8, we have d<=1/8-q, hence

    d <= x*(1/4-x)/(1/8+q).

Summing the rounding errors over all 210 pairs gives, for the integer M=sum k_ij,

    |X-M/4| <= 4P + E/(1/8+q)
              <= 4P + P/(1/8+q)
               = 4P + 1/8-q.                         (4)

The right side is strictly increasing in P. At P=p_* the value equals exactly 1/10, because q_*=(2*sqrt(15)-5)/40 and

    4*p_* + 1/8 - q_* = 1/10.

Thus for P<p_*, (4) is strictly less than 1/10, contradicting the lattice-distance lower bound. This proves (3). The proof uses only elementary exact inequalities and harmonic PSD.

**Scope:** P is the total POSITIVE quartic defect of the full 21 normalized lines, not the raw six-core Type-E defect. The numerical bound (3) is deliberately not advertised as sharp.

## 3. Exact D5 Q-Gram spectrum and an interpretive correction

**[PROVED EXACTLY — D5 template]** For the 20 D5 projective root representatives (e_i +/- e_j)/sqrt(2), define Q_v=vv^T-I/5. Their 20x20 Q-Gram matrix has spectrum

    eigenvalue 3/2 with multiplicity 4,
    eigenvalue 1   with multiplicity 10,
    eigenvalue 0   with multiplicity 6.

Proof. The traceless symmetric 5x5 matrices decompose orthogonally into diagonal traceless (dimension 4) and off-diagonal (dimension 10). For each pair i<j, write Q_ij^+/-=D_ij +/- O_ij, where D_ij=(E_ii+E_jj)/2-I/5 and O_ij=(E_ij+E_ji)/2. The frame operator sum_{ij,+/-} |Q_ij^+/-><Q_ij^+/-| acts as 3/2 on diagonal traceless matrices, since (1/2)sum_{i<j}(t_i+t_j)^2=(3/2)sum_i t_i^2 when sum t_i=0, and as 1 on each normalized off-diagonal basis matrix. This proves the spectrum.

**[PROVED EXACTLY — universal dimensional observation]** For ANY twenty projected vectors z_i in R^5, the matrices Q_i=z_i z_i^T-(||z_i||^2/5)I belong to a 14-dimensional real vector space. Hence their Q-Gram nullity is AT LEAST six, irrespective of contact structure. D5 achieves the generic maximum rank 14. The numerical equality between six exceptional core pairings and six Q-null directions is therefore NOT evidence of a canonical one-to-one correspondence; the six-dimensional nullspace is forced by dimension alone. D5's special information lies in the structure of its nullspace and nonzero spectrum, not its nullity count.

## 4. Relation to Type E and proof ledger

For the actual isolated-center Type-E branch, the 21 unit lines are x_0 and u_i=z_i/sqrt(1-a_i), i=1,...,20. Equation (3) forces their total positive homogeneous quartic defect to be >=p_*. This includes the six potentially exceptional core pairs AND the center row and normalization effects.

**Notation warning:** in the earlier six-exception flex note, the retained *homogeneous* cap 5792292955405/4129544208384 is applied to the unweighted excess sum [(v_i.v_j)^2-1/4]_+, whereas the present P uses the quartic-weighted sum [(v_i.v_j)^2*((v_i.v_j)^2-1/4)]_+. Other notes have reused the letter P for the weighted quantity. These must not be identified without an explicit conversion. Even after conversion, the six-core cap does not control the center row or normalization contributions.

At A=0, all 21 pair coherences are <=1/2, contradicting (3); this recovers the zero-midpoint boundary exclusion constructively.

**[RETAINED]** 40<=tau_5<=44; 1/49<A<=383/504 for Type E; M(F3)<=89; M(P)>=S/2-28/3; twenty-edge mass >=2137/6; raw squared-correlation floor >=8790283/317520; the 184-safe/six-core distinction. Types C,D,E, generic e>=27, and non-isolated branches remain open. Sparse e=23,24 classification remains conditional on delta(G)>=1.

Companion exact verifier: `research/tau5_21line_quartic_integrality_gap_2026-10-27_verify.py`.
