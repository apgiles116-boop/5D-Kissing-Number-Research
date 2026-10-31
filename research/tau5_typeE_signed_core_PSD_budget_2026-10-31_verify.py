#!/usr/bin/env python3
"""Exact Fraction checks for 2026-10-31 Type-E signed core PSD note."""
from fractions import Fraction as F
from itertools import product

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def neg(x): return max(F(0),-x)
def ceil(q): return -(-q.numerator//q.denominator)

def check(v):
    A=sum(dot(x,x) for x in v)
    p=[dot(v[i],v[j]) for i in range(4) for j in range(i+1,4)]
    assert sum(neg(t) for t in p)<=A
    assert sum(neg(t)**2 for t in p)<=A*A/4

vectors=[(F(a),F(b)) for a,b in product([-1,0,1],repeat=2)]
for ids in product(range(9),repeat=4):
    check([vectors[k] for k in ids])
v=[(F(1),F(0)),(F(1),F(0)),(F(-1),F(0)),(F(-1),F(0))]
check(v)
p=[dot(v[i],v[j]) for i in range(4) for j in range(i+1,4)]
assert sum(neg(t) for t in p)==4
assert sum(neg(t)**2 for t in p)==4

D=F(1780062775,4032758016)
A=F(383,504)
Qmin=F(17456771,635040)
Q6=F(3,2)+D+min(D*D,A*A/4)
Qsafe=Qmin-Q6
assert Q6==F(1051426055,504094752)
assert Qsafe==F(2000899807,78764805)
counts={}
for r in (F(0),F(1,8),F(1,4)):
    counts[str(r)]=ceil((Qsafe-184*r*r)/(F(1,4)-r*r))
assert counts=={'0':102,'1/8':97,'1/4':75}
A2=F(567,1000)
Qcritical=F(28397,1000)
Q6critical=F(3,2)+D+A2*A2/4
assert ceil((Qcritical-Q6critical-184*F(1,16))/(F(1,4)-F(1,16)))==80
print("Exact PSD tests: 6561 rational four-vector families PASS")
print("Sharp rank-one example PASS")
print("Q6 upper:",Q6,"Qsafe lower:",Qsafe)
print("Safe-pair counts:",counts,"critical rectangle: 80")
print("ALL CHECKS PASS")
