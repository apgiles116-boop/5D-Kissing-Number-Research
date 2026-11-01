#!/usr/bin/env python3
"""Exact checks for the 21-line quartic-defect theorem E>1/64.
Analytic harmonic-positivity and rounding arguments are in the proof note.
"""
from fractions import Fraction as F
import sympy as s
x=s.symbols("x", real=True)
P2=(5*x*x-1)/4
P4=(21*x**4-14*x*x+1)/8
assert s.expand(F(1,28)+P2/3+8*P4/21-(x**4-x*x/4))==0
E0=F(1,64); t0=F(27,1000)
assert 4*E0+F(1,8)==F(3,16)<F(7,20)
assert F(3,20)>F(1,8)
assert F(40,3)*t0==F(9,25)
assert F(27,2000)+F(3,40)==F(177,2000)>F(7,80)
assert F(93,10)**2>F(21,5)**2*F(24,5)
assert F(40,3)/16>F(9,10)**2
assert F(33,200)**2>t0
assert F(42,5)*F(33,200)+t0+F(3,8)==F(447,250)<F(9,5)
for k in range(21):
    assert abs(F(16,5)-F(k,4))>=F(1,20)+F(3,20)*(13-k)
assert 21*F(1,20)+F(3,20)*(21*13-268)==F(9,5)
assert F(2,3)*E0==F(1,96)
print("PASS: polynomial identity, rounding, degree, and rational margins")
