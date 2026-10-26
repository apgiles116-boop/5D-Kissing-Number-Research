#!/usr/bin/env python3
"""Exact SymPy checks for the rational 4D projection obstruction."""
import sympy as s

x=s.symbols("x")
mu=s.Rational(73,132)
f=s.expand((x+1)*(x+s.Rational(2,3))**2*x**2*(x-mu))
P=[s.chebyshevu(k,x)/(k+1) for k in range(7)]
c=[s.Rational(1475,19008),s.Rational(5455,19008),
   s.Rational(1621,3168),s.Rational(1475,2376),
   s.Rational(215,396),s.Rational(235,704),s.Rational(7,64)]
assert all(v>0 for v in c)
assert s.expand(f-s.Add(*(c[k]*P[k] for k in range(7))))==0
assert f.subs(x,1)==32*c[0]==s.Rational(1475,594)
assert mu!=s.Rational(2,3)

A,L=s.symbols("A L")
poly=s.expand(4356*((2*mu)**2*(A+L-1)+(1+L)**2))
assert s.expand(poly-(5329*A+14041*L+4356*L**2-973))==0
assert s.Rational(973,5329)>s.Rational(1,10)
low=s.Rational(5329,10)+s.Rational(14041*3,100)+s.Rational(4356*9,10000)
assert low==s.Rational(1197563,1250) and low<973

E=s.eye(5)
lines=[]
for i in range(5):
    for j in range(i+1,5):
        lines.append((E[:,i]+E[:,j])/s.sqrt(2))
        lines.append((E[:,i]-E[:,j])/s.sqrt(2))
Z=lines[:16]
assert all(abs(Z[i].dot(Z[j]))<=s.Rational(1,2)
           for i in range(16) for j in range(i+1,16))
F=sum((z*z.T for z in Z),s.zeros(5))
assert min(F.eigenvals())==2
assert 14041*2+4356*4>973
print("PASS: exact Gegenbauer expansion, strict 16-line LP certificate,")
print("      spectral polynomial, rational low-energy gap, D5 example")
