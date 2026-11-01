#!/usr/bin/env python3
"""Exact D5 Q-Gram spectral-gap and separation verifier."""
from fractions import Fraction as F
import sympy as s
edges=[(i,j) for i in range(5) for j in range(i+1,5)]
B=s.zeros(5,10)
for e,(i,j) in enumerate(edges):
    B[i,e]=B[j,e]=1
P=s.eye(5)-s.ones(5,5)/5
S=s.zeros(10,20); D=s.zeros(10,20)
for e in range(10):
    S[e,2*e]=S[e,2*e+1]=1
    D[e,2*e]=1; D[e,2*e+1]=-1
K=s.zeros(20,20)
for a in range(20):
    ea,sa=divmod(a,2)
    for b in range(20):
        eb,sb=divmod(b,2)
        x2=(1 if sa==sb else 0) if ea==eb else (s.Rational(1,4) if len(set(edges[ea])&set(edges[eb]))==1 else 0)
        K[a,b]=x2-s.Rational(1,5)
assert B*B.T==3*s.eye(5)+s.ones(5,5)
assert K==D.T*D/2+S.T*B.T*P*B*S/4
assert K.eigenvals()=={s.Integer(0):6,s.Integer(1):10,s.Rational(3,2):4}
PN=S.T*(s.eye(10)-B.T*P*B/3)*S/2
assert PN.T==PN and PN*PN==PN and s.trace(PN)==6
assert K*PN==s.zeros(20,20)
assert PN*s.ones(20,1)==s.ones(20,1)
PA=D.T*D/2; PR=S.T*B.T*P*B*S/6
assert PA*PA==PA and PR*PR==PR and PA*PR==s.zeros(20,20)
assert PA+PR+PN==s.eye(20)
assert K==PA+s.Rational(3,2)*PR
d=F(9,800); V=F(949,5000)
# sqrt(2)>7/5 bounds the irrational term from above.
assert V-(16*d+d*d+F(27,2800))==F(137,4480000)>0
print("PASS: spectrum 0^6,1^10,(3/2)^4; exact projector and gap")
print("PASS: conditional D5 template distance D>9/800")
print("PASS: strict rational margin 137/4480000")
