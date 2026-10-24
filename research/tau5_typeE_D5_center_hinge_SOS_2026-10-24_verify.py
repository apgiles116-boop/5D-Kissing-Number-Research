#!/usr/bin/env python3
"""Exact verification: D5 center hinge-square theorem, 2026-10-24."""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp
q=sp.symbols("q",real=True)
p=sp.Rational(39,64)*q**2-sp.Rational(3,16)*q
assert sp.simplify((q-sp.Rational(1,4))**2-p-(5*q-2)**2/64)==0
assert sp.simplify(-p-q*(12-39*q)/64)==0
u=sp.symbols("u0:5",real=True)
S=sum(t*t for t in u)
qs=[(u[i]+s*u[j])**2/2 for i,j in combinations(range(5),2) for s in (-1,1)]
assert sp.expand(sum(qs)-4*S)==0
assert sp.expand(sum(t*t for t in qs)-sp.Rational(3,2)*S*S-sp.Rational(1,2)*sum(t**4 for t in u))==0
qeq=[F(0)]*10+[F(2,5)]*10
assert sum((max(t-F(1,4),F(0))**2 for t in qeq),F(0))==F(9,40)
B=sp.Rational(383,504)
Scap=sp.Rational(3,16)+(B-sp.Rational(3,4))**2
assert Scap==sp.Rational(47653,254016)
L=sp.simplify(sp.Rational(5,4)*(sp.sqrt(sp.Rational(9,40))-sp.sqrt(Scap)/5)**2)
assert sp.simplify(L-(sp.Rational(1476493,5080320)-sp.sqrt(476530)/6720))==0
a=sp.Rational(1476493,5080320)-sp.Rational(1879,10000)
b=sp.sqrt(476530)/6720
assert a>0 and sp.expand(a*a-b*b)>0
print("PASS: exact D5 moments, polynomial SOS, sharp equality")
print("PASS: Q-column bound",L,"=",sp.N(L,18))
