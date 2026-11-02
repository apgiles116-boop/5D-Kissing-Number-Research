#!/usr/bin/env python3
"""Exact SymPy/Fraction audit of the 2026-11-02 singleton mass/spectral note.
Checks algebraic identities and rational margins, not upstream Type-E assumptions.
"""
from fractions import Fraction as F
from itertools import combinations
from sympy import Matrix, Rational, symbols, simplify, sqrt, factor

t, d = symbols('t d', real=True)
assert simplify((t-2*d)*(1-t-2*d)-4*d*d-(t*(1-t)-2*d)) == 0

b=t/2
D=t*(1-t)/2
G=Matrix([[b,0,-D,-D],
          [0,1-b,-D,-Rational(1,2)-D],
          [-D,-D,b,0],
          [-D,-Rational(1,2)-D,0,1-b]])
P=Matrix([[1,0,1,0],[0,1,0,1],[1,0,-1,0],[0,1,0,-1]]) / sqrt(2)
T=simplify(P.T*G*P)
Bplus=Matrix([[t*t/2,-D],[-D,(1-t)**2/2]])
Bminus=Matrix([[t*(2-t)/2,D],[D,(3-t*t)/2]])
assert simplify(T[:2,:2]-Bplus)==Matrix.zeros(2)
assert simplify(T[2:,2:]-Bminus)==Matrix.zeros(2)
assert simplify(T[:2,2:])==Matrix.zeros(2)
assert factor(Bplus.det())==0
assert simplify(Bminus.det()-t*(3-2*t)/2)==0

for tv in [F(1,100),F(1,10),F(1,4),F(49,100)]:
    gv=G.subs(t,Rational(tv.numerator,tv.denominator))
    assert gv.det()>=0
    de=tv*(1-tv)/2
    c=-de; z=-F(1,2)-de; p=q=-de
    assert c+z+p+q==-F(1,2)-4*de
    assert c+z-p-q==-F(1,2)
    assert c-z+p-q==F(1,2)
    assert c-z-p+q==F(1,2)
    assert tv-1<-F(1,2)

s=Rational(3703,2500)
E={(0,1),(0,2),(1,2),(2,3)}
Adj=Matrix(4,4,lambda i,j: 1 if tuple(sorted((i,j))) in E and i!=j else 0)
L=Adj+s*Matrix.eye(4)
minors=[factor(L[:k,:k].det()) for k in range(1,5)]
assert minors==[Rational(3703,2500), Rational(7462209,6250000),
                Rational(12595059927,15625000000),
                Rational(700659681,39062500000000)]
assert all(x>0 for x in minors)

all_edges=list(combinations(range(4),2))
patterns=set()
for e4 in combinations(all_edges,4):
    deg=[0]*4
    for i,j in e4:
        deg[i]+=1
        deg[j]+=1
    patterns.add(tuple(sorted(deg)))
assert patterns=={(1,2,2,3),(2,2,2,2)}

a0,a1,a2,a3,c01,c02,c03,c12,c13,c23=symbols(
    'a0 a1 a2 a3 c01 c02 c03 c12 c13 c23')
C=a0+a1+a2+a3
X2=a0+a1+2*c01
Y2=a2+a3+2*c23
D012=a0+a1-2*c01
XY=c02+c03+c12+c13
N=-XY-c23
lhs=C/sqrt(2)-N
rhs=(X2+2*sqrt(2)*XY+2*Y2+D012)/(2*sqrt(2))-(sqrt(2)-1)*c23
assert simplify(lhs-rhs)==0

Cbar=F(567,1000)
Dstar=F(2099601,5000000)
Dold=F(1780062775,4032758016)
assert Dstar==F(3703,5000)*Cbar
assert F(3,8)<Dstar
assert Cbar*(1-Cbar/F(2))<Dstar
assert Cbar*Cbar/F(2)<Dstar*Dstar
assert Cbar/F(2)<Dstar
assert Dstar<Dold

r=Dstar-F(3,8)
assert 0<r<F(1,8)
Qsq=F(3,64)+r*r
Qexc=F(3,2)+Dstar+Qsq
Qsafe=F(283626,10000)-Qexc
assert Qsq==F(1222320609201,25000000000000)
assert Qexc==F(49220325609201,25000000000000)
assert Qsafe==F(659844674390799,25000000000000)
assert F(42,4)+F(184-42,9)<Qsafe<F(43,4)+F(184-43,9)

print('PASS: local PSD, graph cases, exact 5-edge SOS, spectral and rational bounds.')
print('Dstar:',Dstar,'=',float(Dstar),'old:',float(Dold))
print('Qsafe >',Qsafe,'=',float(Qsafe))
