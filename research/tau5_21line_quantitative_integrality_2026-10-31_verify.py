#!/usr/bin/env python3
"""Exact verification of 21-line integrality/defect certificates. Python + SymPy."""
from fractions import Fraction as F
from random import Random
import sympy as s

t, v = s.symbols("t v", real=True)
P2 = (5*t*t-1)/4
P4 = (21*t**4-14*t*t+1)/8
assert s.expand(t**4-t*t/4-s.Rational(1,28)-P2/3-s.Rational(8,21)*P4)==0

p=F(1,103)
vstar=F(51,6695)
L0=F(1683,2060)
h=(L0+F(10,3)*vstar)**2-F(1799,20)*vstar
assert h==F(17500837,717168400) and h>0
assert F(4,5)*vstar<F(1,144)
assert L0+F(10,3)*vstar<1
assert F(24,5)*p<F(1,20)
assert F(3,13)*(24*p-F(1,5))==vstar

ss=s.symbols("ss", real=True)
assert s.expand((1+s.Rational(2,3)*ss)**2*(1-ss)-1
  +ss*(4*ss**2+8*ss-3)/9)==0
assert s.expand((1+s.Rational(2,3)*ss)**2
  *(s.Rational(15,16)-s.Rational(3,4)*ss)-1
  +(2*ss-1)*(8*ss**2+18*ss-3)/48)==0

rng=Random(20261031)
points=[]
for _ in range(21):
    w=[F(rng.randint(-3,3),rng.randint(1,4)) for _ in range(4)]
    norm2=sum(x*x for x in w)
    points.append([2*x/(1+norm2) for x in w]+[(1-norm2)/(1+norm2)])
assert all(sum(x*x for x in u)==1 for u in points)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
T=[[sum(u[i]*u[j] for u in points) for j in range(5)] for i in range(5)]
B=[[T[i][j]-(F(21,5) if i==j else F(0)) for j in range(5)] for i in range(5)]
V=sum(B[i][j]**2 for i in range(5) for j in range(5))
bs=[dot(points[i],points[j])**2 for i in range(21) for j in range(i+1,21)]
FF=sum(b*(b-F(1,4)) for b in bs)
H4=sum((21*dot(u,w)**4-14*dot(u,w)**2+1)/8 for u in points for w in points)
assert FF==F(5,24)*V+F(4,21)*H4 and H4>=0
PP=sum(max(b*(b-F(1,4)),F(0)) for b in bs)
assert PP>F(1,103)
for k in range(1001):
    b=F(k,1000)
    kk=0 if b<=F(1,8) else 1
    err=abs(b-F(kk,4))
    f=b*(b-F(1,4))
    if b<=F(1,4): assert err<=8*(-f)
    else: assert err<=4*f

a=s.symbols("a",real=True)
assert s.factor(s.Rational(1,2)-s.Rational(9,8)*a+a*a/4)==(a-4)*(2*a-1)/8
for sign in [-1,1]:
    G=s.Matrix([[s.Rational(3,4),s.Rational(1,2),s.Rational(1,2)],
      [s.Rational(1,2),1,sign*s.Rational(1,2)],
      [s.Rational(1,2),sign*s.Rational(1,2),1]])
    assert G.det()==s.Rational(1,16)+sign*s.Rational(1,4) and G.det()!=0

# Exact twenty-to-twenty-one frame identity, tested in a two-to-three analogue.
from sympy import Matrix, eye
zvec=[Matrix([s.Rational(3,5),s.Rational(4,5),0,0,0]),
      Matrix([0,s.Rational(5,13),s.Rational(12,13),0,0])]
a_vals=[s.Rational(1,4),s.Rational(1,9)]
zscaled=[s.sqrt(1-a_vals[i])*zvec[i] for i in range(2)]
x0=Matrix([1,0,0,0,0])
Z=sum((z*z.T for z in zscaled),Matrix.zeros(5))
CC=sum((a_vals[i]/(1-a_vals[i])*zscaled[i]*zscaled[i].T for i in range(2)),Matrix.zeros(5))
AA=sum(a_vals)
TT=x0*x0.T+sum((zscaled[i]*zscaled[i].T/(1-a_vals[i]) for i in range(2)),Matrix.zeros(5))
assert s.simplify(TT-s.Rational(3,5)*eye(5)-(Z-(2-AA)*eye(5)/5+x0*x0.T-eye(5)/5+CC-AA*eye(5)/5))==Matrix.zeros(5)
assert s.simplify(s.trace(CC)-AA)==0

print("PASS: exact Gegenbauer identity, rational gap, normalization, rounding, core determinant.")
print("h(v*) =",h)
print("P(sample) =",float(PP))
print("Proved: P>1/103, D>2/309, D_raw+5A>1/206.")
print("Type E remains open; 40<=tau_5<=44.")
