#!/usr/bin/env python3
"""Exact rational high-center Type-E checks; does not rerun upstream atlases."""
from fractions import Fraction as F
D=lambda x:196*x-644*x*x+896*x**3-448*x**4
E=lambda s:F(10)+F(35,64)*(5*s-32)**2
n=lambda s:7*(7-s)*(1-4*(7-s))
Dx2=F(2509,6400)
Amax=F(383,504)
sd=F(6961,1000)
xcap=F(1,400)
assert D(F(2,1000))<Dx2<D(F(2094,1000000))
assert F(2094,1000000)<xcap
for x in [F(0),xcap,F(1,250),F(1,2),Amax,F(1)]:
    y=x*(1-x)
    assert D(x)==28*y*(7-16*y)
assert D(F(1,2))==21
assert D(Amax)>D(F(1,250))>D(xcap)>Dx2
# E+n is increasing on [sd,7]: its decreasing derivative
# has minimum 301/32 at s=7.
assert F(175,32)*(5*7-32)-7==F(301,32)>0
assert E(F(7))+Dx2>15
# Atlas-free scalar exclusion x>=1/250, s>=6933/1000.
sg=F(6933,1000)
gap=D(F(1,250))+E(sg)+n(sg)-15
assert gap==F(1090526187,1000000000000)>0
# Atlas-dependent high-center exclusion x>=x2, s>=sd.
R=15-Dx2-E(sd)-n(sd)
N0=15-Dx2-E(sd)
Dupper=15-E(sd)-n(sd)
assert R==F(4782757,64000000)<F(7,90)<F(5,64)
assert N0==F(156233,512000)<F(21,64)
assert Dupper==F(29872757,64000000)<D(xcap)
# Hence x<xcap by concavity of y and D(y).
assert F(1,8)-xcap/2>0
assert 2*xcap<(F(1,8)-xcap/2)**2
assert 4*xcap<F(1,64)
Gerr=F(81,1078)*R+xcap*xcap
atlas=F(158207437,26950000000)
assert Gerr==F(55404931,9856000000)<atlas<F(1,169)
F3err=F(81,1078)*R
assert F3err==F(55343331,9856000000)<F(1,64)
J=F(4,21)*N0
assert J==F(22319,384000)
assert 4*J<4*sd-27 and 4*J<29-4*7
assert J+(7-sd)<F(3,4)
center=J/4+J*J/6
assert center==F(13353881761,884736000000)<F(1,64)
print("PASS exact scalar exclusion: x>=1/250, s>=6933/1000")
print("PASS exact high-center atlas thresholds: x>=x2, s>=6961/1000")
print("Rmax",R,"N0max",N0,"Gerr",Gerr,"center",center)
print("CONDITIONAL: upstream resource, signed-Gram/ADE/extension atlases not rerun")
print("GLOBAL PROVED RANGE UNCHANGED: 40<=tau_5<=44")
