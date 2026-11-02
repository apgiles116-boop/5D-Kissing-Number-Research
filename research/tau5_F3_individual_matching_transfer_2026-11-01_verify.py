#!/usr/bin/env python3
"""Exact SymPy/Fraction verifier for F3 individual matching transfer."""
from fractions import Fraction as F
from itertools import combinations
import sympy as s

E={tuple(sorted(e)) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
P0={tuple(sorted(e)) for e in [(0,4),(1,7),(2,3),(5,6)]}
P1={tuple(sorted(e)) for e in [(0,2),(1,4),(3,6),(5,7)]}
P2={tuple(sorted(e)) for e in [(0,5),(1,4),(2,7),(3,6)]}
perms=[(0,1,2,3,4,5,6,7),(2,6,0,4,3,7,1,5),(5,3,7,1,6,0,4,2),(7,4,5,6,1,2,3,0)]
for p in perms:
    image=lambda pairs:{tuple(sorted((p[a],p[b]))) for a,b in pairs}
    assert image(E)==E and image(P0)==P0 and image(P1)==P1
swap=(0,1,5,6,4,2,3,7)
assert {tuple(sorted((swap[a],swap[b]))) for a,b in E}==E
assert {tuple(sorted((swap[a],swap[b]))) for a,b in P0}==P0
assert {tuple(sorted((swap[a],swap[b]))) for a,b in P1}==P2
orbits={
0:[(1,6),(3,4)],1:[(0,6),(1,2),(3,7),(4,5)],2:[(1,3),(4,6)],
3:[(0,2),(5,7)],4:[(0,5),(2,7)],5:[(0,7),(2,5)],
6:[(0,4),(1,7),(2,3),(5,6)],7:[(1,4),(3,6)],
8:[(0,1),(2,6),(3,5),(4,7)],9:[(0,3),(1,5),(2,4),(6,7)]}
assert {tuple(sorted(pair)) for pairs in orbits.values() for pair in pairs}==set(combinations(range(8),2))
for pairs in orbits.values():
    for p in perms:
        assert {tuple(sorted((p[a],p[b]))) for a,b in pairs}==set(pairs)
assert set(orbits[4]).issubset(E) and set(orbits[9]).isdisjoint(E)
assert set(orbits[6])==P0 and set(orbits[3])|set(orbits[7])==P1
x=s.symbols('x0:10')
blocks=[]
for r,v in [(1,1),(1,-1),(-1,1),(-1,-1)]:
    A=1+r*x[3]+v*x[4]+r*v*x[5]
    B=1+r*x[0]+v*x[2]+r*v*x[7]
    R=x[8]+r*x[1]+v*x[9]+r*v*x[6]
    blocks.append(s.Matrix([[A,R],[R,B]]))
Z=[
 s.Matrix([[s.Rational(309,400),s.Rational(1857,8000)],[s.Rational(1857,8000),s.Rational(599,1000)]]),
 s.Matrix([[s.Rational(109,200),-s.Rational(1857,8000)],[-s.Rational(1857,8000),s.Rational(99,1000)]]),
 s.Matrix([[s.Rational(109,400),-s.Rational(1313,8000)],[-s.Rational(1313,8000),s.Rational(99,1000)]]),
 s.Matrix([[s.Rational(9,200),s.Rational(1313,8000)],[s.Rational(1313,8000),s.Rational(599,1000)]])
]
assert [z.det() for z in Z]==[s.Rational(k,64000000) for k in [26166111,4671,2591,1151]]
assert all(z[0,0]>0 and z[1,1]>0 and z.det()>0 for z in Z)
C0=2+2*x[6]; C1=2+x[3]+x[7]
rhs=sum(s.trace(z*m) for z,m in zip(Z,blocks))+s.Rational(91,200)*(-s.Rational(1,2)-x[4])+s.Rational(34,125)*(s.Rational(1,2)-x[9])
assert s.expand(C1-(1291-1585*C0)/s.Integer(2000)-rhs)==0
assert (F(1291)-F(1585)*F(383,504))/F(2000)==F(43609,1008000)
assert (F(1291)-F(1585)*F(567,1000))/F(2000)==F(78461,400000)
assert F(78461,400000)>F(49,250)
print('PASS: exact F3 automorphisms, 28-pair orbit partition, PSD SOS and rational corollaries')
print('STATUS: Type E OPEN; 40<=tau_5<=44')
