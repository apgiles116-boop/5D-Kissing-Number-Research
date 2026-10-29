#!/usr/bin/env python3
"""Exact Fraction verifier for conditional Type-E A>1/86."""
from fractions import Fraction as F
from itertools import combinations

EDGES = {frozenset(edge) for edge in ((0,2),(0,4),(0,5),(1,4),(1,7),
                                       (2,3),(2,7),(3,6),(5,6),(5,7))}
def matchings(vertices):
    if not vertices:
        yield ()
        return
    v = min(vertices)
    for w in vertices - {v}:
        if frozenset((v,w)) in EDGES:
            for rest in matchings(vertices - {v,w}):
                yield ((v,w),) + rest

M = list(matchings(set(range(8))))
assert len(M) == 3, M
for matching in M:
    deep_core = []
    for i,j in combinations(range(4),2):
        a,b = matching[i]
        c,d = matching[j]
        pairs = [((a,c),+1), ((a,d),-1), ((b,c),-1), ((b,d),+1)]
        deep = [sgn for (v,w),sgn in pairs if frozenset((v,w)) in EDGES]
        safe = [sgn for (v,w),sgn in pairs if frozenset((v,w)) not in EDGES]
        assert safe.count(+1)>=2 or safe.count(-1)>=2
        if deep:
            assert len(set(deep)) == 1
            deep_core.append((i,j))
    assert len(deep_core) in (5,6)
    degrees = sorted(sum(i in e for e in deep_core) for i in range(4))
    assert degrees in ([2,2,3,3], [3,3,3,3])
print("PASS F3: all matchings and deep/safe incidence")

p=F(1,58)
a0=F(1,86)
r0=1-a0
s=F(99,100)
U=F(153,1000)
q=F(27,100)
h=F(161,500)
assert s*s<r0 and U*U>2*a0 and h*h>6*p
c0=(F(1,2)-U-a0/2)**2
T0=(1+a0)/(2*s)
k0=T0*T0*(T0+F(1,2))/(2*s)
d0=c0/4
assert q*q>4*k0*k0+d0*d0/4
R0=k0*(1+F(3)/(1+s))-F(5,2)*d0+q
C0=a0*(F(4,5)/r0**2+F(1,16)/r0**2+R0)
D0=a0/(5*r0**2)
assert D0==F(86,36125)
gap=p-C0-D0*h
assert gap==F(9329200545913122660407,324578490573724679952000000)
assert gap>0
print("PASS exact rational radical enclosures")
print("PASS strict contradiction margin:",gap)
print("CONDITIONAL THEOREM: 1/86 < A <= 383/504")
print("GLOBAL PROVED RANGE UNCHANGED: 40 <= tau_5 <= 44")
