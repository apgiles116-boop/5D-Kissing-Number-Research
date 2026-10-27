#!/usr/bin/env python3
"""Exact arithmetic tests; harmonic PSD is proved via addition theorem in the note."""
from fractions import Fraction as F
import sympy as s

z = [s.Matrix([s.Rational(((i+2*j)%7)-3,9+j) for j in range(5)])
     for i in range(20)]
x = s.Matrix([s.Rational(3,5),s.Rational(4,5),0,0,0])
r = [v.dot(v) for v in z]
R2 = sum((v*v for v in r),s.Integer(0))
S4 = sum((v**4 for v in r),s.Integer(0))
Fr = sum((ri*vi*vi.T for ri,vi in zip(r,z)),s.zeros(5))
W = s.trace((Fr-R2*s.eye(5)/5)**2)
D = sum(((z[i].dot(z[j]))**2*
         ((z[i].dot(z[j]))**2-r[i]*r[j]/4)
         for i in range(20) for j in range(i+1,20)),s.Integer(0))

def h4(v,w):
    q=v.dot(w); rv=v.dot(v); rw=w.dot(w)
    return q**4-s.Rational(2,3)*rv*rw*q*q+rv**2*rw**2/21

K=sum((h4(vi,vj) for vi in z for vj in z),s.Integer(0))
h=sum((h4(x,vi) for vi in z),s.Integer(0))
assert s.expand(D-(R2**2/56-s.Rational(3,8)*S4+
                   s.Rational(5,24)*W+K/2))==0
assert K>=0 and s.Rational(8,21)*K>=h*h
assert all(abs(x.dot(vi))<=s.Rational(1,2) for vi in z)
t0=sum(((x.dot(vi))**2 for vi in z),s.Integer(0))
tr=sum((ri*(x.dot(vi))**2 for ri,vi in zip(r,z)),s.Integer(0))
q=s.Rational(2,3)*tr-t0/4-R2/21
lower=R2**2/56-s.Rational(3,8)*S4+\
      s.Rational(25,96)*(tr-R2/5)**2+\
      s.Rational(21,16)*max(q,s.Integer(0))**2
assert D>=lower

A=F(383,504); b=A-F(3,4)
phi=F(3,16)+b*b
new=F(30)-3*A+A*A/10-phi/2
old=F(17456771,635040)
assert b==F(5,504)
assert phi==F(47653,254016)
assert new==F(8790283,317520)
assert new-old==F(131,672)
for k in range(4):
    lo=F(k,4); hi=min(A,F(k+1,4))
    if hi>=lo:
        assert -3+hi/5<0
print("PASS: raw harmonic identity, center inequality, and exact improved floor")
print("new floor =",new,"improvement =",new-old)
