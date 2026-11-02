#!/usr/bin/env python3
"""Exact SymPy/Fraction audit of canonical F3 C4 defect-stability theorem.
Upstream Type-E harmonic, endpoint and Q-frame certificates are assumed, not re-proved.
"""
from fractions import Fraction as F
from itertools import combinations
from sympy import Matrix, sqrt, symbols, simplify, factor

w=sqrt(2)
lam=symbols("lambda")
W=Matrix([[0,w,1,0],[w,0,1,0],[1,1,0,1],[0,0,1,0]])
K=W+w*Matrix.eye(4)
assert factor(W.charpoly().as_expr(),extension=w)==(lam+w)**2*(lam-w-1)*(lam-w+1)
assert K.rank()==2
v=symbols("v0:4",real=True)
x=Matrix(v)
sos=w*(v[0]+v[1]+v[2]/w)**2+(v[2]+w*v[3])**2/w
assert simplify((x.T*K*x)[0]-sos)==0

a=symbols("a0:4",nonnegative=True)
C=sum(a)
cycle=[(0,1),(1,2),(2,3),(3,0)]
bound=sum((a[i]+a[j])*(1-a[i]-a[j])/2 for i,j in cycle)
variance=C*(1-C/2)-((a[0]-a[2])**2+(a[1]-a[3])**2)/2
assert simplify(bound-variance)==0

c={tuple(sorted((i,j))):symbols("c%d%d"%(i,j),real=True)
   for i,j in combinations(range(4),2)}
aa=symbols("aa0:4",nonnegative=True)
CC=sum(aa)
X2=aa[0]+aa[1]+2*c[0,1]
Y2=aa[2]+aa[3]+2*c[2,3]
XY=c[0,2]+c[0,3]+c[1,2]+c[1,3]
lhs=CC/w+XY+c[2,3]
rhs=(X2+2*w*XY+2*Y2+aa[0]+aa[1]-2*c[0,1])/(2*w)-(w-1)*c[2,3]
assert simplify(lhs-rhs)==0

pairs=list(combinations(range(4),2))
types=set()
for edges in combinations(pairs,4):
    deg=[0]*4
    for i,j in edges: deg[i]+=1;deg[j]+=1
    types.add(tuple(sorted(deg)))
assert types=={(1,2,2,3),(2,2,2,2)}

Cmax=F(567,1000)
Dstar=Cmax*(1-Cmax/F(2))
assert Dstar==F(812511,2000000)
assert Dstar>F(3,8)
assert 2*F(401,1000)**2>Cmax**2
assert F(401,1000)<Dstar
assert Dstar<F(2099601,5000000)
assert Dstar<F(1780062775,4032758016)

r=Dstar-F(3,8)
assert F(0)<r<F(1,8)
sq=F(3,64)+r*r
safe=F(283626,10000)-F(3,2)-Dstar-sq
assert sq==F(191407625121,4000000000000)
assert safe==F(105633970374879,4000000000000)
assert F(42,4)+F(142,9)<safe<F(43,4)+F(141,9)
print("PASS: exact signed paw SOS, C4 variance, five-edge SOS, graph cases, rational bounds.")
print("canonical D_raw <",Dstar,"safe squared sum >",safe)
