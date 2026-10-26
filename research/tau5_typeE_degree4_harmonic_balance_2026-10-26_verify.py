#!/usr/bin/env python3
"""Exact symbolic certificate for Type-E harmonic balance (2026-10-26)."""
import sympy as s
A,A2,A3,A4,B,C,R,S,T4,W,V,D,J,E4,eps,H=s.symbols('A A2 A3 A4 B C R S T4 W V D J E4 eps H')
Psi=C/6+B**2/42-R**2/24+5*B/24
psi_poly=(-s.Rational(4,3)*A+s.Rational(53,24)*A2-s.Rational(2,3)*A3+s.Rational(1,6)*A4+s.Rational(3,56)*A**2-s.Rational(2,21)*A*A2+A2**2/42)
assert s.expand(Psi.subs({C:21-4*A+6*A2-4*A3+A4,B:21-2*A+A2,R:21-A})-psi_poly)==0
balance=s.Rational(5,24)*V+J-Psi+eps+s.Rational(4,21)*H-s.Rational(2,3)*D-E4
balance=balance.subs({H:(7*C+42*T4-28*W+B**2)/8,eps:S/4-J+E4-T4})
balance=balance.subs({D:S-W,V:2*S+B-R**2/5})
assert s.expand(balance)==0
x=s.symbols('x',real=True)
h=lambda t:s.Rational(4,3)*t-s.Rational(53,24)*t**2+s.Rational(2,3)*t**3-s.Rational(1,6)*t**4
maxA=s.Rational(383,504)
values=[]
for k in range(4):
    r=x-s.Rational(k,4)
    a2=s.Rational(k,16)+r*r
    Hdef=k*h(s.Rational(1,4))+h(r)-s.Rational(3,56)*x*x+a2*(4*x-a2)/42
    p=s.expand(Hdef-s.Rational(51,64)*x)
    lo=s.Rational(k,4); hi=min(s.Rational(k+1,4),maxA)
    t=s.symbols('t')
    q=s.Poly(s.expand(-s.diff(p,x,2)).subs(x,lo+(hi-lo)*t),t)
    c0,c1,c2=q.nth(0),q.nth(1),q.nth(2)
    assert min(c0,c0+c1/2,c0+c1+c2)>0
    vals=(s.factor(p.subs(x,lo)),s.factor(p.subs(x,hi)))
    assert min(vals)>=0
    values.append(vals)
assert values==[(0,s.Rational(1,256)),(s.Rational(1,256),s.Rational(1,256)),(s.Rational(1,256),0),(0,s.Rational(759861745,169375836672))]
print('PASS: harmonic/frame balance identity, norm polynomial, sharp 51/64 scalar certificate')
