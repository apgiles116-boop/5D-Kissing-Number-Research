#!/usr/bin/env python3
"""Exact rational checks for conditional Type-E residual-center quantization.

Uses only Python standard library. Upstream Type-E mass/harmonic certificates,
conditional near-seven exclusion, and retained L'(x)>27/56 are NOT recertified.
"""
from fractions import Fraction as R

D=lambda t:196*t-644*t*t+896*t**3-448*t**4
Dp=lambda t:196-1288*t+2688*t*t-1792*t**3
E=lambda s:10+R(35,64)*(5*s-32)**2
n=lambda s:7*(s-R(27,4))*(1-4*(s-R(27,4)))
B=R(2595,256)
s0=R(209,30)
xhi=R(2094,1000000)
xfar=R(1,250)
chi=R(111271,2000000)
cfar=R(5427,100000)
sfar=R(69561,10000)
Qfloor=R(709911,25000)

def target_c(x):
    return R(43,3)-(B+D(x))/2

def F(x,c,s):
    a=R(1,2)+x+c
    u=R(1,8)+x*x+c*c
    h=4-a/5-s/2
    return 30-3*a+a*a/10-u/2+R(5,8)*h*h

assert E(s0)==R(33155,2304)
assert n(s0)==R(91,450)
assert 15-E(s0)-n(s0)==R(23477,57600)
assert D(xhi)>R(23477,57600) # x1<xhi

# .054<c(x)<.06 for 0<=x<=.004, and derivative bounds.
assert D(R(3,50))>target_c(R(0))
assert D(R(27,500))<target_c(xfar)
assert Dp(xfar)>190
assert Dp(R(27,500))<135
assert Dp(R(3,50))>128
assert 1-R(196,256)==R(15,64)
assert 1-R(190,270)==R(8,27)

# On 6.9<=s<=s0, h>3/8, h<1/2, -2<F_x<0.
assert 4-R(57,100)/5-s0/2>R(3,8)
assert 4-R(1,2)/5-R(69,10)/2<R(1,2)
assert (-3+R(57,100)/5)*R(15,64)+R(3,50)*R(49,64)<0
assert -R(25,8)*R(1,2)-xfar>-2

Ep=lambda s:R(175,32)*(5*s-32)
np=lambda s:7*(1-8*(s-R(27,4)))
assert Ep(R(69,10))+np(s0)>0
assert Ep(s0)<16 and np(R(69,10))<0
assert -2+R(15,64)*R(190,16)>0

# Rational lower bound at x1 and at the far-region threshold.
assert D(chi)>target_c(xhi)
assert F(xhi,chi,s0)>Qfloor
assert D(cfar)>target_c(xfar)
assert D(xfar)+E(sfar)>15
assert F(xfar,cfar,sfar)>Qfloor
assert D(xfar)+E(R(69,10))+n(R(69,10))<15
assert F(xfar,cfar,R(69,10))>Qfloor

# Retained F3 six-core squared-correlation caps.
assert Qfloor-R(473,256)==R(21239027,800000)
assert Qfloor-R(57,32)==R(2661519,100000)

# Sample exact checks of paired-center polynomial identity.
for p,q in [(R(0),R(1,2)),(R(1,20),R(1,3)),(R(1,7),R(1,8))]:
    tp,tm=p+q,p-q
    si=tp*tp+tm*tm
    lhs=7*(tp*tp*(1-4*tp*tp)+tm*tm*(1-4*tm*tm))
    rhs=7*(si*(1-2*si)-16*si*p*p+32*p**4)
    assert lhs==rhs

print("PASS: exact rational residual-center quantization certificate")
print("Conditional Q >",Qfloor,"=",float(Qfloor))
print("P1/P3 safe >",float(Qfloor-R(473,256)))
print("P2 safe >",float(Qfloor-R(57,32)))
print("Upstream mass/harmonic/atlas certificates are retained, not re-proved.")
