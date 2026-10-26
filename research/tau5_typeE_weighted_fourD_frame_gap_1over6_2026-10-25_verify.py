#!/usr/bin/env python3
"""Exact arithmetic verifier for Type-E weighted 4D LP frame gap 1/6.

The companion mathematical note proves the analytic inequalities.
"""
from fractions import Fraction as Q
import sympy as sp

Amax = Q(383, 504)
a = [Q(1, 4)] * 3 + [Q(5, 504)] + [Q(0)] * 12
c = [1 - x for x in a]
assert len(a) == 16 and sum(a) == Amax

def R(b):
    return sum(x*x for x in b)**2 / 32 - Q(3, 8)*sum(x**4 for x in b)

def U(b):
    return sum((1-b[i]*b[j])/16 for i in range(16)
               for j in range(i+1, 16))

Dstar = R(c)-U(c)
assert Dstar == Q(1665618603949, 2064772104192)
assert sum(x*x for x in a) <= Q(49, 256)
assert Amax / 4 < Q(49, 256)

t = sp.symbols("t")
f = t**4-t*t/sp.Integer(4)
assert sp.expand(f-(sp.Rational(1,16)
    +sp.Rational(1,8)*(4*t*t-1)
    +sp.Rational(1,16)*(16*t**4-12*t*t+1))) == 0

A, S2, S3, S4 = sp.symbols("A S2 S3 S4")
Dpoly = (64-46*A+5*A*A-4*A*S2-41*S2+S2*S2+48*S3-12*S4)/32
subs = {A:sp.Rational(383,504)}
for sym, degree in ((S2,2),(S3,3),(S4,4)):
    subs[sym] = sum(sp.Rational(x.numerator,x.denominator)**degree for x in a)
assert Dpoly.subs(subs) == sp.Rational(Dstar.numerator,Dstar.denominator)

x,y = sp.symbols("x y")
coefficient = (-8*A+4*S2-82+144*(x+y)-48*(x*x+x*y+y*y))/32
assert sp.expand(coefficient-((-8*A+4*S2-82)/32
    +sp.Rational(9,2)*(x+y)
    -sp.Rational(3,2)*(x*x+x*y+y*y))) == 0
assert Q(-82+1+72,32) == Q(-9,32)

v = sp.symbols("v")
monotone_lower = sp.Rational(17,16)*v+sp.Rational(3,4)-sp.Rational(3,2)*v**3
assert monotone_lower.subs(v,1) == sp.Rational(5,16)
assert sp.diff(monotone_lower,v).subs(v,sp.Rational(3,4)) < 0
phi = 2*v-sp.Rational(3,2)*v**3
assert phi.subs(v,sp.Rational(2,3)) == sp.Rational(8,9)
assert sp.diff(phi,v).subs(v,sp.Rational(2,3)) == 0

delta = Q(1,6)
k0 = Q(1,2)-(1-delta)**2/4
k2 = Q(3,2)+delta+delta**2/4
assert k0 == Q(47,144) and k2 == Q(241,144)
pcoef = k0*Q(15,2)+(1-delta)/4*Q(7,4)
assert pcoef == Q(45,16)
assert Q(15,16)+pcoef == Q(15,4)

rhs = (Q(15,4)+Q(8,9))*delta + k2*delta**2/2
assert rhs == Q(8257,10368)
margin = Dstar-rhs
assert margin == Q(21249076141,2064772104192) and margin > 0
print("PASS exact Gegenbauer, deficit extremum, pair bounds and margin")
print("Contradiction margin:", margin, "=", float(margin))
print("Theorem: F_O > I_5/6; Type-E corollary (conditional): H_184 > A/12 for A>0")
