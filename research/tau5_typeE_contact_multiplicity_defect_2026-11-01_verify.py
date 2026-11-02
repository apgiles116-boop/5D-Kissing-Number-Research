#!/usr/bin/env python3
"""Exact arithmetic and F3 incidence verifier for contact-multiplicity defect caps."""
from fractions import Fraction as F
from itertools import combinations
import sympy as s

E={tuple(sorted(e)) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
P=[[(0,4),(1,7),(2,3),(5,6)],[(0,2),(1,4),(3,6),(5,7)],[(0,5),(1,4),(2,7),(3,6)]]
assert len(E)==10
for k,matching in enumerate(P):
    assert {v for pair in matching for v in pair}==set(range(8))
    assert all(tuple(sorted(p)) in E for p in matching)
    counts=[]
    for i,j in combinations(range(4),2):
        edges=[(x,y) for x in matching[i] for y in matching[j] if tuple(sorted((x,y))) in E]
        counts.append(len(edges))
        if len(edges)==2:
            assert len({x for x,y in edges})==len({y for x,y in edges})==2
    assert sorted(counts)==([1]*6 if k==0 else [0,1,1,1,1,2])

h=s.Rational(1,2)
G1=s.Matrix([[1,-h,-1,h],[-h,1,h,-h],[-1,h,1,-h],[h,-h,-h,1]])
assert G1.eigenvals()=={s.Integer(0):1,h:1,(7-s.sqrt(17))/4:1,(7+s.sqrt(17))/4:1}
assert (G1[0,2]-G1[0,3]-G1[1,2]+G1[1,3])/4==-s.Rational(5,8)
G2=s.Matrix([[1,-h,-1,h],[-h,1,h,-1],[-1,h,1,-h],[h,-1,-h,1]])
assert G2.eigenvals()=={s.Integer(0):2,s.Integer(1):1,s.Integer(3):1}
assert (G2[0,2]-G2[0,3]-G2[1,2]+G2[1,3])/4==-s.Rational(3,4)

D_exact=F(1780062775,4032758016)
D0=F(441401,10**6)
assert F(3,8)<D_exact<D0<F(1,2)
r=D0-F(3,8)
q0=3*F(1,8)**2+r*r
q1=F(1,4)**2+F(1,8)**2+r*r
assert q0==F(51284092801,10**12)
assert q1==F(82534092801,10**12)
for caps,vec in [([F(1,8)]*6,[F(1,8)]*3+[r]+[F(0)]*2),
                 ([F(1,4)]+[F(1,8)]*4,[F(1,4),F(1,8),r,F(0),F(0)])]:
    assert sum(vec)==D0
    assert all(0<=v<=c for v,c in zip(vec,caps))
    assert all(sum(sorted(vec,reverse=True)[:k])==min(D0,sum(caps[:k])) for k in range(1,len(caps)+1))

C=F(283626,10000)
for n,k,q,count,expected in [(184,6,q0,42,F(26369914907199,10**12)),
                             (185,5,q1,43,F(26588664907199,10**12))]:
    safe=C-F(k,4)-D0-q
    threshold=F(count,4)+F(n-count,9)
    assert safe==expected and safe>threshold
    print(f'{n} safe: squared mass > {safe} ({float(safe):.12f}); at least {count+1} correlations > 1/3')
print('PASS: exact local PSD witnesses, F3 incidence, cap concentration, and rational count margins')
print('STATUS: conditional Type E; OPEN; 40<=tau_5<=44')
