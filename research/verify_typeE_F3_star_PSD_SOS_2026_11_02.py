#!/usr/bin/env python3
"""Exact symbolic verification of the canonical F3 three-defect-star PSD/SOS obstruction."""
from sympy import Matrix, Rational, symbols, eye, factor

T=Matrix([
 [299,115,145,-145,0,146,-146,209],
 [115,131,0,0,209,0,0,0],
 [145,0,187,0,-145,188,0,268],
 [-145,0,0,283,145,0,280,0],
 [0,209,-145,145,531,-146,146,-209],
 [146,0,188,0,-146,195,0,268],
 [-146,0,0,280,146,0,283,0],
 [209,0,268,0,-209,268,0,387]
])
assert T == T.T
minors=[T[:k,:k].det() for k in range(1,9)]
assert minors==[299,25944,2097253,78473174,776559545,
               4645182931,20057485321,40545532209]
assert all(x>0 for x in minors)
print("PASS: integer T is positive definite (Sylvester's criterion).")

G=eye(8)
for i in range(8):
 for j in range(i+1,8):
  G[i,j]=G[j,i]=symbols("g%d%d"%(i,j))
P=((0,4),(7,1),(2,3),(5,6))
def wdot(i,j):
 a,b=P[i];c,d=P[j]
 return (G[a,c]-G[a,d]-G[b,c]+G[b,d])/4
slacks=[
 (81,Rational(1,2)-G[0,1]),
 (47,Rational(1,2)-G[2,5]),
 (67,-Rational(1,2)-G[2,7]),
 (70,-Rational(1,2)-G[3,6]),
 (67,-Rational(1,2)-G[5,7]),
 (209,-Rational(1,2)-wdot(0,1)),
 (145,-Rational(1,2)-wdot(0,2)),
 (146,-Rational(1,2)-wdot(0,3))
]
identity=sum(Rational(k,500)*s for k,s in slacks)+(T*G).trace()/4000
assert factor(identity)==-Rational(1,500)
print("PASS: 28-variable exact SOS identity equals -1/500.")

E={tuple(sorted(e)) for e in
 ((0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7))}
matching={frozenset(e) for e in ((0,4),(1,7),(2,3),(5,6))}
assert (0,1) not in E and (2,5) not in E
assert (2,7) in E and (3,6) in E and (5,7) in E
autos=[
 (0,1,2,3,4,5,6,7),
 (7,4,2,3,1,5,6,0),
 (2,6,0,4,3,7,1,5),
 (5,3,0,4,6,7,1,2)
]
images=set()
for p in autos:
 assert {tuple(sorted((p[i],p[j]))) for i,j in E}==E
 assert {frozenset((p[i],p[j])) for i,j in matching}==matching
 images.add(frozenset((p[0],p[4])))
assert images==matching
print("PASS: all four canonical centers covered by graph automorphisms.")

from fractions import Fraction as F
D=F(366383,1016064)
DS=F(834099607777,2064772104192)
assert D<F(3,8)
assert DS<F(81,200)
Qcore=F(3,2)+DS
Qbase=F(8790283,317520)-Qcore
Qstrong=F(141813,5000)-Qcore
assert Qbase==F(266151394575259,10323860520960)
assert Qstrong==F(34144404698931887,1290482565120000)
assert Qbase>38*F(1,4)+(184-38)*F(1,9)
assert Qstrong>43*F(1,4)+(184-43)*F(1,9)
print("PASS: conditional canonical path-only rational ceilings and counts.")
print("GLOBAL STATUS UNCHANGED: 40 <= tau_5 <= 44; Type E open.")
