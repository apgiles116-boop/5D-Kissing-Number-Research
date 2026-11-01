#!/usr/bin/env python3
"""Exact checks for Type-E refined 16-line harmonic leakage (2026-11-01)."""
from fractions import Fraction as F
import sympy as S

x=S.symbols('x')
f=x**4-S.Rational(1,4)*x**2
assert S.expand(f-(S.Rational(7,60)*S.legendre(0,x)+S.Rational(17,42)*S.legendre(2,x)+S.Rational(8,35)*S.legendre(4,x)))==0
assert S.expand(f-(S.Rational(1,16)+S.Rational(1,8)*(4*x*x-1)+S.Rational(1,16)*(16*x**4-12*x*x+1)))==0
b,s=S.symbols('b s')
assert S.expand((S.Rational(1,4)+s+s*s)*(b/4+s+s*s)-(b/16+b*s/4+b*s*s/4+s/4+S.Rational(5,4)*s*s+2*s**3+s**4))==0
assert F(1,2)+F(15,256)+F(75,128)==F(293,256)
assert F(1,16)+F(1,4)==F(5,16)
print('PASS: harmonic expansions and pairwise envelope coefficients')

A=F(383,504)
def H(d,B):
    alpha=F(7,60) if d==3 else F(1,16)
    M=15+(1-B)**4 if B<=1 else 14+(2-B)**4
    return alpha/F(2)*(16-2*B+B*B/16)**2-F(3,8)*M

def U(B,L):
    return F(15,16)*B+F(45,16)*L+F(293,256)*L**2+F(5,16)*L**3+F(1,16)*L**4

cases=[(3,F(4,5),F(15739941658327447,1238863262515200000)),
       (4,F(11,250),F(530015660962164281377,129048256512000000000000))]
for d,L,expected in cases:
    B=A+L
    assert H(d,B)-U(B,L)==expected and expected>0
    assert B<(F(8,5) if d==3 else F(81,100))
    print('PASS: dimension',d,'L=',L,'exact margin=',expected)
assert -F(7,60)*F(64,5)*F(9,5)+F(3,2)==-F(297,250)
assert -F(1,16)*F(719,50)*F(1519,800)+F(3,2)==-F(132161,640000)
print('PASS: derivative certificates')

c=F(11,250)
xy=c*(F(4,5)-c)
minor=F(81,131072)*xy**2
assert xy==F(2079,62500)
assert minor==F(350101521,512000000000000)
sigma=S.Rational(9,512)*S.Rational(xy.numerator,xy.denominator)/S.sqrt(2)
assert S.simplify(sigma-18711*S.sqrt(2)/64000000)==0
print('PASS: conditional two-ray and minor/singular-value constants')
print('ALL EXACT ALGEBRA CHECKS PASSED')
