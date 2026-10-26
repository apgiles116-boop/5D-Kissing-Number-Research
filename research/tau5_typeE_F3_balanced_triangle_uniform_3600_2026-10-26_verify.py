#!/usr/bin/env python3
"""Exact checks for F3 matching-uniform balanced-triangle 1/3600 theorem.
Analytic vector inequalities are proved in the companion research note.
"""
from itertools import combinations
from fractions import Fraction as F
from random import Random
import sympy as s

edges=[(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]
matchings=[m for m in combinations(edges,4)
           if len({v for e in m for v in e})==8]
assert len(matchings)==3
assert set(matchings)=={
 ((0,2),(1,4),(3,6),(5,7)),
 ((0,4),(1,7),(2,3),(5,6)),
 ((0,5),(1,4),(2,7),(3,6))}
for m in matchings:
    index={v:i for i,e in enumerate(m) for v in e}
    sign={v:(1 if v==e[0] else -1) for e in m for v in e}
    cross=[(frozenset((index[a],index[b])),sign[a]*sign[b],(a,b))
           for a,b in edges if index[a]!=index[b]]
    assert len(cross)==6
    balanced=[]
    for tri in combinations(cross,3):
        p=[c[0] for c in tri]
        if len(set(p))==3 and len(set().union(*p))==3 and tri[0][1]*tri[1][1]*tri[2][1]==1:
            balanced.append(tuple(c[2] for c in tri))
    assert len(balanced)==4,(m,balanced)
    print("matching",m,"balanced quotient triangles",len(balanced))

r,t=s.symbols("r t",nonnegative=True)
expr=s.expand((30-r-2*t)**2-832*r)
reduced=s.expand(expr-r**2+1-t**2)
assert s.expand(reduced-(901+3*t**2+4*r*t-892*r-120*t))==0
assert s.expand(449*(t-s.Rational(60,449))**2+s.Rational(441,449)
                -(9+449*t**2-120*t))==0
assert s.Rational(26,15)**2>3
assert 480*s.Rational(26,15)==832
assert F(4608,3600)==F(32,25)
assert F(1,4)-F(1,3600)==F(899,3600)

rng=Random(360026)
for trial in range(200):
    m=[[F(rng.randint(-5,5),rng.randint(2,8)) for k in range(5)]
       for i in range(4)]
    dot=lambda x,y:sum(a*b for a,b in zip(x,y))
    a=[dot(x,x) for x in m]
    C=sum(a)
    gij={(i,j):dot(m[i],m[j]) for i,j in combinations(range(4),2)}
    N=sum(max(F(0),-v) for v in gij.values())
    E=sum(a[i]+a[j]-2*abs(v) for (i,j),v in gij.items())
    M=[sum(m[i][k] for i in range(4)) for k in range(5)]
    assert E+dot(M,M)==4*(C-N)
    assert E>=0 and C-N>=0
print("PASS: graph, rational SOS, and 200 exact Gram identities")
