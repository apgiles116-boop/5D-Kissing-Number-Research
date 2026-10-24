#!/usr/bin/env python3
"""Exact algebraic checks for the Type-E cross-matching theorem."""
from sympy import symbols, simplify, expand, Rational, Matrix
from fractions import Fraction
X,U,V,W=symbols("X U V W",real=True)
a=(X+U+V+W)/4
b=(X-U-V+W)/4
c=(X-U+V-W)/4
d=(X+U-V-W)/4
assert simplify(a+b-(X+W)/2)==0
assert simplify(c+d-(X-W)/2)==0
assert simplify(a-b-(U+V)/2)==0
assert simplify(c-d-(V-U)/2)==0
p,q,t,C=symbols("p q t C",nonnegative=True)
assert expand((C**2/4-(p+q)**2).subs(C,2*(p+q)+t)-t*(p+q)-t*t/4)==0
B=Fraction(383,504);h=Fraction(1,1000)
v=B*h-h*h
assert v==Fraction(11953,15750000)
assert Fraction(7,250)**2-v==Fraction(79,3150000)>0
m1=Matrix([Rational(1,2),0])
m3=Matrix([-Rational(1,10),Rational(1,5)])
m4=Matrix([-Rational(1,10),-Rational(1,5)])
beta=-m3.dot(m4);s=-m1.dot(m3)
t34=m3.dot(m3)+m4.dot(m4)-2*beta
assert beta==Rational(3,100)
assert s==Rational(1,20)
assert t34==16*s*s==Rational(1,25)
print("PASS: cross-product identities, Pythagorean algebra, rational branch, midpoint witness")
print("STATUS: analytic four-vector theorem; Type-E application conditional; exclusion open")
