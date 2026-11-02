#!/usr/bin/env python3
"""Exact F3 C4 contact/matching/Walsh and conditional Q-count audit.
The analytic Cauchy and triangle arguments are documented in the note.
No generic SDP and no invalid endpoint-average/Perron substitution.
"""
from itertools import combinations
from fractions import Fraction as F
import sympy as sp

B=((0,4),(1,7),(2,3),(5,6))
deep={frozenset(p) for p in ((0,2),(0,4),(0,5),(1,4),(1,7),
                             (2,3),(2,7),(3,6),(5,6),(5,7))}
P1={frozenset(p) for p in ((0,2),(1,4),(3,6),(5,7))}
P2={frozenset(p) for p in ((0,5),(1,4),(2,7),(3,6))}
g=(1,-1,1,1)
E=list(combinations(range(4),2))
contact={}
for i,j in E:
    hits=[]
    for si,x in enumerate(B[i]):
        for sj,y in enumerate(B[j]):
            if frozenset((x,y)) in deep:
                hits.append((frozenset((x,y)),(1-2*si)*g[i],(1-2*sj)*g[j]))
    assert len(hits)==1,(i,j,hits)
    edge,s,t=hits[0]
    assert s==t
    contact[(i,j)]=(edge,s)
plus={e for e in E if contact[e][1]==1}
minus=set(E)-plus
assert plus=={(0,2),(0,3),(1,2),(1,3)}
assert minus=={(0,1),(2,3)}
assert {contact[e][0] for e in plus}=={
    frozenset(p) for p in ((0,2),(0,5),(7,2),(7,5))}
assert frozenset((0,7)) not in deep
assert frozenset((2,5)) not in deep

# The three C4s are K4 minus one of its three opposite-edge pairs.
cycles=[]
for omitted in ((0,1),(0,2),(0,3)):
    opposite=tuple(v for v in range(4) if v not in omitted)
    edges=set(E)-{omitted,opposite}
    assert len(edges)==4
    cycles.append(edges)
assert len(cycles)==3
for edges in cycles:
    hits={contact[e][0] for e in edges}
    if edges==plus:
        assert len(set().union(*hits))==4
    else:
        assert hits in (P1,P2)
        assert len(set().union(*hits))==8

# Local singleton inequality from the exact full Walsh formula:
# h<=-delta-|p-q|, p+q<=h-delta,
# udeep<=-1/2-4delta-2|p-q|.
delta,s=sp.symbols("delta s",nonnegative=True)
h=-delta-s
pq=h-delta
assert sp.expand(h-sp.Rational(1,2)-delta+pq)==(
    -sp.Rational(1,2)-4*delta-2*s)

# K2,2 exact endpoint norm identity.
D,eta,slack=sp.symbols("D eta slack",nonnegative=True)
T=sp.expand(4+2*(-2-4*D-eta+1-slack))
assert sp.simplify(D+T/8+eta/4+slack/4-sp.Rational(1,4))==0

# Alternative matching energy C=2+sum(deep correlations)/2.
assert sp.simplify(2+(-2-4*D-eta)/2-(1-2*D-eta/2))==0

# Conditional rational bounds from the retained individual-matching SOS,
# harmonic midpoint cap, C4 quadratic certificate and Q-frame floor.
cstar=F(567,1000)
Calt_lower=(F(1291)-1585*cstar)/2000
Dmax=(1-Calt_lower)/2
assert Calt_lower==F(78461,400000)
assert Dmax==F(321539,800000)
assert F(3,8)<Dmax<F(812511,2000000)
Dstar=cstar*(1-cstar/F(2))
assert Dstar==F(812511,2000000)
budget=Dmax+Dstar**2/F(4)
assert budget==F(7090954125121,16000000000000)
assert budget>F(27,64)
assert budget>F(1,4)+F(1,32)
old=F(7160262125121,16000000000000)
assert old-budget==F(17327,4000000)
Qtotal=F(141813,5000)
Qsafe=Qtotal-F(3,2)-budget
assert Qsafe==F(422710645874879,16000000000000)
threshold=F(43,4)+F(141,9)
assert threshold==F(317,12)
assert Qsafe-threshold==F(131937624637,48000000000000)>0
assert Qsafe<F(44,4)+F(140,9)
print("PASS: F3 contact incidence, C4 matching classification, Walsh identities,")
print("      exact rational budget, and conditional 44-of-184 count")
print("D_raw <",Dmax,"Q_safe >",Qsafe,"~",float(Qsafe))
