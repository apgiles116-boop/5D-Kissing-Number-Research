# Exact 21-line edge-count and frame-stability obstruction (2026-11-01)

**[PROVED EXACTLY — standalone]** For any 21 unit vectors u_0,...,u_20 in R^5, put x_ij=(u_i·u_j)^2 and E=Σ_{i<j}[x_ij(x_ij−1/4)]_+. Then

    E > 27/2000 = 0.0135.

Consequently Δ=Σ_{i<j}(|u_i·u_j|−1/2)_+ > 9/1000. This improves the earlier E>1/341 and Δ>2/1023. It is **not** a Type-E exclusion or a claim of novelty over the literature.

## Exact proof

Set S=Σ_i u_i u_i^T, B=S−(21/5)I, t=tr(B²), and N=Σ_{i<j}[−x_ij(x_ij−1/4)]_+. The Gegenbauer identity

    s^4−s²/4 = 1/28+(1/3)P_2(s)+(8/21)P_4(s)

with P_2=(5s²−1)/4 and P_4=(21s⁴−14s²+1)/8, together with positivity of the harmonic sums and exact diagonal cancellation, gives

    E−N ≥ (5/24)t,   N≤E−5t/24,   t≤24E/5.     (1)

Round x_ij to q_ij=0 for x_ij<1/8 and q_ij=1/4 otherwise. Let e be the number of rounded edges. For 0≤y≤1/64 set g(y)=(1−sqrt(1−64y))/8. For a negative quartic term, the magnitude d of its rounding error satisfies y=d(1/4−d), so d=g(y). Since g is increasing, convex, and g(0)=0, its rounding errors total at most g(N) when N<1/64. Positive quartic terms have rounding error x−1/4≤4x(x−1/4). Thus, if E<1/64,

    R=Σ_{i<j}|x_ij−q_ij|≤4E+g(N),              (2)
    −g(N)≤Σ_{i<j}(x_ij−q_ij)≤4E+g(N).          (3)

The frame trace identity is

    Σ_{i<j}x_ij = 168/5+t/2.                   (4)

Assume E≤E_0=27/2000. Exact arithmetic gives g(E_0)<79/1000: indeed 1−64E_0=17/125 and sqrt(17/125)>46/125 because 2125>2116.

If e≤133, (3)–(4) imply 7/20≤4E+g(N)<133/1000, impossible. If e≥135, they imply 3/20−t/2≤g(N)<79/1000; yet t≤24E/5 forces 3/20−t/2≥147/1250>79/1000. Therefore **e=134**.

For e=134, equations (1),(3),(4) yield

    1/10+t/2≤4E+g(E−5t/24).

Since g'(y)≥4, the right side is ≤4E+g(E)−5t/6. Hence

    (4/3)t≤4E+g(E)−1/10,
    t<(3/4)(4E_0+79/1000−1/10)
     =99/4000<1/40.                            (5)

Let k_i be the rounded degree at vertex i, so Σ_i k_i=2e=268. For every integer k≥0,

    |16/5−k/4| ≥ 1/20+(3/20)(13−k).

Summing gives the exact degree-discrepancy lower bound

    Σ_i|16/5−k_i/4|≥21/20+(3/20)(273−268)=9/5. (6)

But Σ_{j≠i}x_ij=16/5+u_i^T B u_i, so

    Σ_i|16/5−k_i/4|
      ≤Σ_i|u_i^T B u_i|+2R
      ≤(21/5)tr|B|+t+8E+2g(N).

For trace-free symmetric 5×5 matrices, tr|B|≤sqrt(24/5)sqrt(t). Using (5), sqrt(3)<7/4, and E≤E_0 gives

    Σ_i|16/5−k_i/4|
      <21sqrt(3)/25+1/40+8E_0+158/1000
      <147/100+1/40+108/1000+158/1000
      =1761/1000<9/5,

contradicting (6). Therefore E>27/2000. Since [s⁴−s²/4]_+≤(3/2)(|s|−1/2)_+ for |s|≤1, Δ>(2/3)(27/2000)=9/1000.

## Application and status

**[CONDITIONAL TYPE E]** Under the previously recorded 21-vector normalization, center-safety, and six-exception hypotheses, the existing transfer improves to

    27/2000 < (320/81)A+(49/54)A_C+2D_raw.

This does **not** contradict retained Type-E bounds. No D5 labeling, core coplanarity, or new SDP is used in the standalone theorem. Type E, C, D, generic e≥27, and non-isolated branches remain open. The e=23/24 sparse classification still assumes δ(G)≥1. Preserve M(F3)≤89 and M(P)≥S/2−28/3.

**[GLOBAL PROVED RANGE — UNCHANGED]** 40≤τ_5≤44.

Exact verifier: research/tau5_21line_edgecount_stability_2026-11-01_verify.py.
