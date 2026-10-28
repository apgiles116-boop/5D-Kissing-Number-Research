"""Exact rational regression for the 2026-10-28 center-quantized Type-E KKT note.

The analytic Cauchy, convexity and derivative arguments are in the .md note.
This script checks the exact polynomial, root brackets, derivative constants,
branch separation and the near-integrality counting threshold.
"""
from fractions import Fraction as F
import sympy as S

x,d=S.symbols("x d",real=True)
D=lambda t:196*t-644*t**2+896*t**3-448*t**4
Dp=S.diff(D(x),x)
B=F(2595,256)
n=7*d*(1-4*d)
q=d-F(1,5)
a=F(5,7)+F(5,12)*q
E=F(175,24)*q*q+F(147,4)*(a+n/28)**2
g=S.factor(E+n-F(955,64))
assert S.expand(g-F(7,4)*d*(d+1)*(21*d*d-49*d+20))==0
assert S.expand(S.diff(g,d)-F(7,2)*(42*d**3-42*d**2-29*d+10))==0
assert S.simplify(E.subs(d,0)-F(955,64))==0

xc0,xc1=F(399,10**6),F(400,10**6)
c00,c01=F(57184,10**6),F(57185,10**6)
cc0,cc1=F(56886,10**6),F(56887,10**6)
d0,d1=F(2239,10**6),F(2240,10**6)
def bracket(fn,lo,hi,target):
    assert fn(lo)<target<fn(hi)
bracket(D,xc0,xc1,F(5,64))
bracket(D,c00,c01,F(43,3)-B/2)
bracket(D,cc0,cc1,F(43,3)-(B+F(5,64))/2)
bracket(lambda t:g.subs(d,t),d0,d1,F(5,64))

# Monotone D' and c' rational enclosures in the tiny KKT rectangle.
assert Dp.subs(x,F(1,2000))>195
assert Dp.subs(x,F(29,500))>129
assert Dp.subs(x,F(7,125))<133
assert F(196,2*129)<F(19,25)
assert F(1,5)<1-F(195,2*133)<F(3,10)
assert 2*F(1,2000)+2*F(29,500)*F(19,25)<F(1,10)
assert F(19,20)/195<F(3,448)

def frame_lower(xv,cv,dv):
    av=F(1,2)+xv+cv
    uv=F(1,8)+xv*xv+cv*cv
    h=F(1,2)-av/5-dv/2
    return 30-3*av+av*av/10-uv/2+F(5,8)*h*h

low_lower=frame_lower(xc1,cc1,F(0))
high_upper=frame_lower(F(0),c00,d0)
high_lower=frame_lower(F(0),c01,d1)
assert low_lower>F(283894,10000)
assert high_upper<F(283892,10000)
assert high_lower>F(283891,10000)
assert low_lower>high_upper

# At most five nondeep contacts can have rho>=1/20.
assert 6*F(21,4)*F(1,20)**2>F(5,64)
assert F(4,21)*F(5,64)==F(5,336)
print("PASS: exact polynomial, KKT constants, branch ordering, contact count")
print("L_high rational enclosure:",float(high_lower),float(high_upper))
print("L_low rational lower:",float(low_lower))
