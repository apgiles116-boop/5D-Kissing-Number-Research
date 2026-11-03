#!/usr/bin/env python3
"""Exact rational certificate: 16 isolated Type-E projected vectors span R^5.
Fraction checks all rational gaps; SymPy checks two polynomial identities.
No numerical SDP, optimizer, or floating-point tolerance.
"""
from fractions import Fraction as F
from sympy import symbols, expand, simplify

A0 = F(383, 504)
E0 = F(9, 50)
M2 = 3*F(1,16) + F(5,504)**2
B0 = A0 + E0
q0 = F(1,4) + E0
V0 = M2 + E0/F(2) + E0**2
C0 = F(1,8) + (6-F(3,2)*q0)/B0
K0 = 5+B0/2
R = 8-2*B0+B0**2/2 -K0*V0+C0*V0**2
U = F(15,4)*A0+13*E0+F(19,4)*E0**2+F(5,2)*E0**3+E0**4/2
gap = R-U

assert B0 < 2 and q0 < 1 and C0 > 0
assert F(49,256)-M2 == F(3869,1016064) > 0
assert K0-2*C0*V0 == F(13989845831977,7520778720000) > 0
assert gap == F(32005920115782093751,477599531834880000000) > 0

B,U2,U3,U4 = symbols('B U2 U3 U4')
Fraw = (16-2*B+U2)**2/8 - F(3,2)*(16-4*B+6*U2-4*U3+U4)
Fexp = 8-2*B+B**2/2-(5+B/2)*U2+U2**2/8+6*U3-F(3,2)*U4
assert simplify(Fraw-Fexp)==0

s,t,u = symbols('s t u')
K2 = 4*t*u*s**2-t**2*u**2
K4 = 16*s**4-12*t*u*s**2+t**2*u**2
assert expand(K4/4+K2/2-(4*s**4-t*u*s**2-t**2*u**2/4))==0

print('A0=',A0,'M2=',M2,'E0=',E0)
print('B0=',B0,'q0=',q0,'V0=',V0,'C0=',C0,'K0=',K0)
print('quadratic derivative margin=',K0-2*C0*V0)
print('quartic lower R=',R,'~',float(R))
print('safe-pair upper U=',U,'~',float(U))
print('strict rational contradiction gap=',gap,'~',float(gap))
print('PASS: lambda_min(Z_isolated_16)>9/50 under stated hypotheses.')
