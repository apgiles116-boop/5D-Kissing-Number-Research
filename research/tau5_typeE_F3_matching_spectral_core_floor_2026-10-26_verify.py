#!/usr/bin/env python3
"""Exact SymPy checks for the F3 matching spectral midpoint floors."""
from itertools import combinations
import sympy as S

E={(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)}
P1={(0,2),(1,4),(3,6),(5,7)}
P2={(0,4),(1,7),(2,3),(5,6)}
P3={(0,5),(1,4),(2,7),(3,6)}
perfect={frozenset(m) for m in combinations(E,4)
         if len({v for e in m for v in e})==8}
assert perfect=={frozenset(P1),frozenset(P2),frozenset(P3)}
perm={0:0,1:1,2:5,3:6,4:4,5:2,6:3,7:7}
image=lambda e:tuple(sorted(perm[v] for v in e))
assert {image(e) for e in E}==E
assert {image(e) for e in P1}==P3

B=S.zeros(8)
for u in (0,2,5,7): B[u,u]=12291
for u in (1,3,4,6): B[u,u]=11095
for u,v in P2: B[u,v]=B[v,u]=10000
for u,v in {(1,4),(3,6)}: B[u,v]=B[v,u]=2958
for u,v in {(0,2),(0,5),(2,7),(5,7)}: B[u,v]=B[v,u]=2587
x=S.symbols('x')
f=(x**2-31518*x+145435645)*(x**2-21170*x+15201)*(x**2-20428*x+11867)**2
assert S.expand(B.charpoly(x).as_expr()-f)==0
assert all(B[:k,:k].det(method='domain-ge')>0 for k in range(1,9))
da,db=S.Rational(12291,10000),S.Rational(11095,10000)
b1,b2=S.Rational(2958,10000),S.Rational(2587,10000)
assert b1+2*b2-2*(da+db)==-S.Rational(483,125)
assert 2+(b1+2*b2-2*(da+db))/2==S.Rational(17,250)

h=S.Matrix([7,4,4,7])
L=S.Matrix([[0,-28,28,0],[28,0,0,-28],[-28,0,0,28],[0,28,-28,0]])
assert (L.T*L).eigenvals()=={S.Integer(3136):2,S.Integer(0):2}
order=[(0,2),(1,4),(3,6),(5,7)]
idx={v:i for i,e in enumerate(order) for v in e}
sgn={v:(1 if v==e[0] else -1) for e in order for v in e}
Lgraph=S.zeros(4)
for u,v in [(0,4),(2,3),(1,7),(5,6)]:
    i,j=idx[u],idx[v]
    Lgraph[i,j]+=h[i]*h[j]*sgn[v]
    Lgraph[j,i]+=h[i]*h[j]*sgn[u]
assert Lgraph==L
assert (sgn[0],sgn[5],sgn[2],sgn[7])==(1,1,-1,-1)
assert all(tuple(sorted((u,v))) not in E for u in order[1] for v in order[2])
deep=[(0,1),(0,2),(0,3),(1,3),(2,3)]
assert sum(a*a for a in h)-sum(h[i]*h[j] for i,j in deep)+h[1]*h[2]==-15
assert S.Rational(15,2)**2/56**2==S.Rational(225,12544)
floor=2-S.sqrt(4-S.Rational(225,12544))
assert floor>S.Rational(448,100000)

v=[S.Matrix([1,0]),S.Matrix([-S.Rational(1,2),S.sqrt(3)/2]),
   S.Matrix([-S.Rational(1,2),-S.sqrt(3)/2])]
assert all(S.simplify(v[i].dot(v[j]))==-S.Rational(1,2)
           for i,j in combinations(range(3),2))
print("PASS: F3 enumeration, exact PSD witness, doubled-pattern certificate, erratum")
print("P2 C >=",S.Rational(17,250))
print("P1/P3 C >=",floor)
