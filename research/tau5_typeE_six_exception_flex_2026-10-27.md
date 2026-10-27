# Type E: exact six-exception flex after deleting a K4 from D5

Date: 2026-10-27.

**[PROVED EXACTLY — finite projective geometry]** There is an explicit one-parameter deformation of the 20 D5 root lines with precisely six projective threshold violations (a K4 on four distinguished lines), while all other 184 pairings remain safe. At a rational parameter both positive-defect budgets are respected. **[PROVED EXACTLY — conditional local center obstruction]** Small deformations in this family cannot admit an isolated center with individual midpoint energy <=1/4. **[OPEN]** This is NOT a Type-E configuration and does not eliminate Type E.

## Exact construction

Use the standard basis e_1,...,e_5 of R^5. Distinguish the four core D5 lines

    r_j=(e_1-e_j)/sqrt(2),  j=2,3,4,5,

and keep the other 16 D5 root lines fixed. Put

    w_j=(e_1+e_j - sum_{k=2..5, k!=j} e_k)/sqrt(2),
    u_j(t)=(r_j+t*w_j)/sqrt(1+(5/2)t^2).

Here r_j.w_j=0 and ||w_j||^2=5/2.

For each core/outside pair, use unnormalized R_j=e_1-e_j, W_j=e_1+e_j-sum_{k!=j,k>=2}e_k, and an outside integer root s=e_a +/- e_b. The 64 ordered core/outside pairs have (p,q)=(R_j.s,W_j.s) in

    {(-1,0),(1,0),(-1,2),(1,-2),(0,-2),(0,0),(0,2)}.

Their squared inner product is (p+t*q)^2/[2(2+5t^2)]. The safe condition reduces to (p+t*q)^2<=1+(5/2)t^2, which is automatic for (±1,0), follows from t(8-3t)>=0 for (±1,∓2), and follows from t^2<=2/3 for (0,±2). The other 120 outside/outside pairings are unchanged D5 contacts or orthogonal pairs.

For distinct core lines,

    u_j(t).u_k(t)=(1+4t+t^2)/(2+5t^2)>1/2

whenever 0<t<8/3. Hence for EVERY 0<t<=sqrt(2/3) there are exactly six violating pairs (the four-core K4) and 184 safe pairs.

At t=0, all six deleted core contact inequalities have derivative +2, while the retained active contacts have derivative <=0. Thus deleting these six inequalities destroys the full-contact D5 infinitesimal rigidity. This is compatible with the full-contact rigidity theorem of Cohn--Jiao--Kumar--Torquato.

## Exact defect comparison

At t=1/20, the six exceptional correlations are 481/805. With w=(481/805)^2=231361/648025,

    P_hom=6*(w-1/4)=832257/1296050 = 0.64214883685...
    P_raw=6*w*(w-1/4)=192551811777/839872801250 = 0.22926306399...

Both are strictly BELOW the retained Type-E necessary upper bounds

    P_hom <= 5792292955405/4129544208384 = 1.40264703878...
    P_raw <= 1780062775/4032758016 = 0.44140083981...

Therefore 20 unit projected vectors, 184 safe pairings, six core exceptions, both positive-defect caps, and the universal frame/Q/harmonic identities are mutually consistent. The example has a_i=0 and does NOT satisfy or assert the isolated-center endpoint conditions or the full Type-E mass certificates. Consequently, the REDUCED twenty-line projective/defect system cannot alone eliminate Type E.

## Exact local center obstruction

The D5 projective covering constant is

    min_{||x||=1} max_{d in D5}|x.d| = sqrt(2/5).

Proof: let a>=b be the largest two absolute coordinates of unit x. Then max|x.d|=(a+b)/sqrt(2), while

    1=sum x_i^2 <= a^2+4b^2 <= (5/4)(a+b)^2.

Equality occurs when all |x_i|=1/sqrt(5).

The deformation has max labeled Euclidean displacement

    delta(t)=sqrt(2-2/sqrt(1+(5/2)t^2)) <= sqrt(5/2)*t.

Thus its covering constant rho(t)>=sqrt(2/5)-sqrt(5/2)*t. At t=1/50, use the exact rational comparisons sqrt(2/5)>63/100, sqrt(5/2)/50<1/25 and 1/sqrt(3)<29/50 to obtain

    rho(1/50)>59/100>29/50>1/sqrt(3).

An isolated center x0 with endpoints m_i +/- z_i and z_i=sqrt(1-a_i)u_i, 0<=a_i<=1/4, would require

    |x0.z_i|+|x0.m_i|<=1/2,
    |x0.u_i|<=1/(2 sqrt(1-a_i))<=1/sqrt(3)

for all 20 lines. Hence the t=1/50 deformation has NO such isolated center. This is conditional on the explicit family, not a label-free Type-E theorem.

## Research consequence and proof ledger

The six exceptional K4 correlations are compatible with small raw/homogeneous positive defects and even with a genuine D5 first-order escape after deleting six contacts. A finite KKT/SOS elimination must retain the isolated-center row, midpoint variables and their mixed endpoint constraints; the twenty-line projective/defect system alone is insufficient.

**[RETAINED]** 40<=tau_5<=44; Type E 1/49<A<=383/504; M(F3)<=89; matching M(P)>=S/2-28/3; twenty-edge mass>=2137/6; raw squared-correlation floor>=8790283/317520; Musin/Boyvalenkov 21-line zero-midpoint exclusion. Types C,D,E, generic e>=27 and non-isolated branches remain open. Sparse e=23,24 classification remains conditional on delta(G)>=1.

Companion exact SymPy verifier: tau5_typeE_six_exception_flex_2026-10-27_verify.py.
