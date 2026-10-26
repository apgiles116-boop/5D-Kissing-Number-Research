"""Exact arithmetic verification for Type-E center-frame bridge (2026-10-26)."""
from fractions import Fraction as F
from itertools import product
import sympy as sp

t = sp.symbols('t')
P2 = (5*t*t-1)/4
P4 = (21*t**4-14*t*t+1)/8
assert sp.expand(t**4-t*t/4-(sp.Rational(1,28)+P2/3+sp.Rational(8,21)*P4)) == 0

a = F(1,40)
K = (17+(1+a)**2*(7+a))/(16*(1-a)**2)
assert K == F(1560361,973440)
assert 24*K*a == F(1560361,1622400)
assert F(99,100)**2-24*K*a == F(743831,40560000)>0
Vfloor = F(24,25)**2/5
assert Vfloor == F(576,3125)
Sfloor = 30-3*a-F(2,5)*a*a+Vfloor/2
assert Sfloor == F(3001691,100000)>30

vals=[F(-1,4),F(-1,8),F(0),F(1,8),F(1,4)]
pos=lambda q:max(F(0),q)
n=0
for ai,aj in product([F(0),F(1,20),F(1,10),F(1,4)],repeat=2):
    w=(1-ai)*(1-aj)
    for M,Z,X,Y in product(vals,repeat=4):
        if abs(M+Z)+abs(X+Y)>F(1,2): continue
        if abs(M-Z)+abs(X-Y)>F(1,2): continue
        if Z*Z>w: continue
        rho=abs(M)+abs(abs(X)-abs(Y))
        assert rho+abs(Z)<=F(1,2)
        s=Z*Z/w
        assert pos(s*(s-F(1,4)))<=pos(ai+aj-ai*aj-4*rho+4*rho*rho)/(16*w*w)
        n+=1

m=0
for ai in [F(0),F(1,20),F(1,10),F(1,4)]:
    for r,z in product(vals,repeat=2):
        if abs(r)+abs(z)>F(1,2): continue
        s=z*z/(1-ai)
        assert pos(s*(s-F(1,4)))<=pos(ai-4*abs(r)+4*r*r)/(16*(1-ai)**2)
        m+=1

A,B,V=sp.symbols('A B V')
assert sp.expand((20-A)**2/5+V-(20-2*A+B)-2*(30-3*A+A*A/10-B/2+V/2))==0
print('PASS: Gegenbauer, frame identity, exact fractions,',n,'safe and',m,'center cases')
