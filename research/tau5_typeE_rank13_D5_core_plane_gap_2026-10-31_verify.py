#!/usr/bin/env python3
"""Exact audit of conditional D5 rank-13 core-plane and sign-parity theorem."""
from fractions import Fraction as F
from itertools import combinations
from sympy import sqrt, simplify, Rational, zeros, eye

assert 19998>141**2
assert F(3,2)**2>2
assert F(18,25)-F(101,141)-F(3,1000)==F(97,141000)>0
assert 579>24**2
assert F(478,625)-F(383,504)==F(1537,315000)>0
assert simplify(2*(sqrt(2)-1)-Rational(383,504))>0
print("PASS: exact margins and boundary inequality")

supports=list(combinations(range(5),2))
roots=[(s,t) for s in supports for t in (-1,1)]
count=0
for missing in supports:
    full={(missing,-1),(missing,1)}
    for extra in combinations([r for r in roots if r not in full],2):
        if extra[0][0]==extra[1][0]: continue
        remaining=set(roots)-full-set(extra)
        assert len(remaining)==16
        assert all(any((s,t) in remaining for t in (-1,1))
                   for s in supports if s!=missing)
        count+=1
assert count==1440
print("PASS: all 1440 rank-13 D5 support patterns")

removed={((0,1),-1),((0,1),1),((0,2),1),((0,3),-1)}
S=zeros(5); S[0,1]=S[1,0]=1
for (i,j),sign in roots:
    if ((i,j),sign) in removed: continue
    v=zeros(5,1);v[i]=1;v[j]=sign
    Q=v*v.T/2-eye(5)/5
    assert simplify(sum(S[k,l]*Q[k,l] for k in range(5) for l in range(5)))==0
print("PASS: exact rank-two missing-Q direction")

x=F(13,20);w=2*x*x;B=2*x**4;tt=2*x**4;h=F(1,4)-B
assert w==F(169,200) and -tt<=h<tt
for mask in range(8):
    signs=[1 if mask&(1<<i) else -1 for i in range(3)]
    assert not all(B+signs[i]*signs[j]*tt<=F(1,4)
                   for i,j in combinations(range(3),2))
print("PASS: forced K3 sign graph impossible")

t=[F(1,7),F(2,9),F(3,11),F(4,13)]
for mask in range(16):
    signs=[1 if mask&(1<<i) else -1 for i in range(4)]
    T=sum(signs[i]*t[i] for i in range(4))**2
    U=sum(signs[i]*signs[j]*t[i]*t[j] for i,j in combinations(range(4),2))
    assert T-2*U==sum(v*v for v in t)
print("PASS: all 16 sign choices cancel from V-2Q6")
print("Type E OPEN; global 40<=tau5<=44")
