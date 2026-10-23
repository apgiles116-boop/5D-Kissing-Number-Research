# Type E: 21-line row-integrality defect gap (2026-10-23)

**[PROVED EXACTLY]** Universal 21-vector theorem. **[CONDITIONAL ON RETAINED TYPE-E REDUCTIONS]** Energy corollary. **[OPEN]** Type E and global 41-code exclusion. The proved global range remains `40 <= tau_5 <= 44`.

## Universal theorem

For arbitrary 21 unit vectors `y_i in R^5`, set `v_ij=(y_i.y_j)^2`, `phi(v)=7v(4v-1)`, and `P=sum_{i<j} max(phi(v_ij),0)`. Then

**P > 9/20 = 0.45.**

This improves the prior `(7sqrt(15)-21)/20 = 0.305544...` bound. No D5 labeling or numerical SDP is used.

### Exact proof

Let `S=sum_i y_i y_i^T`, `B=S-(21/5)I`, `V=tr(B^2)`, and `N=sum max(-phi(v_ij),0)`. The degree-two/four Gegenbauer identity `phi(t^2)=1+(28/3)P2(t)+(32/3)P4(t)` and addition-theorem positivity give

`P-N >= (35/6)V` and `sum_{i<j} v_ij = 168/5+V/2`. (1)

Round each `v<=1/4` to the nearer of `0,1/4` (distance `d=min(v,1/4-v)`), and each `v>1/4` to `1/4`. Write `b_ij` for the rounded value, `e_ij=v_ij-b_ij`, `E=4sum b_ij` (an integer), `D_-=sum_{v<=1/4}d`, and `D_+=sum_{v>1/4}(v-1/4)`. Direct polynomial algebra gives

`N >= (7/2)D_-`, `N >= g(D_-)=7D_--28D_-^2`, `D_+<=P/7`, `sum|e_ij|=D_-+D_+<=3P/7`. (2)

Assume `P<=9/20`. Then `V<=27/350`, `sum|e_ij|<=27/140`, and `sum v_ij in [168/5,168/5+27/700]`. Hence only `E=134` or `E=135` is possible. For `E=135`, `sum e=-3/20+V/2` forces `D_->=3/20-V/2`, so (1)-(2) yield

`P >= (7/2)(3/20-V/2)+(35/6)V =21/40+(49/12)V>9/20`,

a contradiction. Thus `E=134`.

Let `k_i` be the degrees of the rounded graph, so `sum k_i=268`. Let `L={i:k_i<=12}`, `p=|L|` (necessarily `1<=p<=20`), `H` its complement, and `b=sum_{i in L}(16/5-k_i/4)`. The integer degree sum and the baseline contributions at degrees 12 and 13 give

`b>=max(p/5,(25-p)/20)`. (3)

Define `r_i=y_i^T B y_i=k_i/4-16/5+sum_{j!=i}e_ij`. Crucially `sum r_i=tr(BS)=V`. With `E_+=sum max(e_ij,0)` and `q=2E_+`, `sum_L r_i<=-b+q`. For `0<=q<1`, separate Cauchy-Schwarz estimates on L and H give

`sum_i r_i^2 >= (b-q)^2(1/p+1/(21-p)) >= (21/80)(1-q)^2`. (4)

For `p<=5`, use `b>=1` and `1/p+1/(21-p)>=21/80`; for `p>=5`, use `b>=p/5`, `b-q>=(p/5)(1-q)`, and `(p/5)^2(1/p+1/(21-p))=21p/[25(21-p)]>=21/80`. Thus (4) holds without any graph classification.

From (1)-(2), `E_+<=D_-+D_+<=(2/7)N+P/7<=3P/7-(5/3)V`. Therefore `q<=27/70-(10/3)V<1` and

`sum r_i^2 >= (21/80)(43/70+(10/3)V)^2`. (5)

But `sum r_i^2<=tr(B^2 S)<=lambda_max(S)V`. Because B is traceless symmetric 5x5, `lambda_max(B)^2<=(4/5)V<=54/875<1/16`, hence `lambda_max(S)<89/20`. It follows that

`(89/20)V > (21/80)(43/70+(10/3)V)^2`. (6)

For `h(t)=(21/80)(43/70+(10/3)t)^2-(89/20)t`, `h'(t)<0` on `[0,3/100]`, yet `h(3/100)=3/7000>0`. Therefore (6) forces `V>3/100`.

Since `E=134`, `sum e=1/10+V/2`. Thus `D_->=1/10+V/2-P/7>71/1400`. Also `D_-<=(2/7)(P-(35/6)V)<11/140<1/8`. On this interval g is increasing, so

`P >= N+(35/6)V > g(71/1400)+7/40 =19809/70000+7/40=32059/70000>9/20`,

the final contradiction. QED.

## Type-E corollary [CONDITIONAL]

Import the **one mass-selected matching** Type-E degree-counted inequality from `tau5_typeE_degree_counted_integrality_2026-10-23.md`:

`P<=fstar(A)=7A[17+(1+A)^2(7+A)]/[4(1-A)^2]`,

where `A=sum_{i=1}^{20}||m_i||^2<1`. Since `fstar` is increasing and

`9/20-fstar(521/50000)=4072230841334633/24481714410000000000>0`,

the universal theorem yields **A > 521/50000 = 0.01042**. The scalar root is approximately `0.0104237495011`. This improves the preceding `A>0.0071393` by about 45.95% but remains far below the retained ceiling `A<=383/504` and the later mass-derived ceilings.

**[OPEN]** No Type-E exclusion, D5 labeling, or six-exception/Q-kernel correspondence follows. Types C/D, generic e>=27, non-isolated cases, and the sparse-classification delta(G)>=1 dependency remain open. Preserve the exact F3 inputs `M(F3)<=89`, `M(P)>=S/2-28/3`, and selected mass `>=2137/6`. The Boyvalenkov/Musin zero-midpoint exclusion remains independent and valid.

**Next target:** Keep the 21 row discrepancies and F3 six-core variables in a small exact polynomial/KKT model, rather than collapsing them to the scalar P.
