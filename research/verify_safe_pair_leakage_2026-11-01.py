#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
from sympy import symbols, expand
z1=tuple(F(v,10) for v in (9,3,3,0,0))
z2=tuple(F(v,10) for v in (1,7,7,0,0))
m1=tuple(F(v,10) for v in (0,0,0,1,0))
m2=tuple(F(v,10) for v in (0,0,0,-1,0))
dot=lambda a,b:sum((x*y for x,y in zip(a,b)),F(0))
assert dot(z1,z2)==F(51,100)>F(1,2)
assert dot(m1,m2)==-F(1,100)
assert dot(z1,z1)==dot(z2,z2)==F(99,100)
assert dot(m1,z1)==dot(m2,z2)==0
for s,t in product((-1,1),repeat=2):
    a=tuple(u+s*v for u,v in zip(m1,z1))
    b=tuple(u+t*v for u,v in zip(m2,z2))
    assert dot(a,a)==dot(b,b)==1
    assert dot(a,b)<=F(1,2)
assert F(1,50)<F(11,400)
v=symbols('v')
P2=(3*v**2-1)/2
P4=(35*v**4-30*v**2+3)/8
U2=4*v**2-1
U4=16*v**4-12*v**2+1
assert expand(F(7,60)+F(17,42)*P2+F(8,35)*P4-(v**4-v**2/4))==0
assert expand(F(1,16)+F(1,8)*U2+F(1,16)*U4-(v**4-v**2/4))==0
def H(B,d):
    alpha=F(7,60) if d==3 else F(1,16)
    M=15+(1-B)**4 if B<=1 else 14+(2-B)**4
    return alpha/2*(16-2*B+B*B/16)**2-F(3,8)*M
def U(B):
    return F(45,16)*B+F(139,128)*B**2+F(5,16)*B**3+B**4/16
for d,L,expected in [
    (3,F(93,80),F(43441740007,3072000000000)),
    (4,F(83,200),F(666696943297,209715200000000))
]:
    B=F(11,400)+L
    assert H(B,d)-U(B)==expected>0
print('PASS: exact counterexample, harmonic identities and repaired margins')
