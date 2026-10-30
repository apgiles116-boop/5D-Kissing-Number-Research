#!/usr/bin/env python3
"""Exact rational checks for Type-E critical Q-gap and five-well Walsh theorem.
Does NOT rerun upstream tensor/harmonic or signed-Gram/D5 finite atlases.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

D=lambda x:196*x-644*x*x+896*x**3-448*x**4
E=lambda s:F(10)+F(35,64)*(5*s-32)**2
f=lambda t:7*t*t*(1-4*t*t)
s0=F(209,30); x2hi=F(2094,1000000); Dx2=F(2509,6400)
eps=F(1,1440)
R=112*eps
x=x2hi+F(3,2)*eps
smin=s0-10*eps
N0=15-Dx2-E(smin)
assert D(F(2,1000))<Dx2<D(x2hi)
assert Dx2+E(s0)+7*(s0-F(13,2))*(1-2*(s0-F(13,2)))==15
assert R==F(7,90) and R<F(5,64)
assert x==F(9407,3000000) and x<F(1,256)
assert smin==F(5011,720)
assert N0==F(10773469,33177600) and N0<F(21,64)
assert f(F(1,9))>F(5,64) and f(F(12,25))>F(5,64)
assert F(12,25)-F(1,9)==F(83,225)>F(1,4)
assert F(1,8)-x/2>0 and 2*x<(F(1,8)-x/2)**2
Gerr=F(81,1078)*R+x*x
old=F(158207437,26950000000)
assert Gerr==F(4056813856973,693000000000000)
assert Gerr<old<F(1,169)
assert F(81,1078)*R<F(1,64)
J=F(4,21)*N0
assert J==F(1539067,24883200) and J<F(1,16)
assert 4*J<F(1,4) and 28-4*smin<F(1,4)
d=7-s0
assert d==F(1,30) and J+7-smin<F(3,4)
center=(J-d)/4+(J+d)**2/6
assert center==F(32096511258649,3715041853440000)
assert center<F(1,64)

wells={F(j,16) for j in range(5)}
for t in product([F(j,16) for j in range(-8,9)],repeat=4):
    W=sum(v*v for v in t)/4
    b=F(1,4)-W
    k=(16*b).__floor__()
    r=b-F(k,16)
    mass=sum(f(v) for v in t)
    eta=min(abs(W-w) for w in wells)
    assert mass>=28*r*(1-16*r)>=14*eta
for k in range(4):
    for r in [F(0),F(1,256),F(1,128),F(1,64),F(1,32),F(1,16)]:
        ds=[F(1,4)]*k+[4*r]+[F(0)]*(3-k)
        assert sum(ds)/4==F(k,16)+r
        assert sum(28*d*(F(1,4)-d) for d in ds)==28*r*(1-16*r)

states=defaultdict(set)
for t in product([F(-1,2),F(0),F(1,2)],repeat=4):
    p=sum(t)/4
    b=(t[0]+t[1]-t[2]-t[3])/4
    c=(t[0]-t[1]+t[2]-t[3])/4
    h=(t[0]-t[1]-t[2]+t[3])/4
    W=sum(v*v for v in t)/4
    assert p*p+b*b+c*c+h*h==W
    assert W in wells and sum(f(v) for v in t)==0
    states[abs(h)].add(W)
assert dict(states)=={
    F(0):{F(0),F(1,8),F(1,4)},
    F(1,8):{F(1,16),F(3,16)},
    F(1,4):{F(1,8),F(1,4)},
    F(3,8):{F(3,16)},
    F(1,2):{F(1,4)}
}
print("PASS exact rational critical Q-gap 1/1440")
print("PASS new center H-L refinement and 16-line atlas thresholds")
print("PASS 17^4 safe four-contact grid, sharp extremizers, 81 zero-slack states")
print("NOT RERUN upstream tensor/harmonic, rank atlas, ADE and D5 extension certificates")
print("STATUS conditional critical rectangle only; 40<=tau_5<=44")
