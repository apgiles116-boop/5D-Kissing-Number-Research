# Type E: isolated-center forcing of projected Q-frame anisotropy

Date: 2026-11-01. **[PROVED EXACTLY — conditional on retained Type-E harmonic and F3 broom/matching certificates]**. No Type-E exclusion; global proved range remains **40 <= tau_5 <= 44**.

## Theorem

Let u be the isolated center of a hypothetical 41-code, and let the 20 disjoint selected deep edges have endpoints m_i +/- z_i (16 isolated plus four F3 matching edges). Put a_i=||m_i||^2, A=sum a_i, S_z=sum z_i z_i^T, S_m=sum m_i m_i^T, and

    V_z=||S_z-(20-A)I_5/5||_F^2=||sum_i Q_i||_F^2.

Retain B=2595/256, c=1245/256, D(t)=196t-644t^2+896t^3-448t^4, r=D^{-1}(c), s1=D^{-1}(41/6), Astar=1/2+r+s1, and Xi=N+(35/6)||T||_F^2+14K4-B>=0, with D_I+Xi<=c and D_C+(D_I+Xi)/2<=169/3-B/2.

**[PROVED EXACTLY — conditional Type E]**

    V_z >= (5/4)*(7/10-s1/5-4/sqrt(175))^2
        > 949/5000 = 0.1898.                                (1)

In particular, the 20 projected vectors cannot form a tight frame. This is label-free and does not require core coplanarity, D5 labeling, Q-rank assumptions, or identifying six exceptional pairings with the six D5 Q-kernel relations.

More precisely, with h(Xi)=sqrt(1/100+64 Xi/875), one has the **coupled second-order inequality**

    V_z >= (5/4)*(4/5-A/5-h(Xi)/2)^2,                    (2)

whose parenthesis is positive. There is an additional nonnegative term u^T S_m u inside the exact square.

## Proof: isolated-center direction

Let T=sum_{v in X}vv^T-(41/5)I_5, q=u^T T u, and E=(35/6)||T||_F^2+14K4. Because the other 40 endpoints form the selected 20 pairs,

    T=uu^T+2S_z+2S_m-(41/5)I_5,
    u^T S_z u=18/5+q/2-u^T S_m u.                     (3)

For B_z=S_z-(20-A)I_5/5,

    -u^T B_z u=2/5-A/5-q/2+u^T S_m u.                (4)

Trace-free Cauchy gives ||B_z||_F^2 >= (5/4)(u^T B_z u)^2.

The retained isolated-center harmonic inequality is E>=10+(875/64)(q+4/5)^2 for q>=-12/7; for q<-12/7, E>150/7. Since Xi=N+E-B, D_I+Xi<=c and N>=0, we have E<=B+Xi<=15. Thus the second case is impossible and

    |q+4/5|<=sqrt((64/875)*(Xi+35/256))
           =sqrt(1/100+64 Xi/875)=h(Xi).              (5)

Equations (4)-(5) prove (2), once positivity is checked below.

## Proof: mass-slack coupling

The retained scalar constraints imply

    A+(r/c)*Xi<=Astar.                                  (6)

Here is an independent derivation from those constraints. Write x=sum_I a_i and y=sum_C a_i. Concavity gives D_I>=D(x), so x<=r_Xi=D^{-1}(c-Xi). The core inequality gives y<=1/2+D^{-1}(K-(D(x)+Xi)/2), K=43/3-B/2. For fixed Xi, the upper bound on x+y is convex in x, since D is concave and D^{-1} is increasing and convex, so its maximum occurs at x=0 or x=r_Xi. At x=r_Xi, it is 1/2+r_Xi+s1. At x=0, the inverse argument is D(s1)+(c-Xi)/2. Because s1<0.04, r_Xi<=r<0.028, D'(t)>120 for t<=0.068, and D(r_Xi)<=196r_Xi, the latter endpoint is no larger. Finally convexity of D^{-1} and D^{-1}(0)=0 give r_Xi<=r(1-Xi/c), proving (6). The low-core-mass case y<=1/2 is also covered.

Combining (2) and (6),

    V_z >= (5/4)*f(Xi)^2,
    f(Xi)=4/5-Astar/5+(r/(5c))*Xi-h(Xi)/2.

On 0<=Xi<=c, r<0.028, c>4, h(Xi)<=8/sqrt(175)<0.61, and

    f'(Xi)=r/(5c)-16/(875*h(Xi))<0.

Thus f(Xi)>=f(c)=7/10-s1/5-4/sqrt(175)>0. Exact rational brackets s1<39782/1000000 and 8/sqrt(175)<604744/1000000 yield

    f(c)>974179/2500000,
    V_z>(5/4)*(974179/2500000)^2
       =949024724041/5000000000000 >949/5000.

The last positive margin is 24724041/5000000000000. The exact polynomial and radical comparisons are checked by the companion Fraction verifier.

A further spectral consequence of (3)-(5) is u^T S_z u<3.502372, hence lambda_min(S_z)<3503/1000. Since tr S_z=20-A and A<0.567, lambda_max(S_z)>3.9825.

## Six-exception transfer

Retain the earlier exact Q-frame stability

    C_z=sum_{i<j}(z_i.z_j)^2 >= Lstar+(delta_I+delta_C+V_z)/2,
    Lstar>282677/10000.

Therefore **C_z>283626/10000=28.3626**. The six exceptional core pairings have raw positive defect D_raw<441401/1000000 and total squared correlation at most 3/2+D_raw+D_raw^2. The 184 safe pairings consequently satisfy

    sum_safe (z_i.z_j)^2
      > 26226364157199/1000000000000
      = 26.226364157199.

At most 41 safe pairings with |z_i.z_j|>1/3 would yield a squared mass at most 41/4+143/9=941/36, less than this floor. Thus **at least 42 of the 184 safe pairings have |z_i.z_j|>1/3**. Stronger separately conditional F3 branchwise caps are not superseded.

## Proof-status ledger

- **[PROVED EXACTLY, CONDITIONAL ON RETAINED TYPE-E INPUTS]** Center-to-Q-frame identity, coupled inequality (2), non-tightness (1), spectral consequences.
- **[PROVED EXACTLY, WITH ADDITIONAL RETAINED Q-STABILITY AND SIX-CORE DEFECT INPUTS]** Squared-correlation floor and 42-safe-pair count.
- **[VERIFIED EXACT ARITHMETIC]** Companion Python Fraction script checks root brackets, radical bounds, monotonicity margins, squared-mass floors, and count.
- **[OPEN]** Type E is not eliminated. Missing: signed F3-incidence-sensitive upper bound contradicting the lower frame/safe-correlation energy. Types C,D, generic e>=27 and non-isolated branches remain open; e=23/24 classification still requires delta(G)>=1. Preserve M(F3)<=89, M(P)>=S/2-28/3 and the Musin/Boyvalenkov zero-midpoint theorem. Global proved range **40<=tau_5<=44**.
