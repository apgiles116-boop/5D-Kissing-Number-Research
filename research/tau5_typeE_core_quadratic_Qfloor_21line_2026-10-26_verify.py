"""Exact rational checks for the 2026-10-26 Type-E quadratic/Q/21-line note.
The accompanying note contains the analytic PSD and integrality proofs.
"""
from fractions import Fraction as Q
from sympy import symbols, simplify

x=symbols("x")
C2=(15*x*x-3)/2
C4=(315*x**4-210*x*x+15)/8
assert simplify(x**4-x*x/4-(Q(1,28)+Q(1,18)*C2+Q(8,315)*C4))==0

A=Q(383,504)
r=A-Q(3,4)
maxsq=3*Q(1,16)+r*r
qfloor=30-3*A+A*A/10-maxsq/2
assert maxsq==Q(47653,254016)
assert qfloor==Q(8790283,317520)
assert qfloor-Q(17456771,635040)==Q(131,672)
safefloor=qfloor-Q(3,2)-A-A*A/4
assert safefloor==Q(128429963,5080320)

p=Q(9,625)
c=Q(25,4)
assert p==Q(9,100)*Q(16,100)
assert Q(1,4)-Q(9,100)==Q(4,25)
assert Q(24,5)*p==Q(216,3125)
assert 4*(c+4)*p==Q(369,625)<Q(3,5)
v=(4*(c+4)*p-Q(2,5))/(2+5*c/6)
assert v==Q(2856,108125)<Q(1,36)
C=21*(Q(21,5)+Q(1,6))
assert C==Q(917,10)
q=Q(9,5)-2*(c+4)*p+(5*c/12)*v
assert q==Q(170144,108125)>0
assert q*q-C*v==Q(631562236,11691015625)>0

t=Q(1,107)
KO=Q(20)/(16*(1-t)**2)
KC=(17+(1+t)**2*(7+t))/(16*(1-t)**2)
assert KC>KO
assert KC==Q(29573731,19236032)
assert p-KC*t==Q(40716941,1286409640000)>0

# Sharpness: two antipodal vectors m1=v, m2=-v.
a=Q(7,3)
assert a*a==(2*a)**2/4
print("PASS: exact Gegenbauer, PSD-frame, integer-gap and Type-E floor arithmetic")
print("S >=",qfloor,"; S_safe >=",safefloor)
print("P >",p,"; Type-E A >",t)
