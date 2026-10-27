#!/usr/bin/env python3
"""Exact rational test of the center-tangent harmonic SOS identity.
Universal nonnegativity of K_res follows from the harmonic addition theorem,
not from a finite test.
"""
import sympy as s
from random import Random
Q=s.Rational
rng=Random(20261027)
z=[s.Matrix([Q(rng.randrange(-3,4),5) for _ in range(5)]) for _ in range(20)]
x=s.Matrix([1,0,0,0,0]); I=s.eye(5); P=I-x*x.T
dot=lambda a,b:(a.T*b)[0]
sq=lambda a:dot(a,a)
r=[sq(v) for v in z]
R2=sum((v*v for v in r),s.S.Zero)
S4=sum((v**4 for v in r),s.S.Zero)
F=s.zeros(5)
for ri,zi in zip(r,z): F+=ri*zi*zi.T
E=F-R2*I/5
d=dot(x,E*x); b=P*E*x; C=P*E*P
c=[dot(x,v) for v in z]
p=s.zeros(5,1)
for ci,zi in zip(c,z):p+=ci**3*(zi-ci*x)
h=sum((ci**4-Q(2,3)*ri*ci**2+ri**2/Q(21)
       for ci,ri in zip(c,r)),s.S.Zero)
g=4*(p-b/3)
def H4(u,v):
    w=dot(u,v)
    return w**4-Q(2,3)*sq(u)*sq(v)*w**2+sq(u)**2*sq(v)**2/Q(21)
K=sum((H4(u,v) for u in z for v in z),s.S.Zero)
Kres=K-Q(21,8)*h**2-Q(3,8)*sq(g)
D=sum((dot(z[i],z[j])**2*
       (dot(z[i],z[j])**2-r[i]*r[j]/4)
       for i in range(20) for j in range(i+1,20)),s.S.Zero)
base=R2**2/Q(56)-Q(3,8)*S4
rhs=(base+Q(25,96)*d**2+Q(21,16)*h**2+Q(5,3)*sq(p)
     +Q(3,4)*sq(b-Q(4,3)*p)
     +Q(5,24)*s.trace((C+d*P/4)**2)+Kres/2)
assert s.factor(D-rhs)==0
assert s.factor(s.trace(E*E)-Q(5,4)*d**2-2*sq(b)
                -s.trace((C+d*P/4)**2))==0
assert Kres>=0
print("PASS: exact rational center-tangent SOS identity and test residual")
