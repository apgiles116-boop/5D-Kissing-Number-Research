"""Exact rational checker for Type E singleton-contact six-defect theorem.
Analytic Cauchy and implicit-differentiation proofs are in companion note.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

edges=[(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]
ms=[m for m in combinations(edges,4) if len({v for e in m for v in e})==8]
assert len(ms)==3
patterns=[]
for m in ms:
    ids={v:i for i,e in enumerate(m) for v in e}
    counts={e:0 for e in combinations(range(4),2)}
    for a,b in edges:
        if ids[a]!=ids[b]:
            counts[tuple(sorted((ids[a],ids[b])))]+=1
    patterns.append(sorted(counts.values()))
    if sorted(counts.values())==[0,1,1,1,1,2]:
        z=next(k for k,v in counts.items() if v==0)
        d=next(k for k,v in counts.items() if v==2)
        assert not set(z).intersection(d)
assert sorted(patterns)==[[0,1,1,1,1,2],[0,1,1,1,1,2],[1,1,1,1,1,1]]

D=F(1780062775,4032758016)
b=F(383,1008)
target=F(79,1000)
lo=F(2071067,10**7)
hi=F(207107,10**6)
cu=F(154025,10**6)
Du=F(441401,10**6)
assert (1+2*lo)**2<2<(1+2*hi)**2
assert F(2,5)<D<Du
assert D>b and lo>b/2 and hi<F(1,4) and hi<2*b-D

def P(x,y):return x+y+4*(x*x+y*y-x*y)-F(1,2)
assert P(lo,cu)>0
assert D*D/3<target
assert b*b/2+(D-b)**2<target
assert hi*hi+(b-lo)**2+(D-b)**2<target
assert hi*hi+cu*(Du-lo)<target

def Q4(x):return 12800*x**4+7040*x**3-1688*x*x-704*x+135
for j in range(7):
    x=F(1,5)+F(j,120)
    R=(7-40*x*x-9*x)/(13+40*x)
    assert 2*(13+40*x)**2*P(x,R)==3*Q4(x)
mono=[F(87,25),-F(156,25),F(701,50),F(54,25),F(2,25)]
for j in range(5):
    assert sum(mono[k]*j**k for k in range(5))==Q4(F(1,5)+F(j,20))
bern=[sum(mono[k]*F(comb(j,k),comb(4,k)) for k in range(j+1)) for j in range(5)]
assert bern==[F(87,25),F(48,25),F(809,300),F(127,20),F(27,2)]
assert all(v>0 for v in bern)

L=F(8790283,317520)
safe=L-F(3,2)-D-target
assert safe==F(12936979830517,504094752000)
assert safe-(L-F(3,2)-D-F(40949,500000))==F(2898,10**6)
print("PASS: F3 patterns, rational algebra, positive Bernstein certificate")
print("Q<79/1000; S_safe>",safe,"=",float(safe))
