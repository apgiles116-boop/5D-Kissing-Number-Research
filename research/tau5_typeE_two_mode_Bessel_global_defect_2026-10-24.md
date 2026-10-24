# Type E: two-mode Bessel geometry improves the global six-defect ceiling

2026-10-24. **[PROVED EXACTLY]** Universal energy-transfer and Schur/Bessel lemmas. **[PROVED UNDER RETAINED TYPE-E INPUTS]** Q<40949/500000. **[OPEN]** Type-E elimination, global D5 labeling, and tau_5.

## Setup
For selected deep edges x_i^±=m_i±z_i, a_i=||m_i||²≤1/4, m_i·z_i=0, ||z_i||²=1-a_i, and m_i·m_j+|z_i·z_j|≤1/2. Put δ_ij=(|z_i·z_j|-1/2)_+. The six Type-E core defects obey D=Σδ≤D0=1780062775/4032758016 and C=Σ_core a_i≤A≤B=383/504. Retain the exact lifted-triangle adjacent inequality p+q+4(p²+q²-pq)≤1/2 and global frame floor L=8790283/317520.

## New universal four-edge theorem
Suppose α=δ12>0, β=δ34>0, γ=δ13>0, and t=Σ_{i=1}^4 a_i-2(α+β)≥0. Define rα=√(αt+t²/4), rβ=√(βt+t²/4), N=1-α+rα, P=1-β+rβ, c=1/2+α, x=1/2+γ, Y=1/2-γ+rβ.

**[PROVED EXACTLY]** When N>c, endpoint feasibility implies

P ≥ x²/N + N/(N²-c²) * max(0,cx/N-Y)².

If Y≤cx/N, equivalently,

(1+rβ)²/(3+2rα) + (2γ-rβ)²/(1-4α+2rα) ≤ 1-β+rβ. (B)

Proof: Let t12=a1+a2-2α, t34=a3+a4-2β. Then ||m1+m2||²≤t12, a3a4≥β², and
||m1+m2||² a3≤(t-a3-a4+2β)a3≤t a3-(a3-β)²≤βt+t²/4.
Orient z2,z3 so z1·z2=c and z1·z3=x. With y=z2·z3, the endpoint inequality yields y≤1/2-γ+rβ=Y. From a1a2≥α², a1+a2≤2α+t, and analogously for 34, we get a1,a2≥α-rα and a3≥β-rβ. Inflating the diagonal of the PSD Gram(z1,z2,z3) gives PSD [[N,c,x],[c,N,y],[x,y,P]]. Its Schur complement is P≥x²/N+N/(N²-c²)(y-cx/N)². Minimize over y≤Y. At t=0, (B) recovers 4γ²≤(1-4α)(2/3-β).

## Exact robust exclusion box
Let α0=244473/1000000, β0=8535701/63000000, γ0=D0-B/2, h=1/10000. **[PROVED EXACTLY]** There is no endpoint-feasible configuration with |α-α0|,|β-β0|,|γ-γ0|≤h and 0≤t≤1/50000. Indeed rα<23/10000, rβ<17/10000; exact rational checks ensure Y<cx/N and lower-bound the left side of (B) above its right side by
2603293159010046381219438287/404239298123534816332656000000>0.

## Global six-defect theorem
**[PROVED UNDER RETAINED TYPE-E INPUTS]**
Σ_{six core pairs} δ_ij² < q0=40949/500000=0.081898.
This improves the previous exact 0.0819 ceiling by 1/500000.

Proof outline, with every rational comparison in the accompanying verifier. Put b=B/2, r=D0-b, T=122237/500000, e=1/100000. Let p be the largest defect, y its unique disjoint partner, z the largest adjacent defect, hp=b-p. Every two defects sum to at most b. Each defect adjacent to p is ≤c(p), the nonnegative root of p+c+4(p²+c²-pc)=1/2.

(1) For p≤D0/3, Q≤D0²/3; for D0/3≤p≤b/2, Q≤max(D0²/3,b²/2+r²); for b/2≤p≤T, Q≤F(p)=p²+(b-p)²+r². These exclude Q≥q0 when p≤T-e. For p≥T, Q≤max(G0(p),G1(p)) with G0=p²+c(p)(D0-p)<3/40 and G1=p²+(b-p)²+r c(p), strictly decreasing because c'(p)≤-4 and 1+B-4D0<0. The exact bound c(T+e)<61385/1000000 gives G1(T+e)<q0. Thus Q≥q0 forces T-e<p<T+e.

(2) It also forces hp-e<y≤hp. For p≤T, use c(p)<6149/100000 and Σ_adj δ²≤min(S²,cmax*S), S=D0-p-y. If y≤hp-e, the convex expressions have only three relevant endpoints y=0, y=D0-p-cmax, y=hp-e; all yield <q0 by rational comparison. For p≥T, convexity bounds Q at y=0 by G0 and at y=hp-e by G1(p)-e(2hp-c(p))+e²<q0, using c(T)<61437/1000000.

(3) The adjacent total is <r+e. If z≤r-h, then Q≤(T+e)²+(b-T-e)²+(r-h)(r+e)<q0. Hence r-h<z<r+e.

(4) Since T-α0=10^-6 and β0=b-α0, (1)-(3) imply |p-α0|,|y-β0|,|z-γ0|<h. Also 0≤t=Σ_core a_i-2(p+y)≤B-2(p+y)=2(hp-y)<2e=1/50000. Relabel the adjacent pair z as 13. This falls in the excluded robust box: contradiction.

## Consequence and status
**[CONDITIONAL TYPE E]** The 184 projectively safe pairs satisfy
Σ_safe(z_i·z_j)² > L-3/2-D0-q0
=1616939870490713/63011844000000≈25.6608879830705.

**[OPEN]** No Type-E contradiction or safe-pair upper bound follows. Types C,D, generic e≥27 and non-isolated branches remain open. Global proved range stays 40≤τ5≤44. Retain M(F3)≤89, M(P)≥S/2-28/3, A≤383/504, and the audited zero-midpoint 21-line exclusion. Sparse e=23,24 graph classification remains conditional on δ(G)≥1.

The companion pure-Python Fraction checker certifies all rational comparisons; the analytic PSD and convexity arguments are stated above.