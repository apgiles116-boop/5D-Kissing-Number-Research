#!/usr/bin/env python3
"""Exact symbolic check: F3 canonical radical SOS, 2026-11-02."""
import sympy as s
from itertools import combinations
R=s.sqrt
h=s.Rational(1,2)
D={tuple(sorted(e)) for e in [(0,2),(0,4),(0,5),(1,4),(1,7),(2,3),(2,7),(3,6),(5,6),(5,7)]}
P0={tuple(sorted(e)) for e in [(0,4),(1,7),(2,3),(5,6)]}
perms=[(0,1,2,3,4,5,6,7),(2,6,0,4,3,7,1,5),(5,3,7,1,6,0,4,2),(7,4,5,6,1,2,3,0)]
for p in perms:
    assert {tuple(sorted((p[i],p[j]))) for i,j in D}==D
    assert {tuple(sorted((p[i],p[j]))) for i,j in P0}==P0
orbits={0:[(1,6),(3,4)],1:[(0,6),(1,2),(3,7),(4,5)],2:[(1,3),(4,6)],
3:[(0,2),(5,7)],4:[(0,5),(2,7)],5:[(0,7),(2,5)],
6:[(0,4),(1,7),(2,3),(5,6)],7:[(1,4),(3,6)],
8:[(0,1),(2,6),(3,5),(4,7)],9:[(0,3),(1,5),(2,4),(6,7)]}
assert {tuple(sorted(p)) for v in orbits.values() for p in v}==set(combinations(range(8),2))
for v in orbits.values():
    for p in perms:
        assert {tuple(sorted((p[i],p[j]))) for i,j in v}==set(v)
assert all(set(orbits[i]).issubset(D) for i in [3,4,7])
assert set(orbits[6])==P0
x=s.symbols('x0:10')
G=s.eye(8)
for i,v in orbits.items():
    for a,b in v:G[a,b]=G[b,a]=x[i]
Z={(1,1):s.Matrix([[(2*R(6)-R(2))/8,s.Rational(1,4)],[s.Rational(1,4),R(2)/4]]),
(1,-1):s.Matrix([[R(6)/8,-s.Rational(1,4)],[-s.Rational(1,4),R(6)/12]]),
(-1,1):s.Matrix([[R(6)/8,-s.Rational(1,4)],[-s.Rational(1,4),R(6)/12]]),
(-1,-1):s.Matrix([[R(2)/8,s.Rational(1,4)],[s.Rational(1,4),R(2)/4]])}
assert s.simplify(Z[(1,1)].det()-(R(3)-1)/8)==0
assert all(s.simplify(z.det())==0 for k,z in Z.items() if k!=(1,1))
assert all(z[0,0]>0 and z[1,1]>0 for z in Z.values())
M={}
for r,t in [(1,1),(1,-1),(-1,1),(-1,-1)]:
    v0=s.zeros(8,1);v1=s.zeros(8,1)
    for c,p in zip([1,r,t,r*t],perms):
        v0[p[0]]+=s.Rational(c,2)
        v1[p[1]]+=s.Rational(c,2)
    A=1+r*x[3]+t*x[4]+r*t*x[5]
    B=1+r*x[0]+t*x[2]+r*t*x[7]
    V=x[8]+r*x[1]+t*x[9]+r*t*x[6]
    M[r,t]=s.Matrix([[A,V],[V,B]])
    U=s.Matrix.hstack(v0,v1)
    assert U.T*G*U==M[r,t]
lam=(R(6)-R(2))/4
mu=(3*R(2)-R(6))/6
floor=2-(R(6)+R(2))/2
rhs=sum(s.trace(Z[k]*M[k]) for k in M)
rhs+=lam*(-h-x[3])+lam*(-h-x[4])+mu*(-h-x[7])
assert s.simplify(s.expand(rhs-(2+2*x[6]-floor)))==0
assert lam>0 and mu>0 and s.simplify(2*lam+mu-R(6)/3)==0
xx={x[0]:-s.Rational(1,4),x[1]:R(2)/4,x[2]:-s.Rational(1,4),
x[3]:-h,x[4]:-h,x[5]:0,x[6]:-(R(6)+R(2))/4,
x[7]:-h,x[8]:(R(6)-R(2))/4,x[9]:R(2)/4}
assert [M[k].subs(xx).rank() for k in M]==[0,1,1,1]
assert G.subs(xx).rank()==3
assert s.simplify((2+2*x[6]).subs(xx)-floor)==0
assert all(float(xx[x[i]])<=-.5 if i in [3,4,6,7] else
           -.5<=float(xx[x[i]])<=.5 for i in range(10))
print('PASS: exact graph, 28 orbits, Fourier PSD blocks, radical SOS and rank-three weak-deep witness')
print('PROVED canonical C0 > 2-(sqrt(6)+sqrt(2))/2 =',s.N(floor,15))
print('PROVED uniform six-contact margin coefficient sqrt(6)/3')
print('OPEN: Type E; global 40<=tau_5<=44')
