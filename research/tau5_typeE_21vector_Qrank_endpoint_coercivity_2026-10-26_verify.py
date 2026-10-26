#!/usr/bin/env python3
"""Exact symbolic/rational checker for 21-vector Q-rank endpoint coercivity.
The proof is analytic in the companion Markdown note; this checks its algebra.
"""
from fractions import Fraction as F
from itertools import product
import sympy as s

A,A2,A3,A4=s.symbols("A A2 A3 A4")
B=21-2*A+A2
C=21-4*A+6*A2-4*A3+A4
phi=s.expand(s.Rational(3,10)*C-B**2/350
             -s.Rational(3,40)*((21-A)**2/5-B))
expected=(-s.Rational(12,25)*A+s.Rational(351,200)*A2
          -s.Rational(6,5)*A3+s.Rational(3,10)*A4
          -s.Rational(37,1400)*A**2+s.Rational(2,175)*A*A2-A2**2/350)
assert s.expand(phi-expected)==0
x,d=s.symbols("x d")
g=-s.Rational(12,25)+s.Rational(351,200)*x-s.Rational(6,5)*x*x+s.Rational(3,10)*x**3
assert g.subs(x,s.Rational(1,4))==-s.Rational(357,3200)
assert s.expand(s.diff(g,x)-(s.Rational(351,200)-s.Rational(12,5)*x+s.Rational(9,10)*x*x))==0
assert s.Rational(351,200)-s.Rational(3,5)>0
assert -s.Rational(37,1400)+s.Rational(2,175)/4==-s.Rational(33,1400)
assert s.expand((s.Rational(1,2)+d)**2*((s.Rational(1,2)+d)**2-s.Rational(1,4))
                -(d/4+s.Rational(5,4)*d*d+2*d**3+d**4))==0

# Exact rational Gram identity, rank and fourth-moment inequality.
ys=[s.Matrix([s.Rational(((i+1)*(j+2)+j*j)%11-5,7+j)
              for j in range(5)]) for i in range(21)]
rs=[y.dot(y) for y in ys]
Q=[y*y.T-r*s.eye(5)/5 for y,r in zip(ys,rs)]
K=s.Matrix(21,21,lambda i,j:s.trace(Q[i]*Q[j]))
assert K.rank()<=14
BB=sum(r*r for r in rs)
CC=sum(r**4 for r in rs)
S=sum(ys[i].dot(ys[j])**2 for i in range(21) for j in range(i+1,21))
T=sum(ys[i].dot(ys[j])**4 for i in range(21) for j in range(i+1,21))
W=sum(rs[i]*rs[j]*ys[i].dot(ys[j])**2
      for i in range(21) for j in range(i+1,21))
assert s.trace(K)==s.Rational(4,5)*BB
assert s.trace(K*K)==s.Rational(3,5)*CC+BB**2/25+2*T-s.Rational(4,5)*W
assert T>=s.Rational(2,5)*W+BB**2/350-s.Rational(3,10)*CC
Fmat=sum((y*y.T for y in ys),s.zeros(5))
V=s.trace((Fmat-s.trace(Fmat)*s.eye(5)/5)**2)
assert S==(s.trace(Fmat)**2/5-BB+V)/2

# Exact scalar check for all safe endpoint dots on a 1/8 grid.
vals=[F(k,8) for k in range(-4,5)]
count=0
for M,Z,X,Y in product(vals,repeat=4):
    dots=(M+Z+X+Y,M+Z-X-Y,M-Z+X-Y,M-Z-X+Y)
    if all(abs(t)<=F(1,2) for t in dots):
        assert M*M+Z*Z+X*X+Y*Y<=F(1,4)
        assert Z**4<=Z*Z/F(4)-Z*Z*(M*M+X*X+Y*Y)
        count+=1
for t,b in product(vals,repeat=2):
    if abs(t)+abs(b)<=F(1,2):
        assert t**4<=t*t/F(4)-t*t*(abs(b)-b*b)
print("PASS: exact polynomial, Q-rank/frame, and",count,"safe-pair checks")
