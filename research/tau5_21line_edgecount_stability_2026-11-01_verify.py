#!/usr/bin/env python3
"""Exact rational verification of the 21-line edge-count stability constants."""
from fractions import Fraction as F
E0=F(27,2000)
G0=F(79,1000)
assert E0<F(1,64)
assert 1-64*E0==F(17,125)
assert 1-8*G0==F(46,125)
assert F(17,125)>F(46,125)**2
assert F(7,20)>4*E0+G0
assert F(3,20)-F(12,5)*E0>G0
tmax=F(3,4)*(4*E0+G0-F(1,10))
assert tmax==F(99,4000) and tmax<F(1,40)
assert F(3)<F(7,4)**2
upper=F(147,100)+F(1,40)+8*E0+2*G0
assert upper==F(1761,1000)<F(9,5)
assert F(2,3)*E0==F(9,1000)
assert E0>F(1,341)
print("PASS: exact 21-line edge-count and variance contradiction")
print("PASS: E>27/2000; linear excess >9/1000")
