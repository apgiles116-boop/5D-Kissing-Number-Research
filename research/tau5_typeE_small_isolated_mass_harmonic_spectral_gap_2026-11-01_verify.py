#!/usr/bin/env python3
"""Exact checks for 2026-11-01 Type-E isolated-mass spectral theorem.
Upstream graph/harmonic/wedge lemmas are retained inputs, not checked here.
"""
from fractions import Fraction as Q
from sympy import symbols, expand, Rational
t=symbols("t")
P2=(3*t*t-1)/2;P4=(35*t**4-30*t*t+3)/8
U2=4*t*t-1;U4=16*t**4-12*t*t+1
f=t**4-t*t/4
assert expand(f-(Rational(7,60)+Rational(17,42)*P2+Rational(8,35)*P4))==0
assert expand(f-(Rational(1,16)+Rational(1,8)*U2+Rational(1,16)*U4))==0
D=lambda a:196*a-644*a*a+896*a**3-448*a**4
x=Q(11,400);c=Q(1245,256)
assert D(x)-c==Q(23228613,400000000)
assert Q(415,7168)<Q(1,4)
def H(d,B):
 alpha=Q(7,60) if d==3 else Q(1,16)
 M=Q(15)+(1-B)**4 if B<=1 else Q(14)+(2-B)**4
 return alpha/2*(16-2*B+B*B/16)**2-Q(3,8)*M
def U(B,L):
 return Q(15,16)*B+Q(45,16)*L+Q(293,256)*L**2+Q(5,16)*L**3+L**4/16
L3=Q(531,500);B3=x+L3
L4=Q(73,200);B4=x+L4
assert B3==Q(2179,2000) and B3<Q(11,10)
assert B4==Q(157,400) and B4<Q(2,5)
assert H(3,B3)-U(B3,L3)==Q(1042276961532727,491520000000000000)>0
assert H(4,B4)-U(B4,L4)==Q(843766658257,209715200000000)>0
assert -Q(7,60)*Q(69,5)*Q(149,80)+Q(3,2)==-Q(11989,8000)<0
assert -Q(1,16)*Q(76,5)*Q(39,20)+Q(3,2)==-Q(141,400)<0
xy=L4*(L3-L4)
assert xy==Q(50881,200000)
minor=Q(81,131072)*xy**2
assert minor==Q(209698969041,5242880000000000)
assert Q(9,1024)*xy==Q(457929,204800000)
print("PASS: harmonic expansions, isolated mass, spectral margins, tomography fractions")
print("3D margin",H(3,B3)-U(B3,L3))
print("4D margin",H(4,B4)-U(B4,L4))
