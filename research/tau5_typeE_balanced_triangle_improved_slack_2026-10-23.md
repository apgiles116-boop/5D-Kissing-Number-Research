# Type E: improved matching-uniform balanced-triangle slack (2026-10-23)

**[PROVED EXACTLY]** Euclidean vector theorem under deep-contact/balanced-triangle hypotheses, with exhaustive finite F3 enumeration. **[CONDITIONAL ON RETAINED TYPE-E REDUCTIONS]** Type-E application. **[OPEN]** Type-E elimination. Global proved range: 40 <= tau_5 <= 44.

## Theorem

For any perfect matching of F3 (edge list 02,04,05,14,17,23,27,36,56,57), write its four deep edge endpoints as x_i^±=m_i±z_i with m_i.z_i=0 and a_i=||m_i||²<1/4. Put C=sum a_i, d=sum_{i<j}(-m_i.m_j)_+, epsilon=C-d. Then 0<C<1 and

    epsilon > C²/(3072+80C) > C²/3152.

This strengthens the earlier matching-uniform C²/4608 slack by a factor 288/197 (about 46.2%). No D5 labeling is used.

## Proof

Define M=sum m_i and E_ij=a_i+a_j-2|m_i.m_j|=min(||m_i-m_j||²,||m_i+m_j||²)>=0. The exact identity

    4epsilon=||M||²+sum_{i<j}E_ij                              (1)

follows by expanding the negative-part function.

The exact F3 enumeration gives three perfect matchings; each has a balanced quotient triangle among three matched-pair indices I, with omitted index h. For that triangle choose endpoint signs sigma_ij,tau_ij, with beta_ij=sigma_ij*tau_ij=eta_i*eta_j for consistent signs eta_i. Summing its three strict deep endpoint inequalities gives

    sum_T (x_i^sigma.x_j^tau+1/2)
      = ||sum_{i in I}m_i||²/2+||sum_{i in I}eta_i z_i||²/2+T < 0,

where T=sum_T(sigma_ij*z_i.m_j+tau_ij*m_i.z_j). Orthogonality m_i.z_i=0 yields |T|<=2sum_T sqrt(E_ij)<=2sqrt(3)r, with r²=sum_{i<j in I}E_ij. Thus

    ||sum_{i in I}m_i||²/2 < 2sqrt(3)r.                     (2)

Put s=||M||, t²=sum_{i in I}E_ih, w=||sum_{i in I}m_i||. Equation (1) says s²+t²+r²=4epsilon. Writing b_i=||m_i||, the reverse triangle inequality in R⁴ and |b_i-b_h|²<=E_ih imply

    sqrt(C)<=2b_h+t<=2w+2s+t.

Therefore w>=max(0,sqrt(C)/2-s-t/2), which implies the globally valid bound w²>=C/4-sqrt(C)(s+t/2). Combining with (2),

    C/8 < sqrt(C)*s/2+sqrt(C)*t/4+2sqrt(3)r.               (3)

Cauchy-Schwarz and s²+t²+r²=4epsilon give

    C/8 < sqrt(12+5C/16)*2sqrt(epsilon)
        = sqrt(48+5C/4)*sqrt(epsilon).

Squaring proves epsilon>C²/(3072+80C). Since C<1, epsilon>C²/3152. If C=0, the balanced triangle would require three unit signed z vectors all pairwise inner products <-1/2, contradicting nonnegativity of their squared vector sum; hence C>0.

## KKT consequences

Keep inequality (3) **for each balanced triangle** separately. The exhaustive checker finds four balanced triangle edge selections in each matching, involving at least two distinct triples of pair indices (all four triples for matching P2). These simultaneous constraints are stronger than the scalar bound and can be encoded with nonnegative auxiliary variables s,t,r.

In the retained six-exception bound, 4d=4C-4epsilon, so

    4d < 4C-C²/(768+20C) < 4C-C²/788.

The independent 4d<=4C-||M||² remains valid. Combine via max(||M||²,C²/788), **not by adding** the penalties. The older C²/1152 penalty may thus be replaced by C²/788. This does not eliminate Type E or contradict A<=383/504.

## Ledger

[PROVED EXACTLY] Graph enumeration, identity (1), triangle inequality (3), new rational slack. [CONDITIONAL] Insertion into retained Type-E endpoint/matching/defect reductions. [OPEN] Type E; Types C and D; generic e>=27; non-isolated 41-code branches; D5 labeling/Q-cycle identification. Preserve M(F3)<=89, M(P)>=S/2-28/3, selected mass >=2137/6, A<=383/504; sparse e=23/24 graph classification requires delta(G)>=1.
