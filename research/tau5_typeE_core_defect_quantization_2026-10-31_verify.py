#!/usr/bin/env python3
"""Exact rational verifier for Type-E core defect quantization."""
from fractions import Fraction as F
from itertools import product,combinations
from random import Random
D=F(1780062775,4032758016)
A=F(383,504)
old=F(16176768847,8065516032)
def capped(t):
    k=int(4*t)
    return F(k,16)+(t-F(k,4))**2
assert F(1,4)<D<F(9,20) and A<F(19,25)
new=F(3,2)+D/4+capped(D)+F(3,8)*A
assert new==F(32436090936603055633,16263137215612256256)<2
assert old-new==F(182406183756108143,16263137215612256256)
assert F(3,2)+F(9,20)/4+F(1,16)+(F(9,20)-F(1,4))**2+F(3,8)*F(19,25)==2
Q0=F(17456771,635040)
assert Q0-new==F(2073126471766663342507,81315686078061281280)
n=0
for ci in range(-16,17):
    c=F(ci,64)
    for di in range(65):
        d=F(di,64)
        if c+d>F(1,2): continue
        eps=max(F(0),d-F(1,2))
        rem=c*(F(1,4)-c) if c>=0 else F(3,4)*(-c-eps)+eps*(F(1,4)-eps)
        assert rem>=0 and d*d<=F(1,4)+eps/2-F(3,4)*c-rem
        n+=1
k=0
for v in product(range(5),repeat=6):
    es=[F(j,16) for j in v]
    t=sum(es)
    if t>D: continue
    assert sum(e*e for e in es)<=capped(t)
    k+=1
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
rng=Random(20261031); r=0
for trial in range(4000):
    m=[[F(rng.randrange(-4,5),8) for _ in range(3)] for _ in range(4)]
    a=[dot(v,v) for v in m]
    if max(a)>F(1,4) or sum(a)>A: continue
    pairs=list(combinations(range(4),2))
    c=[dot(m[i],m[j]) for i,j in pairs]
    d=[(F(1,2)-x)*F(rng.randrange(9),8) for x in c]
    es=[max(F(0),x-F(1,2)) for x in d]
    delta=sum(es)
    if delta>D: continue
    s=dot([sum(m[j][h] for j in range(4)) for h in range(3)],
          [sum(m[j][h] for j in range(4)) for h in range(3)])
    assert sum(x*x for x in d)<=F(3,2)+delta/4+sum(x*x for x in es)+F(3,8)*(sum(a)-s)
    assert sum(x*x for x in d)<=new
    for ((i,j),ei),((h,l),ej) in combinations(zip(pairs,es),2):
        if len({i,j,h,l})==4: assert ei+ej<=sum(a)/2
    for i,j,h in combinations(range(4),3):
        cij=dot(m[i],m[j]); cih=dot(m[i],m[h]); cjh=dot(m[j],m[h])
        assert (a[i]*cjh-cij*cih)**2 <= (a[i]*a[j]-cij*cij)*(a[i]*a[h]-cih*cih)
    r+=1
print("PASS: exact core defect quantization")
print("endpoint cases",n,"defect allocations",k,"four-core Gram cases",r)
print("Q6 cap",new,"decimal",float(new))
print("safe floor",Q0-new,"decimal",float(Q0-new))
print("global proved 40<=tau_5<=44; Type E OPEN")
