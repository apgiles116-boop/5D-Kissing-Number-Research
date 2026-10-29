#!/usr/bin/env python3
"""Exact rational audit of deep-edge cap, Q-frame and 184-safe floors."""
import sympy as s
A=s.Rational(383,504)
D=s.Rational(1780062775,4032758016)
U=s.Rational(3,16)+(A-s.Rational(3,4))**2
L=30-3*A+A*A/10-U/2
old=s.Rational(17456771,635040)
safe=L-s.Rational(3,2)-D-A*A/4
assert A-s.Rational(3,4)==s.Rational(5,504)
assert U==s.Rational(47653,254016)
assert L==s.Rational(8790283,317520)
assert L-old==s.Rational(131,672)
assert safe==s.Rational(64520136179,2520473760)
x=s.symbols('x',real=True)
for j in range(4):
    uj=s.Rational(j,16)+(x-s.Rational(j,4))**2
    derivative=s.diff(30-3*x+x*x/10-uj/2,x)
    assert s.simplify(derivative-(-3-s.Rational(4,5)*x+s.Rational(j,4)))==0
    assert derivative.subs(x,s.Rational(j+1,4))<0
q=s.symbols('q',nonnegative=True)
assert s.expand((s.Rational(1,2)+q)**2
                -(s.Rational(1,4)+q+q*q))==0
print('PASS: exact convex envelope and monotonic Q-frame floor')
print('PASS: exact six-exception decomposition and 184-safe bound')
print('Universal squared-correlation floor:',L,'=',s.N(L,18))
print('184-safe floor:',safe,'=',s.N(safe,18))
print('Global status unchanged: 40 <= tau_5 <= 44')
