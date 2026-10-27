# Exact saturated 17-line D5 subframe and a conditional Type-E core-energy gap (2026-10-27)

**Proof status:** [PROVED EXACTLY — finite geometry]. The explicit 17-line set below is a projective spherical code of coherence at most 1/2, but cannot be extended to 18 lines at that coherence. [PROVED EXACTLY — CONDITIONAL TYPE E] Its covering constant forces positive four-core midpoint energy if it occurs as the isolated center plus 16 outside-core normalized directions. [OPEN] No theorem puts arbitrary Type E into this template. No improvement to the global 40 <= tau_5 <= 44 range or label-free Type-E A>1/49.

## Construction

Let e_1,...,e_5 be the standard basis. Define D_16 to contain (e_j+e_k)/sqrt(2) and (e_j-e_k)/sqrt(2) for 2<=j<k<=5 (12 lines), together with (e_1+e_j)/sqrt(2) for 2<=j<=5 (4 lines). Set x=(8,-3,-3,-3,-3)/10, a unit vector. The D_16 lines are a subset of the 20 D5 projective roots, so have coherence <=1/2. Their squared inner products with x belong to {0,1/8,9/50}, hence V=D_16 union {x} is a valid 17-line code. In particular, the isolated center is compatible with all sixteen outside-core D5 directions at zero outside-core midpoint energy: any D5 mismatch can be concentrated in the four omitted lines.

## Exact covering certificate

For any unit y let q=max_{v in V}|y·v|>0. Set w=y/(sqrt(2)q), t=w_1, v_j=w_j (j=2,...,5), S=sum_{j=2}^5 v_j. The twelve D4 roots give |v_j+v_k|<=1 and |v_j-v_k|<=1, so |v_j|+|v_k|<=1. These imply sum_{j=2}^5 v_j^2<=1: for sorted absolute values h_1>=...>=h_4, if h_1<=1/2 this is immediate; otherwise h_2<=1-h_1, and the sum is at most h_1^2+3(1-h_1)^2<=1 for h_1 in [1/2,1].

The four roots (e_1+e_j)/sqrt(2) imply |t+v_j|<=1, hence -4(1+t)<=S<=4(1-t). The center constraint is |8t-3S|<=5sqrt(2). Combining gives -c<=t<=c with c=(12+5sqrt(2))/20=3/5+sqrt(2)/4<1. Thus
1/(2q^2)=||w||^2<=1+c^2,
and therefore

**q >= rho_0 = 10/sqrt(297+60sqrt(2)) > 1/2.**

This strict universal covering bound proves the 17-line set is saturated. It is not claimed sharp.

## Conditional Type-E core gap

Suppose the isolated center and sixteen outside-core *normalized* directions are this 17-line set up to one common orthogonal transformation, with outside-core midpoint energies a_j<=b<1. For any one of the four core edges write a_i=||m_i||^2 and u_i=z_i/sqrt(1-a_i). Center-to-core and outside-to-core endpoint safety imply
max_{v in V}|u_i·v| <= 1/[2sqrt((1-a_i)(1-b))].
By the covering theorem,
a_i >= [1-kappa/(1-b)]_+,  kappa=1/(4rho_0^2)=297/400+3sqrt(2)/20.
Consequently the four-core midpoint energy C obeys
**C >= 4[1-kappa/(1-b)]_+.**
For b=0,
**C >= 103/100 - 3sqrt(2)/5 = 0.181471862576...**

This is a conditional template calculation, not a new global Type-E lower bound. The general strategy is to certify a covering constant for the actual center-plus-16 outside directions and combine it with their midpoint energies. The six exceptional core pairings are not identified with D5 Q-kernel directions.

Retain M(F3)<=89, M(P)>=S/2-28/3, twenty-edge mass>=2137/6, A<=383/504, and label-free A>1/49. Types C,D, generic e>=27, non-isolated branches remain open. Sparse e=23/e=24 classification assumes delta(G)>=1.