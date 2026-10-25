"""Exact arithmetic and symbolic checks for tau5 Type-E basis-chart note.

Does not certify the retained spectral gaps or Type-E infeasibility.
"""
from fractions import Fraction as F
from math import comb
from itertools import combinations
import sympy as sp

B=F(383,504)
g16,g15=F(5,88),F(1,65)
det16=g16**4*(16-B-4*g16)
det15=g15**4*(15-B-4*g15)
eta16,eta15=det16/comb(16,5),det15/comb(15,5)
assert det16==F(52019375,332471107584)
assert det15==F(464489,584786475000)
assert eta16==F(52019375,1452233797926912)
assert eta15==F(464489,1756113784425000)
assert 16-B-4*g16>0 and 15-B-4*g15>0
assert eta16*F(4,5)**4==F(83231,5672788273152)

V=sp.Matrix([[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],
             [0,0,0,1,1],[0,0,0,0,1]])
G=V.T*V
d=G.det()
u=sp.Matrix([sp.Rational(1,3),2,-1,sp.Rational(2,5),3])
v=sp.Matrix([1,sp.Rational(3,7),2,-1,sp.Rational(4,3)])
yu,yv=V.T*u,V.T*v
assert (yu.T*G.adjugate()*yv)[0]==d*u.dot(v)
assert (yu.T*G.adjugate()*yu)[0]==d*u.dot(u)
W=V.row_join(sp.Matrix([1,0,1,1,0]))
assert (W*W.T).det()==sum((W[:,list(I)].T*W[:,list(I)]).det()
                                for I in combinations(range(6),5))

A,s,R2,SC,L,H=sp.symbols("A s R2 SC L H")
Ssafe=46-L+H
Stotal=30-3*A+A**2/sp.Integer(10)-s/sp.Integer(2)+R2/sp.Integer(2)
rhs=16+3*A-A**2/sp.Integer(10)+s/sp.Integer(2)+SC-R2/sp.Integer(2)
assert sp.expand((L-H)-rhs+(Ssafe+SC-Stotal))==0
D,Q,LC,HC=sp.symbols("D Q LC HC")
core=sp.Rational(3,2)+D+Q-LC+HC
rhs2=sp.Rational(35,2)+3*A-A**2/sp.Integer(10)+s/sp.Integer(2)+D+Q-R2/sp.Integer(2)
assert sp.expand((L+LC-H-HC)-rhs2+(Ssafe+core-Stotal))==0

smax=3*F(1,4)**2+(B-F(3,4))**2
assert 30-3*B+B*B/F(10)-smax/F(2)==F(8790283,317520)
print("PASS: exact determinant, adjugate, Cauchy-Binet and Q/slack identities")
print("eta16 =",eta16, "; eta15 =",eta15)
