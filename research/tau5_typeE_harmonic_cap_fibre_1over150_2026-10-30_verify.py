#!/usr/bin/env python3
"""Exact Type-E 1/150 support-fibre certificate; no floating-point pruning.

Conditional on the retained harmonic/F3 mass and inverse-Q theorems.
Expected: 759391 cells, 44395 domain, 335301 function prunings, depth 34.
"""
from fractions import Fraction as Q
from math import isqrt
from itertools import combinations

PAIRS=list(combinations(range(5),2))
MULT=(60,30,20,15,12)
TARGET=Q(7,3)
EXPECTED=(759391,44395,335301,34)

def D(a):
    return 196*a-644*a*a+896*a**3-448*a**4

def Dprime(a):
    return 196-1288*a+2688*a*a-1792*a**3

def scalar_checks():
    B=Q(2595,256); c=15-B
    assert c==Q(1245,256)
    assert D(Q(17,625))>c
    assert D(Q(199,5000))>Q(41,6)
    assert D(Q(29,500))>Q(43,3)-B/2
    assert Dprime(Q(29,500))>129
    assert Q(1,2)+Q(17,625)+Q(199,5000)==Q(567,1000)
    eps=Q(1,150); kap=Q(3,5); cc=(1+4*eps)**2
    assert Q(16,9)*cc-1<2*kap/(1+kap*kap)
    upper=8*(cc-1)+Q(28,9)*cc*Q(567,1000)
    assert upper==Q(3222689,1406250)
    assert TARGET-upper==Q(58561,1406250)>0
    b=Q(19433,20000); r=(Q(99,70)/b); o=Q(33,70)
    hcoef=r+22*Q(26,15)*(2*o+5*r+r*r/1000)
    assert hcoef<Q(3151,10)
    assert Q(3151,10)/101300<Q(1,10)
    assert Q(15,7)*Q(3151,10)/101300<Q(1,150)
    print("PASS exact harmonic cap, robust gap, and Q residual arithmetic")

def pnum(v):
    return tuple(sum(v[k]*MULT[k] for k in range(j,5)) for j in range(5))

def cell(simplex,depth):
    den=60*(1<<depth)
    pp=[pnum(v) for v in simplex]
    lo=[min(p[j] for p in pp) for j in range(5)]
    hi=[max(p[j] for p in pp) for j in range(5)]
    if 150*(lo[0]+lo[1])>103*den:
        return 1,None
    lower=Q(0)
    for i,j in PAIRS:
        n=150*(lo[i]+lo[j]+2*isqrt(lo[i]*lo[j]))-103*den
        if n>0:
            root=isqrt(hi[i]*hi[j])
            root+=root*root!=hi[i]*hi[j]
            d=150*(hi[i]-lo[j])+180*root
            assert d>0
            lower+=Q(n,d)
    if lower>=TARGET:
        return 2,None
    best=-1;edge=None
    for i,j in PAIRS:
        ds=sum((pp[i][k]-pp[j][k])**2 for k in range(5))
        if ds>best:
            best=ds;edge=(i,j)
    return 0,edge

def verify(max_nodes=2_000_000):
    simp=tuple(tuple(int(i==j) for i in range(5)) for j in range(5))
    stack=[(simp,0)]
    n=nd=nf=depthmax=0
    while stack:
        simplex,depth=stack.pop()
        n+=1
        status,edge=cell(simplex,depth)
        if status==1:nd+=1
        elif status==2:nf+=1
        else:
            depthmax=max(depthmax,depth)
            i,j=edge
            doubled=[tuple(2*x for x in v) for v in simplex]
            mid=tuple(simplex[i][k]+simplex[j][k] for k in range(5))
            left=doubled.copy();left[i]=mid
            right=doubled.copy();right[j]=mid
            stack.extend([(tuple(left),depth+1),(tuple(right),depth+1)])
        assert n<max_nodes or not stack, "INCOMPLETE certificate"
    result=(n,nd,nf,depthmax)
    assert result==EXPECTED,(result,EXPECTED)
    print("PASS exact simplex certificate",result)

if __name__=="__main__":
    scalar_checks()
    verify()
    print("ALL EXACT CHECKS PASSED; arbitrary Type E remains OPEN")
