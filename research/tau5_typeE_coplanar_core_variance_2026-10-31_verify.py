#!/usr/bin/env python3
"""Exact SymPy verification: four-core coplanar variance identity and witness."""
import sympy as sp
from itertools import combinations
Q=sp.Rational
a=Q(1,6); t=1-a
u=[sp.Matrix([1,0]),sp.Matrix([Q(3,5),Q(4,5)]),
   sp.Matrix([0,1]),sp.Matrix([-Q(3,5),Q(4,5)])]
z=[sp.sqrt(t)*v for v in u]
m=[(-1)**i*sp.sqrt(a)*sp.Matrix([1,0,0]) for i in range(4)]
A=sum((v.dot(v) for v in m),sp.Integer(0))
assert A==Q(2,3)
assert all(v.dot(v)+w.dot(w)==1 for v,w in zip(m,z))
assert all(v.dot(v)<=Q(1,4) for v in m)
Z=sum((v*v.T for v in z),sp.zeros(2))
M=sum((v*v.T for v in m),sp.zeros(3))
V_z=sp.trace((Z-(4-A)*sp.eye(2)/2)**2)
V_m=A*A-sp.trace(M*M)
vsum=sum(m,sp.zeros(3,1)); s=vsum.dot(vsum)
R=sp.Integer(0); delta=sp.Integer(0)
for i,j in combinations(range(4),2):
    c=m[i].dot(m[j]); d=sp.Abs(z[i].dot(z[j]))
    assert c+d<=Q(1,2)
    R+=(Q(1,2)-c)**2-d**2
    delta+=max(sp.Integer(0),d-Q(1,2))
assert sp.simplify(A*A+6*A-2-2*(V_z+V_m+s)-4*R)==0
assert (V_z,V_m,s,R)==(Q(49,450),0,0,Q(167,300))
assert delta==Q(1,3)<Q(1780062775,4032758016)
assert A==Q(2,3)<Q(383,504)
assert sp.simplify((sp.sqrt(11)-3)**2+6*(sp.sqrt(11)-3)-2)==0
print("PASS exact identity, endpoint constraints, defect and midpoint caps")
print("A_C=",A,"delta=",delta,"V_z=",V_z,"R=",R)
print("strict coplanar lower bound sqrt(11)-3; see analytic proof")
