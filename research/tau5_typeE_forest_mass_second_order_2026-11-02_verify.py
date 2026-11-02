#!/usr/bin/env python3
"""Exact Fraction verification for Type E forest mass/defect bounds."""
from fractions import Fraction as F
from itertools import combinations

A=F(383,504)
A_cond=F(567,1000)
Q_base=F(8790283,317520)
Q_center=F(141813,5000)
def f(t): return t*(1-t)/2
def g(t): return f(t)+f(t)**2
def star(c,h): return 3*h((c+F(1,2))/3)
def path(c,h): return 2*h(c/2)+h(F(1,2))

edges=list(combinations(range(4),2))
classes={"<=2":0,"star":0,"P4":0,"C4":0}
for mask in range(64):
    E={edges[i] for i in range(6) if (mask>>i)&1}
    triangle=any(all(tuple(sorted(e)) in E for e in combinations(t,2))
                 for t in combinations(range(4),3))
    if triangle: continue
    deg=sorted(sum(v in e for e in E) for v in range(4))
    if len(E)==4:
        assert deg==[2,2,2,2]
        classes["C4"]+=1
    elif len(E)==3:
        assert deg in ([1,1,1,3],[1,1,2,2])
        classes["star" if deg==[1,1,1,3] else "P4"]+=1
    else: classes["<=2"]+=1
assert classes=={"<=2":22,"star":4,"P4":12,"C4":3}, classes

for c in (A,A_cond):
    assert 0<c<1
    for h in (f,g):
        assert star(c,h)>path(c,h)>2*h(F(1,2))
assert star(A,f)==F(556895,1524096)
assert star(A,g)==F(2856416366785,6968605851648)
assert path(A,f)==F(366383,1016064)
assert path(A,g)==F(834099607777,2064772104192)
assert star(A,f)<F(3,8)
assert star(A,g)<F(27,64)
assert star(A_cond,f)==F(2062511,6000000)
assert star(A_cond,g)==F(41379149625121,108000000000000)
assert star(F(2,3),g)==F(55825,139968)<F(2,5)
assert path(F(2,3),g)==F(2009,5184)<F(2,5)
assert A-F(2,3)==F(47,504)

core=F(3,2)+star(A,g)
base=Q_base-core
center=Q_center-core
assert core==F(13309325144257,6968605851648)
assert base==F(898054305738811,34843029258240)
assert center==F(115211534489809103,4355378657280000)
assert 38*F(1,4)+146*F(1,9)<base<39*F(1,4)+145*F(1,9)
assert 43*F(1,4)+141*F(1,9)<center<44*F(1,4)+140*F(1,9)

alt_core=F(5,4)+path(A,g)
alt_base=Q_base-alt_core
alt_center=Q_center-alt_core
assert alt_core==F(3415064738017,2064772104192)
assert alt_base==F(268732359705499,10323860520960)
assert alt_center==F(34467025340211887,1290482565120000)
assert 39*F(1,4)+146*F(1,9)<alt_base<40*F(1,4)+145*F(1,9)
assert 44*F(1,4)+141*F(1,9)<alt_center<45*F(1,4)+140*F(1,9)
print("ALL EXACT FRACTION CHECKS PASSED",classes)
