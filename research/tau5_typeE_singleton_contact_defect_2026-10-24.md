# Type E: singleton-contact cap and improved six-core square budget (2026-10-24)

**[PROVED EXACTLY]** Universal singleton-cross-contact lemma, F3 matching enumeration, rational six-defect optimization. **[CONDITIONAL ON RETAINED TYPE-E INPUTS]** Q<79/1000 and safe squared-correlation floor. **[OPEN]** Type E elimination. Global status 40<=tau_5<=44.

## Hypotheses

For twenty disjoint deep edges, write unit endpoints x_i^±=m_i±z_i, m_i.z_i=0, a_i=||m_i||²<=1/4, A=sum a_i<=B=383/504. Deep graph edges correspond to cross endpoint dot products <-1/2; kissing imposes all endpoint dots <=1/2. Let δ_ij=(|z_i.z_j|-1/2)_+. Only six pairs within the four selected F3 matching edges can have positive δ. Retain D=sum δ<=D0=1780062775/4032758016. For any adjacent pair defects p,q, retain the exact lifted-triangle inequality P(p,q):=p+q+4(p²+q²-pq)-1/2<=0. For disjoint pair defects p+q<=B/2=b=383/1008. Thus every two core defects sum to at most b (the adjacent bound (sqrt(3)-1)/2 is smaller).

## Singleton-contact lemma [PROVED EXACTLY]

If two selected deep edges have exactly one cross deep endpoint pair among their four cross endpoint pairs, then δ_ij<=α=(sqrt(2)-1)/2.

Proof: If δ>0, switch z_j so r=z_i.z_j=1/2+δ. Write c=m_i.m_j, p=z_i.m_j, q=m_i.z_j. Averaging the st=+1 endpoint kissing inequalities gives c+r+|p+q|<=1/2, hence c<=-δ and |p+q|<=-c-δ. Since c>=-sqrt(a_i a_j)>=-1/4, both st=+1 cross endpoint dots are >=2c+1/2+2δ>=2δ>=0, hence cannot be deep. Among the st=-1 dots c-r±(p-q), exactly one is deep and the other nondeep, so |p-q|>=r-c-1/2=δ-c>=2δ. In R^5⊕R^5 set X=(m_i+m_j,z_i-z_j), Y=(-z_j,m_j). Then X.Y=p-q, ||Y||²=1, ||X||²=2+2c-2r=1+2c-2δ<=1-4δ. Cauchy gives 4δ²<=1-4δ, hence δ<=α. QED.

A quotient pairing with zero cross deep contacts has δ=0, because δ>0 forces c-r<=-1/2-2δ and thus at least one st=-1 deep cross contact.

## Exact F3 enumeration [PROVED EXACTLY]

E(F3)={02,04,05,14,17,23,27,36,56,57}. The three perfect matchings, obtained by testing all 210 four-edge subsets, have these quotient contact multiplicities among six unordered pairs of matched edges:

* P1=02|14|36|57: (0,1,1,1,1,2); the zero and double are disjoint quotient pairs.
* P2=04|17|23|56: (1,1,1,1,1,1).
* P3=05|14|27|36: (0,1,1,1,1,2); again zero and double are disjoint.

Thus either all six defects are <=α, or one possibly larger double-contact defect x<=1/4 has its disjoint partner zero and four adjacent defects <=α.

## Exact Q bound [PROVED UNDER TYPE-E INPUTS]

**Q=sum_(six core) δ² < 79/1000.** This improves the previously proved Q<40949/500000=0.081898; the later Q<0.096 estimate was weaker and must not replace that earlier benchmark.

If all δ<=α, put t=max δ. Capped-simplex concentration using every pair sum<=b gives:
* t<=D0/3: Q<=D0²/3.
* D0/3<=t<=b/2: Q<=2t²+(D0-2t)².
* b/2<=t<=α: Q<=t²+(b-t)²+(D0-b)².
The latter two are convex, so endpoints suffice. Exact comparisons show D0²/3, b²/2+(D0-b)², and α²+(b-α)²+(D0-b)² are all <79/1000.

Otherwise the double-contact defect x>α has zero opposite defect. Each adjacent y obeys P(x,y)<=0 and thus y<=c(x), the nonnegative root of P(x,c)=0. Hence Q<=F(x):=x²+(D0-x)c(x). We show F decreases on [α,1/4]. Implicit differentiation gives c'=-(1+8x-4c)/(1+8c-4x). The sign numerator of F' simplifies, using P=0, to N=8x²+5x-1-D0(1+8x)+c(4D0+8x+1). Since D0>2/5, N<N at D0=2/5, which is negative if c<R(x):=(7-40x²-9x)/(13+40x). For x∈[1/5,1/4], R>0, P increases in c>=0, and

P(x,R)=3(12800x⁴+7040x³-1688x²-704x+135)/(2(40x+13)²)>0.

The quartic is positive because after x=1/5+t/20 (0<=t<=1), its degree-four Bernstein coefficients are exactly 87/25, 48/25, 809/300, 127/20, 27/2, all positive. Thus c<R, N<0, F'<0. Consequently Q<=F(α)<79/1000. The last strict rational comparison follows from 2071067/10^7<α<207107/10^6, c(α)<154025/10^6, D0<441401/10^6, giving F(α)<0.0789804890065<0.079. The c(α) bound is certified by P(2071067/10^7,154025/10^6)>0.

## Improved safe-mass floor [PROVED UNDER TYPE-E INPUTS]

The retained raw squared-correlation floor is L=8790283/317520, with an additional nonnegative Q-frame variance remainder. The six candidate core pairings contribute at most 3/2+D+Q<3/2+D0+79/1000. Therefore

**sum_(184 raw-safe pairs)(z_i.z_j)² > 12936979830517/504094752000 = 25.6637859830705...**

plus the retained nonnegative frame-variance remainder. This improves the previous 25.6608879830705 by exactly 0.002898. This is a necessary condition, not a contradiction.

**[RETAINED]** M(F3)<=89, M(P)>=S/2-28/3, selected mass >=2137/6, A<=383/504, 40<=tau_5<=44. Sparse e=23/24 classification conditional on δ(G)>=1.

**[OPEN]** Type E, C, D, generic e>=27, non-isolated 41-code branches; no global D5 labeling and no six-exception/Q-kernel identification.

Companion exact verifier: tau5_typeE_singleton_contact_defect_2026-10-24_verify.py.


---

## Addendum: stronger exact Q < 77/1000 certificate (supersedes 79/1000)

**[PROVED EXACTLY, under the same retained Type-E inputs]**

The preceding Q<79/1000 is valid but not optimal. Capped-simplex concentration across the **four** singleton-contact defects adjacent to a possible double-contact defect sharpens it to

**Q=sum_(six core) delta_ij² < 77/1000 = 0.077.**

Case A (all six defects <=alpha) is unchanged: the three exact endpoint bounds in the preceding proof are all <77/1000, not merely <79/1000.

In Case B, the double-contact defect x>alpha has opposite defect zero. The four remaining defects y_j satisfy P(x,y_j)<=0, so y_j<=c(x), where c(x) is the nonnegative root of P(x,c)=0, and sum y_j<=D0-x. Partition [alpha,1/4] into thirteen rational intervals [l,h] (starting at l=207/1000<alpha). On each interval, use the rational cap C listed below. Each satisfies P(l,C)>0, and P increases in x and in nonnegative c throughout the region. Hence y_j<C for x in [l,h].

Let R=D0-l, k=min(4,floor(R/C)). The exact capped-simplex maximum for the four squares is Phi(C,R)=k*C²+(R-k*C)² when k<4 and Phi=4*C² when k=4. Thus Q<h²+Phi(C,D0-l). The following C numerators have denominator 10^6:

| Interval [l,h] | C numerator |
|---|---:|
| 207/1000, 631/3000 | 154180 |
| 631/3000, 641/3000 | 149194 |
| 641/3000, 217/1000 | 143883 |
| 217/1000, 661/3000 | 138204 |
| 661/3000, 671/3000 | 132102 |
| 671/3000, 227/1000 | 125506 |
| 227/1000, 691/3000 | 118321 |
| 691/3000, 701/3000 | 110417 |
| 701/3000, 237/1000 | 101606 |
| 237/1000, 721/3000 | 91599 |
| 721/3000, 731/3000 | 79902 |
| 731/3000, 247/1000 | 65535 |
| 247/1000, 1/4 | 45863 |

All 13 exact rational inequalities h²+Phi(C,D0-l)<77/1000 pass. The largest rational upper bound is 305420404476709867702417033/3970492484280336000000000000 = 0.07692254945... . No numerical optimizer is used; the companion `tau5_typeE_F3_singleton_77_1000_2026-10-24_verify.py` uses only Python Fraction arithmetic.

**Updated strongest safe-mass floor:**

S_184-safe > L-3/2-D0-77/1000
= 12937988020021/504094752000
= 25.6657859830705...,

with the previously retained nonnegative raw Q-frame variance and concentration remainders. This improves the previously best Q<40949/500000=0.081898 and its safe-mass floor by **exactly 0.004898**.

**[OPEN]** No Type-E elimination follows; global 40<=tau_5<=44 and all retained F3 mass and midpoint bounds remain unchanged.
