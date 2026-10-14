#!/usr/bin/env python3
"""Exact arithmetic verification for Type E mass-deficit concavity bound.
The inherited Delsarte, F3 and matching theorems are inputs, not reproved.
"""
import sympy as s
a=s.symbols('a', real=True)
D=s.expand(21-7*(1-2*a)**2*(4*(1-2*a)**2-1))
assert D==196*a-644*a**2+896*a**3-448*a**4
assert s.expand(D-84*a-112*a*(s.Rational(1,4)-a)*(4*a*a-7*a+4))==0
assert s.expand(s.diff(D,a,2)+56*(96*a*a-96*a+23))==0
assert D.subs(a,0)==0 and D.subs(a,s.Rational(1,4))==21
assert s.diff(D,a).subs(a,s.Rational(1,4))==14
assert (96*a*a-96*a+23).subs(a,s.Rational(1,4))==5

r=(1-s.sqrt((7+s.sqrt(721))/56))/2
s0=(1-s.sqrt((7+s.sqrt(s.Rational(2387,3)))/56))/2
s1=(1-s.sqrt((7+s.sqrt(s.Rational(4907,3)))/56))/2
assert s.simplify(D.subs(a,r)-15)==0
assert s.simplify(D.subs(a,s0)-s.Rational(43,3))==0
assert s.simplify(D.subs(a,s1)-s.Rational(41,6))==0
assert D.subs(a,s.Rational(111256,10**6))>15
assert D.subs(a,s.Rational(103545,10**6))>s.Rational(43,3)
assert D.subs(a,s.Rational(39782,10**6))>s.Rational(41,6)

assert 84-(s.Rational(74,2)-s.Rational(28,3))==s.Rational(169,3)
assert s.Rational(169,3)-42==s.Rational(43,3)
assert s.Rational(43,3)-s.Rational(15,2)==s.Rational(41,6)
assert s.Rational(169,3)<63
assert s.Rational(15,84)<s.Rational(1,4)
assert s.Rational(1,2)+s.Rational(111256,10**6)+s.Rational(39782,10**6)==s.Rational(651038,10**6)
print("Exact polynomial, radical, and rational checks: PASS")
print("Scalar upper bound:",s.N(s.Rational(1,2)+r+s1,18))
print("The concavity exchange and convex-composition arguments are in the note.")
