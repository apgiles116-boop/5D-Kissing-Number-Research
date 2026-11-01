#!/usr/bin/env python3
"""Exact rational arithmetic checks for 2026-11-01 center-Q anisotropy.
Analytic proof in companion .md supplies universal quantifiers.
"""
from fractions import Fraction as F
D=lambda x:196*x-644*x*x+896*x**3-448*x**4
Dp=lambda x:196-1288*x+2688*x*x-1792*x**3
c=F(1245,256)
B=F(2595,256)
rlo,rhi=F(27143,10**6),F(27144,10**6)
slo,shi=F(39781,10**6),F(39782,10**6)
assert B+c==15
assert D(rlo)<c<D(rhi)
assert D(slo)<F(41,6)<D(shi)
assert Dp(F(68,1000))>120
assert rhi<F(28,1000) and shi<F(4,100)
# 8/sqrt(175) < 604744/10^6, exact by squaring.
h_upper=F(604744,10**6)
assert 175*h_upper*h_upper>64
q_upper=-F(4,5)+h_upper
assert q_upper==F(-195256,10**6)
f_lower=F(7,10)-shi/5-h_upper/2
assert f_lower==F(974179,2500000)
V_lower=F(5,4)*f_lower*f_lower
assert V_lower==F(949024724041,5000000000000)
assert V_lower-F(949,5000)==F(24724041,5000000000000)>0
# f' <= r/(5c)-16/(875h) <0 throughout 0<=Xi<=c.
assert rhi/(5*c)<F(14,10000)
assert h_upper<F(61,100)
assert F(14,10000)<F(16,875)/F(61,100)
# Lower Lstar from upper root brackets (scalar expression decreasing).
A_hi=F(1,2)+rhi+shi
L_lo=30-3*A_hi+A_hi*A_hi/10-(F(1,8)+rhi*rhi+shi*shi)/2
assert L_lo>F(282677,10000)
C_floor=F(282677,10000)+F(949,10000)
assert C_floor==F(283626,10000)
raw_hi=F(441401,1000000)
raw_exact=F(1780062775,4032758016)
assert raw_exact<raw_hi
safe_floor=C_floor-F(3,2)-raw_hi-raw_hi*raw_hi
assert safe_floor==F(26226364157199,10**12)
assert safe_floor>F(41,4)+F(143,9)
assert safe_floor<F(42,4)+F(142,9)
# ||uu^T-I/5||_F^2=4/5.
assert 1-F(2,5)+F(1,5)==F(4,5)
print("PASS: exact D-root brackets, radical bound, Q anisotropy,")
print("      slack monotonicity, safe squared mass and 42-count.")
print("V_z >",F(949,5000))
print("C_z >",C_floor)
print("safe mass >",safe_floor)
