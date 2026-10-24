#!/usr/bin/env python3
"""Exact symbolic checks for the adjacent-defect quadratic budget.
The analytic endpoint/Cauchy proof is in the companion research note.
"""
from fractions import Fraction as F
from sympy import Rational, sqrt, simplify, symbols, diff, N

B=F(383,504)
D=F(1780062775,4032758016)
L=F(8790283,317520)
old=F(2067388216673,80655160320)
alpha=(sqrt(2)-1)/2
assert F(11,25)<D<F(9,20)
assert D>F(1,3)
assert B/2-F(1,4)<F(13,100)
assert B/2<F(2,5)
assert simplify(alpha+alpha**2-Rational(1,4))==0
assert alpha>Rational(207,1000)
assert alpha<Rational(208,1000)

Ds=Rational(D.numerator,D.denominator)
Bs=Rational(B.numerator,B.denominator)
s=symbols('s',real=True,nonnegative=True)
t=Rational(1,4)-s*s
Fs=t*t+(Ds-t)*s
certificate=4*s**3+3*(s-Rational(1,6))**2+Ds-Rational(1,3)
assert simplify(diff(Fs,s)-certificate)==0

x=symbols('x',real=True)
Fd=x*x+(Ds-x)*(Bs/2-x)
assert simplify(diff(Fd,x,2)-4)==0
assert Bs/2<2*alpha
assert simplify(Fd.subs(x,alpha)-alpha*Ds)<0
assert Fd.subs(x,Rational(1,4))<Rational(177,2000)
assert Rational(177,2000)<Rational(207,1000)*Rational(11,25)
assert Rational(207,1000)*Rational(11,25)<alpha*Ds

K=simplify(Rational(L.numerator,L.denominator)-Rational(3,2)-(1+alpha)*Ds)
expected=Rational(1047044579149,40327580160)-Rational(1780062775,8065516032)*sqrt(2)
assert simplify(K-expected)==0
assert simplify(K-Rational(old.numerator,old.denominator)-Ds*(Rational(1,4)-alpha))==0
assert K>Rational(old.numerator,old.denominator)
assert F(5,8)*B<F(1,2)
assert Rational(L.numerator,L.denominator)-2==Rational(8155243,317520)

print("PASS: alpha quadratic identity and exact rational bounds")
print("PASS: sqrt-branch derivative SOS and disjoint-branch convexity")
print("PASS: both endpoint comparisons and new safe-floor constant")
print("alpha D0 =",N(alpha*Ds,18))
print("K_new =",N(K,18))
print("gain =",N(K-Rational(old.numerator,old.denominator),18))
print("K_two =",float(L-F(2,1)))
