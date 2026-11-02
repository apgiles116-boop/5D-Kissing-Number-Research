#!/usr/bin/env python3
from itertools import product
from sympy import symbols, expand, sqrt, simplify
c,d,p,q=symbols('c d p q', real=True)
T=lambda s,t:c+s*q+t*p+s*t*d
assert expand(sum(T(s,t)**2 for s,t in product((-1,1),repeat=2))-4*(c*c+d*d+p*p+q*q))==0
assert expand(T(1,1)-(c+d+p+q))==0
assert expand(T(-1,-1)-(c+d-p-q))==0
assert expand(T(1,-1)-(c-d+q-p))==0
assert expand(T(-1,1)-(c-d-q+p))==0
edges={tuple(sorted(e)) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
perm={i:i for i in range(8)}
perm[2],perm[5],perm[3],perm[6]=5,2,6,3
assert {tuple(sorted((perm[i],perm[j]))) for i,j in edges}==edges
P1={tuple(sorted(e)) for e in [(0,2),(1,4),(3,6),(5,7)]}
P2={tuple(sorted(e)) for e in [(0,5),(1,4),(2,7),(3,6)]}
assert {tuple(sorted((perm[i],perm[j]))) for i,j in P1}==P2
assert (1,3) not in edges
assert all(e in edges for e in [(0,4),(1,7),(2,3),(5,6),(0,5)])
delta=(7-4*sqrt(3))/16
assert simplify(delta-(2-sqrt(3))**2/16)==0
assert delta>0
print('PASS: Walsh Parseval, F3 automorphism, incidence, exact floor')
