#!/usr/bin/env python3
"""Exact audit: D5 covering-energy polynomial, moments, and Q-gap."""
from fractions import Fraction as F
from itertools import combinations, product
import sympy as S

b,t=S.symbols("b t", nonnegative=True)
q=(1-S.Rational(25,4)*b*b)*t*t-2*b*(1-S.Rational(5,2)*b)*t
assert S.simplify((t-b)**2-q-S.Rational(25,4)*b*b*(t-S.Rational(2,5))**2)==0
assert S.simplify((1-S.Rational(25,4)*b*b)*S.Rational(8,5)
       -8*b*(1-S.Rational(5,2)*b)-10*(S.Rational(2,5)-b)**2)==0

pairs=list(combinations(range(5),2))
def ts_for(v):
    N=sum(x*x for x in v)
    return [F((v[i]+sgn*v[j])**2,2*N)
            for i,j in pairs for sgn in (-1,1)]

count=0
for v in product((-2,-1,0,1,2), repeat=5):
    if not any(v): continue
    count+=1
    ts=ts_for(v)
    N=sum(x*x for x in v)
    assert sum(ts)==4
    assert sum(x*x for x in ts)==F(3,2)+F(sum(x**4 for x in v),2*N*N)
    for cap in (F(0),F(1,8),F(1,4),F(1,3),F(2,5)):
        assert sum(max(F(0),x-cap)**2 for x in ts)>=10*(F(2,5)-cap)**2

ts=ts_for((1,1,1,1,1))
assert ts.count(F(2,5))==10 and ts.count(F(0))==10
assert sum(max(F(0),x-F(1,4))**2 for x in ts)==F(9,40)
T=S.Rational(383,504)
Umax=3*S.Rational(1,16)+(T-S.Rational(3,4))**2
assert Umax==S.Rational(47653,254016)
v=S.sqrt(S.Rational(9,40))
E2=S.simplify(2*(v-S.sqrt(Umax)/3)**2)
assert S.simplify(E2-S.Rational(2810177,5715360)+S.sqrt(476530)/2520)==0
assert E2>S.Rational(217,1000)
U=S.symbols("U",nonnegative=True)
lhs=S.Rational(3,2)*(v-S.sqrt(U)/3)**2+S.Rational(4,5)*U
rhs=S.Rational(81,290)+S.Rational(29,30)*(S.sqrt(U)-S.Rational(15,29)*v)**2
assert S.simplify(lhs-rhs)==0
print("PASS: exact symbolic identities, sharp equality, and",count,
      "integer direction tests at five caps")
print("Umax:",Umax,"E2 bound:",E2,"~",E2.evalf(17))
print("Weighted Q-distance >= 81/290")
