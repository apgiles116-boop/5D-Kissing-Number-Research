#!/usr/bin/env python3
"""Exact integer/rational interval certificate: Type-E support-fibre distance >1/360."""
from fractions import Fraction as F
from math import isqrt
from itertools import combinations

pairs=list(combinations(range(5),2))
mult=(60,30,20,15,12)
DEN=360
TARGET=F(13,5)
A=F(383,504)

def pnum(v):
    return tuple(sum(v[k]*mult[k] for k in range(j,5)) for j in range(5))

def check(simplex,depth):
    D=60*(1<<depth)
    pp=[pnum(v) for v in simplex]
    lo=[min(p[j] for p in pp) for j in range(5)]
    hi=[max(p[j] for p in pp) for j in range(5)]
    if 3*DEN*(lo[0]+lo[1])>(2*DEN+9)*D:
        return 1,None
    bound=F(0)
    for i,j in pairs:
        N=lo[i]+lo[j]+2*isqrt(lo[i]*lo[j])
        numerator=3*DEN*N-(2*DEN+9)*D
        if numerator>0:
            s=isqrt(hi[i]*hi[j])
            s+=s*s!=hi[i]*hi[j]
            denominator=DEN*(75*(hi[i]-lo[j])+78*s)
            assert denominator>0
            bound+=F(25*numerator,denominator)
    if bound>=TARGET:
        return 2,None
    longest=(-1,None)
    for i,j in pairs:
        size=sum((pp[i][k]-pp[j][k])**2 for k in range(5))
        if size>longest[0]:
            longest=(size,(i,j))
    return 0,longest[1]

def run():
    eps=F(1,DEN)
    c=(1+4*eps)**2
    assert c==F(8281,8100)
    assert F(16,9)*c-1==F(14899,18225)<F(325,397)
    upper=8*(c-1)+F(28,9)*c*A
    assert upper==F(3406199,1312200)
    assert TARGET-upper==F(5521,1312200)>0
    assert 2*(F(6,5)*eps+eps**2)<=3*eps
    initial=tuple(tuple(int(i==j) for i in range(5)) for j in range(5))
    stack=[(initial,0)]
    nodes=domain=boundpruned=maxdepth=0
    while stack:
        simplex,depth=stack.pop()
        nodes+=1
        status,edge=check(simplex,depth)
        if status==1:
            domain+=1
        elif status==2:
            boundpruned+=1
        else:
            maxdepth=max(maxdepth,depth)
            i,j=edge
            doubled=[tuple(2*x for x in v) for v in simplex]
            mid=tuple(simplex[i][k]+simplex[j][k] for k in range(5))
            left=doubled.copy()
            right=doubled.copy()
            left[i]=mid
            right[j]=mid
            stack.append((tuple(left),depth+1))
            stack.append((tuple(right),depth+1))
        assert nodes<2_000_000
    assert (nodes,domain,boundpruned,maxdepth)==(988525,73371,420892,43)
    assert domain+boundpruned==(nodes+1)//2
    print("PASS: Type-E support-fibre distance >1/360")
    print("nodes",nodes,"domain",domain,"bound",boundpruned,"depth",maxdepth)

if __name__=="__main__":
    run()
