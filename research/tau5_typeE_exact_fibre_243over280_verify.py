"""Exact Type-E support-plane fibre certificate, 2026-10-30.

Proves F(p)>=27/10 on the ordered simplex with p1+p2<=2/3,
checks A>=243/280, and a sharp rational Petersen-variance example.
Only integer and Fraction comparisons are used in certification.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
from time import monotonic

PAIRS=list(combinations(range(5),2))
MULT=(60,30,20,15,12)
TARGET=F(27,10)
EXPECTED=(407557,32997,170782,36)

def pnum(v):
    return tuple(sum(v[k]*MULT[k] for k in range(j,5)) for j in range(5))

def certify_cell(simplex,depth):
    D=60*(1<<depth)
    pp=[pnum(v) for v in simplex]
    lo=[min(p[j] for p in pp) for j in range(5)]
    hi=[max(p[j] for p in pp) for j in range(5)]
    if 3*(lo[0]+lo[1])>2*D:
        return 1,None
    lower=F(0)
    for i,j in PAIRS:
        n=3*(lo[i]+lo[j]+2*isqrt(lo[i]*lo[j]))-2*D
        if n>0:
            sq=isqrt(hi[i]*hi[j])
            if sq*sq!=hi[i]*hi[j]: sq+=1
            den=3*(hi[i]-lo[j]+sq)
            assert den>0
            lower+=F(n,den)
    if lower>=TARGET:
        return 2,None
    longest=(-1,None)
    for i,j in PAIRS:
        d=sum((pp[i][k]-pp[j][k])**2 for k in range(5))
        if d>longest[0]: longest=(d,(i,j))
    return 0,longest[1]

def verify_center(max_nodes=2_000_000):
    simp=tuple(tuple(int(i==j) for i in range(5)) for j in range(5))
    stack=[(simp,0)]
    n=nd=nf=depthmax=0
    start=monotonic()
    while stack:
        simp,depth=stack.pop()
        n+=1
        status,edge=certify_cell(simp,depth)
        if status==1: nd+=1
        elif status==2: nf+=1
        else:
            depthmax=max(depthmax,depth)
            i,j=edge
            doubled=[tuple(2*x for x in v) for v in simp]
            mid=tuple(simp[i][k]+simp[j][k] for k in range(5))
            left=list(doubled);left[i]=mid
            right=list(doubled);right[j]=mid
            stack.append((tuple(left),depth+1))
            stack.append((tuple(right),depth+1))
        assert n<max_nodes or not stack, "Certificate incomplete"
    result=(n,nd,nf,depthmax)
    assert result==EXPECTED, (result,EXPECTED)
    print("PASS: exact ordered-simplex F>=27/10 certificate",result,
          "elapsed_s",round(monotonic()-start,2))

def verify_energy():
    assert F(4,3)+F(16,9)/8==F(14,9)
    assert F(9,28)*F(27,10)==F(243,280)
    assert F(243,280)-F(383,504)==F(34,315)>0
    assert F(28,9)<F(35,11)
    print("PASS: rational safe-block coefficient and energy gap 34/315")

def verify_sharpness():
    cycle={(0,1):1,(1,2):-1,(2,3):1,(0,3):-1}
    a0=F(3,100);eps=F(1,100)
    support=[]; vec=[]; a=[]
    for p,q in PAIRS:
        for sign in (1,-1):
            t=[0]*5;t[p]=1;t[q]=sign
            vec.append(t);support.append((p,q))
            a.append(a0+eps*cycle.get((p,q),0))
    assert all(F(0)<=x<=F(1,4) for x in a)
    assert sum(a)==F(3,5)<F(383,504)
    w=[1-x for x in a]
    n=len(a)
    P0=[[F(3,10) if i==j or support[i]==support[j]
          else F(-1,30) if len(set(support[i])&set(support[j]))==1
          else F(2,15) for j in range(n)] for i in range(n)]
    Pc=[[P0[i][j]-F(1,20) for j in range(n)] for i in range(n)]
    K=[[w[i]*w[j]*(F(sum(vec[i][k]*vec[j][k] for k in range(5))**2,4)-F(1,5))
        for j in range(n)] for i in range(n)]
    V=sum(K[i][j] for i in range(n) for j in range(n))
    C=sum(Pc[i][j]*K[i][j] for i in range(n) for j in range(n))
    E=V+12*C
    variance=sum((x-sum(a)/n)**2 for x in a)
    assert (variance,V,C,E)==(F(1,1250),F(0),F(1,9375),F(4,3125))
    assert variance==F(5,8)*E
    print("PASS: Petersen variance 5/8 sharpness at A=3/5")

if __name__=='__main__':
    verify_energy()
    verify_sharpness()
    verify_center()
    print("ALL EXACT CERTIFICATES PASSED; arbitrary Type E remains OPEN")
