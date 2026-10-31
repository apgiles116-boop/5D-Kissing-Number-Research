#!/usr/bin/env python3
"""Exact rational finite audit: rank-13 D5 spectral gap >1/8 and Type-E margins."""
from itertools import combinations
from fractions import Fraction as F
import sympy as s

labels=[(i,j,sg) for i,j in combinations(range(5),2) for sg in (1,-1)]
Q=[]
for i,j,sg in labels:
    v=s.zeros(5,1); v[i]=1; v[j]=sg
    Q.append(v*v.T/s.Integer(2)-s.eye(5)/5)
K=s.Matrix(20,20,lambda i,j:s.trace(Q[i]*Q[j]))
x=s.symbols("x")
base=[i for i,l in enumerate(labels) if l[:2]==(0,1)]
polys={}
n=0
for rem in combinations([i for i in range(20) if i not in base],2):
    if labels[rem[0]][:2]==labels[rem[1]][:2]: continue
    kept=[i for i in range(20) if i not in base+list(rem)]
    p=s.Poly(K.extract(kept,kept).charpoly(x).as_expr(),x)
    while p.eval(0)==0: p=p.exquo(s.Poly(x,x))
    assert p.degree()==13
    fac=str(s.factor(p.as_expr()))
    polys[fac]=polys.get(fac,0)+1
    n+=1
assert n==144 and len(polys)==5
assert sorted(polys.values())==[12,24,24,36,48]
for fac,count in polys.items():
    p=s.Poly(s.sympify(fac),x)
    assert p.count_roots(0,s.Rational(1,8))==0
    print("PASS exact polynomial",count,fac)
print("PASS all 144 for missing support 01, hence all 1440 by symmetry")

eta=F(3,2500);B=F(18,25)
assert 19998>141**2 and 2<F(3,2)**2
assert B-F(101,141)-F(3,20000)-eta==F(6593,2820000)>0
assert F(3,4)-eta*eta-B*B-F(12,25)**2==F(7491,6250000)>0
assert F(478,625)-4*eta*eta-F(383,504)==F(959491,196875000)>0
print("PASS exact plane, coordinate, and midpoint-energy margins")
print("CONDITIONAL Type-E exclusion only; global 40<=tau5<=44 unchanged")
