#!/usr/bin/env python3
"""Exact checks for Type-E weighted-harmonic 16-line leakage, 2026-11-01."""
from fractions import Fraction as F
import sympy as S
x=S.symbols('x')
f=x**4-S.Rational(1,4)*x*x
assert S.expand(f-(S.Rational(7,60)*S.legendre(0,x)+S.Rational(17,42)*S.legendre(2,x)+S.Rational(8,35)*S.legendre(4,x)))==0
assert S.expand(f-(S.Rational(1,16)+S.Rational(1,8)*(4*x*x-1)+S.Rational(1,16)*(16*x**4-12*x*x+1)))==0
b,s=S.symbols('b s')
assert S.expand((S.Rational(1,4)+s+s*s)*(b/4+s+s*s)-(b/16+b*s/4+b*s*s/4+s/4+S.Rational(5,4)*s*s+2*s**3+s**4))==0
A=F(383,504)
def M(B):
    return 15+(1-B)**4 if B<=1 else 14+(2-B)**4
def H(d,B):
    alpha=F(7,60) if d==3 else F(1,16)
    return alpha*(16-2*B+B*B/16)**2/2-F(3,8)*M(B)
def U(B,L):
    return (F(15,16)*B+F(15,8)*(F(1,2)+L)*L+
        F(15,128)*(F(1,2)+L)*L**2+F(15,8)*L+
        F(75,128)*L**2+F(15,32)*L**3+F(15,128)*L**4)
for d,L,expected in [
    (4,F(1,25),F(4974138029636009089,206477210419200000000)),
    (3,F(7,10),F(125849511944131207,1238863262515200000))]:
    B=A+L
    assert H(d,B)-U(B,L)==expected and expected>0
assert -F(1,16)*F(72,5)*F(19,10)+F(3,2)==-F(21,100)
assert -F(7,60)*13*F(29,16)+F(3,2)==-F(1199,960)
XY=F(1,25)*(F(7,10)-F(1,25))
assert XY==F(33,1250)
assert F(81,131072)*XY*XY==F(88209,204800000000)
assert S.simplify(9*S.Rational(33,1250)/(512*S.sqrt(2))-297*S.sqrt(2)/1280000)==0
print('ALL EXACT VERIFICATION CHECKS PASSED')
