#!/usr/bin/env python3
"""Exact arithmetic checks for the 21-line quartic parity certificate."""
import sympy as s
from itertools import combinations
x=s.symbols("x",real=True)
P2=(5*x*x-1)/4
P4=(21*x**4-14*x*x+1)/8
f=x**4-x*x/4
assert s.expand(f-(s.Rational(1,28)+P2/3+s.Rational(8,21)*P4))==0
assert 21*f.subs(x,1)==s.Rational(441,28)
assert s.simplify(8*x*(s.Rational(1,4)-x)-x-x*(1-8*x))==0
assert s.simplify(8*x*(s.Rational(1,4)-x)-(s.Rational(1,4)-x)-(s.Rational(1,4)-x)*(8*x-1))==0
assert s.simplify(8*x*(x-s.Rational(1,4))-(x-s.Rational(1,4))-(x-s.Rational(1,4))*(8*x-1))==0
assert max(s.Rational(p*q,p+q) for p in range(1,5) for q in range(1,5) if p+q<=5)==s.Rational(6,5)
assert 21*13%2==1
assert min(abs(s.Rational(16,5)-s.Rational(k,4)) for k in range(21) if k!=13)==s.Rational(1,5)
assert abs(s.Rational(16,5)-s.Rational(13,4))==s.Rational(1,20)
d=s.Integer(341)
margin=s.factor((s.Rational(6,5)-s.Rational(184,5)/d)**2-s.Rational(504,25)**2/d)
assert margin==s.Rational(56644,72675625)>0
assert s.Rational(6,5)-s.Rational(184,5)/d>0
g=lambda a,b:1/s.sqrt((1-a)*(1-b))-1-s.Rational(2,3)*(a+b)
for a,b in [(0,0),(s.Rational(1,4),0),(0,s.Rational(1,4)),(s.Rational(1,4),s.Rational(1,4))]:
    assert s.simplify(g(a,b))<=0
# D5 20-line coherence/tight-frame sanity check.
from sympy import Matrix,sqrt
vs=[]
for i,j in combinations(range(5),2):
    for sign in (-1,1):
        v=[0]*5;v[i]=1;v[j]=sign
        vs.append(Matrix(v)/sqrt(2))
assert len(vs)==20
assert all(abs(s.simplify(v.dot(w)))<=s.Rational(1,2) for v,w in combinations(vs,2))
assert sum((v*v.T for v in vs),Matrix.zeros(5))==4*Matrix.eye(5)
print("PASS exact quartic identity, parity, nuclear norm, rational margin and D5 sanity check")
