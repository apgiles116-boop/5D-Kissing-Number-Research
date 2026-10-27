# Type E: rank-five endpoint lift of the core defect envelope and near-antipodal stability

Date: 2026-10-27.

**[PROVED EXACTLY — finite four-edge geometry]** A parametric family of four selected deep edges in R^5 attains the relaxed core spectral defect ceiling, satisfies every cross-endpoint kissing inequality, and admits a strictly safe isolated center. The joint midpoint/projected Gram matrix has rank five.

**[PROVED EXACTLY — universal endpoint lemma]** A raw core defect near its individual cap 1/4 forces two nearly antipodal cross-endpoint pairs, with explicit square-root error.

**[OPEN]** This is not a realization of Type E: the other sixteen selected deep edges, the prescribed F3 deep graph, 184 safe pairings, and global mass constraints are NOT imposed. The constructed configuration has only two strictly active raw core defects, not six. No Type-E exclusion or improvement of 40 <= tau_5 <= 44 is claimed.

## 1. Exact rank-five lift

Let e1,...,e5 be orthonormal. For any rational or real 0<b<1/4 define

m1=e1/2,  m2=-e1/2,  m3=sqrt(b)e2,  m4=-sqrt(b)e2,

z1=z2=(sqrt(3)/2)e3,

z3=(1/sqrt(3))e3+sqrt(5/12)e4+sqrt(1/4-b)e5,

z4=(1/sqrt(3))e3+sqrt(5/12)e4-sqrt(1/4-b)e5.

Every m_i.z_i=0, and ||m_i||^2+||z_i||^2=1. The eight endpoints v_i^+/-=m_i +/- z_i are unit vectors, and each selected pair is deep: v_i^+.v_i^-=2||m_i||^2-1 <= -1/2.

The midpoint and projected Gram matrices are

G_m = [[1/4,-1/4,0,0],[-1/4,1/4,0,0],[0,0,b,-b],[0,0,-b,b]],

G_z = [[3/4,3/4,1/2,1/2],[3/4,3/4,1/2,1/2],
       [1/2,1/2,1-b,1/2+b],[1/2,1/2,1/2+b,1-b]].

All mixed Gram entries m_i.z_j vanish. For distinct selected edges i,j, the maximum of the four cross-endpoint inner products equals m_i.m_j+|z_i.z_j|=1/2: the pair 12 gives -1/4+3/4, pair 34 gives -b+(1/2+b), and the four cross-block pairs give 0+1/2. Thus all eight endpoints satisfy the spherical-code kissing inequality <=1/2.

The additional unit center x=(e1+e2)/sqrt(2) obeys |x.v_i^+/-| in {1/(2sqrt(2)),sqrt(b/2)} <1/2. Thus it is strictly isolated relative to these eight endpoints.

For 0<b<1/4, the m_i span <e1,e2> and the z_i span <e3,e4,e5>. Hence the joint 8-by-8 Gram matrix has rank exactly five. Adding x does not change the rank.

**Graph caveat (exact):** At the deep threshold inner product <= -1/2, the eight constructed endpoints have all 16 deep contacts between the four plus endpoints and the four minus endpoints, and none within either sign class. Their induced deep graph is K4,4, whereas the retained F3 core has exactly ten deep edges. This explicit construction therefore violates the prescribed Type-E core adjacency, even though it satisfies every kissing inequality and the isolated-center row.

The raw positive correlation excesses d_ij=(|z_i.z_j|-1/2)_+ are

d12=1/4, d34=b, and d13=d14=d23=d24=0.

Consequently A_C=sum_i||m_i||^2=1/2+2b, and sum_{i<j} d_ij=1/4+b=A_C/2: the four-core spectral ceiling is attained with a genuine rank-five endpoint configuration and a strictly safe center. The core quartic positive defect equals f(1/4)+f(b), f(d)=(1/2+d)^2 d(1+d).

At b=131/1008, A_C=383/504 and

sum d_ij=383/1008,
sum f(d_ij)=241638909745/1032386052096.

This is the same numerical value as the earlier *relaxed* six-active supremum, but the present exact endpoint realization has **two** active pairs. It does not show that the six-strictly-active rank-five branch approaches this value.

## 2. Quantitative near-antipodal stability for a single exceptional pair

**[PROVED EXACTLY — conditional only on four endpoint upper kissing inequalities and a_i<=1/4]**

For any two selected deep edges v_i^+/-=m_i +/- z_i, set a_i=||m_i||^2<=1/4, r_i=1-a_i, and d=(|z_i.z_j|-1/2)_+>0. Write s=sign(z_i.z_j), epsilon=1/4-d. Then 0<=epsilon<1/4 and

||m_i+m_j||^2 <= 2 epsilon,
||z_i-s z_j||^2 <= 4 epsilon,
|m_i.z_j+s z_i.m_j| <= epsilon.

Proof: among the four endpoint inequalities, those with sign product s imply

m_i.m_j+|z_i.z_j|+|m_i.z_j+s z_i.m_j|<=1/2.

Hence B=m_i.m_j<=-d and |mix|<=-B-d<=1/4-d=epsilon, since -B<=sqrt(a_i a_j)<=1/4. Since -B<=sqrt(a_i a_j)<=(a_i+a_j)/2 and -B>=d, we have a_i+a_j>=2d. Therefore

||m_i+m_j||^2=a_i+a_j+2B <=1/2-2d=2epsilon,

||z_i-s z_j||^2=(2-a_i-a_j)-2(1/2+d)
 =1-(a_i+a_j)-2d<=1-4d=4epsilon.

For either sigma=+/-1, the two cross-endpoints p=v_i^sigma and q=v_j^(-sigma*s) satisfy

||p+q|| <= (sqrt(2)+2)*sqrt(epsilon).

At epsilon=0 the endpoints form two exact antipodal cross-pairs. Moreover any other unit code vector w with w.p<=1/2 and w.q<=1/2 satisfies

-1/2-(sqrt(2)+2)*sqrt(epsilon) <= w.p <=1/2.

This supplies a two-sided, quantitative near-antipodal constraint for the remaining endpoints.

The family in Section 1 attains epsilon=0 for pair 12 and equality in the projected-difference bound for pair 34.

## 3. Interpretation and proof ledger

This result shows that merely adding rank<=5, m_i.z_i=0, the four-core endpoint kissing inequalities, and a strictly compatible center does NOT lower the two-active core spectral envelope. A stronger obstruction must use the *actual F3 adjacency*, the sixteen outside edges and their 184 safe pairings, or a branch-specific strict-six-active argument.

The near-antipodal stability lemma gives a useful exact case split for a finite polynomial/KKT proof: either every exceptional defect is separated from 1/4, or an almost-antipodal pair enforces near-two-sided constraints on all other code endpoints. No uniform positive separation has yet been established for actual Type E.

**[RETAINED, NOT REPROVED]** Global 40<=tau_5<=44; Type-E 1/49<A<=383/504; M(F3)<=89; M(P)>=S/2-28/3; twenty-edge mass >=2137/6; Musin/Boyvalenkov zero-midpoint exclusion; 184 safe plus six potentially exceptional core pairs; exact fixed-versus-weighted harmonic correction. Types C, D, E, generic e>=27, and non-isolated branches remain open. Sparse e=23/24 classification remains conditional on delta(G)>=1.
