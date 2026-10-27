#!/usr/bin/env python3
"""Exact symbolic checks: Type-E frame variance and conditional 17-line energy."""
import sympy as s
from itertools import combinations
r=s.sqrt(2); U=s.Rational(383,504)
rho2=8/(31-6*r); k=s.simplify(1/(4*rho2))
assert k==(31-6*r)/32
C=s.simplify(4*(1-k/s.Rational(3,4)))
A=s.simplify(s.Rational(1,4)+C)
assert C==r-s.Rational(7,6)
assert A==r-s.Rational(11,12)
assert (U-A).is_positive
x=s.symbols('x')
poly=s.expand(-504*((x+4-U)*(1-x)-4*k))
assert poly==504*x*x+1129*x+320-378*r
root=(s.sqrt(629521+762048*r)-1129)/1008
assert s.simplify(poly.subs(x,root))==0
assert root.is_positive and (s.Rational(1,4)-root).is_positive
assert s.simplify(U-C)==s.Rational(971,504)-r
# Test the exact unnormalized frame identity on 20 rational vectors.
Z=[]
for i in range(5):
 for j in range(4):
  v=s.zeros(5,1); v[i]=s.Rational(j+1,5); Z.append(v)
F=sum((v*v.T for v in Z),s.zeros(5))
ai=[1-v.dot(v) for v in Z]; AA=sum(ai)
T=sum((Z[i].dot(Z[j])**2 for i,j in combinations(range(20),2)),s.Integer(0))
V=s.trace((F-(20-AA)/5*s.eye(5))**2)
assert s.simplify(T-(30-3*AA+AA**2/10-sum(t*t for t in ai)/2+V/2))==0
# Tight frame equality need not imply D5.
E=[s.eye(5)[:,i] for i in range(5) for _ in range(4)]
assert sum((v*v.T for v in E),s.zeros(5))==4*s.eye(5)
assert sum((E[i].dot(E[j])**2 for i,j in combinations(range(20),2)),s.Integer(0))==30
print("PASS: exact frame-variance identity and normalized Welch equality")
print("PASS: conditional C >=",C,"~",s.N(C,12))
print("PASS: conditional A >=",A,"~",s.N(A,12))
print("PASS: conditional outside energy lower =",root,"~",s.N(root,12))
print("PASS: conditional outside energy upper =",s.simplify(U-C),"~",s.N(U-C,12))
