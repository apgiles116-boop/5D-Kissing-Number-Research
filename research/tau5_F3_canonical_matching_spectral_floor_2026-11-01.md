# Type E / F3: sharp canonical-matching midpoint floor from C4 + 2K2

Date: 2026-11-01. **[PROVED EXACTLY — standalone eight-unit-vector theorem].** Type-E application is conditional on the retained F3 graph. **No Type-E exclusion. Global proved range 40 <= tau_5 <= 44.**

## Statement

Let p_0,...,p_3,q_0,...,q_3 be eight unit vectors in any Euclidean space, with indices modulo four. Suppose p_i.p_(i+1)<-1/2 for all four cycle edges, and q_0.q_2<-1/2, q_1.q_3<-1/2 for the two opposite edges. No constraints on the other 22 pairings are needed. Then

    (1/4) sum_i p_i.q_i > -(sqrt(6)+sqrt(2))/4 = -cos(pi/12).

For m_i=(p_i+q_i)/2, the canonical matching midpoint energy satisfies

    C_can=sum_i ||m_i||^2
         =2+(1/2)sum_i p_i.q_i
         > 2-(sqrt(6)+sqrt(2))/2
         =0.0681483474218634265... >681/10000.

This improves the earlier unconditional all-singleton C-N>1/96 consequence C>1/96 and even the separately conditional C>33/500 benchmark, **for this canonical matching only**.

## F3 incidence

Use E(F3)={02,04,05,14,17,23,27,36,56,57}. Set

    p=(0,2,7,5), q=(4,3,1,6).

The canonical matching is 04|23|17|56. The six other F3 edges are the p-cycle 02,27,75,50 and q-opposites 41,36. They are all deep in Type E.

## Proof: D4 averaging and Fourier PSD

Average the eight-by-eight Gram matrix over simultaneous dihedral permutations of the four indices. This preserves PSD, unit diagonals, the six strict deep constraints, and the objective sum_i p_i.q_i. The averaged Gram has symmetric circulant blocks P,Q,R, with first rows

    P=(1,x,y,x), Q=(1,u,v,u), R=(s,t,r,t),

where x<-1/2, v<-1/2 and s=(1/4)sum_i p_i.q_i. Fourier diagonalization yields three two-by-two PSD blocks (frequency 1 has multiplicity two):

    P0=1+2x+y, Q0=1+2u+v, R0=s+2t+r;
    P1=1-y,    Q1=1-v,    R1=s-r;
    P2=1-2x+y, Q2=1-2u+v, R2=s-2t+r.

Thus Pk,Qk>=0, |Rk|<=sqrt(Pk Qk), and

    -4s <= F=sqrt(P0 Q0)+2sqrt(P1 Q1)+sqrt(P2 Q2).

Take alpha0=1, alpha1=sqrt(3/2), alpha2=1/sqrt(2). Weighted AM-GM gives the exact affine upper envelope

    F<=L=(1/2)[P0+Q0
      +2(alpha1 P1+Q1/alpha1)
      +(alpha2 P2+Q2/alpha2)].

Its derivatives in (x,y,u,v) have signs (+,-,-,+), explicitly

    L_x=1-sqrt(2)/2>0;
    L_y=1/2-sqrt(6)/2+sqrt(2)/4<0;
    L_u=1-sqrt(2)<0;
    L_v=1/2-sqrt(6)/3+sqrt(2)/2>0.

P0>=0 and x<-1/2 force y>0; Q0>=0 and v<-1/2 force u>-1/4. Consequently

    F<=L<L(-1/2,0,-1/4,-1/2)=sqrt(6)+sqrt(2),

so 4s>-(sqrt(6)+sqrt(2)). This proves the strict bound analytically, without SDP or numerical optimization.

## Sharpness and a strict-contact family

For the weak constraints <=-1/2, choose

    x=-1/2, y=0, u=-1/4, v=-1/2,
    s=-(sqrt(6)+sqrt(2))/4,
    t=sqrt(2)/4, r=(sqrt(6)-sqrt(2))/4.

The Fourier blocks have (P0,Q0,R0)=(0,0,0), (P1,Q1,R1)=(1,3/2,-sqrt(3/2)), and (P2,Q2,R2)=(2,1,-sqrt(2)). Each is PSD of rank at most one; hence the full Gram is PSD of rank three. All F3 nonedges are safe and the four matching contacts are deep.

For epsilon>0 small, set x=-1/2-epsilon, y=2epsilon, v=-1/2-epsilon, u=-1/4+epsilon/2. Then P0=Q0=0, P1=1-2epsilon, Q1=3/2+epsilon, P2=2+4epsilon, Q2=1-2epsilon. Choose R0=0 and Rk=-sqrt(Pk Qk) for k=1,2; invert the Fourier transform for s,t,r. The Gram remains PSD of rank three, and by continuity all ten F3 edges are strictly deep and all 18 nonedges remain safe for sufficiently small positive epsilon. The constant is therefore the sharp **infimum** even with strict contacts.

## Proof ledger

**[PROVED EXACTLY]** The canonical F3 matching 04|23|17|56 has midpoint energy >0.0681, independent of D5 labeling, rank-five reconstruction, core coplanarity, and the other sixteen Type-E edges. This is a stronger standalone signed-incidence obstruction than the earlier all-singleton C>1/96.

**[OPEN]** The F3 mass theorem may select either of the other two matchings, each with a double-contact pattern. No transfer of this canonical matching floor to the mass-selected matching is established. A matching-transfer inequality or an F3-incidence-sensitive upper certificate remains needed. Type E, Types C and D, generic e>=27, and non-isolated branches remain open. Sparse e=23/e=24 classification still requires delta(G)>=1. Preserve star<=70/3, broom M(F3)<=89, matching M(P)>=S/2-28/3, A<=383/504, and Musin/Boyvalenkov's 21-line boundary exclusion.

Companion exact SymPy verifier checks graph incidence, derivative signs, radical floor, PSD Fourier witness, and the strict-contact family. **Global proved range unchanged: 40<=tau_5<=44.**
