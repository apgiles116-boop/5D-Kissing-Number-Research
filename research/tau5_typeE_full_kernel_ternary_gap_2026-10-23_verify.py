"""Exact integer/rational verifier for full-kernel Type-E D5 spectral gap.
Pure Python 3; no packages, no floating-point optimization.
"""
from fractions import Fraction as F
from itertools import combinations, product

edges=list(combinations(range(5),2))
def intersects(i,j): return bool(set(edges[i]) & set(edges[j]))
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
M=[[21 if i==j else -9 if i//2==j//2 else
    1 if intersects(i//2,j//2) else -4
    for j in range(20)] for i in range(20)]
H=[[16 if i==j else -4 if i//2==j//2 else
    1 if intersects(i//2,j//2) else -4
    for j in range(20)] for i in range(20)]  # H=20*G_D5
M2=mm(M,M);H2=mm(H,H)
assert all(M2[i][j]==30*M[i][j] for i in range(20) for j in range(20))
assert all(sum(M[i])==0 for i in range(20))
assert sum(M[i][i] for i in range(20))==420
assert all(20*M[i][j]==50*H[i][j]-H2[i][j]
           for i in range(20) for j in range(20))
assert sum(H[i][i] for i in range(20))==320
assert sum(H2[i][i] for i in range(20))==7600
print("PASS: D5 rank-14 projector and spectrum (3/2 x4, 1 x10, 0 x6)")

C=[[0 if i==j else 1 if intersects(i,j) else -4
    for j in range(10)] for i in range(10)]
best=-1;count=0;witness=None
for s in product((0,1,2),repeat=10):
    T=[sum(C[i][j]*s[j] for j in range(10)) for i in range(10)]
    mx=[]
    for i,k in enumerate(s):
        if k==0: mx.extend((T[i],T[i]))
        elif k==1: mx.extend((T[i]+21,T[i]-9))
        else: mx.extend((T[i]+12,T[i]+12))
    quad=sum(21*k-18*(k==2)+k*T[i] for i,k in enumerate(s))
    top=sorted((max(0,v) for v in mx),reverse=True)[:4]
    N=315*quad+126*sum(top[:3])+5*top[3]
    if N>best: best=N;count=1;witness=s
    elif N==best: count+=1
assert best==52995 and count==21
print("PASS: all 3^10=59049 occupancy cases, max N=52995, count=21")

B=F(383,504);r=F(5,504)
aquad=F(2,3)*(F(3,16)+r*r)+B*B/30
assert aquad==F(52369,362880)
upper=F(best,151200)+aquad/25
gap=1-F(5,4)*upper
assert upper==F(3232069,9072000)
assert gap==F(4025531,7257600)
assert gap>F(56198549,101606400)
print("PASS: exact quadratic bound and improved rational gap")

mask=28443
x=[(mask>>i)&1 for i in range(20)]
a=[F(0) for _ in range(20)]
for i in (0,8,10): a[i]=F(1,4)
a[13]=r
assert sum(a)==B
assert all(x[i] for i in (0,8,10,13))
assert all(M[i][j]==1 for i,j in combinations((0,8,10,13),2))
y=[F(x[i],4)+a[i]/5 for i in range(20)]
assert sum(y[i]*M[i][j]*y[j] for i in range(20) for j in range(20))/30==upper
print("PASS: exact scalar-relaxation equality witness (not a physical code)")
print("RESULT: conditional d >=",gap,"=",float(gap))
