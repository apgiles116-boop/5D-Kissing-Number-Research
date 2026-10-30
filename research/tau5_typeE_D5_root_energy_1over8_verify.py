#!/usr/bin/env python3
"""Exact integer/rational interval certificate: D5 root separation >sqrt(2)/8."""
from fractions import Fraction as F
from math import isqrt
from itertools import combinations

pairs=list(combinations(range(5),2))
mult=(60,30,20,15,12)
A=F(383,504)

def pnum(v):
    return tuple(sum(v[k]*mult[k] for k in range(j,5)) for j in range(5))

def check(simplex,depth):
    D=60*(1<<depth)
    pp=[pnum(v) for v in simplex]
    lo=[min(p[j] for p in pp) for j in range(5)]
    N=lo[0]+lo[1]+2*isqrt(lo[0]*lo[1])
    if 12*N>11*D:
        return 1,None
    bound=F(0)
    for i,j in pairs:
        N=lo[i]+lo[j]+2*isqrt(lo[i]*lo[j])
        if 4*N>3*D:
            bound+=F(4*N-3*D,4*N-D)
    if bound>A:
        return 2,None
    longest=(-1,None)
    for i,j in pairs:
        size=sum((pp[i][k]-pp[j][k])**2 for k in range(5))
        if size>longest[0]:
            longest=(size,(i,j))
    return 0,longest[1]

def run():
    initial=tuple(tuple(int(i==j) for i in range(5)) for j in range(5))
    stack=[(initial,0)]
    nodes=domain=energy=maxdepth=0
    while stack:
        simplex,depth=stack.pop()
        nodes+=1
        status,edge=check(simplex,depth)
        if status==1:
            domain+=1
        elif status==2:
            energy+=1
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
    assert (nodes,domain,energy,maxdepth)==(111395,1636,54062,36)
    assert domain+energy==(nodes+1)//2
    print("PASS: D5 root distance >sqrt(2)/8")
    print("nodes",nodes,"domain",domain,"energy",energy,"depth",maxdepth)

if __name__=="__main__":
    run()
