#!/usr/bin/env python3
"""Exact incidence and algebraic checks for F3 switched-endpoint Perron theorem.
The Perron/Gram argument itself is analytic in the companion Markdown proof.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as s

deep={tuple(sorted(p)) for p in [(0,2),(0,4),(0,5),(1,4),(1,7),
                                   (2,3),(2,7),(3,6),(5,6),(5,7)]}
matchings=[
    ([(0,4),(1,7),(2,3),(5,6)], (1,-1,1,1), [1]*6),
    ([(0,2),(1,4),(3,6),(5,7)], (1,-1,-1,1), [0,1,1,1,1,2]),
    ([(0,5),(1,4),(2,7),(3,6)], (1,-1,1,1), [0,1,1,1,1,2]),
]
for pairs,g,expected in matchings:
    mult=[]
    for i,j in combinations(range(4),2):
        contacts=[]
        for ki,vi in enumerate(pairs[i]):
            for kj,vj in enumerate(pairs[j]):
                if tuple(sorted((vi,vj))) in deep:
                    contacts.append((ki,kj))
        mult.append(len(contacts))
        for ki,kj in contacts:
            sig=(1 if ki==0 else -1)*(1 if kj==0 else -1)
            assert sig==g[i]*g[j], (pairs,i,j,contacts)
        if len(contacts)==2:
            assert set(contacts) in ({(0,0),(1,1)},{(0,1),(1,0)})
    assert sorted(mult)==sorted(expected), (pairs,mult)
print("PASS exact F3 matching incidence and switching")

edges=list(combinations(range(4),2))
patterns=set()
for n in range(7):
    for es in combinations(edges,n):
        if any(all(tuple(sorted(e)) in es for e in combinations(tri,2))
               for tri in combinations(range(4),3)):
            continue
        degree=tuple(sorted(sum(v in e for e in es) for v in range(4)))
        patterns.add((n,degree))
assert {d for n,d in patterns if n==3}=={(1,1,1,3),(1,1,2,2)}
assert {d for n,d in patterns if n==4}=={(2,2,2,2)}
print("PASS triangle-free graph support classification")

x,y,z=s.symbols('x y z',real=True)
B=s.Matrix([[0,x,0,0],[x,0,y,0],[0,y,0,z],[0,0,z,0]])
assert s.expand((s.eye(4)-B).det()-(1-x*x)*(1-z*z)+y*y)==0
S=s.Matrix([[0,x,y,z],[x,0,0,0],[y,0,0,0],[z,0,0,0]])
assert s.expand((s.eye(4)-S).det()-(1-x*x-y*y-z*z))==0
print("PASS exact path and star determinant identities")

C=F(567,1000)
Ddis=C*(1-C/2)/2
assert Ddis==F(812511,4000000)
assert (1+2*Ddis)**2<2  # proves Ddis<(sqrt(2)-1)/2
D=(s.sqrt(2)-1)/2
cap=s.simplify(D+s.Rational(1,64)+(D-s.Rational(1,8))**2)
assert s.simplify(cap-(s.Rational(13,32)-s.sqrt(2)/8))==0
Q=F(283626,10000)
Qc=Q-F(57,32)
Qa=Q-F(49,32)
assert Qc==F(531627,20000) and Qc>F(239,9)
assert Qa==F(536627,20000) and Qa>F(965,36)
assert Qc<F(961,36)
assert Qa<F(46,4)+F(139,9)
Qs=s.Rational(Q.numerator,Q.denominator)-s.Rational(3,2)-cap
assert s.simplify(Qs-(s.Rational(529127,20000)+s.sqrt(2)/8))==0
assert float(Qs)>float(F(239,9)) and float(Qs)<float(F(961,36))
print("PASS exact radical, cap-concentration and Q-safe integer thresholds")
print("canonical D strong ceiling =",s.N(D,16))
print("canonical Q-safe strong floor =",s.N(Qs,16))
print("alternative double-free Q-safe floor =",float(Qa))
