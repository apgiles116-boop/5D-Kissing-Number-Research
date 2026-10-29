#!/usr/bin/env python3
"""Exact F3 incidence and rational verifier for the Type-E A>1/98 theorem.
The analytic inequalities and retained 21-line P>1/58 proof are in the note.
"""
from fractions import Fraction as F
from itertools import combinations

E = {frozenset(edge) for edge in ((0,2),(0,4),(0,5),(1,4),(1,7),
                                   (2,3),(2,7),(3,6),(5,6),(5,7))}

def matchings(vertices):
    if not vertices:
        yield ()
        return
    v = min(vertices)
    for w in vertices - {v}:
        if frozenset((v,w)) in E:
            for rest in matchings(vertices - {v,w}):
                yield ((v,w),) + rest

M = list(matchings(set(range(8))))
assert len(M) == 3, M
for matching in M:
    cross = []
    for i,j in combinations(range(4),2):
        a,b = matching[i]
        c,d = matching[j]
        pairs = [((a,c),+1), ((a,d),-1), ((b,c),-1), ((b,d),+1)]
        deep = [sgn for (v,w),sgn in pairs if frozenset((v,w)) in E]
        safe = [sgn for (v,w),sgn in pairs if frozenset((v,w)) not in E]
        assert safe.count(+1)>=2 or safe.count(-1)>=2, (matching,i,j)
        if deep:
            assert len(set(deep)) == 1
            cross.append((i,j))
    assert len(cross) in (5,6)
    deg = [sum(i in edge for edge in cross) for i in range(4)]
    assert sorted(deg) in ([2,2,3,3], [3,3,3,3])
    print("PASS matching:",matching,"deep core pairs",len(cross),"degrees",deg)

A=F(1,98)
r=1-A
c=(F(1,2)-F(1,7)-A/2)**2
T=(1+A)/(2*r)
K=T*T*(T+F(1,2))
k=K/(2*r)
d=c/4
assert c==F(4761,38416)
assert k==F(23532201,177058562)
assert d==F(4761,153664)
assert F(267,1000)**2 > 4*k*k+d*d/4
assert F(161,500)**2 > F(3,29)
R0=4*k-F(5,2)*d+F(267,1000)
C0=A*(F(4,5)/r**4+F(1,16)/r**2+R0)
D0=A/(5*r**4)
assert C0==F(5504307003982407,333292204171808000)
gap=F(1,58)-C0-D0*F(161,500)
assert gap==F(2018010242038857,48327369604912160000)
assert gap>0
print("PASS exact root enclosures and rational contradiction:",gap)
print("CONDITIONAL TYPE-E THEOREM: 1/98 < A <= 383/504")
