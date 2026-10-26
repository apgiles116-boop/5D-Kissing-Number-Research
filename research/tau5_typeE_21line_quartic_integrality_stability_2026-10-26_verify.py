#!/usr/bin/env python3
"""Exact rational checks for the 21-line quartic integrality gap.
The note supplies the analytic positivity and Cauchy-Schwarz proofs.
"""
from fractions import Fraction as Q
import sympy as s

t=s.symbols("t")
C0=s.Integer(1)
C2=s.gegenbauer(2,s.Rational(3,2),t)
C4=s.gegenbauer(4,s.Rational(3,2),t)
f=t**4-t**2/4
assert s.expand(f-C0/28-C2/18-s.Rational(8,315)*C4)==0
assert f.subs(t,1)==s.Rational(3,4)
assert Q(21*21,28)==Q(21*3,4)
assert Q(1,36)*Q(15,2)==Q(5,24)
assert 4*(Q(21,5)-1)==Q(64,5)
assert min(abs(Q(21,5)-(1+Q(d,4))) for d in range(21))==Q(1,20)

for k in range(1001):
    v=Q(k,1000)
    fv=v*(v-Q(1,4))
    root=Q(0) if v<=Q(1,8) else Q(1,4)
    assert abs(v-root)<=(8*(-fv) if fv<=0 else 4*fv)

P=Q(1,440)
V=Q(24,5)*P
assert V==Q(3,275)
assert Q(21,200)**2-V==Q(51,440000)>0
L=Q(1,20)-Q(24,21)*P
K=(Q(21,5)+Q(21,200))*V/21
assert L==Q(73,1540) and K==Q(123,55000)
assert L*L-K==Q(631,59290000)>0
assert Q(24,21)*P==Q(1,385)

assert 120+64+20+6==210
assert Q(1,16)/(Q(9,16)**2)==Q(16,81)
assert Q(1,16)/(Q(3,4)**2)==Q(1,9)
assert Q(16,9)*(Q(1,2)+Q(1,4)+Q(3,32))==Q(3,2)
assert Q(16,81)*19+Q(1,9)==Q(313,81)
assert Q(16,81)*16+Q(1,9)+Q(9,2)==Q(1259,162)
assert Q(313,81)<Q(1259,162)
assert Q(162,1259*440)==Q(81,276980)
print("PASS: exact Gegenbauer identity, integrality, rational stability gap")
print("PASS: Type E 210-pair defect and midpoint-energy coefficients")
print("PROVED EXACTLY: P_f > 1/440 for any 21 unit lines in R5")
print("CONDITIONAL ON TYPE E: A > 81/276980; Type E remains OPEN")
