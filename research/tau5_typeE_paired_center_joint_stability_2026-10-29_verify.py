#!/usr/bin/env python3
"""Exact rational checker for 2026-10-29 conditional Type-E Q/stability theorem.
Does NOT recertify upstream mass/harmonic/atlas or large-x monotonicity."""
from fractions import Fraction as R
import sympy as sp

D=lambda x:196*x-644*x*x+896*x**3-448*x**4
Dp=lambda x:196-1288*x+2688*x*x-1792*x**3
s0=R(209,30); B0=R(2595,256); xfar=R(1,250); slo=R(69,10)
E=lambda s:10+R(35,64)*(5*s-32)**2
Ep=lambda s:R(175,32)*(5*s-32)
n2=lambda s:7*(s-R(13,2))*(1-2*(s-R(13,2)))
n2p=lambda s:7*(1-4*(s-R(13,2)))
target_c=lambda x:R(43,3)-(B0+D(x))/2
def F(x,c,s):
    a=R(1,2)+x+c
    u=R(1,8)+x*x+c*c
    h=4-a/5-s/2
    return 30-3*a+a*a/10-u/2+R(5,8)*h*h

assert E(s0)==R(33155,2304)
assert n2(s0)==R(49,225)
assert 15-E(s0)-n2(s0)==R(2509,6400)
xlo=R(2013442,10**9); xhi=R(2013443,10**9)
chi=R(55694237,10**9); floor=R(283965067,10**7)
assert D(xlo)<R(2509,6400)<D(xhi)
assert D(chi)>target_c(xlo)
assert F(xhi,chi,s0)>floor

clo=R(27,500); cu=R(3,50)
assert D(clo)<target_c(xfar) and D(cu)>target_c(R(0))
assert Dp(xfar)>190 and Dp(R(0))==196
assert Dp(cu)>128 and Dp(clo)<135
assert 1-R(196,256)==R(15,64)
assert 1-R(190,270)==R(8,27)
assert 4-(R(1,2)+xfar+cu)/5-s0/2>R(2,5)
assert 4-R(1,2)/5-slo/2<R(1,2)
assert (-3+R(1,2)/5-R(1,2)/4)*R(8,27)-xfar > -1
assert (-3+R(57,100)/5)*R(15,64)+cu < -R(1,2)
assert R(5,8)*R(2,5)==R(1,4)
assert Ep(s0)<16 and n2p(slo)<0
assert -1+R(190,112)>R(2,3)
assert -R(1,4)+R(16,112)<-R(1,10)
assert R(1,2)/5+R(5,8)==R(29,40)

cfar=R(5427,100000); sfar=R(69561,10000)
assert D(cfar)>target_c(xfar)
assert D(xfar)+E(sfar)>15
assert F(xfar,cfar,sfar)>floor
assert F(xfar,cfar,slo)>floor
assert floor-R(473,256)==R(530977009,20000000)
assert floor-R(57,32)==R(266152567,10000000)

p,q=sp.symbols("p q",real=True)
si=2*(p*p+q*q)
lhs=7*((p+q)**2*(1-4*(p+q)**2)+(p-q)**2*(1-4*(p-q)**2))
rhs=7*(si*(1-2*si)-16*si*p*p+32*p**4)
assert sp.expand(lhs-rhs)==0
b,h=sp.symbols("b h",real=True)
assert sp.expand(sp.Rational(5,8)*(h+b)**2-sp.Rational(5,8)*h*h
                 -sp.Rational(5,4)*h*b-sp.Rational(5,8)*b*b)==0
print("PASS: exact rational paired-center/frame certificate")
print("Q >", floor, "=", float(floor))
print("safe P1/P3 >", floor-R(473,256))
print("safe P2 >", floor-R(57,32))
print("Upstream Type-E mass/harmonic/atlas inputs remain conditional.")
