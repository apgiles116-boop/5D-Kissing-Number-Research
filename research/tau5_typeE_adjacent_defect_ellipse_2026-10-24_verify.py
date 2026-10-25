#!/usr/bin/env python3
"""Exact rational certificate for Type-E adjacent-defect ellipse consequences.
The geometric Cauchy proof is in the accompanying markdown note.
"""
from fractions import Fraction as F
from sympy import sqrt, simplify, Rational

B=F(383,504)
D=F(1780062775,4032758016)
F0=F(8790283,317520)
C0=F(133562881183,362948221440)
GOAL=F(12,125)
t=(sqrt(15)-3)/4
assert simplify(t*t+Rational(3,2)*t-Rational(3,8))==0
assert float(B/2)<float(2*t)
assert F(1,4)<D<F(1,2)

# x=max defect. For x<=.216 use sum delta^2<=x D.
x0=F(27,125)
assert x0*D<GOAL
# For .216<x<=.219, capped simplex has two x's and one remainder.
x1=F(219,1000)
assert D>2*x1 and D<3*x0 and x0>D/3
assert 2*x1*x1+(D-2*x1)**2<GOAL

intervals=[
 (F(219,1000),F(11,50),F(27,125)),
 (F(11,50),F(223,1000),F(1061,5000)),
 (F(223,1000),F(9,40),F(101,500)),
 (F(9,40),F(23,100),F(97,500)),
 (F(23,100),F(6,25),F(87,500)),
 (F(6,25),F(1,4),F(7,50)),
]
for lo,hi,cap in intervals:
    # Adjacent and disjoint defect caps at left endpoint:
    assert cap*cap>F(3,8)*(1-4*lo)
    assert cap>B/2-lo
    # Other five defects have total R in [cap,2cap].
    assert cap<D-hi and D-lo<2*cap
    # Capped simplex: one cap and one remainder.
    bound=hi*hi+cap*cap+(D-lo-cap)**2
    assert bound<GOAL, (lo,hi,cap,bound)

old_square=F(1,16)+(D-F(1,4))**2
assert GOAL<old_square
core=F(3,2)+D+GOAL
safe=F0-core
assert core==F(1027043071067,504094752000)
assert safe==F(12928410219733,504094752000)
old_safe=F0-(F(13,8)+D/2+D*D)
assert safe>old_safe and safe>F(409,16)

print("PASS: exact rational six-core square-budget certificate")
print("t* =",t,"~",float(t))
print("sum core delta^2 <",GOAL)
print("S_core <",core,"~",float(core))
print("S_safe >",safe,"~",float(safe))
print("retained W norm^2 ceiling =",C0)
