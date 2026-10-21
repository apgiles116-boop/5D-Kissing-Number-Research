# Type E: negative-Gram raw/squared defect audit (2026-10-21)

**[PROVED EXACTLY — vector lemma]** For arbitrary real midpoints m_i, let C=sum ||m_i||² and w=sum ||m_i||m_i. Then

    sum_{i<j} (-m_i·m_j)_+² <= (C²-||w||²)/4 <= C²/4.

Proof: with a_i=||m_i||², u_i=m_i/sqrt(a_i), use (-t)_+² <= (1-t)/2 for -1<=t<=1 and sum over a_i a_j. The inequality is dimension-free and sharp.

**[PROVED EXACTLY — endpoint geometry]** Averaging all four cross-endpoint kissing inequalities gives m_i·m_j+|z_i·z_j|<=1/2. Hence δ_ij=(|z_i·z_j|-1/2)_+ <=(-m_i·m_j)_+.

**[AUDIT CORRECTION]** D*=1780062775/4032758016 is a cap on the sum of six *raw absolute-correlation* defects δ_ij. It is **not** automatically a cap on squared defects ((z_i·z_j)²-1/4)_+=δ_ij+δ_ij². Previous summaries using D* directly as the squared-defect cap are not certified by that input. The new lemma repairs the conversion:

    Hsq=sum_core (δ_ij+δ_ij²) <= D*+C²/4.

**[PROVED EXACTLY — conditional on retained Type E mass/harmonic lemmas]** With U>=0 and the isolated-center mass gap, the selected four-core deficits obey W<=154/3-U/2-35/512. Concentration of D(a)=196a-644a²+896a³-448a⁴ gives C<557185/1000000 (exact bracket D(57185/1000000)>28/3-35/512). The retained total squared-correlation floor is R>56719845779369/2000000000000.

Therefore the **corrected safe-pair floor** is

    R_safe > 1659789202653287342993/63011844000000000000
           =26.34090826882145... .

The exact stability identity, with d=sum_core δ_ij, Hminus=sum_core(1/4-(z_i·z_j)²)_+, A2=sum a_i², V=||sum Q(z_i)||², is

    R_safe >=57/2-3A+A²/10-A2/2+V/2-D*-C²/4
             +(D*-d)+||w||²/4+Hminus.

At least 101 of the 184 safe pairs have |z_i·z_j|>63/500, hence some selected edge has >=11 such safe neighbors. This is an incidence theorem, not a rigidity result or a Type E exclusion.

**[OPEN]** Type E, Types C/D, generic e>=27; global 40<=tau_5<=44. Sparse e=23/24 classification retains its delta(G)>=1 hypothesis. Do not infer a D5 labeling or transfer matching-specific bounds between F3 matchings.
