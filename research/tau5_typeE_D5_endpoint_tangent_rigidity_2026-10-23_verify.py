"""Exact integer/modular/rational certificate: D5 endpoint tangent rigidity.

No numerical rank thresholds, eigensolvers, or LP solvers. Analytic endpoint
argument and local-isolation proof are in the companion .md note.
"""
from itertools import combinations
from collections import Counter
from sympy import Matrix, Rational, eye

V=[]; labels=[]
for a,b in combinations(range(5),2):
    for s in (-1,1):
        v=[0]*5; v[a]=1; v[b]=s
        V.append(v); labels.append((a,b,s))
def dot(x,y): return sum(a*b for a,b in zip(x,y))
E=[(i,j) for i in range(20) for j in range(i+1,20)
   if abs(dot(V[i],V[j]))==1]
assert len(V)==20 and len(E)==120
R=[]
for i,j in E:
    row=[0]*100; s=dot(V[i],V[j])
    for k in range(5):
        row[5*i+k]=s*V[j][k]
        row[5*j+k]=s*V[i][k]
    R.append(row)
T=[]
for i in range(20):
    row=[0]*100
    for k in range(5): row[5*i+k]=V[i][k]
    T.append(row)

def rank_mod(rows,p):
    M=[[int(x)%p for x in row] for row in rows]
    r=0; n=len(M); cols=len(M[0])
    for c in range(cols):
        pivot=next((i for i in range(r,n) if M[i][c]),None)
        if pivot is None: continue
        M[r],M[pivot]=M[pivot],M[r]
        inv=pow(M[r][c],-1,p)
        for j in range(c,cols): M[r][j]=M[r][j]*inv%p
        for i in range(r+1,n):
            f=M[i][c]
            if f:
                for j in range(c,cols):
                    M[i][j]=(M[i][j]-f*M[r][j])%p
        r+=1
    return r

for i in range(20):
    N=[j for j in range(20) if j!=i and abs(dot(V[i],V[j]))==1]
    assert len(N)==12
    assert [sum(dot(V[i],V[j])*V[j][k] for j in N)
            for k in range(5)]==[6*x for x in V[i]]
assert rank_mod(R+T,3)==rank_mod(R+T,101)==90
print("PASS: 20 signed stress identities, exact real rank 90")

N=[j for j in range(20) if j!=0 and abs(dot(V[0],V[j]))==1]
vv=[Matrix(v) for v in V]
S0=sum((vv[j]*vv[j].T/2 for j in N),Matrix.zeros(5))
assert S0==Matrix.diag(3,3,2,2,2)
minors=[None]*5
for missing in combinations(N,3):
    S=S0-sum((vv[j]*vv[j].T/2 for j in missing),Matrix.zeros(5))
    H=S-Rational(3,8)*eye(5)
    for k in range(1,6):
        d=H[:k,:k].det()
        assert d>0
        if minors[k-1] is None or d<minors[k-1]: minors[k-1]=d
assert minors==[Rational(9,8),Rational(189,64),Rational(13,512),
               Rational(169,4096),Rational(2197,32768)]
print("PASS: 220 exact Sylvester tests; retained neighbors span R5")

core=[i for i,(a,b,s) in enumerate(labels) if a==0 and s==1]
removed=[k for k,(i,j) in enumerate(E) if i in core and j in core]
kept=[k for k in range(120) if k not in removed]
assert len(core)==4 and len(removed)==6
assert rank_mod([R[k] for k in kept]+T,101)==90
u=[0]*100
for i in core:
    _,b,_=labels[i]
    for k in range(5): u[5*i+k]=1-(2 if k==b else 0)
assert all(dot(row,u)==0 for row in T)
d=[dot(row,u) for row in R]
assert Counter(d[k] for k in removed)==Counter({4:6})
assert Counter(d[k] for k in kept)==Counter({0:102,-2:12})
print("PASS: six deleted contacts +4, twelve retained -2, 102 retained 0")
print("PASS: exact finite certificate complete")
