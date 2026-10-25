#!/usr/bin/env python3
"""Exact symbolic/rational checks for Type-E outside-16 rank-five theorem."""
from fractions import Fraction as Q
import sympy as s
t=s.symbols('t',real=True)
f=t**4-t**2/4
P2=(4*t**2-1)/3
P4=(16*t**4-12*t**2+1)/5
assert s.expand(f-(1+6*P2+5*P4)/16)==0
assert f.subs(t,1)==s.Rational(3,4)
a,b=s.symbols('a b',real=True,nonnegative=True)
h=1-a*b/(a+b)
ratio=h/((1-a)**2*(1-b)**2)
derivative_sign=2*h-(1-a)*b*b/(a+b)**2
assert s.simplify(s.diff(ratio,a)-derivative_sign/((1-a)**3*(1-b)**2))==0
assert ratio.subs({a:s.Rational(1,4),b:s.Rational(1,4)})==s.Rational(224,81)
B=Q(383,504)
assert Q(27,35)-B==Q(203,17640)>0
assert Q(224,81)*Q(30,16)==Q(140,27)
assert Q(4)-Q(140,27)*B==Q(29,486)
n=s.symbols('n',positive=True)
assert s.simplify(n*(n-12)/(2*s.Rational(224,81)*(n-1))-81*n*(n-12)/(448*(n-1)))==0
c=Q(187,250)
coef=1/(2*c)+1/(4*c*c)
assert coef==Q(39000,34969) and coef<Q(9,8)
assert Q(501,748)<Q(67,100)
fp=s.diff(f,t)
assert fp.subs(t,s.Rational(67,100))==s.Rational(217013,250000)<s.Rational(22,25)
tmin=1/s.sqrt(24)
assert s.simplify(s.diff(fp,t).subs(t,tmin))==0
assert s.simplify(fp.subs(t,tmin))==-1/(3*s.sqrt(24))
assert Q(22,25)*Q(9,8)==Q(99,100)
assert 30*Q(99,100)==Q(297,10)
assert Q(4)-(Q(140,27)*B+Q(297,10)*Q(1,500))==Q(329,1215000)>0
print('PASS: exact algebra, LP constants, rank obstruction, and spectral-gap contradiction.')
print('Status: lambda_min(Z_O)>1/500 under retained Type-E hypotheses; Type E open.')
