#!/usr/bin/env python3
"""Exact rational certificate for the isolated-16 quartic frame theorem.
Fraction handles the rational certificate; SymPy audits polynomial identities.
No numerical SDP, tolerance or optimizer.
"""
from fractions import Fraction as F
from sympy import symbols, expand, simplify

A0 = F(383, 504)
E0 = F(133, 1000)
M2 = 3*F(1,16) + F(5,504)**2
B0 = A0 + E0
q0 = F(1,4) + E0
V0 = M2 + E0/F(2) + E0**2
C0 = F(1,8) + (6-F(3,2)*q0)/B0
K0 = 5+B0/2
R = 8-2*B0+B0**2/2 -K0*V0+C0*V0**2
U = (1+E0)**2/F(4)*(15*A0+45*E0+2*E0**2)
gap = R-U

assert B0 < 2
assert q0 < 1
assert C0 > 0
assert 2*C0*V0 < K0
assert gap == F(35049611975917149533, 88616706809400000000000)
assert gap > 0

# Verify the sixteen-vector quartic expansion.
B, U2, U3, U4 = symbols('B U2 U3 U4')
Fraw = (16-2*B+U2)**2/8 - F(3,2)*(16-4*B+6*U2-4*U3+U4)
Fexp = 8-2*B+B**2/2-(5+B/2)*U2+U2**2/8+6*U3-F(3,2)*U4
assert simplify(Fraw-Fexp)==0

# Verify the Gegenbauer kernel decomposition.
s,t,u = symbols('s t u')
K2 = 4*t*u*s**2 - t**2*u**2
K4 = 16*s**4 -12*t*u*s**2+t**2*u**2
assert expand(K4/4+K2/2-(4*s**4-t*u*s**2-t**2*u**2/4))==0

print('A0=',A0,'M2=',M2)
print('E0=',E0,'B0=',B0,'q0=',q0,'V0=',V0)
print('C0=',C0,'K0=',K0)
print('derivative margin=',K0-2*C0*V0)
print('quartic lower R=',R)
print('pair upper U=',U)
print('strict rational gap=',gap,'~',float(gap))
print('PASS: lambda_min(Z_isolated_16)>133/1000 under the stated hypotheses.')
