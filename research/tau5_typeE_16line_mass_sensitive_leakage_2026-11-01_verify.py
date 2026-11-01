#!/usr/bin/env python3
from fractions import Fraction as Q
import sympy as sp
s=sp.symbols('s')
P2=(3*s**2-1)/2
P4=(35*s**4-30*s**2+3)/8
U2=4*s**2-1
U4=16*s**4-12*s**2+1
f=s**4-s**2/4
assert sp.expand(sp.Rational(7,60)+sp.Rational(17,42)*P2+sp.Rational(8,35)*P4-f)==0
assert sp.expand(sp.Rational(1,16)+U2/8+U4/16-f)==0
x=Q(11,400)
def H(d,B):
    alpha=Q(7,60) if d==3 else Q(1,16)
    M=15+(1-B)**4 if B<=1 else 14+(2-B)**4
    return alpha/2*(16-2*B+B*B/16)**2-Q(3,8)*M
def U(x,L):
    B=x+L
    return (Q(15,16)*B+Q(15,8)*L+x*L/2+Q(139,128)*L**2
            +x*L**2/16+Q(5,16)*L**3+L**4/16)
L3=Q(59,50)
L4=Q(429,1000)
assert x+L3==Q(483,400)<Q(5,4)
assert x+L4==Q(913,2000)<Q(1,2)
assert H(3,x+L3)-U(x,L3)==Q(2132463706807,786432000000000)>0
assert H(4,x+L4)-U(x,L4)==Q(315704614065217,131072000000000000)>0
assert -Q(7,60)*Q(27,2)*Q(59,32)+Q(3,2)<0
assert -Q(1,16)*15*Q(31,16)+Q(3,2)==-Q(81,256)<0
xy=L4*(L3-L4)
assert xy==Q(322179,1000000)
assert Q(81,131072)*xy**2==Q(8407743951321,131072000000000000)
assert Q(9,1024)*xy==Q(2899611,1024000000)
print("PASS: harmonic identities, rational leakage margins and conditional two-ray constants")